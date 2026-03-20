from datetime import datetime
# coding: utf-8
from __init__ import *
from models.conexion_pos import *
from werkzeug.security import generate_password_hash
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=PLAZOS_SEGUNDO_CDTE \
        user=postgres \
        password=NICval10**")
    return conn

def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor

def guardar_evento(datos, acta_reserva_file_nombres):
    # excel_amenaza
    numero_orden =  datos["numero_orden"]
    fecha_creacion_orden =  datos["fecha_registro"]
    origen  = datos["origen"]
    unidad_que_radica  = datos["unidad_que_radica"]
    unidad  = datos["unidad"]
    otros_radicados  = datos["otros_radicados"]
    orfeo  = datos["orfeo"]
    asuntos  = datos["asuntos"]
    estado_orden = "ORDEN CREADA"
    dato="""('{}','{}','{}','{}','{}','{}','{}','{}', '{}' )""".format(numero_orden, fecha_creacion_orden, origen, unidad_que_radica, unidad, otros_radicados, orfeo, asuntos, estado_orden)

    query="insert into tabla_ordenes (numero_orden, fecha_creacion_orden, origen, unidad_que_radica, unidad, otros_radicados, orfeo, asuntos, estado_orden) values"+dato
       
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = """select id_tabla_ordenes from tabla_ordenes where numero_orden = '{}' and orfeo = '{}' """.format(numero_orden, orfeo)

    cursor.execute(query)
    data = cursor.fetchall()

    for x in data:
        no_id = x[0]

    if acta_reserva_file_nombres !="validar":
        query = """
        SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
        FROM folders f
        LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS SIN ASIGNAR' and s.active = True
        ORDER BY f.id, s.created_at DESC;
        """
        
        cursor.execute(query)
        numero_orden_regitrado = cursor.fetchall()
        carpeta_raiz = numero_orden_regitrado[0][0]
        sub_carpeta  = numero_orden_regitrado[0][1]
        direcion = str("/plazos_sejec/{}/{}/").format(carpeta_raiz, sub_carpeta)
        acta_reserva_file_nombres =acta_reserva_file_nombres.replace(" ", "_")
        nombre_actas_reserva = str(direcion)+str(no_id)+"_"+str(acta_reserva_file_nombres)

    else:
        nombre_actas_reserva = datos["acta_reserva_2"]

    query = """UPDATE tabla_ordenes SET documento_pdf_dir = '{}' WHERE id_tabla_ordenes = '{}' ;""".format(nombre_actas_reserva, no_id)
    cursor.execute(query)
    conn.commit()

    full_nombre = datos["full_nombre"]
    unidad_user = datos["unidad_user"]
    id_tabla_ordenes = no_id
    evento_registrar = "creación orden"
    fecha =  datos["fecha_registro"]

    query = """insert into tabla_log (full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, fecha) values ('{}','{}',{},'{}','{}')""".format(full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, fecha)
    cursor.execute(query)
    conn.commit()

    query="SELECT * FROM tabla_ordenes ORDER BY id_tabla_ordenes DESC LIMIT 1;"
    cursor.execute(query)
    numero_orden_regitrado = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close

    if numero_orden_regitrado:
        for x in numero_orden_regitrado:
            numero_orden_regitrado =  int(x[1])+1
    else:
        numero_orden_regitrado = 1


    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [nombre_actas_reserva, numero_orden_regitrado, direcion]


def numero_orden_select():

       
    conn = connect()
    cursor = conn.cursor() 


    query="SELECT * FROM tabla_ordenes ORDER BY id_tabla_ordenes DESC LIMIT 1;"
    cursor.execute(query)
    numero_orden_regitrado = cursor.fetchall()

    conn.close()
    cursor.close

    if numero_orden_regitrado:
        for x in numero_orden_regitrado:
            numero_orden_regitrado =  int(x[1])+1
    else:
        numero_orden_regitrado = 1


    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [numero_orden_regitrado]

