from flask import make_response
from datetime import date, time, datetime

from tipo_docker.t_c_resultados_resaltantes_div.models.estadistica.estadistica_boletin_coe import *

from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *
from tipo_docker.z_z_z_funtions.funciones import * 
from __init__ import * 
#Funcion para la creacion del reporte de resultados 

#RESULTADOS COMPARATIVOS
def resultados_resaltantes_div(fecha_inicial_u_l, fecha_final_u_l, filtro, dirercion_archvios, nombre_carpeta):

    

    pdf = PDF(orientation = 'L', unit = 'mm', format='letter')

      
    pdf.parametros( tamanio = "carta",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/carta/Diapositiva1.JPG")
    pdf.add_page()
          
    pdf.parametros( tamanio = "carta",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/carta/Diapositiva2.JPG")
    pdf.add_page()


    pdf.set_auto_page_break(True, 4)


    caligrafia_ingreso( pdf, filtro[15])
    
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    

    img_qr = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/t_c_resultados_resaltantes_div/models/img_qr"
    
    pdf.parametros( tamanio = "carta",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/carta/Diapositiva10.JPG", seguridad = "nueva" , img_qr = img_qr)
        
    pdf.add_page()
    pdf.set_auto_page_break(True, 4)


    titulo = "CUADRO RESULTADOS"
    titulo_2 = "DEL EJÉRCITO NACIONAL"

    pdf.set_text_color(50,50,50)
    pdf.set_font('Calibri', 'B', 40)
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


    divisiones = ["EJÉRCITO NACIONAL", "DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "DIVFE", "DAVAA","APOYO DAVAA", "APOYO CONAT", "FUTCO", "FTCEC"]
    
    for division in divisiones:

        # print(division)

        if division == "EJÉRCITO NACIONAL":
            titulo = "RESULTADO RESALTANTES - {}".format(division)
            dato = ["", "", ""]

        elif division == "APOYO DAVAA":
            
            titulo = "RESULTADO RESALTANTES - {}".format(division)
            dato =  ["hop_accion_davaa", "hop_accion_davaa", "mpio_erradicacion", "SI"]
            dato = union_filtro(dato)
        
        elif division == "APOYO CONAT":
            
            titulo = "RESULTADO RESALTANTES - {}".format(division)
            dato =  ["hop_apoyo_conat", "hop_apoyo_conat", "mpio_erradicacion", "S"]
            dato = union_filtro(dato)

        else:
            titulo = "RESULTADO RESALTANTES - {}".format(division)
            dato = ["agr_div", "agr_div", "agr_div", division]
            dato = union_filtro(dato)
            

        fechas_inicial = fecha(fecha_inicial_u_l)
        fechas_final = fecha(fecha_final_u_l)

        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
        fecha_titulo = fecha_titulo.upper()

        pdf.parametros(titulo = titulo, tamanio = "carta", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15],  imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad = "nueva" , img_qr = img_qr)
        pdf.add_page()
        pdf.ln(5)
        pdf.set_auto_page_break(True, 4)
        resultados_spoa = Calculo_Spoa()
        resultados_spoa.resultados_resaltantes_pdf(fecha_inicial_u_l, fecha_final_u_l, filtro, pdf, dato)
    
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    
    pdf.parametros(tamanio = "carta",  permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/carta/Diapositiva19.JPG")
    pdf.add_page()

    
    titulo = "resultados resaltantes por div"
    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]