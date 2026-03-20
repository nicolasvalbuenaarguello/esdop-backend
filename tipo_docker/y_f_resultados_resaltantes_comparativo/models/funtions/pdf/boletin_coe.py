from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_f_resultados_resaltantes_comparativo. models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
#comparativo por divisiones
#resultados para sacar el boletin de DISEO
def resultados_resaltantes_comparativo(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios,nombre_carpeta):

    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    calcular = Calculo_Spoa()

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/c_h.JPG")
    pdf.add_page()
  
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/principal.JPG")
    pdf.add_page()

    titulo = "BOLETÍN DIARIO OPERACIONAL EJÉRCITO NACIONAL"

    caligrafia_ingreso( pdf, filtro[15])

    fecha_inicial_dia = datetime.now().day
    fecha_inicial_mes = datetime.now().month
    fecha_inicial_anio = datetime.now().year
    
    fecha_inicial_actual = str(fecha_inicial_anio) + "-" + str(fecha_inicial_mes)  + "-" + str(fecha_inicial_dia)

    fechas_inicial = fecha(str(fecha_inicial_actual))

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " DEL " + fechas_inicial[2] 
    fecha_titulo = fecha_titulo.upper()

    pdf.set_text_color(70,70,70)
    pdf.set_font('Calibri', 'B', 24)
    pdf.text(70,193, titulo)
    pdf.set_font('Calibri', 'B', 14)
    pdf.text(70,198, fecha_titulo)

    pdf.set_font('Calibri', 'B', 10)
    pdf.set_text_color(90,90,90)

    pdf.text(70,207, 'JEMPP - CEDE3 - DISEO ')
    pdf.text(180,207, 'RESTRINGIDO')
    pdf.set_alpha(0)
    pdf.set_draw_color(217,217,217)
    pdf.set_line_width(1.5)
    pdf.line(95, 203, 95, 208)
    pdf.line(160, 203, 160, 208)

    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo_dia = fechas_final[0] + " "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo_dia = fecha_titulo_dia.upper()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dia, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dia, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")
    dato  = ""
    calcular.resultados_resaltantes_pdf_oficio(fecha_final_u_l, fecha_final_u_l, filtro, pdf, dato)

    #---------------------------------------------------------------------------
    #--------------------------Resultados comparativos  ------------------------
    #---------------------------------------------------------------------------
    
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos =  fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    
    fechas_final[2] 
    fechas_inicial[2]
    fecha_titulo_dos_ =""
    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")

    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")
    
    imagen = '{}static/img/fondo_res_ayuda.png'.format(filtro[15])

    div01_ayuda = '{}static/img/diviciones/div01_ayuda.png'.format(filtro[15])
    div02_ayuda = '{}static/img/diviciones/div02_ayuda.png'.format(filtro[15])
    div03_ayuda = '{}static/img/diviciones/div03_ayuda.png'.format(filtro[15])
    div04_ayuda = '{}static/img/diviciones/div04_ayuda.png'.format(filtro[15])

    div05_ayuda = '{}static/img/diviciones/div05_ayuda.png'.format(filtro[15])
    div06_ayuda = '{}static/img/diviciones/div06_ayuda.png'.format(filtro[15])
    div07_ayuda = '{}static/img/diviciones/div07_ayuda.png'.format(filtro[15])
    div08_ayuda = '{}static/img/diviciones/div08_ayuda.png'.format(filtro[15])
    
    davaa_ayuda = '{}static/img/diviciones/davaa_ayuda.png'.format(filtro[15])
    omega_ayuda = '{}static/img/diviciones/omega_ayuda.png'.format(filtro[15])
    hercules_ayuda = '{}static/img/diviciones/hercules_ayuda.png'.format(filtro[15])


    # pdf.image(fondo,0,0,355.6,215.9)

    # pdf.image(titulo_ayuda,65,8,195,20)

    pdf.image(imagen,9,31,79,63)
    pdf.image(imagen,99,31,79,63)
    pdf.image(imagen,189,31,79,63)
    pdf.image(imagen,277,31,79,63)

    # pdf.image(div01_ayuda,0,80,20,20)
    pdf.image(imagen,9,91,79,63)
    pdf.image(imagen,99,91,79,63)
    pdf.image(imagen,189,91,79,63)
    pdf.image(imagen,277,91,79,63)

    pdf.image(imagen,9,153,79,63)
    pdf.image(imagen,99,153,79,63)
    pdf.image(imagen,189,153,79,63)
    pdf.image(imagen,277,153,79,63)

    pdf.image(div01_ayuda,0,33,20,20)
    pdf.image(div02_ayuda,89,33,20,20)
    pdf.image(div03_ayuda,179,33,20,20)
    pdf.image(div04_ayuda,267,33,20,20)

    pdf.image(div05_ayuda,0,93,20,20)
    pdf.image(div06_ayuda,89,93,20,20)
    pdf.image(div07_ayuda,179,93,20,20)
    pdf.image(div08_ayuda,267,93,20,20)

    pdf.image(davaa_ayuda,0,156,20,20)
    pdf.image(omega_ayuda,89,156,20,20)
    pdf.image(hercules_ayuda,179,156,20,20)


    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 4)
    
    # fechas en el titulo
    dato =""
    calcular.resultados_diarios_divisiones(pdf, fecha_final_u_l, fecha_final_u_l, filtro, fecha_titulo_dia, dato)

    #---------------------------------------------------------------------------
    #--------------------------Resultados comparativos  ------------------------
    #---------------------------------------------------------------------------
     
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    
    fechas_final[2] 
    fechas_inicial[2]

    fecha_titulo_titulo = "("+ str(fechas_inicial[2]) + " - " + str(fechas_final[2]) + ")"

    titulo = "BALANCE RESULTADOS OPERACIONALES {}".format(fecha_titulo_titulo)

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")
    

    # fechas en el titulo
    dato = ""
    calcular.resultados_resaltantes_pdf_comparativo(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo_dos, fecha_titulo,  dato)


    titulo = "BOLETIN_DISEO"
    direcion = dirercion_archvios+str("BOLETIN_DISEO")+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]





