# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from flask import json
from tipo_docker.c_c_boletin_estadistica_narcotrafico_power_point.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_power_point.models.funtions.componest.tablas import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_power_point.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import pandas as pd
class Calculo_Spoa:
    def __init__(self, fecha_inicial_u_l, fecha_final_u_l,fecha_dia_anterior, filtro,  anio, mes_l, mes_n, fecha_primer_lapso_final, fecha_ultimo_lapso_final):
        
        self.filtro = filtro
        self.anio = anio
        self.mes_l = mes_l
        self.mes_n = mes_n
        self.meta = 0
        self.filtros = selecion_filtro(self.filtro) #parametros de self.filtros
        dato =""
        if  self.filtro[4] == "lugar":
            if self.filtro[6]!="" and self.filtro[6]!="---" :#self.filtro por municipio
                nueva=self.filtro[6].split(",")
                dato = ""
                dato_res=""
                if len(nueva) > 1:
                        ids = tuple(nueva)
                        dato = "and dpto = '{}' and mpio in {}".format(self.filtro[5], ids)
                        dato_res= "and hop_depto = '{}' and hop_mpio in {}".format(self.filtro[5], ids)

                else:
                    mpio = nueva[0]  
                    dato = "and {} = '{}' and {} = '{}'".format("dpto",self.filtro[5], "mpio",mpio)
                    dato_res = "and {} = '{}' and {} = '{}'".format("hop_depto", self.filtro[5], "hop_mpio",mpio)
                self.filtros =[dato_res, dato, ""]
            else:
                if dato == "":
                    self.filtros = selecion_filtro(self.filtro)
                else:
                    self.filtros = dato
        else:
            if dato == "":
                self.filtros = selecion_filtro(self.filtro)
            else:
                self.filtros = dato

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, self.filtros, self.filtro) #querys modificados

        query_2 = parametros(fecha_final_u_l, fecha_final_u_l, self.filtros, self.filtro) #querys modificados

        self.resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        self.hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos

        self.res_calculo = estadistica_resultados(self.resultados, self.hechos, self.filtro)


        #encabezado de interdicion
        
        self.hechos_anterior = conexion_pos.comando_query(query_2[1]) #resultados de la base de datos
        self.resultados_anterior = conexion_pos.comando_query(query_2[0]) #resultados de la base de datos
        self.res_calculo_anterior = estadistica_resultados(self.resultados_anterior, self.hechos_anterior, self.filtro)

        #encabezado de interdicion
        query_3 = parametros(fecha_primer_lapso_final, fecha_ultimo_lapso_final, self.filtros, self.filtro) #querys modificados
        
        self.hechos_anterior_anio = conexion_pos.comando_query(query_3[1]) #resultados de la base de datos
        self.resultados_anterior_anio = conexion_pos.comando_query(query_3[0]) #resultados de la base de datos
        self.res_calculo_anterior_anio = estadistica_resultados( self.resultados_anterior_anio, self.hechos_anterior_anio, self.filtro)


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


            # f.write("-----------------------------------------------------"+"\n")
            # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

            if validar == "SI":
                spoa = spoa
            else:
                spoa =  res_calculo[numero]
                

            return[spoa, no_spoa]

    # resultados por enemigo 
    def resultados_narcotrafico_boletin(self):
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

                
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos_anterior = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        # datos_anterior = [self.res_calculo_anterior[21],self.res_calculo_anterior[23],self.res_calculo_anterior[29],self.res_calculo_anterior[22],self.res_calculo_anterior[47],self.res_calculo_anterior[48], self.res_calculo_anterior[28], self.res_calculo_anterior[24], self.res_calculo_anterior[25], self.res_calculo_anterior[26], self.res_calculo_anterior[65], self.res_calculo_anterior[66], self.res_calculo_anterior[67], self.res_calculo_anterior[68]]
        
            
        ruta = self.filtro[15] 
        json_ruta = '{}static/metas docna.json'.format(ruta)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
        # Unidades y tipos de sustancia
        unidades = [
            "EJC", "DAVAA",
            "DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "FUTOM"
        ]

        tipos = {
            "Clorhidrato de Cocaína": "COCAINA",
            "Pasta Base de Coca": "PBC",
            "Marihuana": "MARIHUANA",
            "Laboratorios (HCL)": "LAB COCAINA",
            "Laboratorios (PBC)": "LAB PBC"
        }

        # Inicializar diccionario dinámico para resultados
        valores_por_unidad = {
            unidad: {clave: 0 for clave in tipos.values()}
            for unidad in unidades
        }

        # Rellenar desde data
        for x in data:
            for y in data[x]:
                unidad = y["UNIDAD"]
                if unidad in valores_por_unidad:
                    for clave in tipos.values():
                        valores_por_unidad[unidad][clave] = y.get(clave, 0)

        # Ahora genera resultados_meta y color
        resultados_meta = []
        color = []

        # Índices de referencia en los datos (mantienes tu lógica)
        indices = {
            "Clorhidrato de Cocaína": 0,
            "Pasta Base de Coca": 1,
            "Marihuana": 3,
            "Laboratorios (HCL)": 7,
            "Laboratorios (PBC)": 8
        }

        for unidad in unidades:
            nombre_visible = "EJÉRCITO NACIONAL" if unidad == "EJC" else unidad  # Alias visual
            resultados_meta.append([nombre_visible, "META", self.anio, "%"])
            for nombre_largo, clave_data in tipos.items():
                idx = indices[nombre_largo]
                valor = valores_por_unidad[unidad][clave_data]
                res = calculo_de_interdion(nombre_largo, valor, datos[idx], datos_anterior[idx], nombre_visible)
                resultados_meta.append(res[0])
                color.append(res[1])

        return [resultados_meta, color]

    # resultados por enemigo 
    def resultados_narcotrafico_valores(self):
        

        # print("2-1")

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior, 69,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 27,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos_anterior = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]
        
        
        ruta = self.filtro[15] 
        resultados_listados= []
 
        valor = valores_tabla_interdicion(datos[0] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")

        resultados_listados.append(valor_text)

        
        valor = valores_tabla_interdicion(datos[1] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")
        
        resultados_listados.append(valor_text)
        
        valor = valores_tabla_interdicion(datos[3] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")
        
        resultados_listados.append(valor_text)
        
        valor = valores_tabla_interdicion(datos[7] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        
        resultados_listados.append(valor_text)
         
        valor = valores_tabla_interdicion(datos[8] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        
        resultados_listados.append(valor_text)
                  
        valor = valores_tabla_interdicion(datos[9] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        
        resultados_listados.append(valor_text)
                                   
        valor = valores_tabla_interdicion(datos[10] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        
        resultados_listados.append(valor_text)

       

        # pdf.ln(-100)
        # DATO = [datos[7], datos[8]]
        # valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios HCL", 5965 )


        # pdf.ln(50)
        # DATO = [datos[8], datos[7]]
        # valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios PBC", 5965 )


        
        # valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 27,  "SI") #funcion para filtar el spoa
        # dato=[datos[9], valor_9[0]]
        # pdf.ln(45)
        # valores_tabla_interdicion_semilleros(pdf, 255, dato, "Semilleros")

            
        ruta = self.filtro[15] 
        json_ruta = '{}static/metas docna.json'.format(ruta)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
        cocaina_ejc = 0
        marihuana_ejc = 0
        pbc_ejc = 0
        lab_chl_ejc = 0
        lab_pbc_ejc = 0

            
            
        for x in data:
                for y in data[x]:
                    if y["UNIDAD"] == "EJC":
                        cocaina_ejc = y["COCAINA"]
                        marihuana_ejc = y["MARIHUANA"]
                        pbc_ejc = y["PBC"]
                        lab_chl_ejc = y["LAB COCAINA"]
                        lab_pbc_ejc = y["LAB PBC"]
        # ruta = self.filtro[15]
        # pdf.ln(15)
        # encabezado_interdicion(pdf, ruta, 245, 241, 170,"escudo_ejc","EJÉRCITO NACIONAL", anio)
        self.meta =cocaina_ejc 
    #--------------------------------------------------------------------------
    #----------------------INICIO CODIGO RESULTADOS DEL EJC  ------------------
    #--------------------------------------------------------------------------
        resultados_lista_meta= [["EJÉRCITO NACIONAL", "META", self.anio, "%"]]
        color =[]
        res = calculo_de_interdion_solo("Clorhidrato de Cocaína", cocaina_ejc ,datos_anterior[0],  "EJÉRCITO NACIONAL")
        resultados_lista_meta.append(res[0])
        color.append(res[1])

        res = calculo_de_interdion_solo("Marihuana", marihuana_ejc ,datos_anterior[3],  "EJÉRCITO NACIONAL")
        resultados_lista_meta.append(res[0])
        color.append(res[1])
        res = calculo_de_interdion_solo("Pasta Base de Coca", pbc_ejc ,datos_anterior[1],  "EJÉRCITO NACIONAL")
        resultados_lista_meta.append(res[0])
        color.append(res[1])
        res = calculo_de_interdion_solo("Laboratorios (HCL)", lab_chl_ejc ,datos_anterior[7],  "EJÉRCITO NACIONAL")
        resultados_lista_meta.append(res[0])
        color.append(res[1])
        res = calculo_de_interdion_solo("Laboratorios (PBC)", lab_pbc_ejc ,datos_anterior[8],  "EJÉRCITO NACIONAL")
        resultados_lista_meta.append(res[0])
        color.append(res[1])
        

    #--------------------------------------------------------------------------
    #------------------------INICIO DEL CODIGO DEL MAPA -- --------------------
    #--------------------------------------------------------------------------



        # print("4")
        mapa_narcotrafico(datos, self.filtro)
        # print("5")




        return [resultados_listados, resultados_lista_meta, color]


    # resultados por enemigo 
    def resultados_narcotrafico_boletin_metas(self):

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

                
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos_anterior = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        # datos_anterior = [self.res_calculo_anterior[21],self.res_calculo_anterior[23],self.res_calculo_anterior[29],self.res_calculo_anterior[22],self.res_calculo_anterior[47],self.res_calculo_anterior[48], self.res_calculo_anterior[28], self.res_calculo_anterior[24], self.res_calculo_anterior[25], self.res_calculo_anterior[26], self.res_calculo_anterior[65], self.res_calculo_anterior[66], self.res_calculo_anterior[67], self.res_calculo_anterior[68]]
        
            
        ruta = self.filtro[15] 
        json_ruta = '{}static/metas docna.json'.format(ruta)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
        # Unidades y tipos de sustancia
        unidades = [
            "EJC", "DAVAA",
            "DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "FUTOM"
        ]

        tipos = {
            "Clorhidrato de Cocaína": "COCAINA",
            "Pasta Base de Coca": "PBC",
            "Marihuana": "MARIHUANA",
            "Laboratorios (HCL)": "LAB COCAINA",
            "Laboratorios (PBC)": "LAB PBC"
        }

        # Inicializar diccionario dinámico para resultados
        valores_por_unidad = {
            unidad: {clave: 0 for clave in tipos.values()}
            for unidad in unidades
        }

        # Rellenar desde data
        for x in data:
            for y in data[x]:
                unidad = y["UNIDAD"]
                if unidad in valores_por_unidad:
                    for clave in tipos.values():
                        valores_por_unidad[unidad][clave] = y.get(clave, 0)

        # Ahora genera resultados_meta y color
        resultados_meta = []
        color = []

        # Índices de referencia en los datos (mantienes tu lógica)
        indices = {
            "Clorhidrato de Cocaína": 0,
            "Pasta Base de Coca": 1,
            "Marihuana": 3,
            "Laboratorios (HCL)": 7,
            "Laboratorios (PBC)": 8
        }

        for unidad in unidades:
            nombre_visible = "EJÉRCITO NACIONAL" if unidad == "EJC" else unidad  # Alias visual
            resultados_meta.append([nombre_visible, f"META {self.anio}", f"META {self.mes_l}", "AVANCE"  , "%"])
            for nombre_largo, clave_data in tipos.items():
                idx = indices[nombre_largo]
                valor = valores_por_unidad[unidad][clave_data]
                res = calculo_de_interdion_mes(nombre_largo, valor, datos[idx], datos_anterior[idx], nombre_visible,self.mes_n)
                resultados_meta.append(res[0])
                color.append(res[1])

        return [resultados_meta, color]

    #--------------------------------------------------------------------------
    #------------------------FIN DEL CODIGO DEL MAPA --------------------------
    #--------------------------------------------------------------------------
    def cocaina_en_proceso(self):
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "NO") #funcion para filtar el spoa
        valor_0 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_anterior = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_anterior_anio, 47,  "NO") #funcion para filtar el spoa
        cocaina = 0
        total_anterior = comparativo_metas_valores(valor_anterior[0], 18)
        total = comparativo_metas_valores(valor[0], 18)
        porcentaje = 0 if total_anterior == 0 else formato_numero((total* 100)/total_anterior)
        datos= [str(formato_numero(total_anterior))+" Gal", str(formato_numero(total_anterior*0.876))+" Kg",str(formato_numero(total))+" Gal", str(formato_numero(total*0.876))+" Kg", str(formato_numero(total-total_anterior))+" Gal", str(formato_numero((total *0.876)-(total_anterior*0.876)))+" Kg", str(porcentaje)+" %"]
        unidades = [
            
            "DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "DAVAA", "FUTOM"
        ]
        resultados_data =[]
        for x in unidades:
        
            resultados = calculo_sin_formato(valor[0], x, 1, 18)
            resultados_data.append(str(formato_numero(resultados))+" Gal")
            resultados_data.append(str(formato_numero(resultados*0.876))+" Kg")

        resultados_data.append(str(formato_numero(total))+" Gal")
        resultados_data.append(str(formato_numero(total*0.876))+" Kg")
        data_total =[]


        cocaina = comparativo_metas_valores(valor_0[0], 18)

        # 1. Cocaina Kg
        data_total.append(f"{formato_numero(cocaina)} Kg")

        # 2. Cocaina %
        porcentaje = (cocaina * 100 / self.meta) if self.meta != 0 else 0
        data_total.append(f"{formato_numero(porcentaje)} %")

        # 3. Total ajustado Kg
        total_ajustado = (total * 0.876) + cocaina
        data_total.append(f"{formato_numero(total_ajustado)} Kg")

        # 4. Total ajustado %
        if self.meta != 0:
            porcentaje_ajustado = (total_ajustado * 100) / self.meta
        else:
            porcentaje_ajustado = 0   # o "N/A"

        data_total.append(f"{formato_numero(porcentaje_ajustado)} %")

        data_total.append(f"{formato_numero(self.meta)} Kg")

        return [datos, resultados_data, data_total]