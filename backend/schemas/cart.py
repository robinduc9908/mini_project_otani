from .base_schemas import SchemasBase


class Cart(SchemasBase):
    product_id: int
    quantity: int
    size : str
    is_hidden : int

