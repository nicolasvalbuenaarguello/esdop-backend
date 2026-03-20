from flask import make_response
from datetime import date, time, datetime

from tipo_docker.n_c_cuadro_compartivo_afectaciones.models.estadistica.estadistica_boletin_coe import *

from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
from __init__ import *
#Funcion para la creacion del reporte de resultados 

def cuadro_compartivo_afectaciones(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):
    
    #en el presente bloque de codigo se llama el listado de las afectaciones.
    #---------------------------------------------------------#
    #--------------listado de afectaciones--------------------#
    #---------------------------------------------------------#
    
    
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])

    titulo  =  titulos_name(filtro)

    municipios= ""
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


    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    
    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_c_boletin_estadistica/models/qr_img"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15],  imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

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
#--------
    if municipios !="":
        pdf.text(63,30,str(municipios)) 

            # print(titulo)
    if  filtro[4] == "lugar":
        if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
            municipios = str(filtro[6])
        else:
            titulo = titulo
    else:
        if titulo != "":
            titulo = titulo
        else:
            titulo = "RESULTADO RESALTANTES DEL EJÉRCITO NACIONAL"
            nombre_doc = titulo
    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    resultados_spoa  = Calculo_Spoa()
    resultados_spoa.cuadro_afectaciones_pdf_comparativo(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo, fecha_titulo_dos)

    titulo  = "cuadros comparativos afec propias tropas"

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]

