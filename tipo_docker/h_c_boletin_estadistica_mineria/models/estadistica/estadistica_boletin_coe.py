# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.h_c_boletin_estadistica_mineria.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.h_c_boletin_estadistica_mineria.models.funtions.componest.tablas import *
from tipo_docker.h_c_boletin_estadistica_mineria.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()

import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            pass

    def validar_spoa_unidad(self, filtro, res_calculo, numero, validar):
        spoa=[]
        no_spoa=[]
        
        if validar == "SI":
            
            startdate = pd.to_datetime("2024-06-04").date()
            # startdate = pd.to_datetime("2024-01-01").date()
            
            if filtro[16] == "sin_spoa" or filtro[16] == "res_sin_spoa" :
                for x in res_calculo[numero]:
            
                    if x[0] >= startdate:

                        # if x[29] =="-" or  x[29] =="" or  x[29] =="0":
                        if x[29] =="-" or  x[29] =="" or len(x[29]) != 21 or  x[29] =="0":
                            no_spoa.append(x)
                            # print(x[29])
                        else: 
                            numero_dep = x[29][0:5]
                                
                            # if numero_dep == "00000":
                            #     no_spoa.append(x)
                            # else:
                            #     spoa.append(x)
                            spoa.append(x)

                    else: 
                        spoa.append(x)      
            else:
                spoa =  res_calculo[numero]

                

            spoa = spoa
        else:
            spoa =  res_calculo[numero]

        if filtro[16]== "res_sin_spoa":
                    # print(len(no_spoa))
                    spoa = no_spoa
        #DOCUMENTOS SIN SPOA

        return[spoa, no_spoa]

    def validar_spoa(self, filtro, res_calculo, numero, nombre, validar):
        spoa=[]
        no_spoa=[]
        
        startdate = pd.to_datetime("2024-06-04").date()
        # startdate = pd.to_datetime("2024-01-01").date()
        
        if filtro[16] == "sin_spoa" or filtro[16] == "res_sin_spoa" :
            for x in res_calculo[numero]:
        
                if x[0] >= startdate:

                    if x[29] =="-" or  x[29] =="" or  x[29] =="0":
                    # if x[29] =="-" or  x[29] =="" or len(x[29]) != 21 or  x[29] =="0":
                        no_spoa.append(x)
                        # print(x[29])
                    else: 
                        numero_dep = x[29][0:5]
                            
                        # if numero_dep == "00000":
                        #     no_spoa.append(x)
                        # else:
                        #     spoa.append(x)
                        spoa.append(x)

                else: 
                    spoa.append(x)      
        else:
            spoa =  res_calculo[numero]

        if filtro[16]== "res_sin_spoa":
                    # print(len(no_spoa))
                    spoa = no_spoa
        #DOCUMENTOS SIN SPOA

        
        # f.write(str(nombre)+"\n")
        # f.write("-----------------------------------------------------"+"\n")


        # f.write("-----------------------------------------------------"+"\n")
        # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

        if validar == "SI":
            spoa = spoa
        else:
            spoa =  res_calculo[numero]
            

        return[spoa, no_spoa]


    #funcion de para generar estadistica mineria 
    def resultados_mineria_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):
        
        dato =""

        filtros = selecion_filtro(filtro)

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro) #querys modificados

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos
        erradicacion = conexion_pos.comando_query(query[2]) #resultados de la base de datos
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        datos = [res_calculo[33], res_calculo[35], res_calculo[40], res_calculo[38], res_calculo[39], res_calculo[36], res_calculo[37], res_calculo[41], res_calculo[59], res_calculo[60], res_calculo[65]]

        
        datos_prueba = [res_calculo[0], res_calculo[1], res_calculo[2], res_calculo[3], res_calculo[4], res_calculo[7], res_calculo[8], res_calculo[9], res_calculo[16], res_calculo[17], res_calculo[35], res_calculo[41], res_calculo[36], res_calculo[37], res_calculo[38], res_calculo[39], res_calculo[21], res_calculo[22], res_calculo[23], res_calculo[24], res_calculo[25]]

        #encabezado de interdicion
        encabezado_tabla_resultados_mapa(pdf, "RESULTADOS MINERÍA ILEGAL ")
        pdf.ln(10)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa(pdf,"Capturas",valor[0], "Personas",18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Yacimientos Mineros ",datos[1], "Unidades", 14)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Unidad Producción Minera",datos[2], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Maquinaria Pesada ",datos[3], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Tractor Con Uruga ",datos[4], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Excavadoras",datos[5], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Retroexcavadoras",datos[6], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Dragas",datos[7], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Motores",datos[8], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Combustibles",datos[9], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Coltan",datos[10], "Kilos", 18)

        nombre = "mineria"
        # mapa_hechos_p(datos_prueba, nombre, filtro)
        # mapa_hechos(hechos, nombre, filtro)
        mapa_hechos(datos[1], nombre, filtro)
        
        
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

