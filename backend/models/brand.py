from .base_models import BaseModel_db
from peewee import CharField,IntegerField


class Brand(BaseModel_db):
    type = CharField()


    class Meta:
        db_table = 'brands'

    @classmethod
    def get_list(cls):
        query = cls.select().dicts()
        return list(query)


