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


def guardar_evento(datos, foto_aetcr_nombres, foto_user_name_nombres):

    #datos
    permiso = datos["permiso"]
    unidad = datos["unidad"]

            
    numero = datos['numero']
    fecha = datos['fecha']
    nombre_aetcr = datos['nombre_aetcr']
    nivel_de_seguridad = datos['nivel_de_seguridad']
    cant_mujeres = datos['cant_mujeres']
    cant_hombres = datos['cant_hombres']
    departamento = datos['departamento']
    municipio = datos['municipio']
    sitio = datos['sitio']
    latitud = datos['latitud']
    gr_n = datos['gr_n']
    m_n = datos['m_n']
    s_n = datos['s_n']
    longitud = datos['longitud']
    gr_l = datos['gr_l']
    m_l = datos['m_l']
    s_l = datos['s_l']
    nombre_aetcr_encargado = datos['nombre_aetcr_encargado']
    seudonimo_aetcr_encargado = datos['seudonimo_aetcr_encargado']
    celular_aetcr_encargado = datos['celular_aetcr_encargado']
    ubicacion_aetcr_encargado = datos['ubicacion_aetcr_encargado']

    cantidad_per_anio = datos['cantidad_per_anio']
    servicio_publico = datos['servicio_publico']



   
    numero = numero.upper()
    fecha = fecha.upper()
    nombre_aetcr = nombre_aetcr.upper()
    nivel_de_seguridad = nivel_de_seguridad.upper()
    cant_mujeres = cant_mujeres.upper()
    cant_hombres = cant_hombres.upper()
    departamento = departamento.upper()
    municipio = municipio.upper()
    sitio = sitio.upper()
    latitud = latitud.upper()
    gr_n = gr_n.upper()
    m_n = m_n.upper()
    s_n = s_n.upper()
    longitud = longitud.upper()
    gr_l = gr_l.upper()
    m_l = m_l.upper()
    s_l = s_l.upper()
    nombre_aetcr_encargado = nombre_aetcr_encargado.upper()
    seudonimo_aetcr_encargado = seudonimo_aetcr_encargado.upper()
    celular_aetcr_encargado = celular_aetcr_encargado.upper()
    ubicacion_aetcr_encargado = ubicacion_aetcr_encargado.upper()




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
    nombre_aetcr = transformar(nombre_aetcr) 
    nivel_de_seguridad = transformar(nivel_de_seguridad) 
    cant_mujeres = transformar(cant_mujeres) 
    cant_hombres = transformar(cant_hombres) 
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
    nombre_aetcr_encargado = transformar(nombre_aetcr_encargado) 
    seudonimo_aetcr_encargado = transformar(seudonimo_aetcr_encargado) 
    celular_aetcr_encargado = transformar(celular_aetcr_encargado) 
    ubicacion_aetcr_encargado = transformar(ubicacion_aetcr_encargado) 
    coordenadas_x = transformar(coordenadas_x) 
    coordenadas_y = transformar(coordenadas_y) 

    dato="""('{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}',	'{}')""".format(numero ,	fecha ,	nombre_aetcr ,	nivel_de_seguridad ,	cant_mujeres ,	cant_hombres ,	departamento ,	municipio ,	sitio ,	latitud ,	gr_n ,	m_n ,	s_n ,	longitud ,	gr_l ,	m_l ,	s_l ,	coordenadas_x ,	coordenadas_y ,	nombre_aetcr_encargado ,	seudonimo_aetcr_encargado ,	celular_aetcr_encargado ,	ubicacion_aetcr_encargado )

    
    query="insert into aetcr (numero ,	fecha ,	nombre_aetcr ,	nivel_de_seguridad ,	cant_mujeres ,	cant_hombres ,	departamento ,	municipio ,	sitio ,	latitud ,	gr_n ,	m_n ,	s_n ,	longitud ,	gr_l ,	m_l ,	s_l ,	coordenadas_x ,	coordenadas_y ,	nombre_aetcr_encargado ,	seudonimo_aetcr_encargado ,	celular_aetcr_encargado ,	ubicacion_aetcr_encargado ) values"+dato

    
    #print(query)
    
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    
    #secuencia para guardar el nombre de la foto de la aetcr
    if foto_aetcr_nombres !="validar":
        foto_aetcr_nombres = str("/foto_aetcr/aetcr/")+str(numero)+"_"+str(fecha)+"_"+str(foto_aetcr_nombres)
    else:
        foto_aetcr_nombres = datos["foto_aetcr_2"]

    query = """UPDATE aetcr SET foto_aetcr = '{}' WHERE numero = '{}' and  nombre_aetcr = '{}';""".format(foto_aetcr_nombres, numero, nombre_aetcr)
    cursor.execute(query)
    conn.commit()

        
    #secuencia para guardar el nombre de la foto del responsable de la aetcr
    if foto_user_name_nombres !="validar":
        foto_user_name_nombres = str("/foto_aetcr/responsable/")+str(numero)+"_"+str(fecha)+"_"+str(foto_user_name_nombres)
    else:
        foto_user_name_nombres = datos["foto_user_name_2"]

    query = """UPDATE aetcr SET foto_user_name = '{}' WHERE numero = '{}' and  nombre_aetcr = '{}';""".format(foto_user_name_nombres, numero, nombre_aetcr)
    cursor.execute(query)
    conn.commit()


    #modulo para cargar por volcamiento de datos una informacion que viene por obejto y llgar str y se debe camabiar a obj antes de guardar 
    nueva=cantidad_per_anio.split(",") 
    i =0
    o =1
    cant  = len(nueva)
    #><
    anios =  []
    for x in nueva:
        if cant > i:    
            anios.append((numero, nombre_aetcr, nueva[i], nueva[o]))
            i = i+2
            o = o+2

    anios =  str(anios)
    
    anios = anios.replace('[', '')
    anios = anios.replace(']', '')
    #print(anios)
    query = """insert into cantidad_per_anio(id_aetcr, aetcr,  anio, cantidad )values {} """.format(anios)
    #print(query)
    cursor.execute(query)
    conn.commit()
  
    
    #modulo para cargar por volcamiento de datos una informacion que viene por obejto y llgar str y se debe camabiar a obj antes de guardar 
    nueva=servicio_publico.split(",") 

    i =0
    o =1
    p =2
    a =3

    cant  = len(nueva)
    #><
    anios =  []
    for x in nueva:
        if cant > i:    
            anios.append((numero, nombre_aetcr, nueva[i], nueva[o], nueva[p], nueva[a]))
            i = i+4
            o = o+4
            p = p+4
            a = a+4

    anios =  str(anios)

    
    anios = anios.replace('[', '')
    anios = anios.replace(']', '')
    
    query = """insert into servicio_publico(id_aetcr, aetcr,  servicios_basicos, servicios_basicos_selecionados, cantidad_tipo, cantidad_infor_servicios )values {} """.format(anios)
    cursor.execute(query)
    conn.commit()


#1234567890'sdfghjkuytrfvb)(/&%$#) 
                        
    conn.close()
    cursor.close

    return [foto_aetcr_nombres, foto_user_name_nombres]

def listado(datos):

    #datos


    conn = connect()
    cursor = conn.cursor()


    query_eventos =  "SELECT * FROM aetcr ORDER BY FECHA ASC"
 
    cursor.execute(query_eventos)
    data = cursor.fetchall()
    conn.close()
    cursor.close

    return [data]

def info_aetcr(datos):

    #datos
    id_aetcr = datos["id_aetcr"]  

    conn = connect()
    cursor = conn.cursor()


    query_eventos =  "SELECT * FROM aetcr WHERE id = {}".format(id_aetcr)
    cursor.execute(query_eventos)
    data = cursor.fetchall()

    query_eventos =  "SELECT * FROM cantidad_per_anio WHERE id_aetcr = '{}'".format(id_aetcr)
    cursor.execute(query_eventos)
    data_cantidad = cursor.fetchall()

    query_eventos =  "SELECT * FROM servicio_publico WHERE id_aetcr = '{}'".format(id_aetcr)
    cursor.execute(query_eventos)
    data_servicios = cursor.fetchall()


    conn.close()
    cursor.close

    return [data, data_cantidad, data_servicios]
def mapa_aetcr_buscar(datos):

    #datos
    fecha_ingreso = datos["fecha_ingreso"]  

    conn = connect()
    cursor = conn.cursor()


    query_eventos =  "SELECT * FROM aetcr "
    cursor.execute(query_eventos)
    data = cursor.fetchall()

    query_eventos =  "SELECT * FROM pelotones_aetcr WHERE fecha_registro = '{}'".format(fecha_ingreso)
    cursor.execute(query_eventos)
    data_cantidad = cursor.fetchall()




    conn.close()
    cursor.close
    
    return [data, data_cantidad]

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

def guardar_evento_aetcr_url_peloton(datos):
    informacion_peloton = datos['informacion_peloton']

    nueva=informacion_peloton.split(",") 

    a= 0
    b= 1
    c= 2
    d= 3
    e= 4
    f= 5
    g= 6
    h= 7
    i= 8
    j= 9
    k= 10
    l= 11
    m= 12
    n= 13
    
    o= 14
    p= 15
    q= 16
    r= 17
    s= 18
    t= 19
    u= 20
    v= 21
    w= 22
    x= 23
    y= 24
    z= 25
    aa= 26
    ab= 27

    cant  = len(nueva)
    
    #><
    anios =  []

    for nuev in nueva:
        if cant > i:    
            anios.append((nueva[a], nueva[b], nueva[c], nueva[d], nueva[e], nueva[f], nueva[g], nueva[h], nueva[i], nueva[j], nueva[k], nueva[l], nueva[m], nueva[n], nueva[o], nueva[p], nueva[q], nueva[r], nueva[s], nueva[t], nueva[u], nueva[v], nueva[w], nueva[x], nueva[y], nueva[z], nueva[aa], nueva[ab]))


            a = a + 28
            b = b + 28
            c = c + 28
            d = d + 28
            e = e + 28
            f = f + 28
            g = g + 28
            h = h + 28
            i = i + 28
            j = j + 28
            k = k + 28
            l = l + 28
            m = m + 28
            n = n + 28
            o = o + 28
            p = p + 28
            q = q + 28
            r = r + 28
            s = s + 28
            t = t + 28
            u = u + 28
            v = v + 28
            w = w + 28
            x = x + 28
            y = y + 28
            z = z + 28
            aa = aa + 28
            ab = ab + 28

    anios =  str(anios)

    
    anios = anios.replace('[', '')
    anios = anios.replace(']', '')
        
    query = """insert into pelotones_aetcr(cordenada_x, cordenada_y, fecha_registro, numero_hr, divi_padre, divi_hija, brigada, batallon, compania, peloton, grd, nombre_cdte, telefono_cdte, ofi, sub, slp, sl_18, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, vereda, nombre_aetcr, numero) values {} """.format(anios)
    #print(query)
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()
    conn.close()
    cursor.close


