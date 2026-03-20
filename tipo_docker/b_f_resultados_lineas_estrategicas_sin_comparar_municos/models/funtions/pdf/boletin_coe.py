from flask import make_response
from datetime import date, time, datetime

from tipo_docker.b_f_resultados_lineas_estrategicas_sin_comparar_municos.models.estadistica.estadistica_boletin_coe import *

from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
#Funcion para la creacion del reporte de resultados 
from __init__ import *

#RESULTDOS COMPARATIVOS
def resultados_resaltantes(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):



    pdf = PDF(orientation = 'L', unit = 'mm', format='letter')

    caligrafia_ingreso( pdf, filtro[15])


    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    if fechas_final[2] == fechas_inicial[2]:
        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    else:
        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] +" " +  fechas_inicial[2] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]

    if fecha_inicial_u_l == fecha_final_u_l:
       
       fecha_titulo = fechas_final[0] + " DE "+fechas_final[1] + " DEL "+fechas_final[2]


    fecha_titulo = fecha_titulo.upper()
        #titulo="SEGUIMIENTO OBJ #2 {}".format(unidad)
    fecha_titulo_sub = 'Debilitar las capacidades de la amenaza'

    titulo_unidad  =  titulos_name_lineas_estrategicas_resaltantes(filtro, fechas_final[2])
    
    if len(titulo_unidad[1]) > 0:
        municipios = ", ".join(titulo_unidad[1])
    else:
        municipios = ""

    titulo= titulo_unidad[0]

    
    img_qr = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/s_c_resultados_resaltantes/models/img_qr"
    pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/carta/Diapositiva18.JPG", seguridad = "nueva" , img_qr = img_qr,  fecha_titulo_2 = "")

    pdf.set_auto_page_break(True, 4)
    pdf.add_page()
    
    # fecha_inicial_mes = mes(fecha_inicial_mes)
        
    if municipios != "":
        pdf.set_text_color(70, 70, 70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(165, 30, str(municipios))

    if filtro[24]:
        pdf.set_text_color(70, 70, 70)
        pdf.set_font('BebasNeue', '', 14)
        pdf.text(165, 30, str(filtro[24]))



    dato  = ""
    resultados_spoa = Calculo_Spoa(filtro)
    resultados_spoa.resultados_resaltantes_pdf(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf, dato)

    direcion = dirercion_archvios+str("resultados_resaltantes")+'.pdf'
    pdf.output(direcion, 'F')
    
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str("resultados_resaltantes")+'.pdf'
    return [direcion, "resultados_resaltantes"]

