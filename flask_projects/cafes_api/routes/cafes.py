"""Cafes Api routes"""

import logging
import os
import secrets

from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from sqlalchemy import func
from sqlalchemy.exc import SQLAlchemyError

from models import Cafe, db
from schemas import CafeSchema

cafes_bp = Blueprint("cafes_bp", __name__, url_prefix="/api/v1/cafes")

cafe_schema = CafeSchema()
cafes_schema = CafeSchema(many=True)
APIKey = os.environ.get("API_TOKEN", None)


# Jsonify return structure
def return_data(
    success, error=None, result=None
):  # pylint: disable=too-few-public-methods
    """Return jsonify structure response"""

    return jsonify(response={"success": success, "error": error, "result": result})


# GET /api/v1/cafes/random
@cafes_bp.route("/random", methods=["GET"])
def get_random_cafe():
    """Get random cafe from DB"""

    try:
        # pylint: disable=not-callable
        count = db.session.scalar(db.select(func.count()).select_from(Cafe))
        if count == 0:
            return return_data(success=False, error="No cafes found"), 404
        offset = secrets.randbelow(count)
        random_cafe = db.session.scalar(db.select(Cafe).offset(offset).limit(1))
    except SQLAlchemyError as e:
        logging.error("Failed to retrieve random cafe", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    return return_data(success=True, result=CafeSchema().dump(random_cafe))


# GET /api/v1/cafes/all?page=1&per_page=20
@cafes_bp.route("/all", methods=["GET"])
def get_all_cafes():
    """Get all cafes from DB with pagination"""

    # Read pagination query params, set defaults
    page = request.args.get("page", 1, type=int)
    per_page = request.args.get("per_page", 20, type=int)

    try:
        # pylint: disable=not-callable
        total = db.session.scalar(db.select(func.count()).select_from(Cafe))
        offset = (page - 1) * per_page
        cafes = db.session.scalars(db.select(Cafe).offset(offset).limit(per_page)).all()
    except SQLAlchemyError as e:
        logging.error("Failed to retrieve all cafes", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    total_pages = (total + per_page - 1) // per_page
    return return_data(
        success=True,
        result={
            "page": page,
            "per_page": per_page,
            "total": total,
            "total_pages": total_pages,
            "cafes": CafeSchema(many=True).dump(cafes),
        },
    )


# GET /api/v1/cafes/search?loc=Paris
@cafes_bp.route("/search", methods=["GET"])
def search_by_location():
    """Search cafe by location"""

    query_loc = request.args.get("loc")

    if not query_loc:
        return return_data(success=False, error="Missing query parameter: loc"), 400

    try:
        cafes_at_loc = Cafe.query.filter(Cafe.location.ilike(query_loc)).all()
    except SQLAlchemyError as e:
        logging.error("Failed to search cafe by location", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    if cafes_at_loc:
        return return_data(
            success=True,
            result=CafeSchema(many=True).dump(cafes_at_loc),
        )

    logging.info("No cafe found at location: %s", query_loc)
    return return_data(
        success=True,
        result=["Sorry, we don't have a cafe at that location"],
    )


# POST /api/v1/cafes/add
@cafes_bp.route("/add", methods=["POST"])
def add_cafe():
    """Add a new cafe"""

    try:
        data = CafeSchema().load(request.form)
    except ValidationError as e:
        return jsonify(success=False, error=e.messages), 400

    new_cafe = Cafe(**data)

    try:
        db.session.add(new_cafe)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error("Failed to add cafe into database", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    logging.info("Successfully added new cafe: %s", data)
    return (
        return_data(success=True, result="Successful added the new cafe"),
        201,
    )


# PATCH /api/v1/cafes/update-price/<int:cafe_id>
@cafes_bp.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_coffe_price(cafe_id):
    """Patch coffee price of given cafe id"""

    new_price = request.args.get("new_price")
    if not new_price:
        return (
            return_data(success=False, error="Missing required field: new_price"),
            400,
        )

    cafe = db.session.get(Cafe, cafe_id)
    if not cafe:
        logging.info("Cafe not found with id: %d", cafe_id)
        return (
            return_data(
                success=False,
                error="Sorry a cafe with that id was not found",
            ),
            404,
        )

    old_price = cafe.coffee_price

    try:
        cafe.coffee_price = new_price
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error("Failed to update coffee price", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    logging.info(
        "Updated coffe price from %s to %s for cafe %s with id %d",
        old_price,
        new_price,
        cafe.name,
        cafe_id,
    )
    return return_data(success=True, result="Successfuly updated the price")


# DELETE /api/v1/cafes/report-closed/<int:cafe_id>
@cafes_bp.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def report_closed_cafe(cafe_id):
    """Delete closed cafe from database"""

    key = request.headers.get("x-api-key")
    if not key:
        return (
            return_data(success=False, error="Missing required header: x-api-key"),
            400,
        )

    if key != APIKey:
        logging.warning("Incorrect API key supplied while reporting the closed cafe")
        return (
            return_data(
                success=False,
                error="Forbidden, Make sure you have the correct api key",
            ),
            403,
        )

    cafe = db.session.get(Cafe, cafe_id)
    if cafe is None:
        logging.info("Closed reported cafe not found with id: %d", cafe_id)
        return (
            return_data(
                success=False,
                error="Sorry a cafe with that id was not found",
            ),
            404,
        )

    try:
        db.session.delete(cafe)
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        logging.error("Failed to delete cafe from database", exc_info=e)
        return return_data(success=False, error=str(e)), 500

    logging.info("Cafe has been deleted from database: %s", CafeSchema().dump(cafe))
    return return_data(
        success=True,
        result="Closed cafe has been removed from the database",
    )
