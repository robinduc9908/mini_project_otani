from .base_models import BaseModel_db
from peewee import CharField, IntegerField


class Cart_item(BaseModel_db):
    cart_id = IntegerField()
    product_id = IntegerField()
    quantily = IntegerField()

    class Meta:
        db_table = 'cart_items'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)
