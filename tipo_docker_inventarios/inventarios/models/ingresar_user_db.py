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

def guardar_evento(datos, foto):


    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]



    fecha_asignacion = datos["fecha_asignacion"]
    director = datos["director"]
    director_cargo = datos["director_cargo"]
    seccion = datos["seccion"]
    seccion_cargo = datos["seccion_cargo"]
    responsable = datos["responsable"]
    responsable_cargo = datos["responsable_cargo"]


    fecha_asignacion = fecha_asignacion.upper()
    director = director.upper()
    director_cargo = director_cargo.upper()
    seccion = seccion.upper()
    seccion_cargo = seccion_cargo.upper()
    responsable = responsable.upper()
    responsable_cargo = responsable_cargo.upper()

    

    inventario = datos["inventario"]

    observaciones = datos["observaciones"]


    import json
    inventario = json.loads(inventario)
    observaciones = json.loads(observaciones)


    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(fecha_asignacion, director, director_cargo, seccion, seccion_cargo, responsable, responsable_cargo)

    query="insert into inventarios_unidad (fecha_asignacion, director, director_cargo, seccion, seccion_cargo, responsable, responsable_cargo) values"+dato
    
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = """select id from inventarios_unidad where director = '{}' and seccion = '{}' and responsable = '{}' """.format(director, seccion, responsable)

    cursor.execute(query)
    data = cursor.fetchall()

    for x in data:
        no_id = x[0]
    if foto !="validar":
        nombre_foto = str("/fotos_inventarios/")+str(no_id)+"_"+str(foto)
    else:
        nombre_foto = datos["foto_2"]
    
    query = """UPDATE inventarios_unidad SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    cursor.execute(query)
    conn.commit()



    for x in inventario:

        dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(no_id,x[0], x[1].upper(), x[2], x[3], x[4], x[5])

        query="insert into inventarios_unidad_material (id_inventarios_unidad, numero_activo, denominacion, numero_de_serie, numero_de_inventario, valor, ubicacion_material) values"+dato
        cursor.execute(query)

    conn.commit()

    for x in observaciones:
        # print(x)
        dato="""('{}', '{}')""".format(no_id, x.upper())

        query="insert into inventarios_unidad_observaciones (id_inventarios_unidad, observaciones_elemento) values"+dato
        cursor.execute(query)

    conn.commit()
    
    query = "select * from inventarios_unidad"
    cursor.execute(query)
    data = cursor.fetchall()


    conn.close()
    cursor.close


    return [nombre_foto, data]


def delete_evento(datos):

    #datos
    id_personal = datos["id_personal"]

    query="""DELETE FROM personal WHERE id = {}""".format(id_personal)
    # print(query)
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = "select * from personal"
    cursor.execute(query)
    datos = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [datos]


def delete_cargo_personal(datos):

    #datos
    id_personal = datos["id_personal"]

    query="""DELETE FROM Cargos_personal  WHERE id_personal = '{}'""".format(id_personal)
    # print(query)
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = "select * from Cargos_personal WHERE id_personal = '{}'""".format(id_personal)
    cursor.execute(query)
    datos = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [datos]

def delete_cargo_personal_unico(datos):

    #datos
    id_personal = datos["id_personal"]
    id = datos["id"]

    query="""DELETE FROM Cargos_personal  WHERE id = {} and id_personal = '{}' """.format(id, id_personal)
    # print(query)
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = "select * from Cargos_personal WHERE id_personal = '{}' """.format(id_personal)
    cursor.execute(query)
    datos = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [datos]

def select_cargo_personal(datos):

    #datos
    id_inventarios_unidad = datos["id_inventarios_unidad"]


    # print(query)
    
    conn = connect()
    cursor = conn.cursor()

    query = "select * from inventarios_unidad_material WHERE id_inventarios_unidad = '{}' """.format(id_inventarios_unidad)
    # print(query)
    cursor.execute(query)
    datos = cursor.fetchall()

    query = "select * from inventarios_unidad_observaciones WHERE id_inventarios_unidad = '{}' """.format(id_inventarios_unidad)
    # print(query)
    cursor.execute(query)
    datos_2 = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [datos, datos_2]


def guardar_cargo(datos):


    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]

    id_personal = datos["id_personal"]
    cedula = datos["cedula"]
    cargo = datos["cargo"]
    fecha_inicio_cargo = datos["fecha_inicio_cargo"]
    fecha_termino_cargo = datos["fecha_termino_cargo"]
    tiempo_cargo = datos["tiempo_cargo"]

    id_personal = id_personal.upper()
    cedula = cedula.upper()
    cargo = cargo.upper()
    fecha_inicio_cargo = fecha_inicio_cargo.upper()
    fecha_termino_cargo = fecha_termino_cargo.upper()
    tiempo_cargo = tiempo_cargo.upper()

    

    dato="""('{}', '{}', '{}',	'{}', '{}', '{}')""".format(id_personal, cedula, cargo, fecha_inicio_cargo, fecha_termino_cargo, tiempo_cargo)

    query="insert into Cargos_personal (id_personal, cedula, cargo, fecha_inicio_cargo, fecha_termino_cargo, tiempo_cargo) values"+dato
    
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


    query = "select * from Cargos_personal"
    cursor.execute(query)
    data = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [data]

