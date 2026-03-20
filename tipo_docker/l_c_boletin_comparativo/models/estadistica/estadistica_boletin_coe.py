# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.l_c_boletin_comparativo.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.l_c_boletin_comparativo.models.funtions.componest.tablas import *
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

    #funcion para calcular resultados  
    def comparativo_resultados(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos):

        
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

        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)

        
        encabezado_comparativo(pdf, True, fecha_titulo_dos, fecha_titulo, 10)
        pdf.ln(-5)

        sepador_mapa_dos(pdf, True, "AFECTACIÓN A LA AMENAZA ", 5)
        # pdf.ln()
        claculo_mapa_dos(pdf, res_calculo_ante[0], res_calculo_act[0], "MENORES RECUPERADOS",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[1], res_calculo_act[1], "PRESENTACIÓN VOLUNTARIA",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[2], res_calculo_act[2], "SOMETIMIENTOS",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 3,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 3,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "CAPTURAS",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 4,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 4,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "MDOM",1, 7, 18, 5)

        sepador_mapa_dos(pdf, True, "AFECTACIÓN A PROPIAS TROPAS", 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 5,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "ASESINADOS",-1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 6,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "HERIDOS",-1, 7, 18, 5)

        sepador_mapa_dos(pdf, True, "MATERIAL DE GUERRA", 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "ARMAS DE LARGO ALCANCE",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 8,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 8,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "ARMAS DE CORTO ALCANCE",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 9,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 9,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "ARMAS DE ACOMPAÑAMIENTO",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 10,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 10,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "MUNICIONES",1, 7, 18, 5)

        sepador_mapa_dos(pdf, True, "COMBATES", 5)
        claculo_mapa_dos(pdf, res_calculo_ante[11], res_calculo_act[11], "COMBATES POSITIVOS",1, 8, 14, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[12], res_calculo_act[12], "COMBATES NEGATIVOS",1, 8, 14, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[13], res_calculo_act[13], "COMBATES SIN RESULTADOS",1, 8, 14, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[14], res_calculo_act[14], "TOTAL DE COMBATES",1, 8, 14, 5)

        sepador_mapa_dos(pdf, True, "MATERIAL DE EXPLOSIVOS", 5)
        claculo_mapa_dos(pdf, res_calculo_ante[15], res_calculo_act[15], "NEUTRALIZACIÓN TERRORISTA",1, 8, 14, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[16], res_calculo_act[16], "A.E",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[17], res_calculo_act[17], "MAP(Mina Anti Persona)",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[18], res_calculo_act[18], "EXPLOSIVOS kg",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[19], res_calculo_act[19], "CORDÓN DETONANTE m",1, 7, 18, 5)
        claculo_mapa_dos(pdf, res_calculo_ante[20], res_calculo_act[20], "MECHA LENTA m",1, 7, 18, 5)

        sepador_mapa_dos(pdf, True, "NARCOTRÁFICO", 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 21,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 21,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "COCAÍNA Kg",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 22,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 22,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "MARIHUANA Kg",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 23,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 23,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "PBC Kg",1, 7, 18, 5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 24,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 24,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "LAB. CLORHIDRATO DE COCAINA",1, 7, 18, 5)
        #cabecera tabla

        pdf.ln(-160)
        # # encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)
        
        encabezado_comparativo(pdf, True, fecha_titulo_dos, fecha_titulo, 170)
        pdf.ln(-5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 25,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 25,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "LAB. PASTA O BASE DE COCA",1, 7, 18,165)
        # pdf.ln(-5)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 26,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 26,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "SEMILLEROS",1, 7, 18,165)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 27,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 27,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "MATA(S) DE COCA EN SEMILLERO",1, 7, 18,165)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 28,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 28,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "INSUMOS LIQUIDOS Gal",1, 7, 18,165)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 29,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 29,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "INSUMOS SOLIDOS Kg",1, 7, 18,165)

        sepador_mapa_dos(pdf, True, "PLAN AMAZONÍA", 165)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "CAPTURAS PLAN AMAZONIA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[31], res_calculo_act[31], "PLANTULAS SEMBRADA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[32], res_calculo_act[32], "MADERA INCAUTADA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[63], res_calculo_act[63], "ANIMALES INCAUTADOS",1, 7, 18, 165)
            
        sepador_mapa_dos(pdf, True, "MINERÍA ILEGAL", 165)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(pdf, valor_ant[0], valor_act[0], "CAPTURAS MINERIA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[34], res_calculo_act[34], "MENORES R. MINERIA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[35], res_calculo_act[35], "EIYM",1, 8, 14, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[36], res_calculo_act[36], "EXCAVADORA(S)",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[37], res_calculo_act[37], "RETROEXCAVADORA(S)",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[38], res_calculo_act[38], "MAQUINARIA PESADA",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[40], res_calculo_act[40], "UPM ILEGAL",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[65], res_calculo_act[65], "COLTAN KG",1, 7, 18, 165)

        sepador_mapa_dos(pdf, True, "ECONOMÍAS ILÍCITAS", 165)
        claculo_mapa_dos(pdf, res_calculo_ante[42], res_calculo_act[42], "LIBERADOS",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[43], res_calculo_act[43], "RESCATADOS",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[44], res_calculo_act[44], "VÁLVULAS",1, 7, 18, 165)
        claculo_mapa_dos(pdf, res_calculo_ante[45], res_calculo_act[45], "REFINERIAS",1, 7, 18, 165)

        sepador_mapa_dos(pdf, True, "DEPÓSITOS", 165)
        claculo_mapa_dos(pdf, res_calculo_ante[46], res_calculo_act[46], "DEPÓSITO ILEGAL",1, 7, 18, 165) 
    
