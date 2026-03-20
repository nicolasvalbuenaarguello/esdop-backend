from datetime import datetime
# coding: utf-8
import psycopg2
import base64 

from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()


from z_z_configuarcion.caligrafia import *
from z_z_configuarcion.fechas import *


from flask import make_response
from datetime import date, time, datetime

from fpdf import FPDF
from math import sqrt, pi, sin, cos
from fpdf.php import sprintf
#Funcion para la creacion del reporte de resultados 
from __init__ import *

class PDF(FPDF):
    
    def __init__(self, orientation = 'P', unit = 'mm', format = 'A4'):
        self.ext_gstates = [ ]
        
        super(PDF, self).__init__(orientation, unit, format)

    def rounded_rect(self, x, y, w, h, r, style = '', corners = '1234'):
    
        k = self.k
        hp = self.h
        if(style=='F'):
            op='f'
        elif(style=='FD' or style=='DF'):
            op='B'
        else:
            op='S'
        myArc = 4/3 * (sqrt(2) - 1)
        self._out('%.2F %.2F m' % ((x+r)*k,(hp-y)*k))

        xc = x+w-r
        yc = y+r
        self._out('%.2F %.2F l' % (xc*k,(hp-y)*k))
        if '2' not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k,(hp-y)*k))
        else:
            self._arc(xc + r*myArc, yc - r, xc + r, yc - r*myArc, xc + r, yc)

        xc = x+w-r
        yc = y+h-r
        self._out('%.2F %.2F l' % ((x+w)*k,(hp-yc)*k))
        if '3' not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k,(hp-(y+h))*k))
        else:
            self._arc(xc + r, yc + r*myArc, xc + r*myArc, yc + r, xc, yc + r)

        xc = x+r
        yc = y+h-r
        self._out('%.2F %.2F l' % (xc*k,(hp-(y+h))*k))
        if '4' not in corners:
            self._out('%.2F %.2F l' % (x*k,(hp-(y+h))*k))
        else:
            self._arc(xc - r*myArc, yc + r, xc - r, yc + r*myArc, xc - r, yc)

        xc = x+r 
        yc = y+r
        self._out('%.2F %.2F l' % (x*k,(hp-yc)*k))
        if '1' not in corners:
            self._out('%.2F %.2F l' % (x*k,(hp-y)*k))
            self._out('%.2F %.2F l' % ((x+r)*k,(hp-y)*k))
        else:
            self._arc(xc - r, yc - r*myArc, xc - r*myArc, yc - r, xc, yc - r)
        self._out(op)
    
    def _arc(self, x1, y1, x2, y2, x3, y3):
    
        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c ' % (x1*self.k, (h-y1)*self.k,
            x2*self.k, (h-y2)*self.k, x3*self.k, (h-y3)*self.k))
        
    def sector(self, xc, yc, r, a, b, style='FD', cw=True, o=90):
    
        d0 = a - b
        if cw:
            d = b
            b = o - a
            a = o - d
        else:
            b += o
            a += o
        
        while a<0:
            a += 360
        while a>360:
            a -= 360
        while b<0:
            b += 360
        while b>360:
            b -= 360
        if a > b:
            b += 360
        b = b/360*2*pi
        a = a/360*2*pi
        d = b - a
        if d == 0 and d0 != 0:
            d = 2*pi
        k = self.k
        hp = self.h
        if sin(d/2):
            myArc = 4/3*(1-cos(d/2))/sin(d/2)*r
        else:
            myArc = 0
        #first put the center
        self._out('%.2F %.2F m' % ((xc)*k,(hp-yc)*k))
        #put the first point
        self._out('%.2F %.2F l' % ((xc+r*cos(a))*k,((hp-(yc-r*sin(a)))*k)))
        #draw the arc
        if d < pi/2:
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
        else:
            b = a + d/4
            myArc = 4/3*(1-cos(d/8))/sin(d/8)*r
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
           
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
        
        #terminate drawing
        if style=='F':
            op='f'
        elif style=='FD' or style=='DF':
            op='b'
        else:
            op='s'
        self._out(op)
    
    def sector_arc(self, x1, y1, x2, y2, x3, y3 ):
    
        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c' %
            (x1*self.k,
            (h-y1)*self.k,
            x2*self.k,
            (h-y2)*self.k,
            x3*self.k,
            (h-y3)*self.k))
 
    def set_alpha(self, alpha, bm='Normal'):
        state = {
            'ca': alpha,
            'CA': alpha,
            'BM': '/' + bm
        }
        self.ext_gstates.append(state)
        self._set_ext_gstate(len(self.ext_gstates))

    def _set_ext_gstate(self, gstate_index):
        self._out(sprintf('/GS%d gs', gstate_index))

    def _enddoc(self):
        if len(self.ext_gstates) > 0 and self.pdf_version < '1.4':
            self.pdf_version = '1.4'
        super(PDF, self)._enddoc()

    def _putextgstates(self):
        for gstate in self.ext_gstates:
            self._newobj()
            gstate['n'] = self.n
            self._out('<</Type /ExtGState')
            self._out(sprintf('/ca %.3F', gstate['ca']))
            self._out(sprintf('/CA %.3F', gstate['CA']))
            self._out('/BM ' + gstate['BM'])
            self._out('>>')
            self._out('endobj')

    def _putresourcedict(self):
        super(PDF, self)._putresourcedict()
        self._out('/ExtGState <<')
        for index, gstate in enumerate(self.ext_gstates):
            self._out('/GS' + str(index+1) + ' ' + str(gstate['n']) +' 0 R')
        self._out('>>')

    def _putresources(self):
        self._putextgstates()
        super(PDF, self)._putresources()

def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor
    
def transformar(dato):
    dato = str(dato)
    # dato = dato.replace("datetime.time(",  " '")
    dato = dato.replace("?",  ' ')
    dato = dato.replace("#",  ' ')
    dato = dato.replace("/",  ' ')
    dato = dato.replace("*",  ' ')
    dato = dato.replace(",",  ',')
    # dato = dato.replace("datetime.datetime(", " '")
    dato = dato.replace("),",  "',")
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
def transformar_cedula(dato):
    dato = str(dato)
    # dato = dato.replace("datetime.time(",  " '")
    dato = dato.replace("?",  ' ')
    dato = dato.replace("#",  ' ')
    dato = dato.replace("/",  ' ')
    dato = dato.replace("*",  ' ')
    dato = dato.replace(",",  ',')
    dato = dato.replace(".",  '')
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

def mes(date):
    months = ("ENE", "FEB", "MAR", "ABR", "MAY", "JUN", "JUL", "AGO", "SEP", "OCT", "NOV", "DIC")

    if date == "01" or date == 1:
        return months[0]
    
    if date == "02" or date == 2:
        return months[1]
    
    if date == "03" or date == 3:
        return months[2]
    
    if date == "04" or date == 4:
        return months[3]
    
    if date == "05" or date == 5:
        return months[4]
        
    if date == "06" or date == 6:
        return months[5]
        
    if date == "07" or date == 7:
        return months[6]
        
    if date == "08" or date == 8:
        return months[7]
        
    if date == "09" or date == 9:
        return months[8]
        
    if date == "10" or date == 10:
        return months[9]
        
    if date == "11" or date == 11:
        return months[10]
        
    if date == "12" or date == 12:
        return months[11]
    
    
def fecha(fecha):
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    dia_inicial = str(fecha_dt.strftime('%d'))
    mes_inicial = str(fecha_dt.strftime('%m'))
    año_inicial = str(fecha_dt.strftime('%Y'))
    mes_inicial_d = str(mes(mes_inicial))

    return[dia_inicial,mes_inicial_d,año_inicial, mes_inicial]



def editar_personal_afectado(datos):

    id = datos["id"]
    grd = datos["grd"]
    apellidos_nombres = datos["apellidos_nombres"]
    cc = datos["cedula"]
    afectacion = datos["afectacion"]
    estado_civil = datos["estado_civil"]
    tiempo_servicio = datos["tiempo_servicio"]
    situacion_actual = datos["situacion_actual"]
    familiares = datos["familiares"]
    coordinador = datos["coordinador"]


    grd = transformar(grd)
    apellidos_nombres = transformar(apellidos_nombres)
    cc = transformar(cc)
    afectacion = transformar(afectacion)
    estado_civil = transformar(estado_civil)
    tiempo_servicio = transformar(tiempo_servicio)
    situacion_actual = transformar(situacion_actual)
    familiares = transformar(familiares)
    coordinador = transformar(coordinador)

    grd =grd.upper()
    apellidos_nombres =apellidos_nombres.upper()
    cc =cc.upper()
    afectacion =afectacion.upper()
    estado_civil =estado_civil.upper()
    tiempo_servicio =tiempo_servicio.upper()
    situacion_actual =situacion_actual.upper()
    familiares =familiares.upper()
    coordinador =coordinador.upper()
   
    query="""UPDATE registro_afectacion set  grd = '{}', apellidos_nombres = '{}', cc= '{}', afectacion= '{}', estado_civil= '{}', tiempo_servicio= '{}', situacion_actual= '{}', familiares= '{}', coordinador= '{}' where id = {} """.format(grd, apellidos_nombres, cc, afectacion, estado_civil, tiempo_servicio, situacion_actual, familiares, coordinador, id)


    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def eeliminar_afectacion_evento_relavante(datos):

    #datos
    
    id = datos["id"]
     
    query="""DELETE FROM  registro_afectacion  where id = {} """.format( id)



    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def eeliminar_bitacora_evento_relavante(datos):

    #datos

    id = datos["id"]
     
    query="""DELETE FROM  bitacora  where id = {} """.format( id)



    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def editar_bitacora_evento_relavante(datos):

    #datos
    hora_evento = datos["hora_evento"]
    evento = datos["evento"]
    fecha_evento = datos["fecha_evento"]

    id = datos["id"]

    evento = transformar(evento)
    evento = evento.upper()
    hora_evento = hora_evento.upper()
   
     
    query="""UPDATE bitacora set  fecha_evento = '{}', hora_evento = '{}', evento= '{}' where id = {} """.format(fecha_evento, hora_evento, evento, id)


    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close


def ingreso_bitacora_evento_relavante(datos):

    #datos

    hora_evento = datos["hora_evento"]
    evento = datos["evento"]
    id_evento = datos["id_evento"]
    fecha_evento = datos["fecha_evento"]

    
        
    evento = evento.upper()
    evento = transformar(evento)
    hora_evento = hora_evento.upper()
    evento = evento.upper()
    
   
     
    dato="""('{}', '{}', '{}', '{}')""".format(id_evento, fecha_evento, hora_evento, evento)

    
    query="insert into bitacora (id_evento, fecha_evento, hora_evento, evento) values"+dato

    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



def elimnar_asignacion(datos):

    #datos

    
    id_eliminar =  datos["id"]
    
    conn = connect()
    cursor = conn.cursor()
    query_eliminar = "delete from medallas where id = '{}' ".format(id_eliminar)
    cursor.execute(query_eliminar)
    conn.commit()

    conn.close()
    cursor.close
    


def ingreso_evento_relavante(datos):

    #datos

    fecha_evento = datos["fecha_evento"]
    hora_evento = datos["hora_evento"]
    fecha_m = fecha(fecha_evento)
    
    divi_padre = datos["divi_padre"]
    divi_hija = datos["divi_hija"]
    brigada = datos["brigada"]
    batallon = datos["batallon"]
    cp = datos["cp"]
    pel = datos["pel"]
    departamento = datos["departamento"]
    municipio = datos["municipio"]
    sitio = datos["sitio"]
    latitud = datos["latitud"]
    gr_n = datos["gr_n"]
    m_n = datos["m_n"]
    s_n = datos["s_n"]
    longitud = datos["longitud"]
    gr_l = datos["gr_l"]
    m_l = datos["m_l"]
    s_l = datos["s_l"]
    enemigo = datos["enemigo"]
    estructura =datos["estructura"]
    hecho = datos["hecho"]
    resumen = datos["resumen"]
    tipo_evento = datos["tipo_evento"]


    divi_padre = transformar(divi_padre)
    divi_hija = transformar(divi_hija)
    brigada = transformar(brigada)
    batallon = transformar(batallon)
    cp = transformar(cp)
    pel = transformar(pel)
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
    enemigo = transformar(enemigo)
    estructura= transformar(estructura)
    hecho = transformar(hecho)
    resumen = transformar(resumen)
    tipo_evento = transformar(tipo_evento)
    
    
    fecha_evento = fecha_evento.upper()
    hora_evento = hora_evento.upper()
    divi_padre = divi_padre.upper()
    divi_hija = divi_hija.upper()
    brigada = brigada.upper()
    batallon = batallon.upper()
    cp = cp.upper()
    pel = pel.upper()
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
    enemigo = enemigo.upper()
    estructura = estructura.upper()
    hecho = hecho.upper()
    resumen = resumen.upper()
    tipo_evento = tipo_evento.upper()

    if tipo_evento == "POSITIVO":

        
        color = "verde_bg"
        color_titulo ="crema"
    else:
        color = "rojo_bg"
        color_titulo ="rojo"

    estado = "SIN CARGAR"

    

    if latitud =="LN":
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))*1
    else:
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))*-1

    if longitud=="LW":

        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*-1
    else:
        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*1




    hora_evento_f = datetime.strptime(hora_evento, "%H:%M")
    hora = str(hora_evento_f.strftime('%H'))
    minutos = str(hora_evento_f.strftime('%M'))

    hora_evento_militar = hora +":" +minutos

    fecha_hora_militar =str(fecha_m[0])+str(hora_evento_militar)+str(fecha_m[1])+str(fecha_m[2])


    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, cp, pel, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, enemigo, estructura, hecho, resumen, estado, tipo_evento, color, fecha_hora_militar, color_titulo, coordenadas_x, coordenadas_y)

    
    query="insert into registro_eventos_relevantes (fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, cp, pel, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, enemigo, estructura, hecho, resumen, estado, tipo_evento, color, fecha_hora_militar, color_titulo, x, y) values"+dato

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close


def cargar_documento_evento_relavante(datos, acta_alerta_nombres):

    #datos
    
    id = datos["id"]
    tipo_documneto = datos["tipo_documneto"]

    acta_alerta_nombres = str(acta_alerta_nombres).replace(" ","_")
    if acta_alerta_nombres != "validar":
        if tipo_documneto == "MANIOBRA":
            documento = "/eventos_relevantes/maniobra/"+str(id)+"_"+acta_alerta_nombres
            documento_where = "documento_maniobra = '{}'".format(documento)
        elif tipo_documneto == "AFECTACIONES":
            documento = "/eventos_relevantes/afectaciones/"+str(id)+"_"+acta_alerta_nombres
            documento_where = "documento_lamina_afectaciones = '{}'".format(documento)
        elif tipo_documneto == "OTROS DOCUMENTOS":
            documento = "/eventos_relevantes/otros/"+str(id)+"_"+acta_alerta_nombres
            documento_where = "documento_otros = '{}'".format(documento)
    else:
        documento = "----"
        documento_where = "documento_otros = '{}'".format(documento)

    
    query=" UPDATE  registro_eventos_relevantes SET {} where id  = '{}' ".format(documento_where, id)

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close
    return [documento]


def editar_evento_relavante(datos):

    #datos

    fecha_evento = datos["fecha_evento"]
    hora_evento = datos["hora_evento"]
    fecha_m = fecha(fecha_evento)
    
    divi_padre = datos["divi_padre"]
    divi_hija = datos["divi_hija"]
    brigada = datos["brigada"]
    batallon = datos["batallon"]
    cp = datos["cp"]
    pel = datos["pel"]
    departamento = datos["departamento"]
    municipio = datos["municipio"]
    sitio = datos["sitio"]
    latitud = datos["latitud"]
    gr_n = datos["gr_n"]
    m_n = datos["m_n"]
    s_n = datos["s_n"]
    longitud = datos["longitud"]
    gr_l = datos["gr_l"]
    m_l = datos["m_l"]
    s_l = datos["s_l"]
    enemigo = datos["enemigo"]
    estructura =datos["estructura"]
    hecho = datos["hecho"]
    resumen = datos["resumen"]
    tipo_evento = datos["tipo_evento"]
    estado = datos["estado"]
    id = datos["id"]


    divi_padre = transformar(divi_padre)
    divi_hija = transformar(divi_hija)
    brigada = transformar(brigada)
    batallon = transformar(batallon)
    cp = transformar(cp)
    pel = transformar(pel)
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
    enemigo = transformar(enemigo)
    estructura= transformar(estructura)
    hecho = transformar(hecho)
    resumen = transformar(resumen)
    tipo_evento = transformar(tipo_evento)
    estado = transformar(estado)
    
    
    fecha_evento = fecha_evento.upper()
    hora_evento = hora_evento.upper()
    divi_padre = divi_padre.upper()
    divi_hija = divi_hija.upper()
    brigada = brigada.upper()
    batallon = batallon.upper()
    cp = cp.upper()
    pel = pel.upper()
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
    enemigo = enemigo.upper()
    estructura = estructura.upper()
    hecho = hecho.upper()
    resumen = resumen.upper()
    tipo_evento = tipo_evento.upper()
    estado = estado.upper()

    if tipo_evento == "POSITIVO":

        
        color = "verde_bg"
        color_titulo ="crema"
    else:
        color = "rojo_bg"
        color_titulo ="rojo"


    if latitud =="LN":
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))*1
    else:
        coordenadas_x= ((int(gr_n)+int(m_n)/60)+(float(s_n)/3600))*-1

    if longitud=="LW":

        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*-1
    else:
        coordenadas_y= ((int(gr_l)+int(m_l)/60)+(float(s_l)/3600))*1




    fecha_hora_militar =str(fecha_m[0])+str(hora_evento)+str(fecha_m[1])+str(fecha_m[2])


    query=" UPDATE  registro_eventos_relevantes SET fecha_evento = '{}', hora_evento = '{}', divi_padre = '{}', divi_hija = '{}', brigada = '{}', batallon = '{}', cp = '{}', pel = '{}', departamento = '{}', municipio = '{}', sitio = '{}', latitud = '{}', gr_n = '{}', m_n = '{}', s_n = '{}', longitud = '{}', gr_l = '{}', m_l = '{}', s_l = '{}', enemigo = '{}', estructura = '{}', hecho = '{}', resumen = '{}', estado = '{}', tipo_evento = '{}', color = '{}', fecha_hora_militar = '{}', color_titulo = '{}', x = '{}', y = '{}' where id  = '{}' ".format(fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, cp, pel, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, enemigo, estructura, hecho, resumen, estado, tipo_evento, color, fecha_hora_militar, color_titulo, coordenadas_x, coordenadas_y, id)

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close


def listado_eventos(datos):

    #datos
    fecha_evento =  datos["fecha_evento"]
    fecha_evento_final =  datos["fecha_evento_final"]
    tipo_evento =  datos["tipo_evento"]
    departamento =datos["departamento"]
   
    conn = connect()
    cursor = conn.cursor()
  
    fechas=""
    if fecha_evento and fecha_evento_final:
        filtro_fecha = "where fecha_evento >= '{}'  AND fecha_evento <= '{}'".format(fecha_evento, fecha_evento_final,)
        fechas=""
    else:
        filtro_fecha = ""
        fechas="1"
    
    if tipo_evento !="null" and tipo_evento !="---" and tipo_evento !="":
        if fechas =="":
            filtro = "and tipo_evento = '{}'".format(tipo_evento)
        elif fechas=="1":
            filtro = "where tipo_evento = '{}'".format(tipo_evento)
    else:
        filtro =""

    if departamento !="null" and departamento !="---" and departamento !="":

        if fechas =="":
            filtro_departamento = "and departamento = '{}'".format(departamento)
        elif fechas=="1":
            filtro_departamento = "where departamento = '{}'".format(departamento)
    else:
        filtro_departamento =""


    query="select * from registro_eventos_relevantes  {} {} {}  order by fecha_evento asc, hora_evento asc".format(filtro_fecha, filtro, filtro_departamento)

    cursor.execute(query)
    data = cursor.fetchall()

    unidades = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","DAVAA","DIVFE","FUTCO","FTCEC","FUTOM","TREJC","JEMGF","JEMOP","JEMPP" , "-"]
    data = sorted(data, key = lambda m: unidades.index(m[3]))
    
    conn.commit()
    conn.close()
    cursor.close

    return[data]


def buscar(datos):


    #print(permiso)
    id_evento = datos["id_evento"]

    

    conn = connect()
    cursor = conn.cursor()
    query="select * from bitacora where id_evento = '{}' order by fecha_evento, hora_evento asc".format(id_evento)
    cursor.execute(query)
    data = cursor.fetchall()

    query_2="select * from registro_afectacion where id_evento = '{}'".format(id_evento)
    cursor.execute(query_2)
    data_2 = cursor.fetchall()
        
    GRD = ["GR","MG","BG","CR","TC","MY","CT","TE","ST","SMC","SM","SP","SV", "SS", "CP","CS","C3", "DGSLP","SLP","SL18","SL12","----",]
    data_2 = sorted(data_2, key = lambda m: GRD.index(m[2]))

    query_3="select DISTINCT grd, apellidos_nombres  from registro_afectacion where id_evento = '{}'".format(id_evento)
    cursor.execute(query_3)
    data_3 = cursor.fetchall()
    
    GRD = ["GR","MG","BG","CR","TC","MY","CT","TE","ST","SMC","SM","SP","SV", "SS", "CP","CS","C3", "DGSLP","SLP","SL18","SL12","----",]
    data_3 = sorted(data_3, key = lambda m: GRD.index(m[0]))


    conn.commit()
    conn.close()
    cursor.close



    return [data, data_2, data_3]

    
def ingresar_afectacion(datos):

    grd = datos["grd"]
    apellidos_nombres = datos["apellidos_nombres"]
    afectacion = datos["afectacion"]
    id_evento = datos["id_evento"]

    grd = transformar(grd)
    apellidos_nombres = transformar(apellidos_nombres)
    afectacion = transformar(afectacion)

        
    grd = grd.upper()
    apellidos_nombres = apellidos_nombres.upper()
    afectacion = afectacion.upper()
    foto = "vacio"
     
    dato="""('{}', '{}', '{}', '{}', '{}')""".format(id_evento, grd, apellidos_nombres, afectacion, foto)

    
    query="insert into registro_afectacion (id_evento, grd, apellidos_nombres, afectacion, foto) values"+dato

    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



def buscar_2(datos):

    permiso =datos["unidad"]
   

    if permiso == "EJC":
        query="select * from asignacion_plazos  where respuesta = 'SI'  ORDER BY  fecha_plazo ASC"
    else:
        query="select * from asignacion_plazos where cargo LIKE '%{}%' AND respuesta = 'SI' ORDER BY  fecha_plazo ASC".format(permiso)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close
    #print(data)
    return [data]




def crear_plazo(datos):

    #datos

    nivel_orden = datos["nivel_orden"]
    unidad_que_genera = datos["unidad_que_genera"]
    clasificacion = datos["clasificacion"]
    orfeo = datos["orfeo"]
    orden_excel = datos["orden_excel"]
    doc_radicado = datos["doc_radicado"]
    fecha_orden = datos["fecha_orden"]
    asunto = datos["asunto"]
    orden = datos["orden"]
    obervaciones = datos["obervaciones"]

    nivel_orden = transformar(nivel_orden)
    unidad_que_genera = transformar(unidad_que_genera)
    clasificacion = transformar(clasificacion)
    orfeo = transformar(orfeo)
    doc_radicado = transformar(doc_radicado)
    fecha_orden = transformar(fecha_orden)
    asunto = transformar(asunto)
    orden = transformar(orden)
    obervaciones = transformar(obervaciones)
    orden_excel = transformar(orden_excel)

    

    nivel_orden = nivel_orden.upper()
    unidad_que_genera = unidad_que_genera.upper()
    clasificacion = clasificacion.upper()
    orfeo = orfeo.upper()
    doc_radicado = doc_radicado.upper()
    fecha_orden = fecha_orden.upper()
    asunto = asunto.upper()
    orden = orden.upper()
    obervaciones = obervaciones.upper()

    orden_excel = orden_excel.upper()


    ordenes=[nivel_orden, unidad_que_genera, clasificacion, orden_excel, orfeo,  doc_radicado, fecha_orden, asunto, orden, obervaciones]
    campos =["ORDEN EMITIDA POR:", "UNIDAD QUE GENERA LA ORDEN", "CLASIFICACIÓN", "ORDEN SEJEC", "ORFEO", "DOCUMENTO RAD", "FECHA PARA CUMPLIMINETO", "ASUNTO", "ORDEN", "OBSERVACIONES"]

    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(nivel_orden, unidad_que_genera, clasificacion, orden_excel, orfeo,  doc_radicado, fecha_orden, asunto, orden, obervaciones)

    query="insert into creacion_ordenes_directas (nivel_orden, unidad_que_genera, clasificacion, orden_excel, orfeo,  doc_radicado, fecha_orden, asunto, orden, obervaciones) values"+dato

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    nombre_doc = 0
    qyery_select = "select id from creacion_ordenes_directas where unidad_que_genera = '{}' and nivel_orden = '{}' and  fecha_orden = '{}' and  asunto = '{}'".format(unidad_que_genera, nivel_orden, fecha_orden, asunto)
    cursor.execute(qyery_select)
    data = cursor.fetchall()

    for x in data:
        nombre_doc = str(x[0]) +"_"+str(orfeo)


    query_DELETE ="DELETE FROM creacion_ordenes_directas"
    cursor.execute(query_DELETE)
    conn.commit()
    conn.close()
    cursor.close

    
    pdf = PDF(orientation = 'P', unit = 'mm', format='letter')


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)
    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.set_fill_color(210, 214, 209)
    pdf.rounded_rect(5, 5, 206, 270, 1,'D', '1234')
    
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)

    pdf.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
    pdf.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
    pdf.text(35,25,str("DIRECCIÓN DE OPERACIONES"))

    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/ejc.png",10,9,16,19)

    pdf.set_line_width(0.1)
    pdf.line(5, 30, 211, 30)
    pdf.set_font('BebasNeue', '', 12)
    pdf.text(7,35,str("LUGAR Y FECHA:"))
    pdf.set_font('BebasNeue', '', 10)
    dia = datetime.now().day
    mes = datetime.now().month
    anio = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    segun = datetime.now().second
    lugar_fecha  = str("Bogota - ")+str(dia)+" - " +str(mes)+" - " +str(anio) 
    pdf.text(30,35,lugar_fecha)
    hora = str(hour)+":" +str(minute)+":" +str(segun) 
    pdf.text(100,35,hora)
    pdf.set_font('BebasNeue', '', 12)

    radicado = "Radicado: "+nombre_doc
    pdf.text(120,35,radicado)

    pdf.line(5, 37, 211, 37)

    responsable = "ORDENES EMITIDAS POR EL MANDO SUPERIOR"
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(70,45,responsable)
    
    pdf.set_font('BebasNeue', '', 16)
    res_ponsable = "ORDEN EMITIDA POR: "
    pdf.text(7,55, res_ponsable)

    pdf.set_text_color(125,0,0)
    pdf.text(55,55, nivel_orden)

    pdf.line(5, 50, 211, 50)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(55)
    pdf.cell(200,7,"ORDEN EMITIDA",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)

    #bucle para crear cuadro e ordenes
    numero=0
    for x in ordenes:
        campos
        if x !="":
            y = pdf.get_y()
            pdf.multi_cell(50, 5, str(campos[numero]), 1, "L", False)
            x = pdf.get_y()
            z = (x-y)
            pdf.ln(-z)
            
            pdf.cell(50)
            pdf.multi_cell(150, 5, str(ordenes[numero]), 1, "J", False)
    
            #pdf.ln(-5)
            numero = numero +1
        else:
            numero = numero +1


    
    pdf.line(5, 255, 211, 255)

    pdf.set_font('BebasNeue', '', 12)
    #pdf.text(10,265,"TC. JULIAN PRIETO")
    pdf.set_font('BebasNeue', '', 10)
    pdf.text(10,270,"DireCción de Operaciones del Ejército (DIROP)")

 
    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos_qr/"
    import qrcode
    
    inf_qur = "ORFEO:"+nombre_doc+" \n FECHA DE CUMPLIMIENTO "+fecha_orden + "\n QUIEN EMITE LA ORDEN "+nivel_orden
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    nivel_orden = nivel_orden.replace(" ", "_")
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/creacion_plazos_documentos/"
    direcion = dirercion_archvios+str(nombre_doc)+"_"+nivel_orden+'.pdf'
    pdf.output(direcion, 'F')
 

