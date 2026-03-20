# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.g_c_boletin_estadistica_contrabando_comp.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.g_c_boletin_estadistica_contrabando_comp.models.funtions.componest.tablas import *
from tipo_docker.g_c_boletin_estadistica_contrabando_comp.maps.funciones.mapa_filtro import *
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
    def resultados_contrabando_boletin_comp(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos):

        dato =""
        if  filtro[4] == "lugar":
            if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
                nueva=filtro[6].split(",")
                dato = ""
                dato_res=""
                if len(nueva) > 1:
                        ids = tuple(nueva)
                        dato = "and dpto = '{}' and mpio in {}".format(filtro[5], ids)
                        dato_res= "and hop_depto = '{}' and hop_mpio in {}".format(filtro[5], ids)

                else:
                    mpio = nueva[0]  
                    dato = "and {} = '{}' and {} = '{}'".format("dpto",filtro[5], "mpio",mpio)
                    dato_res = "and {} = '{}' and {} = '{}'".format("hop_depto", filtro[5], "hop_mpio",mpio)
                filtros =[dato_res, dato, ""]
            else:
                if dato == "":
                    filtros = selecion_filtro(filtro)
                else:
                    filtros = dato
        else:
            if dato == "":
                filtros = selecion_filtro(filtro)
            else:
                filtros = dato


        query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)
        query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        res_calculo_ante_2 = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo = estadistica_resultados(resultados_actual, hechos_actual, filtro)


        datos = [res_calculo[0], res_calculo[1], res_calculo[2], res_calculo[2], res_calculo[4], res_calculo[5], res_calculo[9], res_calculo[10], res_calculo[11], res_calculo[12], res_calculo[13], res_calculo[14]]

        res_calculo_ante = [res_calculo_ante_2[0], res_calculo_ante_2[1], res_calculo_ante_2[2], res_calculo_ante_2[2], res_calculo_ante_2[4], res_calculo_ante_2[5], res_calculo_ante_2[9], res_calculo_ante_2[10], res_calculo_ante_2[11], res_calculo_ante_2[12], res_calculo_ante_2[13], res_calculo_ante_2[14]]

        #encabezado de interdicion
        encabezado_tabla_resultados_mapa_compa(pdf, "RESULTADOS CONTRABANDO", anio_act, anio_ant)
        pdf.ln(10)

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_2, 0,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 0,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa_comp(pdf,"Capturas", valor_ant[0], valor_act[0], "Personas", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Gasolina",res_calculo_ante[1], datos[1], "Galones", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"ACPM",res_calculo_ante[2], datos[2], "Galones", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Insumos Líquidos",res_calculo_ante[3], datos[3], "Galones", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Vehículos",res_calculo_ante[4], datos[4], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Animales incautados",res_calculo_ante[5], datos[5], "Unidades", 18, 1)

        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Combustible de Contrabando",res_calculo_ante[7], datos[7], "Galones", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Licores",res_calculo_ante[8], datos[8], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Cigarrillos",res_calculo_ante[9], datos[9], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Telefonos",res_calculo_ante[10], datos[10], "Unidades", 18, 1)
        pdf.ln()
        tabla_resultados_con_mapa_comp(pdf,"Muebles Incautados",res_calculo_ante[11], datos[11], "Unidades", 18, 1)



        nombre = "contrabando"
        mapa_hechos(datos[6], nombre, filtro)

        
        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)


        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
    
