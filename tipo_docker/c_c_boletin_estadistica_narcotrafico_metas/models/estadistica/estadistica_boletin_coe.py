# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from flask import json
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.models.funtions.componest.tablas import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            self.archivo = "RESULTADO SIN SPOA" +".txt"              
            self.f = open("doc_sin_spoa/"+self.archivo, "w")
            self.f.write(str("RESULTADO")+", " + str("HR")+", " +str("FECHA")+", "+str("SPOA")+", "+str("DIV")+"\n")

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



    # resultados por enemigo 
    def resultados_narcotrafico_boletin(self, fecha_inicial_u_l, fecha_final_u_l,fecha_dia_anterior, filtro, pdf, anio):
        
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

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro) #querys modificados

        query_2 = parametros(fecha_inicial_u_l, fecha_dia_anterior, filtros, filtro) #querys modificados

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos

        # resultados_anterior = conexion_pos.comando_query(query_2[0]) #resultados de la base de datos
        # hechos_anterior = conexion_pos.comando_query(query_2[1]) #resultados de la base de datos

        res_calculo = estadistica_resultados(resultados, hechos, filtro)
        # res_calculo_anterior = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        # print("1-1")
        #encabezado de interdicion
        
        pdf.ln()

        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

                
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 69,  "SI") #funcion para filtar el spoa


        datos_anterior = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        # datos_anterior = [res_calculo_anterior[21],res_calculo_anterior[23],res_calculo_anterior[29],res_calculo_anterior[22],res_calculo_anterior[47],res_calculo_anterior[48], res_calculo_anterior[28], res_calculo_anterior[24], res_calculo_anterior[25], res_calculo_anterior[26], res_calculo_anterior[65], res_calculo_anterior[66], res_calculo_anterior[67], res_calculo_anterior[68]]
        
            
        ruta = filtro[15] 
        json_ruta = '{}static/metas docna.json'.format(ruta)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
        cocaina_ejc = 0
        marihuana_ejc = 0
        pbc_ejc = 0
        lab_chl_ejc = 0
        lab_pbc_ejc = 0

        cocaina_davaa = 0
        marihuana_davaa = 0
        pbc_davaa = 0
        lab_chl_davaa = 0
        lab_pbc_davaa = 0
        
        cocaina_div01 = 0
        marihuana_div01 = 0
        pbc_div01 = 0
        lab_chl_div01 = 0
        lab_pbc_div01 = 0
            
        cocaina_div02 = 0
        marihuana_div02 = 0
        pbc_div02 = 0
        lab_chl_div02 = 0
        lab_pbc_div02 = 0
                
        cocaina_div03 = 0
        marihuana_div03 = 0
        pbc_div03 = 0
        lab_chl_div03 = 0
        lab_pbc_div03 = 0
                    
        cocaina_div04 = 0
        marihuana_div04 = 0
        pbc_div04 = 0
        lab_chl_div04 = 0
        lab_pbc_div04 = 0

                
        cocaina_div05 = 0
        marihuana_div05 = 0
        pbc_div05 = 0
        lab_chl_div05 = 0
        lab_pbc_div05 = 0
        
        cocaina_div06 = 0
        marihuana_div06 = 0
        pbc_div06 = 0
        lab_chl_div06 = 0
        lab_pbc_div06 = 0
            
        cocaina_div07 = 0
        marihuana_div07 = 0
        pbc_div07 = 0
        lab_chl_div07 = 0
        lab_pbc_div07 = 0
            
        cocaina_div08 = 0
        marihuana_div08 = 0
        pbc_div08 = 0
        lab_chl_div08 = 0
        lab_pbc_div08 = 0
                
        cocaina_ftcec = 0
        marihuana_ftcec = 0
        pbc_ftcec = 0
        lab_chl_ftcec = 0
        lab_pbc_ftcec = 0
                
        cocaina_futco = 0
        marihuana_futco = 0
        pbc_futco = 0
        lab_chl_futco = 0
        lab_pbc_futco = 0


        for x in data:
                for y in data[x]:
                    if y["UNIDAD"] == "EJC":
                        cocaina_ejc = y["COCAINA"]
                        marihuana_ejc = y["MARIHUANA"]
                        pbc_ejc = y["PBC"]
                        lab_chl_ejc = y["LAB COCAINA"]
                        lab_pbc_ejc = y["LAB PBC"]
                    if y["UNIDAD"] == "DAVAA":
                        cocaina_davaa = y["COCAINA"]
                        marihuana_davaa = y["MARIHUANA"]
                        pbc_davaa = y["PBC"]
                        lab_chl_davaa = y["LAB COCAINA"]
                        lab_pbc_davaa = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV01":
                        cocaina_div01 = y["COCAINA"]
                        marihuana_div01 = y["MARIHUANA"]
                        pbc_div01 = y["PBC"]
                        lab_chl_div01 = y["LAB COCAINA"]
                        lab_pbc_div01 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV02":
                        cocaina_div02 = y["COCAINA"]
                        marihuana_div02 = y["MARIHUANA"]
                        pbc_div02 = y["PBC"]
                        lab_chl_div02 = y["LAB COCAINA"]
                        lab_pbc_div02 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV03":
                        cocaina_div03 = y["COCAINA"]
                        marihuana_div03 = y["MARIHUANA"]
                        pbc_div03 = y["PBC"]
                        lab_chl_div03 = y["LAB COCAINA"]
                        lab_pbc_div03 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV04":
                        cocaina_div04 = y["COCAINA"]
                        marihuana_div04 = y["MARIHUANA"]
                        pbc_div04 = y["PBC"]
                        lab_chl_div04 = y["LAB COCAINA"]
                        lab_pbc_div04 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV05":
                        cocaina_div05 = y["COCAINA"]
                        marihuana_div05 = y["MARIHUANA"]
                        pbc_div05 = y["PBC"]
                        lab_chl_div05 = y["LAB COCAINA"]
                        lab_pbc_div05 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV06":
                        cocaina_div06 = y["COCAINA"]
                        marihuana_div06 = y["MARIHUANA"]
                        pbc_div06 = y["PBC"]
                        lab_chl_div06 = y["LAB COCAINA"]
                        lab_pbc_div06 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV07":
                        cocaina_div07 = y["COCAINA"]
                        marihuana_div07 = y["MARIHUANA"]
                        pbc_div07 = y["PBC"]
                        lab_chl_div07 = y["LAB COCAINA"]
                        lab_pbc_div07 = y["LAB PBC"]
                    if y["UNIDAD"] == "DIV08":
                        cocaina_div08 = y["COCAINA"]
                        marihuana_div08 = y["MARIHUANA"]
                        pbc_div08 = y["PBC"]
                        lab_chl_div08 = y["LAB COCAINA"]
                        lab_pbc_div08 = y["LAB PBC"]
                    if y["UNIDAD"] == "FTCEC":
                        cocaina_ftcec = y["COCAINA"]
                        marihuana_ftcec = y["MARIHUANA"]
                        pbc_ftcec = y["PBC"]
                        lab_chl_ftcec = y["LAB COCAINA"]
                        lab_pbc_ftcec = y["LAB PBC"]
                    if y["UNIDAD"] == "FUTOM":
                        cocaina_futco = y["COCAINA"]
                        marihuana_futco = y["MARIHUANA"]
                        pbc_futco = y["PBC"]
                        lab_chl_futco = y["LAB COCAINA"]
                        lab_pbc_futco = y["LAB PBC"]
                        
                    # if y['AGR_DIV'] == filtro[0]:
            
        # capturas =[]
        # for dato_e in res_calculo[3]:
        #     if dato_e[7]!= "DELINCUENCIA":
        #         capturas.append(dato_e)    

        ruta = filtro[15]
        pdf.ln(-7)
        encabezado_interdicion(pdf, ruta, 6.5, 3, 41,"escudo_ejc","EJÉRCITO NACIONAL", anio)
        pdf.ln()
        pos = 46.3
        numero = 5
        altura =93
        cel = 6.5
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_ejc ,datos[0], datos_anterior[0], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_ejc ,datos[3], datos_anterior[3], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_ejc ,datos[1], datos_anterior[1], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_ejc ,datos[7], datos_anterior[7], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_ejc ,datos[8], datos_anterior[8], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln(-31)

        encabezado_interdicion(pdf, ruta, 125, 121.5, 41,"escudo_davaa","DAVAA", anio)

        pdf.ln()
        pos = 46.3
        numero = 5
        altura =211.5
        cel = 125
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_davaa ,datos[0], datos_anterior[0], cel,"DAVAA", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_davaa ,datos[3], datos_anterior[3], cel,"DAVAA", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_davaa ,datos[1], datos_anterior[1], cel,"DAVAA", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_davaa ,datos[7], datos_anterior[7], cel,"DAVAA", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_davaa ,datos[8], datos_anterior[8], cel,"DAVAA", ruta, altura, pos)
        pdf.ln(-31)

        encabezado_interdicion(pdf, ruta, 245, 241.5, 41,"escudo_div01","DIV01", anio)

        pdf.ln()
        pos = 46.3
        numero = 5
        altura =332
        cel = 245
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div01 ,datos[0],  datos_anterior[0], cel,"DIV01", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div01 ,datos[3],  datos_anterior[3], cel,"DIV01", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div01 ,datos[1],  datos_anterior[1], cel,"DIV01", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div01 ,datos[7],  datos_anterior[7], cel,"DIV01", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div01 ,datos[8],  datos_anterior[8], cel,"DIV01", ruta, altura, pos)
        pdf.ln(10)
        

        # #------------------------------------------------------------------

        encabezado_interdicion(pdf, ruta, 6.5, 3, 82,"escudo_div02","DIV02", anio)
        pdf.ln()
        pos = 87.3
        numero = 5
        altura =93
        cel = 6.5
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div02 ,datos[0], datos_anterior[0], cel,"DIV02", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div02 ,datos[3], datos_anterior[3], cel,"DIV02", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div02 ,datos[1], datos_anterior[1], cel,"DIV02", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div02 ,datos[7], datos_anterior[7], cel,"DIV02", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div02 ,datos[8], datos_anterior[8], cel,"DIV02", ruta, altura, pos)
        pdf.ln(-31)


        encabezado_interdicion(pdf, ruta, 125, 121.5, 82,"escudo_div03","DIV03", anio)

        pdf.ln()
        pos = 87.3
        numero = 5
        altura =211.5
        cel = 125
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div03 ,datos[0],  datos_anterior[0], cel,"DIV03", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div03 ,datos[3],  datos_anterior[3], cel,"DIV03", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div03 ,datos[1],  datos_anterior[1], cel,"DIV03", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div03 ,datos[7],  datos_anterior[7], cel,"DIV03", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div03 ,datos[8],  datos_anterior[8], cel,"DIV03", ruta, altura, pos)
        pdf.ln(-31)


        encabezado_interdicion(pdf, ruta, 245, 241.5, 82,"escudo_div04","DIV04", anio)

        pdf.ln()
        pos = 87.3
        numero = 5
        altura =332
        cel = 245
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div04 ,datos[0],  datos_anterior[0], cel,"DIV04", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div04 ,datos[3],  datos_anterior[3], cel,"DIV04", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div04 ,datos[1],  datos_anterior[1], cel,"DIV04", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div04 ,datos[7],  datos_anterior[7], cel,"DIV04", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div04 ,datos[8],  datos_anterior[8], cel,"DIV04", ruta, altura, pos)
        pdf.ln(10)


        #------------------------------------------------------------------

        encabezado_interdicion(pdf, ruta, 6.5, 3, 123,"escudo_div05","DIV05", anio)
        pdf.ln()
        pos = 128.3
        numero = 5
        altura =93
        cel = 6.5
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div05 ,datos[0],  datos_anterior[0], cel,"DIV05", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div05 ,datos[3],  datos_anterior[3], cel,"DIV05", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div05 ,datos[1],  datos_anterior[1], cel,"DIV05", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div05 ,datos[7],  datos_anterior[7], cel,"DIV05", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div05 ,datos[8],  datos_anterior[8], cel,"DIV05", ruta, altura, pos)
        pdf.ln(-31)


        encabezado_interdicion(pdf, ruta, 125, 121.5, 123,"escudo_div06","DIV06", anio)

        pdf.ln()
        pos = 128.3
        numero = 5
        altura =211.5
        cel = 125
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div06 ,datos[0],  datos_anterior[0], cel,"DIV06", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div06 ,datos[3],  datos_anterior[3], cel,"DIV06", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div06 ,datos[1],  datos_anterior[1], cel,"DIV06", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div06 ,datos[7],  datos_anterior[7], cel,"DIV06", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div06 ,datos[8],  datos_anterior[8], cel,"DIV06", ruta, altura, pos)
        pdf.ln(-31)



        encabezado_interdicion(pdf, ruta, 245, 241.5, 123,"escudo_div07","DIV07", anio)

        pdf.ln()
        pos = 128.3
        numero = 5
        altura =332
        cel = 245
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div07 ,datos[0],  datos_anterior[0],  cel,"DIV07", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div07 ,datos[3],  datos_anterior[3],  cel,"DIV07", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div07 ,datos[1],  datos_anterior[1],  cel,"DIV07", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div07 ,datos[7],  datos_anterior[7],  cel,"DIV07", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div07 ,datos[8],  datos_anterior[8],  cel,"DIV07", ruta, altura, pos)
        pdf.ln(10)


        #------------------------------------------------------------------

        encabezado_interdicion(pdf, ruta, 6.5, 3, 164,"escudo_div08","DIV08", anio)
        pdf.ln()
        pos = 169.3
        numero = 5
        altura =93
        cel = 6.5
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_div08 ,datos[0],  datos_anterior[0],  cel,"DIV08", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_div08 ,datos[3],  datos_anterior[3],  cel,"DIV08", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_div08 ,datos[1],   datos_anterior[1], cel,"DIV08", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_div08 ,datos[7],  datos_anterior[7],  cel,"DIV08", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_div08 ,datos[8],  datos_anterior[8],  cel,"DIV08", ruta, altura, pos)
        pdf.ln(-31)


        encabezado_interdicion(pdf, ruta, 125, 121.5, 164,"escudo_futco","FUTOM", anio)

        pdf.ln()
        pos = 169.3
        numero = 5
        altura =211.5
        cel = 125
 
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_futco ,datos[0], datos_anterior[0], cel,"FUTOM", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_futco ,datos[3], datos_anterior[3], cel,"FUTOM", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_futco ,datos[1], datos_anterior[1], cel,"FUTOM", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (HCL)", lab_chl_futco ,datos[7], datos_anterior[7], cel,"FUTOM", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC)", lab_pbc_futco ,datos[8], datos_anterior[8], cel,"FUTOM", ruta, altura, pos)
    
        # print("2-2")
    #-------------------------------------------------------------// ------------------------------------------------------

        

    # resultados por enemigo 
    def resultados_narcotrafico_valores(self, fecha_inicial_u_l, fecha_final_u_l, fecha_dia_anterior, filtro, pdf, anio):
        filtros = selecion_filtro(filtro) #parametros de filtros
        
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

        query = parametros(fecha_final_u_l, fecha_final_u_l, filtros, filtro) #querys modificados

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos
        erradicacion = conexion_pos.comando_query(query[2]) #resultados de la base de datos
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        #encabezado de interdicion
        query_2 = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro) #querys modificados
        hechos_anterior = conexion_pos.comando_query(query_2[1]) #resultados de la base de datos
        resultados_anterior = conexion_pos.comando_query(query_2[0]) #resultados de la base de datos
        res_calculo_anterior = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)

        # print("2-1")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 66,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 67,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 68,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_anterior, 69,  "SI") #funcion para filtar el spoa


        datos_anterior = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]
        

        pdf.ln()

        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "NO") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "NO") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "NO") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "NO") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "NO") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "NO") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "NO") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "NO") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "NO") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "NO") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "NO") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 67,  "NO") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 68,  "NO") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 69,  "NO") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]
        
            
        ruta = filtro[15] 
        
        valores_interdicion(pdf, ruta)
        valor = valores_tabla_interdicion(datos[0] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,42,"Clorhidrato de cocaína ")
        pdf.text(40,46.5,"(incautada)")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,54.2,valor_text)
        
        valor = valores_tabla_interdicion(datos[1] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,71,"Pasta base de coca")
        pdf.text(40,75.5,"(incautada)")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,83.2,valor_text)
        
        valor = valores_tabla_interdicion(datos[3] )
        valor = formato_numero_un_decimal(valor)
        valor_text = str(valor)+str(" KG")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,100,"Marihuana")
        pdf.text(40,104.5,"(incautada)")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,112.2,valor_text)
        
        valor = valores_tabla_interdicion(datos[7] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,129,"Laboratorios HCL")
        pdf.text(40,133.5,"(destruido)")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,141.2,valor_text)
         
        valor = valores_tabla_interdicion(datos[8] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,158,"Laboratorios PBC")
        pdf.text(40,162.5,"(destruido)")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,170.2,valor_text)

                  
        valor = valores_tabla_interdicion(datos[9] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,180,"Semilleros")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,187.5,valor_text)
                                   
        valor = valores_tabla_interdicion(datos[10] )
        valor = formato_numero(valor)
        valor_text = str(valor)+str(" UND")
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 12)
        pdf.text(40,195,"Matas de coca en semillero")
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(40,202.5, valor_text)

       

        # pdf.ln(-100)
        # DATO = [datos[7], datos[8]]
        # valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios HCL", 5965 )


        # pdf.ln(50)
        # DATO = [datos[8], datos[7]]
        # valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios PBC", 5965 )


        
        # valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        # dato=[datos[9], valor_9[0]]
        # pdf.ln(45)
        # valores_tabla_interdicion_semilleros(pdf, 255, dato, "Semilleros")

            
        ruta = filtro[15] 
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
        # ruta = filtro[15]
        # pdf.ln(15)
        # encabezado_interdicion(pdf, ruta, 245, 241, 170,"escudo_ejc","EJÉRCITO NACIONAL", anio)

    #--------------------------------------------------------------------------
    #----------------------INICIO CODIGO RESULTADOS DEL EJC  ------------------
    #--------------------------------------------------------------------------
        pdf.ln(126)
        pos = 162.5
        numero = 7
        altura =322
        cel = 235

        calculo_de_interdion_solo_encabezado(pdf,"EJÉRCITO NACIONAL", cel, altura, pos, anio)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Clorhidrato de Cocaína", cocaina_ejc ,datos_anterior[0],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos,1)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Marihuana", marihuana_ejc ,datos_anterior[3],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos,0)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Pasta Base de Coca", pbc_ejc ,datos_anterior[1],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos,1)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Laboratorios (HCL)", lab_chl_ejc ,datos_anterior[7],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos,0)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Laboratorios (PBC)", lab_pbc_ejc ,datos_anterior[8],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos,1)
        
    #--------------------------------------------------------------------------
    #----------------------FIN  CODIGO RESULTADOS DEL EJC  --------------------
    #--------------------------------------------------------------------------
    #----------------------INICIO CODIGO DE LAS CONVENCIONES ------------------
    #--------------------------------------------------------------------------
        pdf.set_fill_color(193, 30, 38)
        pdf.rounded_rect(305, 10, 40, 38, 1,'D', '1234')

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 14)
        pdf.text(307,15,"CONVENCIONES")

        pdf.set_font('BebasNeue', '', 12)
        pdf.set_text_color(50,50,50)

        ejc = '{}static/img/escudos/cir_cocaina_new.png'.format(ruta) #CONVENCION DE COCAINA
        pdf.image(ejc,307,16.5,4,4) #CONVENCION DE COCAINA
        texto = "cocaína incautada"  #CONVENCION DE COCAINA
        pdf.text(312,20,texto) #CONVENCION DE COCAINA  

        ejc = '{}static/img/escudos/cir_pbc_new.png'.format(ruta) #CONVENCION DE PBC
        pdf.image(ejc,307,21.5,4,4) #CONVENCION DE PBC
        texto = "pbc incautada" #CONVENCION DE PBC
        pdf.text(312,25,texto) #CONVENCION DE PBC

        ejc = '{}static/img/escudos/cir_marihuana_new.png'.format(ruta) #CONVENCIONES DE MARIHUANA
        pdf.image(ejc,307,26.5,4,4) #CONVENCIONES DE MARIHUANA
        texto = "marihuana incautada" #CONVENCIONES DE MARIHUANA
        pdf.text(312,30,texto) #CONVENCIONES DE MARIHUANA


        ejc = '{}static/img/escudos/cir_lab_cocaina_new.png'.format(ruta) #convenciones de lab de cocaina
        pdf.image(ejc,307,31.5,4,4) #convenciones de lab de cocaina
        texto = "laboratorios HCL" #convenciones de lab de cocaina
        pdf.text(312,35,texto) #convenciones de lab de cocaina

        ejc = '{}static/img/escudos/cir_lab_pbc_new.png'.format(ruta) #convenciones de lab pbc
        pdf.image(ejc,307,36.5,4,4) #convenciones de lab pbc
        texto = "laboratorios pbc" #convenciones de lab pbc
        pdf.text(312,40,texto) #convenciones de lab pbc

        ejc = '{}static/img/escudos/cir_semilleros_new.png'.format(ruta) #convenciones de semilleros
        pdf.image(ejc,307,41.5,4,4) #convenciones de semilleros
        texto = "semilleros" #convenciones de semilleros
        pdf.text(312,45,texto) #convenciones de semilleros


    #--------------------------------------------------------------------------
    #----------------------FIN  CODIGO DE LAS CONVENCIONES --------------------
    #--------------------------------------------------------------------------
    #------------------------INICIO DEL CODIGO DEL MAPA -- --------------------
    #--------------------------------------------------------------------------



        # print("4")
        mapa_narcotrafico(datos, filtro)
        # print("5")


        mapa_narcotraficos = '{}static/img/img_mapas/mapa_narcotrafico.png'.format(ruta)
        rosa_nautica = '{}static/img/img_mapas/rosa_de_vientos_n.png'.format(ruta)


        pdf.image(mapa_narcotraficos,100.5,-0.5,173.5,215)
        pdf.image(rosa_nautica,220, 65, 17, 17)

    #--------------------------------------------------------------------------
    #------------------------FIN DEL CODIGO DEL MAPA --------------------------
    #--------------------------------------------------------------------------
    #------------------------INICIO DEL CODIGO DEL DIV ------------------------
    #--------------------------------------------------------------------------

        div = '{}static/img/diviciones/div01_ayuda.png'.format(ruta)
        img_text = '{}static/img/diviciones/imagne_text_new.png'.format(ruta)
        pdf.image(img_text,116, 40.5, 35, 10)
        pdf.image(div,144, 40, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(126,40,"2,1%")
        pdf.set_text_color(0,0,0)
        pdf.text(124,46.5,"5.057 HA.")
        
        div = '{}static/img/diviciones/div02_ayuda.png'.format(ruta)
        pdf.image(img_text,100, 60.5, 35, 10)
        pdf.image(div,128, 60, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(110,60,"21,5%")
        pdf.set_text_color(0,0,0)
        pdf.text(108,66.5,"52,683 HA.")

        div = '{}static/img/diviciones/div03_ayuda.png'.format(ruta)
        pdf.image(img_text,92, 80.5, 35, 10)
        pdf.image(div,118, 80, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(102,80,"40.0%")
        pdf.set_text_color(0,0,0)
        pdf.text(98,86.5,"98,170HA.")


        div = '{}static/img/diviciones/div04_ayuda.png'.format(ruta)
        pdf.image(img_text,90, 100.5, 35, 10)
        pdf.image(div,116, 100, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(105,100,"4,1%")
        pdf.set_text_color(0,0,0)
        pdf.text(96,106.5,"10,293 HA.")

        
        div = '{}static/img/diviciones/div05_ayuda.png'.format(ruta)
        pdf.image(img_text,90, 120.5, 35, 10)
        pdf.image(div,116, 120, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        # pdf.text(137,120,"4,1%")
        # pdf.set_text_color(0,0,0)
        pdf.text(95,126.5,"HISTÓRICO.")

        div = '{}static/img/diviciones/div06_ayuda.png'.format(ruta)
        pdf.image(img_text,97, 140.5, 35, 10)
        pdf.image(div,123, 140, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(107,140,"23,7%")
        pdf.set_text_color(0,0,0)
        pdf.text(103,146.5,"58,480 HA.")
        
        div = '{}static/img/diviciones/div07_ayuda.png'.format(ruta)
        pdf.image(img_text,112, 160.5, 35, 10)
        pdf.image(div,136, 160, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        pdf.text(118,160,"8,1%")
        pdf.set_text_color(0,0,0)
        pdf.text(118,166.5,"21,179 HA.")
        
        div = '{}static/img/diviciones/div08_ayuda.png'.format(ruta)
        pdf.image(img_text,137, 180.5, 35, 10)
        pdf.image(div,163, 180, 10, 10)

        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 16)
        # pdf.text(177,180,"8,6%")
        # pdf.set_text_color(0,0,0)
        pdf.text(143,186.5,"HISTÓRICO.")