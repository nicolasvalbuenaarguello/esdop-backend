from flask import make_response
from datetime import date, time, datetime
from tipo_docker.a_c_boletin_estadistica_resultados.models.estadistica.estadistica_boletin_coe import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
from __init__ import *
#Funcion para la creacion del reporte de resultados 


#Funcion para la creacion del reporte de resultados 
def pdf_boletin_resultados(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):
            

    municipios= ""
    titulo =  titulos_name(filtro)
    # print(titulo)
    if  filtro[4] == "lugar":
        if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
            titulo = "RESULTADO RESALTANTES"
            municipios = str(filtro[6])
        else:
            titulo = "RESULTADO RESALTANTES ({})".format(titulo)
    else:
        if titulo != "":
            titulo = "RESULTADO RESALTANTES ({})".format(titulo)
        else:
            titulo = "RESULTADO RESALTANTES DEL EJÉRCITO NACIONAL"
    municipios = municipios.replace(",", ", ")

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14],"SI")


    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/a_c_boletin_estadistica_resultados/models/qr_img"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
        
    if municipios !="":
        pdf.set_text_color(70,70,70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(63,30,str(municipios))
    # pdf.header()
    # pdf.image("src/static/img/Imagen1.jpg", 50, 50)
    
    # fechas en el titulo
    calcular_spo = Calculo_Spoa()

    calcular_spo.resultados_resultados_boletin(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    direcion = dirercion_archvios+"/"+str(titulo)+'.pdf'
    
    pdf.output(direcion, 'F')
    LINK = os.getenv('DIRECION_3')
    direcion= LINK+nombre_carpeta+str(titulo)+'.pdf'
    # print(direcion)
    return [direcion, titulo]
