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
    


def actulizar_informacion_estado_medalla(datos):

    #datos
    proyecto_difab_estado =  datos["proyecto_difab_estado"]
    proyecto_estado_medalla =  datos["proyecto_estado_medalla"]

    proyecto_difab_estado = proyecto_difab_estado.upper()
    proyecto_estado_medalla = proyecto_estado_medalla.upper()

    query=" UPDATE  medallas SET  estado_medalla = '{}' WHERE proyecto = '{}' ".format(proyecto_estado_medalla, proyecto_difab_estado)
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



def actulizar_informacion_medallas(datos):

    #datos
    id = datos["id"]
    grd_persona = datos["grd_persona"]
    arma_persona = datos["arma_persona"]
    cc_nombre_persona = datos["cc_nombre_persona"]
    nombre_persona_2 = datos["nombre_persona_2"]
    fecha_ingreso = datos["fecha_ingreso"]
    proyecto_estado_medalla = datos["proyecto_estado_medalla"]
    fecha_resolucion = datos["fecha_resolucion"]
    resolucion = datos["resolucion"]
    decreto = datos["decreto"]
    observaciones = datos["observaciones"]

    grd_persona = transformar(grd_persona)
    arma_persona = transformar(arma_persona)
    cc_nombre_persona = transformar_cedula(cc_nombre_persona)
    nombre_persona_2 = transformar(nombre_persona_2)
    fecha_ingreso = transformar(fecha_ingreso)
    proyecto_estado_medalla = transformar(proyecto_estado_medalla)
    fecha_resolucion = transformar(fecha_resolucion)
    resolucion = transformar(resolucion)
    decreto = transformar(decreto)
    observaciones = transformar(observaciones)

    grd_persona = grd_persona.upper()
    arma_persona = arma_persona.upper()

    nombre_persona_2 = nombre_persona_2.upper()
    fecha_ingreso = fecha_ingreso.upper()
    proyecto_estado_medalla = proyecto_estado_medalla.upper()
    fecha_resolucion = fecha_resolucion.upper()
    resolucion = resolucion.upper()
    decreto = decreto.upper()
    observaciones = observaciones.upper()
    
    query=" UPDATE  medallas SET  grd ='{}', arma ='{}', cedula ='{}', nombre_apellido ='{}', enrega_medalla_difab ='{}', estado_medalla ='{}', resolucion ='{}', decreto ='{}', fecha_resolucion ='{}', observaciones ='{}' WHERE id = '{}' ".format(grd_persona, arma_persona, cc_nombre_persona, nombre_persona_2, fecha_ingreso, proyecto_estado_medalla, resolucion, decreto, fecha_resolucion, observaciones, id)
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close





def actulizar_informacion_difab(datos):

    #datos

    proyecto_difab =  datos["proyecto_difab"]
    enrega_medalla_difab =  datos["enrega_medalla_difab"]
    estado_medalla =  "EN DIFAB - DINEG"
 
    proyecto_difab = proyecto_difab.upper()
    enrega_medalla_difab = enrega_medalla_difab.upper()


    query=" UPDATE  medallas SET  enrega_medalla_difab = '{}', estado_medalla = '{}' WHERE proyecto = '{}' ".format(enrega_medalla_difab, estado_medalla, proyecto_difab)
    print(query)
    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



def listado(datos):

    #datos


    proyecto =  datos["proyecto_registro"]
 
    
    proyecto = proyecto.upper()

    dato="""('{}')""".format(proyecto)

    query="insert into proyecto (proyecto) values"+dato

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    query = "select * from proyecto"
    cursor.execute(query)
    data = cursor.fetchall()

    conn.close()
    cursor.close

    return [data]

def guardar_medalla(datos):

    #datos
    recibidad_por =  datos["recibidad_por"]
    medalla =  datos["medalla"]
    fecha_ingreso =  datos["fecha_ingreso"]
    fecha_mes =  datos["fecha_mes"]
    oficio =  datos["oficio"]
    radicado =  datos["radicado"]
    batallon =  datos["batallon"]
    brigada =  datos["brigada"]
    division =  datos["division"]
    grd =  datos["grd"]
    arma =  datos["arma"]
    cedula =  datos["cedula"]
    nombre_apellido =  datos["nombre_apellido"]
    categoria =  datos["categoria"]
    operacion =  datos["operacion"]
    motivo =  datos["motivo"]
    fecha_hecho =  datos["fecha_hecho"]
    fecha_hecho_final =  datos["fecha_hecho_final"]
    departamento =  datos["departamento"]
    municipio =  datos["municipio"]
    veredad =  datos["veredad"]
    amenaza =  datos["amenaza"]
    resumen =  datos["resumen"]
    proyecto =  datos["proyecto"]

    como =  datos["como"]
    area_de_responsabilidad =  datos["area_de_responsabilidad"]

    


    recibidad_por = recibidad_por.upper()
    medalla = medalla.upper()
    fecha_ingreso = fecha_ingreso.upper()
    fecha_mes = fecha_mes.upper()
    oficio = oficio.upper()
    radicado = radicado.upper()
    batallon = batallon.upper()
    brigada = brigada.upper()
    division = division.upper()
    grd = grd.upper()
    arma = arma.upper()
    cedula = cedula.upper()
    nombre_apellido = nombre_apellido.upper()
    categoria = categoria.upper()
    operacion = operacion.upper()
    motivo = motivo.upper()
    fecha_hecho = fecha_hecho.upper()
    fecha_hecho_final = fecha_hecho_final.upper()
    departamento = departamento.upper()
    municipio = municipio.upper()
    veredad = veredad.upper()
    amenaza = amenaza.upper()
    resumen = resumen.upper()
    proyecto = proyecto.upper()

    como = como.upper()
    area_de_responsabilidad = area_de_responsabilidad.upper()

    recibidad_por = transformar(recibidad_por)
    medalla = transformar(medalla)
    fecha_ingreso = transformar(fecha_ingreso)
    fecha_mes = transformar(fecha_mes)
    oficio = transformar(oficio)
    radicado = transformar(radicado)
    batallon = transformar(batallon)
    brigada = transformar(brigada)
    division = transformar(division)
    grd = transformar(grd)
    arma = transformar(arma)
    cedula = transformar_cedula(cedula)
    nombre_apellido = transformar(nombre_apellido)
    categoria = transformar(categoria)
    operacion = transformar(operacion)
    motivo = transformar(motivo)
    fecha_hecho = transformar(fecha_hecho)
    fecha_hecho_final = transformar(fecha_hecho_final)
    departamento = transformar(departamento)
    municipio = transformar(municipio)
    veredad = transformar(veredad)
    amenaza = transformar(amenaza)
    resumen = transformar(resumen)
    proyecto = transformar(proyecto)

    como = transformar(como)
    area_de_responsabilidad = transformar(area_de_responsabilidad)

    estado_medalla = 'TRAMITE DIROP'


    dato="""('{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}', '{}')""".format(recibidad_por, medalla, fecha_ingreso, fecha_mes, oficio, radicado, batallon, brigada, division, grd, arma, cedula, nombre_apellido, categoria, operacion, motivo, fecha_hecho, fecha_hecho_final, departamento, municipio, veredad, amenaza, resumen, proyecto, como, area_de_responsabilidad, estado_medalla)

    query="insert into medallas (recibidad_por, medalla, fecha_ingreso, fecha_mes, oficio, radicado, batallon, brigada, division, grd, arma, cedula, nombre_apellido, categoria, operacion, motivo, fecha_hecho, fecha_hecho_final, departamento, municipio, veredad, amenaza, resumen, proyecto, como, area_de_responsabilidad, estado_medalla) values"+dato

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

    query="select radicado from medallas "
    cursor.execute(query)
    radicado = cursor.fetchall()


    conn.close()
    cursor.close

    if radicado:
        for x in radicado:
            radicado =  int(x[0])+1
    else:
        radicado = 1

    return [radicado]

def buscar(datos):


    #print(permiso)

    conn = connect()
    cursor = conn.cursor()
    query="select * from proyecto "
    cursor.execute(query)
    data = cursor.fetchall()

    query="select radicado from medallas order by id asc "
    cursor.execute(query)
    radicado = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close
    if radicado:
        for x in radicado:
            radicado =  int(x[0])+1
    else:
        radicado = 1


    return [data, radicado]

    


def listado_medallas(datos):


    #print(permiso)

    conn = connect()
    cursor = conn.cursor()
    query="select * from medallas order by id asc "
    cursor.execute(query)
    data = cursor.fetchall()

    query_proeyecto="select * from proyecto "
    cursor.execute(query_proeyecto)
    data_proyecto = cursor.fetchall()

    query_3="select DISTINCT division from medallas order by division asc "
    cursor.execute(query_3)
    data_3 = cursor.fetchall()

    query_4="select DISTINCT medalla from medallas order by medalla asc "
    cursor.execute(query_4)
    data_4 = cursor.fetchall()

    query_5="select DISTINCT estado_medalla from medallas order by estado_medalla asc "
    cursor.execute(query_5)
    data_5 = cursor.fetchall()


    conn.commit()
    conn.close()
    cursor.close



    return [data, data_proyecto, data_3, data_4, data_5]

    



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
 

