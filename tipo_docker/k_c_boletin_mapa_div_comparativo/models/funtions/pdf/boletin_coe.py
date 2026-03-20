from flask import make_response
from datetime import date, time, datetime
from tipo_docker.k_c_boletin_mapa_div_comparativo.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  


#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, dirercion_archvios, nombre_carpeta):

    pdf = PDF(orientation = 'L', unit = 'mm', format='legal')

    caligrafia_ingreso( pdf, filtro[15])
 
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)

    fechas_inicial_final = fecha(fecha_inicial_p_l)
    fechas_final_final = fecha(fecha_final_p_l)

    
    titulo_unidad  =  titulos_name_2(filtro,fechas_final[2] )

    if len(titulo_unidad[1])>0:
        municipios=tuple(titulo_unidad[1])
    else: 
        municipios =""
    titulo= titulo_unidad[0]

    fecha_anio_tres_inicial= str(int(fechas_inicial_final[2])-1)+"-"+str(fechas_inicial_final[3])+"-"+str(fechas_inicial_final[0])
    fecha_anio_tres_final = str(int(fechas_final_final[2])-1)+"-"+str(fechas_final_final[3])+"-"+str(fechas_final_final[0])

    fecha_titulo = fechas_inicial[0]+" " +  fechas_inicial[1] + " AL " + fechas_final[0] + " "+fechas_final[1] + " "+fechas_final[2]
    fecha_titulo = fecha_titulo.upper()

    fecha_titulo_dos = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+fechas_final_final[2]
    fecha_titulo_dos = fecha_titulo_dos.upper()

    anio = int(fechas_final_final[2])-1
    # print(anio)
    fecha_titulo_tres = fechas_inicial_final[0]+" " +  fechas_inicial_final[1] + " AL " + fechas_final_final[0] + " "+fechas_final_final[1] + " "+str(anio)
    fecha_titulo_tres = fecha_titulo_tres.upper()

    ruta = filtro[15] 
    #imagen ="static/img/oficio/Diapositiva18_DISEO.JPG"
    
    if filtro[0]=="" and filtro[0]=="---" and filtro[5]=="" and filtro[5]=="---":
        imagen ="static/img/oficio/Diapositiva20.JPG"

 
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0] == "FUTCO" or filtro[0] == "FUTOM":

            if filtro[0] == "FUTCO":
                unidad = "FUTCO"
            elif filtro[0] == "FUTOM":
                unidad = "FUTCO"
            else:
                unidad = filtro[0]

            
            imagen ="static/img/divisiones_2025/{}.JPG".format(unidad)
    elif filtro[5]!="" and filtro[5]!="---":
            imagen ="static/img/oficio/Diapositiva18_DISEO.JPG"
  
    else:
        imagen ="static/img/oficio/Diapositiva20.JPG"


    fecha_titulo_sub = 'Debilitar las capacidades de la amenaza'.format(fechas_final[2])
    pdf.parametros(titulo = titulo, tamanio = "oficio", logo = filtro[11], fecha_titulo = fecha_titulo_sub, permiso =filtro[12], nivel = filtro[13], usuario = filtro[14], pie_pagina = "SI" , ruta = filtro[15], imagen = imagen, seguridad="nueva")
    # pdf.set_margin(10,10,10,True)
    pdf.set_auto_page_break(True, 5)
    pdf.add_page()
    
    rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)
    if filtro[0]=="" or filtro[0]=="---":
        pdf.image(rosa_nautica,100, 40, 15, 15)
    elif filtro[0]=="DIV01" or filtro[0]=="DIV02" or filtro[0]=="DIV03" or filtro[0]=="DIV04" or filtro[0]=="DIV05" or filtro[0]=="DIV06" or filtro[0]=="DIV07" or filtro[0]=="DIV08" or filtro[0]=="FUTCO"  or filtro[0]=="FUTOM": 
        pass
    else:
        pdf.image(rosa_nautica,100, 40, 15, 15)

        
    if municipios !="":
        pdf.set_text_color(70,70,70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(175,27.5,str(municipios))
#--------
    if municipios !="":
        pdf.text(175,27.5,str(municipios)) 


    
    # fechas en el titulo
    fechas_inicial = fecha(fecha_final_p_l)
    fechas_final = fecha(fecha_final_u_l)
    resultados_spoa = Calculo_Spoa()
    resultados_spoa.comparativo_mapa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, fechas_final[2], fechas_inicial[2],fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio)
    
    

    direcion = dirercion_archvios+str("Evaluación objetivo estratégico 2")+'.pdf'
    pdf.output(direcion, 'F')
    DIRECION_3 = os.getenv('DIRECION_3')
    direcion= DIRECION_3+nombre_carpeta+str("Evaluación objetivo estratégico 2")+'.pdf'
    return [direcion, "Evaluación objetivo estratégico 2"]

