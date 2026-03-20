from flask import make_response
from datetime import date, time, datetime
from tipo_docker.y_r_resultados_dash.models.estadistica.estadistica_boletin_coe import *
from __init__ import *
from tipo_docker.z_z_configuarcion.caligrafia import *
from tipo_docker.z_z_configuarcion.fechas import *
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import *  
 
  
#comparativo por divisiones
def comparativo_comparativo_mapa(fecha_inicial_p_l, fecha_final_p_l, filtro, obj):


  
    resultados_spoa =  Calculo_Spoa(fecha_inicial_p_l, fecha_final_p_l, filtro, obj)
    resultados = resultados_spoa.comparativo_mapa_2()

    return  [resultados]
