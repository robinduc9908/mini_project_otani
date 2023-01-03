from .base_schemas import SchemasBase


class addproduct(SchemasBase):
    product_code: str
    name: str
    img: str
    brand: str
    category: str
    price: str
    detail: str
    is_hidden: int
