import os
import shutil
# from funtions.pdf.resultados.pdf import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.models.funtions.pdf.boletin_coe import *
#Funcion de resultados nueva ayuda

def c_c_boletin_estadistica_narcotrafico_metas(datos, link, ruta, puerto):


    nombre_carpeta = "narcotrafico_metas{}/".format(puerto)
    link = link+nombre_carpeta
    dirercion_archvios = link
    try:
        os.mkdir(link)
    except FileExistsError:
        print("Directorio %s ya existe" % link)
        for files in os.listdir(dirercion_archvios):
            path = os.path.join(dirercion_archvios, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
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
    # print(documento)
    filtros = (agr_div, Div_FT, br, ut, filtro, dpto, mpio, enemigo, op_mayores, apoyo_unidad, afectaciones, tipo_titulo, permiso, unidad, fullname, ruta, spoa, delco_cap, estrategia, gaulas, coordinadas, conjuntas, tipo_afectaciones, tipo_operacion, cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion)

    direcion = pdf_boletin_narcotrafico(fecha_primer_lapso_inicial, fecha_ultimo_lapso_inicial, filtros, dirercion_archvios, nombre_carpeta) 
    
    dir = {
                "direccion":direcion[0],
                "nombre":direcion[1]
            }

    return dir