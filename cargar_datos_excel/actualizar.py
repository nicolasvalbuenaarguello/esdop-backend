import os
from dotenv import load_dotenv
load_dotenv() 
from datetime import datetime
# coding: utf-8
import psycopg2

def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def actualizar_datos():
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


    dato = "REFRESH MATERIALIZED VIEW view_enemigo_materializados"
    cursor.execute(dato)
    

    print("se actualizo view_enemigo_materializados")

    
    dato = "REFRESH MATERIALIZED VIEW view_unidades_materializados"
    cursor.execute(dato)
    print("se actualizo unidades")
    
    conn.commit()
    conn.close()
    print("se actulizo los datos")
 
actualizar_datos()