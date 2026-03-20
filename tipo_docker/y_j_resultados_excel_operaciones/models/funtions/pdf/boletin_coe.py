from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_j_resultados_excel_operaciones.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  

import openpyxl
 
#comparativo por divisiones
#resultados para sacar el boletin de DISEO

#RESULTADOS COMPARATIVOS PARA EL BOLTIN DE DISEO
def resultados_resaltantes_comparativo_div(fecha_inicial_u_l, fecha_final_u_l,  filtro, dirercion_archvios, nombre_carpeta):

 
    wb = openpyxl.Workbook()
    # hoja = wb.active

    
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


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION_3')
    
    wb.save(dirercion_archvios+ "resultados tipo operaciones.xlsx")

    
    titulo = "resultados tipo operaciones"

    direcion= DIRECION+nombre_carpeta+str(titulo)+'.xlsx'
    return [direcion, titulo]
