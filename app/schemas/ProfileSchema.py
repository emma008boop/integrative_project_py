from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime
from enums import ItemCategoryEnum, ItemStateEnum

class ItemSchema(BaseModel):
    id: int
    created_at: datetime
    currency: str
    price: Decimal
    state: ItemStateEnum
    category: ItemCategoryEnum
    need_level: int
    
    class Config:
        from_attributes = True

class ProfileSchema(BaseModel):
    id: int 
    items: list[ItemSchema]
    
    class Config:
        from_attributes = True


