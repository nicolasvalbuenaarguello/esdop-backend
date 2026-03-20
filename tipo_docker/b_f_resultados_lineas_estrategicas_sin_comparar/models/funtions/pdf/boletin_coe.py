from flask import make_response
from datetime import date, time, datetime
from tipo_docker.b_f_resultados_lineas_estrategicas_sin_comparar.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
  
#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):

    unidades = {
        "DIV01": "Primera División", "DIV02": "Segunda División", "DIV03": "Tercera División",
        "DIV04": "Cuarta División", "DIV05": "Quinta División", "DIV06": "Sexta División",
        "DIV07": "Séptima División", "DIV08": "Octava División", "FUTCO": "Fuerza de Tarea Omega", "FUTOM": "Fuerza de Tarea Omega","DAVAA": "División de Aviación de Asalto Aérea","DIVFE": "División de Fuerzas Especiales"
    }
    unidad_codigo = filtro[0]
    unidad = unidades.get(unidad_codigo, "Ejército Nacional").upper()
    pdf = PDF(orientation = 'L', unit = 'mm', format='letter')

    caligrafia_ingreso( pdf, filtro[15])
        

    imagen ="static/img/carta/Diapositiva3.JPG"
    pdf.parametros(tamanio = "carta", logo = filtro[11], permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr")
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()


    pdf.set_text_color(56,87,35)
    pdf.set_font('Arial Black', '', 22)
    pdf.text(20,81, "EVALUACIÓN")
    pdf.text(20,91, "OBJETIVO")
    pdf.text(20,101, "ESTRATÉGICO #2")
    pdf.text(20,111, "“DEBILITAR LAS")
    pdf.text(20,121, "CAPACIDADES DE LA")
    pdf.text(20,131, "AMENAZA”")


    if filtro[0] == "DAVAA" :
        pdf.text(20,146, str("División de Aviación").upper())
        pdf.text(20,156, str("de Asalto Aéreo").upper())
    elif filtro[0] == "DIVFE":
        pdf.text(20,146, str("División de").upper())
        pdf.text(20,156, str("Fuerzas Especiales").upper())
    else:
        pdf.text(20,146, str(unidad))

    pdf.set_text_color(56,87,35)
    # Go to 1.5 cm from bottom
    pdf.set_y(-15)
    # Select Arial italic 8
    pdf.set_font('Arial Black', '', 16)
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
  
    if filtro[0] == "DAVAA" or filtro[0] == "DIVFE":
        pdf.text(20, 170, str(fecha_actual))
    else:
        pdf.text(20, 160, str(fecha_actual))
    #pdf.text(90, 212, 'Fuente: SICOE')
    
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

    #titulo="SEGUIMIENTO OBJ #2 {}".format(unidad)
    fecha_titulo_sub = 'Debilitar las capacidades de la amenaza'

    titulo_unidad  =  titulos_name_lineas_estrategicas(filtro, fechas_final[2])
    
    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]
        
    imagen ="static/img/carta/Diapositiva18.JPG"


    pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo_sub, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr", fecha_titulo_2 = fechas)
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()

    titulo_sub(pdf, municipios, filtro)

    nombre_doc = "Evaluación Objetivo Estratégico 2".format(unidad)

    resultados_spoa =  Calculo_Spoa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_final_final[2], fecha_titulo, fecha_titulo_dos)
    resultados_spoa.comparativo_mapa()

            
    imagen ="static/img/carta/Diapositiva18.JPG"
    pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo_sub, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI - SIN FECHA" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr", fecha_titulo_2 = fechas)
    
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    resultados_spoa.comparativo_mapa_2()



    titulo_unidad  =  titulos_name_lineas_estrategicas_evaluacion(filtro, fechas_final[2])
    
    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]

    #titulo="CONSOLIDADO EVALUACIÓN OBJETIVO #2 {}".format(unidad)
    fecha_titulo_sub = 'DEBILITAR LAS CAPACIDADES DE LA AMENAZA'

    imagen ="static/img/carta/Diapositiva18.JPG"
    pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo_sub, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI - SIN FECHA" , ruta = filtro[15], imagen = imagen, seguridad = "sin_qr", fecha_titulo_2 = fechas)
    
    titulo_sub(pdf, municipios, filtro)
    # pdf.set_margin(10,10,10,True)
    #pdf.set_auto_page_break(True, 6)
    #pdf.add_page()
    #resultados_spoa.evaluacion()


    unidades = {
        "DIV01": "DIV01", "DIV02": "DIV02", "DIV03": "DIV03",
        "DIV04": "DIV04", "DIV05": "DIV05", "DIV06": "DIV06",
        "DIV07": "DIV07", "DIV08": "DIV08", "FUTCO": "FUTCO", "FUTOM": "FUTOM", "DAVAA": "DAVAA", "DIVFE": "DIVFE"
    }

    unidad_codigo = filtro[0]
    unidad = unidades.get(unidad_codigo, "Ejército Nacional")

    nombre_doc = "{} - Evaluación Objetivo Estratégico No 2".format(unidad)
    direcion = dirercion_archvios+str(nombre_doc)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(nombre_doc)+'.pdf'
    return [direcion, nombre_doc]

