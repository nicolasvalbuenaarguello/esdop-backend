from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_k_resultados_excel_plano.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import * 

import pandas as pd 

import openpyxl
 
#comparativo por divisiones
#resultados para sacar el boletin de DISEO

#RESULTADOS COMPARATIVOS PARA EL BOLTIN DE DISEO
def resultados_resaltantes_comparativo_div(fecha_inicial_u_l, fecha_final_u_l,  filtro, dirercion_archvios, nombre_carpeta):

 
    wb = openpyxl.Workbook()
    # hoja = wb.active

    titulo  =  titulos_name(filtro)
    municipios= ""
    # print(titulo)
    if  filtro[4] == "lugar":
        if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
            titulo = "ARCHIVO PLANO"
            municipios = str(filtro[6])
        else:
            titulo = "ARCHIVO PLANO ({})".format(titulo)
    else:
        if titulo != "":
            titulo = "ARCHIVO PLANO ({})".format(titulo)
        else:
            titulo = "ARCHIVO PLANO DEL EJÉRCITO NACIONAL"
    
    fechas_inicial = fecha(fecha_inicial_u_l)
    fechas_final = fecha(fecha_final_u_l)


    # titulo = "EXCEL"
    # direcion = dirercion_archvios+str("productos")+'.xlsx'
    # wb.save(direcion)
    
    # DIRECION_3 = os.getenv('DIRECION_3')
    # direcion= DIRECION_3+str(titulo)+'.xlsx'


    dato  = ""
    calcular = Calculo_Spoa()
    calcular.resultados_resaltantes_pdf_oficio( fecha_inicial_u_l, fecha_final_u_l, filtro, dato, wb)

    # df_ref = pd.DataFrame(valor_calculado)
    
    #------------------------
    # LINK = os.getenv('DIRECION_3_B')
    # archivo = "RESULTADO_SIN_SPOA" +".txt" 
    # jungle_zip = zipfile.ZipFile(LINK+'resultados.zip', 'w')
    # jungle_zip.write(LINK+archivo, compress_type=zipfile.ZIP_DEFLATED)
    # jungle_zip.close()
    # DIRECION = os.getenv('DIRECION_3')
    # # df_ref.to_csv(LINK+ "resultados UT.csv")
    # # df_ref.to_excel
    # # df_ref.to_excel(LINK+ "resultados UT.xlsx")
    # # wb.save(LINK+ "resultados UT.xlsx")


    # titulo = "resultados"
    # # resultados.zip

    # direcion= DIRECION+str(titulo)+'.zip'
    #------------------------

    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
    
    wb.save(dirercion_archvios+ str(titulo)+'.xlsx')

    
    # titulo = "resultados UT"

    direcion= DIRECION+nombre_carpeta+str(titulo)+'.xlsx'
    print(direcion)
    return [direcion, titulo]
