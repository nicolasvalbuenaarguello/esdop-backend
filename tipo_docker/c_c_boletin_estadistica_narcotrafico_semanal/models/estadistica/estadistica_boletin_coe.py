# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from flask import json
from tipo_docker.c_c_boletin_estadistica_narcotrafico_semanal.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_semanal.models.funtions.componest.tablas import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_semanal.maps.funciones.mapa_filtro import *
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


        resultados_anterior = conexion_pos.comando_query(query_2[0]) #resultados de la base de datos
        hechos_anterior = conexion_pos.comando_query(query_2[1]) #resultados de la base de datos

        res_calculo = estadistica_resultados(resultados, hechos, filtro)
        res_calculo_anterior = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)

        #encabezado de interdicion
        
        pdf.ln()

        datos = [res_calculo[21],res_calculo[23],res_calculo[29],res_calculo[22],res_calculo[47],res_calculo[48], res_calculo[28], res_calculo[24], res_calculo[25], res_calculo[26], res_calculo[65], res_calculo[66], res_calculo[67], res_calculo[68]]

        
        datos_anterior = [res_calculo_anterior[21],res_calculo_anterior[23],res_calculo_anterior[29],res_calculo_anterior[22],res_calculo_anterior[47],res_calculo_anterior[48], res_calculo_anterior[28], res_calculo_anterior[24], res_calculo_anterior[25], res_calculo_anterior[26], res_calculo_anterior[65], res_calculo_anterior[66], res_calculo_anterior[67], res_calculo_anterior[68]]
        
            
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
                    if y["UNIDAD"] == "FUTCO":
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_ejc ,datos[7], datos_anterior[7], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_ejc ,datos[8], datos_anterior[8], cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_davaa ,datos[7], datos_anterior[7], cel,"DAVAA", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_davaa ,datos[8], datos_anterior[8], cel,"DAVAA", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div01 ,datos[7],  datos_anterior[7], cel,"DIV01", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div01 ,datos[8],  datos_anterior[8], cel,"DIV01", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div02 ,datos[7], datos_anterior[7], cel,"DIV02", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div02 ,datos[8], datos_anterior[8], cel,"DIV02", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div03 ,datos[7],  datos_anterior[7], cel,"DIV03", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div03 ,datos[8],  datos_anterior[8], cel,"DIV03", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div04 ,datos[7],  datos_anterior[7], cel,"DIV04", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div04 ,datos[8],  datos_anterior[8], cel,"DIV04", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div05 ,datos[7],  datos_anterior[7], cel,"DIV05", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div05 ,datos[8],  datos_anterior[8], cel,"DIV05", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div06 ,datos[7],  datos_anterior[7], cel,"DIV06", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div06 ,datos[8],  datos_anterior[8], cel,"DIV06", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div07 ,datos[7],  datos_anterior[7],  cel,"DIV07", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div07 ,datos[8],  datos_anterior[8],  cel,"DIV07", ruta, altura, pos)
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
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_div08 ,datos[7],  datos_anterior[7],  cel,"DIV08", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_div08 ,datos[8],  datos_anterior[8],  cel,"DIV08", ruta, altura, pos)
        pdf.ln(-31)


        encabezado_interdicion(pdf, ruta, 125, 121.5, 164,"escudo_ftcec","FUTCO", anio)

        pdf.ln()
        pos = 169.3
        numero = 5
        altura =211.5
        cel = 125

        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", cocaina_futco ,datos[0], datos_anterior[0], cel,"FUTCO", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Marihuana", marihuana_futco ,datos[3], datos_anterior[3], cel,"FUTCO", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Pasta Base de Coca", pbc_futco ,datos[1], datos_anterior[1], cel,"FUTCO", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (CLHC)", lab_chl_futco ,datos[7], datos_anterior[7], cel,"FUTCO", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion(pdf,"Laboratorios (PBC))", lab_pbc_futco ,datos[8], datos_anterior[8], cel,"FUTCO", ruta, altura, pos)
    

    #-------------------------------------------------------------// ------------------------------------------------------

        # datos_2 = [res_calculo[42],res_calculo[43],res_calculo[44],res_calculo[45]]

    
    
        # #Liberados
        # numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[42], division, "", 1, 18, "Liberados", numero)
        # #Rescatados
        # numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[43], division, "", 1, 18, "Rescatados", numero)
        # #Válvulas Ilícitas Destruidas
        # numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[44], division, "", 1, 18, "Válvulas Ilícitas Destruidas", numero)
        # #Refinerias Ilegales Destruidas
        # numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[45], division, "", 1, 18, "Refinerias Ilegales Destruidas", numero)


        # calculo_de_interdion(pdf,"Clorhidrato de Cocaína", datos[0], 0, "Toneladas")
        
        # pdf.ln()
        # calculo_de_interdion(pdf,"Pasta Base de Coca", datos[1], 0, "Toneladas")

        # pdf.ln()
        # calculo_de_interdion(pdf,"Heroína", datos[11], 0, "Kilos")

        # pdf.ln()
        # calculo_de_interdion(pdf,"Basuco", datos[10], 0, "Kilos")
    
        # pdf.ln()
        # calculo_de_interdion(pdf,"Drogas Sinteticas", datos[12], 0, "Unidades")

        # pdf.ln()
        # calculo_de_interdion(pdf,"Insumos Sólidos ", datos[2], 0, "Toneladas")
        
        # pdf.ln()
        # calculo_de_interdion(pdf,"Marihuana", datos[3], 0, "Toneladas")
            
        # pdf.ln()
        # calculo_de_interdion(pdf,"CLHC en proceso", datos[4], 0, "Galones")
                
        # pdf.ln()
        # calculo_de_interdion(pdf,"PBC en proceso ", datos[5], 0, "Galones")
                    
        # pdf.ln()
        # calculo_de_interdion(pdf,"Insumos Líquidos  ", datos[6], 0, "Galones")
                
        # pdf.ln()
        # calculo_de_interdion(pdf,"Laboratorios CLHC ", datos[7], 0, "Unidades")
                    
        # pdf.ln()
        # calculo_de_interdion(pdf,"Laboratorios PBC", datos[8], 0, "Unidades")

                        
        # pdf.ln()
        # calculo_de_interdion(pdf,"Laboratorios Heroína", datos[13], 0, "Unidades")
                        
        # pdf.ln()
        # calculo_de_interdion(pdf,"Semilleros", datos[9], 0, "Unidades")

        # mapa_narcotrafico(datos, filtro)

        # ruta = filtro[15]
        # convecion_narcotrafico = '{}static/img/img_mapas/convecion_narcotrafico.jpg'.format(ruta)
        # mapa_narcotraficos = '{}static/img/img_mapas/mapa_narcotrafico.png'.format(ruta)
        # rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)

        # # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        # pdf.image(convecion_narcotrafico,5, 175, 51, 32)
        # pdf.image(mapa_narcotraficos,25,12,170,210)
        # pdf.image(rosa_nautica,5, 40, 30, 30)
        

    # resultados por enemigo 
    def resultados_narcotrafico_valores(self, fecha_inicial_u_l, fecha_final_u_l, fecha_dia_anterior, filtro, pdf, anio):
        
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

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos
        erradicacion = conexion_pos.comando_query(query[2]) #resultados de la base de datos
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        #encabezado de interdicion
        query_2 = parametros(fecha_dia_anterior, fecha_final_u_l, filtros, filtro) #querys modificados
        hechos_anterior = conexion_pos.comando_query(query_2[1]) #resultados de la base de datos
        resultados_anterior = conexion_pos.comando_query(query_2[0]) #resultados de la base de datos
        res_calculo_anterior = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)



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
        
            
        ruta = filtro[15] 

        valores_interdicion(pdf, ruta)
        pdf.ln(15)
        valores_tabla_interdicion(pdf, 30, datos[0], "Clorhidrato de Cocaína", 1375 )

        pdf.ln(50)
        valores_tabla_interdicion(pdf, 30, datos[1], "Pasta Base de Coca ", 1375 )
        
        pdf.ln(50)
        valores_tabla_interdicion_marihuna(pdf, 30, datos[3], "Marihuana", 96 )

            
        pdf.ln(-100)
        DATO = [datos[7], datos[8]]
        valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios CLHC", 5965 )


        pdf.ln(50)
        DATO = [datos[8], datos[7]]
        valores_tabla_interdicion_2(pdf, 255, DATO, "Laboratorios PBC", 5965 )


        
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        dato=[datos[9], valor_9[0]]
        pdf.ln(45)
        valores_tabla_interdicion_semilleros(pdf, 255, dato, "Semilleros")

            
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
                    if y["UNIDAD"] == "FUTCO":
                        cocaina_futco = y["COCAINA"]
                        marihuana_futco = y["MARIHUANA"]
                        pbc_futco = y["PBC"]
                        lab_chl_futco = y["LAB COCAINA"]
                        lab_pbc_futco = y["LAB PBC"]
                        
                    # if y['AGR_DIV'] == filtro[0]:
            
        ruta = filtro[15]
        pdf.ln(15)
        encabezado_interdicion(pdf, ruta, 245, 241, 170,"escudo_ejc","EJÉRCITO NACIONAL", anio)

        pdf.ln()
        pos = 176.3
        numero = 5
        altura =332
        cel = 245

        


        calculo_de_interdion_solo(pdf,"Clorhidrato de Cocaína", cocaina_ejc ,datos_anterior[0],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Marihuana", marihuana_ejc ,datos_anterior[3],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Pasta Base de Coca", pbc_ejc ,datos_anterior[1],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Laboratorios (CLHC)", lab_chl_ejc ,datos_anterior[7],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
        pdf.ln()
        pos = pos +numero
        calculo_de_interdion_solo(pdf,"Laboratorios (PBC))", lab_pbc_ejc ,datos_anterior[8],  cel,"EJÉRCITO NACIONAL", ruta, altura, pos)
    
    


        ejc = '{}static/img/escudos/cir_cocaina_new.png'.format(ruta)
        pdf.image(ejc,52,171.5,4,4)
        ejc = '{}static/img/escudos/cir_pbc_new.png'.format(ruta)
        pdf.image(ejc,52,176.5,4,4)
        ejc = '{}static/img/escudos/cir_marihuana_new.png'.format(ruta)
        pdf.image(ejc,52,181.5,4,4)
        ejc = '{}static/img/escudos/cir_lab_cocaina_new.png'.format(ruta)
        pdf.image(ejc,52,186.5,4,4)
        ejc = '{}static/img/escudos/cir_lab_pbc_new.png'.format(ruta)
        pdf.image(ejc,52,191.5,4,4)
        ejc = '{}static/img/escudos/cir_semilleros_new.png'.format(ruta)
        pdf.image(ejc,52,196.5,4,4)

        pdf.set_fill_color(193, 30, 38)
        # pdf.rounded_rect(50, 165, 70, 38, 1,'D', '1234')
        # pdf.set_text_color(0,0,0)
        pdf.set_text_color(128,0,0)
        pdf.set_font('BebasNeue', '', 14)
        pdf.text(52,170,"CONVENCIONES")
        pdf.set_font('BebasNeue', '', 12)
        pdf.set_text_color(50,50,50)
        texto = "cocaína incautada"
        pdf.text(57,175,texto)
        texto = "pbc incautada"
        pdf.text(57,180,texto)
        texto = "marihuana incautada"
        pdf.text(57,185,texto)
        texto = "laboratorios clhc"
        pdf.text(57,190,texto)
        texto = "laboratorios pbc"
        pdf.text(57,195,texto)
        texto = "semilleros"
        pdf.text(57,200,texto)
        # pdf.text(70,37,fecha_titulo_dos)


        mapa_narcotrafico(datos, filtro)

        ruta = filtro[15]
        # convecion_narcotrafico = '{}static/img/img_mapas/CONVENCIONES_VALORES_N.png'.format(ruta)
        mapa_narcotraficos = '{}static/img/img_mapas/mapa_narcotrafico.png'.format(ruta)
        rosa_nautica = '{}static/img/img_mapas/rosa_de_vientos_n.png'.format(ruta)

        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        # pdf.image(convecion_narcotrafico,150, 160, 50, 25)
        pdf.image(mapa_narcotraficos,104.7,25,140.2,174.8)
        pdf.image(rosa_nautica,200, 70, 17, 17)

