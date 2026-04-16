from fastapi import APIRouter
from typing import List
from schemas.ProfileSchema import ProfileSchema
from services.panda_logic import data_analize_mean
from data.data import SEED_PROFILES

router = APIRouter()

@router.get("/test-analysis")
async def test_analysis():
    # 1. Transformamos los datos crudos a objetos validados por Pydantic
    profiles = [ProfileSchema(**p) for p in SEED_PROFILES]
    
    # 2. Ejecutamos tu lógica de Pandas
    # Usamos 'category' para agrupar y 'price' para el promedio
    result = data_analize_mean(profiles, column="category", value="price")
    
    return {
        "message": "Datos de prueba procesados",
        "analysis": result
    }

@router.get("/montly-resume")
async def resume_items(profile: List[ProfileSchema]):
    result = data_analize_mean(profile, column="category", value="price")
    return {"status": "success", "analysis": result}