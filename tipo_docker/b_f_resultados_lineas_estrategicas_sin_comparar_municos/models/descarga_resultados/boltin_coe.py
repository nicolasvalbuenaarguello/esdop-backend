import json
import os
import shutil
# from funtions.pdf.resultados.pdf import *

from tipo_docker.b_f_resultados_lineas_estrategicas_sin_comparar_municos.models.funtions.pdf.boletin_coe import *
#Funcion de resultados nueva ayuda

def b_c_resultados_resaltantes_token(datos, link, ruta, puerto):

    nombre_carpeta = f"resultados_resaltantes{puerto}/"
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
    #permisos

    permiso = datos['permiso']
    unidad =  datos['unidad']
    fullname = datos['fullname']

    #fechas
    fecha_primer_lapso_inicial = datos['fecha_primer_lapso_inicial']
    fecha_ultimo_lapso_inicial = datos['fecha_ultimo_lapso_inicial']
    fecha_primer_lapso_final = datos['fecha_primer_lapso_final']
    fecha_ultimo_lapso_final = datos['fecha_ultimo_lapso_final']

    #unidades
    agr_div = datos['agr_div']
    Div_FT = datos['Div_FT']
    br = datos['br']
    ut = datos['ut']
    #lugar 
    dpto = datos['dpto']
    mpio = datos['mpio']
    #tipo de filtro
    filtro = datos['filtro']

    #enemigo - op - mayor
    enemigo = datos['enemigo']
    op_mayores = datos['op_mayores']
    #apoyo unidad
    apoyo_unidad = datos['apoyo_unidad']
    #afectaciones y titulo
    afectaciones = datos['afectaciones']
    tipo_titulo = datos['tipo_titulo']
    direcion = []
    #documento
    documento = datos['documento']
    spoa =  datos['spoa']
    delco_cap =  datos['delco_cap']
    estrategia =  datos['estrategia']
    gaulas =  datos['gaulas']
    coordinadas =  datos['coordinadas']
    conjuntas =  datos['conjuntas']
    tipo_afectaciones =  datos['tipo_afectaciones']
     
    tipo_operacion =  datos['tipo_operacion']

    cdte =  datos['cdte']

    hechos =  datos['hechos']

    acam_enemigo =  datos['acam_enemigo']
    acam_estructura =  datos['acam_estructura']
    ene_estructura =  datos['ene_estructura']
    subregion = json.loads(datos['subregion'])
    unidades_asc =  datos['unidades_asc']

 
    filtros = (agr_div, Div_FT, br, ut, filtro, dpto, mpio, enemigo, op_mayores, apoyo_unidad, afectaciones, tipo_titulo, permiso, unidad, fullname, ruta, spoa, delco_cap, estrategia, gaulas, coordinadas, conjuntas, tipo_afectaciones, tipo_operacion, cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion, unidades_asc)
    direcion =  resultados_resaltantes(fecha_primer_lapso_inicial, fecha_ultimo_lapso_inicial, filtros, dir_archivos, nombre_carpeta)

    dir = {
                "direccion":direcion[0],
                "nombre":direcion[1]
            }

    return dir