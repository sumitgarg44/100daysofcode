"""Database Models"""

from marshmallow import Schema, fields


class BlogSchema(Schema):
    """Blogs Schema"""

    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    subtitle = fields.Str(required=True)
    date = fields.Str(required=True)
    body = fields.Str(required=True)
    author = fields.Str(required=True)
    img_url = fields.Str(required=True)
