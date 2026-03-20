import os
import shutil
from tipo_docker.s_c_resultados_mapa.models.funtions.pdf.boletin_coe import *

def b_e_resultados_mapa_token(datos, link, ruta, puerto):
    # Obtener puerto desde parámetro o entorno
    puerto_str = str(puerto or os.getenv("PUERTO", "0"))
    nombre_carpeta = f"resultados_mapa_{puerto_str}/"
    dir_archivos = os.path.join(link, nombre_carpeta)

    # Crear o limpiar carpeta destino
    os.makedirs(dir_archivos, exist_ok=True)
    for archivo in os.listdir(dir_archivos):
        archivo_path = os.path.join(dir_archivos, archivo)
        try:
            if os.path.isdir(archivo_path):
                shutil.rmtree(archivo_path)
            else:
                os.remove(archivo_path)
        except Exception as e:
            print(f"⚠️ Error al eliminar '{archivo_path}': {e}")

    # Variables clave desde el dict `datos` usando get con fallback
    fechas = (
        datos.get('fecha_primer_lapso_inicial'),
        datos.get('fecha_ultimo_lapso_inicial'),
    )
    subregion = json.loads(datos['subregion'])
    filtros = (
        datos.get('agr_div'),
        datos.get('Div_FT'),
        datos.get('br'),
        datos.get('ut'),
        datos.get('filtro'),
        datos.get('dpto'),
        datos.get('mpio'),
        datos.get('enemigo'),
        datos.get('op_mayores'),
        datos.get('apoyo_unidad'),
        datos.get('afectaciones'),
        datos.get('tipo_titulo'),
        datos.get('permiso'),
        datos.get('unidad'),
        datos.get('fullname'),
        ruta,
        datos.get('spoa'),
        datos.get('delco_cap'),
        datos.get('estrategia'),
        datos.get('gaulas'),
        datos.get('coordinadas'),
        datos.get('conjuntas'),
        datos.get('tipo_afectaciones'),
        datos.get('tipo_operacion'),
        datos.get('cdte'),
        datos.get('hechos'),
        datos.get('acam_enemigo'),
        datos.get('acam_estructura'),
        datos.get('ene_estructura'),
        subregion
    )

    # Ejecutar la generación del archivo
    try:
        direccion = comparativo_comparativo_mapa(
            fechas[0], fechas[1], filtros, dir_archivos, nombre_carpeta
        )
        return {"direccion": direccion[0], "nombre": direccion[1]}
    except Exception as e:
        print(f"❌ Error generando el comparativo mapa: {e}")
        return {"error": str(e)}
