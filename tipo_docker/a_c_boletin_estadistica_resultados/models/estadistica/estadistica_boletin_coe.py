# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.a_c_boletin_estadistica_resultados.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.a_c_boletin_estadistica_resultados.models.funtions.componest.tablas import *
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



    def resultados_resultados_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):
        
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

        cabecera_tabla_dinamica(pdf, "RESULTADOS", 5, 5)
        pdf.ln()
        # resultados_tabla_dinamica(pdf, datos_res_act, text, suma, unidad, cell)
        separador_boletin_tabla_resultados(pdf, 5, "NARCOTRÁFICO")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "COCAÍNA Kg", 18, "Toneladas", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "MARIHUANA Kg ", 18, "Toneladas", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "PBC Kg ", 18, "Toneladas", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "LAB. CLORHIDRATO DE COCAINA", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "LAB. PASTA O BASE DE COCA", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "SEMILLEROS", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "MATA(S) DE COCA EN SEMILLERO", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "INSUMOS LIQUIDOS Gal", 18, "Galones", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "INSUMOS SOLIDOS Kg ", 18, "Toneladas", 5)

        separador_boletin_tabla_resultados(pdf, 5, "AFECTACIÓN A LA AMENAZA")
        resultados_tabla_dinamica(pdf, res_calculo[0], "MENORES RECUPERADOS", 18, "Personas",5)
        resultados_tabla_dinamica(pdf, res_calculo[1], "PRESENTACIÓN VOLUNTARIA", 18, "Personas",5)
        resultados_tabla_dinamica(pdf, res_calculo[2], "SOMETIMIENTOS", 18, "Personas",5)

        
        # print(filtro[17])
        if filtro[17] == "sin_delco":

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 61,  "SI") #funcion para filtar el spoa
        else:
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa

        resultados_tabla_dinamica(pdf, valor[0], "CAPTURAS", 18, "Personas",5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 4,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "MDOM", 18, "Personas",5)

        separador_boletin_tabla_resultados(pdf, 5, "AFECTACIÓN A PROPIAS TROPAS")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "ASESINADOS", 18, "Personas",5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "HERIDOS", 18, "Personas",5)

        separador_boletin_tabla_resultados(pdf, 5, "MATERIAL DE GUERRA")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "ARMAS DE LARGO ALCANCE", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "ARMAS DE CORTO ALCANCE", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "ARMAS DE ACOMPAÑAMIENTO", 18, "Unidades", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "MUNICIONES", 18, "Unidades", 5)


        separador_boletin_tabla_resultados(pdf, 5, "MATERIAL DE EXPLOSIVOS")
        resultados_tabla_dinamica(pdf, res_calculo[15], "NEUTRALIZACIÓN TERRORISTA",14, "Unidades",5)
        resultados_tabla_dinamica(pdf, res_calculo[16], "A.E",18, "Unidades",5)
        resultados_tabla_dinamica(pdf, res_calculo[17], "MAP(Mina Anti Persona)",18, "Unidades",5)
        resultados_tabla_dinamica(pdf, res_calculo[18], "EXPLOSIVOS kg",18, "Toneladas",5)

        pdf.ln(-165)
        cabecera_tabla_dinamica(pdf, "RESULTADOS", 5, 166)
        pdf.ln()

        separador_boletin_tabla_resultados(pdf, 166, "PLAN AMAZONÍA")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "CAPTURAS PLAN AMAZONIA ", 18, "Personas", 166)
        resultados_tabla_dinamica(pdf, res_calculo[31], "PLANTULAS SEMBRADAS ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[32], "MADERA INCAUTADA ", 18, "Metros Cub.", 166)
        resultados_tabla_dinamica(pdf, res_calculo[63], "ANIMALES INCAUTADOS ", 18, "unidades", 166)

        separador_boletin_tabla_resultados(pdf, 166, "MINERÍA ILEGAL")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        resultados_tabla_dinamica(pdf, valor[0], "CAPTURAS MINERIA ", 18, "Personas", 166)
        resultados_tabla_dinamica(pdf, res_calculo[35], "EIYM", 14, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[36], "EXCAVADORA(S) ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[37], "RETROEXCAVADORA(S)  ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[38], "MAQUINARIA PESADA ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[39], "BULDOCER(ES)  ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[40], "UPM ILEGAL ", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[41], "DRAGA(S)", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[65], "COLTAN", 18, "Toneladas", 166)

        separador_boletin_tabla_resultados(pdf, 166, "ECONOMÍAS ILÍCITAS")
        resultados_tabla_dinamica(pdf, res_calculo[42], "LIBERADOS ", 18, "Personas", 166)
        resultados_tabla_dinamica(pdf, res_calculo[43], "RESCATADOS", 18, "Personas", 166)
        resultados_tabla_dinamica(pdf, res_calculo[44], "VÁLVULAS", 18, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[45], "REFINERIAS ", 18, "Unidades", 166)

        separador_boletin_tabla_resultados(pdf, 166, "COMBATES")
        resultados_tabla_dinamica(pdf, res_calculo[11], "COMBATES POSITIVOS", 14, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[12], "COMBATES NEGATIVOS", 14, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[13], "COMBATES SIN RESULTADOS", 14, "Unidades", 166)
        resultados_tabla_dinamica(pdf, res_calculo[14], "TOTAL DE COMBATES", 14, "Unidades", 166)

        separador_boletin_tabla_resultados(pdf, 166, "DEPÓSITOS")
        resultados_tabla_dinamica(pdf, res_calculo[46], "DEPÓSITO ILEGAL ", 18, "Unidades", 166)


