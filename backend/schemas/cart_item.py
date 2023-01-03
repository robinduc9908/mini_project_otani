from .base_schemas import SchemasBase


class Cart_item(SchemasBase):
    cart_id: int
    product_id : int
    quantily : int
