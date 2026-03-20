from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_d_cartilla_ejc_cdt_r. models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
#comparativo por divisiones
def cartilla_ejc_cdt_r(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):
    
    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    pdf.parametros(tamanio = "oficio",  pie_pagina = "NO", permiso =filtro[12], nivel = filtro[13], usuario = filtro[14],  ruta = filtro[15], imagen = "static/img/oficio/Diapositiva13.JPG")
   
    pdf.add_page()
    pdf.set_auto_page_break(True, 10)

    caligrafia_ingreso( pdf, filtro[15])

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()


    titulo  =  titulos_name(filtro)
    if titulo != "":
        titulo = "CUADRO RESULTADO"
        titulo_2 = "DEL EJÉRCITO NACIONAL"
    else:
        titulo = "CUADRO RESULTADOS"
        titulo_2 = "DEL EJÉRCITO NACIONAL"

    pdf.set_text_color(50,50,50)
    pdf.set_font('Calibri', 'B', 55)
    pdf.text(35,93, titulo)
    pdf.text(35,110, titulo_2)
    pdf.set_text_color(80,80,80)
    pdf.set_font('Calibri', 'B', 30)
    pdf.text(35,125, fecha_titulo)

    pdf.set_font('Calibri', 'B', 14)
    pdf.set_text_color(200,0,0)

    dias = datetime.now().day
    meses = datetime.now().month
    anios = datetime.now().year

    meses = str(mes(meses))
    meses = meses.upper()
    fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)
    pdf.text(190,213, fecha_actual)
    pdf.text(240,213, 'JEMOP - DIROP ')
    pdf.text(300,213, 'SECRETO')


    img_qr =  "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_c_boletin_estadistica/models/qr_img"


    titulo = "RESULTADOS DEL EJÉRCITO NACIONAL"
    
   

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    dias = datetime.now().day
    meses = datetime.now().month
    anios = datetime.now().year



    meses = str(mes(meses))
    meses = meses.upper()
    fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)


    titulo = "RESULTADO DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)
    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)

    calcular_spoa = Calculo_Spoa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo, fecha_titulo_dos)
    calcular_spoa.resultados_resaltantes_r_n()
    
    #en el presente bloque de codigo se llama las afectaciones a la amenaza
    #---------------------------------------------------------#
    #--------------afectaciones a la amenaza------------------#
    #---------------------------------------------------------#
    
    titulo = "AFECTACIONES A LA AMENAZA EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    
    calcular_spoa.resultados_afectaciones_a_la_amenaza()

    #en el presente bloque de codigo se llama el listado de las afectaciones.
    #---------------------------------------------------------#
    #--------------listado de afectaciones--------------------#
    #---------------------------------------------------------#

    titulo = "AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18.JPG", seguridad="nueva_sin_mapa", img_qr =img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    
    calcular_spoa.cuadro_afectaciones_pdf_comparativo()

    titulo  = "cartilla Cdte Ejército Nacional"

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]

