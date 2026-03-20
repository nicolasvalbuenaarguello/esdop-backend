# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.y_e_cartilla_ejc_cdt.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.y_e_cartilla_ejc_cdt.models.funtions.componest.tablas import *
from tipo_docker.y_e_cartilla_ejc_cdt.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()

import pandas as pd
class Calculo_Spoa:
    def __init__(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant, fecha_titulo, fecha_titulo_dos ):

            self.filtro = filtro
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant
            self.pdf =pdf
            self.fecha_titulo = fecha_titulo
            self.fecha_titulo_dos = fecha_titulo_dos

            query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)
            query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)

            resultados_actual = conexion_pos.comando_query(query_actual[0])
            hechos_actual = conexion_pos.comando_query(query_actual[1])
            erradicacion_actual = conexion_pos.comando_query(query_actual[2])

            resultados_anterior = conexion_pos.comando_query(query_anterior[0])
            hechos_anterior = conexion_pos.comando_query(query_anterior[1])
            erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

            self.res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
            self.res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)

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


    #funcion para graficar las afectaciones propias tropas en el mapa
    def afectaciones_propias_tropas_mapa(self):


        valor_asesinados = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        valor_asesinados_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 5,  "SI") #funcion para filtar el spoa

        valor_heridos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        valor_heridos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 6,  "SI") #funcion para filtar el spoa

        datos = [valor_asesinados_ant[0], valor_asesinados[0], valor_heridos_ant[0], valor_heridos[0], self.anio_ant, self.anio_act, self.fecha_titulo, self.fecha_titulo_dos]

        afectaciones = [valor_asesinados[0],valor_heridos[0]]

        cuadro_afectaciones(self.pdf, datos, self.filtro)
        #calculo de afectaciones propias tropas

        afecataciones_propias_tropas(afectaciones, self.filtro)

        afectaciones_img  = '{}static/img/img_mapas/afectaciones.png'.format(self.filtro[15])
        afectaciones_img_fondo  = '{}static/img/img_mapas/afectaciones_fondo.png'.format(self.filtro[15])

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.filtro[15])
        self.pdf.image(afectaciones_img_fondo,13,18.7,162.1,199)
        self.pdf.image(afectaciones_img,-8,5,180,220)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)


    def cuadro_afectaciones_pdf_comparativo(self):

        valor_asesinados = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        valor_asesinados_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 5,  "SI") #funcion para filtar el spoa

        valor_heridos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        valor_heridos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 6,  "SI") #funcion para filtar el spoa

        datos = [valor_asesinados_ant[0], valor_asesinados[0], valor_heridos_ant[0], valor_heridos[0], self.anio_ant, self.anio_act, self.fecha_titulo, self.fecha_titulo_dos]
        
        # cuadro_afectaciones(pdf, datos, filtro)

        cuadro_heridos_asesinados_comparativos(self.pdf, datos, self.filtro)
        #cuadro de afectaciones, heridos  y asesinados 

    # cuadro de resultados resaltantes comparativos
    def resultados_mineria_boletin_comp(self):


        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        datos = [valor[0], valor_1[0], self.res_calculo_act[40], self.res_calculo_act[38], self.res_calculo_act[39], self.res_calculo_act[36], self.res_calculo_act[37], self.res_calculo_act[41], self.res_calculo_act[59], self.res_calculo_act[60], self.res_calculo_act[65]]

        datos_ant = [self.res_calculo_ante[33], self.res_calculo_ante[35], self.res_calculo_ante[40], self.res_calculo_ante[38], self.res_calculo_ante[39], self.res_calculo_ante[36], self.res_calculo_ante[37], self.res_calculo_ante[41], self.res_calculo_ante[59], self.res_calculo_ante[60], self.res_calculo_ante[65]]
        #encabezado de interdicion
        encabezado_tabla_resultados_mapa_compa(self.pdf, "RESULTADOS MINERÍA ILEGAL ", self.anio_act, self.anio_ant)
        self.pdf.ln(10)
        tabla_resultados_con_mapa_comp(self.pdf,"Capturas", datos_ant[0], datos[0], "Personas", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Yacimientos Mineros ",datos_ant[1], datos[1], "Unidades", 14, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Unidad Producción Minera",datos_ant[2], datos[2], "Unidades", 18, 1)
        self.pdf.ln()
        maquinaria_anterior = [self.res_calculo_ante[36], self.res_calculo_ante[37], self.res_calculo_ante[38], self.res_calculo_ante[39], self.res_calculo_ante[41]]
        maquinaria_anctual = [self.res_calculo_act[36], self.res_calculo_act[37], self.res_calculo_act[38], self.res_calculo_act[39], self.res_calculo_act[41]]
        tabla_resultados_con_mapa_comp_maquinaria(self.pdf, maquinaria_anterior, maquinaria_anctual, "Maquinaria Amarilla",1, 7, 18, "Unidades")
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Motores",datos_ant[8], datos[8], "Unidades", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Combustibles",datos_ant[9], datos[9], "Galones", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Coltan",datos_ant[10], datos[10], "Kilos", 18, 1)
        # print(datos)
        nombre = "mineria"
        mapa_hechos(datos[1], nombre, self.filtro)

        
        afectaciones_img  = '{}static/img/img_mapas/mineria.png'.format(self.filtro[15])
        afectaciones_img_fondo  = '{}static/img/img_mapas/mineria_fondo.png'.format(self.filtro[15])

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.filtro[15])
        self.pdf.image(afectaciones_img_fondo,13,18.7,162.1,199)
        self.pdf.image(afectaciones_img,-8,5,180,220)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)


    # cuadro de resultados resaltantes comparativos
    def resultados_contrabando_boletin_comp(self):


        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 49,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 49,  "SI") #funcion para filtar el spoa
        datos = [valor[0], valor_1[0], self.res_calculo_act[51], self.res_calculo_act[52], self.res_calculo_act[53], self.res_calculo_act[54], self.res_calculo_act[55], self.res_calculo_act[56], self.res_calculo_act[57], self.res_calculo_act[58]]

        res_calculo_ante = [self.res_calculo_ante[49], self.res_calculo_ante[50], self.res_calculo_ante[51], self.res_calculo_ante[52], self.res_calculo_ante[53], self.res_calculo_ante[54], self.res_calculo_ante[55], self.res_calculo_ante[56], self.res_calculo_ante[57], self.res_calculo_ante[58]]

        #encabezado de interdicion
        encabezado_tabla_resultados_mapa_compa(self.pdf, "RESULTADOS CONTRABANDO", self.anio_act, self.anio_ant)
        self.pdf.ln(10)


        tabla_resultados_con_mapa_comp(self.pdf,"Capturas", res_calculo_ante[0], datos[0], "Personas", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Gasolina",res_calculo_ante[1], datos[1], "Galones", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"ACPM",res_calculo_ante[2], datos[2], "Galones", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Insumos Líquidos",res_calculo_ante[3], datos[3], "Galones", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Vehículos",res_calculo_ante[4], datos[4], "Unidades", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Animales incautados",res_calculo_ante[5], datos[5], "Unidades", 18, 1)

        nombre = "contrabando"
        mapa_hechos(datos[9], nombre, self.filtro)

        contrabando  = '{}static/img/img_mapas/{}.png'.format(self.filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(self.filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.filtro[15])
        self.pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        self.pdf.image(contrabando,-8,5,180,220)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)

        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
    
    # resultados por enemigo 
    def resultados_narcotrafico_boletin(self):
   
        #encabezado de interdicion
        encabezado_interdicion(self.pdf)
        self.pdf.ln()

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 69,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 68,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 70,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 71,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        # datos = [res_calculo[21],res_calculo[23],res_calculo[29],res_calculo[22],res_calculo[47],res_calculo[48], res_calculo[28], res_calculo[24], res_calculo[25], res_calculo[26], res_calculo[65], res_calculo[66], res_calculo[67], res_calculo[68]]

        # datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]
        
        calculo_de_interdion(self.pdf,"Clorhidrato de Cocaína", datos[0], 85758, "Toneladas")
        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Pasta Base de Coca", datos[1], 26000, "Toneladas")

        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Heroína", datos[10], 0, "Kilos")
        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Basuco", datos[11], 0, "Kilos")
        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Drogas Sinteticas", datos[12], 0, "Unidades")

        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Insumos Sólidos ", datos[2], 0, "Toneladas")
        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Marihuana", datos[3], 120000, "Toneladas")
            
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"CLHC en proceso", datos[4], 0, "Galones")
                
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"PBC en proceso ", datos[5], 0, "Galones")
                    
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Insumos Líquidos  ", datos[6], 0, "Galones")
                
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Laboratorios CLHC ", datos[7], 150, "Unidades")
                    
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Laboratorios PBC", datos[8], 2764, "Unidades")
                        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Laboratorios Heroína", datos[13], 0, "Unidades")
                        
        self.pdf.ln()
        calculo_de_interdion(self.pdf,"Semilleros", datos[9], 0, "Unidades")
        
        nombre =  "mapa_narcotrafico"
        mapa_narcotrafico(datos, self.filtro, nombre)


        ruta = self.filtro[15]
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(self.filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(self.filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.filtro[15])
        self.pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        self.pdf.image(contrabando,-8,5,180,220)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)

        convecion_narcotrafico = '{}static/img/img_mapas/convecion_narcotrafico.jpg'.format(ruta)
        self.pdf.image(convecion_narcotrafico,5, 175, 51, 32)

    
    # cuadro de resultados resaltantes artemisa
    def resultados_artemisas_boletin_comp(self):



        #encabezado de interdicion
        encabezado_tabla_resultados_mapa_compa(self.pdf, "LOE AMAZONIA", self.anio_act, self.anio_ant)
        self.pdf.ln(10)
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa_comp(self.pdf,"Capturas LOE Amazonía", valor_1[0], valor[0], "Personas", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Plantulas Sembradas",self.res_calculo_ante[31], self.res_calculo_act[31], "Unidades", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Incautacion Madera m3",self.res_calculo_ante[32], self.res_calculo_act[32], "Metros Cubi.", 18, 1)
        self.pdf.ln()
        tabla_resultados_con_mapa_comp(self.pdf,"Animales Incautados",self.res_calculo_ante[63], self.res_calculo_act[63], "Unidades", 18, 1)
        self.pdf.ln()

        datos = [self.res_calculo_act[30], self.res_calculo_act[63]]

        nombre = "artemisa"
        mapa_dos_puntos(datos, nombre, self.filtro)
        # self.pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        convecion_artmisa = '{}static/img/img_mapas/convecion_artmisa.jpg'.format(self.filtro[15])
        contrabando  = '{}static/img/img_mapas/{}.png'.format(self.filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(self.filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.filtro[15])
        self.pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        self.pdf.image(contrabando,-8,5,180,220)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)

        self.pdf.image(convecion_artmisa,155, 165, 65, 30)

    #    convecion_artmisa.jpg
    #AFECTACIONES A LA AMENAZA
    def resultados_resaltantes_r_n(self):


        z = encabezado_comparativo(self.pdf, True, self.fecha_titulo_dos, self.fecha_titulo, 10)
        self.pdf.ln(-5)

        sepador_mapa_dos(self.pdf, True, "NARCOTRÁFICO", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 21,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "COCAÍNA Kg",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 22,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 22,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "MARIHUANA Kg",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 23,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 23,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "PBC Kg",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 24,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 24,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "LAB. CLORHIDRATO DE COCAINA",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 25,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 25,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "LAB. PASTA O BASE DE COCA",1, 7, 18,5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 26,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 26,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "SEMILLEROS",1, 7, 18,5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 27,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 27,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "MATA(S) DE COCA EN SEMILLERO",1, 7, 18,5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 28,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 28,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "INSUMOS LIQUIDOS Gal",1, 7, 18,5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 29,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 29,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "INSUMOS SOLIDOS Kg",1, 7, 18,5)



        sepador_mapa_dos(self.pdf, True, "MATERIAL DE GUERRA", 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "ARMAS DE LARGO ALCANCE",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 8,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 8,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "ARMAS DE CORTO ALCANCE",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 9,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 9,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "ARMAS DE ACOMPAÑAMIENTO",1, 7, 18, 5)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 10,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 10,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "MUNICIONES",1, 7, 18, 5)


        sepador_mapa_dos(self.pdf, True, "MATERIAL DE EXPLOSIVOS", 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[15], self.res_calculo_act[15], "NEUTRALIZACIÓN TERRORISTA",1, 8, 14, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[16], self.res_calculo_act[16], "A.E",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[17], self.res_calculo_act[17], "MAP(Mina Anti Persona)",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[18], self.res_calculo_act[18], "EXPLOSIVOS kg",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[19], self.res_calculo_act[19], "CORDÓN DETONANTE m",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[20], self.res_calculo_act[20], "MECHA LENTA m",1, 7, 18, 5)

        
        sepador_mapa_dos(self.pdf, True, "PLAN AMAZONÍA", 5)
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "CAPTURAS PLAN AMAZONIA",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[31], self.res_calculo_act[31], "PLANTULAS SEMBRADA",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[32], self.res_calculo_act[32], "MADERA INCAUTADA",1, 7, 18, 5)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[63], self.res_calculo_act[63], "ANIMALES INCAUTADOS",1, 7, 18, 5)


        alrura = 130 + z
        self.pdf.ln(-alrura)
        # # encabezado_comparativo_mapa(self.pdf, True, anio_act, anio_ant)
        
        encabezado_comparativo(self.pdf, True, self.fecha_titulo_dos, self.fecha_titulo, 175)

        self.pdf.ln(-5)

        sepador_mapa_dos(self.pdf, True, "MINERÍA ILEGAL", 170)
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "CAPTURAS MINERIA",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[34], self.res_calculo_act[34], "MENORES R. MINERIA",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[35], self.res_calculo_act[35], "EIYM",1, 8, 14, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[40], self.res_calculo_act[40], "UPM ILEGAL",1, 7, 18, 170)
        

        maquinaria_anterior = [self.res_calculo_ante[36], self.res_calculo_ante[37], self.res_calculo_ante[38], self.res_calculo_ante[39], self.res_calculo_ante[41]]
        maquinaria_anctual = [self.res_calculo_act[36], self.res_calculo_act[37], self.res_calculo_act[38], self.res_calculo_act[39], self.res_calculo_act[41]]

        claculo_maquinaria_amarialla_mapa_dos(self.pdf, maquinaria_anterior, maquinaria_anctual, "MAQUINARIA AMARILLA",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[65], self.res_calculo_act[65], "COLTAN KG",1, 7, 18, 170)

        sepador_mapa_dos(self.pdf, True, "ECONOMÍAS ILÍCITAS", 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[42], self.res_calculo_act[42], "LIBERADOS",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[43], self.res_calculo_act[43], "RESCATADOS",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[44], self.res_calculo_act[44], "VÁLVULAS",1, 7, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[45], self.res_calculo_act[45], "REFINERIAS",1, 7, 18, 170)

        
        sepador_mapa_dos(self.pdf, True, "COMBATES", 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[11], self.res_calculo_act[11], "COMBATES POSITIVOS",1, 8, 14, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[12], self.res_calculo_act[12], "COMBATES NEGATIVOS",1, 8, 14, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[13], self.res_calculo_act[13], "COMBATES SIN RESULTADOS",1, 8, 14, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[14], self.res_calculo_act[14], "TOTAL DE COMBATES",1, 8, 14, 170)
        
        sepador_mapa_dos(self.pdf, True, "CONTRABANDO", 170)
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 49,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 49,  "SI") #funcion para filtar el spoa
        claculo_mapa_dos(self.pdf,  valor_1[0], valor[0], "CAPTURAS",1, 8, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[50], self.res_calculo_act[50], "GASOLINA GAL",1, 8, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[51], self.res_calculo_act[51], "ACPM GAL",1, 8, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[52], self.res_calculo_act[52], "INUMOS LIQUIDOS GAL",1, 8, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[53], self.res_calculo_act[53], "VEHICULOS",1, 8, 18, 170)
        claculo_mapa_dos(self.pdf, self.res_calculo_ante[54], self.res_calculo_act[54], "ANIMALES INCAUTADOS",1, 8, 18, 170)

       #AFECTACIONES A LA AMENAZA
    def resultados_afectaciones_a_la_amenaza(self):

        # cuadro_afectaciones(pdf, datos, filtro)
        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.rounded_rect(4, 40, 350, 145, 1,'DF', '1234')

        # pdf.ln()
        claculo_afectacion_amenaza_cabecera(self.pdf,self.anio_act, self.anio_ant)

        self.pdf.set_fill_color(234, 236, 234)
        self.pdf.rounded_rect(5, 65, 347, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 111, 347, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 157, 347, 20, 1,'F', '1234')

        self.pdf.set_fill_color(210, 214, 209)
        self.pdf.rounded_rect(5, 88, 347, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 134, 347, 20, 1,'F', '1234')

        self.pdf.set_fill_color(94, 119, 89)
        self.pdf.rounded_rect(5, 65, 35, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 88, 35, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 111, 35, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 134, 35, 20, 1,'F', '1234')
        self.pdf.rounded_rect(5, 157, 35, 20, 1,'F', '1234')
        ruta = self.filtro[15] 

        afectacion_ameneza_enemigo(self.pdf, "MENORES RECUPERADOS", 10,10, -5, self.res_calculo_ante[0], self.res_calculo_act[0], 18, 1, 7,ruta, 80)
        afectacion_ameneza_enemigo(self.pdf, "PRESENTACIÓN VOLUNTARIA",13,10, -5, self.res_calculo_ante[1], self.res_calculo_act[1], 18, 1, 7,ruta,102)
        afectacion_ameneza_enemigo(self.pdf, "SOMETIMIENTOS A LA JUSTICIA",10,10, -5, self.res_calculo_ante[2], self.res_calculo_act[2], 18, 1, 7,ruta,124)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 3,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 3,  "SI") #funcion para filtar el spoa
        afectacion_ameneza_enemigo(self.pdf, "CAPTURAS", 15,6, -5, valor_1[0], valor[0], 18, 1, 7,ruta, 148 )

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 4,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 4,  "SI") #funcion para filtar el spoa
        afectacion_ameneza_enemigo(self.pdf, "MDOM", 9,7, -5, valor_1[0], valor[0], 18, 1, 7,ruta, 170 )
