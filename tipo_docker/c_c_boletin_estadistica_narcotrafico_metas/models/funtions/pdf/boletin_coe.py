from flask import make_response
from datetime import date, time, datetime
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.models.estadistica.estadistica_boletin_coe import *

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
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva3.JPG")

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
    
    pdf.set_font('BebasNeue', '', 16)
    fechas= dia_semana + " " +str(fecha_inicial_dia) + " de " + str(fecha_inicial_mes) + " del "+ str(fecha_inicial_anio)
    fechas = fechas.upper()
   
    pdf.set_text_color(255,255,255)
    pdf.text(80,212,fechas) 
    texto_nivel = "PUBLICA RESERVADA "
    pdf.text(190,212,texto_nivel) 


    titulo = "DIRECCIÓN DE OPERACIONES"
    titulo_2 = "CONTRA EL NARCOTRÁFICO"
    titulo_3 = "ESTADÍSTICA DIARIA"
    titulo_4 = "DE INTERDICCIÓN"

    pdf.set_text_color(56,87,35)
    pdf.set_font('Calibri', 'B', 28)
    pdf.text(25,95, titulo)
    pdf.text(25,105, titulo_2)
    pdf.text(25,115, titulo_3)
    pdf.text(25,125, titulo_4)

    dias = datetime.now().day
    meses = datetime.now().month
    anios = datetime.now().year

    meses = str(mes(meses))
    meses = meses.upper()
    pdf.set_text_color(250,250,250)
    fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)
    pdf.text(240,213, 'JEMOP - DOCNA ')

    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_final[0] + " "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()
    calcular_spoa =  Calculo_Spoa()
#--------------------------------------------------------------------------------------
#--------------------------------//   \\-----------------------------------------------

    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/c_c_boletin_estadistica_narcotrafico_metas/models/qr_img"

    pdf.parametros(ttamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    dato  = ""


    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    #texto de la fecha de los resultados 
    pdf.set_text_color(255,255,255)
    pdf.set_font('BebasNeue', '', 16)
    fecha_resultado = dia_semana + " " +str(fecha_inicial_dia) + " de " + str(fecha_inicial_mes) + " del "+ str(fecha_inicial_anio)
    fechas = fechas.upper()
    pdf.text(80,6,fecha_resultado) 

    #titulo de la ayuda en negro
    pdf.set_text_color(0,0,0)
    pdf.set_font('BebasNeue', '', 28)
    titulo_ayuda= str("JEFATURA DE ESTADO MAYOR DE OPERACIONES")
    titulo_ayuda = titulo_ayuda.upper()
    pdf.text(55,20,titulo_ayuda) 

    
    #titulo de la ayuda en rejo
    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 28)
    titulo_ayuda= str("RESULTADOS CONTRA EL NARCOTRÁFICO")
    titulo_ayuda = titulo_ayuda.upper()
    pdf.text(55,28,titulo_ayuda) 

    #TITULO DE PIUE DE PAGINA
    pdf.set_text_color(40,40,40)
    pdf.set_font('BebasNeue', '', 16)

    # fecha_inicial_mes = mes(fecha_inicial_mes)
    pdf.set_font('BebasNeue', '', 16)
    unidad= "JEMOP-DOCNA"
    unidad = unidad.upper()
    pdf.text(50,212,unidad) 
    pdf.set_text_color(125,0,0)
    texto_nivel = "PUBLICA RESERVADA "
    pdf.text(170,212,texto_nivel) 

    pdf.set_font('BebasNeue', '', 16)
    texto_nivel = "fuente: SICOE "
    pdf.text(280,212,texto_nivel) 



    caligrafia_ingreso( pdf, filtro[15])

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()
  
    pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15],  imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    # pdf.set_margin(10,10,10,True)
    # pdf.set_auto_page_break(True, 6)
    # pdf.add_page()
    # pdf.header()
    # pdf.image("src/static/img/Imagen1.jpg", 50, 50)
    
    # fechas en el titulo

    # resultados_narcotrafico_boletin(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf)

    fecha_dia_anterior = str(fecha_inicial_anio)+"-"+str("01")+"-"+str("01")
    # calcular_spoa =  Calculo_Spoa()
    # print("1")
    calcular_spoa.resultados_narcotrafico_valores(fecha_inicial_u_l, fecha_final_u_l, fecha_dia_anterior, filtro, pdf, anio)



#--------------------------------//   \\-----------------------------------------------
#--------------------------------------------------------------------------------------



    pdf.parametros(tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15],  imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.set_text_color(0,0,0)
    pdf.set_font('BebasNeue', '', 28)

    titulo = "JEFATURA DE ESTADO MAYOR DE OPERACIONES"
    pdf.text(55,20,titulo) 
    
    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 25)
    fechas= str("resultados contra el narcotráfico desde el ")+str(fecha_inicial_dia_inicial) + " " +str(fecha_inicial_mes_inicial) + " hasta " + str(fecha_inicial_dia) + " de "+ str(fecha_inicial_mes) + " del " + str(fecha_inicial_anio)
    fechas = fechas.upper()
    pdf.text(55,28,fechas) 

    #TITULO DE PIUE DE PAGINA
    pdf.set_text_color(40,40,40)
    pdf.set_font('BebasNeue', '', 16)

    # fecha_inicial_mes = mes(fecha_inicial_mes)
    pdf.set_font('BebasNeue', '', 16)
    unidad= "JEMOP-DOCNA"
    unidad = unidad.upper()
    pdf.text(50,212,unidad) 
    pdf.set_text_color(125,0,0)
    texto_nivel = "PUBLICA RESERVADA "
    pdf.text(170,212,texto_nivel) 

    pdf.set_font('BebasNeue', '', 16)
    texto_nivel = "fuente: SICOE "
    pdf.text(280,212,texto_nivel) 

    dia_anterior = int(fecha_inicial_dia) - 1

    # print(fecha_inicial_dia)
    # print(dia_anterior)
    fecha_dia_anterior = str(fecha_inicial_anio)+"-"+str(fecha_inicial_mes_number)+"-"+str(dia_anterior)
    # print("2")
    calcular_spoa.resultados_narcotrafico_boletin(fecha_inicial_u_l, fecha_final_u_l,fecha_dia_anterior, filtro, pdf, anio)

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]
  #funcion de resultados de contrabando 

  #Funcion en python para la creacion de resultado de nacrotrafico
