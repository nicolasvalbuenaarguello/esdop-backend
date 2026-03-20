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

#Funcion de resultados nueva ayuda
#pip install seaborn
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn


def informe_pendiente(datos):

    #datos

    permiso =datos["unidad"]
    unidad =datos["unidad"]
    fullname =datos["fullname"]

    reporte =datos["reporte"]
    reporte_2 =datos["reporte_2"]
    numero_variable =int(datos["numero_variable"])
    numero_variable_2 =int(datos["numero_variable_2"])

    orden =datos["orden"]
    

    if permiso == "EJC":
        query="select * from asignacion_plazos  {}   ORDER BY  {} ASC".format(reporte,orden)
    else:
        query="select * from asignacion_plazos where cargo LIKE '%{}%' {}  ORDER BY  {} ASC".format(permiso, reporte_2, orden)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close

 
    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/"
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
    
          
    pdf.parametros( tipo = "REPORTE",   permiso =unidad,  usuario = fullname, pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/", imagen = "ejc.png", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/QR.png")


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)


    pdf.add_page()
    #pdf.set_auto_page_break(True, 6)

    pdf.set_font('BebasNeue', '', 12)
    numero=1

    nuevo_listados=[]
    paso=[]
    for data_x in data:
        if data_x[numero_variable] != "SI":
            ahora = datetime.now()
            fin_anio_2021 = datetime.strptime(data_x[numero_variable], "%Y-%m-%d")
            diferencia = fin_anio_2021-ahora
            paso = list(data_x)
            if diferencia.days < 0:
                dia = int(diferencia.days)*-1
                paso.append(f"{dia} Dias Vencidos")
            else:
                dia = int(diferencia.days)*1
                paso.append(f"{dia} Dias Para Vencer")
            nuevo_listados.append(paso)
    
    for data_x in nuevo_listados:

        if data_x[numero_variable_2] != "SI":
            pdf.set_text_color(0,0,0)
            pdf.set_font('Calibri', '', 11)
            
            pdf.multi_cell(10, 5, str(numero), 0, "L", False)
            num = pdf.get_x()
                
            pdf.ln(-num+5)
            pdf.cell(10)

            pdf.multi_cell(50, 5, str(data_x[3]), 0, "J", False)

            pdf.ln(-num+5)
            pdf.cell(60)

            pdf.multi_cell(80, 5, str(data_x[2]), 0, "J", False)

            pdf.ln(-num+5)
            pdf.cell(140)

            pdf.multi_cell(40, 5, str(data_x[1]), 0, "J", False)
        
            pdf.ln(-num+5)
            pdf.cell(180)
            pdf.multi_cell(40, 5, str(data_x[36]), 0, "J", False)
                
    
            pdf.ln(-num+5)
            pdf.cell(220)
            dato = data_x[54]

            if "Vencidos" in str(dato):
                pdf.set_fill_color(128, 0, 0)
                pdf.set_text_color(255,255,255)
                pdf.set_font('Calibri', 'B', 10)
                pdf.multi_cell(35, 5, str(data_x[54]), 0, "J", True)
            elif  "0 Dias Para Vencer" == str(dato):
                pdf.set_fill_color(242, 187, 29)
                pdf.set_text_color(255,255,255)
                pdf.set_font('Calibri', 'B', 10)
                pdf.multi_cell(35, 5, str(data_x[54]), 0, "J", True)
            else:
                pdf.set_text_color(0,0,0)
                pdf.set_font('Calibri', 'B', 10)
                pdf.multi_cell(35, 5, str(data_x[54]), 0, "J", False)
            
                #pdf.ln(-5)

            pdf.set_text_color(0,0,0)
            pdf.set_font('Calibri', '', 10)
            pdf.ln(-num+5)
            pdf.cell(255)
            pdf.multi_cell(85, 5, str(data_x[53]), 0, "J", False)
            numero = numero +1

            posicion_final = pdf.get_y()
                # print(num1)
                # num1 = num1-num2
            pdf.set_line_width(0.1)
            pdf.set_draw_color(140, 140, 140)
            pdf.line(10, posicion_final, 350, posicion_final)
       
         
        #pdf.cell(10,5,str(numero),1,0, 'L',False)
        #pdf.cell(40,5,str(x[3]),1,0, 'L',False)
        #pdf.cell(60,5,str(x[4]),1,0, 'L',False)
        #pdf.cell(60,5,str(x[1]),1,0, 'L',False)
        #pdf.cell(40,5,str(x[38]),1,0, 'L',False)
        #pdf.cell(60,5,"---",1,0, 'L',False)
        #pdf.ln()
        
    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
    titulo = "informe respuesta"

    direcion =  LINK+"informe respuesta.pdf"
    pdf.output(direcion, 'F')
    pdf.output("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/informe respuesta.pdf", 'F')

    direcion= DIRECION+str("informe respuesta.pdf")
 
    return [direcion, titulo]
 
def informe_pendiente_estadistica(datos):

    #datos

    permiso =datos["unidad"]
    unidad =datos["unidad"]
    fullname =datos["fullname"]

    reporte =datos["reporte"]
    reporte_2 =datos["reporte_2"]
    numero_variable =int(datos["numero_variable"])

    orden =datos["orden"]

    if permiso == "EJC":
        query="select * from asignacion_plazos  {}  ORDER BY  cargo ASC".format(reporte)
    else:
        query="select * from asignacion_plazos where cargo LIKE '%{}%' {} ORDER BY  cargo ASC".format(permiso, reporte_2)

        
    if permiso == "EJC":
        query_2="select * from asignacion_plazos  {}  ORDER BY  {} ASC".format(reporte, orden)
    else:
        query_2="select * from asignacion_plazos where cargo LIKE '%{}%' {}  ORDER BY  {} ASC".format(permiso, reporte_2, orden)

    conn = connect()
    cursor = conn.cursor()

    cursor.execute(query)
    data = cursor.fetchall()

    cursor.execute(query_2)
    data_2 = cursor.fetchall()

    conn.commit()
    conn.close()
    cursor.close

 
    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/"
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
    
          
    pdf.parametros( tipo = "ESTADISTICA",   permiso =unidad,  usuario = fullname, pie_pagina = "SI" , ruta = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/", imagen = "ejc.png", QR="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/QR.png")


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)


    pdf.add_page()
    #pdf.set_auto_page_break(True, 6)

    nuevo_listados=[]
    paso=[]
    for data_x in data_2:
        if data_x[40] != "SI":
            ahora = datetime.now()
            fin_anio_2021 = datetime.strptime(data_x[numero_variable], "%Y-%m-%d")
            diferencia = fin_anio_2021-ahora
            paso = list(data_x)
            if diferencia.days < 0:
                dia = int(diferencia.days)*-1
                paso.append(f"{dia} Dias Vencidos")
            else:
                dia = int(diferencia.days)*1
                paso.append(f"{dia} Dias Para vencer")
            nuevo_listados.append(paso)

    
    dias_vencidos=[]
    for data_x in nuevo_listados:

        if data_x[40] != "SI":
            if data_x[54] not in dias_vencidos:
                dias_vencidos.append(data_x[54])

    Cantidad_dias_vencidos=[]         
    for x in dias_vencidos:
        numero = 0 
        for data_x in nuevo_listados:
            if data_x[40] != "SI":
                if data_x[54] == x:
                    numero = numero +1
        Cantidad_dias_vencidos.append(numero)
 


    unidades=[]
    for data_x in data:

        if data_x[40] != "SI":
            if data_x[3] not in unidades:
                unidades.append(data_x[3])



    cantidad=[]           
    for x in unidades:
        numero = 0 
        for data_x in data:
            if data_x[40] != "SI":
                if data_x[3] == x:
                    numero = numero +1
        cantidad.append(numero)

                
    dias=[]
    for data_x in data_2:

        if data_x[40] != "SI":
            if data_x[36] not in dias:
                dias.append(data_x[36])
             
    cantidad_dias=[]           
    for x in dias:
        numero = 0 
        for data_x in data_2:
            if data_x[40] != "SI":
                if data_x[36] == x:
                    numero = numero +1
        cantidad_dias.append(numero)



    #fig, ax = plt.subplots(figsize=(8,6))


    #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
    ax = sns.barplot(x = unidades, y = cantidad, color="darkred")
    ax.bar_label(ax.containers[0], fontsize=10, color="b")
    sns.despine()
    sns.color_palette("rocket")
    locs, labels = plt.xticks()
    plt.rcParams["figure.figsize"] = (250, 150)
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'darkred','size':15}

    plt.title("PLAZOS POR DEPENDENCIAS", fontdict = font1)
    plt.xlabel("Dependencia", fontdict = font2)
    plt.ylabel("Cantidad", fontdict = font2)

    plt.setp(labels, rotation=90)
    plt.tight_layout()
    
    plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/Ejemplo1.jpg", transparent=True)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/Ejemplo1.jpg",5,35,150,110)
    ax.get_figure().clf()


    #grafico de la cantidad de la cantidad de dias         


    #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
    ax_2 = sns.barplot(x = cantidad_dias, y = dias , color="darkred", orient="h")
    ax_2.bar_label(ax_2.containers[0], fontsize=10, color="b")
    sns.despine()
    sns.color_palette("rocket")
    locs, labels = plt.xticks()
    plt.rcParams["figure.figsize"] = (250, 150)
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'darkred','size':15}

    plt.title("PLAZOS POR FECHAS VENCIDOS", fontdict = font1)
    plt.xlabel("Cantidad", fontdict = font2)
    plt.ylabel("Fecha", fontdict = font2)

    plt.setp(labels, rotation=90)
    plt.tight_layout()

    plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/dias.jpg", transparent=True)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/dias.jpg",190,10,130,115)
    ax_2.get_figure().clf()



    #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
    ax_3 = sns.barplot(x = dias_vencidos, y =  Cantidad_dias_vencidos , color="darkred")
    ax_3.bar_label(ax_3.containers[0], fontsize=10, color="b")
    sns.despine()
    sns.color_palette("rocket")
    locs, labels = plt.xticks()
    plt.rcParams["figure.figsize"] = (250, 150)
    font1 = {'family':'serif','color':'black','size':15}
    font2 = {'family':'serif','color':'darkred','size':15}

    plt.title("PLAZOS POR DIAS VENCIDOS", fontdict = font1)
    plt.xlabel("Cantidad", fontdict = font2)
    plt.ylabel("Dias", fontdict = font2)

    plt.setp(labels, rotation=90)
    plt.tight_layout()

    plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/dias_vencidos.jpg", transparent=True)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente_qr/dias_vencidos.jpg",190,125,150,90)
    ax_3.get_figure().clf()

    suma_de_notas = sum(cantidad)
    pdf.rounded_rect(55, 150, 70, 50, 1,'D', '1234')
    pdf.set_font('BebasNeue', '', 50)
    pdf.text(85,175,str(suma_de_notas))
    pdf.set_font('BebasNeue', '', 20)
    pdf.text(70,185,"CANTIDAD DE PLAZOS")


         
        #pdf.cell(10,5,str(numero),1,0, 'L',False)
        #pdf.cell(40,5,str(x[3]),1,0, 'L',False)
        #pdf.cell(60,5,str(x[4]),1,0, 'L',False)
        #pdf.cell(60,5,str(x[1]),1,0, 'L',False)
        #pdf.cell(40,5,str(x[38]),1,0, 'L',False)
        #pdf.cell(60,5,"---",1,0, 'L',False)
        #pdf.ln()
        
    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
    titulo = "estadistica"

    direcion =  LINK+"estadistica.pdf"
    pdf.output(direcion, 'F')
    pdf.output("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/estadistica.pdf", 'F')

    direcion= DIRECION+str("estadistica.pdf")
 
    return [direcion, titulo]
 
def balance(datos):

    from PyPDF2 import PdfFileMerger, PdfFileReader
    import PyPDF2
    listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/')
    merger = PdfFileMerger()

    donmbre_archivo = "balance de plazos que requieren respuesta.pdf"

    documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'+donmbre_archivo
    for file in listaPdfs:
        #print(file)
        merger.append(PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/'+file))
    #merger.write(documento_guardado)
    LINK = os.getenv('DIRECION_3_B')
    direcion =  LINK+donmbre_archivo
    merger.write(direcion)
    
    dirercion_archvios= "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/informe_pendiente/"
    documento_eliminar = ["estadistica.pdf", "informe respuesta.pdf"]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

    
    DIRECION = os.getenv('DIRECION_3')
    titulo = "balance de plazos que requieren respuesta"





    direcion= DIRECION+str("balance de plazos que requieren respuesta.pdf")
    
    return [direcion, titulo]
    