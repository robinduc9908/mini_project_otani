from .base_models import BaseModel_db
from peewee import CharField, IntegerField
from models.product import Product



class Cart(BaseModel_db):
    product_id = IntegerField()
    quantity = IntegerField()
    size = CharField()
    is_hidden = IntegerField()

    class Meta:
        db_table = 'carts'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)
