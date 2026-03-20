# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.y_f_resultados_diseo_diario.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.y_f_resultados_diseo_diario.models.funtions.componest.tablas import *
from flask import json
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


    # cuadro de resultados resaltantes tamaño oficio
    def resultados_resaltantes_pdf_oficio(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf, dato):


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

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)

        resultados = conexion_pos.comando_query(query[0])
        hechos = conexion_pos.comando_query(query[1])
        erradicacion = conexion_pos.comando_query(query[2])
        # print(query[2])
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        pdf.set_line_width(0.5)

        posicion_inicial =0
        posicion_inicial_linea =45
        posicion_inicial = cuadro_menores_edad_ofico(pdf, res_calculo[0])

        
        if res_calculo[0] != 0 :

            #---------------------------------
            pdf.set_draw_color(140, 140, 140)
            pdf.set_line_width(0.3)
            lineas = posicion_inicial_linea + (posicion_inicial-6)
            # a = posicion_inicial_linea
            # while a < lineas:
            #     pdf.line(33, a+1, 33, a+2)
            #     a = a+2
            pdf.set_line_width(0.5)
            pdf.set_draw_color(0, 0, 0)
            #---------------------------------


            
            if lineas == 44:
                pdf.line(33, posicion_inicial_linea, 33, lineas+6)
                pdf.line(53, posicion_inicial_linea-5, 53, lineas+6)
                pdf.line(4.7, posicion_inicial_linea-5, 4.7, lineas+6)
                posicion_inicial = posicion_inicial + 5
            else:
                pdf.line(33, posicion_inicial_linea, 33, lineas)
                pdf.line(53, posicion_inicial_linea-5, 53, lineas)
                pdf.line(4.7, posicion_inicial_linea-5, 4.7, lineas)
                posicion_inicial = posicion_inicial
        


        posicion_inicial_rme =0
        datos_res =[res_calculo[1],res_calculo[2],res_calculo[3],res_calculo[4]]
        posicion_inicial_rme = cuadro_enemigo_afectaciones_oficio(pdf, posicion_inicial, datos_res)

        #--------------------------------------------
        pdf.set_line_width(0.3)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(30, 94, 79)
        pdf.rounded_rect(80, 33.5, 150, 6, 1,'F', '1234')      
        pdf.set_font('Arial', 'B', 12) 
        pdf.set_text_color(255, 255, 255)
        pdf.text(120, 38, "AFECTACIONES A LA AMENAZA" )
        pdf.set_text_color(0,0,0)
        #--------------------------------------------
        # pdf.text(210, 200, "Oficial Centro de Operaciones de Ejército (Entrante) " )

        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = posicion_inicial_linea + (posicion_inicial_rme-6)
        # a = posicion_inicial_linea
        # while a < lineas:
        #     pdf.line(83, a+1, 83, a+2)
        #     pdf.line(118, a+1, 118, a+2)
        #     pdf.line(149, a+1, 149, a+2)
        #     pdf.line(182, a+1, 182, a+2)
        #     pdf.line(215, a+1, 215, a+2)
        #     a = a+2
        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)

            #---------------------------------
                
        if lineas == 44:
            pdf.line(82, posicion_inicial_linea-5, 82, lineas+6)
            pdf.line(117, posicion_inicial_linea-5, 117, lineas+6)
            pdf.line(149, posicion_inicial_linea-5, 149, lineas+6)
            pdf.line(182, posicion_inicial_linea-5, 182, lineas+6)
            pdf.line(215, posicion_inicial_linea-5, 215, lineas+6)
        
            pdf.line(54.7, posicion_inicial_linea-5, 54.7, lineas+6)
            pdf.line(248.2, posicion_inicial_linea-5, 248.2, lineas+6)
            posicion_inicial_rme = posicion_inicial_rme + 5
        else:

            pdf.line(83, posicion_inicial_linea-5, 83, lineas+1)
            pdf.line(117, posicion_inicial_linea-5, 117, lineas+1)
            pdf.line(149, posicion_inicial_linea-5, 149, lineas+1)
            pdf.line(182, posicion_inicial_linea-5, 182, lineas+1)
            pdf.line(215, posicion_inicial_linea-5, 215, lineas+1)
        
            pdf.line(54.7, posicion_inicial_linea-5, 54.7, lineas+1)
            pdf.line(248.7, posicion_inicial_linea-5, 248.7, lineas+1)
            posicion_inicial_rme = posicion_inicial_rme
        

        datos_res_afectaciones = [res_calculo[5], res_calculo[6], res_calculo[93], res_calculo[94]]
        pocision= 0
        pocision = cuadro_afectaciones_tropas_combate_oficio (pdf, posicion_inicial_rme, datos_res_afectaciones )
        
        #--------------------------------------------
        pdf.set_line_width(0.3)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(193, 31, 37)
        pdf.rounded_rect(255, 33.5, 93, 6, 1,'F', '1234')      
        pdf.set_font('Arial', 'B', 12) 
        pdf.set_text_color(255, 255, 255)
        pdf.text(265, 38, "AFECTACIONES PROPIAS TROPAS" )
        pdf.set_text_color(0,0,0)
            #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
    
        if pocision == 5:
            lineas = posicion_inicial_linea + pocision-2
        else:lineas = posicion_inicial_linea + pocision
        # a = posicion_inicial_linea
        # while a < lineas:
        #     pdf.line(278, a+1, 278, a+2)
        #     pdf.line(303, a+1, 303, a+2)
        #     pdf.line(328, a+1, 328, a+2)
        #     a = a+2
        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)

        #---------------------------------
    
        if pocision == 0:
            pdf.line(278, posicion_inicial_linea-5, 278, posicion_inicial_linea+pocision)
            pdf.line(303, posicion_inicial_linea-5, 303, posicion_inicial_linea+pocision)
            pdf.line(328, posicion_inicial_linea-5, 328, posicion_inicial_linea+pocision)
        
            pdf.line(250, posicion_inicial_linea-5, 250, posicion_inicial_linea+pocision)
            pdf.line(353.2, posicion_inicial_linea-5, 353.2, posicion_inicial_linea+pocision)
            
        else:
            pdf.line(278, posicion_inicial_linea-5, 278, posicion_inicial_linea+pocision)
            pdf.line(303, posicion_inicial_linea-5, 303, posicion_inicial_linea+pocision)
            pdf.line(328, posicion_inicial_linea-5, 328, posicion_inicial_linea+pocision)
        
            pdf.line(250, posicion_inicial_linea-5, 250, posicion_inicial_linea+pocision)
            pdf.line(353.2, posicion_inicial_linea-5, 353.2, posicion_inicial_linea+pocision)
            
        
        if pocision == 0:
            if posicion_inicial_rme == 0:

                if posicion_inicial == 0:
                    numero = 60
                else:
                    pdf.ln(-posicion_inicial)
                    numero = 60
            else:
                pdf.ln(-posicion_inicial_rme)
                numero = 60
        else:

            pdf.ln(-pocision)
            numero = 60

            
        pdf.ln(numero)
        
    
        #separador
        pdf.set_line_width(1)
        pdf.line(4, 90, 353, 90)
        pdf.set_line_width(0.3)

        #calculo por grupos de resultados 
        pos = 98
        pos_vert = [22,65,10, 18, 115,30]
        # pdf.ln(30)
        if res_calculo[7] or res_calculo[8] or res_calculo[9]  or res_calculo[10] :

            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "MATERIAL DE GUERRA")
            
            # pos = grupo_result_resal(pdf, pos)
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Largo Alcance", res_calculo[7], 18, 'fusil.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Corto Alcance", res_calculo[8], 18, 'pistola.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Acompañamiento", res_calculo[9], 18, 'mortero.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Municiones", res_calculo[10], 18, 'municion.jpg', filtro)
            pos = pos + 4
            pdf.ln(10)

        if res_calculo[15] or res_calculo[16] or res_calculo[17] or res_calculo[18]  or res_calculo[19] or res_calculo[20]:
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "MATERIAL DE EXPLOSIVOS")

            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización AE", res_calculo[16], 18, 'ae1.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización MAP", res_calculo[17], 18, 'map.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Explosivos Destruidos Kg", res_calculo[18], 18, 'esplosivos.jpg', filtro)

            pos = grupo_result_resal(pdf, pos_vert, pos, "Cordón Detonante m", res_calculo[19], 18, 'cordon.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Mecha Lenta m ", res_calculo[20], 18, 'mecha.jpg', filtro)
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización Terrorista", res_calculo[15], 14, 'neutralizacion.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)

          
        if res_calculo[95] or res_calculo[96] :
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "ATAQUES DRONES")

            pos = grupo_result_resal(pdf, pos_vert, pos, "Ataque UAS", res_calculo[95], 18, 'DRONS_new.png', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "UAS Derribado / Neutralizado", res_calculo[96], 18, 'DRONS_2_new.png', filtro)


            pos = pos + 4
            pdf.ln(10)
   
             
        if res_calculo[11] or res_calculo[12] or res_calculo[13] or res_calculo[14] :
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "COMBATES")

            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates con Resultados", res_calculo[11], 14, 'combate.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates sin Resultados", res_calculo[13], 14, 'combate_rs.jpg', filtro)       
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates Negativos", res_calculo[12], 14, 'combate_neg.jpg', filtro)      
            pos = grupo_result_resal(pdf, pos_vert, pos, "Total de Combates", res_calculo[14], 14, 'combate.jpg', filtro)

        pdf.set_line_width(0.3)
        pdf.line(120, 95, 120, 205)
        
        
        #calculo por grupos de resultados 
        pos = 98
        pos_vert = [134,75,123, 130, 239,30]
        

        y = pdf.get_y()
        if y == 100.00125:
            pdf.ln(-numero)
            pdf.ln(60)
        else: 
            x = 100.00125 - y
            numero =  x 
            pdf.ln(numero)

        if res_calculo[21] or res_calculo[22] or res_calculo[23] or res_calculo[24] or res_calculo[25] or res_calculo[26] or res_calculo[27] or res_calculo[28] or res_calculo[29] or res_calculo[47] or res_calculo[48]:
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "NARCOTRÁFICO")
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Cocaína Kg", res_calculo[21], 18, 'cocaina.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Cocaína en Proceso Gal", res_calculo[47], 18, 'cocaina_pbc.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Marihuana Kg", res_calculo[22], 18, 'marihuana.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Pasta Base de Coca Kg", res_calculo[23], 18, 'pbc.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "P.B.C en Proceso Gal", res_calculo[48], 18, 'pbc_proceso.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Laboratorios de Cocaína", res_calculo[24], 18, 'lab_cocaina.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Laboratorios de PBC", res_calculo[25], 18, 'lab_pbc.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Semilleros", res_calculo[26], 18, 'semilleros.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Matas de Coca en Semilleros", res_calculo[27], 18, 'erradicacion.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Insumos Iiquidos Gal", res_calculo[28], 18, 'liquidos.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Insumos Solidos Kg", res_calculo[29], 18, 'solidos.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)
            
        if res_calculo[30] or res_calculo[31] or res_calculo[32] or res_calculo[63] :
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "PROTECCIÓN AL MEDIO AMBIENTE")

            pos = grupo_result_resal(pdf, pos_vert, pos, "Capturas LOE Amazonía", res_calculo[30], 18, 'capturas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Plantulas Sembradas", res_calculo[31], 18, 'plantulas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Incautacion Madera m3", res_calculo[32], 18, 'madera.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Especies Animales Incautados", res_calculo[63], 18, 'loro.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)
            
        if res_calculo[97] or res_calculo[98] or res_calculo[99]  :
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "OPERACIONES CIBERESPACIO")
           
            pos = grupo_result_resal(pdf, pos_vert, pos, "Incidente Cibernético", res_calculo[97], 18, 'incidente_cibernetico_new.png', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Ataque Cibernético Contenido", res_calculo[98], 18, 'ataque_cibernetico_new.png', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Ataque Cibernético Materializado", res_calculo[99], 18, 'incidente_cibernetico_materializado_new.png', filtro)


            pos = pos + 4

        pdf.set_line_width(0.3)
        pdf.line(245, 95, 245, 205)
        
        #calculo por grupos de resultados 
        pos = 98
        pos_vert = [258,60,247, 254, 348,30]

        y = pdf.get_y()
        if y == 100.00125:
            pdf.ln(-numero)
            pdf.ln(60)
        else: 
            x = 100.00125 - y
            numero =  x 
            pdf.ln(numero)

        if res_calculo[33] or res_calculo[34] or res_calculo[35] or res_calculo[36] or res_calculo[37] or res_calculo[38] or res_calculo[39] or res_calculo[40] or res_calculo[41]:
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "MINERÍA ILEGAL")

            # pos = pos + 6

            pos = grupo_result_resal(pdf, pos_vert, pos, "Capturas", res_calculo[33], 18, 'capturas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Menores Recuperados", res_calculo[34], 18, 'rme.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "EIYM Minas Ilegales", res_calculo[35], 14, 'ejc.jpg', filtro)
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Excavadoras", res_calculo[36], 18, 'excavadoras.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Retroexcavadoras", res_calculo[37], 18, 'retroexcavadoras.jpg', filtro)
            # pos = grupo_result_resal(pdf, pos_vert, pos, "Maquinaria Pesada", res_calculo[38], 18, 'maquinaria.jpg', filtro)
            # pos = grupo_result_resal(pdf, pos_vert, pos, "Tractor con Uruga", res_calculo[39], 18, 'buldocer.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Unidad Producción Minera", res_calculo[40], 18, 'upm.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Dragas", res_calculo[41], 18, 'dragas.jpg', filtro)
            
        # # claculo_mapa_dos(pdf, res_calculo_ante[36], res_calculo_act[36], "EXCAVADORA(S)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[37], res_calculo_act[37], "RETROEXCAVADORA(S)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[38], res_calculo_act[38], "MAQUINARIA PESADA",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18, 175)


            maquinaria_anctual = [res_calculo[38], res_calculo[39]]

            # claculo_maquinaria_amarialla_mapa_dos(pdf, maquinaria_anterior, maquinaria_anctual, "MAQUINARIA AMARILLA",1, 7, 18, 175)

            coltan =claculo_maquinaria_amarialla_mapa(pdf,  maquinaria_anctual,  18)

            pos = grupo_result_resal_dos(pdf, pos_vert, pos, "Maquinaria Pesada", coltan, 18, 'buldocer.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Coltan KG", res_calculo[65], 18, 'coltan.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)
        
        if res_calculo[42] or res_calculo[43] or res_calculo[44] or res_calculo[45] or res_calculo[62]:
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "ECONOMIAS ILICITAS")

            pos = grupo_result_resal(pdf, pos_vert, pos, "Liberados", res_calculo[42], 18, 'cadena.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Rescatados", res_calculo[43], 18, 'cadena2.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Válvulas Ilícitas Destruidas", res_calculo[44], 18, 'valvula.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Refinerias Ilegales Destruidas", res_calculo[45], 18, 'refineria.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combustible Incautado Gal", res_calculo[62], 18, 'combustible.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)

        if res_calculo[46] :
            
            pos = titulos_resultados_dia_diseo(pdf, pos_vert, pos, "DEPÓSITO ILEGAL")
            pos = grupo_result_resal(pdf, pos_vert, pos, "Depósito Ilegal", res_calculo[46], 18, 'deposito.jpg', filtro)
            
        pdf.set_line_width(0.5)
        pdf.line(4, 209, 353, 209)
        pdf.set_line_width(0.3)

    def resultados_diarios_divisiones(self, pdf, fecha_inicial_u_l, fecha_final_u_l, filtro, fecha_titulo_dos, dato):
        

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
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)

        #--------------------------------------------
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(193, 30, 38)
        pdf.rounded_rect(280, 13, 50, 15, 1,'D', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 12)
        pdf.text(281,17,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 11)
        pdf.text(281,21,fecha_titulo_dos)
   
        #--------------------------------------------
        
        posiciones = [52, 17,14,7]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV01", posiciones)
        posiciones = [52, 107, -numero, 97]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV02", posiciones)   
        posiciones = [52, 198, -numero, 187]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV03", posiciones)
        posiciones = [52, 286, -numero, 275]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV04", posiciones)
        y = pdf.get_y()
        if y == 89.00125:
            numero =  20
        else: 
            x = 89.00125 - y
            numero =  x + 20
        # print(y)
            
        posiciones = [112, 17, numero, 7]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV05", posiciones)
        posiciones = [112, 107, -numero, 97]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV06", posiciones)    
        posiciones = [112, 198, -numero, 187]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV07", posiciones)               
        posiciones = [112, 286, -numero, 275]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DIV08", posiciones)

        y = pdf.get_y()
        if y == 149.00125:
            numero =  22
        else: 
            x = 149.00125 - y
            numero =  x + 22
        # print(y)          
        posiciones = [174, 17, numero, 7]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "DAVAA", posiciones)
        posiciones = [174, 107, -numero, 97]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "FUTCO", posiciones)    
        posiciones = [174, 198, -numero,187]
        numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "FTCEC", posiciones)               
        posiciones = [174, 286, -numero, 275]
        numero = resultados_diarios_divisiones_coe_tropas(pdf, res_calculo_act, "DIVFE", posiciones, filtro, hechos_actual)

        # posiciones = [174, 286, -numero, 275]
        # numero = resultados_diarios_divisiones_coe(pdf, res_calculo_act, "TREJC", posiciones)

    # cuadro de resultados resaltantes comparativos
    def resultados_resaltantes_pdf_comparativo(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, dato):


        if filtro[29] == "com_metas_narcotrafico":
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
                
            print(cocaina_ejc)
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

        pdf.set_line_width(0.5)
        #--------------------------------------------
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(217, 217, 217)
        pdf.rounded_rect(280, 13, 53, 15, 1,'DF', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 11)
        pdf.text(281,17,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 9)
        pdf.text(281,21,fecha_titulo)
        pdf.text(281,25,fecha_titulo_dos)
        #--------------------------------------------
        
        # encabezado_comparativo_mapa(pdf, True, anio_act, anio_ant)

        pdf.set_font('Arial', 'B', 10) 
        pdf.set_fill_color(106, 78, 64)
        pdf.rounded_rect(2, 34, 48, 5, 1,'F', '1234')
        pdf.set_text_color(255, 255, 255)
        pdf.text(3, 38, "MENORES RECUPERADOS" )

        pdf.set_fill_color(30, 94, 79)
        pdf.rounded_rect(88, 29, 118, 5, 1,'F', '1234')
        pdf.text(115, 33, "AFECTACIONES  A LA AMENAZA" )

        posicion_inicial =0
        posicion_inicial_linea =40

        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 0, "NO") #funcion para filtar el spoa
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 0, "NO") #funcion para filtar el spoa
        
        posicion_inicial = cuadro_menores_edad_comparativo(pdf, valor_calculado_ant[0], valor_calculado_act[0], filtro, anio_act, anio_ant)
        # print(posicion_inicial)
        pdf.set_line_width(0.5)
        pdf.line(2, posicion_inicial_linea, 50, posicion_inicial_linea)
        if posicion_inicial[1] != 0 or posicion_inicial[2] != 0:

            posicion_inicial_linea_f =  posicion_inicial_linea + (posicion_inicial[0]-5)

            pdf.line(2, posicion_inicial_linea_f, 50, posicion_inicial_linea_f)

            #---------------------------------
            pdf.set_draw_color(0, 0, 0)
            pdf.set_line_width(0.1)
            lineas = posicion_inicial_linea + (posicion_inicial[0]-6)
            a = posicion_inicial_linea
            while a < lineas:
                # pdf.set_draw_color(0, 0, 0)
                # pdf.line(16.2, a+1, 16.2, a+2)
                pdf.set_draw_color(180, 180, 180)
                pdf.line(27, a+1, 27, a+2)
                pdf.line(38, a+1, 38, a+2)
                # pdf.line(182, a+1, 182, a+2)
                # pdf.line(215, a+1, 215, a+2)
                a = a+2
            pdf.set_line_width(0.5)
            pdf.set_draw_color(0, 0, 0)
            #---------------------------------

            # pdf.line(2, posicion_inicial_linea, 2, posicion_inicial_linea_f)
            # pdf.line(16.2, posicion_inicial_linea, 16.2, posicion_inicial_linea_f)
            # pdf.line(50, posicion_inicial_linea, 50, posicion_inicial_linea_f)
            pdf.line(16.2, posicion_inicial_linea, 16.2, lineas)
            pdf.line(2, posicion_inicial_linea, 2, lineas)
            pdf.line(50, posicion_inicial_linea, 50, lineas)
                # posicion_inicial = posicion_inicial + 5


        # posicion_inicial_rme =0
        datos_res_actu =[res_calculo_act[1],res_calculo_act[2],res_calculo_act[3],res_calculo_act[4]]
        datos_res_ante =[res_calculo_ante[1],res_calculo_ante[2],res_calculo_ante[3],res_calculo_ante[4]]



        posicion_inicial_rme = cuadro_enemigo_afectaciones_comparativo(pdf, posicion_inicial[0], datos_res_ante, datos_res_actu, filtro, anio_act, anio_ant)
        
        pdf.set_line_width(0.5)
        posicion_inicial_linea =35
        pdf.set_draw_color(0, 0, 0)
        pdf.line(52, posicion_inicial_linea, 238, posicion_inicial_linea)
        if posicion_inicial_rme[1] != 0 or posicion_inicial_rme[2] != 0:
            posicion_inicial_linea_f =  posicion_inicial_linea + posicion_inicial_rme[0]

            pdf.line(52, posicion_inicial_linea_f, 238, posicion_inicial_linea_f)
            # pdf.line(52, posicion_inicial_linea, 52, posicion_inicial_linea_f)

            # pdf.line(238, posicion_inicial_linea, 238, posicion_inicial_linea_f)

            #---------------------------------
            pdf.set_draw_color(0, 0, 0)
            pdf.set_line_width(0.1)
            lineas = posicion_inicial_linea + (posicion_inicial_rme[0]-2)
            # a = posicion_inicial_linea
            # while a < lineas:
            #     pdf.set_draw_color(0, 0, 0)
            #     pdf.line(66, a+1, 66, a+2)
            #     pdf.line(100.5, a+1, 100.5, a+2)
            #     pdf.line(135.1, a+1, 135.1, a+2)
            #     pdf.line(169.6, a+1, 169.6, a+2)
            #     pdf.line(204.2, a+1, 204.2, a+2)
            #     a = a+2
            # pdf.set_line_width(0.5)
            # pdf.set_draw_color(0, 0, 0)
            # #---------------------------------

            #---------------------------------
            pdf.set_draw_color(0, 0, 0)
            pdf.set_line_width(0.1)
            posicion_inicial_linea =40
            lineas = posicion_inicial_linea + (posicion_inicial_rme[0]-7)
            a = posicion_inicial_linea
            while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)

                pdf.line(77.2, a+1, 77.2, a+2)
                pdf.line(88.45, a+1, 88.45, a+2)

                pdf.line(111.8, a+1, 111.8, a+2)
                pdf.line(122.9, a+1, 122.9, a+2)

                pdf.line(146.2, a+1, 146.2, a+2)
                pdf.line(157.4, a+1, 157.4, a+2)

                pdf.line(180.7, a+1, 180.7, a+2)
                pdf.line(191.9, a+1, 191.9, a+2)

                pdf.line(215.2, a+1, 215.2, a+2)
                pdf.line(226.6, a+1, 226.6, a+2)
                
                a = a+2
            pdf.set_line_width(0.5)
            pdf.set_draw_color(0, 0, 0)
            #---------------------------------
            pdf.line(66, posicion_inicial_linea-5, 66, lineas+2)
            pdf.line(100.5, posicion_inicial_linea-5, 100.5, lineas+2)
            pdf.line(135.1, posicion_inicial_linea-5, 135.1, lineas+2)
            pdf.line(169.6, posicion_inicial_linea-5, 169.6, lineas+2)
            pdf.line(204.2, posicion_inicial_linea-5, 204.2, lineas+2)
                    
            pdf.line(52, posicion_inicial_linea-5, 52, lineas+2)
            pdf.line(238.2, posicion_inicial_linea-5, 238.2, lineas+2)

            
        pdf.set_font('Arial', 'B', 12)
        pdf.set_text_color(255, 255, 255)
        
        pdf.set_fill_color(193, 31, 37)
        pdf.rounded_rect(254, 29, 88, 5, 1,'F', '1234')
        pdf.text(265, 33, "AFECTACIONES PROPIAS TROPAS" )
        pdf.set_text_color(0, 0, 0)
        
        datos_res_afectaciones_act = [res_calculo_act[5], res_calculo_act[6], res_calculo_act[93], res_calculo_act[94]]
        datos_res_afectaciones_ant = [res_calculo_ante[5], res_calculo_ante[6], res_calculo_ante[93], res_calculo_ante[94]]

        posiscion_cero = cuadro_afectaciones_tropas_combate_comparativo (pdf, posicion_inicial_rme[0], datos_res_afectaciones_ant, datos_res_afectaciones_act, filtro, anio_act, anio_ant )
        posicion_inicial_linea =35
        pdf.set_line_width(0.5)
        pdf.line(240, posicion_inicial_linea, 354, posicion_inicial_linea)  

        if posiscion_cero[1] != "-" or posiscion_cero[2] != "-":
            posicion_inicial_linea_f =  posicion_inicial_linea + posiscion_cero[0] 
            pdf.line(240, posicion_inicial_linea_f, 354, posicion_inicial_linea_f)
                    #---------------------------------
            pdf.set_draw_color(0, 0, 0)
            pdf.set_line_width(0.1)
            lineas = posicion_inicial_linea + (posiscion_cero[0]-2)
            # a = posicion_inicial_linea
            # while a < lineas:
            #     pdf.set_draw_color(0, 0, 0)
            #     pdf.line(254.1, a+1, 254.1, a+2)
            #     pdf.line(287.5, a+1, 287.5, a+2)
            #     pdf.line(321, a+1, 321, a+2)
            #     a = a+2
            # pdf.set_line_width(0.5)
            # pdf.set_draw_color(0, 0, 0)
            #---------------------------------

            
            #---------------------------------

            pdf.set_line_width(0.1)
            posicion_inicial_linea =40
            lineas = posicion_inicial_linea + (posiscion_cero[0]-7)
            a = posicion_inicial_linea
            while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)

                pdf.line(264.6, a+1, 264.6, a+2)
                pdf.line(275.1, a+1, 275.1, a+2)

                pdf.line(297.9, a+1, 297.9, a+2)
                pdf.line(308.7, a+1, 308.7, a+2)

                pdf.line(331.4, a+1, 331.4, a+2)
                pdf.line(342.1, a+1, 342.1, a+2)

                a = a+2
            pdf.set_line_width(0.5)
            pdf.set_draw_color(0, 0, 0)
            #---------------------------------

            pdf.line(254.1, posicion_inicial_linea-5, 254.1, lineas+2)
            pdf.line(287.5, posicion_inicial_linea-5, 287.5, lineas+2)
            pdf.line(321, posicion_inicial_linea-5, 321, lineas+2)
                            
            pdf.line(240, posicion_inicial_linea-5, 240, lineas+2)
            pdf.line(354, posicion_inicial_linea-5, 354, lineas+2)
            # pdf.line(240, posicion_inicial_linea, 240, posicion_inicial_linea_f)

            # # pdf.line(170, posicion_inicial_linea, 170, posicion_inicial_linea_f)
            # # pdf.line(204.5, posicion_inicial_linea, 204.5, posicion_inicial_linea_f)
            # pdf.line(354, posicion_inicial_linea, 354, posicion_inicial_linea_f)
            
        #separador
        #pdf.set_line_width(1)
        #pdf.line(4, 95, 351, 95)
        pdf.set_line_width(0.3)

        #calculo por grupos de resultados 
        pos = 93
        #------------indentificacion de la lista -----------#
            # 0: imagen
        # 1: inicio celda
        # 2: tamaño celda texto
        # 3: tamaño celda numero
        # 4: tamaño celda porcentaje
        # 5: inicio linea punteada
        # 6: fin linea punteada
        # 7: altura linea punteada
        # 8: año anterior
        # 9: año actual
        # 10: porcentaje
        # 11: pocision triangulo
        # 12: ajuste altura porcentaje
        #------------indentificacion de la lista -----------#
        pos_vert = [3,1,45,22, 16,12,115,2, 63, 85, 107,100,2]


        pdf.ln(-posiscion_cero[0])
        pdf.ln(67)
        
   
        
        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "MATERIAL DE GUERRA", filtro, 105)
 
        pdf.ln(-8)
        pos = pos + 5
            # pos = grupo_result_resal(pdf, pos)
            # pdf.ln(-6)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 7, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Armas de Largo Alcance", res_calculo_ante[7], valor_calculado_act[0], 18, 'fusil.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 8, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Armas de Corto Alcance",res_calculo_ante[8], valor_calculado_act[0], 18, 'pistola.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 9, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Armas de Acompañamiento",res_calculo_ante[9], valor_calculado_act[0], 18, 'mortero.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 10, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Municiones",res_calculo_ante[10], valor_calculado_act[0], 18, 'municion.jpg', filtro, 1)
        
        pdf.set_line_width(0.5)
        x = pos-1.5
        pdf.line(pos_vert[0]+8,   pos-29, pos_vert[0]+8 , pos-3)
        pdf.line( x, pos-29, x , pos-3)
        pdf.line( 56, pos-24, 56 , pos-3)
        pdf.line( pos_vert[0]+8, pos-3, x , pos-3)

        
        posicion_inicial_linea =pos-29
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(77.5, a+1, 77.5, a+2)
                pdf.line(100, a+1, 100, a+2)

                a = a+2
        pos = pos + 3
        pdf.ln(8.5)

        
            
        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "MATERIAL DE EXPLOSIVOS", filtro, 105 )
        pos = pos + 5

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Neutralización AE",res_calculo_ante[16], res_calculo_act[16], 18, 'ae1.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Neutralización MAP",res_calculo_ante[17], res_calculo_act[17], 18, 'map.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Explosivos Destruidos Kg",res_calculo_ante[18], res_calculo_act[18], 18, 'esplosivos.jpg', filtro, 1)

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Cordón Detonante m",res_calculo_ante[19], res_calculo_act[19], 18, 'cordon.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Mecha Lenta m",res_calculo_ante[20], res_calculo_act[20], 18, 'mecha.jpg', filtro, 1)
            
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Neutra. Acción Terrorista",res_calculo_ante[15], res_calculo_act[15], 14, 'neutralizacion.jpg', filtro, 1)

        pdf.set_line_width(0.5)

        pdf.line(pos_vert[0]+8,   pos-39, pos_vert[0]+8 , pos-3)
        pdf.line( x, pos-39, x , pos-3)
        pdf.line( 56, pos-34, 56 , pos-3)
        pdf.line( pos_vert[0]+8, pos-3, x , pos-3)

        posicion_inicial_linea =pos-39
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(77.5, a+1, 77.5, a+2)
                pdf.line(100, a+1, 100, a+2)

                a = a+2
        pos = pos + 3
        pdf.ln(8.5)


        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "ATAQUE DRONES", filtro, 105 )
        pos = pos + 5
        
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Ataque UAS",res_calculo_ante[95], res_calculo_act[95], 18, 'DRONS_new.png', filtro, 1)

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "UAS Neutralizados",res_calculo_ante[96], res_calculo_act[96], 18, 'DRONS_2_new.png', filtro, 1)
        

        pdf.set_line_width(0.5)

        pdf.line(pos_vert[0]+8,   pos-19, pos_vert[0]+8 , pos-3)
        pdf.line( x, pos-19, x , pos-3)
        pdf.line( 56, pos-14, 56 , pos-3)
        pdf.line( pos_vert[0]+8, pos-3, x , pos-3)

        posicion_inicial_linea =pos-19
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(77.5, a+1, 77.5, a+2)
                pdf.line(100, a+1, 100, a+2)

                a = a+2
        pos = pos + 3
        pdf.ln(8.5)

        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "COMBATES", filtro, 105 )
        pos = pos + 5
        
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Combates con Resultados",res_calculo_ante[11], res_calculo_act[11], 14, 'combate.jpg', filtro, 1)

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Combates sin Resultados",res_calculo_ante[13], res_calculo_act[13], 14, 'combate_rs.jpg', filtro, -1)
                    
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Combates Negativos",res_calculo_ante[12], res_calculo_act[12], 14, 'combate_neg.jpg', filtro, -1)
                   
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Total de Combates",res_calculo_ante[14], res_calculo_act[14], 14, 'combate.jpg', filtro, 1)

        pdf.set_line_width(0.5)

        pdf.line(pos_vert[0]+8,   pos-29, pos_vert[0]+8 , pos-3)
        pdf.line( x, pos-29, x , pos-3)
        pdf.line( 56, pos-24, 56 , pos-3)
        pdf.line( pos_vert[0]+8, pos-3, x , pos-3)

        posicion_inicial_linea =pos-29
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(77.5, a+1, 77.5, a+2)
                pdf.line(100, a+1, 100, a+2)

                a = a+2
        pos = pos + 3
        pdf.ln(8.5)
        
        #calculo por grupos de resultados 
        pos = 93
        #------------indentificacion de la lista -----------#
        # 0: imagen
        # 1: inicio celda
        # 2: tamaño celda texto
        # 3: tamaño celda numero
        # 4: tamaño celda porcentaje
        # 5: inicio linea punteada
        # 6: fin linea punteada
        # 7: altura linea punteada
        # 8: año anterior
        # 9: año actual
        # 10: porcentaje
        # 11: pocision triangulo
        # 12: ajuste altura porcentaje
        #------------indentificacion de la lista -----------#

        pos_vert = [119,116,48,23, 16,128,235,2, 182, 204, 227,220,2, 3]

        
        pdf.ln(-pos-12)


        if filtro[29] != "com_metas_narcotrafico":
            titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "NARCOTRÁFICO", filtro, 110 )
        else:
             titulo_comparatibo_muñecos(pdf, pos_vert, pos, "META", anio_act, "NARCOTRÁFICO", filtro, 110 )

        pdf.ln(-8)
        pos = pos + 5     

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 21, "SI") #funcion para filtar el spoa
        if filtro[29] != "com_metas_narcotrafico":
            pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Cocaína Kg",res_calculo_ante[21], valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)
        else:
            pos = grupo_result_resal_comparativa_metas(pdf, pos_vert, pos, "Cocaína Kg",cocaina_ejc, valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 47, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Cocaína en Proceso Gal",res_calculo_ante[47], valor_calculado_act[0], 18, 'cocaina_pbc.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 22, "SI") #funcion para filtar el spoa
        if filtro[29] != "com_metas_narcotrafico":
            pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Marihuana Kg",res_calculo_ante[22], valor_calculado_act[0], 18, 'marihuana.jpg', filtro, 1)
        else:
            pos = grupo_result_resal_comparativa_metas(pdf, pos_vert, pos, "Marihuana Kg",marihuana_ejc, valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)
        
                
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 23, "SI") #funcion para filtar el spoa
        if filtro[29] != "com_metas_narcotrafico":
            pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Pasta Base de Coca Kg",res_calculo_ante[23], valor_calculado_act[0], 18, 'pbc.jpg', filtro, 1)
        else:
            pos = grupo_result_resal_comparativa_metas(pdf, pos_vert, pos, "Pasta Base de Coca Kg",pbc_ejc, valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)
        
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 48, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "P.B.C en Proceso Gal",res_calculo_ante[48], valor_calculado_act[0], 18, 'pbc_proceso.jpg', filtro, 1)
                
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 24, "SI") #funcion para filtar el spoa
        if filtro[29] != "com_metas_narcotrafico":
            pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Laboratorios de Cocaína",res_calculo_ante[24], valor_calculado_act[0], 18, 'lab_cocaina.jpg', filtro, 1)
        else:
            pos = grupo_result_resal_comparativa_metas(pdf, pos_vert, pos, "Laboratorios de Cocaína",lab_chl_ejc, valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)
        
                
        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 25, "SI") #funcion para filtar el spoa
        if filtro[29] != "com_metas_narcotrafico":
            pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Laboratorios de PBC",res_calculo_ante[25], valor_calculado_act[0], 18, 'lab_pbc.jpg', filtro, 1)
        else:
            pos = grupo_result_resal_comparativa_metas(pdf, pos_vert, pos, "Laboratorios de PBC",lab_pbc_ejc, valor_calculado_act[0], 18, 'cocaina.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 26, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Semilleros",res_calculo_ante[26], valor_calculado_act[0], 18, 'semilleros.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 27, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Matas de Coca Semilleros",res_calculo_ante[27], valor_calculado_act[0], 18, 'erradicacion.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 28, "SI") #funcion para filtar 
        
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Insumos Iiquidos Gal",res_calculo_ante[28], valor_calculado_act[0], 18, 'liquidos.jpg', filtro, 1)

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 29, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Insumos Solidos Kg",res_calculo_ante[29], valor_calculado_act[0], 18, 'solidos.jpg', filtro, 1)

        pdf.set_line_width(0.5)
        x = 237

        pdf.line(pos_vert[0]+7,   pos-64, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-64, x , pos-3)
        pdf.line( 170, pos-59, 170 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-64
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(197.5, a+1, 197.5, a+2)
                pdf.line(220, a+1, 220, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)
                
        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "MEDIO AMBIENTE", filtro, 110 )
        pos = pos + 5

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 30, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Capturas LOE Amazonía", res_calculo_ante[30], valor_calculado_act[0], 18, 'capturas.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Plantulas Sembradas", res_calculo_ante[31], res_calculo_act[31], 18, 'plantulas.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Incautacion Madera m3", res_calculo_ante[32], res_calculo_act[32], 18, 'madera.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Especies Animales Incautados", res_calculo_ante[63], res_calculo_act[63], 18, 'loro.jpg', filtro, 1)
        # pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Hectareas Recuperadas h", res_calculo_ante[30], res_calculo_act[30], 18, 'bosque.jpg', filtro, 1)

        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+7,   pos-29, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-29, x , pos-3)
        pdf.line( 175.5, pos-24, 175.5 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-29
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(197.5, a+1, 197.5, a+2)
                pdf.line(220, a+1, 220, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)

        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "OPE. CIBERESPACIO", filtro, 110 )
        pos = pos + 5

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Incidente Cibernético", res_calculo_ante[97], res_calculo_act[97], 18, 'incidente_cibernetico_new.png', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Ataque Cibernético", res_calculo_ante[98], res_calculo_act[98], 18, 'ataque_cibernetico_new.png', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Ataq Cibernético Materializado", res_calculo_ante[99], res_calculo_act[99], 18, 'incidente_cibernetico_materializado_new.png', filtro, 1)

        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+7,   pos-24, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-24, x , pos-3)
        pdf.line( 175.5, pos-19, 175.5 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-24
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(197.5, a+1, 197.5, a+2)
                pdf.line(220, a+1, 220, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)

        
        #calculo por grupos de resultados 
        pos = 117
        #------------indentificacion de la lista -----------#
        # 0: imagen
        # 1: inicio celda
        # 2: tamaño celda texto
        # 3: tamaño celda numero
        # 4: tamaño celda porcentaje
        # 5: inicio linea punteada
        # 6: fin linea punteada
        # 7: altura linea punteada
        # 8: año anterior
        # 9: año actual
        # 10: porcentaje
        # 11: pocision triangulo
        # 12: ajuste altura porcentaje
        #------------indentificacion de la lista -----------#

        pos_vert = [239,235.5,45,23, 16,248,351,1, 299, 321, 342,337,3]
        pdf.ln(-pos)   

        pos = pos-25
        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "MINERÍA ILEGAL", filtro ,107)
        pos = pos + 5

        valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 33, "SI") #funcion para filtar el spoa
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Capturas",res_calculo_ante[33],  valor_calculado_act[0], 18, 'capturas.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Menores Recuperados",res_calculo_ante[34],  res_calculo_act[34], 18, 'rme.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "EIYM Minas Ilegales",res_calculo_ante[35],  res_calculo_act[35], 14, 'ejc.jpg', filtro, 1)
            
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Excavadoras",res_calculo_ante[36], res_calculo_act[36], 18, 'excavadoras.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Retroexcavadoras",res_calculo_ante[37], res_calculo_act[37], 18, 'retroexcavadoras.jpg', filtro, 1)
        
        
        maquinaria_anterior = [res_calculo_ante[38], res_calculo_ante[39]]
        maquinaria_anctual = [res_calculo_act[38], res_calculo_act[39]]

        resultados  = claculo_maquinaria_amarialla_mapa_dos(maquinaria_anterior, maquinaria_anctual, 1, 18)

        pos = grupo_result_resal_comparativa_dos (pdf, pos_vert, pos, "Maquinaria Pesada", resultados[0], resultados[1], resultados[2], 'buldocer.jpg', filtro, 1)

        # pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Maquinaria Pesada",res_calculo_ante[38], res_calculo_act[38], 18, 'buldocer.jpg', filtro, 1)
        # pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Bulldozer",res_calculo_ante[39], res_calculo_act[39], 18, 'maquinaria.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Unidad Producción Minera",res_calculo_ante[40], res_calculo_act[40], 18, 'upm.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Dragas",res_calculo_ante[41], res_calculo_act[41], 18, 'dragas.jpg', filtro, 1)

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Coltan kg",res_calculo_ante[65], res_calculo_act[65], 18, 'coltan.jpg', filtro, 1)
        x = 354
        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+7,   pos-54.5, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-54.5, x , pos-3)
        pdf.line( 290.5, pos-50, 290.5 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-54.5
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(313.5, a+1, 313.5, a+2)
                pdf.line(336, a+1, 336, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)
        # # claculo_mapa_dos(pdf, res_calculo_ante[36], res_calculo_act[36], "EXCAVADORA(S)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[37], res_calculo_act[37], "RETROEXCAVADORA(S)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[38], res_calculo_act[38], "MAQUINARIA PESADA",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18, 175)
        # # claculo_mapa_dos(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18, 175)

        # maquinaria_anterior = [res_calculo_ante[38], res_calculo_ante[39]]
        # maquinaria_anctual = [res_calculo_act[38], res_calculo_act[39]]

        # resultados  = claculo_maquinaria_amarialla_mapa_dos(pdf, maquinaria_anterior, maquinaria_anctual, 1, 7, 18, 175)

            
        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "ECONOMIAS ILICITAS", filtro ,107)
        pos = pos + 5

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Liberados",res_calculo_ante[42], res_calculo_act[42], 18, 'cadena.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Rescatados",res_calculo_ante[43], res_calculo_act[43], 18, 'cadena2.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Válvulas ilícitas Destruidas",res_calculo_ante[44], res_calculo_act[44], 18, 'valvula.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Refinerias Ilegales Destruidas",res_calculo_ante[45], res_calculo_act[45], 18, 'refineria.jpg', filtro, 1)
        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Combustible Incautado Gal",res_calculo_ante[62], res_calculo_act[62], 18, 'combustible.jpg', filtro, 1)

        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+7,   pos-34.5, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-34.5, x , pos-3)
        pdf.line( 293.5, pos-29, 293.5 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-34.5
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(313.5, a+1, 313.5, a+2)
                pdf.line(336, a+1, 336, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)

        titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, "DEPÓSITO ILEGAL", filtro ,107)
        pos = pos + 5

        pos = grupo_result_resal_comparativa(pdf, pos_vert, pos, "Depósito Ilegal",res_calculo_ante[46], res_calculo_act[46], 18, 'deposito.jpg', filtro, 1)

        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+7,   pos-13.5, pos_vert[0]+7 , pos-3)
        pdf.line( x, pos-13.5, x , pos-3)
        pdf.line( 293.5, pos-9, 293.5 , pos-3)
        pdf.line( pos_vert[0]+7, pos-3, x , pos-3)

        posicion_inicial_linea =pos-13.5
        lineas = pos-4
        a = posicion_inicial_linea
        while a < lineas:
                pdf.set_draw_color(140, 140, 140)
                pdf.set_line_width(0.3)
                pdf.line(313.5, a+1, 313.5, a+2)
                pdf.line(336, a+1, 336, a+2)

                a = a+2

        pos = pos + 3
        pdf.ln(8.5)

        pdf.set_line_width(0.5)
        pdf.line(4, 209, 353, 209)
        pdf.set_line_width(0.3)

    # 