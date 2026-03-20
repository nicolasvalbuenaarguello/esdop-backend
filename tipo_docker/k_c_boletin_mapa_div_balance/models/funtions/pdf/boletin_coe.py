from flask import make_response
from datetime import date, time, datetime
from tipo_docker.k_c_boletin_mapa_div_balance.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
import shutil


#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):
    titulo_unidad  =  titulos_name(filtro)

    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]


    #municipios = municipios.replace(",", ", ")


    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])
 
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    fecha_anio_tres_inicial= str(int(fechas_inicial_final[2])-1)+"-"+str(fechas_inicial_final[3])+"-"+str(fechas_inicial_final[0])
    fecha_anio_tres_final = str(int(fechas_final_final[2])-1)+"-"+str(fechas_final_final[3])+"-"+str(fechas_final_final[0])


    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " ( "+fechas_final_final[2]+" - " +fechas_final[2]+")"
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    anio = int(fechas_final_final[2])-1
    # print(anio)
    fecha_titulo_tres = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] +" ("+ str(fechas_final_final) +" - "+str(anio)+")"
    fecha_titulo_tres = fecha_titulo_tres.upper()

    ruta = filtro[15] 
    
    if filtro[0]=="" or filtro[0]=="---":
        imagen ="static/img/divisiones_2025/EJC.JPG"
 
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0]=="FUTCO":
        
        imagen ="static/img/divisiones_2025/{}.JPG".format(filtro[0])

    else:
        imagen ="static/img/divisiones_2025/EJC.JPG"


    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad ="nueva")
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 6)
    pdf.add_page()

    rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)
    if filtro[0]=="" or filtro[0]=="---":
        pdf.image(rosa_nautica,100, 40, 15, 15)
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0]=="FUTCO": 
        pass
    else:
        pdf.image(rosa_nautica,100, 40, 15, 15)

        
    if municipios !="":
        pdf.set_text_color(70,70,70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(150,36,str(municipios))
#--------
    if municipios !="":
        pdf.text(150,36,str(municipios)) 

            # print(titulo)
    if  filtro[4] == "lugar":
        if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
            municipios = str(filtro[6])
        else:
            titulo = titulo
    else:
        if titulo != "":
            titulo = titulo
        else:
            titulo = "RESULTADO DEL EJÉRCITO NACIONAL"
            nombre_doc = titulo
    
    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    resultados_spoa = Calculo_Spoa()


    
    resultados_spoa.comparativo_mapa_gracica_1(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)

    resultados_spoa.comparativo_mapa_grafica_2(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)
        
    resultados_spoa.comparativo_mapagrafica_3(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)
   
    resultados_spoa.comparativo_mapagrafica_4(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)

    resultados_spoa.comparativo_mapa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)
    

    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo1.png",135,55,100,80)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo2.png",240,50,100,80)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo3.png",140,140,100,70)
    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas//torta_code.png",255,130,65,65)
    

    pdf.set_text_color(125,0,0)
    pdf.set_font('BebasNeue', '', 16)
    pdf.text(270,210,str("SECRETO"))
    
    direcion = dirercion_archvios+str(titulo)+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str(titulo)+'.pdf'
    return [direcion, titulo]

