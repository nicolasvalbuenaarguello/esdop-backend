from flask import make_response
from datetime import date, time, datetime
from tipo_docker.z_b_ayudas_un_solo_resultados.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
  
#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):


    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])

    
    fechas_inicial = fecha(fecha_inicial_u_l)
    
    fecha_inicial_dia_inicial = fechas_inicial[0]
    fecha_inicial_mes_inicial = fechas_inicial[1]
    fecha_inicial_anio_inicial = fechas_inicial[2]

    fechas = fecha(fecha_final_u_l)

    fecha_inicial_dia = fechas[0]
    fecha_inicial_mes = fechas[1]
    fecha_inicial_anio = fechas[2]
    fecha_inicial_mes_number = fechas[3]

        
    
    if filtro[0]=="" or filtro[0]=="---":
        imagen ="static/img/oficio/Diapositiva20.JPG"
 
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0] == "FUTCO" or filtro[0] == "FUTOM":

        if filtro[0] == "FUTCO":
            unidad = "FUTCO"
        elif filtro[0] == "FUTOM":
            unidad = "FUTCO"
        else:
            unidad = filtro[0]

        
        imagen ="static/img/divisiones_2025/{}.JPG".format(unidad)

    else:
        imagen ="static/img/oficio/Diapositiva20.JPG"

    pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen,  seguridad ="nueva")
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()

    pdf.set_text_color(125,0,0)
    pdf.set_font('Arial Narrow', 'B', 12)

    if fecha_inicial_anio_inicial == fecha_inicial_anio:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    else:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " " +str(fecha_inicial_anio_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    fechas = fechas.upper()
    pdf.text(155,5.5,fechas) 


    pdf.set_font('BebasNeue', '', 28)
    pdf.set_text_color(0,0,0)
    titulo = "RESULTADOS"
    pdf.text(150,17,titulo) 
    pdf.set_text_color(125,0,0)

    titulo_e  =  titulos_name(filtro)

    titulo = titulo_e[0]
    municipios = filtro[26]

 
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
                pdf.set_font('BebasNeue', '', 7)
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
            pdf.text(150,24,str(titulo)) 
            
        else:
            pdf.set_font('BebasNeue', '', 30)
            pdf.text(150,26,str(titulo)) 
            nombre_doc = titulo
    else:
        pdf.text(150,26,str(titulo)) 
        nombre_doc = titulo
    
    
    
    # fechas en el titulo
    ruta = filtro[15] 
    
    rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)
    if filtro[0]=="" or filtro[0]=="---":
        pdf.image(rosa_nautica,100, 40, 15, 15)
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0]=="FUTCO" or filtro[0]=="FUTOM": 
        pass
    else:
        pdf.image(rosa_nautica,100, 40, 15, 15)
    
    resultados_spoa =  Calculo_Spoa()
    resultados_spoa.comparativo_mapa(pdf, fecha_inicial_u_l, fecha_final_u_l,  filtro)
    
    direcion = dirercion_archvios+str(nombre_doc)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(nombre_doc)+'.pdf'
    return [direcion, nombre_doc]

