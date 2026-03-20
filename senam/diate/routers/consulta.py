from fastapi import APIRouter, Depends, HTTPException, Form
from sqlalchemy.orm import Session
from sqlalchemy import text
from database import get_db
from auth import verificar_token

router = APIRouter()


@router.post("/parametros_resultados_fecha_cinam")
def consultar_vista(
    fecha_inicio: str = Form(...),
    fecha_fin: str = Form(...),
    db: Session = Depends(get_db),
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        print(f"Usuario autenticado: {user}")

        query = text("""
            SELECT *
            FROM view_resultados_materializados
            WHERE res_accion like 'ATAQUE CON UAS (SISTEMA AÉREO NO TRIPULADO) ADECUADO CON EXPLOSIVOS' and hop_fecha_hecho BETWEEN :fecha_inicio AND :fecha_fin
        """)

        result = db.execute(query, {
            "fecha_inicio": fecha_inicio,
            "fecha_fin": fecha_fin
        })

        rows = result.fetchall()

        data = [dict(row._mapping) for row in rows]

        return {
            "status": "ok",
            "usuario": user,
            "total": len(data),
            "data": data
        }

    except Exception as e:
        print(f"❌ Error: {e}")
        raise HTTPException(status_code=500, detail="Error en la consulta")