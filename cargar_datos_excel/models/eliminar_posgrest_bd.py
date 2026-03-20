import os
import psycopg2
import openpyxl
from dotenv import load_dotenv
from models.conversor import conversion

load_dotenv()

def connect():
    return psycopg2.connect(
        dbname="dirop",
        user="postgres",
        password="NICval10**"
    )
def eliminar_bd_posgrest(fecha_inicial, fecha_final):

    global dato
    dato=0
    conn = connect()
    cursor = conn.cursor()
        
    dato = "delete from hechos where fecha_hecho >= '{}' and fecha_hecho <= '{}'".format(fecha_inicial, fecha_final)
    cursor.execute(dato)
    conn.commit()
        
    dato = "delete from resultados where hop_fecha_hecho >= '{}' and hop_fecha_hecho <= '{}'".format(fecha_inicial, fecha_final)
    cursor.execute(dato)
    conn.commit()
        
    dato = "delete from erradicacion where unidad >= '{}' and unidad <= '{}'".format(fecha_inicial, fecha_final)
    cursor.execute(dato)
    conn.commit()

    conn.close()

    
async def actualizar_datos():
    print("🔄 Actualizando vistas materializadas...")
    conn = connect()
    cursor = conn.cursor()
    try:
        vistas = [
            "view_hechos_materializados",
            "view_erradicacion_materializados",
            "view_resultados_materializados"
        ]
        for vista in vistas:
            cursor.execute(f"REFRESH MATERIALIZED VIEW {vista}")
            print(f"✅ Vista actualizada: {vista}")
        conn.commit()
    except Exception as e:
        conn.rollback()
        print(f"❌ Error actualizando vistas: {e}")
    finally:
        cursor.close()
        conn.close()

async def cargar_resultados():
    ruta_base = os.getenv('DIRECION')
    if not ruta_base:
        raise ValueError("❌ La variable de entorno 'DIRECION' no está definida.")

    carpeta_documentos = os.path.join(ruta_base, 'cargar_datos_excel', 'documentos')

    ARCHIVOS_EXCEL = {
        "ERRADICACION APLICATIVO.xlsx": "ERRADICACION",
        "HECHOS ARCHIVO PLANO.xlsx": "HECHOS",
        "RESULTADOS APLICATIVO.xlsx": "RESULTADOS"
    }

    for nombre_archivo, _ in ARCHIVOS_EXCEL.items():
        ruta_archivo = os.path.join(carpeta_documentos, nombre_archivo)
        if os.path.exists(ruta_archivo):
            try:
                wb = openpyxl.load_workbook(ruta_archivo, read_only=True)
                hoja = wb.sheetnames[0]
                wb.close()  # ✅ Cierra el workbook inmediatamente después de obtener la hoja

                print(f"📄 Cargando archivo: {nombre_archivo} (Hoja: {hoja})")
                conv = conversion()
                conv.leer_excel(ruta_archivo)
                conv.convertir(hoja)
            except Exception as e:
                print(f"❌ Error cargando {nombre_archivo}: {e}")
        else:
            print(f"⚠️ Archivo no encontrado: {ruta_archivo}")

