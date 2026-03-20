# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.s_c_resultados_mapa.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.s_c_resultados_mapa.models.funtions.componest.tablas import *
from tipo_docker.s_c_resultados_mapa.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import json
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            pass

    def divisiones_nombre(self, divisiones_lis, resultados, div):
        divisiones=[]
        divisiones = divisiones_lis
        for x in resultados:
                if x[div] not in divisiones:
                    divisiones.append(x[div])
        divisiones.sort()
        return divisiones

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
    def comparativo_mapa(self, pdf, fecha_inicial_u_l, fecha_final_u_l, filtro):

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


        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])


        res_calculo = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        pdf.ln(5) 
    
        # if filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
        #     mapa_filtrado(hechos_actual, filtro)
            
        # else:
        #     mapa_general(hechos_actual, filtro)


        # pdf.set_fill_color(193, 30, 38)
        # pdf.rounded_rect(65, 26, 115, 12, 1,'D', '1234')
        # pdf.set_text_color(0,0,0)
        # pdf.set_font('Arial', 'B', 10)
        # pdf.text(70,30,"FECHA INFORMACIÓN")
        # pdf.set_font('Arial', 'B', 8)
        # pdf.text(70,33.5,fecha_titulo)
        # pdf.text(70,37,fecha_titulo_dos)

        # print(type(hechos_actual))
        # print(type(res_calculo[98]))


        mapa_general(res_calculo[98], filtro) 

        # ruta = filtro[15] 

        mapa  = '{}static/img/img_mapas/mapa_resaltante.png'.format(filtro[15])
        # mapa_fondo  = '{}static/img/img_mapas/mapa_fondo.png'.format(filtro[15])

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        # pdf.image(mapa_fondo,13,18.7,162.1,199)
        pos_x = -83
        pos_y = -47
        ancho = 270
        alto = 295

        pdf.image(mapa,pos_x,pos_y,ancho,alto)
        pdf.image(rosa_nautica,100, 35, 25, 25)

   
        #pdf.image(label_eventos,5, 175, 60, 15)

        #convenciones 
        pdf.set_fill_color(255, 255, 255)
        pdf.set_draw_color(40, 40, 40)
        pdf.rounded_rect(3, 173, 29, 35, 1,'DF', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 8.5)
        pdf.text(4,177,"CONCENTRACIÓN")
        pdf.text(4,180.5,"DE EVENTOS")
        pdf.set_font('Arial', 'B', 7.5)
        # pdf.text(10,42.5,fecha_titulo_tres)
        pdf.text(10,185,"81%  A 100 %")
        pdf.text(10,190, "61%  A 80 %")
        pdf.text(10,195, "41%  A 60 %")
        pdf.text(10,200, "21%  A 40 %")
        pdf.text(10,205, "1%  A 20 %")

        img = '{}static/img/img_mapas/100.png'.format(filtro[15]) 
        pdf.image(img,5, 183, 3, 3)
        img = '{}static/img/img_mapas/80.png'.format(filtro[15]) 
        pdf.image(img,5, 188, 3, 3)
        img = '{}static/img/img_mapas/60.png'.format(filtro[15]) 
        pdf.image(img,5, 193, 3, 3)
        img = '{}static/img/img_mapas/40.png'.format(filtro[15]) 
        pdf.image(img,5, 198, 3, 3)
        img = '{}static/img/img_mapas/20.png'.format(filtro[15]) 
        pdf.image(img,5, 203, 3, 3)


        # pdf.ln(5)

        pdf.cell(-5)
        fill = True
        #cabecera tabla
        divisiones = []

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[0], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[1], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[2], 1)
        

        if filtro[17] == "sin_delco":
            divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[61], 1)
        else:
             divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[3], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[4], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[5], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[6], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[7], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[8], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[9], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[10], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[11], 2)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[12], 2)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[13], 2)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[14], 2)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[15], 2)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[16], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[17], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[18], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[19], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[20], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[21], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[22], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[23], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[24], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[25], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[26], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[27], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[28], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[29], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[33], 1)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[35], 2)
        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[40], 1)

        divisiones = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo[93], 1)



        valor_0 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 0,  "NO") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 1,  "NO") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 2,  "NO") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 4,  "SI") #funcion para filtar el spoa

                # print(filtro[17])
        if filtro[17] == "sin_delco":
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 61, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        else:
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 3, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        # print(divisiones)
        numero = encabezado_coe(pdf, fill, divisiones)
        if valor_0[0] or valor_1[0] or valor_2[0] or valor_calculado[0] or valor_4[0]:
        #separador
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA AMENAZA" , numero)
        #tabla de resultados
        #estadistica
    
        tabla_boletin_coe(pdf, valor_0[0], "MENORES RECUPERADOS", divisiones)
        tabla_boletin_coe(pdf, valor_1[0], "PRESENTACIÓN VOLUNTARIA", divisiones)
        tabla_boletin_coe(pdf, valor_2[0], "SOMETIMIENTOS", divisiones)
        # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        tabla_boletin_coe(pdf, valor_calculado[0], "CAPTURAS", divisiones)
        tabla_boletin_coe(pdf, valor_4[0], "MDOM", divisiones)


        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 6,  "SI") #funcion para filtar el spoa

        if valor_5[0] or valor_6[0]:
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A PROPIAS TROPAS" , numero)

        tabla_boletin_coe(pdf, valor_5[0], "ASESINADOS", divisiones)
        tabla_boletin_coe(pdf, valor_6[0], "HERIDOS", divisiones)


        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa

        if valor_7[0] or valor_8[0]  or valor_9[0]  or valor_10[0]:
            separador_cuadro_coe(pdf, fill, "MATERIAL DE GUERRA" , numero)

        tabla_boletin_coe(pdf, valor_7[0], "ARMAS DE LARGO ALCANCE", divisiones)
        tabla_boletin_coe(pdf, valor_8[0], "ARMAS DE CORTO ALCANCE", divisiones)
        tabla_boletin_coe(pdf, valor_9[0], "ARMAS DE ACOMPAÑAMIENTO", divisiones)
        tabla_boletin_coe(pdf, valor_10[0], "MUNICIONES", divisiones)


        if res_calculo[11] or res_calculo[12]  or res_calculo[13]  or res_calculo[14]:
            separador_cuadro_coe(pdf, fill, "COMBATES" , numero)
        tabla_boletin_coe_hechos(pdf, res_calculo[11], "COMBATES POSITIVOS", divisiones)
        tabla_boletin_coe_hechos(pdf, res_calculo[12], "COMBATES NEGATIVOS", divisiones)
        tabla_boletin_coe_hechos(pdf, res_calculo[13], "COMBATES SIN RESULTADOS", divisiones)
        tabla_boletin_coe_hechos(pdf, res_calculo[14], "TOTAL DE COMBATES", divisiones)

        if res_calculo[15] or res_calculo[16]  or res_calculo[17]  or res_calculo[18] or res_calculo[19] or res_calculo[20]:
            separador_cuadro_coe(pdf, fill, "MATERIAL DE EXPLOSIVOS" , numero)

        tabla_boletin_coe_hechos(pdf, res_calculo[15], "NEUTRALIZACIÓN TERRORISTA", divisiones)
        tabla_boletin_coe(pdf, res_calculo[16], "A.E", divisiones)
        tabla_boletin_coe(pdf, res_calculo[17], "MAP(Mina Anti Persona)", divisiones)
        tabla_boletin_coe(pdf, res_calculo[18], "EXPLOSIVOS kg", divisiones)
        tabla_boletin_coe(pdf, res_calculo[19], "CORDÓN DETONANTE m", divisiones)
        tabla_boletin_coe(pdf, res_calculo[20], "MECHA LENTA m", divisiones)

        valor_21 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_22 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_23 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_24 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_25 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_26 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_27 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
        valor_28 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_29 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa

        if valor_21[0] or valor_22[0] or valor_23[0] or valor_24[0] or valor_25[0] or valor_26[0] or valor_27[0] or valor_28[0] or valor_29[0]:
            separador_cuadro_coe(pdf, fill, "NARCOTRÁFICO" , numero)
        tabla_boletin_coe(pdf, valor_21[0], "COCAÍNA Kg", divisiones)
        tabla_boletin_coe(pdf, valor_22[0], "MARIHUANA Kg ", divisiones)
        tabla_boletin_coe(pdf, valor_23[0], "PBC Kg ", divisiones)
        tabla_boletin_coe(pdf, valor_24[0], "LAB. CLORHIDRATO DE COCAINA", divisiones)
        tabla_boletin_coe(pdf, valor_25[0], "LAB. PASTA O BASE DE COCA", divisiones)
        tabla_boletin_coe(pdf, valor_26[0], "SEMILLEROS", divisiones)
        tabla_boletin_coe(pdf, valor_27[0], "MATA(S) DE COCA EN SEMILLERO", divisiones)
        tabla_boletin_coe(pdf, valor_28[0], "INSUMOS LIQUIDOS Gal", divisiones) 
        tabla_boletin_coe(pdf, valor_29[0], "INSUMOS SOLIDOS Kg ", divisiones)

        tabla_boletin_coe(pdf, res_calculo[46], "DEPÓSITO ILEGAL ", divisiones)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        if valor[0] or res_calculo[35] or res_calculo[40]:
            separador_cuadro_coe(pdf, fill, "ECONOMÍAS ILÍCITAS" , numero)
        
        tabla_boletin_coe(pdf, valor[0], "CAPTURAS MINERIA ", divisiones)
        tabla_boletin_coe_hechos(pdf, res_calculo[35], "EIYM", divisiones)
        tabla_boletin_coe(pdf, res_calculo[40], "UPM ILEGAL ", divisiones)
        
        # tabla_boletin_coe(pdf, res_calculo[42], "LIBERADOS ", filtro)
        # tabla_boletin_coe(pdf, res_calculo[43], "RESCATADOS", filtro)
        if res_calculo[93]:
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA INFRAESTRUCTURA CRÍTICA" , numero)
        tabla_boletin_coe(pdf, res_calculo[93], "AFECTACIÓN A OLEODUCTO ", divisiones)
        
        # pdf.ln()

        
        # pdf.cell(-5)
        # fill = True
        # #cabecera tabla
        # encabezado_coe(pdf, fill)
        




        # separador_cuadro_coe(pdf, fill, "PLAN AMAZONÍA")
        # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa
        # tabla_boletin_coe(pdf, valor[0], "CAPTURAS PLAN AMAZONIA ")
        # tabla_boletin_coe(pdf, res_calculo[31], "PLANTULAS SEMBRADAS ")
        # tabla_boletin_coe(pdf, res_calculo[32], "MADERA INCAUTADA ")
        # tabla_boletin_coe(pdf, res_calculo[63], "ANIMALES INCAUTADOS ")

        # separador_cuadro_coe(pdf, fill, "MINERÍA ILEGAL")
        # 
        # 
        # tabla_boletin_coe(pdf, res_calculo[34], "MENORES R. MINERIA ")
        
        # tabla_boletin_coe(pdf, res_calculo[36], "EXCAVADORA(S) ")
        # tabla_boletin_coe(pdf, res_calculo[37], "RETROEXCAVADORA(S)  ")
        # tabla_boletin_coe(pdf, res_calculo[38], "MAQUINARIA PESADA ")
        # tabla_boletin_coe(pdf, res_calculo[39], "BULDOCER(ES)  ")
        
        # tabla_boletin_coe(pdf, res_calculo[41], "DRAGA(S)")
        # tabla_boletin_coe(pdf, res_calculo[65], "COLTAN KG")

        # separador_cuadro_coe(pdf, fill, "ECONOMÍAS ILÍCITAS")

        # tabla_boletin_coe(pdf, res_calculo[44], "VÁLVULAS")
        # tabla_boletin_coe(pdf, res_calculo[45], "REFINERIAS ")

        # separador_cuadro_coe(pdf, fill, "DEPÓSITOS")
        # 