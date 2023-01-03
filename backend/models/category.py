from .base_models import BaseModel_db
from peewee import CharField, IntegerField


class Category(BaseModel_db):
    type = CharField()

    class Meta:
        db_table = 'categories'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)
