# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.k_c_boletin_comparativo_mapa.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.k_c_boletin_comparativo_mapa.models.funtions.componest.tablas import *
from tipo_docker.k_c_boletin_comparativo_mapa.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import json
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
    def comparativo_mapa(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos):

        
        dato =""

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
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        # pdf.ln(5) 
    
        # if filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
        #     mapa_filtrado(hechos_actual)
            
        # else:
        #     mapa_general(hechos_actual)


        pdf.set_fill_color(193, 30, 38)
        #pdf.rounded_rect(65, 31, 90, 12, 1,'D', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        pdf.text(70,35,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 8)
        pdf.text(70,38.5,fecha_titulo)
        pdf.text(70,42,fecha_titulo_dos)

        mapa_general(hechos_actual, filtro) 

        ruta = filtro[15] 

        mapa  = '{}static/img/img_mapas/mapa.png'.format(filtro[15])
        mapa_fondo  = '{}static/img/img_mapas/mapa_fondo.png'.format(filtro[15])

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(mapa_fondo,13,18.7,162.1,199)
        pdf.image(mapa,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

        pdf.ln(5)

        encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)

        sepador_mapa(pdf, True, "AFECTACIÓN A LA AMENAZA ")
        claculo_mapa(pdf, res_calculo_ante[0], res_calculo_act[0], "MENORES RECUPERADOS",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[1], res_calculo_act[1], "PRESENTACIÓN VOLUNTARIA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[2], res_calculo_act[2], "SOMETIMIENTOS",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 3,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 3,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "CAPTURAS",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 4,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 4,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "MDOM",1, 7, 18)

        sepador_mapa(pdf, True, "AFECTACIÓN A PROPIAS TROPAS")
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 5,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "ASESINADOS",-1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 6,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "HERIDOS",-1, 7, 18)

        sepador_mapa(pdf, True, "MATERIAL DE GUERRA")
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "ARMAS DE LARGO ALCANCE",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 8,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 8,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "ARMAS DE CORTO ALCANCE",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 9,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 9,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "ARMAS DE ACOMPAÑAMIENTO",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 10,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 10,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "MUNICIONES",1, 7, 18)

        sepador_mapa(pdf, True, "COMBATES")
        claculo_mapa(pdf, res_calculo_ante[11], res_calculo_act[11], "COMBATES POSITIVOS",1, 8, 14)
        claculo_mapa(pdf, res_calculo_ante[12], res_calculo_act[12], "COMBATES NEGATIVOS",1, 8, 14)
        claculo_mapa(pdf, res_calculo_ante[13], res_calculo_act[13], "COMBATES SIN RESULTADOS",1, 8, 14)
        claculo_mapa(pdf, res_calculo_ante[14], res_calculo_act[14], "TOTAL DE COMBATES",1, 8, 14)


        sepador_mapa(pdf, True, "MATERIAL DE EXPLOSIVOS")
        claculo_mapa(pdf, res_calculo_ante[15], res_calculo_act[15], "NEUTRALIZACIÓN TERRORISTA",1, 8, 14)
        claculo_mapa(pdf, res_calculo_ante[16], res_calculo_act[16], "A.E",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[17], res_calculo_act[17], "MAP(Mina Anti Persona)",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[18], res_calculo_act[18], "EXPLOSIVOS kg",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[19], res_calculo_act[19], "CORDÓN DETONANTE m",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[20], res_calculo_act[20], "MECHA LENTA m",1, 7, 18)

        sepador_mapa(pdf, True, "NARCOTRÁFICO")
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 21,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 21,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "COCAÍNA Kg",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 22,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 22,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "MARIHUANA Kg",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 23,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 23,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "PBC Kg",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 24,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 24,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "LAB. CLORHIDRATO DE COCAINA",1, 7, 18)
        #cabecera tabla
        # pdf.ln(10)

        pdf.ln(5)
        # # encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)
        
        encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 25,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 25,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "LAB. PASTA O BASE DE COCA",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 26,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 26,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "SEMILLEROS",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 27,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 27,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "MATA(S) DE COCA EN SEMILLERO",1, 7, 18)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 28,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 28,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "INSUMOS LIQUIDOS Gal",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[29], res_calculo_act[29], "INSUMOS SOLIDOS Kg",1, 7, 18)

        sepador_mapa(pdf, True, "PLAN AMAZONÍA")
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "CAPTURAS PLAN AMAZONIA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[31], res_calculo_act[31], "PLANTULAS SEMBRADA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[32], res_calculo_act[32], "MADERA INCAUTADA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[63], res_calculo_act[63], "ANIMALES INCAUTADOS",1, 7, 18)

        sepador_mapa(pdf, True, "MINERÍA ILEGAL")
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        claculo_mapa(pdf, valor_ant[0], valor_act[0], "CAPTURAS MINERIA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[34], res_calculo_act[34], "MENORES R. MINERIA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[35], res_calculo_act[35], "EIYM",1, 8, 14)
        claculo_mapa(pdf, res_calculo_ante[36], res_calculo_act[36], "EXCAVADORA(S)",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[37], res_calculo_act[37], "RETROEXCAVADORA(S)",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[38], res_calculo_act[38], "MAQUINARIA PESADA",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[40], res_calculo_act[40], "UPM ILEGAL",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[65], res_calculo_act[65], "COLTAN KG",1, 7, 18)

        sepador_mapa(pdf, True, "ECONOMÍAS ILÍCITAS")
        claculo_mapa(pdf, res_calculo_ante[42], res_calculo_act[42], "LIBERADOS",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[43], res_calculo_act[43], "RESCATADOS",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[44], res_calculo_act[44], "VÁLVULAS",1, 7, 18)
        claculo_mapa(pdf, res_calculo_ante[45], res_calculo_act[45], "REFINERIAS",1, 7, 18)

        sepador_mapa(pdf, True, "DEPÓSITOS")
        claculo_mapa(pdf, res_calculo_ante[46], res_calculo_act[46], "DEPÓSITO ILEGAL",1, 7, 18) 

        mapa  = '{}static/img/img_mapas/mapa.png'.format(filtro[15])
        mapa_fondo  = '{}static/img/img_mapas/mapa_fondo.png'.format(filtro[15])

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(mapa_fondo,13,18.7,162.1,199)
        pdf.image(mapa,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)



        pdf.set_fill_color(193, 30, 38)
        #pdf.rounded_rect(65, 31, 90, 12, 1,'D', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)
        pdf.text(70,35,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 8)
        pdf.text(70,38.5,fecha_titulo)
        pdf.text(70,42,fecha_titulo_dos)
