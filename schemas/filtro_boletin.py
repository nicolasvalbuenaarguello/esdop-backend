from pydantic import BaseModel, ConfigDict
from typing import Optional

class FiltroBoletin(BaseModel):
    agr_div: Optional[str] = None
    Div_FT: Optional[str] = None
    br: Optional[str] = None
    ut: Optional[str] = None
    filtro: Optional[str] = None
    dpto: Optional[str] = None
    mpio: Optional[str] = None
    enemigo: Optional[str] = None
    op_mayores: Optional[str] = None
    apoyo_unidad: Optional[str] = None
    afectaciones: Optional[str] = None
    tipo_titulo: Optional[str] = None
    permiso: Optional[str] = None
    unidad: Optional[str] = None
    fullname: Optional[str] = None
    ruta: Optional[str] = None
    spoa: Optional[str] = None
    delco_cap: Optional[str] = None
    estrategia: Optional[str] = None
    gaulas: Optional[str] = None
    coordinadas: Optional[str] = None
    conjuntas: Optional[str] = None
    tipo_afectaciones: Optional[str] = None
    tipo_operacion: Optional[str] = None
    cdte: Optional[str] = None
    hechos: Optional[str] = None
    acam_enemigo: Optional[str] = None
    acam_estructura: Optional[str] = None
    ene_estructura: Optional[str] = None
    logo: Optional[str] = None
    usuario: Optional[str] = None
    nivel: Optional[str] = None

    model_config = ConfigDict(extra="allow")  # ✅ Ignora los campos extra que no están definidos
