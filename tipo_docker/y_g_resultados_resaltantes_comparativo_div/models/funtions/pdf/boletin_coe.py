from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_g_resultados_resaltantes_comparativo_div. models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
from datetime import datetime, timedelta
 
#comparativo por divisiones
#resultados para sacar el boletin de DISEO

#RESULTADOS COMPARATIVOS PARA EL BOLTIN DE DISEO
def resultados_resaltantes_comparativo_div(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):
    calcular_spoa =  Calculo_Spoa()
    #en el presente bloque de codigo se llama la creacion de las portadas de las ayudas
    #---------------------------------------------------------#
    #--------------portadas de las laminas--------------------#
    #---------------------------------------------------------#

    # pdf.parametros(titulo, "oficio", filtro[11], fecha_titulo, filtro[12], filtro[13], filtro[14])
    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva2.JPG")
    pdf.add_page()
  
    pdf.parametros( tamanio = "oficio",   permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva10.JPG")
    pdf.add_page()

    titulo = "BOLETÍN SEMANAL"
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
    pdf.text(35,110, titulo)
    pdf.text(35,125, titulo_1)
    pdf.text(35,140, titulo_2)
    pdf.set_text_color(80,80,80)
    pdf.set_font('Calibri', 'B', 30)
    pdf.text(35,155, str(fecha_titulo))

    pdf.set_font('Calibri', 'B', 14)
    pdf.set_text_color(200,0,0)

    
    pdf.text(190,213, "JEMPP - CEDE3 - DISEO ")
    pdf.text(240,213, 'RESTRINGIDO')
    
    pdf.set_font('Calibri', 'B', 10)
    pdf.set_text_color(90,90,90)


    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)
    

    # ✅ Convertir el string a objeto datetime
    fecha_obj = datetime.strptime(fecha_final_u_l, "%Y-%m-%d")

    # ✅ Restar 8 días
    nueva_fecha = fecha_obj - timedelta(days=7)

    # ✅ Si necesitas devolverla como string al front
    nueva_fecha_str = nueva_fecha.strftime("%Y-%m-%d")
    nueva_fecha_str_sep = fecha(nueva_fecha_str)

    fecha_titulo = nueva_fecha_str_sep[0] +" "+nueva_fecha_str_sep[1] +" AL "+ fechas_final[0] + " "+fechas_final[1] + " DEL "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    dato  = ""



    calcular_spoa.resultados_resaltantes_pdf_oficio(nueva_fecha_str, fecha_final_u_l, filtro, pdf, dato)

    #---------------------------------------------------------------------------
    #--------------------------Resultados comparativos  ------------------------
    #---------------------------------------------------------------------------
    
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_p_final = fecha(fecha_inicial_p_l)
    fechas_f_final = fecha(fecha_final_p_l)

    fecha_titulo_dos_ =  fechas_p_final[0] + " "+fechas_p_final[1] + " AL " + fechas_f_final[0] + " "+fechas_f_final[1] +" "+fechas_f_final[2] 
    fecha_titulo_dos_ = fecha_titulo_dos_.upper()





    fechas_final_final = fecha(fecha_final_u_l)
    

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos =  nueva_fecha_str_sep[0]+" " +nueva_fecha_str_sep[1]+" AL "+fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2] 
    fecha_titulo_dos = fecha_titulo_dos.upper()


    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    
    fechas_final[2] 
    fechas_inicial[2]

    titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"
    fecha_titulo_ =""

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")

    pdf.set_auto_page_break(True, 4)
    pdf.add_page()
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    
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
    divfe_ayuda = '{}static/img/diviciones/divfe_ayuda.png'.format(filtro[15])
   

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
    #pdf.image(imagen,277,153,79,63)

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
    pdf.image(divfe_ayuda,179,156,20,20)
    pd

    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 4)
    
    # fechas en el titulo

    calcular_spoa.resultados_diarios_divisiones(pdf, nueva_fecha_str, fecha_final_u_l, filtro, fecha_titulo_dos)

    #---------------------------------------------------------------------------
    #--------------------------Resultados comparativos  ------------------------
    #---------------------------------------------------------------------------

    divisiones = ["DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "DIVFE", "DAVAA", "FUTOM", "FTCEC"]

    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    
    fechas_final[2] 
    fechas_inicial[2]

    fecha_titulo_titulo = "("+ str(fechas_inicial[2]) + " - " + str(fechas_final[2]) + ")"



    titulo = "BALANCE RESULTADOS OPERACIONALES {}".format(fecha_titulo_titulo)

    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "NO" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    # pdf.set_margin(10,10,10,True)
    
    pdf.add_page()  

    titulo = "BALANCE RESULTADOS OPERACIONALES {}".format(fecha_titulo_titulo)
    dato = ["", "", ""]
    
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
    pdf.set_auto_page_break(True, 4)
    

    calcular_spoa.resultados_resaltantes_pdf_comparativo(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo_dos_, fecha_titulo, dato)

    pdf.set_auto_page_break(True, 4)

    

    for division in divisiones:
        
        # print(division)

        # print(division)


        if division == "APOYO DAVAA":
            
            titulo = "BALANCE RESULTADOS OPERACIONALES - {} {} ".format(division,fecha_titulo_titulo)
            dato =  ["hop_accion_davaa", "hop_accion_davaa", "mpio_erradicacion", "SI"]
            dato = union_filtro(dato)
        
        elif division == "APOYO CONAT":
            
            titulo = "BALANCE RESULTADOS OPERACIONALES- {} {}".format(division, fecha_titulo_titulo)
            dato =  ["hop_apoyo_conat", "hop_apoyo_conat", "mpio_erradicacion", "S"]
            dato = union_filtro(dato)

        else:
            titulo = "BALANCE RESULTADOS OPERACIONALES - {} {}".format(division, fecha_titulo_titulo)
            dato = ["agr_div", "agr_div", "agr_div", division]
            dato = union_filtro(dato)
            
    # fechas en el titulo
        
        fechas_inicial = fecha(fecha_inicial_u_l)
        fechas_final = fecha(fecha_final_u_l)

        fechas_inicial_final = fecha(fecha_inicial_p_l)
        fechas_final_final = fecha(fecha_final_p_l)

        fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
        fecha_titulo = fecha_titulo.upper()

        fechas_inicial = fecha(fecha_final_p_l)
        fechas_final = fecha(fecha_final_u_l)
        
        fechas_final[2] 
        fechas_inicial[2]

        fecha_titulo_titulo = "("+ str(fechas_inicial[2]) + " - " + str(fechas_final[2]) + ")"

        pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = "static/img/oficio/Diapositiva18_DISEO.JPG", seguridad="DISEO")
        pdf.set_auto_page_break(True, 4)
        pdf.add_page()  

        calcular_spoa.resultados_resaltantes_pdf_comparativo(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2], fecha_titulo_dos_, fecha_titulo, dato)
          
        
        # print(fechas_final[2])
        # print(fechas_inicial[2])

    titulo = "BOLETIN_DISEO_SEMANAL"
    direcion = dirercion_archvios+str("BOLETIN_DISEO_SEMANAL")+'.pdf'
    pdf.output(direcion, 'F')
    
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]
