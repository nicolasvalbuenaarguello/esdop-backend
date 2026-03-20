from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_e_cartilla_ejc_cdt. models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
#comparativo por divisiones
def cartilla_ejc(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):

    

    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    # pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/c_h.JPG")
    # pdf.add_page()
  
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva11.JPG")
    pdf.add_page()


    caligrafia_ingreso( pdf, filtro[15])

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
    titulo_unidad  =  titulos_name_cartilla(filtro)

    pdf.set_text_color(90,115,85)
    pdf.set_font('Calibri', 'B', 45)
    pdf.text(35,65, "REUNIÓN DE SEGURIDAD")
    pdf.text(35,90, "PRESIDENCIA DE LA")
    pdf.text(35,107, "REPÚBLICA")
    fecha_actual = str(dias) +"-"+ str(meses) +"-"+ str(anios)
    pdf.set_font('Calibri', 'B', 30)
    pdf.text(35,130, str(fecha_actual))
    if len(titulo_unidad[1])>0:
        municipios=titulo_unidad[1]
        if len(municipios) == 1:
            mpio = str(municipios)
            mpio = mpio.replace(",", "")
            mpio = mpio.replace("'", "")
            mpio = mpio.replace("[", "")
            mpio = mpio.replace("]", "")
            pdf.text(35,143, str(mpio))
        else:
            mpio = str(municipios)
            mpio = mpio.replace("[", "")
            mpio = mpio.replace("]", "")
            pdf.ln(100)
            pdf.cell(20)
            pdf.multi_cell(120,10, str(mpio),0,0,False)


    else: 
        municipios =""
    
    pdf.set_text_color(200,0,0)
    pdf.set_font('Calibri', 'B', 14)


    pdf.text(190,213, "EJC")
    pdf.text(240,213, 'RESERVADO')
    pdf.text(300,213, str(anios))
    
 
   
    #en el presente bloque de codigo se llama el mapa de las afectaciones.
    #---------------------------------------------------------#
    #---------------- mapa de afectaciones--------------------#
    #---------------------------------------------------------#

    titulo = "Proteger y fortalecer la Fuerza y sus capacidades estratégicas"
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()
    
    img_qr = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_e_cartilla_ejc_cdt/models/img_qr"
    imagen = "static/img/oficio/Diapositiva18.JPG"
    seguridad = "nueva_sin_mapa"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)
    pdf.add_page()
    pdf.set_auto_page_break(True, 6)
    
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)
    titulo_sub_2(pdf, municipios, filtro)

    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)

    calcular_spoa = Calculo_Spoa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo, fecha_titulo_dos)

    calcular_spoa.afectaciones_propias_tropas_mapa()


    #en el presente bloque de codigo se llama el listado de las afectaciones.
    #---------------------------------------------------------#
    #--------------listado de afectaciones--------------------#
    #---------------------------------------------------------#

    titulo = "Proteger y fortalecer la Fuerza y sus capacidades estratégicas"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)

    calcular_spoa.cuadro_afectaciones_pdf_comparativo()


    #en el presente bloque de codigo se llama las afectaciones a la amenaza
    #---------------------------------------------------------#
    #--------------afectaciones a la amenaza------------------#
    #---------------------------------------------------------#
    
    titulo = "AFECTACIONES A LA AMENAZA EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    calcular_spoa.resultados_afectaciones_a_la_amenaza()


    #en el presente bloque de codigo se llama los resultados comparativos del EJC
    #---------------------------------------------------------#
    #--------------------resultrados comparativos-------------#
    #---------------------------------------------------------#

    titulo = "RESULTADO DEL EJÉRCITO NACIONAL"


    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)

    calcular_spoa.resultados_resaltantes_r_n()
    

         
    #en el presente bloque de codigo se llama los resultado de narcotrafico
    #---------------------------------------------------------#
    #---------------resultados de narcotrafico----------------#
    #---------------------------------------------------------#

    titulo = "RESULTADOS NARCOTRÁFICO EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    calcular_spoa.resultados_narcotrafico_boletin()

      


    #en el presente bloque de codigo se llama los resultado de mineria
    #---------------------------------------------------------#
    #----------------resultados de mineria--------------------#
    #---------------------------------------------------------#

    titulo = "RESULTADOS MINERÍA ILEGAL DEL EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    calcular_spoa.resultados_mineria_boletin_comp()


    #en el presente bloque de codigo se llama los resultado de Contrabando
    #---------------------------------------------------------#
    #---------------resultados de contrabando-----------------#
    #---------------------------------------------------------#

    titulo = "RESULTADOS CONTRABANDO DEL EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    calcular_spoa.resultados_contrabando_boletin_comp()

        # #en el presente bloque de codigo se llama los resultado de EJC
    # #---------------------------------------------------------#
    # #--------------------resultados de artemisa--------------------#
    # #---------------------------------------------------------#
                
    titulo = "RESULTADO PLAN AMAZONÍA DEL EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad =  seguridad , img_qr = img_qr)

    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    titulo_sub_2(pdf, municipios, filtro)
    calcular_spoa.resultados_artemisas_boletin_comp()


 

    titulo  = "Cartilla Cdte Ejército Nacional"

    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'


    return [direcion, titulo]

