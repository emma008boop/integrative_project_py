from enum import Enum

class ItemStateEnum(str, Enum):
    ABANDONED: "abandoned"
    BOUGHT: "bought"
    
class ItemCategoryEnum(str, Enum):
    SUSCRIPTIONS: "suscriptions"
    CLOTHES: "clothes"
    SNACKS: "snacks"