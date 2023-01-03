from .base_models import BaseModel_db
from peewee import CharField,IntegerField


class Product(BaseModel_db):
    name = CharField()
    product_code = CharField()
    img = CharField()
    brand_id = IntegerField()
    category_id = IntegerField()
    price = CharField()
    detail = CharField()
    is_hidden = IntegerField()


    class Meta:
        db_table = 'products'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)