from app.schemas.ProfileSchema import ProfileSchema
from app.data.data import SEED_PROFILES

# Convertimos la lista de dicts en una lista de objetos ProfileSchema
profiles_ready = [ProfileSchema(**data) for data in SEED_PROFILES]