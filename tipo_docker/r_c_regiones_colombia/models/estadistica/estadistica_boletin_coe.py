# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.r_c_regiones_colombia.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.r_c_regiones_colombia.models.funtions.componest.tablas import *
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


    def calculo_boletin_regiones(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):

       
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

        # print(filtros)

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)

        resultados = conexion_pos.comando_query(query[0])
        hechos = conexion_pos.comando_query(query[1])
        erradicacion = conexion_pos.comando_query(query[2])
        # print(query[2])

        #estadistica
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        pdf.cell(-5)
        fill = True
        #cabecera tabla
        encabezado_coe_regiones(pdf, fill)

        #separador
        separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA AMENAZA")
        #tabla de resultados

        tabla_boletin_coe_regiones(pdf, res_calculo[0], "MENORES RECUPERADOS", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[1], "PRESENTACIÓN VOLUNTARIA", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[2], "SOMETIMIENTOS", 5, 18)

        if filtro[17] == "sin_delco":
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 61,  "SI") #funcion para filtar el spoa
        else:
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "CAPTURAS", 5, 18)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 4,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "MDOM", 5, 18)

        separador_cuadro_coe(pdf, fill, "AFECTACIÓN A PROPIAS TROPAS")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "ASESINADOS", 5, 18)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 6,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "HERIDOS", 5, 18)

        separador_cuadro_coe(pdf, fill, "MATERIAL DE GUERRA")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "ARMAS DE LARGO ALCANCE", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "ARMAS DE CORTO ALCANCE", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "ARMAS DE ACOMPAÑAMIENTO", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "MUNICIONES", 5, 18)

        separador_cuadro_coe(pdf, fill, "COMBATES")
        tabla_boletin_coe_regiones(pdf, res_calculo[11], "COMBATES POSITIVOS", 6, 14)
        tabla_boletin_coe_regiones(pdf, res_calculo[12], "COMBATES NEGATIVOS", 6, 14)
        tabla_boletin_coe_regiones(pdf, res_calculo[13], "COMBATES SIN RESULTADOS", 6, 14)
        tabla_boletin_coe_regiones(pdf, res_calculo[14], "TOTAL DE COMBATES", 6, 14)
        

        separador_cuadro_coe(pdf, fill, "MATERIAL DE EXPLOSIVOS")
        tabla_boletin_coe_regiones(pdf, res_calculo[15], "NEUTRALIZACIÓN TERRORISTA", 6, 14)
        tabla_boletin_coe_regiones(pdf, res_calculo[16], "A.E", 5 ,18)
        tabla_boletin_coe_regiones(pdf, res_calculo[17], "MAP(Mina Anti Persona)", 5 ,18)
        tabla_boletin_coe_regiones(pdf, res_calculo[18], "EXPLOSIVOS kg", 5 ,18)
        tabla_boletin_coe_regiones(pdf, res_calculo[19], "CORDÓN DETONANTE m", 5 ,18)
        tabla_boletin_coe_regiones(pdf, res_calculo[20], "MECHA LENTA m", 5 ,18)

        separador_cuadro_coe(pdf, fill, "NARCOTRÁFICO")
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "COCAÍNA Kg", 5, 18)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "MARIHUANA Kg ", 5, 18)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "PBC Kg ", 5, 18)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "LAB. CLORHIDRATO DE COCAINA", 5, 18)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "LAB. PASTA O BASE DE COCA", 5, 18)
        
        pdf.ln()
        
        pdf.cell(-5)
        fill = True
        #cabecera tabla
        encabezado_coe_regiones(pdf, fill)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "SEMILLEROS", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "MATA(S) DE COCA EN SEMILLERO", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "INSUMOS LIQUIDOS Gal", 5, 18)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "INSUMOS SOLIDOS Kg ", 5, 18)

        separador_cuadro_coe(pdf, fill, "PLAN AMAZONÍA")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "CAPTURAS PLAN AMAZONIA ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[31], "PLANTULAS SEMBRADAS ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[32], "MADERA INCAUTADA ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[63], "ANIMALES INCAUTADOS ", 5, 18)

        separador_cuadro_coe(pdf, fill, "MINERÍA ILEGAL")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe_regiones(pdf, valor[0], "CAPTURAS MINERIA ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[34], "MENORES R. MINERIA ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[35], "EIYM", 6, 14)
        tabla_boletin_coe_regiones(pdf, res_calculo[36], "EXCAVADORA(S) ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[37], "RETROEXCAVADORA(S)  ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[38], "MAQUINARIA PESADA ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[39], "BULDOCER(ES)  ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[40], "UPM ILEGAL ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[41], "DRAGA(S)", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[65], "COLTAN Kg", 5, 18)

        separador_cuadro_coe(pdf, fill, "ECONOMÍAS ILÍCITAS")
        tabla_boletin_coe_regiones(pdf, res_calculo[42], "LIBERADOS ", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[43], "RESCATADOS", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[44], "VÁLVULAS", 5, 18)
        tabla_boletin_coe_regiones(pdf, res_calculo[45], "REFINERIAS ", 5, 18)

        separador_cuadro_coe(pdf, fill, "DEPÓSITOS")
        tabla_boletin_coe_regiones(pdf, res_calculo[46], "DEPÓSITO ILEGAL ", 5, 18)


