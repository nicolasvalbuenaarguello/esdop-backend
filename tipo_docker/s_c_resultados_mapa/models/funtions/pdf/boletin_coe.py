from flask import make_response
from datetime import date, time, datetime
from tipo_docker.s_c_resultados_mapa.models.estadistica.estadistica_boletin_coe import *
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


    pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva20.JPG", seguridad = "nueva", )
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()

    pdf.set_text_color(50,50,50)
    pdf.set_font('Arial Narrow', 'B', 12)

    if fecha_inicial_anio_inicial == fecha_inicial_anio:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    else:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " " +str(fecha_inicial_anio_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    
    fechas = fechas.upper()

            
    t = "Fuerzas Militares de Colombia"
    t_1 ="Ejército Nacional"
    t_2 = "Usuario"
    t_3 = "Unidad"

    img_qr = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/s_c_resultados_mapa/models/img_qr"

    inf= "Resultados del Dia:"
    fecha_Elaboracion = datetime.now()
    inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + fechas +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +filtro[14]+" \n" + t_3+" \n" +filtro[12]
    img = qrcode.make(inf_qur)
    f = open(img_qr+"/QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(img_qr+"/QR.png",33,171,23,23)



    titulos = "CONSOLIDADO RESULTADOS CONTRA"


    titulo_e  =  titulos_name(filtro)
 
    titulo = titulo_e[0]
    municipios = titulo_e[1]
    #print(municipios)
 
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

            
        else:
            pdf.set_font('BebasNeue', '', 30)
 
            nombre_doc = titulo
    else:

        nombre_doc = titulo
    
    titulos = titulos + " " + titulo  
    y = pdf.get_y()               # Select Arial bold 15
    pdf.set_font('Arial Black', '', 16)
    pdf.set_text_color(56,87,35)
    pdf.ln(-22)
    pdf.cell(120)
    pdf.multi_cell(200, 5, titulos, 0, "L", False)
    # fecha = strftime(pdf.fecha, '%y')
           

    #pdf.text(52, 26, pdf.fecha_titulo)
    pdf.ln(0.1)
    pdf.cell(120)
    pdf.multi_cell(180, 5, fechas, 0, "L", False)
    x = pdf.get_y()
    z=y-x
    pdf.ln(1+z-1)


    # fechas en el titulo
    
    resultados_spoa =  Calculo_Spoa()
    resultados_spoa.comparativo_mapa(pdf, fecha_inicial_u_l, fecha_final_u_l,  filtro)
    
    direcion = dirercion_archvios+str(nombre_doc)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(nombre_doc)+'.pdf'
    return [direcion, nombre_doc]

