from .base_schemas import SchemasBase


class Login(SchemasBase):
    email: str
    password: str
