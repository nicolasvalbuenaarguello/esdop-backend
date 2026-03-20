from flask import make_response
from datetime import date, time, datetime
from tipo_docker.b_f_resultados_lineas_estrategica_4.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
  
#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):

    pdf = PDF(orientation = 'L', unit = 'mm', format='letter')

    caligrafia_ingreso( pdf, filtro[15])

    

    imagen ="static/img/carta/Diapositiva3.JPG"
    pdf.parametros(tamanio = "carta", logo = filtro[11], permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr")
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()


    pdf.set_text_color(56,87,35)
    pdf.set_font('Calibri', 'B', 30)
    pdf.text(20,45, "EVALUACIÓN")
    pdf.text(20,57, "OBJETIVO")
    pdf.text(20,69, "ESTRATÉGICO")

    pdf.text(20,90, "PLAN DE CAMPAÑA")
    pdf.text(20,102, "DEL EJÉRCITO")
    pdf.text(20,114, "NACIONAL")
    pdf.set_text_color(0,0,0)
    pdf.text(20,126, "“AYACUCHO PLUS” 2025")

    pdf.set_font('Calibri', 'B', 25)
    pdf.set_text_color(56,87,35)
    pdf.text(20,150, "OBJ #4")
    pdf.set_text_color(0,0,0)
    pdf.text(20,162, "PROTEGER Y FORTALECER")
    pdf.text(20,170, "LA FUERZA Y SUS")
    pdf.text(20,178, "CAPACIDADES ESTRATÉGICAS")

    pdf.set_text_color(255,255,255)
    # Go to 1.5 cm from bottom
    pdf.set_y(-15)
    # Select Arial italic 8
    pdf.set_font('Arial', 'B', 10)
    # Print centered page number
    # self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

    dias = datetime.now().day
    meses = datetime.now().month
    anios = datetime.now().year
    # print(datetime.now().month)
    meses = mes(meses)
    meses =str(meses)
    meses = meses.upper()
    # print(meses)   
    fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)


    pdf.text(220, 212, "SECRETO          " + str(fecha_actual))
    pdf.text(90, 212, 'Fuente: SICOE')
    fechas_inicial = fecha(fecha_inicial_u_l)
    
    fecha_inicial_dia_inicial = fechas_inicial[0]
    fecha_inicial_mes_inicial = fechas_inicial[1]
    fecha_inicial_anio_inicial = fechas_inicial[2]

    fechas = fecha(fecha_final_u_l)

    fecha_inicial_dia = fechas[0]
    fecha_inicial_mes = fechas[1]
    fecha_inicial_anio = fechas[2]
    fecha_inicial_mes_number = fechas[3]

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)
    
    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()



    if fecha_inicial_anio_inicial == fecha_inicial_anio:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    else:
        fechas= str("DEL ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " " +str(fecha_inicial_anio_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    fechas = fechas.upper()

    unidad = ""
    if filtro[0] != "---" and filtro[0] != "":
        unidad = filtro[0]

    titulo_unidad  =  titulos_name_lineas_estrategicas_obj4(filtro, fechas_final[2])
        
    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]

    fecha_titulo_sub = 'Proteger y fortalecer la Fuerza y sus capacidades estratégicas'
        
    imagen ="static/img/carta/Diapositiva18.JPG"
    pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo_sub, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr", fecha_titulo_2 = fechas)
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()

    
    nombre_doc = "Seguimiento_obj_4 {}".format(unidad)

    resultados_spoa =  Calculo_Spoa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_final_final[2], fecha_titulo, fecha_titulo_dos)
    resultados_spoa.comparativo()


    imagen ="static/img/carta/Diapositiva19.JPG"
    pdf.parametros( tamanio = "carta", logo = filtro[11], permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr")
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()


    direcion = dirercion_archvios+str(nombre_doc)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(nombre_doc)+'.pdf'
    return [direcion, nombre_doc]

