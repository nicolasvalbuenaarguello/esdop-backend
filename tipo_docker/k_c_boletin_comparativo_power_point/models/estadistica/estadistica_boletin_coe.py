# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.k_c_boletin_comparativo_power_point.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.k_c_boletin_comparativo_power_point.models.funtions.componest.tablas import *
from tipo_docker.k_c_boletin_comparativo_power_point.maps.funciones.mapa_filtro import *
import json


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
        
        numero_id = 1
        for x in no_spoa:
            self.f.write(str(nombre)+", " + str(x[26])+", " +str(x[0])+", "+str(x[29])+", "+str(x[1])+"\n")
            numero_id = numero_id + 1

        # f.write("-----------------------------------------------------"+"\n")
        # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

        if validar == "SI":
            spoa = spoa
        else:
            spoa =  res_calculo[numero]
            

        return[spoa, no_spoa]



    def comparativo_mapa(self, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro):

        ruta = filtro[15] 
        json_ruta = '{}static/MUNICIPIOS filtrados.json'.format(ruta)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
            nueva_2=[]
            departamento_tuple=[]
            for x in data:
                for y in data[x]:
                    if y['AGR_DIV'] == filtro[0]:
                        nueva_2.append(y['MPIO'])
                        departamento_tuple.append(y['DPTO'])

        if len(nueva_2) > 1:
                ids = tuple(nueva_2)
                ids_2 = tuple(departamento_tuple)

                dato = "and dpto = '{}' and mpio in {}".format(ids_2, ids)
                dato_res= "and hop_depto = '{}' and hop_mpio in {}".format(ids_2, ids)
                         

        dato =""
        
        if  filtro[4] == "lugar":
            if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
                nueva=filtro[6].split(",")
                dato = ""
                dato_res=""
                if len(nueva) > 1:
                        ids = tuple(nueva)
                        if filtro[7] !="" and filtro[7] !="---" and filtro[6]!="---" :
                            dato = "and dpto = '{}' and mpio in {} and enemigo = '{}'".format(filtro[5], ids, filtro[7])
                            dato_res= "and hop_depto = '{}' and hop_mpio in {} and hop_enemigo = '{}'".format(filtro[5], ids, filtro[7])
           
                        else:
                            dato = "and dpto = '{}' and mpio in {} ".format(filtro[5], ids)
                            dato_res= "and hop_depto = '{}' and hop_mpio in {} ".format(filtro[5], ids)
                            print("--///--")

                else:
                    mpio = nueva[0]  

                    if  filtro[7] !="" and filtro[7] !="---"  and filtro[6]!="---":
                        dato = "and {} = '{}' and {} = '{}' and enemigo = '{}'".format("dpto",filtro[5], "mpio",mpio, filtro[7])
                        dato_res = "and {} = '{}' and {} = '{}' and hop_enemigo = '{}'".format("hop_depto", filtro[5], "hop_mpio",mpio, filtro[7])
                    else:
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
        # print(query_actual)
        query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)


        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
 

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
   

    


        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)

        datos_enemigo = [["ITEM", "2025", "2026", "DIF", "%"]]

        # 🔹 Helper
        def agregar_resultado(origen_ant, origen_act, texto):
            resultado = calculo_comprativo_total(origen_ant, origen_act, 18, 1, texto)
            datos_enemigo.append(resultado)

        # 🔹 Casos directos (más limpio con zip)
        casos_directos = [
            (0, "MENORES RECUPERADOS"),
            (1, "PRESENTACIÓN VOLUNTARIA"),
            (2, "SOMETIMIENTOS"),
        ]

        for idx, texto in casos_directos:
            agregar_resultado(res_calculo_ante[idx], res_calculo_act[idx], texto)

        # 🔹 CAPTURAS (condicional)
        indice_captura = 61 if filtro[17] == "sin_delco" else 3

        val_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, indice_captura, "SI")
        val_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, indice_captura, "SI")

        agregar_resultado(val_ant[0], val_act[0], "CAPTURAS")

        # 🔹 MDOM
        val_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 4, "SI")
        val_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 4, "SI")

        agregar_resultado(val_ant[0], val_act[0], "MDOM")




        armas=[]
        incide =[
                (7, "ARMAS DE LARGO ALCANCE"),
                (8, "ARMAS DE CORTO ALCANCE"),
                (9, "ARMAS DE ACOMPAÑAMIENTO"),
                (10, "MUNICIONES")
                ]
        for idx, texto  in incide:
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, idx,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, idx,  "SI") #funcion para filtar el spoa
            resultado = calculo_comprativo_total(valor_ant[0], valor_act[0], 18, 1, texto)
            armas.append(resultado)

        combates=[]
        incide =[
                (11, "COMBATES POSITIVOS"),
                (12, "COMBATES NEGATIVOS"),
                (14, "TOTAL DE COMBATES")
                 ]
        
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx], 14, 1, texto)
            combates.append(resultado)


        explosivos=[]
        incide =[
                (16, "A.E"),
                (17, "MAP "),
                (18, "EXPLOSIVOS kg"),
                (19, "CORDÓN DETONANTE m"),
                (20, "CORDÓN DE SEGURIDAD m"),
                (72, "MEDIOS DE LANZAMIENTO")
                ]
        resultado = calculo_comprativo_total(res_calculo_ante[15], res_calculo_act[15], 14, 1, "NEUTRALIZACIÓN TERRORISTA")
        explosivos.append(resultado)
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx],  18, 1, texto)
            explosivos.append(resultado)

        datos_narcotrafico = [["ITEM", "2025", "2026", "DIF", "%"]]
        incide =[
                    (21, "COCAÍNA Kg"),
                    (22, "MARIHUANA Kg"),
                    (23, "PBC Kg"),
                    (24, "LAB. DE COCAÍNA"),
                    (25, "LAB. BASE DE COCA"),
                    (26, "SEMILLEROS"),                
                    ]
        for idx, texto  in incide:
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, idx,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, idx,  "SI") #funcion para filtar el spoa
            resultado = calculo_comprativo_total(valor_ant[0], valor_act[0],  18, 1, texto)
            datos_narcotrafico.append(resultado)


        eiym = []
        resultado = calculo_comprativo_total(res_calculo_ante[33], res_calculo_act[33],  18, 1, "CAPTURAS EIYM")
        eiym.append(resultado)

        resultado = calculo_comprativo_total(res_calculo_ante[35], res_calculo_act[35], 14, 1, "EIYM")
        eiym.append(resultado)


        maquinaria_anterior = res_calculo_ante[36] + res_calculo_ante[37] + res_calculo_ante[38] + res_calculo_ante[39] + res_calculo_ante[41]
        maquinaria_anctual = res_calculo_act[36] + res_calculo_act[37] + res_calculo_act[38] + res_calculo_act[39] + res_calculo_act[41]

        resultado = calculo_comprativo_total(maquinaria_anterior, maquinaria_anctual,  18, 1, "MAQUINARIA AMARILLA")
        eiym.append(resultado)

        resultado = calculo_comprativo_total(res_calculo_ante[65], res_calculo_act[65],  18, 1, "COLTÁN kg")
        eiym.append(resultado)


        liberta_personal=[]
        incide =[
                    (42, "LIBERADOS"),
                    (43, "RESCATADOS")
                ]
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx],  18, 1, texto)
            liberta_personal.append(resultado)

        hidrocarburos=[]
        incide =[
                    (44, "VÁLVULAS"),
                    (45, "REFINERÍAS")
                ]
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx],  18, 1, texto)
            hidrocarburos.append(resultado)


        contrabando=[]
    
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 49,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 49,  "SI") #funcion para filtar el spoa
        resultado = calculo_comprativo_total(valor_ant[0], valor_act[0],  18, 1, "CAPTURAS CONTRABANDO")
        contrabando.append(resultado)
        incide =[
                    (94, "LICORES CONTRABANDO"),
                    (96, "TELÉFONOS CONTRABANDO"),
                    (62, "COMBUSTIBLES CONTRABANDO")
                ]
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx],  18, 1, texto)
            contrabando.append(resultado)


        amazonia=[]
    
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        resultado = calculo_comprativo_total(valor_ant[0], valor_act[0],  18, 1, "CAPTURAS LOE AMAZONÍA")
        amazonia.append(resultado)
        incide =[
                    (32, "MADERA INCAUTADA"),
                    (63, "ANIMALES INCAUTADOS"),
                    (31, "PLÁNTULAS SEMBRADAS")
                ]
        for idx, texto  in incide:
            resultado = calculo_comprativo_total(res_calculo_ante[idx], res_calculo_act[idx],  18, 1, texto)
            amazonia.append(resultado)

        return [
                datos_enemigo,#0 
                armas,  #1
                combates,  #2
                explosivos,  #3
                datos_narcotrafico,  #4
                eiym,  #5
                liberta_personal,  #6
                hidrocarburos,  #7
                contrabando,  #8
                amazonia #9
                ]

