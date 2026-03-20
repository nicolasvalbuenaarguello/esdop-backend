from datetime import datetime
# coding: utf-8
import psycopg2
import base64 

from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()

def transformar(dato):
    dato = str(dato)
    # dato = dato.replace("datetime.time(",  " '")
    dato = dato.replace("?",  ' ')
    dato = dato.replace("#",  ' ')
    dato = dato.replace("/",  ' ')
    dato = dato.replace("*",  ' ')
    dato = dato.replace(",",  '-')
    # dato = dato.replace("datetime.datetime(", " '")
    dato = dato.replace("(",  ' ')
    dato = dato.replace("),",  "',")
    dato = dato.replace(")",  ' ')
    dato = dato.replace("$",  ' ')
    dato = dato.replace("%",  ' ')
    dato = dato.replace("{",  ' ')
    dato = dato.replace("}",  ' ')
    dato = dato.replace("[",  ' ')
    dato = dato.replace("]",  ' ')
    dato = dato.replace("<",  ' ')
    dato = dato.replace(">",  ' ')
    dato = dato.replace("¨",  ' ')
    dato = dato.replace("^",  ' ')
    dato = dato.replace("~",  ' ')
    dato = dato.replace("`",  ' ')
    dato = dato.replace("'",  ' ')
    dato = dato.replace('"',  ' ')
    
def transformar(dato):
    dato = str(dato)
    # dato = dato.replace("datetime.time(",  " '")
    dato = dato.replace("?",  ' ')
    dato = dato.replace("#",  ' ')
    dato = dato.replace("/",  ' ')
    dato = dato.replace("*",  ' ')
    dato = dato.replace(",",  '-')
    # dato = dato.replace("datetime.datetime(", " '")
    dato = dato.replace("(",  ' ')
    dato = dato.replace("),",  "',")
    dato = dato.replace(")",  ' ')
    dato = dato.replace("$",  ' ')
    dato = dato.replace("%",  ' ')
    dato = dato.replace("{",  ' ')
    dato = dato.replace("}",  ' ')
    dato = dato.replace("[",  ' ')
    dato = dato.replace("]",  ' ')
    dato = dato.replace("<",  ' ')
    dato = dato.replace(">",  ' ')
    dato = dato.replace("¨",  ' ')
    dato = dato.replace("^",  ' ')
    dato = dato.replace("~",  ' ')
    dato = dato.replace("`",  ' ')
    dato = dato.replace("'",  ' ')
    dato = dato.replace('"',  ' ')
    
    
    return dato

#Funcion de resultados nueva ayuda
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn


def guardar_evento(datos, acta_alerta_nombres):

    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]

    	
    numero = datos["numero"]
    fecha = datos["fecha"]
    hora = datos["hora"]

    origen = datos["origen"]
    destino = datos["destino"]
    grd_recibe= datos["grd_recibe"]
    nombre_recibe = datos["nombre_recibe"]
    cargo = datos["cargo"]
    telefono = datos["telefono"]

    grd_remitente = datos["grd_remitente"]
    nombre_remitente = datos["nombre_remitente"]
    cargo_remitente = datos["cargo_remitente"]
    telefono_remitente = datos["telefono_remitente"]

    departamento = datos["departamento"]
    municipio= datos["municipio"]
    sitio = datos["sitio"]
    latitud = datos["latitud"]
    gr_n = datos["gr_n"]
    m_n = datos["m_n"]
    s_n = datos["s_n"]
    longitud = datos["longitud"]
    gr_l = datos["gr_l"]
    m_l = datos["m_l"]
    s_l = datos["s_l"]


    fecha_registro = datos["fecha_registro"]
    hora_registro = datos["hora_registro"]
    numero_folio_registro = datos["numero_folio_registro"]

    enemigo = datos["enemigo"]
    accion_enemiga = datos["accion_enemiga"]
    fuerza = datos["fuerza"]

        
    destino_criptografo = datos["destino_criptografo"]
    grd_recibe_criptografo = datos["grd_recibe_criptografo"]
    nombre_recibe_criptografo = datos["nombre_recibe_criptografo"]
    telefono_criptografo = datos["telefono_criptografo"]
    cargo_criptografo = datos["cargo_criptografo"]



    
    permiso =  permiso.upper()
    unidad =  unidad.upper()
    numero =  numero.upper()
    fecha =  fecha.upper()
    hora =  hora.upper()
    origen =  origen.upper()
    destino =  destino.upper()
    grd_recibe =  grd_recibe.upper()
    nombre_recibe =  nombre_recibe.upper()
    cargo =  cargo.upper()
    telefono =  telefono.upper()
    grd_remitente =  grd_remitente.upper()
    nombre_remitente =  nombre_remitente.upper()
    cargo_remitente =  cargo_remitente.upper()
    telefono_remitente =  telefono_remitente.upper()
    departamento =  departamento.upper()
    municipio =  municipio.upper()
    sitio =  sitio.upper()
    latitud =  latitud.upper()
    gr_n =  gr_n.upper()
    m_n =  m_n.upper()
    s_n =  s_n.upper()
    longitud =  longitud.upper()
    gr_l =  gr_l.upper()
    m_l =  m_l.upper()
    s_l =  s_l.upper()
    fecha_registro =  fecha_registro.upper()
    hora_registro =  hora_registro.upper()
    numero_folio_registro =  numero_folio_registro.upper()


    enemigo =  enemigo.upper()
    accion_enemiga =  accion_enemiga.upper()
    fuerza =  fuerza.upper()

    destino_criptografo =  destino_criptografo.upper()
    grd_recibe_criptografo =  grd_recibe_criptografo.upper()
    nombre_recibe_criptografo =  nombre_recibe_criptografo.upper()
    telefono_criptografo =  telefono_criptografo.upper()
    cargo_criptografo =  cargo_criptografo.upper()



    if latitud =="LN":
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))*1
    else:
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))-1

    if longitud=="LW":

        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*-1
    else:
        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*1


    # print(documento)

    # image_64_encode = base64.encode(documento)
    numero = transformar(numero)
    fecha = transformar(fecha)
    hora = transformar(hora)
    origen = transformar(origen)
    destino = transformar(destino)
    grd_recibe = transformar(grd_recibe)
    nombre_recibe = transformar(nombre_recibe)

    cargo = transformar(cargo)
    telefono = transformar(telefono)
    grd_remitente = transformar(grd_remitente)
    nombre_remitente = transformar(nombre_remitente)

    cargo_remitente = transformar(cargo_remitente)
    telefono_remitente = transformar(telefono_remitente)
    departamento = transformar(departamento)
    municipio = transformar(municipio)
    sitio = transformar(sitio)
    latitud = transformar(latitud)
    gr_n = transformar(gr_n)
    m_n = transformar(m_n)
    s_n = transformar(s_n)
    longitud = transformar(longitud)
    gr_l = transformar(gr_l)
    m_l = transformar(m_l)
    s_l = transformar(s_l)
    coordenadas_x = transformar(coordenadas_x)
    coordenadas_y = transformar(coordenadas_y)
    fecha_registro = transformar(fecha_registro)
    hora_registro = transformar(hora_registro)
    numero_folio_registro = transformar(numero_folio_registro)
    enemigo = transformar(enemigo)
    accion_enemiga = transformar(accion_enemiga)
    fuerza = transformar(fuerza)
    destino_criptografo = transformar(destino_criptografo)
    grd_recibe_criptografo = transformar(grd_recibe_criptografo)
    nombre_recibe_criptografo = transformar(nombre_recibe_criptografo)
    telefono_criptografo = transformar(telefono_criptografo)
    cargo_criptografo = transformar(cargo_criptografo)

    dato="""('{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}')""".format(numero,	fecha,	hora,	origen,	destino,	grd_recibe,	nombre_recibe,	cargo,	telefono,	grd_remitente,	nombre_remitente,	cargo_remitente,	telefono_remitente,	departamento,	municipio,	sitio,	latitud,	gr_n,	m_n,	s_n,	longitud,	gr_l,	m_l,	s_l,	coordenadas_x,	coordenadas_y,	fecha_registro,	hora_registro,	numero_folio_registro, enemigo, accion_enemiga, fuerza, destino_criptografo, grd_recibe_criptografo, nombre_recibe_criptografo, telefono_criptografo, cargo_criptografo)

    
    query="insert into alertas (numero,	fecha,	hora,	origen,	destino,	grd_recibe,	nombre_recibe,	cargo,	telefono,	grd_remitente,	nombre_remitente,	cargo_remitente,	telefono_remitente,	departamento,	municipio,	sitio,	latitud,	gr_n,	m_n,	s_n,	longitud,	gr_l,	m_l,	s_l,	coordenadas_x,	coordenadas_y,	fecha_registro,	hora_registro,	numero_folio_registro, enemigo, accion_enemiga, fuerza, destino_criptografo, grd_recibe_criptografo, nombre_recibe_criptografo, telefono_criptografo, cargo_criptografo) values"+dato
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


   
    if acta_alerta_nombres !="validar":
        nombre_actas_reserva = str("/alertas_scan/")+str(numero)+"_"+str(fecha)+"_"+str(acta_alerta_nombres)
    else:
        nombre_actas_reserva = datos["acta_alerta_2"]

    query = """UPDATE alertas SET acta = '{}' WHERE numero = '{}' and  fecha = '{}';""".format(nombre_actas_reserva, numero, fecha)

    cursor.execute(query)
    conn.commit()

#1234567890'sdfghjkuytrfvb)(/&%$#) 
                        


    query_eventos =  "SELECT * FROM alertas ORDER BY FECHA ASC"

            
    cursor.execute(query_eventos)
    data = cursor.fetchall()
    conn.close()
    cursor.close



    return [data, nombre_actas_reserva]


def eliminar(datos):

    #datos
    id_alerta = datos["id_alerta"]
  
    # print(documento)

    # image_64_encode = base64.encode(documento)

    query="""DELETE FROM alertas WHERE id = {}""".format(id_alerta)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query_eventos =  "SELECT * FROM alertas ORDER BY FECHA ASC"
 
    cursor.execute(query_eventos)
    data = cursor.fetchall()
    conn.close()
    cursor.close

    return [data]