from km_api_app.serializer.vernacular_entity import finiteSetEntity, numericEntity
from marshmallow import Schema, fields, post_load, INCLUDE

class finiteSchema(Schema):
    values = fields.List(fields.Dict(), required = True)
    invalid_trigger = fields.Str(required = True)
    key = fields.Str(required = True)
    support_multiple = fields.Bool(missing = True)
    pick_first = fields.Bool(missing = False)
    supported_values = fields.List(fields.Str(), required = True)

    @post_load()
    def finiteObject(self, data, **kwargs):
        return finiteSetEntity(**data)

class numericSchema(Schema):
    values = fields.List(fields.Dict(), required = True)
    invalid_trigger = fields.Str(required = True)
    key = fields.Str(required = True)
    support_multiple = fields.Bool(missing = True)
    pick_first = fields.Bool(missing = False)
    constraint = fields.Str(missing = None)
    var_name = fields.Str(required = True)

    @post_load
    def numericObject(self, data, **kwargs):
        return numericEntity(**data)

    

        