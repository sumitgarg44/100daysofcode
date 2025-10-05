"""Cafe Schema"""

from marshmallow import Schema, fields


class CafeSchema(Schema):  # pylint: disable=too-few-public-methods
    """Cafe Schema"""

    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    map_url = fields.Str(required=True)
    img_url = fields.Str(required=True)
    location = fields.Str(required=True)
    seats = fields.Str(required=True)
    has_toilet = fields.Bool(required=True)
    has_wifi = fields.Bool(required=True)
    has_sockets = fields.Bool(required=True)
    can_take_calls = fields.Bool(required=True)
    coffee_price = fields.Str(required=False)
