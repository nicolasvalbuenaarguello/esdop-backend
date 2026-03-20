# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.y_c_boletin_estadistica.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.y_c_boletin_estadistica.models.funtions.componest.tablas import *
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

    def calculo_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):

        dato = ""
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

        pdf.cell(-5)
        fill = True
        #cabecera tabla
        encabezado_coe(pdf, fill)
        res_calculo = estadistica_resultados(resultados, hechos, filtro)
        #separador
        separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA AMENAZA")
        #tabla de resultados
        #estadistica

        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 0,  "NO") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "MENORES RECUPERADOS")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 1,  "NO") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "PRESENTACIÓN VOLUNTARIA")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 2,  "NO") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "SOMETIMIENTOS")

        # print(filtro[17])
        if filtro[17] == "sin_delco":
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 61, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        else:
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 3, "CAPTURAS", "SI" ) #funcion para filtar el spoa

        # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor_calculado[0], "CAPTURAS")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 4,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "MDOM")

        #separador_cuadro_coe(pdf, fill, "AFECTACIÓN A PROPIAS TROPAS")

        #valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        #tabla_boletin_coe(pdf, valor[0], "ASESINADOS")

        #valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 6,  "SI") #funcion para filtar el spoa
        #tabla_boletin_coe(pdf, valor[0], "HERIDOS")



        separador_cuadro_coe(pdf, fill, "MATERIAL DE GUERRA")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "ARMAS DE LARGO ALCANCE")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "ARMAS DE CORTO ALCANCE")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "ARMAS DE ACOMPAÑAMIENTO")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "MUNICIONES")

        separador_cuadro_coe(pdf, fill, "COMBATES")
        tabla_boletin_coe_hechos(pdf, res_calculo[11], "COMBATES POSITIVOS")
        tabla_boletin_coe_hechos(pdf, res_calculo[12], "COMBATES NEGATIVOS")
        tabla_boletin_coe_hechos(pdf, res_calculo[13], "COMBATES SIN RESULTADOS")
        tabla_boletin_coe_hechos(pdf, res_calculo[14], "TOTAL DE COMBATES")

        separador_cuadro_coe(pdf, fill, "MATERIAL DE EXPLOSIVOS")
        tabla_boletin_coe_hechos(pdf, res_calculo[15], "NEUTRALIZACIÓN TERRORISTA")
        tabla_boletin_coe(pdf, res_calculo[16], "A.E")
        tabla_boletin_coe(pdf, res_calculo[17], "MAP(Mina Anti Persona)")
        tabla_boletin_coe(pdf, res_calculo[18], "EXPLOSIVOS kg")
        tabla_boletin_coe(pdf, res_calculo[19], "CORDÓN DETONANTE m")
        tabla_boletin_coe(pdf, res_calculo[20], "MECHA LENTA m")

        separador_cuadro_coe(pdf, fill, "NARCOTRÁFICO")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "COCAÍNA Kg")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "MARIHUANA Kg ")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "PBC Kg ")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "LAB. CLORHIDRATO DE COCAINA")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "LAB. PASTA O BASE DE COCA")

        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "SEMILLEROS")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "MATA(S) DE COCA EN SEMILLERO")

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "INSUMOS LIQUIDOS Gal")

        
        pdf.ln()
        
        pdf.cell(-5)
        fill = True
        #cabecera tabla
        encabezado_coe(pdf, fill)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "INSUMOS SOLIDOS Kg ")
        
        separador_cuadro_coe(pdf, fill, "LOE AMAZONÍA")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "CAPTURAS LOE AMAZONIA ")
        tabla_boletin_coe(pdf, res_calculo[31], "PLANTULAS SEMBRADAS ")
        tabla_boletin_coe(pdf, res_calculo[32], "MADERA INCAUTADA ")
        tabla_boletin_coe(pdf, res_calculo[63], "ANIMALES INCAUTADOS ")

        separador_cuadro_coe(pdf, fill, "MINERÍA ILEGAL")
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor[0], "CAPTURAS MINERIA ")
        tabla_boletin_coe(pdf, res_calculo[34], "MENORES R. MINERIA ")
        tabla_boletin_coe_hechos(pdf, res_calculo[35], "EIYM")
        tabla_boletin_coe(pdf, res_calculo[36], "EXCAVADORA(S) ")
        tabla_boletin_coe(pdf, res_calculo[37], "RETROEXCAVADORA(S)  ")
        tabla_boletin_coe(pdf, res_calculo[38], "MAQUINARIA PESADA ")
        tabla_boletin_coe(pdf, res_calculo[39], "BULDOCER(ES)  ")
        tabla_boletin_coe(pdf, res_calculo[40], "UPM ILEGAL ")
        tabla_boletin_coe(pdf, res_calculo[41], "DRAGA(S)")
        tabla_boletin_coe(pdf, res_calculo[65], "COLTAN KG")

        separador_cuadro_coe(pdf, fill, "ECONOMÍAS ILÍCITAS")
        tabla_boletin_coe(pdf, res_calculo[42], "LIBERADOS ")
        tabla_boletin_coe(pdf, res_calculo[43], "RESCATADOS")
        tabla_boletin_coe(pdf, res_calculo[44], "VÁLVULAS")
        tabla_boletin_coe(pdf, res_calculo[45], "REFINERIAS ")

        separador_cuadro_coe(pdf, fill, "DEPÓSITOS")
        tabla_boletin_coe(pdf, res_calculo[46], "DEPÓSITO ILEGAL ")