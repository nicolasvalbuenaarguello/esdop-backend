from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_c_boletin_estadistica.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
#funcion para estaditica
def estadistica_resaltantes(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    pdf.parametros(tamanio = "oficio",  pie_pagina = "NO", permiso =filtro[12], nivel = filtro[13], usuario = filtro[14],  ruta = filtro[15], imagen = "static/img/oficio/Diapositiva3.JPG")
   
    pdf.add_page()
    pdf.set_auto_page_break(True, 10)

    caligrafia_ingreso( pdf, filtro[15])

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO #2 DEBILITAR LAS CAPACIDADES DE LA AMENAZA POR DIVISIONES"


    pdf.set_font('Arial Black', '', 24)

    pdf.set_text_color(56,87,35)
    pdf.ln(40)
    pdf.cell(16)
    pdf.multi_cell(110, 9, titulo, 0, "L", False)

    pdf.text(25,145, fecha_titulo)

    pdf.set_font('Calibri', 'B', 14)
    pdf.set_text_color(200,0,0)

    dias = datetime.now().day
    meses = datetime.now().month
    anios = datetime.now().year

    meses = str(mes(meses))
    meses = meses.upper()
    fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)
    pdf.text(190,213, fecha_actual)
    pdf.text(240,213, 'JEMOP - DIROP ')
    pdf.text(300,213, 'SECRETO')


    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_c_boletin_estadistica/models/qr_img"
    titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO #2 DEBILITAR LAS CAPACIDADES DE LA AMENAZA POR DIVISIONES"
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    
    
    pdf.add_page()
    titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO #2 DEBILITAR LAS CAPACIDADES DE LA AMENAZA POR DIVISIONES"
     
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    pdf.ln(-7)
    calcular_spoa = Calculo_Spoa()
    calcular_spoa.calculo_boletin(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    direcion = dirercion_archvios +str("resultados cuadros")+'.pdf'

    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str("resultados cuadros")+'.pdf'
    return [direcion, "resultados cuadros"]
