from .base_models import BaseModel_db
from peewee import CharField, IntegerField


class User(BaseModel_db):
    name = CharField()
    email = CharField()
    password = CharField()
    permission = CharField()
    phone = CharField()
    address = CharField()


    class Meta:
        db_table = 'user'

    @classmethod
    # def get_list(cls):
    #     query = cls.select().order_by(score)
    #     return list(query)

    def get_user(data):
        query = User.select().where(User.email == data['email'] and User.password == data['password'])
        query = list(query)
        if len(query):
            return {"code": 200, "data": query}
        else:
            return {"code": 400, 'data': query}
