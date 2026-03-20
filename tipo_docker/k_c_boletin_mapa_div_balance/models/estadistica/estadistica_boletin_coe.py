# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.k_c_boletin_mapa_div_balance.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.k_c_boletin_mapa_div_balance.models.funtions.componest.tablas import *
from tipo_docker.k_c_boletin_mapa_div_balance.maps.funciones.mapa_filtro import *
import json


conexion_pos = Databa_bases()
import seaborn as sns
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
        

        # f.write("-----------------------------------------------------"+"\n")
        # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

        if validar == "SI":
            spoa = spoa
        else:
            spoa =  res_calculo[numero]
            

        return[spoa, no_spoa]


#funcion para calcular resultados  
# def comparativo_mapa(pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):

#     filtros = selecion_filtro(filtro)

#     query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros)
#     query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros)
#     query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros)

#     resultados_actual = conexion_pos.comando_query(query_actual[0])
#     hechos_actual = conexion_pos.comando_query(query_actual[1])
#     erradicacion_actual = conexion_pos.comando_query(query_actual[2])

#     resultados_anterior = conexion_pos.comando_query(query_anterior[0])
#     hechos_anterior = conexion_pos.comando_query(query_anterior[1])
#     erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

    
#     resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
#     hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])
#     erradicacion_anterior_tres = conexion_pos.comando_query(query_anterior_tres[2])

#     res_calculo_ante_tres = estadistica_resultados(resultados_anterior_tres, hechos_anterior_tres)
#     res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior)
#     res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual)
    
#     # pdf.ln(5) 
  
#     # if filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
#     #     mapa_filtrado(hechos_actual)
        
#     # else:
#     #     mapa_general(hechos_actual)
#     sece_tres = ""
#     sece_dos = ""
#     sece_uno = ""
#     if anio_ant_tres == "2023":
#         sece_tres = "INICIO CESE AL FUEGO"
#     if anio_ant == "2023":
#         sece_dos = "INICIO CESE AL FUEGO"
#     if anio_act == "2023":
#         sece_uno = "INICIO CESE AL FUEGO"




#     pdf.set_fill_color(193, 30, 38)
#     pdf.rounded_rect(6, 35, 90, 16, 1,'D', '1234')
#     pdf.set_text_color(0,0,0)
#     pdf.set_font('Arial', 'B', 10)
#     pdf.text(10,39,"FECHA INFORMACIÓN")
#     pdf.set_font('Arial', 'B', 8)
#     pdf.text(10,42.5,fecha_titulo_tres)
#     pdf.text(10,46,fecha_titulo_dos)
#     pdf.text(10,49.5, fecha_titulo)

#     pdf.set_text_color(128,0,0)
#     pdf.text(58,42.5,sece_tres)
#     pdf.text(58,46,sece_dos)
#     pdf.text(58,49.5, sece_uno)
    
#     ruta = filtro[15] 
#     json_ruta = '{}static/MUNICIPIOS filtrados.json'.format(ruta)
        
#     rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)   
#     label_eventos = '{}static/img/img_mapas/label_eventos.png'.format(ruta)   
    
#     # datos_diccionario = json.JSONDecoder(json_ruta)
#     # with open(json_ruta, "r") as j:

#     with open(json_ruta, "rb") as read_file:
#         data = dict(json.load(read_file))

#     hechos=[]
#     print(filtro)
#     if filtro[0]!= "" and filtro[0]!= "---" or filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
        
#         if filtro[0]!= "" and filtro[0]!= "---" :

#             if filtro[0] == "DAVAA" or filtro[0] == "DIVFE" or filtro[0] == "TREJC":
                
#                 mapa_general(hechos_actual, filtro) 
#                 mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
#                 pdf.image(mapa,90,3,160,200)
#                 pdf.image(label_eventos,120, 155, 60, 15)
#             else:
#                 for x in data:
#                     for y in data[x]:
#                         if y['AGR_DIV'] == filtro[0]:
#                             for d in hechos_actual:
#                                 if y['MPIO'] == d[7] and y['DPTO'] == d[6]:
#                                     hechos.append(d)
#                                     # print("hola")

#                 mapa_filtrado(hechos, filtro)
#                 mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
#                 pdf.image(mapa,105,3,140,180)
#                 pdf.image(label_eventos,120, 165, 60, 15)
#         else:
#                 # print("---")
#                 mapa_filtrado_dep(hechos_actual, filtro)
#                 mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
#                 pdf.image(mapa,105,3,140,180)
#                 pdf.image(label_eventos,120, 165, 60, 15)

#     else:
#         # mapa_general(hechos_actual)

#         mapa_general(hechos_actual, filtro) 
#         mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
#         pdf.image(mapa,90,3,160,200)
#         pdf.image(label_eventos,120, 155, 60, 15)


#     # mapa_general(hechos_actual, filtro) 
#     # mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
#     # pdf.image(mapa,90,3,160,200)
    
    
#     pdf.image(rosa_nautica,120, 40, 15, 15)
    

#     pdf.ln(5)

#     # encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)

#     sepador_mapa(pdf, True, "AFECTACIÓN A LA AMENAZA ", -7, 12, 115)
#     encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant, anio_ant_tres,  -7)

#     # sepador_mapa(pdf, True, "AFECTACIÓN A LA AMENAZA ", 228, 12, 115)
#     # encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant, anio_ant_tres,  225)
#     altura = 61
#     pos = claculo_mapa(pdf, res_calculo_ante[0], res_calculo_act[0], res_calculo_ante_tres[0], "MENORES RECUPERADOS",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[1], res_calculo_act[1], res_calculo_ante_tres[0], "PRESENTACIÓN VOLUNTARIA",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[2], res_calculo_act[2],res_calculo_ante_tres[2], "SOMETIMIENTOS",1, 7, 18,  -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[3], res_calculo_act[3],res_calculo_ante_tres[3], "CAPTURAS",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[4], res_calculo_act[4],res_calculo_ante_tres[4], "MDOM",1, 7, 18, -7, ruta, 72, altura)

#     sepador_mapa(pdf, True, "AFECTACIÓN A PROPIAS TROPAS ", pos_cell, 1, ancho_cel)
#     pdf.ln(6)
#     altura =  pos+6.9
#     pos = claculo_mapa(pdf, res_calculo_ante[5], res_calculo_act[5],res_calculo_ante_tres[5], "ASESINADOS",-1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[6], res_calculo_act[6],res_calculo_ante_tres[6], "HERIDOS",-1, 7, 18, -7, ruta, 72, altura)

#     sepador_mapa(pdf, True, "MATERIAL DE GUERRA ", -7, 1, 115)
#     pdf.ln(6)
#     altura =  pos+6.9
#     pos = claculo_mapa(pdf, res_calculo_ante[7], res_calculo_act[7],res_calculo_ante_tres[7], "ARMAS DE LARGO ALCANCE",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[8], res_calculo_act[8],res_calculo_ante_tres[8], "ARMAS DE CORTO ALCANCE",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[9], res_calculo_act[9],res_calculo_ante_tres[9], "ARMAS DE ACOMPAÑAMIENTO",1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[10], res_calculo_act[10],res_calculo_ante_tres[10], "MUNICIONES",1, 7, 18, -7, ruta, 72, altura)

#     sepador_mapa(pdf, True, "COMBATES", -7, 1, 115)
#     pdf.ln(6)

#     altura =  pos+7
#     pos = claculo_mapa(pdf, res_calculo_ante[11], res_calculo_act[11],res_calculo_ante_tres[11], "COMBATES POSITIVOS",1, 8, 14, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[12], res_calculo_act[12],res_calculo_ante_tres[12], "COMBATES NEGATIVOS",-1, 8, 14, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[13], res_calculo_act[13],res_calculo_ante_tres[13], "COMBATES SIN RESULTADOS",-1, 8, 14, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[14], res_calculo_act[14],res_calculo_ante_tres[14], "TOTAL DE COMBATES",1, 8, 14, -7, ruta, 72, altura)

#     sepador_mapa(pdf, True, "ATAQUES A LA FUERZA PUBLICA", -7, 1, 115)
#     pdf.ln(6)
#     altura =  pos+7.5
#     pos = claculo_mapa(pdf, res_calculo_ante[66], res_calculo_act[66],res_calculo_ante_tres[66], "HOSTIGAMIENTOS",-1, 7, 18, -7, ruta, 72, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[67], res_calculo_act[67],res_calculo_ante_tres[67], "ASONADAS",-1, 7, 18, -7, ruta, 72, altura)


#     pdf.ln(-184)
#     sepador_mapa(pdf, True, "NARCOTRÁFICO", 228, 12, 115)
#     encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant, anio_ant_tres,  228)

#     altura = 35.2
#     pos = claculo_mapa(pdf, res_calculo_ante[21], res_calculo_act[21], res_calculo_ante_tres[21], "COCAÍNA Kg",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[22], res_calculo_act[22], res_calculo_ante_tres[22], "MARIHUANA Kg",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[23], res_calculo_act[23], res_calculo_ante_tres[23], "PBC Kg",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[24], res_calculo_act[24], res_calculo_ante_tres[24], "LAB. CLORHIDRATO DE COCAINA",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[25], res_calculo_act[25], res_calculo_ante_tres[25], "LAB. PASTA O BASE DE COCA",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[26], res_calculo_act[26], res_calculo_ante_tres[26], "SEMILLEROS",1, 7, 18, 228, ruta, 307, altura)

#     sepador_mapa(pdf, True, "MATERIAL DE EXPLOSIVOS", pos_cell, 1, ancho_cel)
#     pdf.ln(6)
#     altura =  pos+7
#     pos = claculo_mapa(pdf, res_calculo_ante[15], res_calculo_act[15], res_calculo_ante_tres[15], "NEUTRALIZACIÓN TERRORISTA",1, 8, 14, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[16], res_calculo_act[16], res_calculo_ante_tres[16], "A.E",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[17], res_calculo_act[17], res_calculo_ante_tres[17], "MAP (Mina Anti Persona)",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[18], res_calculo_act[18], res_calculo_ante_tres[18], "EXPLOSIVOS kg",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[19], res_calculo_act[19], res_calculo_ante_tres[19], "CORDÓN DETONANTE m",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[20], res_calculo_act[20], res_calculo_ante_tres[20], "MECHA LENTA m",1, 7, 18, 228, ruta, 307, altura)

#     sepador_mapa(pdf, True, "ECONOMÍAS ILÍCITAS", 228, 1, 115)
#     pdf.ln(6)
#     altura =  pos+7
#     pos = claculo_mapa(pdf, res_calculo_ante[42], res_calculo_act[42], res_calculo_ante_tres[42], "LIBERADOS",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[43], res_calculo_act[43], res_calculo_ante_tres[43], "RESCATADOS",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[44], res_calculo_act[44], res_calculo_ante_tres[44], "VÁLVULAS",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[45], res_calculo_act[45], res_calculo_ante_tres[45], "REFINERIAS",1, 7, 18, 228, ruta, 307, altura)

#     sepador_mapa(pdf, True, "MINERÍA ILEGAL", 228, 1, 115)
#     pdf.ln(6)
#     altura =  pos+7
#     pos = claculo_mapa(pdf, res_calculo_ante[33], res_calculo_act[33], res_calculo_ante_tres[33], "CAPTURAS MINERIA",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[35], res_calculo_act[35], res_calculo_ante_tres[35], "EIYM",1, 8, 14, 228, ruta, 307, altura)
#     altura =  pos

#     maquinaria_anterior = [res_calculo_ante[36], res_calculo_ante[37], res_calculo_ante[38], res_calculo_ante[39], res_calculo_ante[41]]
#     maquinaria_anctual = [res_calculo_act[36], res_calculo_act[37], res_calculo_act[38], res_calculo_act[39], res_calculo_act[41]]
#     maquinaria_anterior_tres = [res_calculo_ante_tres[36], res_calculo_ante_tres[37], res_calculo_ante_tres[38], res_calculo_ante_tres[39], res_calculo_ante_tres[41]]

#     pos = claculo_mapa_mapa(pdf, maquinaria_anterior, maquinaria_anctual, maquinaria_anterior_tres, "MAQUINARIA AMARILLA",1, 7, 18, 228, ruta, 307, altura)
    
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[65], res_calculo_act[65], res_calculo_ante_tres[65], "COLTAN kg",1, 7, 18, 228, ruta, 307, altura)

#     sepador_mapa(pdf, True, "PLAN AMAZONÍA", 228, 1, 115)
#     pdf.ln(6)
#     altura =  pos+7
#     pos = claculo_mapa(pdf, res_calculo_ante[30], res_calculo_act[30], res_calculo_ante_tres[30], "CAPTURAS PLAN AMAZONIA",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[32], res_calculo_act[32], res_calculo_ante_tres[32], "MADERA INCAUTADA",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[63], res_calculo_act[63], res_calculo_ante_tres[63], "ANIMALES INCAUTADOS",1, 7, 18, 228, ruta, 307, altura)
#     altura =  pos
#     pos = claculo_mapa(pdf, res_calculo_ante[31], res_calculo_act[31], res_calculo_ante_tres[31], "PLANTULAS SEMBRADA",1, 7, 18, 228, ruta, 307, altura)
   

#     # claculo_mapa(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[40], res_calculo_act[40], "UPM ILEGAL",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[65], res_calculo_act[65], "COLTAN KG",1, 7, 18)



#     # claculo_mapa(pdf, res_calculo_ante[27], res_calculo_act[27], "MATA(S) DE COCA EN SEMILLERO",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[28], res_calculo_act[28], "INSUMOS LIQUIDOS Gal",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[29], res_calculo_act[29], "INSUMOS SOLIDOS Kg",1, 7, 18)




#     # sepador_mapa(pdf, True, "PLAN AMAZONÍA")
#     # claculo_mapa(pdf, res_calculo_ante[30], res_calculo_act[30], "CAPTURAS PLAN AMAZONIA",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[31], res_calculo_act[31], "PLANTULAS SEMBRADA",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[32], res_calculo_act[32], "MADERA INCAUTADA",1, 7, 18)
#     # claculo_mapa(pdf, res_calculo_ante[63], res_calculo_act[63], "ANIMALES INCAUTADOS",1, 7, 18)




#     # sepador_mapa(pdf, True, "DEPÓSITOS")
#     # claculo_mapa(pdf, res_calculo_ante[46], res_calculo_act[46], "DEPÓSITO ILEGAL",1, 7, 18) 

#     # # pdf.image(mapa,25,12,170,210)
#     # # pdf.image(rosa_nautica,5, 40, 30, 30)


#     # pdf.set_fill_color(193, 30, 38)
#     # pdf.rounded_rect(65, 26, 115, 12, 1,'D', '1234')
#     # pdf.set_text_color(0,0,0)
#     # pdf.set_font('Arial', 'B', 10)
#     # pdf.text(70,30,"FECHA INFORMACIÓN")
#     # pdf.set_font('Arial', 'B', 8)
#     # pdf.text(70,33.5,fecha_titulo)
#     # pdf.text(70,37,fecha_titulo_dos)
  
#funcion para calcular resultados  

    def comparativo_mapa(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):

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
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        
        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])
        erradicacion_anterior_tres = conexion_pos.comando_query(query_anterior_tres[2])

        res_calculo_ante_tres = estadistica_resultados(resultados_anterior_tres, hechos_anterior_tres, filtro)
        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
        # pdf.ln(5) 
    
        # if filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
        #     mapa_filtrado(hechos_actual)
            
        # else:
        #     mapa_general(hechos_actual)
        sece_tres = ""
        sece_dos = ""
        sece_uno = ""
        if anio_ant_tres == "2023":
            sece_tres = "INICIO CESE AL FUEGO"
        if anio_ant == "2023":
            sece_dos = "INICIO CESE AL FUEGO"
        if anio_act == "2023":
            sece_uno = "INICIO CESE AL FUEGO"




        pdf.set_fill_color(193, 30, 38)
        #pdf.rounded_rect(160, 33, 70, 16, 1,'D', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 12)
        #pdf.text(165,37,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 8)
        # pdf.text(10,42.5,fecha_titulo_tres)
        #pdf.text(165,42,fecha_titulo_dos)
        #pdf.text(165,45.5, fecha_titulo)


          
        label_eventos = '{}static/img/img_mapas/label_eventos.png'.format(ruta)    
        hechos=[]


        try:
   
            if filtro[0]!= "" and filtro[0]!= "---" or filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
                
                if filtro[0]!= "" and filtro[0]!= "---" :

                    if filtro[0] == "DAVAA" or filtro[0] == "DIVFE" or filtro[0] == "TREJC":
                        
                        mapa_general(res_calculo_act[100], filtro) 
                        mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                        pdf.image(mapa,-59.5,-59,229,310)
                        pdf.image(label_eventos,5, 175, 60, 15)
                        
                    else:
                        for x in data:
                            for y in data[x]:
                                if y['AGR_DIV'] == filtro[0]:
                                    for d in res_calculo_act[100]:
                                        if y['MPIO'] == d[7] and y['DPTO'] == d[6]:
                                        
                                            hechos.append(d)
                                            # print("hola")
                        
                        mapa_filtrado(hechos, filtro)
                        if filtro[0] == "DIV01":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta,filtro[0])
                            pdf.image(mapa,-23,-34.5,205.5,282.5)
                            pdf.image(label_eventos,70, 180, 60, 15)

                        elif filtro[0] == "DIV02":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-39,-35.5,206,282.5)
                            pdf.image(label_eventos,80, 193, 60, 15)

                        elif filtro[0] == "DIV03":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-33,-36,205,282)
                            pdf.image(label_eventos,80, 193, 60, 15)
                          
                        elif filtro[0] == "DIV04":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25.5,-23,189.7,258)
                            pdf.image(label_eventos,80, 193, 60, 15)
                                                      
                        elif filtro[0] == "DIV05":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-21.5,-24,180,245.5)
                            pdf.image(label_eventos,80, 193, 60, 15)
                        
                        elif filtro[0] == "DIV06":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-20,186.5,251)
                            pdf.image(label_eventos,80, 193, 60, 15)
                                                       
                        elif filtro[0] == "DIV07":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-30,-24,198,268.5)
                            pdf.image(label_eventos,80, 193, 60, 15)
                                                                               
                        elif filtro[0] == "DIV08":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-26,186.2,251.5)
                            pdf.image(label_eventos,80, 193, 60, 15)
                           
                        elif filtro[0] == "FUTCO":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-44,-149,315,476)
                            pdf.image(label_eventos,80, 193, 60, 15)
                        
                        else:
                            mapa_general(res_calculo_act[100], filtro) 
                            mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                            pdf.image(mapa,-59.5,-59,229,310)
                            pdf.image(label_eventos,5, 175, 60, 15)


                            
                else:
   
                    mapa_general(res_calculo_act[100], filtro) 
                    mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                    pdf.image(mapa,-59.5,-59,229,310)
                    pdf.image(label_eventos,5, 175, 60, 15)

            else:
                # mapa_general(hechos_actual)

                    mapa_general(res_calculo_act[100], filtro) 
                    mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                    pdf.image(mapa,-53.5,-55,229,310)
                    pdf.image(label_eventos,5, 175, 60, 15)


            #mapa_general(hechos_actual, filtro) 
           # mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
            #pdf.image(mapa,90,3,160,200)
              
        except:
             print("sin datos")
             

    def comparativo_mapa_gracica_1(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):
        plt.clf()
        plt.cla()
        plt.close()
        plt.rcParams["figure.figsize"] = (6, 5)
        plt.figure()
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
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        
        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])
        erradicacion_anterior_tres = conexion_pos.comando_query(query_anterior_tres[2])

        res_calculo_ante_tres = estadistica_resultados(resultados_anterior_tres, hechos_anterior_tres, filtro)
        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
        # pdf.ln(5) 
    
        # if filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
        #     mapa_filtrado(hechos_actual)
            
        # else:
        


        #CALCULO DE RESULTADOS 
        CANTIDAD_2=[]
        ANIO=[]
        columns=[]

        pos = claculo_mapa_2(res_calculo_ante[0], res_calculo_act[0],1, 7, 18)

    
        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("MENORES RECU.")
        columns.append("MENORES RECU.")

        
        pos = claculo_mapa_2(res_calculo_ante[1], res_calculo_act[1],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("PRES. VOLUNTARIA")
        columns.append("PRES. VOLUNTARIA")

                        
        pos = claculo_mapa_2(res_calculo_ante[2], res_calculo_act[2],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("SOMETIMIENTOS")
        columns.append("SOMETIMIENTOS")


        if filtro[17] == "sin_delco":
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 61,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 61,  "SI") #funcion para filtar el spoa
            valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 61,  "SI") #funcion para filtar el spoa
        else:
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 3,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 3,  "SI") #funcion para filtar el spoa
            valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 3,  "SI") #funcion para filtar el spoa

                        
        pos = claculo_mapa_2(valor_ant[0], valor_act[0],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("CAPTURAS")
        columns.append("CAPTURAS")

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 4,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 4,  "SI") #funcion para filtar el spoa
       
        pos = claculo_mapa_2(valor_ant[0], valor_act[0],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("MDOM")
        columns.append("MDOM")
  

        # Count plot
        #sns.countplot(x = CANTIDAD_2, hue = AÑO)
        #plt.rcParams["figure.figsize"] = (50, 50)
        #plt.figure()
        Palette = ["#7F7F7F", "#FFC000"] #define your preference
        sns.set()
        
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        ax = sns.barplot(x = columns, y=CANTIDAD_2 , hue = ANIO, palette=Palette)
        
        ax.bar_label(ax.containers[1], fontsize=16, color="black")
        ax.bar_label(ax.containers[0], fontsize=16, color="black")
        sns.despine()
        sns.color_palette("rocket")
        locs, labels = plt.xticks()
        plt.rcParams["figure.figsize"] = (250, 150)
        font1 = {'family':'serif','color':'black','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}


        #plt.xlabel("Afectaciones a la Amenaza", fontdict = font2)
        plt.rc('xtick', labelsize=30) 
        plt.rc('ytick', labelsize=30) 

        plt.setp(labels, rotation=45)
       
        plt.tight_layout()

        sns.despine(top=True, right=True, left=True, bottom=True)
        
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo1.png", transparent=True)
        ax.get_figure().clf()

        
        #if len(CANTIDAD_2) > 0:
            #pdf.set_text_color(70,70,70)
            #pdf.set_font('BebasNeue', '', 16)
            #pdf.text(270,200,str("AFECTACIONES A LA AMENAZA"))

                
        if len(CANTIDAD_2) >0:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(170,45,str("AFECTACIONES A LA AMENAZA"))
        else:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(170,45,str("NO REGISTRA AFECTACIONES A LA AMENAZA"))




    def comparativo_mapa_grafica_2(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):
        plt.clf()

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
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        
        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])

        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
        
       #CALCULO DE RESULTADOS 
        CANTIDAD_2=[]
        ANIO=[]
        columns=[]

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 21,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 21,  "SI") #funcion para 

        pos = claculo_mapa_2(valor_ant[0], valor_act[0],1, 7, 18)
    
        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("COCAÍNA Kg")
        columns.append("COCAÍNA Kg")


        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 22,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 22,  "SI") #funcion para 
        pos = claculo_mapa_2(valor_ant[0], valor_act[0],1, 7, 18)
    
        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("MARIHUANA Kg")
        columns.append("MARIHUANA Kg")

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 23,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 23,  "SI") #funcion para

        pos = claculo_mapa_2(valor_ant[0], valor_act[0],1, 7, 18)
    
        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("PBC Kg")
        columns.append("PBC Kg")
           # Count plot
        #sns.countplot(x = CANTIDAD_2, hue = AÑO)
        color = (sns.dark_palette("green"))
        sns.set()
        
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        Palette = ["#7F7F7F", "#FFC000"] #define your preference

        ax = sns.barplot(x = columns , y= CANTIDAD_2 , hue = ANIO, palette =Palette)
        
        ax.bar_label(ax.containers[1], fontsize=16, color="black")
        ax.bar_label(ax.containers[0], fontsize=16, color="black")
        sns.despine()
        sns.color_palette("rocket")
        locs, labels = plt.xticks()
        plt.rcParams["figure.figsize"] = (250, 150)
        font1 = {'family':'serif','color':'black','size':15}
        font2 = {'family':'serif','color':'darkred','size':15}

        #plt.xlabel("Afectaciones al Nacotrafico", fontdict = font2)
    

        plt.rc('xtick', labelsize=20) 
        plt.rc('ytick', labelsize=20) 

        plt.setp(labels, rotation=30)
        plt.tight_layout()
        sns.despine(top=True, right=True, left=True, bottom=True)
        
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo2.png", transparent=True)
        ax.get_figure().clf()
                
        if len(CANTIDAD_2) >0:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(270,45,str("AFECTACIÓN AL NARCOTRAFICO"))
        else:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(270,45,str("NO REGISTRA AFECTACIÓN AL NARCOTRAFICO"))



    def comparativo_mapagrafica_3(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):
        plt.clf()

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
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])


        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])


        
        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])



        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
   
       #CALCULO DE RESULTADOS 
        CANTIDAD_2=[]
        ANIO=[]
        columns=[]

        pos = claculo_mapa_2(res_calculo_ante[14], res_calculo_act[14],1, 8, 14)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("COMBATES")
        columns.append("COMBATES")

        pos = claculo_mapa_2(res_calculo_ante[66], res_calculo_act[66],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("HOSTIGAMIENTOS")
        columns.append("HOSTIGAMIENTOS")

        
        pos = claculo_mapa_2(res_calculo_ante[67], res_calculo_act[67],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("ASONADAS")
        columns.append("ASONADAS")
                
        pos = claculo_mapa_2(res_calculo_ante[95], res_calculo_act[95],1, 7, 18)

        CANTIDAD_2.append(int(pos[0]))
        CANTIDAD_2.append(int(pos[1]))
        ANIO.append(anio_ant)
        ANIO.append(anio_act)
        columns.append("ATAQUE UAS")
        columns.append("ATAQUE UAS")

                #sns.countplot(x = CANTIDAD_2, hue = AÑO)

        sns.set()
        Palette = ["#7F7F7F", "#FFC000"] #define your preference
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        ax = sns.barplot(x = columns, y=CANTIDAD_2 , hue = ANIO, palette =Palette)
        
            
        ax.bar_label(ax.containers[1], fontsize=16, color="black")
        ax.bar_label(ax.containers[0], fontsize=16, color="black")

        sns.despine()
        sns.color_palette("rocket")
        locs, labels = plt.xticks()
        plt.rcParams["figure.figsize"] = (250, 150)
        font1 = {'family':'serif','color':'black','size':15}
        font2 = {'family':'serif','color':'darkred','size':15}

           #plt.xlabel("Afectaciones al Nacotrafico", fontdict = font2)
        
        plt.rc('xtick', labelsize=20) 
        plt.rc('ytick', labelsize=20) 

        plt.setp(labels, rotation=30)
        plt.tight_layout()
        sns.despine(top=True, right=True, left=True, bottom=True)
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo3.png", transparent=True)
        ax.get_figure().clf()
        plt.clf()
        
        if len(CANTIDAD_2) >0:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(170,140,str("ATAQUE A LA FUERZA"))
        else:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(170,140,str("NO REGISTRA ATAQUE A LA FUERZA"))
             
    def comparativo_mapagrafica_4(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres):
        plt.clf()
        plt.rcParams["figure.figsize"] = (6, 6)
        plt.figure()

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
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])

        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])

        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
             
        try:

            # declaring data 
            data_pie = [] 
            keys = [] 
            colors = []

            ANIO=[]
            columns=[]
            explode = []

            pos = claculo_mapa_2(res_calculo_ante[11], res_calculo_act[11],1, 8, 14)
            if pos[1]>0:
                data_pie.append(int(pos[1]))
                keys.append("POS.")
                explode.append(0.05)
                colors.append('#FFC000')

            pos = claculo_mapa_2(res_calculo_ante[12], res_calculo_act[12],1, 8, 14)
            if pos[1]>0:
                data_pie.append(int(pos[1]))
                keys.append("NEG")
                explode.append(0.05)
                colors.append('#FF0000')

            pos = claculo_mapa_2(res_calculo_ante[13], res_calculo_act[13],1, 8, 14)
            if pos[1]>0:
                data_pie.append(int(pos[1]))
                keys.append("SIN RESUL.")
                explode.append(0.05)
                colors.append('#7F7F7F')

            # declaring exploding pie 
            
            # define Seaborn color palette to use 
            palette_color = sns.color_palette('dark') 
            
            # plotting data on chart 
            font2 = {'family':'serif','color':'darkred','size':15}

            #sns.set(font_scale = 1.2)
            #plt.figure(figsize=(8,8))
            ax = plt.pie(data_pie, labels=keys, colors=colors, 
                explode=explode, autopct='%.0f%%', pctdistance=1.2, labeldistance=1.4, textprops={'fontsize':20, 'weight':'bold'}, shadow=True ) 
            
            sns.despine()
            sns.color_palette("rocket")
            locs, labels = plt.xticks()
            plt.rcParams["figure.figsize"] = (250, 150)
            font1 = {'family':'serif','color':'darkred','size':20}
            

            #plt.title("CODE", fontdict = font1)


            plt.setp(labels)
            plt.tight_layout()
            
            # plotting data on chart 
            #plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/torta_code.png",  transparent=True )
            plt.clf()
        except:
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/torta_code.png",  transparent=True )
            plt.clf()

        if len(data_pie) >0:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(290,200,str("COMBATES"))
        else:
            pdf.set_text_color(70,70,70)
            pdf.set_font('BebasNeue', '', 16)
            pdf.text(290,180,str("NO REGISTRA COMBATES"))




    