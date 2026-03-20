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
from PyPDF2 import PdfFileMerger, PdfFileReader

import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
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

def cimplimiento_plazo_respuesta(datos, cumplido_soporte_nombres):

    #datos

    id_eliminar =  datos["id"]
    observaciones =  datos["observaciones_respuesta"]
    funcionario =  datos["funcionario"]
    orfeo =  datos["orfeo"]
    
    observaciones =  observaciones.upper()

    conn = connect()
    cursor = conn.cursor()

    fecha_cumplimiento =  datetime.now()

    cumplio_respuesta = "SI"

    query = """UPDATE asignacion_plazos SET  cumplio_respuesta = '{}',  observaciones_respuesta =  '{}', fecha_plazo_respuesta_cumplido =  '{}' WHERE id = '{}';""".format(cumplio_respuesta,  observaciones, fecha_cumplimiento, id_eliminar )

    cursor.execute(query)
    conn.commit()


    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')

    nombre_documento=""
    if cumplido_soporte_nombres !="validar":
        listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
        error = ""
        for f in listaPdfs:
            nombre, ext = os.path.splitext(f)
            if ext != '.pdf':
                error =  "no pdf"
                nombre_archivo = nombre
        if error !=  "no pdf":
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_"+str(cumplido_soporte_nombres)
            nombre_actas_reserva = str("/plazos/respuestas/")+nombre_documento
            nombre_doc_soporte = cumplido_soporte_nombres
        else:
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_"+str(nombre_archivo)+".zip"
            nombre_actas_reserva = str("/plazos/respuestas/")+nombre_documento
            nombre_doc_soporte = nombre_archivo+".zip"

    else:
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_.pdf"
            nombre_actas_reserva = str("/plazos/respuestas/")+nombre_documento
            nombre_doc_soporte = nombre_documento


    query = """UPDATE asignacion_plazos SET dir_doc_plazo = '{}', cumplido_soporte_respuesta = '{}' WHERE id = '{}' ;""".format(nombre_actas_reserva, nombre_doc_soporte, id_eliminar)

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



   #documento_soporte_plazo_cumplido
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

    radicado = "Radicado: "+orfeo
    pdf.text(120,35,radicado)

    pdf.line(5, 37, 211, 37)

    responsable = "CUMPLIMIENTO A RESPUETAS EMITIDAS POR LAS UNIDADES"
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(50,45,responsable)
    
    pdf.set_font('BebasNeue', '', 16)
    res_ponsable = "ORDEN CUMPLIDA POR: " + funcionario
    pdf.text(7,55, res_ponsable)



    pdf.line(5, 50, 211, 50)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(55)
    pdf.cell(200,7,"ORDEN EMITIDA",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)

    #bucle para crear cuadro e ordenes
    numero=0
    

    ordenes = [cumplio_respuesta, observaciones]
    campos = ["CIMPLIMENTO", "OBSERVACIONES"]
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
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/"
    import qrcode
    
    inf_qur = "ORFEO:"+orfeo+" \n FECHA DE CUMPLIMIENTO "+lugar_fecha + "\n QUIEN CUMPLIO LA ORDEN "+funcionario
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/"
    direcion = dirercion_archvios+str("1_a_nota_cumplimiento.pdf")
    pdf.output(direcion, 'F')
 

    #Get number of pages


    try:
        #import os
        listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
        error = ""
        for f in listaPdfs:
            nombre, ext = os.path.splitext(f)
            if ext != '.pdf':
                error =  "no pdf"

        if error != "no pdf":
            merger = PdfFileMerger()
            if cumplido_soporte_nombres !="validar":
                documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
            else:
                nombre_documento = str(id_eliminar)+"respueta_a_orden_"+orfeo+"_"+responsable_as+"_doc_.pdf"
                documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
                
            for file in listaPdfs:
                
                #print(file)
                merger.append(PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file))
            merger.write(documento_guardado)

            if cumplido_soporte_nombres !="validar":
                documento_eliminar = [cumplido_soporte_nombres, "1_a_nota_cumplimiento.pdf" ]
            else:
                documento_eliminar = ["1_a_nota_cumplimiento.pdf" ]

            for doc in documento_eliminar:
                path = os.path.join('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/', doc)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
        else:
            
            from zipfile import ZipFile
            palzo_guardar = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
            
            listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
            with ZipFile(palzo_guardar, 'w') as myzip:
                for f in listaPdfs:
                    myzip.write('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+f)
            myzip.close()

            if cumplido_soporte_nombres !="validar":
                documento_eliminar = [ cumplido_soporte_nombres, "1_a_nota_cumplimiento.pdf" ]
            else:
                documento_eliminar = [ "1_a_nota_cumplimiento.pdf" ]

            for doc in documento_eliminar:
                path = os.path.join('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/', doc)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

        
    except OSError:
        print("error")
     

    return [nombre_documento]

def cimplimiento_plazo(datos, cumplido_soporte_nombres):

    #datos

    
    id_eliminar =  datos["id"]

    observaciones =  datos["observaciones"]
    funcionario =  datos["funcionario"]
    orfeo =  datos["orfeo"]
    



    observaciones =  observaciones.upper()

    conn = connect()
    cursor = conn.cursor()

    fecha_cumplimiento =  datetime.now()

    cumplido = "SI"

    query = """UPDATE asignacion_plazos SET  cumplido = '{}',  observaciones =  '{}', fecha_cumplimiento =  '{}' WHERE id = '{}';""".format(cumplido,  observaciones, fecha_cumplimiento, id_eliminar )

    cursor.execute(query)
    conn.commit()


    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')

    nombre_documento=""
    if cumplido_soporte_nombres !="validar":
        listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
        error = ""
        for f in listaPdfs:
            nombre, ext = os.path.splitext(f)
            if ext != '.pdf':
                error =  "no pdf"
                nombre_archivo = nombre
        if error !=  "no pdf":
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_"+str(cumplido_soporte_nombres)
            nombre_actas_reserva = str("/plazos/completados/")+nombre_documento
            nombre_doc_soporte = cumplido_soporte_nombres
        else:
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_"+str(nombre_archivo)+".zip"
            nombre_actas_reserva = str("/plazos/completados/")+nombre_documento
            nombre_doc_soporte = nombre_archivo+".zip"

    else:
            nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_.pdf"
            nombre_actas_reserva = str("/plazos/completados/")+nombre_documento
            nombre_doc_soporte = nombre_documento


    query = """UPDATE asignacion_plazos SET documento = '{}', cumplido_soporte = '{}' WHERE id = '{}' ;""".format(nombre_actas_reserva, nombre_doc_soporte, id_eliminar)

    cursor.execute(query)
    conn.commit()

    conn.close()
    cursor.close



   #documento_soporte_plazo_cumplido
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

    radicado = "Radicado: "+orfeo
    pdf.text(120,35,radicado)

    pdf.line(5, 37, 211, 37)

    responsable = "CUMPLIMIENTO A ORDENES EMITIDAS POR EL MANDO SUPERIOR"
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(50,45,responsable)
    
    pdf.set_font('BebasNeue', '', 16)
    res_ponsable = "ORDEN CUMPLIDA POR: " + funcionario
    pdf.text(7,55, res_ponsable)



    pdf.line(5, 50, 211, 50)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(55)
    pdf.cell(200,7,"ORDEN EMITIDA",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)

    #bucle para crear cuadro e ordenes
    numero=0
    

    ordenes = [cumplido, observaciones]
    campos = ["CIMPLIMENTO", "OBSERVACIONES"]
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
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/"
    import qrcode
    
    inf_qur = "ORFEO:"+orfeo+" \n FECHA DE CUMPLIMIENTO "+lugar_fecha + "\n QUIEN CUMPLIO LA ORDEN "+funcionario
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/"
    direcion = dirercion_archvios+str("nota_cumplimiento.pdf")
    pdf.output(direcion, 'F')
 

    #Get number of pages


    try:
        #import os
        listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
        error = ""
        for f in listaPdfs:
            nombre, ext = os.path.splitext(f)
            if ext != '.pdf':
                error =  "no pdf"

        if error != "no pdf":
            merger = PdfFileMerger()
            if cumplido_soporte_nombres !="validar":
                documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
            else:
                nombre_documento = str(id_eliminar)+"_orden_"+orfeo+"_"+responsable_as+"_doc_.pdf"
                documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
                
            for file in listaPdfs:
                
                #print(file)
                merger.append(PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file))
            merger.write(documento_guardado)

            if cumplido_soporte_nombres !="validar":
                documento_eliminar = ["documento_inicial.pdf", cumplido_soporte_nombres, "nota_cumplimiento.pdf" ]
            else:
                documento_eliminar = ["documento_inicial.pdf", "nota_cumplimiento.pdf" ]

            for doc in documento_eliminar:
                path = os.path.join('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/', doc)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
        else:
            
            from zipfile import ZipFile
            palzo_guardar = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+nombre_documento
            
            
            listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
            with ZipFile(palzo_guardar, 'w') as myzip:
                for f in listaPdfs:
                    myzip.write('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+f)
            myzip.close()

            
            if cumplido_soporte_nombres !="validar":
                documento_eliminar = ["documento_inicial.pdf", cumplido_soporte_nombres, "nota_cumplimiento.pdf" ]
            else:
                documento_eliminar = ["documento_inicial.pdf", "nota_cumplimiento.pdf" ]

            for doc in documento_eliminar:
                path = os.path.join('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/', doc)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)

        
    except OSError:
        print("error")
     

    return [nombre_documento]

def listado_reasiganr(datos):

    #datos

    
    id_eliminar =  datos["id"]
    funcionario =  datos["funcionario"]
    cargo =  datos["cargo"]
    op_inmedita =  validar_check(datos["op_inmedita"])
    estrito_cumplimiento =  validar_check(datos["estrito_cumplimiento"])
    para_su_control =  validar_check(datos["para_su_control"])
    autorizado =  validar_check(datos["autorizado"])
    no_autorizado =  validar_check(datos["no_autorizado"])
    lo_de_su_cargo =  validar_check(datos["lo_de_su_cargo"])
    firma_coejc =  validar_check(datos["firma_coejc"])
    firma_secej =  validar_check(datos["firma_secej"])
    firma_jemop =  validar_check(datos["firma_jemop"])
    firma_dirop =  validar_check(datos["firma_dirop"])
    resuelva_informe =  validar_check(datos["resuelva_informe"])
    seguimiento =  validar_check(datos["seguimiento"])
    estudie_recomiende =  validar_check(datos["estudie_recomiende"])
    trate_conmigo =  validar_check(datos["trate_conmigo"])
    de_acuerdo_norma =  validar_check(datos["de_acuerdo_norma"])
    asistir =  validar_check(datos["asistir"])
    archivar =  validar_check(datos["archivar"])
    agendar =  validar_check(datos["agendar"])
    difundir =  validar_check(datos["difundir"])
    remitir =  validar_check(datos["remitir"])
    div1 =  validar_check(datos["div1"])
    div2 =  validar_check(datos["div2"])
    div3 =  validar_check(datos["div3"])
    div4 =  validar_check(datos["div4"])
    div5 =  validar_check(datos["div5"])
    div6 =  validar_check(datos["div6"])
    div7 =  validar_check(datos["div7"])
    div8 =  validar_check(datos["div8"])
    davaa =  validar_check(datos["davaa"])
    divfe =  validar_check(datos["divfe"])
    futco =  validar_check(datos["futco"])

    devolver =  validar_check(datos["devolver"])

    orden =  datos["orden"]
    fecha_plazo =  datos["fecha_plazo"]
    respuesta =  datos["respuesta"]
    fecha_plazo_respuesta =  datos["fecha_plazo_respuesta"]
    
    documento =  datos["documento"]


    funcionario =  funcionario.upper()
    cargo =  cargo.upper()
    orden =  orden.upper()
    fecha_plazo =  fecha_plazo.upper()
    respuesta =  respuesta.upper()
    fecha_plazo_respuesta =  fecha_plazo_respuesta.upper()


     
    orfeo_documento = documento.replace(".PDF",  '')
    orfeo_documento = orfeo_documento.replace(".pdf",  '')
    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')
    donmbre_archivo = orfeo_documento+"_"+responsable_as+".pdf"

    documento_g = "/plazos/asignados/"+donmbre_archivo

    conn = connect()
    cursor = conn.cursor()
    query_eliminar = "delete from asignacion_plazos where id = '{}' ".format(id_eliminar)
    cursor.execute(query_eliminar)
    conn.commit()

    dato="""('{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},  {}, {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}', {})""".format(orfeo_documento, funcionario, cargo, op_inmedita, estrito_cumplimiento, para_su_control, autorizado, no_autorizado, lo_de_su_cargo, firma_coejc, firma_secej, firma_jemop, firma_dirop, resuelva_informe, seguimiento, estudie_recomiende, trate_conmigo, de_acuerdo_norma, asistir, archivar, agendar, difundir, remitir, div1, div2, div3, div4, div5, div6, div7, div8, davaa, divfe, futco,  orden, fecha_plazo, respuesta, fecha_plazo_respuesta,  devolver)

    query="insert into asignacion_plazos (orfeo, funcionario, cargo, op_inmedita, estrito_cumplimiento, para_su_control, autorizado, no_autorizado, lo_de_su_cargo, firma_coejc, firma_secej, firma_jemop, firma_dirop, resuelva_informe, seguimiento, estudie_recomiende, trate_conmigo, de_acuerdo_norma, asistir, archivar, agendar, difundir, remitir, div1, div2, div3, div4, div5, div6, div7, div8, davaa, divfe, futco,  orden, fecha_plazo, respuesta, fecha_plazo_respuesta,  devolver ) values"+dato


    cursor.execute(query)
    conn.commit()
    query_2 = "select id from  asignacion_plazos where orfeo = '{}' order by id desc  limit 1".format(orfeo_documento)
    cursor.execute(query_2)
    data = cursor.fetchall()
    for x in data[0]:
        id = x
    donmbre_archivo = orfeo_documento+"_"+responsable_as+".pdf"
    donmbre_archivo_query = str(id)+"_"+donmbre_archivo
    documento_g = "/plazos/asignados/"+donmbre_archivo_query
    query_2 = """UPDATE asignacion_plazos SET documento = '{}' WHERE orfeo = '{}' and id = {} ;""".format(documento_g, orfeo_documento, id)

    cursor.execute(query_2)
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
    orfeo = documento.replace(".PDF",  '')
    radicado = "Radicado: "+orfeo
    pdf.text(120,35,radicado)

    pdf.line(5, 37, 211, 37)

    responsable = "RESPONSABLE DEL CUMPLIMIENTO DE LA ORDEN "
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(70,45,responsable)
    
    pdf.set_font('BebasNeue', '', 16)
    res_ponsable = "RESPONSABLE: "
    pdf.text(7,55, res_ponsable)
    res_cargo = "CARGO: "
    pdf.text(7,61, res_cargo)
    fecha_plazo_cumplimiento = dato = fecha_plazo.replace("T",  ' HORA ')
    res_fecha = "FECHA DE CUMPLIMIENTO: "
    pdf.text(7,67, res_fecha)

    pdf.set_text_color(125,0,0)
    pdf.text(55,55, funcionario)
    pdf.text(55,61, cargo)
    pdf.text(55,67, fecha_plazo_cumplimiento)

    pdf.line(5, 70, 211, 70)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(65)
    pdf.cell(65,7,"NIVEL DE PRIORIDAD",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(55,6,"OPERACIÓN INMEDIATA",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"ESTRICTO CUMPLIMIENTO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"PARA SU CONTROL",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"AUTORIZADO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"NO AUTORIZADO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"LO DE SU CARGO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)


    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(-49)
    pdf.cell(67)
    pdf.cell(65,7,"NIVEL DE AUTORIDAD",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA COEJC",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA SECEJ",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA JEMOP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA DIROP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESUELVA E INFORME",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"SEGUIMIENTO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"ESTUDIE Y RECOMIENDE",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)


    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(-65)
    pdf.cell(135)
    pdf.cell(65,7,"ACCIÓN",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(135)
    pdf.cell(55,6,"TRATE CON DIROP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DE ACUERDO A NORMA",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"ASISTIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"ARCHIVAR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"AGENDAR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DIFUNDIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)

    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"REMITIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)

    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DEVOLVER",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(-8)

    pdf.line(5, 147, 211, 147)
    responsable = "REMISIONES - DIFUSIONES"
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(85,155,responsable)

    pdf.set_font('BebasNeue', '', 14)
    pdf.rounded_rect(20, 160, 7, 7, 1,'D', '1234')
    pdf.text(10,165,"DIV01")

    pdf.rounded_rect(40, 160, 7, 7, 1,'D', '1234')
    pdf.text(30,165,"DIV02")

    pdf.rounded_rect(60, 160, 7, 7, 1,'D', '1234')
    pdf.text(50,165,"DIV03")

    pdf.rounded_rect(80, 160, 7, 7, 1,'D', '1234')
    pdf.text(70,165,"DIV04")
    
    pdf.rounded_rect(100, 160, 7, 7, 1,'D', '1234')
    pdf.text(90,165,"DIV05")
        
    pdf.rounded_rect(120, 160, 7, 7, 1,'D', '1234')
    pdf.text(110,165,"DIV06")
            
    pdf.rounded_rect(140, 160, 7, 7, 1,'D', '1234')
    pdf.text(130,165,"DIV07")
                
    pdf.rounded_rect(160, 160, 7, 7, 1,'D', '1234')
    pdf.text(150,165,"DIV08")
                    
    pdf.rounded_rect(180, 160, 7, 7, 1,'D', '1234')
    pdf.text(170,165,"DAVAA")
                        
    pdf.rounded_rect(200, 160, 7, 7, 1,'D', '1234')
    pdf.text(190,165,"DIVFE")

    pdf.rounded_rect(20, 170, 7, 7, 1,'D', '1234')
    pdf.text(10,175,"FUTOM")


    pdf.text(60,175,"TRATAR CON JEMOP")

    pdf.text(110,175,"AGENDAMIENTO")
    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 16)

    pdf.text(100,175,respuesta)

    fecha_plazo_cumplimiento_T = dato = fecha_plazo_respuesta.replace("T",  ' HORA ')
    pdf.text(155,175,fecha_plazo_cumplimiento_T)
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 12)
    pdf.text(10,190,"OBSERVACIONES:")
    
    pdf.ln(63)
    #pdf.cell(2)
    y = pdf.get_y()

    pdf.multi_cell(195, 5, str(orden), 0, "J", False)
    x = pdf.get_y()
    z = (x-y)+5
    pdf.rounded_rect(7, 192, 202, z, 1,'D', '1234')
    
    pdf.line(5, 255, 211, 255)

    pdf.set_font('BebasNeue', '', 12)
    #pdf.text(10,265,"TC. JULIAN PRIETO")
    pdf.set_font('BebasNeue', '', 10)
    pdf.text(10,270,"Oficial de  Seguimiento")

    #primera columna
    if op_inmedita:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,84,6,6)
    if estrito_cumplimiento:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,92,6,6)
    if para_su_control:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,100,6,6)
    if autorizado:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,108,6,6)
    if no_autorizado:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,116,6,6)
    if lo_de_su_cargo:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,124,6,6)

    #segunda columna
    if firma_coejc:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,84,6,6)
    if firma_secej:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,92,6,6)
    if firma_jemop:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,100,6,6)
    if firma_dirop:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,108,6,6)
    if resuelva_informe:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,116,6,6)
    if seguimiento:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,124,6,6)
    if estudie_recomiende:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,132,6,6)
    
    #tercera columna
    if trate_conmigo:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,84,6,6)
    if de_acuerdo_norma:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,92,6,6)
    if asistir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,100,6,6)
    if archivar:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,108,6,6)
    if agendar:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,116,6,6)
    if difundir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,124,6,6)
    if remitir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,132,6,6)
    if devolver:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,140,6,6)
    

    #divisiones
    if div1:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",21,160,6,6)
    if div2:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",41,160,6,6)
    if div3:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",61,160,6,6)
    if div4:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",81,160,6,6)
    if div5:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",101,160,6,6)
    if div6:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",121,160,6,6)
    if div7:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",141,160,6,6)
    if div8:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",161,160,6,6)
    if davaa:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",181,160,6,6)
    if divfe:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",201,160,6,6)

    if futco:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",21,170,6,6)



    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/"
    import qrcode
    orfeo_qr = dato = documento.replace(".PDF",  '')
    
    inf_qur = orfeo_qr+" \n"+funcionario + "\n Fecha de Cumplimento " +fecha_plazo_cumplimiento
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/"
    direcion = dirercion_archvios+str("z")+'.pdf'
    pdf.output(direcion, 'F')
    
    #Get number of pages

    object = PyPDF2.PdfFileReader(r'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_eliminar.pdf')
    NumPages = object.getNumPages()
    #print(NumPages)
    #pip install PyPDF2
    from PyPDF2 import PdfWriter, PdfReader
    pages_to_delete = [NumPages] # page numbering starts from 0
    infile = PdfReader(r'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_eliminar.pdf', 'rb')
    output = PdfWriter()

    for i in range(len(infile.pages)):
        if i not in pages_to_delete:
            p = infile.pages[i]
            output.add_page(p)

    with open(r'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/documento_eliminar_2.pdf', 'wb') as f:
        output.write(f)
    documento_eliminar = ["documento_eliminar.pdf"]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    
    #import os
    listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
    merger = PdfFileMerger(strict=False)

     
    orfeo_documento = documento.replace(".PDF",  '')
    orfeo_documento = orfeo_documento.replace(".pdf",  '')
    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')
    donmbre_archivo = orfeo_documento+"_"+responsable_as+".pdf"

    documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+donmbre_archivo_query
    print(documento_guardado)

    #for file in listaPdfs:
        #print(file)
        #pdf_doc = PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file, strict=False)
        #merger.append(pdf_doc)
    #merger.write(documento_guardado)
    import fitz

    result = fitz.open()

    for pdf in listaPdfs:
        pdf_doc = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+pdf
        with fitz.open(pdf_doc) as mfile:
            result.insert_pdf(mfile)
        
    result.save(documento_guardado)

    documento_eliminar = ["z.pdf", "documento_eliminar_2.pdf"]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    

    return [donmbre_archivo]

def elimnar_asignacion(datos):

    #datos

    
    id_eliminar =  datos["id"]
    
    conn = connect()
    cursor = conn.cursor()
    query_eliminar = "delete from asignacion_plazos where id = '{}' ".format(id_eliminar)
    cursor.execute(query_eliminar)
    conn.commit()

    conn.close()
    cursor.close
    
def listado(datos):

    #datos


    funcionario =  datos["funcionario"]
    cargo =  datos["cargo"]
    op_inmedita =  validar_check(datos["op_inmedita"])
    estrito_cumplimiento =  validar_check(datos["estrito_cumplimiento"])
    para_su_control =  validar_check(datos["para_su_control"])
    autorizado =  validar_check(datos["autorizado"])
    no_autorizado =  validar_check(datos["no_autorizado"])
    lo_de_su_cargo =  validar_check(datos["lo_de_su_cargo"])
    firma_coejc =  validar_check(datos["firma_coejc"])
    firma_secej =  validar_check(datos["firma_secej"])
    firma_jemop =  validar_check(datos["firma_jemop"])
    firma_dirop =  validar_check(datos["firma_dirop"])
    resuelva_informe =  validar_check(datos["resuelva_informe"])
    seguimiento =  validar_check(datos["seguimiento"])
    estudie_recomiende =  validar_check(datos["estudie_recomiende"])
    trate_conmigo =  validar_check(datos["trate_conmigo"])
    de_acuerdo_norma =  validar_check(datos["de_acuerdo_norma"])
    asistir =  validar_check(datos["asistir"])
    archivar =  validar_check(datos["archivar"])
    agendar =  validar_check(datos["agendar"])
    difundir =  validar_check(datos["difundir"])
    remitir =  validar_check(datos["remitir"])
    div1 =  validar_check(datos["div1"])
    div2 =  validar_check(datos["div2"])
    div3 =  validar_check(datos["div3"])
    div4 =  validar_check(datos["div4"])
    div5 =  validar_check(datos["div5"])
    div6 =  validar_check(datos["div6"])
    div7 =  validar_check(datos["div7"])
    div8 =  validar_check(datos["div8"])
    davaa =  validar_check(datos["davaa"])
    divfe =  validar_check(datos["divfe"])
    futco =  validar_check(datos["futco"])

    devolver =  validar_check(datos["devolver"])

    orden =  datos["orden"]
    fecha_plazo =  datos["fecha_plazo"]
    respuesta =  datos["respuesta"]
    fecha_plazo_respuesta =  datos["fecha_plazo_respuesta"]
    
    documento =  datos["documento"]


    funcionario =  funcionario.upper()
    cargo =  cargo.upper()
    orden =  orden.upper()
    fecha_plazo =  fecha_plazo.upper()
    respuesta =  respuesta.upper()
    fecha_plazo_respuesta =  fecha_plazo_respuesta.upper()


     
    orfeo_documento = documento.replace(".PDF",  '')
    orfeo_documento = orfeo_documento.replace(".pdf",  '')
    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')



    dato="""('{}', '{}', '{}', {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {},  {}, {}, {}, {}, {}, {}, {}, '{}', '{}', '{}', '{}',  {})""".format(orfeo_documento, funcionario, cargo, op_inmedita, estrito_cumplimiento, para_su_control, autorizado, no_autorizado, lo_de_su_cargo, firma_coejc, firma_secej, firma_jemop, firma_dirop, resuelva_informe, seguimiento, estudie_recomiende, trate_conmigo, de_acuerdo_norma, asistir, archivar, agendar, difundir, remitir, div1, div2, div3, div4, div5, div6, div7, div8, davaa, divfe, futco,  orden, fecha_plazo, respuesta, fecha_plazo_respuesta,  devolver)

    query="insert into asignacion_plazos (orfeo, funcionario, cargo, op_inmedita, estrito_cumplimiento, para_su_control, autorizado, no_autorizado, lo_de_su_cargo, firma_coejc, firma_secej, firma_jemop, firma_dirop, resuelva_informe, seguimiento, estudie_recomiende, trate_conmigo, de_acuerdo_norma, asistir, archivar, agendar, difundir, remitir, div1, div2, div3, div4, div5, div6, div7, div8, davaa, divfe, futco,  orden, fecha_plazo, respuesta, fecha_plazo_respuesta, devolver ) values"+dato

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


    query_2 = "select id from  asignacion_plazos where orfeo = '{}' order by id desc  limit 1".format(orfeo_documento)
    cursor.execute(query_2)
    data = cursor.fetchall()
    for x in data[0]:
        id = x
    donmbre_archivo = orfeo_documento+"_"+responsable_as+".pdf"
    donmbre_archivo_query = str(id)+"_"+donmbre_archivo
    documento_g = "/plazos/asignados/"+donmbre_archivo_query
    query_2 = """UPDATE asignacion_plazos SET documento = '{}' WHERE orfeo = '{}' and id = {} ;""".format(documento_g, orfeo_documento, id)

    cursor.execute(query_2)
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
    orfeo = documento.replace(".PDF",  '')
    radicado = "Radicado: "+orfeo
    pdf.text(120,35,radicado)

    pdf.line(5, 37, 211, 37)

    responsable = "RESPONSABLE DEL CUMPLIMIENTO DE LA ORDEN "
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(70,45,responsable)
    
    pdf.set_font('BebasNeue', '', 16)
    res_ponsable = "RESPONSABLE: "
    pdf.text(7,55, res_ponsable)
    res_cargo = "CARGO: "
    pdf.text(7,61, res_cargo)
    fecha_plazo_cumplimiento = dato = fecha_plazo.replace("T",  ' HORA ')
    res_fecha = "FECHA DE CUMPLIMIENTO: "
    pdf.text(7,67, res_fecha)

    pdf.set_text_color(125,0,0)
    pdf.text(55,55, funcionario)
    pdf.text(55,61, cargo)
    pdf.text(55,67, fecha_plazo_cumplimiento)

    pdf.line(5, 70, 211, 70)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(65)
    pdf.cell(65,7,"NIVEL DE PRIORIDAD",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(55,6,"OPERACIÓN INMEDIATA",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"ESTRICTO CUMPLIMIENTO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"PARA SU CONTROL",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"AUTORIZADO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"NO AUTORIZADO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(55,6,"LO DE SU CARGO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)


    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(-49)
    pdf.cell(67)
    pdf.cell(65,7,"NIVEL DE AUTORIDAD",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA COEJC",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA SECEJ",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA JEMOP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESPUESTA CON FIRMA DIROP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"RESUELVA E INFORME",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"SEGUIMIENTO",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(67)
    pdf.cell(55,6,"ESTUDIE Y RECOMIENDE",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)


    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)
    pdf.ln(-65)
    pdf.cell(135)
    pdf.cell(65,7,"ACCIÓN",1,0, 'C',False)
    pdf.set_font('BebasNeue', '', 12)
    pdf.ln(9)
    pdf.cell(135)
    pdf.cell(55,6,"TRATE CON DIROP",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DE ACUERDO A NORMA",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"ASISTIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"ARCHIVAR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"AGENDAR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DIFUNDIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)

    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"REMITIR",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)

    pdf.ln(8)
    pdf.cell(135)
    pdf.cell(55,6,"DEVOLVER",1,0, 'L',False)
    pdf.cell(10,6,"",1,0, 'L',False)
    pdf.ln(-8)

    pdf.line(5, 147, 211, 147)
    responsable = "REMISIONES - DIFUSIONES"
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(85,155,responsable)

    pdf.set_font('BebasNeue', '', 14)
    pdf.rounded_rect(20, 160, 7, 7, 1,'D', '1234')
    pdf.text(10,165,"DIV01")

    pdf.rounded_rect(40, 160, 7, 7, 1,'D', '1234')
    pdf.text(30,165,"DIV02")

    pdf.rounded_rect(60, 160, 7, 7, 1,'D', '1234')
    pdf.text(50,165,"DIV03")

    pdf.rounded_rect(80, 160, 7, 7, 1,'D', '1234')
    pdf.text(70,165,"DIV04")
    
    pdf.rounded_rect(100, 160, 7, 7, 1,'D', '1234')
    pdf.text(90,165,"DIV05")
        
    pdf.rounded_rect(120, 160, 7, 7, 1,'D', '1234')
    pdf.text(110,165,"DIV06")
            
    pdf.rounded_rect(140, 160, 7, 7, 1,'D', '1234')
    pdf.text(130,165,"DIV07")
                
    pdf.rounded_rect(160, 160, 7, 7, 1,'D', '1234')
    pdf.text(150,165,"DIV08")
                    
    pdf.rounded_rect(180, 160, 7, 7, 1,'D', '1234')
    pdf.text(170,165,"DAVAA")
                        
    pdf.rounded_rect(200, 160, 7, 7, 1,'D', '1234')
    pdf.text(190,165,"DIVFE")

    pdf.rounded_rect(20, 170, 7, 7, 1,'D', '1234')
    pdf.text(10,175,"FUTOM")


    pdf.text(60,175,"TRATAR CON JEMOP")

    pdf.text(110,175,"AGENDAMIENTO")
    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 16)

    pdf.text(100,175,respuesta)

    fecha_plazo_cumplimiento_T = dato = fecha_plazo_respuesta.replace("T",  ' HORA ')
    pdf.text(155,175,fecha_plazo_cumplimiento_T)
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 12)
    pdf.text(10,190,"OBSERVACIONES:")
    
    pdf.ln(63)
    #pdf.cell(2)
    y = pdf.get_y()

    pdf.multi_cell(195, 5, str(orden), 0, "J", False)
    x = pdf.get_y()
    z = (x-y)+5
    pdf.rounded_rect(7, 192, 202, z, 1,'D', '1234')
    
    pdf.line(5, 255, 211, 255)

    pdf.set_font('BebasNeue', '', 12)
    #pdf.text(10,265,"TC. JULIAN PRIETO")
    pdf.set_font('BebasNeue', '', 10)
    pdf.text(10,270,"Oficial de  Seguimiento")

    #primera columna
    if op_inmedita:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,84,6,6)
    if estrito_cumplimiento:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,92,6,6)
    if para_su_control:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,100,6,6)
    if autorizado:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,108,6,6)
    if no_autorizado:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,116,6,6)
    if lo_de_su_cargo:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",67,124,6,6)

    #segunda columna
    if firma_coejc:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,84,6,6)
    if firma_secej:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,92,6,6)
    if firma_jemop:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,100,6,6)
    if firma_dirop:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,108,6,6)
    if resuelva_informe:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,116,6,6)
    if seguimiento:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,124,6,6)
    if estudie_recomiende:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",134,132,6,6)
    
    #tercera columna
    if trate_conmigo:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,84,6,6)
    if de_acuerdo_norma:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,92,6,6)
    if asistir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,100,6,6)
    if archivar:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,108,6,6)
    if agendar:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,116,6,6)
    if difundir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,124,6,6)
    if remitir:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,132,6,6)
    if devolver:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",202,140,6,6)
    

    #divisiones
    if div1:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",21,160,6,6)
    if div2:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",41,160,6,6)
    if div3:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",61,160,6,6)
    if div4:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",81,160,6,6)
    if div5:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",101,160,6,6)
    if div6:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",121,160,6,6)
    if div7:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",141,160,6,6)
    if div8:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",161,160,6,6)
    if davaa:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",181,160,6,6)
    if divfe:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",201,160,6,6)

    if futco:
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/escudos/Imagen1_new.png",21,170,6,6)



    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/qr/"
    import qrcode
    orfeo_qr = dato = documento.replace(".PDF",  '')
    
    inf_qur = orfeo_qr+" \n"+funcionario + "\n Fecha de Cumplimento " +fecha_plazo_cumplimiento
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/"
    direcion = dirercion_archvios+str("z")+'.pdf'
    pdf.output(direcion, 'F')
    
    #pip install PyPDF2

    #import os
    listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/')
    merger = PdfFileMerger()


    orfeo_documento = documento.replace(".PDF",  '')
    orfeo_documento = orfeo_documento.replace(".pdf",  '')
    responsable_as =  funcionario.replace(".",  '_')
    responsable_as =  responsable_as.replace(" ",  '_')
    donmbre_archivo = orfeo_documento+"_"+responsable_as+".pdf"


    documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+donmbre_archivo_query
    print(documento_guardado)

    #for file in listaPdfs:
        #print(file)
        #pdf_doc = PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file, strict=False)
        #merger.append(pdf_doc)
    #merger.write(documento_guardado)
    import fitz

    result = fitz.open()

    for pdf in listaPdfs:
        pdf_doc = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+pdf
        with fitz.open(pdf_doc) as mfile:
            result.insert_pdf(mfile)
        
    result.save(documento_guardado)

    documento_eliminar = ["z.pdf", documento]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    

    return [documento_g]

def buscar(datos):

    permiso =datos["unidad"]
    #print(permiso)

    if permiso == "EJC":
        query="select * from asignacion_plazos ORDER BY  fecha_plazo ASC"
    else:
        query="select * from asignacion_plazos where cargo LIKE '%{}%' ORDER BY  fecha_plazo ASC".format(permiso)

    conn = connect()
    cursor = conn.cursor()


    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    cursor.close
    #print("data")
    return [data]

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


def actualizar_asunto(datos):

    asunto =datos["asunto"]
    id_eliminar =  datos["id"]
  
    
    query = """UPDATE asignacion_plazos SET  asunto = '{}' WHERE id = '{}';""".format(asunto, id_eliminar )

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    conn.commit()

   
    conn.close()
    cursor.close
    #print(data)
  





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
 

