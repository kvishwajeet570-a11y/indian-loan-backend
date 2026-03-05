from marshmallow import Schema, fields, validate


class RechargeSchema(Schema):

    email = fields.Email(

        required=True

    )

    number = fields.Str(

        required=True,

        validate=validate.Length(equal=10)

    )

    operator = fields.Str(

        required=True

    )

    amount = fields.Float(

        required=True

    )

    status = fields.Str(

        dump_only=True

    )

    date = fields.DateTime(

        dump_only=True

    )
