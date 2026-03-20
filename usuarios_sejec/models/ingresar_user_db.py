from datetime import datetime
# coding: utf-8
from __init__ import *
from models.conexion_pos import *
from werkzeug.security import generate_password_hash
import psycopg2
#Funcion de resultados nueva ayuda
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

def guardar_evento(datos, foto):
    

    nombre = datos["nombre"]
    contrasenia = generate_password_hash(datos["contrasenia"])
    usuario = datos["usuario"]
    roll = datos["roll"]
    correo = datos["correo"]
    unidad_selecionada = datos["unidad_selecionada"]


    per_select = validar_check(datos["per_select"])
    per_insert = validar_check(datos["per_insert"])
    per_update = validar_check(datos["per_update"])
    per_delete = validar_check(datos["per_delete"])
    crear_orden = validar_check(datos["crear_orden"])
    asignar_orden = validar_check(datos["asignar_orden"])
    cerrar_orden = validar_check(datos["cerrar_orden"])
    modificar_estado = validar_check(datos["modificar_estado"])
    crear_user =  validar_check(datos["crear_user"])
    listado_user = validar_check(datos["listado_user"])
    editar_user = validar_check(datos["editar_user"])

    # excel_amenaza

    dato="""('{}', '{}', '{}',	'{}', '{}',	'{}',{},{},	{},	{},	{},	{},	{},	{},	{},	{},	{})""".format(nombre, contrasenia, usuario, roll, correo, unidad_selecionada, per_select, per_insert, per_update, per_delete, crear_orden, asignar_orden, cerrar_orden, modificar_estado, crear_user, listado_user, editar_user)

    query="insert into usuarios_sejec (full_nombre,  contrasenia, usuario, roll, correo, ID_COMAND, per_select, per_insert, per_update, per_delete, crear_orden, asignar_orden, cerrar_orden, modificar_estado, crear_user, listado_user, editar_user) values "+dato

    #foto
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    query = """select id from usuarios_sejec where full_nombre = '{}' and usuario = '{}' """.format(nombre, usuario)

    cursor.execute(query)
    data = cursor.fetchall()

    for x in data:
        no_id = x[0]

    nombre_foto = str("/fotos_usurios_sejec/")+str(no_id)+"_"+str(foto)
    query = """UPDATE usuarios_sejec SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    cursor.execute(query)
    conn.commit()

    di_nombre = no_id
    id_cargo = 1
    estado_firma = "NO FIRMA"
    dato="""({}, {}, '{}')""".format(di_nombre, id_cargo, estado_firma)
    query="insert into firmas_documentos (di_nombre,  id_cargo, estado_firma) values "+dato
    cursor.execute(query)
    conn.commit()

    query_f =  """SELECT DISTINCT 
                                                    usuarios_sejec.id, 
                                                    usuarios_sejec.full_nombre, 
                                                    usuarios_sejec.usuario,
                                                    usuarios_sejec.foto,
                                                    usuarios_sejec.roll,
                                                    usuarios_sejec.correo,
                                                    usuarios_sejec.per_select,
                                                    usuarios_sejec.per_insert,
                                                    usuarios_sejec.per_update,
                                                    usuarios_sejec.per_delete,
                                                    usuarios_sejec.crear_orden,
                                                    usuarios_sejec.asignar_orden,
                                                    usuarios_sejec.cerrar_orden,
                                                    usuarios_sejec.modificar_estado,
                                                    usuarios_sejec.crear_user,
                                                    usuarios_sejec.listado_user,
                                                    usuarios_sejec.editar_user,
                                                    cargos_plataforma.cargo_sejec,
                                                    firmas_documentos.estado_firma,
                                                    firmas_documentos.firma_numero, 
                                                    firmas_documentos.di_nombre,
                                                    unidades_internas.ABREV_JEFATURA,
                                                    unidades_internas.DESCRIPCION_JEFATURA,
                                                    firmas_documentos.firma
                    FROM usuarios_sejec INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = usuarios_sejec.ID_COMAND INNER  JOIN  firmas_documentos on firmas_documentos.di_nombre = usuarios_sejec.id  INNER  JOIN  cargos_plataforma on cargos_plataforma.id_cargos_plataforma = firmas_documentos.id_cargo;"""
    cursor.execute(query_f)
    data = cursor.fetchall()

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [nombre_foto, data]


def guardar_cargos(datos):
    

    cargo = datos["cargo"]
 
    cargo = cargo.upper()

    # excel_amenaza

    dato="""('{}') """.format(cargo)

    query="insert into cargos_plataforma (cargo_sejec) values "+dato

    #foto
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

   
    query = "select * from cargos_plataforma"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [data]


def eidtar_permisos_user(datos, guardar_imagen):
    
    estado_firma = datos["estado_firma"]
    firma_numero = datos["firma_numero"]

    id_usuario = datos["id_usuario"]
    id_cargo = datos["id_cargo"]


    per_select = validar_check(datos["per_select"])
    per_insert = validar_check(datos["per_insert"])
    per_update = validar_check(datos["per_update"])
    per_delete = validar_check(datos["per_delete"])
    crear_orden = validar_check(datos["crear_orden"])
    asignar_orden = validar_check(datos["asignar_orden"])
    cerrar_orden = validar_check(datos["cerrar_orden"])
    modificar_estado = validar_check(datos["modificar_estado"])
    crear_user =  validar_check(datos["crear_user"])
    listado_user = validar_check(datos["listado_user"])
    editar_user = validar_check(datos["editar_user"])

    # excel_amenaza

    query = """UPDATE usuarios_sejec SET per_select = {}, per_insert = {}, per_update = {}, per_delete = {}, crear_orden = {}, asignar_orden = {}, cerrar_orden = {}, modificar_estado = {}, crear_user = {}, listado_user = {}, editar_user = {} WHERE id = {} ;""".format(per_select, per_insert, per_update, per_delete, crear_orden, asignar_orden, cerrar_orden, modificar_estado, crear_user, listado_user, editar_user, id_usuario)

    #foto
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    if guardar_imagen:
        firma =  f"/fotos_usurios_sejec/firmas/{id_usuario}_{firma_numero}.png"
    else:
        firma=""

    query = """UPDATE firmas_documentos SET id_cargo = {}, estado_firma = '{}', firma_numero = '{}', firma = '{}' WHERE di_nombre = {} ;""".format(id_cargo, estado_firma, firma_numero, firma, id_usuario)

    #foto
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query_f =  """SELECT DISTINCT 
                                                    usuarios_sejec.id, 
                                                    usuarios_sejec.full_nombre, 
                                                    usuarios_sejec.usuario,
                                                    usuarios_sejec.foto,
                                                    usuarios_sejec.roll,
                                                    usuarios_sejec.correo,
                                                    usuarios_sejec.per_select,
                                                    usuarios_sejec.per_insert,
                                                    usuarios_sejec.per_update,
                                                    usuarios_sejec.per_delete,
                                                    usuarios_sejec.crear_orden,
                                                    usuarios_sejec.asignar_orden,
                                                    usuarios_sejec.cerrar_orden,
                                                    usuarios_sejec.modificar_estado,
                                                    usuarios_sejec.crear_user,
                                                    usuarios_sejec.listado_user,
                                                    usuarios_sejec.editar_user,
                                                    cargos_plataforma.cargo_sejec,
                                                    firmas_documentos.estado_firma,
                                                    firmas_documentos.firma_numero, 
                                                    firmas_documentos.di_nombre,
                                                    unidades_internas.ABREV_JEFATURA,
                                                    unidades_internas.DESCRIPCION_JEFATURA,
                                                    firmas_documentos.firma
                    FROM usuarios_sejec INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = usuarios_sejec.ID_COMAND INNER  JOIN  firmas_documentos on firmas_documentos.di_nombre = usuarios_sejec.id  INNER  JOIN  cargos_plataforma on cargos_plataforma.id_cargos_plataforma = firmas_documentos.id_cargo;"""
    cursor.execute(query_f)
    data = cursor.fetchall()

    conn.close()
    cursor.close
    #     # data = datos.fetchone()

    return [data, firma]

