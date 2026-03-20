import json
import os
import shutil

from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.models.funtions.pdf.boletin_coe import comparativo_comparativo_mapa

def a_w_boletin_mapa_div_comparativo(datos: dict, link: str, ruta: str, puerto: str) -> dict:
    nombre_carpeta = f"consejos_seguridad_{puerto}/"
    dir_archivos = os.path.join(link, nombre_carpeta)

    # Crear directorio si no existe, o limpiar si existe
    os.makedirs(dir_archivos, exist_ok=True)

    for item in os.listdir(dir_archivos):
        item_path = os.path.join(dir_archivos, item)
        try:
            if os.path.isdir(item_path):
                shutil.rmtree(item_path)
            else:
                os.remove(item_path)
        except Exception as e:
            print(f"Error limpiando {item_path}: {e}")

    # Extraer datos con .get para evitar KeyError
    subregion = json.loads(datos['subregion'])
    filtros = (
        datos.get('agr_div'), datos.get('Div_FT'), datos.get('br'), datos.get('ut'),
        datos.get('filtro'), datos.get('dpto'), datos.get('mpio'), datos.get('enemigo'),
        datos.get('op_mayores'), datos.get('apoyo_unidad'), datos.get('afectaciones'), datos.get('tipo_titulo'),
        datos.get('permiso'), datos.get('unidad'), datos.get('fullname'), ruta,
        datos.get('spoa'), datos.get('delco_cap'), datos.get('estrategia'), datos.get('gaulas'),
        datos.get('coordinadas'), datos.get('conjuntas'), datos.get('tipo_afectaciones'),
        datos.get('tipo_operacion'), datos.get('cdte'), datos.get('hechos'),
        datos.get('acam_enemigo'), datos.get('acam_estructura'), datos.get('ene_estructura'), 
        subregion
    )

    direccion_archivo = comparativo_comparativo_mapa(
        datos.get('fecha_primer_lapso_inicial'),
        datos.get('fecha_ultimo_lapso_inicial'),
        datos.get('fecha_primer_lapso_final'),
        datos.get('fecha_ultimo_lapso_final'),
        filtros, dir_archivos, nombre_carpeta
    )

    return {
        "direccion": direccion_archivo[0],
        "nombre": direccion_archivo[1]
    }
