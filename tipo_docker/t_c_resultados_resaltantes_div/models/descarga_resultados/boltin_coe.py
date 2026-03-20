import json
import os
import shutil
from tipo_docker.t_c_resultados_resaltantes_div.models.funtions.pdf.boletin_coe import *

def b_d_resultados_resaltantes_div_token(datos, link, ruta, puerto):
    # Validar y convertir puerto a string
    puerto_str = str(puerto or os.getenv("PUERTO", "0"))
    nombre_carpeta = f"resultados_resaltantes_div_{puerto_str}/"
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

    # Extraer variables del diccionario con .get para mayor seguridad
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

    fecha_inicio = datos.get('fecha_primer_lapso_inicial')
    fecha_final = datos.get('fecha_ultimo_lapso_inicial')

    # Llamar función principal de resultados
    try:
        direccion = resultados_resaltantes_div(
            fecha_inicio,
            fecha_final,
            filtros,
            dir_archivos,
            nombre_carpeta
        )
    except Exception as e:
        print(f"❌ Error generando resultados: {e}")
        return {"error": str(e)}

    return {
        "direccion": direccion[0],
        "nombre": direccion[1]
    }
