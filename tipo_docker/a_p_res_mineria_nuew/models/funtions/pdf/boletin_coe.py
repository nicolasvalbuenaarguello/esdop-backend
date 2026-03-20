from flask import make_response
from datetime import date, time, datetime
from tipo_docker.a_p_res_mineria_nuew.models.estadistica.estadistica_boletin_coe import *
    
from __init__ import *

from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  

    #Funcion para la creacion del reporte de narcotrafico
def pdf_boletin_mineria(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):
            
    titulo_unidad  =  titulos_name(filtro)

    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]

    # print(titulo)

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()
    
    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/h_c_boletin_estadistica_mineria/models/img_qr"
   
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
    # pdf.header()
    # pdf.image("src/static/img/Imagen1.jpg", 50, 50)
    
    # fechas en el titulo
    resultados_spoa = Calculo_Spoa()
    resultados_spoa.resultados_mineria_boletin(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]





    #Funcion para la creacion del reporte de narcotrafico


    #Funcion para la creacion del reporte de narcotrafico
def pdf_boletin_mineria_mapa(fechas, filtro, dirercion_archvios, nombre_carpeta):
            
    # print(titulo)
    #manejo de las fechas
    fecha_inicial, fecha_final, fecha_inicial_anterior, fecha_final_anterior = fechas
    fechas_inicial = fecha(fecha_inicial)
    fechas_final = fecha(fecha_final)
    anio = fechas_final[2]
    titulo = f"RESULTADOS OPERACIONALES {anio}"

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])

    
    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()
    
    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/a_p_res_mineria_nuew/models/img_qr"
   
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/consejo.JPEG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    
        
    #lamina del mapa
    # fechas en el titulo
    nombre_doc="reporte_mineria"
    fechas_final = fecha(fechas[3])
    fechas_actual = fecha(fechas[1])
  
    resultados_spoa = Calculo_Spoa(fechas, fechas_final[2],  fechas_final[4], fechas_actual[2], pdf=pdf, permisos=filtro)
    resultados = resultados_spoa.resultados_mapamineria()

    #lamina del cuadro
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/consejo.JPEG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    resultados = resultados_spoa.resultados_cuadro_mineria()

    direcion = dirercion_archvios+str(nombre_doc)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(nombre_doc)+'.pdf'
    return [direcion, nombre_doc]





    #Funcion para la creacion del reporte de narcotrafico




def pdf_mapa(filtro, permisos):
            
    fechas_final = fecha(filtro[3])
   
    resultados_spoa = Calculo_Spoa(filtro, fechas_final[2], permisos= permisos)
    resultados = resultados_spoa.dinamico()


    return resultados
