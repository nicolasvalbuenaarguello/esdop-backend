import json
import os
import shutil
from tipo_docker.a_a_boletin_estadistica_power_point.models.funtions.pdf.boletin_coe import estadistica_resaltantes

def boletin_estadistica_resultados(datos, link, ruta, puerto):
    nombre_carpeta = f"ayuda_powerpoint{puerto}/"
    dir_archivos = os.path.join(link, nombre_carpeta)

    # Crear o limpiar la carpeta
    os.makedirs(dir_archivos, exist_ok=True)
    for archivo in os.listdir(dir_archivos):
        archivo_path = os.path.join(dir_archivos, archivo)
        try:
            if os.path.isdir(archivo_path):
                shutil.rmtree(archivo_path)
            else:
                os.remove(archivo_path)
        except Exception as e:
            print(f"⚠️ No se pudo eliminar: {archivo_path} - {e}")

    try:
        # Obtener todos los campos del formulario
        permiso = datos['permiso']
        unidad = datos['unidad']
        fullname = datos['fullname']
        fecha_primer_lapso_inicial = datos['fecha_primer_lapso_inicial']
        fecha_ultimo_lapso_inicial = datos['fecha_ultimo_lapso_inicial']
        fecha_primer_lapso_final = datos['fecha_primer_lapso_final']
        fecha_ultimo_lapso_final = datos['fecha_ultimo_lapso_final']
        agr_div = datos['agr_div']
        Div_FT = datos['Div_FT']
        br = datos['br']
        ut = datos['ut']
        dpto = datos['dpto']
        mpio = datos['mpio']
        filtro = datos['filtro']
        enemigo = datos['enemigo']
        op_mayores = datos['op_mayores']
        apoyo_unidad = datos['apoyo_unidad']
        afectaciones = datos['afectaciones']
        tipo_titulo = datos['tipo_titulo']
        documento = datos['documento']
        spoa = datos['spoa']
        delco_cap = datos['delco_cap']
        estrategia = datos['estrategia']
        gaulas = datos['gaulas']
        coordinadas = datos['coordinadas']
        conjuntas = datos['conjuntas']
        tipo_afectaciones = datos['tipo_afectaciones']
        tipo_operacion = datos['tipo_operacion']
        cdte = datos['cdte']
        hechos = datos['hechos']
        acam_enemigo = datos['acam_enemigo']
        acam_estructura = datos['acam_estructura']
        ene_estructura = datos['ene_estructura']
        subregion = json.loads(datos['subregion'])

        # Agrupar filtros
        filtros = (
            agr_div, Div_FT, br, ut, filtro, dpto, mpio,
            enemigo, op_mayores, apoyo_unidad, afectaciones,
            tipo_titulo, permiso, unidad, fullname, ruta,
            spoa, delco_cap, estrategia, gaulas, coordinadas,
            conjuntas, tipo_afectaciones, tipo_operacion,
            cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion
        )

        # Llamada principal
        direccion = estadistica_resaltantes(
            fecha_primer_lapso_inicial,
            fecha_ultimo_lapso_inicial,
            filtros,
            dir_archivos,
            nombre_carpeta
        )

        return {
            "direccion": direccion[0],
            "nombre": direccion[1]
        }

    except KeyError as e:
        print(f"❌ Campo faltante: {e}")
        raise ValueError(f"Campo requerido faltante: {e}")
    except Exception as e:
        print(f"❌ Error general en boletin_estadistica_resultados: {e}")
        raise RuntimeError("Error interno en la generación del boletín")
