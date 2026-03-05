from marshmallow import Schema, fields


class LoanSchema(Schema):

    email = fields.Email(

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
