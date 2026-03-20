from datetime import datetime
# coding: utf-8
import psycopg2
import base64 

from os import getcwd
import os
import shutil
from dotenv import load_dotenv
from math import acos, cos, sin, radians
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

import matplotlib.pyplot as plt
import seaborn as sns

from .reportes_matriz import *
from .funciones.mapa_filtro import *

from funtion.eleciones import *
from pypdf import PdfReader, PdfWriter
import os


from PyPDF2 import PdfReader, PdfWriter
#Funcion de resultados nueva ayuda
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn
def resta(a, b, c):
    num = a-b
    
    if num >0:
        num = -5
    else:
        num = num
    dato = (num*-1) 

    if c < dato:
        c = dato

    return [num, c]
def inf_frontera_div(pdf, TEXTO, NUMERO, IMAGEN, x, y ):
        #informacion de las bases y frontreras a nivel division 
        #frontera 

        img = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/resultados/{}.png".format(IMAGEN)
        pdf.image(img,x,y,20,20)
        x_i =  x +30
        y_i =  y +10
        pdf.set_text_color(70,70,70)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(x_i,y_i,str(TEXTO))
        x_i =  x +30
        y_i =  y +20
        pdf.set_font('BebasNeue', '', 26)
        pdf.text(x_i,y_i,str(NUMERO))

        pdf.set_line_width(1)
        pdf.set_draw_color(130, 130, 130) 

        y_i =  y +5
        y_ii =  y +20
        z_i =  x +25
        pdf.line(z_i, y_i, z_i, y_ii)

def cuadro_unidades(pdf, dato):
    
    #-----------------------------------------
    #-----tabla de los pasos fronterisos------
    #-----------------------------------------
 
    pdf.set_line_width(0.3)
    pdf.set_fill_color(180, 180, 180)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(30,30,30)

    #rectangulos para la creacion de cuadros 
    pdf.rect(135,36,195,5,"FD")#titulo
    pdf.rect(135,41,25,10,"FD")#division
    pdf.rect(160,41,29,10,"FD")#unidades
    pdf.rect(189,41,29,10,"FD")#formales
    pdf.rect(218,41,29,10,"FD")#formales
    pdf.rect(247,41,20,10,"FD")#formales
    pdf.rect(267,41,35,10,"FD")#formales
    pdf.rect(302,41,28,10,"FD")#formales


    pdf.set_font('Arial Narrow', 'B', 12)
    pdf.ln(4)
    pdf.cell(125)
    pdf.multi_cell(195,5,"INFORMACION GENERAL UNIDADES Y BASES EN FRONTERA",1, 'C',False)
    pdf.set_font('Arial Narrow', 'B', 9)
    #pdf.ln()
    pdf.cell(125)
    pdf.multi_cell(25,5,"FRONTERA",0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(150)
    pdf.multi_cell(29, 5, "EXTENCION", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(179)
    pdf.multi_cell(29, 5, "PASOS FORMALES", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(208)
    pdf.multi_cell(29, 5, "PASOS NO FORMALES", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(237)
    pdf.multi_cell(20, 5, "TOTAL PASOS", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(257)
    pdf.multi_cell(35, 5, "TOTAL PELOTONES Y BASES MILITARES", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(292)
    pdf.multi_cell(28, 5, "TROPA DISPONIBLE A 10 km", 0, "C", False)

    pdf.cell(125)
    pdf.multi_cell(25,5,dato[5],1, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(150)
    pdf.multi_cell(29, 5, dato[6], 1, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(179)
    pdf.multi_cell(29, 5, str(dato[0]), 1, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(208)
    pdf.multi_cell(29, 5, str(dato[1]), 1, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(237)
    pdf.multi_cell(20, 5, str(dato[0]+dato[1]), 1, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(257)
    pdf.multi_cell(35, 5, str(dato[2]), 1, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(292)
    hombres = str(dato[3] + dato[4]) +" Hombres"
    pdf.multi_cell(28, 5, str(hombres), 1, "C", False)


def ver_inf_pasos_fronteras(dato):
    fecha_pazos =  dato["fecha_pasos_informacion"]

    conn = connect()
    cursor = conn.cursor()

    query = """select * from  pazos_fronterizos where fecha_pazos = '{}';""".format(fecha_pazos)


    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close

    return[data]

def ver_pasos_fronteras(dato):

    conn = connect()
    cursor = conn.cursor()

    query = """select * from  pazos_fronterizos_directiva """

    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close

    return[data]


def ver_reporte_pasos_fronteras(dato):
    fecha_pazos =  dato["fecha_pasos_informacion"]

    conn = connect()
    cursor = conn.cursor()

    query = """select * from  pazos_fronterizos where fecha_pazos = '{}';""".format(fecha_pazos)
    cursor.execute(query)
    data = cursor.fetchall()

    query_2 = """select * from  pazos_fronterizos_directiva """

    cursor.execute(query_2)
    data_2 = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close
    numero = 0

    point=[]
    for x in data:
        if x[38] != "" and [39] != "":
            point.append(x)

    formal=[]
    no_forma=[]
    for x in data_2:
        if x[11] == "Formal":
            formal.append(x)
        else:
            no_forma.append(x)

    DIRECION = os.getenv('DIRECION')   
    ruta = DIRECION
    #se llam la funcion para la cracion del mapa

    EVENTOS(ruta, formal, no_forma, point)

    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/pazos_fronterizos/QR/"
    import qrcode

    dia = datetime.now().day
    mes = datetime.now().month
    anio = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    segun = datetime.now().second
    lugar_fecha  = str(dia)+" - " +str(mes)+" - " +str(anio) 
    hora = str(hour)+":" +str(minute)+":" +str(segun) 
    
    inf_qur = "LUGAR:"+"Bogota"+" \n FECHA  "+lugar_fecha + "\n HORA "+hora
    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    fechas_inicial = fecha(fecha_pazos)
    fecha_titulo = fechas_inicial[0]+" de " +  fechas_inicial[1] + " del " + fechas_inicial[2] 
    fecha_titulo = fecha_titulo.upper()

    mapa = '{}static/img/img_mapas/PAZOS.png'.format(ruta)
    titulo = "NIVEL DE SEGURIDAD FRONTERIZO"
    
    pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/oficio/", imagen = "Diapositiva20.JPG", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/pazos_fronterizos/QR/QR.png", titulo= titulo, fecha_titulo= fecha_titulo,mapa=mapa)

    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)

    pdf.add_page()
    pdf.set_auto_page_break(True, 10)
    pdf.set_font('BebasNeue', '', 12)

    #-----------------------------------------
    #-----tabla de los pasos fronterisos------
    #-----------------------------------------
 
    pdf.set_line_width(0.3)
    pdf.set_fill_color(180, 180, 180)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(30,30,30)

    #rectangulos para la creacion de cuadros 
    pdf.rect(135,36,195,5,"FD")#titulo
    pdf.rect(135,41,15,23,"FD")#division
    pdf.rect(150,41,29,15,"FD")#unidades
    pdf.rect(179,41,41,15,"FD")#formales
    pdf.rect(220,41,50,15,"FD")#formales
    pdf.rect(270,41,30,15,"FD")#formales
    pdf.rect(300,41,30,23,"FD")#formales

    pdf.rect(150,56,14.5,8,"FD")#unidades
    pdf.rect(164.5,56,14.5,8,"FD")#unidades

    pdf.rect(270,56,15,8,"FD")#unidades
    pdf.rect(285,56,15,8,"FD")#unidades

    pdf.set_fill_color(189, 215, 238)
    pdf.rect(179,56,13.67,8,"FD")#unidades
    pdf.rect(192.67,56,13.67,8,"FD")#unidades
    pdf.rect(206.34,56,13.67,8,"FD")#unidades

    pdf.set_fill_color(0, 176, 80)
    pdf.rect(220,56,16.67,8,"FD")#unidades

    pdf.set_fill_color(255, 255, 0)
    pdf.rect(236.67,56,16.67,8,"FD")#unidades
    
    pdf.set_fill_color(255, 0, 0)
    pdf.rect(253.34,56,16.67,8,"FD")#unidades

    pdf.set_font('Arial Narrow', 'B', 12)
    pdf.ln(4)
    pdf.cell(125)
    pdf.multi_cell(195,5,"UNIDADES Y BASES EN SEGURIDAD FRONTERIZA ",0, 'C',False)
    pdf.set_font('Arial Narrow', 'B', 9)
    pdf.ln()
    pdf.cell(125)
    pdf.multi_cell(15,5,"DIVISIÓN",0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(140)
    pdf.multi_cell(29, 5, "UNIDADES", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(169)
    pdf.multi_cell(41, 5, "PASOS FRONTERIZOS SEGÚN DIRECTIVA", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(210)
    pdf.multi_cell(50, 5, "NIVEL COBERTURA PASOS FRONTERIZOS FORMALES Y NO FORMALES", 0, "C", False)

    num = pdf.get_x()
    pdf.ln(-num-5)
    pdf.cell(260)
    pdf.multi_cell(30, 5, "BASES EN FRONTERA", 0, "C", False)

    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(290)
    pdf.multi_cell(30, 5, "TOTAL  HOMBRES EN SEGURIDAD FRONTERIZA", 0, "C", False)

    #codigo para la creacion de los sub encabezados
    pdf.set_font('Arial Narrow', 'B', 7)
    #pdf.ln(-1)
    pdf.cell(140)
    pdf.multi_cell(14.5, 5, "PELOTONES", 0, "C", False)
    
    pdf.ln(-5)
    pdf.cell(154.5)
    pdf.multi_cell(14.5, 5, "EFECTIVOS", 0, "C", False)
    
    pdf.ln(-5)
    pdf.cell(169)
    pdf.multi_cell(13.67, 4, "PASOS FORMALES", 0, "C", False)
    
    pdf.ln(-8)
    pdf.cell(182.67)
    pdf.multi_cell(13.67, 4, "PASOS NO FORMALES", 0, "C", False)
        
    pdf.ln(-8)
    pdf.cell(196.34)
    pdf.multi_cell(13.67, 4, "TOTAL PASOS ", 0, "C", False)

    pdf.ln(-8)
    pdf.cell(210)
    pdf.multi_cell(16.67, 4, "CUBIERTO ", 0, "C", False)
    
    pdf.ln(-4)
    pdf.cell(226.67)
    pdf.multi_cell(16.67, 4, "PARCIALMENTE CUBIERTO", 0, "C", False)
        
    pdf.ln(-8)
    pdf.cell(243.34)
    pdf.multi_cell(16.67, 4, "SIN COBERTURA", 0, "C", False)
       
    pdf.ln(-8)
    pdf.cell(260)
    pdf.multi_cell(15, 4, "BASMIL",0, "C", False)

    pdf.ln(-4)
    pdf.cell(275)
    pdf.multi_cell(15, 4, "EFECTIVOS", 0, "C", False)

    UNIDADES = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08"]

    
    pdf.set_fill_color(221, 235, 247)
    fill = False
    total = 0
    total_efectivos = 0
    total_efectivos_base= 0
    total_base = 0
    def distacia_puntos(punto_1, punto_2):
        punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
        punto_2 = (radians(punto_2[0]), radians(punto_2[1]))
        distacias = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1]-punto_2[1]))
        distacias = (distacias *6371.01)*1000       
        return distacias
    
    def valor(dato):
      
        if dato != "None":
            ofi = dato
        else:
            ofi = 0
          
        return ofi
    pdf.set_font('Arial Narrow', 'B',10)
    unidad=[]
    for x in data:
        if x[20] not in unidad:
            unidad.append(x[20])
                
            if x[35] == "SI":
                total_base = total_base + 1
                total_efectivos_base = total_efectivos_base + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
            if x[35] == "NO":
                total = total + 1
                total_efectivos = total_efectivos + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))

    total_paso_forma = 0
    total_paso_no_forma = 0
    for z in data_2:
            
            if z[11] == "Formal":
                total_paso_forma = total_paso_forma +1
            if z[11] == "No Formal":
                total_paso_no_forma = total_paso_no_forma +1

    total_cubierto = 0
    total_parcial = 0
    total_sin_cobertura = 0
    total_pelotones = 0
    for x in UNIDADES:
        valor_unidad = 0
        valor_unidad_base=0
        efectivos_base=0
        efectivos = 0
        pasos_formal = 0
        paso_no_forma= 0
        cubierto = 0
        parcial = 0
        sin_cobertura = 0
        pelotones = []
        for y in data:
            if x == y[17]:
                if y[20] not in pelotones:
                    pelotones.append(y[20])
                    if y[35] == "NO":
                        valor_unidad = valor_unidad + 1
                        efectivos = efectivos  + int(valor(y[22])) + int(valor(y[23])) + int(valor(y[24])) + int(valor(y[25]))
                    if y[35] == "SI":
                        valor_unidad_base = valor_unidad_base + 1
                        efectivos_base = efectivos_base  + int(valor(y[22])) + int(valor(y[23])) + int(valor(y[24])) + int(valor(y[25]))

                km = 10000
                if y[37] != '' and y[38] != '' and y[40] != ''and y[40] != '':
                    x1=float(y[37])
                    y1=float(y[38])
                    
                    x2=float(y[39])
                    y2=float(y[40])

                    punto_1 = (x1, y1)
                    punto_2 = (x2, y2)

                    km =  distacia_puntos(punto_1, punto_2)
                if km <= 2000:
                    cubierto = cubierto + 1
                elif km >= 2001 and km >= 5000:
                    parcial = parcial + 1
                else:
                    sin_cobertura = sin_cobertura +1
            
        total_cubierto =  total_cubierto + cubierto
        total_parcial =  total_parcial + parcial
        total_sin_cobertura =  total_sin_cobertura + sin_cobertura
        total_pelotones = total_pelotones + len(pelotones)

        for z in data_2:
            if x == z[4]:
                if z[11] == "Formal":
                    pasos_formal = pasos_formal +1
                if z[11] == "No Formal":
                    paso_no_forma = paso_no_forma +1

        pdf.ln()
        pdf.cell(125)
        pdf.cell(15,5,str(x),1,0, 'C',fill)
        pdf.cell(14.5,5,str(len(pelotones)),1,0, 'C',fill)
        pdf.cell(14.5,5,str(efectivos),1,0, 'C',fill)
        pdf.cell(13.67,5,str(pasos_formal),1,0, 'C',fill)
        pdf.cell(13.67,5,str(paso_no_forma),1,0, 'C',fill)
        pdf.cell(13.67,5,str(pasos_formal+ paso_no_forma),1,0, 'C',fill)
        pdf.cell(16.67,5,str(cubierto),1,0, 'C',fill)
        pdf.cell(16.67,5,str(parcial),1,0, 'C',fill)
        pdf.cell(16.67,5,str(sin_cobertura),1,0, 'C',fill)
        pdf.cell(15,5,str(valor_unidad_base),1,0, 'C',fill)
        pdf.cell(15,5,str(efectivos_base),1,0, 'C',fill)
        pdf.cell(30,5,str(efectivos + efectivos_base),1,0, 'C',fill)
        if fill == True:
            fill = False
        else:
            fill = True
    pdf.set_font('Arial Narrow', 'B', 14)
    pdf.ln()
    fill = True
    pdf.set_fill_color(180, 180, 180)
    pdf.cell(125)
    pdf.cell(15,10,str("TOTAL"),1,0, 'C',fill)
    pdf.cell(14.5,10,str(total_pelotones),1,0, 'C',fill)
    pdf.cell(14.5,10,str(total_efectivos),1,0, 'C',fill)
    pdf.cell(13.67,10,str(total_paso_forma),1,0, 'C',fill)
    pdf.cell(13.67,10,str(total_paso_no_forma),1,0, 'C',fill)
    pdf.cell(13.67,10,str(total_paso_forma+ total_paso_no_forma),1,0, 'C',fill)
    pdf.cell(16.67,5,str(total_cubierto),1,0, 'C',fill)
    pdf.cell(16.67,5,str(total_parcial),1,0, 'C',fill)
    pdf.cell(16.67,5,str(total_sin_cobertura),1,0, 'C',fill)
    pdf.cell(15,10,str(total_base),1,0, 'C',fill)
    pdf.cell(15,10,str(total_efectivos_base),1,0, 'C',fill)
    pdf.cell(30,10,str(total_efectivos +total_efectivos_base),1,0, 'C',fill)
    pdf.ln()
    pdf.ln(-5)
    pdf.cell(210)
    pdf.cell(50,5,str(total_cubierto + total_parcial + total_sin_cobertura),1,0, 'C',fill)


    #cuadro numero dos
    # --------------------------
    # ------------------------- 

    pdf.set_fill_color(200, 200, 200)
    pdf.rect(120,159,25,5,"FD")#unidades
    pdf.rect(120,164,25,10,"FD")#unidades
    pdf.rect(120,174,25,5,"FD")#unidades
    
    pdf.rect(145,159,30,5,"FD")#unidades
    pdf.rect(145,164,30,10,"FD")#unidades
    pdf.rect(145,174,30,5,"FD")#unidades
    
    pdf.set_fill_color(73, 101, 55)
    pdf.rect(120,149,25,10,"FD")#unidades
    pdf.rect(145,149,30,10,"FD")#unidades
    pdf.rect(175,149,30,10,"FD")#unidades
    pdf.rect(205,149,20,10,"FD")#unidades

    pdf.set_fill_color(0, 176, 80)
    pdf.rect(175,159,30,5,"FD")#unidades
    pdf.rect(205,159,20,5,"FD")#unidades

    pdf.set_fill_color(255, 255, 0)
    pdf.rect(175,164,30,10,"FD")#unidades
    pdf.rect(205,164,20,10,"FD")#unidades

    pdf.set_fill_color(255, 0, 0)
    pdf.rect(175,174,30,5,"FD")#unidades
    pdf.rect(205,174,20,5,"FD")#unidades

    pdf.set_font('Arial Narrow', 'B', 9)
    pdf.ln(40)
    pdf.cell(110)
    pdf.multi_cell(25,5,"TOTAL PASOS",0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(135)
    pdf.multi_cell(30, 5, "DISTANCIA", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(165)
    pdf.multi_cell(30, 5, "SEMAFORIZACIÓN", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(195)
    pdf.multi_cell(20, 5, "NIVEL DE COBERTURA", 0, "C", False)
    por =  (total_cubierto/221)*100
    por = format(por, '0.2f')+" %"
    pdf.cell(110)
    pdf.multi_cell(25,5,str(total_cubierto),0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(135)
    pdf.multi_cell(30, 5, "0 a 2000 mts", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(165)
    pdf.multi_cell(30, 5, "CUBIERTOS", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(195)
    pdf.multi_cell(20, 5, str(por), 0, "C", False)

    por =  (total_parcial/221)*100
    por = format(por, '0.2f')+" %"
    pdf.cell(110)
    pdf.multi_cell(25,5,str(total_parcial),0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(135)
    pdf.multi_cell(30, 5, "2.001 mts a 5.000 mts", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(165)
    pdf.multi_cell(30, 5, "PARCIALMENTE CUBIERTOS", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num)
    pdf.cell(195)
    pdf.multi_cell(20, 5, str(por), 0, "C", False)
    pdf.ln()


    por =  (total_sin_cobertura/221)*100
    por = format(por, '0.2f')+" %"
    pdf.cell(110)
    pdf.multi_cell(25,5,str(total_sin_cobertura),0, 'C',False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(135)
    pdf.multi_cell(30, 5, "5.001 mts ó Más", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(165)
    pdf.multi_cell(30, 5, "SIN COBERTURA", 0, "C", False)
    num = pdf.get_x()
    pdf.ln(-num+5)
    pdf.cell(195)
    pdf.multi_cell(20, 5, str(por), 0, "C", False)
    img = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/resultados/hombres.png"
    pdf.image(img,235,140,30,24)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(270,150,str("TOTAL HOMBRES"))
    pdf.set_font('BebasNeue', '', 26)
    pdf.text(270,160,str(total_efectivos +total_efectivos_base))

    img = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/resultados/base.png"
    pdf.image(img,235,170,30,24)

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 18)
    pdf.text(270,180,str("TOTAL BASES"))
    pdf.set_font('BebasNeue', '', 26)
    pdf.text(270,190,str(total_base))

    pdf.set_line_width(1)
    pdf.set_draw_color(130, 130, 130) 
    pdf.line(265, 145, 265, 160)  
    pdf.line(265, 175, 265, 190)
    #codigo_guadar
    UNIDADES = ["DIV01","DIV02","DIV03","DIV04","DIV06","DIV07","DIV08"]
    frontera =[("DIV01","VENEZUELA", "403 km"), ("DIV02","VENEZUELA", "421 km"), ("DIV03","ECUADOR", "586 km"), ("DIV04","BRASIL", "1.043 km"), ("DIV07","PANAMA", "266 km"), ("DIV08","VENEZUELA", "1.996 km")]

    for z in UNIDADES:
        point=[]
        point_fronteriza=[]
        point_base = []
        pasos_formal=0
        paso_no_forma=0
        valor_unidad_base = 0
        total_efectivos_base=0
        total_efectivos=0

        for x in data:
            if x[17]==z:

                if x[38] != "" and [39] != "":
                    point.append(x)

                if x[35] == "SI":
                    valor_unidad_base = valor_unidad_base + 1
                    total_efectivos_base = total_efectivos_base + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
                    if x[20] not in point_base:
                        point_base.append(x[20])

                if x[35] == "NO":
                    total = total + 1
                    total_efectivos = total_efectivos + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
                    if x[20] not in point_fronteriza:
                        point_fronteriza.append(x[20])


        formal=[]
        no_forma=[]

        for x in data_2:
            if x[4]==z:
                if x[11] == "Formal":
                    formal.append(x)
                else:
                    no_forma.append(x)

                if x[11] == "Formal":
                    pasos_formal = pasos_formal +1
                if x[11] == "No Formal":
                    paso_no_forma = paso_no_forma +1
        pais=""
        extencion =""
        for fr in frontera:
           if fr[0] == z:
                pais = fr[1]
                extencion = fr[2]

        EVENTOS_id_2(ruta, formal, no_forma, point, z)
        mapa_img = str(z)+str("_pasos.png")
        mapa = '{}static/img/img_mapas/{}'.format(ruta, mapa_img)
        titulo = "NIVEL DE SEGURIDAD FRONTERIZO"
        lamina = z+".JPG"
        pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/divisiones_2025/", imagen = lamina, titulo= titulo, fecha_titulo= fecha_titulo, mapa=mapa, unidad_png = z, tipo ="mapa_evento")

        pdf.add_page()
        pdf.set_auto_page_break(True, 10)
        pdf.set_font('BebasNeue', '', 12)


     #pdf.ln()
        numero = 1
        total_ofi_pasos =0
        total_sub_pasos= 0
        total_slp_pasos= 0
        total_sl18_pasos= 0
        total_paso_forma = 0
        total_paso_no_forma = 0

        total_cubierto =0
        total_parcial =0
        total_sin_cobertura =0

        peloton_total = []
        for x in point_fronteriza:
            div = ""
            br = ""
            ut = ""
            ind = ""
            cdte = ""
            ofi = 0
            sub = 0
            slp = 0
            sl18 = 0
            formal_paso = 0
            no_formal_paso = 0
            cubierto = 0
            parcial = 0
            sin_cobertura = 0
            peloton = 0
            for xz in data:
                if x == xz[20]:
                    if x not in peloton_total:
                        peloton_total.append(x)
                        
                        ofi = ofi + int(valor(xz[22]))
                        sub = sub + int(valor(xz[23]))
                        slp = slp + int(valor(xz[24]))
                        sl18 = sl18 + int(valor(xz[25]))
                    peloton = peloton +1
                    div = str(xz[17])
                    br = str(xz[18])
                    ut = str(xz[19])
                    ind = str(xz[20])
                    cdte = str(xz[21])

                    
                    if xz[4] == "FORMAL":
                        formal_paso = formal_paso +1
                    else:
                        no_formal_paso = no_formal_paso +1

                    km = 10000
                    if xz[37] != '' and xz[38] != '' and xz[40] != ''and xz[40] != '':
                        x1=float(xz[37])
                        y1=float(xz[38])
                        
                        x2=float(xz[39])
                        y2=float(xz[40])

                        punto_1 = (x1, y1)
                        punto_2 = (x2, y2)

                        km =  distacia_puntos(punto_1, punto_2)
                    if km <= 2000:
                        cubierto = cubierto + 1
                    elif km >= 2001 and km >= 5000:
                        parcial = parcial + 1
                    else:
                        sin_cobertura = sin_cobertura +1


            total_ofi_pasos = total_ofi_pasos + ofi
            total_sub_pasos = total_sub_pasos + sub
            total_slp_pasos = total_slp_pasos + slp
            total_sl18_pasos = total_sl18_pasos+ sl18
            total_paso_forma = total_paso_forma + formal_paso
            total_paso_no_forma = total_paso_no_forma + no_formal_paso
            total_cubierto = total_cubierto + cubierto
            total_parcial = total_parcial + parcial
            total_sin_cobertura = total_sin_cobertura + sin_cobertura

        peloton_total_base=[]
        if point_base !=[]:
                

            numero = 1
            total_ofi =0
            total_sub= 0
            total_slp= 0
            total_sl18= 0
            total_paso_forma = 0
            total_paso_no_forma = 0

            for x in point_base:
                div = ""
                br = ""
                ut = ""
                ind = ""
                cdte = ""
                dtop = ""
                mpio = ""
                nombra_base = ""
                ofi = 0
                sub = 0
                slp = 0
                sl18 = 0
                formal_paso = 0
                no_formal_paso = 0
                cubierto = 0
                parcial = 0
                sin_cobertura = 0
                distacian_km = 0
                c = 0
                for xz in data:
                    if x == xz[20]:
                        if x not in peloton_total_base:
                            peloton_total_base.append(x)
                            ofi = ofi + int(valor(xz[22]))
                            sub = sub + int(valor(xz[23]))
                            slp = slp + int(valor(xz[24]))
                            sl18 = sl18 + int(valor(xz[25]))
                        dtop = str(xz[14])
                        mpio = str(xz[15])
                        div = str(xz[17])
                        br = str(xz[18])
                        ut = str(xz[19])
                        ind = str(xz[20])
                        cdte = str(xz[21])
                        nombra_base = str(xz[3])
                        distacian_km = str(xz[34])

                        
                        if xz[4] == "FORMAL":
                            formal_paso = formal_paso +1
                        else:
                            no_formal_paso = no_formal_paso +1

                        km = 10000
                        if xz[37] != '' and xz[38] != '' and xz[40] != ''and xz[40] != '':
                            x1=float(xz[37])
                            y1=float(xz[38])
                            
                            x2=float(xz[39])
                            y2=float(xz[40])

                            punto_1 = (x1, y1)
                            punto_2 = (x2, y2)

                            km =  distacia_puntos(punto_1, punto_2)


                total_ofi = total_ofi + ofi
                total_sub = total_sub + sub
                total_slp = total_slp + slp
                total_sl18 = total_sl18 + sl18
                total_paso_forma = total_paso_forma + formal_paso
                total_paso_no_forma = total_paso_no_forma + no_formal_paso
    


        total_efe_base=0
        total_efe_pasos=0

        total_efe_base = total_ofi + total_sub + total_slp + total_sl18
        total_efe_pasos = total_ofi_pasos + total_sub_pasos + total_slp_pasos + total_sl18_pasos

        inf_frontera_div(pdf, "FRONTERA", pais, "paso_1", 150, 35)
        inf_frontera_div(pdf, "EXTENCIÓN", extencion, "punto_2", 220, 35)
        inf_frontera_div(pdf, "TOTAL BASES", valor_unidad_base, "base", 280, 35)

        inf_frontera_div(pdf, "PASOS FORMALES", pasos_formal, "paso_2", 150, 70)
        inf_frontera_div(pdf, "PASOS NO FORMALES", paso_no_forma, "paso_3", 215, 70)
        inf_frontera_div(pdf, "TOTAL PASOS ", (paso_no_forma+pasos_formal), "paso_1", 285, 70)

        inf_frontera_div(pdf, "HOMBRES BASES", (total_efe_base), "hombres", 150, 105)
        inf_frontera_div(pdf, "HOMBRES PASOS", (total_efe_pasos), "hombres", 215, 105)
        inf_frontera_div(pdf, "PELOTONES BASES", (len(peloton_total_base)), "PEL", 280, 105)

        inf_frontera_div(pdf, "PELOTONES PASOS FRONTERIZOS", (len(peloton_total)), "PEL", 145, 140)
        inf_frontera_div(pdf, "PELOTONES", (len(peloton_total)+ len(peloton_total_base)), "PEL", 235, 140)
        inf_frontera_div(pdf, "TOTAL EFECTIVOS", (total_efe_base+total_efe_pasos), "hombres", 282, 140)

        inf_frontera_div(pdf, "CUBIERTOS", total_cubierto, "baedera_verde", 150, 175)
        inf_frontera_div(pdf, "PARC. CUBIERTOS", total_parcial, "baedera_amarilla", 220, 175)
        inf_frontera_div(pdf, "SIN CUBRIR", total_sin_cobertura, "baedera_roja", 280, 175)


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
 

    direcion =  LINK+"Reporte Pazos Fronterizos.pdf"
    pdf.output(direcion, 'F')

    DIRECION = os.getenv('DIRECION_3')
    titulo = "Reporte Pazos Fronterizos"


    direcion= DIRECION+str("Reporte Pazos Fronterizos.pdf")
 
    return [direcion, titulo]
 

def dash_reporte_pasos_fronteras(dato):
    fecha_pazos =  dato["fecha_pasos_informacion"]

    das_general=[]

    conn = connect()
    cursor = conn.cursor()

    query = """select * from  pazos_fronterizos where fecha_pazos = '{}';""".format(fecha_pazos)
    cursor.execute(query)
    data = cursor.fetchall()

    query_2 = """select * from  pazos_fronterizos_directiva """

    cursor.execute(query_2)
    data_2 = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close
    numero = 0

    point=[]
    for x in data:
        if x[38] != "" and [39] != "":
            point.append(x)

    formal=[]
    no_forma=[]
    for x in data_2:
        if x[11] == "Formal":
            formal.append(x)
        else:
            no_forma.append(x)

    DIRECION = os.getenv('DIRECION')   
    ruta = DIRECION
    #se llam la funcion para la cracion del mapa

    EVENTOS(ruta, formal, no_forma, point)



    #-----------------------------------------
    #-----tabla de los pasos fronterisos------
    #-----------------------------------------
 


    UNIDADES = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08"]

    
    fill = False
    total = 0
    total_efectivos = 0
    total_efectivos_base= 0
    total_base = 0
    def distacia_puntos(punto_1, punto_2):
        punto_1 = (radians(punto_1[0]), radians(punto_1[1]))
        punto_2 = (radians(punto_2[0]), radians(punto_2[1]))
        distacias = acos(sin(punto_1[0])*sin(punto_2[0]) + cos(punto_1[0])*cos(punto_2[0])*cos(punto_1[1]-punto_2[1]))
        distacias = (distacias *6371.01)*1000       
        return distacias
    
    def valor(dato):
      
        if dato != "None":
            ofi = dato
        else:
            ofi = 0
          
        return ofi

    unidad=[]
    for x in data:
        if x[20] not in unidad:
            unidad.append(x[20])
                
            if x[35] == "SI":
                total_base = total_base + 1
                total_efectivos_base = total_efectivos_base + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
            if x[35] == "NO":
                total = total + 1
                total_efectivos = total_efectivos + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))

    total_paso_forma = 0
    total_paso_no_forma = 0
    for z in data_2:
            
            if z[11] == "Formal":
                total_paso_forma = total_paso_forma +1
            if z[11] == "No Formal":
                total_paso_no_forma = total_paso_no_forma +1

    total_cubierto = 0
    total_parcial = 0
    total_sin_cobertura = 0
    total_pelotones = 0
    for x in UNIDADES:
        valor_unidad = 0
        valor_unidad_base=0
        efectivos_base=0
        efectivos = 0
        pasos_formal = 0
        paso_no_forma= 0
        cubierto = 0
        parcial = 0
        sin_cobertura = 0
        pelotones = []
        for y in data:
            if x == y[17]:
                if y[20] not in pelotones:
                    pelotones.append(y[20])
                    if y[35] == "NO":
                        valor_unidad = valor_unidad + 1
                        efectivos = efectivos  + int(valor(y[22])) + int(valor(y[23])) + int(valor(y[24])) + int(valor(y[25]))
                    if y[35] == "SI":
                        valor_unidad_base = valor_unidad_base + 1
                        efectivos_base = efectivos_base  + int(valor(y[22])) + int(valor(y[23])) + int(valor(y[24])) + int(valor(y[25]))

                km = 10000
                if y[37] != '' and y[38] != '' and y[40] != ''and y[40] != '':
                    x1=float(y[37])
                    y1=float(y[38])
                    
                    x2=float(y[39])
                    y2=float(y[40])

                    punto_1 = (x1, y1)
                    punto_2 = (x2, y2)

                    km =  distacia_puntos(punto_1, punto_2)
                if km <= 2000:
                    cubierto = cubierto + 1
                elif km >= 2001 and km >= 5000:
                    parcial = parcial + 1
                else:
                    sin_cobertura = sin_cobertura +1
            
        total_cubierto =  total_cubierto + cubierto
        total_parcial =  total_parcial + parcial
        total_sin_cobertura =  total_sin_cobertura + sin_cobertura
        total_pelotones = total_pelotones + len(pelotones)

        for z in data_2:
            if x == z[4]:
                if z[11] == "Formal":
                    pasos_formal = pasos_formal +1
                if z[11] == "No Formal":
                    paso_no_forma = paso_no_forma +1


        if fill == True:
            fill = False
        else:
            fill = True

    das_general =[ ("Pelotones", "PEL", total_pelotones ), ("Efectivos Pasos", "hombres", total_efectivos),("Total Bases", "base", total_base), ("Efectivos Bases", "base", total_efectivos_base), ("Total Efectivos", "hombres", (total_efectivos_base + total_efectivos)), ("Pasos Formales", "paso_2", len(formal)),("Pasos no Formales", "paso_3", len(no_forma)),("Total Pasos", "paso_1", (len(formal)+len(no_forma))), ("Cubiertos", "baedera_verde", total_sin_cobertura), ("Parcialmente cubiertos", "baedera_amarilla", total_parcial), ("Sin Coberturas", "baedera_roja", total_sin_cobertura)]
    #cuadro numero dos
    # --------------------------
    # ------------------------- 

    #codigo_guadar
    UNIDADES = ["DIV01","DIV02","DIV03","DIV04","DIV06","DIV07","DIV08"]
    frontera =[("DIV01","VENEZUELA", "403 km", "div01_ayuda"), ("DIV02","VENEZUELA", "421 km", "div02_ayuda"), ("DIV03","ECUADOR", "586 km", "div03_ayuda"), ("DIV04","BRASIL", "1.043 km", "div04_ayuda"), ("DIV06","PANAMA", "266 km", "div06_ayuda"), ("DIV07","PANAMA", "266 km", "div07_ayuda"), ("DIV08","VENEZUELA", "1.996 km", "div08_ayuda")]
    dash_divisiones = []
    for z in UNIDADES:
        point=[]
        point_fronteriza=[]
        point_base = []
        pasos_formal=0
        paso_no_forma=0
        valor_unidad_base = 0
        total_efectivos_base=0
        total_efectivos=0

        for x in data:
            if x[17]==z:

                if x[38] != "" and [39] != "":
                    point.append(x)

                if x[35] == "SI":
                    valor_unidad_base = valor_unidad_base + 1
                    total_efectivos_base = total_efectivos_base + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
                    if x[20] not in point_base:
                        point_base.append(x[20])

                if x[35] == "NO":
                    total = total + 1
                    total_efectivos = total_efectivos + int(valor(x[22])) + int(valor(x[23])) + int(valor(x[24])) + int(valor(x[25]))
                    if x[20] not in point_fronteriza:
                        point_fronteriza.append(x[20])


        formal=[]
        no_forma=[]

        for x in data_2:
            if x[4]==z:
                if x[11] == "Formal":
                    formal.append(x)
                else:
                    no_forma.append(x)

                if x[11] == "Formal":
                    pasos_formal = pasos_formal +1
                if x[11] == "No Formal":
                    paso_no_forma = paso_no_forma +1
        pais=""
        extencion =""
        escudo=""
        for fr in frontera:
           if fr[0] == z:
                pais = fr[1]
                extencion = fr[2]
                escudo = fr[3]



     #pdf.ln()
        numero = 1
        total_ofi_pasos =0
        total_sub_pasos= 0
        total_slp_pasos= 0
        total_sl18_pasos= 0
        total_paso_forma = 0
        total_paso_no_forma = 0

        total_cubierto =0
        total_parcial =0
        total_sin_cobertura =0

        peloton_total = []
        for x in point_fronteriza:
            div = ""
            br = ""
            ut = ""
            ind = ""
            cdte = ""
            ofi = 0
            sub = 0
            slp = 0
            sl18 = 0
            formal_paso = 0
            no_formal_paso = 0
            cubierto = 0
            parcial = 0
            sin_cobertura = 0
            peloton = 0
            for xz in data:
                if x == xz[20]:
                    if x not in peloton_total:
                        peloton_total.append(x)
                        
                        ofi = ofi + int(valor(xz[22]))
                        sub = sub + int(valor(xz[23]))
                        slp = slp + int(valor(xz[24]))
                        sl18 = sl18 + int(valor(xz[25]))
                    peloton = peloton +1
                    div = str(xz[17])
                    br = str(xz[18])
                    ut = str(xz[19])
                    ind = str(xz[20])
                    cdte = str(xz[21])

                    
                    if xz[4] == "FORMAL":
                        formal_paso = formal_paso +1
                    else:
                        no_formal_paso = no_formal_paso +1

                    km = 10000
                    if xz[37] != '' and xz[38] != '' and xz[40] != ''and xz[40] != '':
                        x1=float(xz[37])
                        y1=float(xz[38])
                        
                        x2=float(xz[39])
                        y2=float(xz[40])

                        punto_1 = (x1, y1)
                        punto_2 = (x2, y2)

                        km =  distacia_puntos(punto_1, punto_2)
                    if km <= 2000:
                        cubierto = cubierto + 1
                    elif km >= 2001 and km >= 5000:
                        parcial = parcial + 1
                    else:
                        sin_cobertura = sin_cobertura +1


            total_ofi_pasos = total_ofi_pasos + ofi
            total_sub_pasos = total_sub_pasos + sub
            total_slp_pasos = total_slp_pasos + slp
            total_sl18_pasos = total_sl18_pasos+ sl18
            total_paso_forma = total_paso_forma + formal_paso
            total_paso_no_forma = total_paso_no_forma + no_formal_paso
            total_cubierto = total_cubierto + cubierto
            total_parcial = total_parcial + parcial
            total_sin_cobertura = total_sin_cobertura + sin_cobertura

        peloton_total_base=[]
        if point_base !=[]:
                

            numero = 1
            total_ofi =0
            total_sub= 0
            total_slp= 0
            total_sl18= 0
            total_paso_forma = 0
            total_paso_no_forma = 0

            for x in point_base:
                div = ""
                br = ""
                ut = ""
                ind = ""
                cdte = ""
                dtop = ""
                mpio = ""
                nombra_base = ""
                ofi = 0
                sub = 0
                slp = 0
                sl18 = 0
                formal_paso = 0
                no_formal_paso = 0
                cubierto = 0
                parcial = 0
                sin_cobertura = 0
                distacian_km = 0
                c = 0
                for xz in data:
                    if x == xz[20]:
                        if x not in peloton_total_base:
                            peloton_total_base.append(x)
                            ofi = ofi + int(valor(xz[22]))
                            sub = sub + int(valor(xz[23]))
                            slp = slp + int(valor(xz[24]))
                            sl18 = sl18 + int(valor(xz[25]))
                        dtop = str(xz[14])
                        mpio = str(xz[15])
                        div = str(xz[17])
                        br = str(xz[18])
                        ut = str(xz[19])
                        ind = str(xz[20])
                        cdte = str(xz[21])
                        nombra_base = str(xz[3])
                        distacian_km = str(xz[34])

                        
                        if xz[4] == "FORMAL":
                            formal_paso = formal_paso +1
                        else:
                            no_formal_paso = no_formal_paso +1

                        km = 10000
                        if xz[37] != '' and xz[38] != '' and xz[40] != ''and xz[40] != '':
                            x1=float(xz[37])
                            y1=float(xz[38])
                            
                            x2=float(xz[39])
                            y2=float(xz[40])

                            punto_1 = (x1, y1)
                            punto_2 = (x2, y2)

                            km =  distacia_puntos(punto_1, punto_2)


                total_ofi = total_ofi + ofi
                total_sub = total_sub + sub
                total_slp = total_slp + slp
                total_sl18 = total_sl18 + sl18
                total_paso_forma = total_paso_forma + formal_paso
                total_paso_no_forma = total_paso_no_forma + no_formal_paso
    


            

        total_efe_base=0
        total_efe_pasos=0

        total_efe_base = total_ofi + total_sub + total_slp + total_sl18
        total_efe_pasos = total_ofi_pasos + total_sub_pasos + total_slp_pasos + total_sl18_pasos
        dato = ("Div", escudo, z,"Frontera", "paso_1", pais,"EXTENCIÓN", "punto_2", extencion,"Total Bases", "base", valor_unidad_base,"Pasos Formales", "paso_2", pasos_formal,"Pasos No Formales", "paso_3", paso_no_forma,"Total Pasos", "paso_1", (pasos_formal+paso_no_forma),"Personal Bases", "hombres", total_efe_base,"Personal Pasos", "hombres", total_efe_pasos,"Total Efectivos", "hombres", (total_efe_base+total_efe_pasos),"Pelotones Bases", "PEL", len(peloton_total_base),"Pelotones Pasos", "PEL", len(peloton_total),"Total Pelotones", "PEL", (len(peloton_total)+len(peloton_total_base)),"CUBIERTOS", "baedera_verde", total_cubierto,"PARC. CUBIERTOS", "baedera_amarilla", total_parcial,"SIN CUBRIR", "baedera_roja", total_sin_cobertura)
   

        dash_divisiones.append(dato)

        total_efe_base = total_ofi + total_sub + total_slp + total_sl18
        total_efe_pasos = total_ofi_pasos + total_sub_pasos + total_slp_pasos + total_sl18_pasos

    label=["Total Bases", "Pasos Formales", "Pasos No Formales", "Total Pasos", "Personal Bases", "Personal Pasos", "Total Efectivos", "Pelotones Bases", "Pelotones Pasos", "Total Pelotones", "CUBIERTOS", "PARC. CUBIERTOS", "SIN CUBRIR"]    
    return [das_general, dash_divisiones, UNIDADES, label]
 



def rotar_pdf_temporal(imagen, mapa, temp_pdf_path, pdf, fecha_pazos, fechas_inicial_1, fechas_inicial_2, fechas_inicial_3, division):
    pdf_temp = PDF(orientation='L', unit='mm', format=(130,210))
    pdf_temp.parametros(
        pie_pagina="NO",
        ruta="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/cartilla consejos/",
        imagen=imagen,
        titulo='',
        fecha_titulo='',
        mapa=mapa,
        tipo="reporte",
        y_pdf=210,
        x_pdf=130
    )
    pdf_temp.add_page()
    pdf_temp.set_auto_page_break(True, 3)
    cuadros_caulculo = Funciones_eleciones(pdf_temp, fecha_pazos, fechas_inicial_1, fechas_inicial_2, fechas_inicial_3)
    if imagen == 'Diapositiva_fondo (1).JPG':
        cuadros_caulculo.lamina_4()
    else:
        cuadros_caulculo.lamina_7(division)

    os.makedirs(os.path.dirname(temp_pdf_path), exist_ok=True)
    pdf_temp.output(temp_pdf_path, 'F')

    # Rotar PDF temporal y devolver PdfReader
    reader = PdfReader(temp_pdf_path)
    writer = PdfWriter()
    for page in reader.pages:
        page.rotate(-90)
        writer.add_page(page)

    with open(temp_pdf_path, "wb") as f:
        writer.write(f)

    return PdfReader(temp_pdf_path)  # Retorna el PDF rotado listo para insertar



def reporte_eleciones_pdf(contents):
    fecha_pazos = contents["fecha"]
    actualizarMapas = contents["actualizarMapas"]
    DIRECION = os.getenv('DIRECION')
    ruta = DIRECION

    pdf = PDF(orientation='L', unit='mm', format=(210,130))
    fechas_inicial = fecha(fecha_pazos)
    fecha_titulo = f"{fechas_inicial[0]} de {fechas_inicial[1]} del {fechas_inicial[2]}".upper()

    mapa = os.path.join(ruta, 'static/img/img_mapas/PAZOS.png')
    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
    direcion_final = os.path.join(LINK, "Reporte Pazos Fronterizos.pdf")

    caligrafia_ingreso( pdf, ruta)

    divisiones = [
        {"nombre": "EJC", "diapositivas": ["Diapositiva (2).JPG","Diapositiva (3).JPG","Diapositiva_fondo (1).JPG"]},
        {"nombre": "DIV01", "diapositivas": ["Diapositiva (4).JPG","Diapositiva (5).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (2).JPG"]},
        {"nombre": "DIV02", "diapositivas": ["Diapositiva (7).JPG","Diapositiva (8).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (3).JPG"]},
        {"nombre": "DIV03", "diapositivas": ["Diapositiva (9).JPG","Diapositiva (10).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (2).JPG"]},
        {"nombre": "DIV04", "diapositivas": ["Diapositiva (11).JPG","Diapositiva (12).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (3).JPG"]},
        {"nombre": "DIV05", "diapositivas": ["Diapositiva (13).JPG","Diapositiva (14).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (2).JPG"]},
        {"nombre": "DIV06", "diapositivas": ["Diapositiva (15).JPG","Diapositiva (16).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (3).JPG"]},
        {"nombre": "DIV07", "diapositivas": ["Diapositiva (17).JPG","Diapositiva (18).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (2).JPG"]},
        {"nombre": "DIV08", "diapositivas": ["Diapositiva (19).JPG","Diapositiva (20).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (3).JPG"]},
        {"nombre": "FUTOM", "diapositivas": ["Diapositiva (21).JPG","Diapositiva (22).JPG","Diapositiva (6).JPG","Diapositiva (3).JPG","Diapositiva_fondo (3).JPG"]}
    ]

    cuadros_caulculo = Funciones_eleciones(pdf, fecha_pazos, fechas_inicial[0], fechas_inicial[4], fechas_inicial[2])

    # Objeto final para combinar PDFs
    writer_final = PdfWriter()

    for division in divisiones:
        print("📌 División:", division["nombre"])
        for d in division["diapositivas"]:
            if d.startswith("Diapositiva_fondo"):
                # Crear PDF temporal del fondo rotado
                temp_pdf = 'C:/temp/temp_rotado.pdf'
                rotar_pdf_temporal(d, mapa, temp_pdf, pdf, fecha_pazos, fechas_inicial[0], fechas_inicial[4], fechas_inicial[2], division["nombre"])

                # Leer el PDF temporal y agregar al flujo
                reader_temp = PdfReader(temp_pdf)
                for page in reader_temp.pages:
                    writer_final.add_page(page)
            else:
                base_path = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/cartilla consejos/"

                img_path = os.path.join(base_path, d)

                #print("✅ Ruta construida:", img_path)

                if not os.path.exists(img_path):
                    raise FileNotFoundError(f"No se encontró la imagen: {img_path}")

                # ✅ Crear un objeto PDF nuevo por cada página
                pdf_temp = PDF(orientation='L', unit='mm', format=(210,130))
                pdf_temp.parametros(
                    pie_pagina="NO",
                    ruta=base_path,
                    imagen=d,
                    titulo='',
                    fecha_titulo='',
                    mapa=mapa,
                    tipo="reporte",
                    y_pdf=130,
                    x_pdf=210
                )
                pdf_temp.add_page()

                if d == "Diapositiva (3).JPG":
                    cuadros_caulculo.lamina_3(pdf_temp, division["nombre"])

                if d == 'Diapositiva (5).JPG' or d == 'Diapositiva (8).JPG' or d == 'Diapositiva (10).JPG' or d == 'Diapositiva (12).JPG' or d == 'Diapositiva (14).JPG' or d == 'Diapositiva (16).JPG' or d == 'Diapositiva (18).JPG' or d == 'Diapositiva (20).JPG' or d == 'Diapositiva (22).JPG':
                    cuadros_caulculo.lamina_5(pdf_temp, division["nombre"], actualizarMapas)

                if d == "Diapositiva (6).JPG":
                    cuadros_caulculo.lamina_6(pdf_temp, division["nombre"])


                # Guardar y agregar al flujo
                temp_page_pdf = 'C:/temp/temp_page.pdf'
                pdf_temp.output(temp_page_pdf, 'F')
                reader_page = PdfReader(temp_page_pdf)
                for page in reader_page.pages:
                    writer_final.add_page(page)


    # Guardar PDF final
    os.makedirs(os.path.dirname(direcion_final), exist_ok=True)
    with open(direcion_final, "wb") as f:
        writer_final.write(f)
    direcion= DIRECION+str("Reporte Pazos Fronterizos.pdf")
    titulo = "Reporte Pazos Fronterizos"
    return [direcion, titulo]
