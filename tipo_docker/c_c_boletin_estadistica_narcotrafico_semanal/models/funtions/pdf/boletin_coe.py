from flask import make_response
from datetime import date, time, datetime
from tipo_docker.c_c_boletin_estadistica_narcotrafico_semanal.models.estadistica.estadistica_boletin_coe import *

from __init__ import *

from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  

#Funcion en python para la creacion de resultado de nacrotrafico
def pdf_boletin_narcotrafico(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):
    
    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/docna (1).JPG")
        
    # fecha_inicial_dia = datetime.now().day
    # fecha_inicial_mes = datetime.now().month
    # fecha_inicial_anio = datetime.now().year
    # dia_semana = datetime.now().weekday()

    fecha_dt = datetime.strptime(fecha_final_u_l, '%Y-%m-%d')
    fechas_final = fecha_dt.weekday()

    fechas_inicial = fecha(fecha_inicial_u_l)
    
    fecha_inicial_dia_inicial = fechas_inicial[0]
    fecha_inicial_mes_inicial = fechas_inicial[1]
    fecha_inicial_anio_inicial = fechas_inicial[2]

    fechas = fecha(fecha_final_u_l)

    fecha_inicial_dia = fechas[0]
    fecha_inicial_mes = fechas[1]
    fecha_inicial_anio = fechas[2]
    fecha_inicial_mes_number = fechas[3]

    anio = str(fecha_inicial_anio)

    dia_semana = dias_semana(fechas_final)


    caligrafia_ingreso( pdf, filtro[15])

    pdf.add_page()

    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 30)

    # fecha_inicial_mes = mes(fecha_inicial_mes)
    titulo = "DIRECCIÓN DE OPERACIONES CONTRA EL NARCOTRÁFICO"
    pdf.text(25,195,titulo) 
    
    titulo = "RESULTADOS GEORREFERENCIADOS CONTRA EL NARCOTRÁFICO"
    pdf.text(25,205,titulo) 
    
    pdf.set_font('BebasNeue', '', 16)
    fechas= dia_semana + " " +str(fecha_inicial_dia) + " de " + str(fecha_inicial_mes) + " del "+ str(fecha_inicial_anio)
    fechas = fechas.upper()
    pdf.text(65,212,fechas) 
    pdf.set_text_color(125,0,0)
    texto_nivel = "PUBLICA RESERVADA "
    pdf.text(170,212,texto_nivel) 


    # pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/docna (2).JPG")
    # pdf.add_page()
    
    # pdf.set_text_color(125,0,0)
    # pdf.set_font('BebasNeue', '', 24)

    # fechas= str("resultados contra el narcotráfico del dia ")+dia_semana + " " +str(fecha_inicial_dia) + " de " + str(fecha_inicial_mes) + " del "+ str(fecha_inicial_anio)
    # fechas = fechas.upper()
    # pdf.text(38,28,fechas) 

    # titulo = "BOLETÍN DIARIO OPERACIONAL EJÉRCITO NACIONAL"

    
    # fecha_inicial_actual = str(fecha_inicial_anio) + "-" + str(fecha_inicial_mes)  + "-" + str(fecha_inicial_dia)

    # fechas_inicial = fecha(str(fecha_inicial_actual))

    # fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " DEL " + fechas_inicial[2] 
    # fecha_titulo = fecha_titulo.upper()
    
    # pdf.set_text_color(70,70,70)
    # pdf.set_font('Calibri', 'B', 24)
    # pdf.text(70,193, titulo)
    # pdf.set_font('Calibri', 'B', 14)
    # pdf.text(70,198, fecha_titulo)

    # pdf.set_font('Calibri', 'B', 10)
    # pdf.set_text_color(90,90,90)

    # pdf.text(70,207, 'JEMPP - CEDE3 - DISEO ')
    # pdf.text(180,207, 'RESTRINGIDO')
    # pdf.set_alpha(0)
    # pdf.set_draw_color(217,217,217)
    # pdf.set_line_width(1.5)
    # pdf.line(95, 203, 95, 208)
    # pdf.line(160, 203, 160, 208)

    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_final[0] + " "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/docna (2).JPG")

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 30)

    titulo = "JEFATURA DE ESTADO MAYOR DE OPERACIONES"
    pdf.text(65,20,titulo) 
    
    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 24)
    fechas= str("resultados contra el narcotráfico desde el ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    fechas = fechas.upper()
    pdf.text(65,30,fechas) 

    #TITULO DE PIUE DE PAGINA
    pdf.set_text_color(40,40,40)
    pdf.set_font('BebasNeue', '', 16)

    # fecha_inicial_mes = mes(fecha_inicial_mes)
    pdf.set_font('BebasNeue', '', 16)
    unidad= "DOCNA"
    unidad = unidad.upper()
    pdf.text(50,212,unidad) 
    pdf.set_text_color(125,0,0)
    texto_nivel = "PUBLICA RESERVADA "
    pdf.text(170,212,texto_nivel) 

    pdf.set_font('BebasNeue', '', 16)
    texto_nivel = "fuente: SICOE "
    pdf.text(300,212,texto_nivel) 

    dia_anterior = int(fecha_inicial_dia) - 1


    fecha_dia_anterior = str(fecha_inicial_anio)+"-"+str("01")+"-"+str("01")
    calcular_spoa =  Calculo_Spoa()
    calcular_spoa.resultados_narcotrafico_valores(fecha_inicial_u_l, fecha_final_u_l, fecha_dia_anterior, filtro, pdf, anio)



    # pdf.parametros(ttamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/docna (4).JPG")
    # dato  = ""


    # pdf.add_page()
    # pdf.set_text_color(125,0,0)
    # pdf.set_font('BebasNeue', '', 24)

    # fechas= str("resultados contra el narcotráfico del dia ")+dia_semana + " " +str(fecha_inicial_dia) + " de " + str(fecha_inicial_mes) + " del "+ str(fecha_inicial_anio)
    # fechas = fechas.upper()
    # pdf.text(38,28,fechas) 



    # titulo  =  titulos_name(filtro)
    # if titulo != "":
    #     titulo = "RESULTADOS INTERDICCIÓN  ({})".format(titulo)
    # else:
    #     titulo = "RESULTADOS INTERDICCIÓN DEL EJÉRCITO NACIONAL"

    # # pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    # caligrafia_ingreso( pdf, filtro[15])

    # fechas_inicial = fecha(fecha_inicial_u_l)
    # fechas_final = fecha(fecha_final_u_l)

    # fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    # fecha_titulo = fecha_titulo.upper()
  
    # pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG")
    # # pdf.set_margin(10,10,10,True)
    # pdf.set_auto_page_break(True, 6)
    # pdf.add_page()
    # # pdf.header()
    # # pdf.image("src/static/img/Imagen1.jpg", 50, 50)
    
    # # fechas en el titulo

    # # resultados_narcotrafico_boletin(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    # resultados_narcotrafico_valores(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]
  #funcion de resultados de contrabando 

  #Funcion en python para la creacion de resultado de nacrotrafico
