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
    
async def cargar_resultados(contents):

    DIRECION = os.getenv('DIRECION')
    ruta = DIRECION
    dirercion_archvios = '{}pazos_fronterizos/documentos'.format(ruta)



    ruta =  os.path.abspath(dirercion_archvios) 
    insitop = "/plasos_fronterizos.xlsx"

    hoja = "Hoja1"
    mensaje = "Hoja1"
    fichero = ruta + insitop

    conversion.leer_excel(fichero)
    conversion.convertir(fichero, hoja, mensaje, contents)


    
async def cargar_resultados_pasos(contents):

    DIRECION = os.getenv('DIRECION')
    ruta = DIRECION
    dirercion_archvios = '{}pazos_fronterizos/documentos'.format(ruta)



    ruta =  os.path.abspath(dirercion_archvios) 
    insitop = "/plasos_fronterizos.xlsx"

    hoja = "Pasos Frontera.dbf"
    mensaje = "Pasos Frontera.dbf"
    fichero = ruta + insitop

    conversion.leer_excel(fichero)
    conversion.convertir_2(fichero, hoja, mensaje)


