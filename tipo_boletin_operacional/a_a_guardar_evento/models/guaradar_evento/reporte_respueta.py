from datetime import datetime, timedelta
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
from __init__ import *

from ..reportes_matriz import *
import matplotlib.pyplot as plt
import seaborn as sns

from ..funciones.mapa_filtro import *

#Funcion de resultados nueva ayuda
#pip install seaborn
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def validacion_cantidad_tupla(tupla):
                  
    if len(tupla) == 1:
        valor = " and id = '"+tupla[0]+"'"
        
    else:
        tupla = tuple(tupla)
        valor = " and id in {}" .format(tupla)
    return valor 

def informe_pendiente(datos):

    #datos

    fecha_evento =datos["fecha_evento"]
    fecha_evento_final =datos["fecha_evento_final"]
    tipo_evento =datos["tipo_evento"]

    eventos_relevantes_selecionados =datos["eventos_relevantes_selecionados"]

    eventos_relevantes_selecionados=eventos_relevantes_selecionados.split(",")
    filtro_2 = validacion_cantidad_tupla(eventos_relevantes_selecionados)


    fechas=""
    if fecha_evento and fecha_evento_final:
        filtro_fecha = "where fecha_evento >= '{}'  AND fecha_evento <= '{}'".format(fecha_evento, fecha_evento_final,)
        fechas=""
    else:
        filtro_fecha = ""
        fechas="1"
    if tipo_evento !="null" and tipo_evento:

        if fechas =="":
            filtro = "and tipo_evento = '{}'".format(tipo_evento)
        elif fechas=="1":
            filtro = "where tipo_evento = '{}'".format(tipo_evento)
    else:
        filtro =""

    if eventos_relevantes_selecionados!=['']:
        filtro_3 = filtro_2
    else:
        filtro_3=""

    conn = connect()
    cursor = conn.cursor()

    query="select * from registro_eventos_relevantes  {} {} {} order by fecha_evento asc, hora_evento asc".format(filtro_fecha, filtro, filtro_3)

    cursor.execute(query)
    data = cursor.fetchall()
  
    unidades = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","DAVAA","DIVFE","FUTCO","FTCEC","TREJC", "-"]
    data = sorted(data, key = lambda m: unidades.index(m[3]))
    
    conn.commit()
    conn.close()
    cursor.close

    numero = 0
    datos_f=[]
    datos_final=[]
    for x in data:
        numero =numero+1
        datos_f = list(x)
        datos_f.append(numero)
        datos_final.append(datos_f)
    
    positivos = list(filter(lambda data: "POSITIVO" in data[25], data))
    negativos = list(filter(lambda data: "NEGATIVO" in data[25], data))

    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/"
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

    fechas_inicial = fecha(fecha_evento)
    fechas_final = fecha(fecha_evento_final)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()
    
    datos=[negativos, positivos]
    DIRECION = os.getenv('DIRECION')   
    ruta = DIRECION

    EVENTOS(datos, ruta, datos_final)
    mapa = '{}static/img/img_mapas/EVENTOS.png'.format(ruta)
    

    pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/oficio/", imagen = "Diapositiva20.JPG", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/QR.png", titulo= "EVENTOS RELEVANTES", fecha_titulo= fecha_titulo,mapa=mapa)


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)

    pdf.add_page()
    pdf.set_auto_page_break(True, 10)


    pdf.set_font('BebasNeue', '', 12)
    numero=1
    
    for x in data:

        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial Narrow', 'B', 14)
        pdf.cell(130)   
        pdf.multi_cell(10, 5, str(numero), 0, "C", False)
        num = pdf.get_x()
        pdf.ln(-num+5)
        if x[25] == "POSITIVO":
            pdf.set_text_color(27,41,17)
        else:
            pdf.set_text_color(125,0,0)

        pdf.cell(140) 
        unidad = str(x[22]) 
        pdf.multi_cell(180, 5, unidad, 0, "L", False)
        pdf.cell(140)  
        unidad = str(x[27]) + " " +str(x[3]) + "-"+str(x[5])+" - "+str(x[6])
        pdf.multi_cell(180, 5, unidad, 0, "L", False)
        pdf.ln(2)
        pdf.cell(140) 
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial Narrow', '', 10)
        unidad = str(x[23])
        pdf.multi_cell(180, 5, unidad, 0, "J", False)
        pdf.cell(140) 
        pdf.set_text_color(125,0,0)
        unidad = str(x[20]) +" - "+ str(x[21])
        pdf.set_font('Arial Narrow', 'B', 8)
        pdf.multi_cell(180, 5, unidad, 0, "J", False)
        pdf.ln()



        numero = numero +1

        posicion_final = pdf.get_y()
                # print(num1)
                # num1 = num1-num2
        pdf.set_line_width(1)
        pdf.set_draw_color(140, 140, 140)
        pdf.line(140, posicion_final-3, 335, posicion_final-3)



    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
 

    direcion =  LINK+"Eventos Relevantes.pdf"
    pdf.output(direcion, 'F')

 
    DIRECION = os.getenv('DIRECION_3')
    titulo = "Eventos Relevantes"


    direcion= DIRECION+str("Eventos Relevantes.pdf")
 
    return [direcion, titulo]
 


def informe_pendiente_id(datos):

    #datos

    fecha_evento =datos["fecha_evento"]
    fecha_evento_final =datos["fecha_evento_final"]
    id =datos["id"]

    fechas=""
    if fecha_evento and fecha_evento_final:
        filtro_fecha = "where fecha_evento >= '{}'  AND fecha_evento <= '{}'".format(fecha_evento, fecha_evento_final,)
        fechas=""
    else:
        filtro_fecha = ""
        fechas="1"
    if id !="null" and id:

        if fechas =="":
            filtro = "and id = '{}'".format(id)
            filtro_1 = "where id_evento = '{}'".format(id)
        elif fechas=="1":
            filtro = "where id = '{}'".format(id)
            filtro_1 = "where id_evento = '{}'".format(id)
    else:
        filtro =""

    conn = connect()
    cursor = conn.cursor()
    # query para traes el evento
    query="select * from registro_eventos_relevantes  {} {}   order by fecha_evento asc, hora_evento asc".format(filtro_fecha, filtro)
    cursor.execute(query)
    data = cursor.fetchall()

    # query para traer las afectaciones
    query_1="select * from registro_afectacion  {} ".format(filtro_1)
    cursor.execute(query_1)
    data_1 = cursor.fetchall()
    
    GRD = ["GR","MG","BG","CR","TC","MY","CT","TE","ST","SMC","SM","SP","SV", "SS", "CP","CS","C3", "DGSLP","SLP","SL18","SL12","---",]
    data_1 = sorted(data_1, key = lambda m: GRD.index(m[2]))

    # query para traer las bitacora
    query_2="select * from bitacora  {}    order by fecha_evento asc, hora_evento asc".format(filtro_1)
    cursor.execute(query_2)
    data_2 = cursor.fetchall()
    
    conn.commit()
    conn.close()
    cursor.close

    numero = 0
    datos_f=[]
    datos_final=[]
    for x in data:
        numero =numero+1
        datos_f = list(x)
        dato_a = str(numero)+" - "+str(x[6])
        datos_f.append(dato_a)
        datos_final.append(datos_f)
    
    positivos = list(filter(lambda data: "POSITIVO" in data[25], data))
    negativos = list(filter(lambda data: "NEGATIVO" in data[25], data))

    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/"

    
    datos=[negativos, positivos]
    DIRECION = os.getenv('DIRECION')   
    ruta = DIRECION

    
    
    

    for x  in data:
        unidad = x[3]
        if unidad=="DIV01" or unidad=="DIV02" or unidad=="DIV03" or unidad=="DIV04" or unidad=="DIV05" or unidad=="DIV06" or unidad=="DIV07" or unidad=="DIV08" or unidad=="FUTCO":
            
            unidad ="{}.JPG".format(unidad)
            unidad_png  = x[3]
            EVENTOS_id_2(datos, ruta, datos_final, unidad_png)
            mapa = '{}static/img/img_mapas/{}.png'.format(ruta,unidad_png)

        else:
            EVENTOS(datos, ruta, datos_final)
            mapa = '{}static/img/img_mapas/EVENTOS.png'.format(ruta)
            unidad ="EJC.JPG"
            unidad_png = "EVENTOS.png"

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

    fechas_inicial = fecha(fecha_evento)
    for x in data:
        fechas_final = fecha(x[1])

    fecha_titulo =  fechas_final[0] + " DE "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/divisiones_2025/", imagen = unidad, QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/QR.png", titulo= "EVENTO RELEVANTE", fecha_titulo= fecha_titulo,mapa=mapa, tipo="mapa_evento", unidad_png = unidad_png)


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)

    pdf.add_page()
    pdf.set_auto_page_break(True, 10)


    pdf.set_font('BebasNeue', '', 12)
    numero=1
    pdf.ln(15)
    for x in data:

        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial Narrow', 'B', 14)
        pdf.cell(130)   
        pdf.multi_cell(10, 5, str(numero), 0, "C", False)
        num = pdf.get_x()
        pdf.ln(-num+5)
        if x[25] == "POSITIVO":
            pdf.set_text_color(27,41,17)
        else:
            pdf.set_text_color(125,0,0)

        pdf.cell(140) 
        unidad = str(x[22]) 
        pdf.multi_cell(180, 5, unidad, 0, "L", False)
        pdf.cell(140)  
        unidad = str(x[27]) + " " +str(x[3]) + "-"+str(x[5])+" - "+str(x[6])
        pdf.multi_cell(180, 5, unidad, 0, "L", False)
        pdf.ln(2)
        pdf.cell(140) 
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial Narrow', '', 10)
        unidad = str(x[23])
        pdf.multi_cell(180, 5, unidad, 0, "J", False)
        pdf.cell(140) 
        pdf.set_text_color(125,0,0)
        unidad = str(x[20]) +" - "+ str(x[21])
        pdf.set_font('Arial Narrow', 'B', 8)
        pdf.multi_cell(180, 5, unidad, 0, "J", False)
        pdf.ln()



        numero = numero +1

        posicion_final = pdf.get_y()
                # print(num1)
                # num1 = num1-num2
        pdf.set_line_width(1)
        pdf.set_draw_color(140, 140, 140)
        pdf.line(140, posicion_final-3, 335, posicion_final-3)


    if data_1:

        pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/oficio/", imagen = "Diapositiva18.JPG", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/QR.png", titulo= "AFECTACIONES", fecha_titulo= fecha_titulo,tipo="reporte")

        pdf.add_page()
        pdf.set_auto_page_break(True, 10)

        
        pdf.set_fill_color(210, 214, 209)
        pdf.set_line_width(0.5)
        #pdf.rounded_rect(5, 45, 164, 150, 1,'D', '1234')
        #pdf.rounded_rect(172, 45, 164, 150, 1,'D', '1234')

            
        pdf.set_font('Arial Black', '', 16)
        pdf.set_text_color(80,80,80)

        pdf.ln(8)
        pdf.cell(-3)
        pdf.cell(10,5,"No.",1,0, 'L',True)
        pdf.cell(16,5,"GRD",1,0, 'L',True)
        pdf.cell(133,5,"APELLIDOS Y NOMBRES",1,0, 'L',True)

        numero=1
        pdf.ln(7)
        pdf.set_draw_color(140, 140, 140)
        num_i = pdf.get_x()
        AFECTACION= "ASESINADO"
        for x in data_1:

            if x[4] == "ASESINADO" or x[4] == "SECUESTRADO" or  x[4] == "FALLECIDO":
                AFECTACION = x[4]
                pdf.set_text_color(0,0,0)
                pdf.set_font('Arial Narrow', 'B', 12)
                pdf.cell(-3)   
                pdf.multi_cell(10, 5, str(numero), 0, "C", False)
                num = pdf.get_x()
                pdf.ln(-num+5)
                unidad = str(x[2]) 
                pdf.cell(7)  
                pdf.multi_cell(16, 5, unidad, 0, "c", False)
                num = pdf.get_x()
                pdf.ln(-num+5)
                unidad = str(x[3]) 
                pdf.cell(23)  
                pdf.multi_cell(133, 5, unidad, 0, "L", False)
                numero = numero +1 
                pdf.ln()
                
                posicion_final = pdf.get_y()
                pdf.line(10, posicion_final-3, 165, posicion_final-3)
                
        
        
        pdf.set_font('Arial Black', '', 16)
        pdf.set_text_color(80,80,80)
        pdf.text(55, 37, AFECTACION)


        pdf.set_font('Arial Black', '', 16)
        pdf.set_text_color(80,80,80)
        pdf.text(220, 37, "HERIDOS")

        num_f = num_i -posicion_final

        pdf.ln(num_f)
        pdf.ln(30)
        pdf.cell(163)
        pdf.cell(10,5,"No.",1,0, 'L',True)
        pdf.cell(16,5,"GRD",1,0, 'L',True)
        pdf.cell(133,5,"APELLIDOS Y NOMBRES",1,0, 'L',True)
        
        pdf.ln(7)
        numero=1
        for x in data_1:
            if x[4] == "HERIDO" :

                pdf.set_text_color(0,0,0)
                pdf.set_font('Arial Narrow', 'B', 12)
                pdf.cell(163)   
                pdf.multi_cell(10, 5, str(numero), 0, "C", False)
                num = pdf.get_x()
                pdf.ln(-num+5)
                unidad = str(x[2]) 
                pdf.cell(173)  
                pdf.multi_cell(16, 5, unidad, 0, "C", False)
                num = pdf.get_x()
                pdf.ln(-num+5)
                unidad = str(x[3]) 
                pdf.cell(189)  
                pdf.multi_cell(133, 5, unidad, 0, "L", False)
                numero = numero +1 
                pdf.ln()
                
                posicion_final = pdf.get_y()
                pdf.line(176, posicion_final-3, 331, posicion_final-3)

    if data_2:
            
        pdf.parametros(pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/oficio/", imagen = "Diapositiva18.JPG", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_eventos_relevantes/a_a_guardar_evento/informe_pendiente_qr/QR.png", titulo= "BITACORA", fecha_titulo= fecha_titulo,tipo="reporte")

        pdf.add_page()
        pdf.set_auto_page_break(True, 10)

        pdf.ln(10)
        pdf.set_font('Arial Black', '', 16)
        pdf.set_text_color(80,80,80)
        pdf.cell(5)
        pdf.cell(15,5,"No.",0,0, 'C',False)
        pdf.cell(50,5,"FECHA",0,0, 'C',False)
        pdf.cell(40,5,"HORA",0,0, 'C',False)
        pdf.cell(210,5,"EVENTO",0,0, 'J',False)
    

        pdf.ln(7)
        numero=1
        for x in data_2:

            pdf.set_text_color(0,0,0)
            pdf.set_font('Arial Narrow', '', 12)
            pdf.cell(5)   
            pdf.multi_cell(15, 5, str(numero), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            unidad = str(x[2]) 
            pdf.cell(20)  
            pdf.multi_cell(50, 5, unidad, 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            unidad = str(x[3]) 
            pdf.cell(70)  
            pdf.multi_cell(40, 5, unidad, 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            unidad = str(x[4]) 
            pdf.cell(110)  
            pdf.multi_cell(210, 5, unidad, 0, "J", False)


            numero = numero +1 
            pdf.ln()

            posicion_final = pdf.get_y()
            pdf.line(10, posicion_final-3, 331, posicion_final-3)



    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
 
    direcion =  LINK+"Eventos Relevantes.pdf"
    pdf.output(direcion, 'F')

 
    DIRECION = os.getenv('DIRECION_3')
    titulo = "Eventos Relevantes"


    direcion= DIRECION+str("Eventos Relevantes.pdf")
 
    return [direcion, titulo]
 

