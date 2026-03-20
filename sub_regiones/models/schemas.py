### ✅ schemas.py

from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class DepartamentoSubIn(BaseModel):
    nombre: str
    municipios: List[str] = []

class SubregionIn(BaseModel):
    nombre: str
    departamentos: List[DepartamentoSubIn]

class SubregionUpdate(BaseModel):
    nombre: str

class SubregionOut(BaseModel):
    id: int
    nombre: str
    creado_en: datetime

    class Config:
        orm_mode = True
