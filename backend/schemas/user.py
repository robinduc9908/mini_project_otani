from .base_schemas import SchemasBase


class User(SchemasBase):
    name: str
    email: str
    password: str
    permission: str
    phone: str
    address: str



