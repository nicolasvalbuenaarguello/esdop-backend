import json
import os
import shutil
from tipo_docker.k_c_boletin_mapa_div_balance.models.funtions.pdf.boletin_coe import comparativo_comparativo_mapa

def b_f_boletin_mapa_div_balance_token(datos, link, ruta, puerto):
    """Genera un boletín de mapa comparativo con filtros de datos y guarda los resultados."""

    # Preparar carpeta de resultados
    nombre_carpeta = f"resultados_mpa_eva_{puerto}/"
    dir_archivos = os.path.join(link, nombre_carpeta)
    os.makedirs(dir_archivos, exist_ok=True)

    for archivo in os.listdir(dir_archivos):
        try:
            archivo_path = os.path.join(dir_archivos, archivo)
            if os.path.isdir(archivo_path):
                shutil.rmtree(archivo_path)
            else:
                os.remove(archivo_path)
        except Exception as e:
            print(f"⚠️ No se pudo eliminar: {archivo_path} - {e}")

    # Extraer datos del diccionario
    subregion = json.loads(datos['subregion'])
    campos_obligatorios = [
        'permiso', 'unidad', 'fullname',
        'fecha_primer_lapso_inicial', 'fecha_ultimo_lapso_inicial',
        'fecha_primer_lapso_final', 'fecha_ultimo_lapso_final',
        'agr_div', 'Div_FT', 'br', 'ut', 'dpto', 'mpio', 'filtro',
        'enemigo', 'op_mayores', 'apoyo_unidad', 'afectaciones', 'tipo_titulo',
        'documento', 'spoa', 'delco_cap', 'estrategia', 'gaulas',
        'coordinadas', 'conjuntas', 'tipo_afectaciones', 'tipo_operacion',
        'cdte', 'hechos', 'acam_enemigo', 'acam_estructura', 'ene_estructura'
    ]

    try:
        extraidos = [datos[campo] for campo in campos_obligatorios]
    except KeyError as e:
        raise ValueError(f"Falta el campo obligatorio en datos: {e}")

    # Separar fechas y filtros
    (
        permiso, unidad, fullname,
        fecha_primer_lapso_inicial, fecha_ultimo_lapso_inicial,
        fecha_primer_lapso_final, fecha_ultimo_lapso_final,
        agr_div, Div_FT, br, ut, dpto, mpio, filtro,
        enemigo, op_mayores, apoyo_unidad, afectaciones, tipo_titulo,
        documento, spoa, delco_cap, estrategia, gaulas,
        coordinadas, conjuntas, tipo_afectaciones, tipo_operacion,
        cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion
    ) = extraidos

    filtros = (
        agr_div, Div_FT, br, ut, filtro, dpto, mpio,
        enemigo, op_mayores, apoyo_unidad, afectaciones, tipo_titulo,
        permiso, unidad, fullname, ruta, spoa, delco_cap,
        estrategia, gaulas, coordinadas, conjuntas,
        tipo_afectaciones, tipo_operacion, cdte, hechos,
        acam_enemigo, acam_estructura, ene_estructura, subregion
    )

    # Llamar la generación del comparativo
    direccion = comparativo_comparativo_mapa(
        fecha_primer_lapso_inicial, fecha_ultimo_lapso_inicial,
        fecha_primer_lapso_final, fecha_ultimo_lapso_final,
        filtros, dir_archivos, nombre_carpeta
    )

    return {
        "direccion": direccion[0],
        "nombre": direccion[1]
    }