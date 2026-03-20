from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_f_resultados_diseo_diario.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
#comparativo por divisiones
#resultados para sacar el boletin de DISEO
def resultados_resaltantes_comparativo(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):

    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    calcular = Calculo_Spoa()

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva2.JPG")
    pdf.add_page()
  
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img//oficio/Diapositiva15.JPG")
    pdf.add_page()

    titulo = "BOLETÍN DIARIO"
    titulo_1 = "OPERACIONAL"
    titulo_2 = "EJÉRCITO NACIONAL"

    caligrafia_ingreso( pdf, filtro[15])

    fecha_inicial_dia = datetime.now().day
    fecha_inicial_mes = datetime.now().month
    fecha_inicial_anio = datetime.now().year
    
    fecha_inicial_actual = str(fecha_inicial_anio) + "-" + str(fecha_inicial_mes)  + "-" + str(fecha_inicial_dia)

    fechas_inicial = fecha(str(fecha_inicial_actual))

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " DEL " + fechas_inicial[2] 
    fecha_titulo = fecha_titulo.upper()

    
    pdf.set_text_color(30,30,30)
    pdf.set_font('Calibri', 'B', 50)
    pdf.text(170,110, titulo)
    pdf.text(170,125, titulo_1)
    pdf.text(170,140, titulo_2)
    pdf.set_text_color(80,80,80)
    pdf.set_font('Calibri', 'B', 30)
    pdf.text(170,155, str(fecha_titulo))

    pdf.set_font('Calibri', 'B', 14)
    pdf.set_text_color(200,0,0)

    
    pdf.text(190,213, "JEMPP - CEDE3 - DISEO ")
    pdf.text(240,213, 'RESTRINGIDO')
    
    pdf.set_font('Calibri', 'B', 10)
    pdf.set_text_color(90,90,90)



    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fecha_titulo_dia = fechas_final[0] + " "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo_dia = fecha_titulo_dia.upper()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dia, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dia, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    dato  = ""
    calcular.resultados_resaltantes_pdf_oficio(fecha_final_u_l, fecha_final_u_l, filtro, pdf, dato)

    dir_qr = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/y_f_resultados_diseo_diario/models/funtions/pdf/qr/"
    
    import qrcode
    t = "Fuerzas Militares de Colombia"
    t_1 ="Ejército Nacional"
    t_2 = "Jefactura de Estado Mayor de Planeamiento y Politicas"
    t_3 = "Departamento de Operaciones"
    t_4 = "DISEO"
    
    inf= "Resultados del Dia:"
    fecha_Elaboracion = datetime.now()
    inf_qur = t+" \n" + t_1+" \n" + t_2+" \n" + t_3+" \n" + t_4+" \n" + inf+" \n" + fecha_titulo_dia +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +filtro[14]
    img = qrcode.make(inf_qur)
    f = open(dir_qr+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dir_qr+"QR.png",330,5,23,23)
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

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")

    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/contenido dos.JPG", seguridad="DISEO")
    pdf.image(dir_qr+"QR.png",330,5,23,23)
    
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
    #llamar la nueva hoja                                
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

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_dos_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    pdf.image(dir_qr+"QR.png",334,9.5,20,20)
    

    # fechas en el titulo
    dato = ""
    #llamar la nueva hoja
    calcular.resultados_resaltantes_pdf_comparativo(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo_dos, fecha_titulo,  dato)


    titulo = "BOLETIN_DISEO"
    direcion = dirercion_archvios+str("BOLETIN_DISEO")+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]





