from marshmallow import Schema, fields, validate


class UserSchema(Schema):

    name = fields.Str(

        required=True,

        validate=validate.Length(min=3, max=50)

    )

    email = fields.Email(

        required=True

    )

    password = fields.Str(

        required=True,

        validate=validate.Length(min=6)

    )

    mobile = fields.Str(

        required=True,

        validate=validate.Length(equal=10)

    )

    role = fields.Str(

        missing="user"

    )

    date = fields.DateTime(
        dump_only=True
    )
