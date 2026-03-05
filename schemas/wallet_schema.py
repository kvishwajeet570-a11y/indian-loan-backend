from marshmallow import Schema, fields


class WalletSchema(Schema):

    email = fields.Email(

        required=True

    )

    balance = fields.Float(

        required=True

    )

    date = fields.DateTime(

        dump_only=True

    )
