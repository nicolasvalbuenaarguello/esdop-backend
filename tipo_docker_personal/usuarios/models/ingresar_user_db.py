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

def valorgrado(grd):
    valor = 0
    if grd == "GR":
        valor = 0
    elif grd == "MG":
        valor = 1
    elif grd == "BG":
        valor = 2
    elif grd == "CR":
        valor = 3
    elif grd == "TC":
        valor = 4
    elif grd == "MY":
        valor = 5
    elif grd == "CT":
        valor = 6
    elif grd == "TE":
        valor = 6
    elif grd == "ST":
        valor = 8
    elif grd == "SMC":
        valor = 9
    elif grd == "SM":
        valor = 10
    elif grd == "SP":
        valor = 11
    elif grd == "SV":
        valor = 12
    elif grd == "SS":
        valor = 13
    elif grd == "CP":
        valor = 14
    elif grd == "CS":
        valor = 15
    elif grd == "C3":
        valor = 16
    elif grd == "----":
        valor = 17
    return valor

def guardar_evento(datos, foto):


    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]


    grd= datos["grd"]
    valor_grado = valorgrado(grd)

    apellidos= datos["apellidos"]
    nombres= datos["nombres"]
    cedula= datos["cedula"]
    fecha_cumpleaños= datos["fecha_cumpleaños"]
    tel_principal= datos["tel_principal"]
    correo_ejc= datos["correo_ejc"]
    correo_civil= datos["correo_civil"]
    departamento= datos["departamento"]
    municipio= datos["municipio"]
    barrio= datos["barrio"]
    direcion_principal= datos["direcion_principal"]
    departamento_fuera= datos["departamento_fuera"]
    municipio_fuera= datos["municipio_fuera"]
    barrio_fuera= datos["barrio_fuera"]
    direcion_principal_fuera= datos["direcion_principal_fuera"]
    telefono_alterno= datos["telefono_alterno"]
    nombre_contacto= datos["nombre_contacto"]
    parentesco= datos["parentesco"]
    fecha_unidad= datos["fecha_unidad"]
    cargo= datos["cargo"]
    fecha_cargo= datos["fecha_cargo"]


    grd = grd.upper()
    apellidos = apellidos.upper()
    nombres = nombres.upper()
    cedula = cedula.upper()
    fecha_cumpleaños = fecha_cumpleaños.upper()
    tel_principal = tel_principal.upper()

    departamento = departamento.upper()
    municipio = municipio.upper()
    barrio = barrio.upper()
    direcion_principal = direcion_principal.upper()
    departamento_fuera = departamento_fuera.upper()
    municipio_fuera = municipio_fuera.upper()
    barrio_fuera = barrio_fuera.upper()
    direcion_principal_fuera = direcion_principal_fuera.upper()
    telefono_alterno = telefono_alterno.upper()
    nombre_contacto = nombre_contacto.upper()
    parentesco = parentesco.upper()
    fecha_unidad = fecha_unidad.upper()
    cargo = cargo.upper()
    fecha_cargo = fecha_cargo.upper()

    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})""".format(grd, apellidos, nombres, cedula, fecha_cumpleaños, tel_principal, correo_ejc, correo_civil, departamento, municipio, barrio, direcion_principal, departamento_fuera, municipio_fuera, barrio_fuera, direcion_principal_fuera, telefono_alterno, nombre_contacto, parentesco, fecha_unidad, cargo, fecha_cargo, foto, valor_grado)

    query="insert into personal (grd, apellidos, nombres, cedula, fecha_cumpleaños, tel_principal, correo_ejc, correo_civil, departamento, municipio, barrio, direcion_principal, departamento_fuera, municipio_fuera, barrio_fuera, direcion_principal_fuera, telefono_alterno, nombre_contacto, parentesco, fecha_unidad, cargo, fecha_cargo, foto, valor_grado) values"+dato
    
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = """select id from personal where grd = '{}' and apellidos = '{}' and nombres = '{}' """.format(grd, apellidos, nombres)

    cursor.execute(query)
    data = cursor.fetchall()

    for x in data:
        no_id = x[0]
    if foto !="validar":
        nombre_foto = str("/fotos_personal/")+str(no_id)+"_"+str(foto)
    else:
        nombre_foto = datos["foto_2"]
    
    query = """UPDATE personal SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    cursor.execute(query)
    conn.commit()

    query = "select * from personal"
    cursor.execute(query)
    data = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [nombre_foto, data]

def guardar_evento_update(datos, foto):

    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]

    id_personal = datos["id_personal"]
    grd= datos["grd"]
    valor_grado = valorgrado(grd)
    apellidos= datos["apellidos"]
    nombres= datos["nombres"]
    cedula= datos["cedula"]
    fecha_cumpleaños= datos["fecha_cumpleaños"]
    tel_principal= datos["tel_principal"]
    correo_ejc= datos["correo_ejc"]
    correo_civil= datos["correo_civil"]
    departamento= datos["departamento"]
    municipio= datos["municipio"]
    barrio= datos["barrio"]
    direcion_principal= datos["direcion_principal"]
    departamento_fuera= datos["departamento_fuera"]
    municipio_fuera= datos["municipio_fuera"]
    barrio_fuera= datos["barrio_fuera"]
    direcion_principal_fuera= datos["direcion_principal_fuera"]
    telefono_alterno= datos["telefono_alterno"]
    nombre_contacto= datos["nombre_contacto"]
    parentesco= datos["parentesco"]
    fecha_unidad= datos["fecha_unidad"]
    cargo= datos["cargo"]
    fecha_cargo= datos["fecha_cargo"]
   

    grd = grd.upper()
    apellidos = apellidos.upper()
    nombres = nombres.upper()
    cedula = cedula.upper()
    fecha_cumpleaños = fecha_cumpleaños.upper()
    tel_principal = tel_principal.upper()

    departamento = departamento.upper()
    municipio = municipio.upper()
    barrio = barrio.upper()
    direcion_principal = direcion_principal.upper()
    departamento_fuera = departamento_fuera.upper()
    municipio_fuera = municipio_fuera.upper()
    barrio_fuera = barrio_fuera.upper()
    direcion_principal_fuera = direcion_principal_fuera.upper()
    telefono_alterno = telefono_alterno.upper()
    nombre_contacto = nombre_contacto.upper()
    parentesco = parentesco.upper()
    fecha_unidad = fecha_unidad.upper()
    cargo = cargo.upper()
    fecha_cargo = fecha_cargo.upper()

    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', {})""".format(grd, apellidos, nombres, cedula, fecha_cumpleaños, tel_principal, correo_ejc, correo_civil, departamento, municipio, barrio, direcion_principal, departamento_fuera, municipio_fuera, barrio_fuera, direcion_principal_fuera, telefono_alterno, nombre_contacto, parentesco, fecha_unidad, cargo, fecha_cargo, foto, valor_grado)

    query="insert into personal (grd, apellidos, nombres, cedula, fecha_cumpleaños, tel_principal, correo_ejc, correo_civil, departamento, municipio, barrio, direcion_principal, departamento_fuera, municipio_fuera, barrio_fuera, direcion_principal_fuera, telefono_alterno, nombre_contacto, parentesco, fecha_unidad, cargo, fecha_cargo, foto, valor_grado) values"+dato
    

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = """select id from personal where grd = '{}' and apellidos = '{}' and nombres = '{}' """.format(grd, apellidos, nombres)

    cursor.execute(query)
    data = cursor.fetchall()

    for x in data:
        no_id = x[0]
    if foto !="validar":
        nombre_foto = str("/fotos_personal/")+str(no_id)+"_"+str(foto)
    else:
        nombre_foto = datos["foto_2"]
    
    query = """UPDATE personal SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    cursor.execute(query)
    conn.commit()

    query = """UPDATE Cargos_personal SET id_personal = '{}' WHERE id_personal = '{}' ;""".format(no_id, id_personal)
    cursor.execute(query)
    conn.commit()


    query = "select * from personal"
    cursor.execute(query)
    data = cursor.fetchall()

    # for x in datos:
    #     print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

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
    id_personal = datos["id_personal"]


    #print(id_personal)
    
    conn = connect()
    cursor = conn.cursor()

    query = "select * from Cargos_personal WHERE id_personal = '{}' """.format(id_personal)
    # print(query)
    cursor.execute(query)
    datos = cursor.fetchall()

    #for x in datos:
        #print(x)

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [datos]


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

