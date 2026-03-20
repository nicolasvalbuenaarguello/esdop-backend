from datetime import datetime
# coding: utf-8
from __init__ import *
from models.conexion_pos import *
from werkzeug.security import generate_password_hash
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=PLAZOS_SEGUNDO_CDTE \
        user=postgres \
        password=NICval10**")
    return conn

def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor

def insertar_subcarpeta(folder_id: int, name: str, active: bool):
    conn = psycopg2.connect(
        dbname="PLAZOS_SEGUNDO_CDTE",
        user="postgres",
        password="NICval10**"
    )
    cursor = conn.cursor()

    # 1. Verificar si ya existe
    cursor.execute("""
        SELECT id, active FROM subfolders 
        WHERE folder_id = %s AND name = %s
    """, (folder_id, name))
    result = cursor.fetchone()

    if result:
        subfolder_id, was_active = result

        if active and not was_active:
            # Activar esta → desactivar las demás
            cursor.execute("""
                UPDATE subfolders SET active = FALSE WHERE folder_id = %s
            """, (folder_id,))
            cursor.execute("""
                UPDATE subfolders SET active = TRUE WHERE id = %s
            """, (subfolder_id,))
        elif not active and was_active:
            # Se va a desactivar esta → revisar si es la única activa
            cursor.execute("""
                SELECT COUNT(*) FROM subfolders 
                WHERE folder_id = %s AND active = TRUE AND id != %s
            """, (folder_id, subfolder_id))
            other_active = cursor.fetchone()[0]

            if other_active == 0:
                # No se puede dejar sin ninguna activa
                active = True  # fuerza mantenerla activa

            cursor.execute("""
                UPDATE subfolders SET active = %s WHERE id = %s
            """, (active, subfolder_id))

        operation = "updated"

    else:
        # Si se va a insertar y está activa, desactivar otras
        if active:
            cursor.execute("""
                UPDATE subfolders SET active = FALSE WHERE folder_id = %s
            """, (folder_id,))

        cursor.execute("""
            INSERT INTO subfolders (folder_id, name, active, created_at)
            VALUES (%s, %s, %s, NOW())
            RETURNING id
        """, (folder_id, name, active))
        subfolder_id = cursor.fetchone()[0]
        operation = "created"

    conn.commit()
    cursor.close()
    conn.close()

    return {
        "id": subfolder_id,
        "name": name,
        "folder_id": folder_id,
        "active": active,
        "operation": operation
    }
from pathlib import Path

def crear_directorio(nombre: str, base_path: str = "./carpetas"):
    """
    Crea un directorio si no existe ya.
    
    Args:
        nombre (str): Nombre de la carpeta a crear.
        base_path (str): Ruta base donde se crearán las carpetas.
    
    Returns:
        dict: Información del estado de la operación.
    """
    # Ruta completa: base_path/nombre
    ruta = Path(base_path) / nombre

    try:
        ruta.mkdir(parents=True, exist_ok=False)
        return {
            "success": True,
            "message": f"Carpeta '{nombre}' creada en {ruta.resolve()}",
            "path": str(ruta.resolve())
        }
    except FileExistsError:
        return {
            "success": False,
            "message": f"La carpeta '{nombre}' ya existe.",
            "path": str(ruta.resolve())
        }
    except Exception as e:
        return {
            "success": False,
            "message": f"Error al crear la carpeta: {str(e)}"
        }


def guardar_evento(datos):
    # excel_amenaza
    folder_id =  datos["folder_id"]
    name =  datos["name"]
    active  = datos["active"]
  
    subfolder_id = insertar_subcarpeta(folder_id, name, active)
    
    conn = connect()
    cursor = conn.cursor()
    query="SELECT name FROM folders where id = {}".format(folder_id)
    cursor.execute(query)
    nombre_carpeta = cursor.fetchall()

    conn.close()
    cursor.close
    
    DIRECION = os.getenv('DIRECION')
    base_path ='C:/Users/nicolas.valbuena/Documents/documentos_serve_jemop/plazos_sejec/{}'.format(nombre_carpeta[0][0])
    #base_path
    crear_directorio(name, base_path)
    return [subfolder_id]


def select_ordenes_sejec_folders():
    conn = connect()
    cursor = conn.cursor()

    query = """
    SELECT f.id AS folder_id, f.name AS folder_name, f.created_at AS folder_created,
           s.id AS subfolder_id, s.name AS subfolder_name, s.active, s.created_at AS subfolder_created
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query)
    rows = cursor.fetchall()

    conn.close()
    cursor.close()

    folders_dict = {}

    for row in rows:
        folder_id = row[0]
        folder_name = row[1]
        folder_created = row[2]
        subfolder_id = row[3]
        subfolder_name = row[4]
        active = row[5]
        subfolder_created = row[6]

        if folder_id not in folders_dict:
            folders_dict[folder_id] = {
                "id": folder_id,
                "name": folder_name,
                "created_at": folder_created.isoformat() if folder_created else None,
                "subfolders": [],
                "last_created_name": None  # 🔹 Inicializar para cada carpeta
            }

        if subfolder_id:
            folders_dict[folder_id]["subfolders"].append({
                "id": subfolder_id,
                "name": subfolder_name,
                "active": active,
                "created_at": subfolder_created.isoformat() if subfolder_created else None
            })

            # Solo la primera subcarpeta será la más reciente (por el ORDER BY DESC)
            if folders_dict[folder_id]["last_created_name"] is None:
                folders_dict[folder_id]["last_created_name"] = subfolder_name

    return {
        "folders": list(folders_dict.values())
    }
