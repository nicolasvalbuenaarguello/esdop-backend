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


def estadisitca():
    conn = connect()
    cursor = conn.cursor()

    query_eventos =  "SELECT DISTINCT fecha FROM alertas ORDER BY fecha ASC"
    cursor.execute(query_eventos)
    fecha = cursor.fetchall()

    
    query_eventos =  "SELECT DISTINCT destino FROM alertas ORDER BY destino ASC"
    cursor.execute(query_eventos)
    destino = cursor.fetchall()

    
    query_eventos =  "SELECT DISTINCT departamento FROM alertas ORDER BY departamento ASC"
    cursor.execute(query_eventos)
    departamento = cursor.fetchall()

    
    query_eventos =  "SELECT DISTINCT enemigo FROM alertas ORDER BY enemigo ASC"
    cursor.execute(query_eventos)
    enemigo = cursor.fetchall()

    conn.close()
    cursor.close

    return [fecha, destino, departamento, enemigo]

def estadisitca_cantidad():
    query_eventos =  "SELECT *  FROM alertas ORDER BY destino ASC"


    conn = connect()
    cursor = conn.cursor()
            
    cursor.execute(query_eventos)
    data = cursor.fetchall()
    conn.close()
    cursor.close

    return [data]
