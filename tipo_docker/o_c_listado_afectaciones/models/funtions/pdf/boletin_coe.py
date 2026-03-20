from flask import make_response
from datetime import date, time, datetime
from __init__ import *
from tipo_docker.o_c_listado_afectaciones.models.estadistica.estadistica_boletin_coe import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
#Funcion para la creacion del reporte de resultados 

#Función en Python que genera el listado de las afectaciones de propias tropas 
def listado_afectaciones(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):


    # print(titulo)


    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])


    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    if fechas_final[2] == fechas_inicial[2]:
        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    else:
        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] +" " +  fechas_inicial[2] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]

    if fecha_inicial_u_l == fecha_final_u_l:
       
       fecha_titulo = fechas_final[0] + " DE "+fechas_final[1] + " DEL "+fechas_final[2]

    

    titulo_unidad  =  titulos_name_lineas_estrategicas_obj4(filtro, fechas_final[2])
        
    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]

    fecha_titulo_sub = 'Proteger y fortalecer la Fuerza y sus capaciades estratégicas'

    

    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_c_boletin_estadistica/models/qr_img"
    
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15],  imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
        
    
    if municipios !="":
        municipios =str(municipios)
        municipios = municipios.replace(",", ", ")
        municipios = municipios.replace("[", "")
        municipios = municipios.replace("]", "")
        titulo = municipios
        # print(len(titulo))
        if titulo.find(",") >= 0:
            if len(titulo) > 170:
                nombre_doc = "Resultados por divisiones"
                pdf.set_font('BebasNeue', '', 8)
            elif len(titulo) <= 170 and len(titulo) > 160:
                pdf.set_font('BebasNeue', '', 8)
                nombre_doc = titulo
            elif len(titulo) <= 160 and len(titulo) > 150:
                pdf.set_font('BebasNeue', '', 9)
                nombre_doc = titulo 
            elif len(titulo) <= 150 and len(titulo) > 140:
                pdf.set_font('BebasNeue', '', 10)
                nombre_doc = titulo 
            elif len(titulo) <= 140 and len(titulo) > 130:
                pdf.set_font('BebasNeue', '', 11)
                nombre_doc = titulo 
            elif len(titulo) <= 130 and len(titulo) > 120:
                pdf.set_font('BebasNeue', '', 12)
                nombre_doc = titulo 
            elif len(titulo) <= 120 and len(titulo) > 110:
                pdf.set_font('BebasNeue', '', 13)
                nombre_doc = titulo 
            elif len(titulo) <= 110 and len(titulo) > 100:
                pdf.set_font('BebasNeue', '', 14)
                nombre_doc = titulo
            else:
                pdf.set_font('BebasNeue', '', 16)
                nombre_doc = titulo
            #pdf.text(150,24,str(titulo)) 
            #pdf.ln(-18)
            pdf.cell(40)
            pdf.multi_cell(300, 3.5, str(titulo),0,0,False)
            #pdf.ln(15)
            
        else:
            pdf.set_font('BebasNeue', '', 30)
            #pdf.text(150,26,str(titulo)) 
            nombre_doc = titulo
    else:
        #pdf.text(150,26,str(titulo)) 
        nombre_doc = titulo
    

    if filtro[24]:
        pdf.set_text_color(70,70,70)
        pdf.set_font('BebasNeue', '', 14)
        
        pdf.text(55,28,str(filtro[24]))

    resultados_spoa= Calculo_Spoa()
    resultados_spoa.cuadro_afectaciones_pdf(pdf, fecha_inicial_u_l, fecha_final_u_l, filtro)
    pdf.add_page()

    resultados_spoa.listados_afectaciones_pdf(pdf, fecha_inicial_u_l, fecha_final_u_l, filtro)


    direcion = dirercion_archvios+str("listado_afectaciones")+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str("listado_afectaciones")+'.pdf'
    return [direcion, "listado_afectaciones"]
