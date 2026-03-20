# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.i_c_boletin_estadistica_mineria_comparativo.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.i_c_boletin_estadistica_mineria_comparativo.models.funtions.componest.tablas import *
from tipo_docker.i_c_boletin_estadistica_mineria_comparativo.maps.funciones.mapa_filtro import *
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


    # cuadro de resultados resaltantes comparativos
    def resultados_mineria_boletin_comp(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos):

        filtros = selecion_filtro(filtro)

        query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)
        query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo = estadistica_resultados(resultados_actual, hechos_actual, filtro)

        datos = [res_calculo[33], res_calculo[35], res_calculo[40], res_calculo[38], res_calculo[39], res_calculo[36], res_calculo[37], res_calculo[41], res_calculo[59], res_calculo[60], res_calculo[65]]

        datos_ant = [res_calculo_ante[33], res_calculo_ante[35], res_calculo_ante[40], res_calculo_ante[38], res_calculo_ante[39], res_calculo_ante[36], res_calculo_ante[37], res_calculo_ante[41], res_calculo_ante[59], res_calculo_ante[60], res_calculo_ante[65]]
        #encabezado de interdicion

        encabezado_tabla_resultados_mapa_compa(pdf, "RESULTADOS MINERÍA ILEGAL ", anio_act, anio_ant)
        pdf.ln(10)
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa_comp(pdf,"Capturas", valor_ant[0], valor_act[0], "Personas", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Yacimientos Mineros ",datos_ant[1], datos[1], "Unidades", 14, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Unidad Producción Minera",datos_ant[2], datos[2], "Galones", 18, 1)
        pdf.ln()
        maquinaria_anterior = [res_calculo_ante[36], res_calculo_ante[37], res_calculo_ante[38], res_calculo_ante[39], res_calculo_ante[41]]
        maquinaria_anctual = [res_calculo[36], res_calculo[37], res_calculo[38], res_calculo[39], res_calculo[41]]
        tabla_resultados_con_mapa_comp_maquinaria(pdf, maquinaria_anterior, maquinaria_anctual, "Maquinaria Amarilla",1, 7, 18, "Unidades")
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Motores",datos_ant[8], datos[8], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Combustibles",datos_ant[9], datos[9], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Coltan",datos_ant[10], datos[10], "Kilos", 18, 1)

        nombre = "mineria"
        mapa_hechos(datos[1], nombre, filtro)
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

