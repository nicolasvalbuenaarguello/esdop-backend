# routes/subregiones.py
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import text
from typing import List
from pydantic import BaseModel
from models.database import get_db
from models.models import SubregionIn, Subregion


router = APIRouter()



@router.post("/api/subregiones/crear_subregion")
def crear_o_actualizar_subregion(subregion: SubregionIn, db: Session = Depends(get_db)):
    # Verificar si ya existe la subregión
    result = db.execute(
        text("SELECT id FROM subregion WHERE nombre = :nombre"),
        {"nombre": subregion.nombre}
    )
    subregion_id = result.scalar()

    if subregion_id:
        # Subregión existe: eliminar municipios y departamentos asociados
        db.execute(
            text("""
                DELETE FROM subregion_municipio
                WHERE subregion_departamento_id IN (
                    SELECT id FROM subregion_departamento WHERE subregion_id = :subregion_id
                )
            """),
            {"subregion_id": subregion_id}
        )
        db.execute(
            text("DELETE FROM subregion_departamento WHERE subregion_id = :subregion_id"),
            {"subregion_id": subregion_id}
        )
    else:
        # Subregión no existe: crearla
        result = db.execute(
            text("INSERT INTO subregion (nombre) VALUES (:nombre) RETURNING id"),
            {"nombre": subregion.nombre}
        )
        subregion_id = result.scalar()

    # Insertar los departamentos y municipios nuevos
    for depto in subregion.departamentos:
        result = db.execute(
            text("INSERT INTO subregion_departamento (subregion_id, nombre) VALUES (:subregion_id, :nombre) RETURNING id"),
            {"subregion_id": subregion_id, "nombre": depto.nombre}
        )
        departamento_id = result.scalar()

        for municipio in depto.municipios:
            db.execute(
                text("INSERT INTO subregion_municipio (subregion_departamento_id, nombre) VALUES (:depto_id, :nombre)"),
                {"depto_id": departamento_id, "nombre": municipio}
            )

    db.commit()

    return {"mensaje": "Subregión actualizada correctamente" if subregion_id else "Subregión creada correctamente"}



@router.get("/api/subregiones")
def obtener_subregiones(db: Session = Depends(get_db)):
    subregiones_raw = db.execute(text("""
        SELECT sr.id AS subregion_id, sr.nombre AS subregion,
               d.id AS depto_id, d.nombre AS departamento,
               m.nombre AS municipio
        FROM subregion sr
        JOIN subregion_departamento d ON d.subregion_id = sr.id
        JOIN subregion_municipio m ON m.subregion_departamento_id = d.id
        ORDER BY sr.id, d.id, m.id
    """)).fetchall()

    resultado = {}
    for row in subregiones_raw:
        sr = resultado.setdefault(row.subregion_id, {
            "id": row.subregion_id,
            "nombre": row.subregion,
            "departamentos": {}
        })
        deptos = sr["departamentos"]
        muni = deptos.setdefault(row.departamento, [])
        muni.append(row.municipio)

    # Convertir a lista para el frontend
    return [
        {
            "id": datos["id"],
            "nombre": datos["nombre"],
            "departamentos": [
                {"nombre": dpto, "municipios": municipios}
                for dpto, municipios in datos["departamentos"].items()
            ]
        }
        for datos in resultado.values()
    ]

# ----------------------
# Endpoint auxiliar: departamentos con municipios
# ----------------------
@router.get("/api/subregiones/departamentos_con_municipios")
def obtener_departamentos_y_municipios(db: Session = Depends(get_db)):
    query = """
        SELECT DISTINCT dpto, mpio
        FROM view_hechos_materializados
        ORDER BY dpto, mpio
    """
    resultados = db.execute(text(query)).fetchall()

    departamentos_dict = {}
    for dpto, mpio in resultados:
        if dpto not in departamentos_dict:
            departamentos_dict[dpto] = []
        departamentos_dict[dpto].append(mpio)

    return [{"nombre": dpto, "municipios": mpios} for dpto, mpios in departamentos_dict.items()]



@router.delete("/api/subregiones/eliminar/{subregion_id}")
def eliminar_subregion(subregion_id: int, db: Session = Depends(get_db)):
    subregion = db.query(Subregion).filter(Subregion.id == subregion_id).first()

    if not subregion:
        raise HTTPException(status_code=404, detail="Subregión no encontrada")

    # Los municipios y departamentos se eliminan automáticamente gracias al `cascade="all, delete"`
    db.delete(subregion)
    db.commit()
    return {"detail": "Subregión eliminada correctamente"}

