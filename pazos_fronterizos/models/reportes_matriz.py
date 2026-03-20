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

    
    def texto_vertical(self, x, y, texto, espacio=4):
        """Escribir texto en vertical (cada letra debajo de otra)"""
        for i, letra in enumerate(texto):
            self.text(x, y + (i * espacio), letra)

    def parametros(self, **kwargs):
        self.titulo = ""
        self.tipo = "mapa"
        self.logo = ""
        self.fecha_titulo = ""
        self.permiso = "EJC"
        self.nivel = ""
        self.usuario = ""
        self.pie_pagina = "NO"
        self.fondo_pagina = "SI"
        self.seguridad = "JEMOP"
        self.precidencial =  "OK"
        self.ruta = ""
        self.imagen = ""
        self.qr=""
        self.mapa =""
        self.unidad_png=""
        self.y_pdf = 355.6
        self.x_pdf = 215.9
        self.DIRECION = os.getenv('DIRECION')

        for k in kwargs.items():
            if "titulo" == k[0]:
                self.titulo = k[1]
            if "tipo" == k[0]:
                self.tipo = k[1]
            if "logo" == k[0]:
                self.logo = k[1]
            if "fecha_titulo" == k[0]:
                self.fecha_titulo = k[1]
            if "permiso" == k[0]:
                self.permiso = k[1]
            if "nivel" == k[0]:
                self.nivel = k[1]
            if "usuario" == k[0]:
                self.usuario = k[1]
            if "pie_pagina" == k[0]:
                self.pie_pagina = k[1]
                
            if "fondo_pagina" == k[0]:
                self.fondo_pagina = k[1]
            if "seguridad" == k[0]:
                self.seguridad = k[1]
            if "precidencial" == k[0]:
                self.precidencial = k[1]
            if "ruta" == k[0]:
                self.ruta = k[1]
            if "imagen" == k[0]:
                self.imagen = k[1]
            if "QR" == k[0]:
                self.qr = k[1]
            if "mapa" == k[0]:
                self.mapa = k[1]
            if "unidad_png" == k[0]:
                self.unidad_png = k[1]
            if "y_pdf" == k[0]:
                self.y_pdf = k[1]
            if "x_pdf" == k[0]:
                self.x_pdf = k[1]

                
        
    def header(self):
        #imagen
        
        logos = "LOGO JEMOP"
        imagen = self.ruta+self.imagen
        
        if self.fondo_pagina == "SI":
            if self.tipo =="mapa":
                self.image(imagen,10,9,16,19)
                self.image(self.qr,250,5.5,24,24)

                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
                self.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
                self.text(35,25,str("DIRECCIÓN DE OPERACIONES"))
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)



                self.ln(-20)

                self.image(imagen,0,0,self.y_pdf,self.x_pdf)
                self.image(self.qr,5,180,24,24)
                self.image(self.mapa,-62,-54,228,309)

                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.set_font('Arial Black', '', 16)
                self.set_text_color(56,87,35)
                self.text(135, 18, self.titulo)
                # fecha = strftime(self.fecha, '%y')
                self.set_text_color(40,40,40)
                self.set_font('Arial Black', '', 12)
                self.text(135, 23.5, self.fecha_titulo)
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.ln(7)

                posicion_final = 30

                self.set_line_width(1)
                self.set_draw_color(130, 130, 130)   
                #self.line(140, posicion_final, 335, posicion_final)
                #self.line(140, posicion_final+1.5, 335, posicion_final+1.5) 


                self.ln(35)
            elif self.tipo =="reporte":
                self.image(imagen,10,9,16,19)
                if self.qr!="":
                    self.image(self.qr,250,5.5,24,24)

                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
                self.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
                self.text(35,25,str("DIRECCIÓN DE OPERACIONES"))
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)



                self.ln(-20)

                self.image(imagen,0,0,self.y_pdf,self.x_pdf)
                if self.qr !="":
                    self.image(self.qr,323,10,24,24)

                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.set_font('Arial Black', '', 16)
                self.set_text_color(56,87,35)
                self.text(55, 18, self.titulo)
                # fecha = strftime(self.fecha, '%y')
                self.set_text_color(40,40,40)
                self.set_font('Arial Black', '', 12)
                self.text(55, 23.5, self.fecha_titulo)
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.ln(7)

                posicion_final = 30

                self.set_line_width(1)
                self.set_draw_color(130, 130, 130) 
                if self.imagen == "Diapositiva_fondo (1).JPG" or self.imagen == "Diapositiva_fondo (2).JPG" or self.imagen == "Diapositiva_fondo (3).JPG":

                    self.set_font("Arial", "", 7)
                    self.set_text_color(30, 30, 30)

                    texto = "CONSULTAS POPULARES, INTERNAS O INTERPARTIDISTAS"
                    ancho_texto = self.get_string_width(texto)

                    # Girar -90 grados desde la esquina inferior izquierda
                    self.rotate(-90, x=10, y=self.h - 10)

                    # Calcular posición centrada usando la altura como ancho
                    x_centrado = (((self.h/2) - (ancho_texto/2))*-1) - (ancho_texto/4+ancho_texto/2 )
                    self.text(x_centrado, -70, texto)

                    # Restablecer rotación
                    self.rotate(0)
                    self.set_font('BebasNeue', '', 14)

                #self.line(140, posicion_final, 335, posicion_final)
                #self.line(140, posicion_final+1.5, 335, posicion_final+1.5) 


                self.ln(35)

            elif self.tipo =="mapa_evento":
                self.image(imagen,10,9,16,19)
                #self.image(self.qr,250,323,24,24)

                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                #self.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
                #self.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
                #self.text(35,25,str("DIRECCIÓN DE OPERACIONES"))
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.ln(-20)

                self.image(imagen,0,0,self.y_pdf,self.x_pdf)
                if self.qr !="":
                    self.image(self.qr,314.5,180,24,24)
                if self.unidad_png == "DIV01":
                    
                    self.image(self.mapa,-23.5,-34.5,206.5,283)
                    
                elif self.unidad_png == "DIV02":
                    
                    self.image(self.mapa,-39,-35.5,207.5,282.5)
                    

                elif self.unidad_png == "DIV03":
                    
                    self.image(self.mapa,-38,-39,220,302)
                    

                elif self.unidad_png == "DIV04":
                   
                    self.image(self.mapa,-25,-21,189.7,258)
                    

                elif self.unidad_png == "DIV05":
                    
                    self.image(self.mapa,-21.5,-24,180,245.5)
                    

                elif self.unidad_png == "DIV06":
                    
                    self.image(self.mapa,-25.5,-18.5,187,254)
                    

                elif self.unidad_png == "DIV07":
                    
                    self.image(self.mapa,-105,-53,344,455.5)
                    

                elif self.unidad_png == "DIV08":
                    
                    self.image(self.mapa,-25,-26,186.2,251.5)
                  

                elif self.unidad_png == "FUTCO":
                    
                    self.image(self.mapa,-10,-33,177.5,270)
                    
                else:
                    
                    #self.image(maself.mapapa,-59.5,-59,229,310)
                    self.image(self.mapa,-52,-54,228,309)


    
                caligrafia_ingreso( self, self.DIRECION)

                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.set_font('Arial Black', '', 16)
                self.set_text_color(56,87,35)
                self.text(155, 18, self.titulo)
                # fecha = strftime(self.fecha, '%y')
                self.set_text_color(40,40,40)
                self.set_font('Arial Black', '', 12)
                self.text(155, 23.5, self.fecha_titulo)
    
                     # Select Arial bold 15

                     
                self.set_fill_color(210, 214, 209)
                
                self.set_text_color(70,70,70)
                self.set_font('BebasNeue', '', 14)

                self.ln(7)

                posicion_final = 30

                self.set_line_width(1)
                self.set_draw_color(130, 130, 130)   
                #self.line(140, posicion_final, 335, posicion_final)
                #self.line(140, posicion_final+1.5, 335, posicion_final+1.5) 


                self.ln(35)


        #self.ln(25)

    def footer(self):
        
        if self.pie_pagina =="SI":
            self.set_text_color(80,80,80)
            # Go to 1.5 cm from bottom
            self.set_y(-15)
            # Select Arial italic 8
            self.set_font('Arial', 'B', 10)
            # Print centered page number
            # self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

            dias = datetime.now().day
            meses = datetime.now().month
            anios = datetime.now().year
            # print(datetime.now().month)
            meses = mes(meses)
            meses =str(meses)
            meses = meses.upper()
            # print(meses)   
            fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)

            self.text(90, 212, "SECRETO ")
            self.text(10, 212, 'Fuente: Centro de Operaciones Ejército')



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
