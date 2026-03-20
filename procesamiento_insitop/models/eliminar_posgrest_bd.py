from __init__ import *
from models.conversor import *
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn


async def actualizar_datos():
    print( "entre")
    dato=0
    conn = connect()
    cursor = conn.cursor()
        


    dato = "REFRESH MATERIALIZED VIEW view_hechos_materializados"
    cursor.execute(dato)
    # conn.commit()
    print("se actualizo hechos")

    dato = "REFRESH MATERIALIZED VIEW view_erradicacion_materializados"
    cursor.execute(dato)
    print("se actualizo erradicacion")
    # conn.commit()

    dato = "REFRESH MATERIALIZED VIEW view_resultados_materializados"
    cursor.execute(dato)
    print("se actualizo resultados")
    conn.commit()
    conn.close()

    print("se actulizo los datos")
    
async def cargar_resultados():

    DIRECION = os.getenv('DIRECION')
    ruta = DIRECION
    dirercion_archvios = '{}procesamiento_insitop/documentos'.format(ruta)



    ruta =  os.path.abspath(dirercion_archvios) 
    insitop = "/INSITOP.xlsx"

    hoja = "ReporteDispositivos"
    mensaje = "ReporteDispositivos"
    fichero = ruta + insitop

    conversion.leer_excel(fichero)
    conversion.convertir(fichero, hoja, mensaje)

async def cargar_resultados_unidades():

    DIRECION = os.getenv('DIRECION')
    ruta = DIRECION
    dirercion_archvios = '{}procesamiento_insitop/documentos'.format(ruta)

    ruta =  os.path.abspath(dirercion_archvios) 
    insitop = "/archivo.xlsx"

    hoja = "ReporteDispositivos"
    mensaje = "ReporteDispositivos"
    fichero = ruta + insitop

    conversion.leer_excel(fichero)
    conversion.convertir_unidad(fichero, hoja, mensaje)


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