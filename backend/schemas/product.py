from .base_schemas import SchemasBase


class Product(SchemasBase):
    product_code: str
    name: str
    img: str
    brand_id: str
    category_id: str
    price: str
    detail: str
    is_hidden: int


