from datetime import datetime
# coding: utf-8
import psycopg2
import base64 

from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()


#Funcion de resultados nueva ayuda
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def buscar_personal(datos):

    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]

    fecha = datos["fecha"]
    cedula = datos["cedula"]
    
    conn = connect()
    cursor = conn.cursor()
    # print(fecha)
    if fecha != "" and fecha != "---":
        valor = " where date(Fecha_del_evento) = '{}'".format(fecha)
    elif cedula != "" and cedula != "---":
        valor = " where Documento_de_identidad = '{}'".format(cedula)
    else:
        valor = " "
                
    query_eventos =  "SELECT * FROM formulario_1_dipse {} ORDER BY Fecha_del_evento desc".format(valor)
    # print(query_eventos)
    cursor.execute(query_eventos)
    data = cursor.fetchall()
    conn.close()
    cursor.close
    # print(data)
    return [data]

