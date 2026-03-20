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

#-----------------------------------------
#------------BOLETIN OPERACIONAL-----------
#-----------------------------------------

def registro_boletin_operacional(datos):

    #datos

    numero_boletin = datos["numero_boletin"]
    fecha_ori = datos["fecha"]
    fecha_m = fecha(fecha_ori)
    
    grado_ofi = datos["grado_ofi"]
    apellidos_nombres_ofi = datos["apellidos_nombres_ofi"]
    grado_sub = datos["grado_sub"]
    apellidos_nombres_sub = datos["apellidos_nombres_sub"]



    numero_boletin = transformar(numero_boletin)
    grado_ofi = transformar(grado_ofi)
    apellidos_nombres_ofi = transformar(apellidos_nombres_ofi)
    grado_sub = transformar(grado_sub)
    apellidos_nombres_sub = transformar(apellidos_nombres_sub)

    
    
    numero_boletin = numero_boletin.upper()
    grado_ofi = grado_ofi.upper()
    apellidos_nombres_ofi = apellidos_nombres_ofi.upper()
    grado_sub = grado_sub.upper()
    apellidos_nombres_sub = apellidos_nombres_sub.upper()


    dato="""('{}', '{}', '{}', '{}', '{}', '{}')""".format(numero_boletin, fecha_ori, grado_ofi, apellidos_nombres_ofi, grado_sub, apellidos_nombres_sub)

    
    query="insert into BOLETIN_COE (numero_boletin, fecha, grado_ofi, apellidos_nombres_ofi, grado_sub, apellidos_nombres_sub) values"+dato

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def editar_boletin_operacional(datos):

    #datos
    id = datos["id"]
    numero_boletin = datos["numero_boletin"]
    fecha_ori = datos["fecha"]
    fecha_m = fecha(fecha_ori)
    
    grado_ofi = datos["grado_ofi"]
    apellidos_nombres_ofi = datos["apellidos_nombres_ofi"]
    grado_sub = datos["grado_sub"]
    apellidos_nombres_sub = datos["apellidos_nombres_sub"]



    numero_boletin = transformar(numero_boletin)
    grado_ofi = transformar(grado_ofi)
    apellidos_nombres_ofi = transformar(apellidos_nombres_ofi)
    grado_sub = transformar(grado_sub)
    apellidos_nombres_sub = transformar(apellidos_nombres_sub)

    
    
    numero_boletin = numero_boletin.upper()
    grado_ofi = grado_ofi.upper()
    apellidos_nombres_ofi = apellidos_nombres_ofi.upper()
    grado_sub = grado_sub.upper()
    apellidos_nombres_sub = apellidos_nombres_sub.upper()


    query=" UPDATE  BOLETIN_COE SET numero_boletin = '{}', fecha = '{}', grado_ofi = '{}', apellidos_nombres_ofi = '{}', grado_sub = '{}', apellidos_nombres_sub = '{}' where id  = '{}' ".format(numero_boletin, fecha_ori, grado_ofi, apellidos_nombres_ofi, grado_sub, apellidos_nombres_sub, id)

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def eliminar_boletin_operacional(datos):

    #datos

    id = datos["id"]
     
    query="""DELETE FROM  BOLETIN_COE  where id = {} """.format( id)



    conn = connect()
    cursor = conn.cursor()

    #print(query)
    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close

def listado_registro_boletines(datos):

   
    conn = connect()
    cursor = conn.cursor()


    query="select * from BOLETIN_COE  order by numero_boletin desc"

    cursor.execute(query)
    data = cursor.fetchall()
    
    query_2="select * from resultado_boletin_registrar  order by resultado asc"

    cursor.execute(query_2)
    data_2 = cursor.fetchall()

        
    query_3="select * from hechos_resultados  order by hechos asc"

    cursor.execute(query_3)
    data_3 = cursor.fetchall()

    #unidades = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","DAVAA","DIVFE","FUTCO","FTCEC","TREJC", "-"]
    #data = sorted(data, key = lambda m: unidades.index(m[3]))
    
    conn.commit()
    conn.close()
    cursor.close

    return[data, data_2, data_3]

#-----------------------------------------
#---ANOTACIONES BOLETIN OPERACINAL--------
#-----------------------------------------

def ingreso_anotacion_operacional(datos):

    #datos
    boletin = datos["boletin"]
    fecha_evento = datos["fecha_evento"]
    hora_evento = datos["hora_evento"]
    fecha_m = fecha(fecha_evento)
    estado= datos["estado"] 
    divi_padre = datos["divi_padre"]
    divi_hija = datos["divi_hija"]
    brigada = datos["brigada"]
    batallon = datos["batallon"]

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
    hecho_nuevo = datos["hecho_nuevo"]
    resumen = datos["resumen"]
    tipo_evento = datos["tipo_evento"]

    resultado_reistrar = datos["resultado_reistrar"]
    resultado_reistrar_nuevo = datos["resultado_reistrar_nuevo"]

    resultado_reistrar=resultado_reistrar.split(",")
    resultado_reistrar_nuevo=resultado_reistrar_nuevo.split(",")

    boletin = transformar(boletin)
    divi_padre = transformar(divi_padre)
    divi_hija = transformar(divi_hija)
    brigada = transformar(brigada)
    batallon = transformar(batallon)

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
    hecho_nuevo  = transformar(hecho_nuevo)
    resumen = transformar(resumen)
    tipo_evento = transformar(tipo_evento)
    
    boletin = boletin.upper()
    fecha_evento = fecha_evento.upper()
    hora_evento = hora_evento.upper()
    divi_padre = divi_padre.upper()
    divi_hija = divi_hija.upper()
    brigada = brigada.upper()
    batallon = batallon.upper()

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
    hecho_nuevo  = hecho_nuevo.upper()
    resumen = resumen.upper()
    tipo_evento = tipo_evento.upper()

    if tipo_evento == "POSITIVO":

        color = "verde_bg"
        color_titulo ="crema"
    else:
        color = "rojo_bg"
        color_titulo ="rojo"

    if hecho_nuevo != "null" and hecho_nuevo != "UNDEFINED":
        hecho = hecho_nuevo
    else:
        hecho = hecho

    
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

    dato="""('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}',  '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(boletin, fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, enemigo, estructura, hecho, resumen, estado, tipo_evento, color, fecha_hora_militar, color_titulo, coordenadas_x, coordenadas_y)
    query="insert into ANOTACIONES_BOLETIN_OPERACIONAL (boletin, fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, enemigo, estructura, hecho, resumen, estado, tipo_evento, color, fecha_hora_militar, color_titulo, x, y) values"+dato

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    numero = 1
    numero_a =0
    indice = len(resultado_reistrar)
    query_res_2 = ""
    for x in resultado_reistrar:
        res = str(resultado_reistrar[numero_a]).upper()
        can = str(resultado_reistrar[numero]).upper()
        query_res = "('"+boletin+"', '"+fecha_evento+"', '"+str(res)+"', '"+str(can)+"')"
        if query_res_2 !="":
            query_res_2 =  query_res_2 +","+query_res
        else:
            query_res_2 = query_res

        if numero < indice-1:
            numero = numero +2
            numero_a = numero_a +2
        else:
            break


    query_2="insert into resultado_boletin (boletin, fecha_resultado, resultado, cantidad_resultado) values "+query_res_2
    cursor.execute(query_2)
    conn.commit()
   

    if resultado_reistrar_nuevo[0] != "":
        numero = 1
        numero_a =0
        indice = len(resultado_reistrar_nuevo)
        query_res_3 = ""
        for x in resultado_reistrar_nuevo:
            res = str(resultado_reistrar_nuevo[numero_a]).upper()
            query_res = "('"+str(res)+"')"

            if query_res_3 !="":
                query_res_3 =  query_res_3 +","+query_res
            else:
                query_res_3 = query_res

            if numero_a < indice-1:
                numero_a = numero_a +1
            else:
                break

        query_3="insert into resultado_boletin_registrar (resultado) values "+query_res_3
        cursor.execute(query_3)
        conn.commit()

    if hecho_nuevo != "null"  and hecho_nuevo != "UNDEFINED":
        dato="""('{}')""".format(hecho_nuevo)
        query_4="insert into hechos_resultados (hechos) values "+dato
        cursor.execute(query_4)
        conn.commit()

    conn.close()
    cursor.close


def anotaciones_registro_boletines(datos):


    fecha_evento =datos["fecha_evento"]
    fecha_evento_final =datos["fecha_evento_final"]
    boletin =datos["boletin"]

    conn = connect()
    cursor = conn.cursor()

    fechas=""
    
    if  fecha_evento  != "null" and fecha_evento_final !="null":
        filtro_fecha = "where fecha_evento >= '{}'  AND fecha_evento <= '{}'".format(fecha_evento, fecha_evento_final)
        fechas=""
    else:
        filtro_fecha = ""
        fechas="1"
    if boletin !="null" and boletin:

        if fechas =="":
            filtro = "and boletin = '{}'".format(boletin)
        elif fechas=="1":
            filtro = "where boletin = '{}'".format(boletin)
    else:
        filtro =""
    

    query="select * from ANOTACIONES_BOLETIN_OPERACIONAL {} {} order by boletin desc".format(filtro_fecha, filtro)
    print(fecha_evento)
    cursor.execute(query)
    data = cursor.fetchall()

    #unidades = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","DAVAA","DIVFE","FUTCO","FTCEC","TREJC", "-"]
    #data = sorted(data, key = lambda m: unidades.index(m[3]))
    
    conn.commit()
    conn.close()
    cursor.close

    return[data]

