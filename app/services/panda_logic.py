import pandas as pd
from app.schemas.ProfileSchema import ProfileSchema 
from decimal import Decimal

def data_analize_mean(profile: list[ProfileSchema], column: str, value: Decimal):
    
    all_items = []
    
    for profile in profile:
        items_data = [item.model_dump() for item in profile.items]
        all_items.extend(items_data)
        
    df = pd.DataFrame(all_items)
    
    if df.empty:
        return {}
    
    resume = df.groupby(column)[value].mean().to_dict()
    
    return resume
