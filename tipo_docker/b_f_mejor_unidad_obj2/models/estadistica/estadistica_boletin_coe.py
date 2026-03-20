# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.b_f_mejor_unidad_obj2.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.b_f_mejor_unidad_obj2.models.funtions.componest.tablas import *

conexion_pos = Databa_bases()
import json
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import psycopg2
import sys
from collections import defaultdict
class Calculo_Spoa:

    def __init__(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant, fecha_titulo, fecha_titulo_dos ):

            self.filtro = filtro
            #leer objectivos por unidades
            ruta = self.filtro[15] 
            self.json_ruta = '{}static/obj_2_diferencial_divisiones.json'.format(ruta)
            self.json_ruta_br = '{}static/INDICADORES OBJ_JSON_BR.json'.format(ruta)


            self.obj_2 = ['SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI']
            

            self.numero =0        
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant
            self.pdf =pdf
            self.fecha_titulo = fecha_titulo
            self.fecha_titulo_dos = fecha_titulo_dos
            self.indicadores = []

            self.fecha_inicial_u_l = fecha_inicial_u_l
            self.fecha_final_u_l = fecha_final_u_l

            query_actual = parametros(self.fecha_inicial_u_l, self.fecha_final_u_l, filtros, filtro)
            query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)

            query_anterior_unidades = parametros_unidades(self.fecha_inicial_u_l, self.fecha_final_u_l, filtros, filtro)

            self.unidades_filtradas = conexion_pos.comando_query(query_anterior_unidades[0])

            self.jerarquia_unidades = defaultdict(
                lambda: defaultdict(
                    lambda: defaultdict(set)
                )
            )

            for agr_div, division, brigada, unidad in self.unidades_filtradas:
                if not (agr_div and division and brigada and unidad):
                    continue

                self.jerarquia_unidades[agr_div.strip()][division.strip()][brigada.strip()].add(unidad.strip())


            resultados_actual = conexion_pos.comando_query(query_actual[0])
            self.hechos_actual = conexion_pos.comando_query(query_actual[1])

            resultados_anterior = conexion_pos.comando_query(query_anterior[0])
            self.hechos_anterior = conexion_pos.comando_query(query_anterior[1])


            self.res_calculo_ante = estadistica_resultados(resultados_anterior, self.hechos_anterior, filtro)
            self.res_calculo_act = estadistica_resultados(resultados_actual, self.hechos_actual, filtro)
    def validar_obj(self, unidad, pos):
            if pos == 1:
                self.obj_2  = validar_indicador_unidad(json, self.json_ruta_br, unidad)
            elif pos == 0:

                self.obj_2  = validar_indicador_unidad(json, self.json_ruta, unidad)

            if  self.obj_2 == []:
                self.obj_2 = ['SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI']  
    
    def buscar_unidad(self, jerarquia, unidad_buscada):
        for agr, divisiones in jerarquia.items():
            for div, brigadas in divisiones.items():
                for bri, unidades in brigadas.items():
                    if unidad_buscada in unidades:
                        return agr, div, bri
        return None      
    def mes(self, date):
        months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

        if date == "01" or date == 1:
            return months[0]
        
        if date == "02" or date == 2:
            return months[1]
        
        if date == "03" or date == 3:
            return months[2]
        
        if date == "04" or date == 4:
            return months[3]
        
        if date == "05" or date == 5:
            return months[4]
            
        if date == "06" or date == 6:
            return months[5]
            
        if date == "07" or date == 7:
            return months[6]
            
        if date == "08" or date == 8:
            return months[7]
            
        if date == "09" or date == 9:
            return months[8]
            
        if date == "10" or date == 10:
            return months[9]
            
        if date == "11" or date == 11:
            return months[10]
            
        if date == "12" or date == 12:
            return months[11]
    
    def meses_nombre(self, divisiones_lis):
        divisiones=[]
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]
        años = []

        for x in self.res_calculo_act:
            for y in x:

                if numero == 12 or numero == 13 or numero == 14 or numero == 15 or numero == 16 or numero == 17 or numero == 54 or numero == 98 or numero == 99 or numero == 100 or numero == 101 or numero == 102 or numero == 103:

                    format = '%Y-%m-%d'
                    datetime_str = datetime.datetime.strptime(str(y[1]), format)
                    mes_n = str(datetime_str.strftime('%m'))
                    año = str(datetime_str.strftime('%Y'))
                    mes_d = str(self.mes(mes_n))

                    if mes_d not in divisiones:
                        divisiones.append(mes_d)

                    if año not in años:
                        años.append(año)
                else:
                    format = '%Y-%m-%d'
                    datetime_str = datetime.datetime.strptime(str(y[0]), format)
                    mes_n = str(datetime_str.strftime('%m'))
                    año = str(datetime_str.strftime('%Y'))
                    mes_d = str(self.mes(mes_n))
         
                    if mes_d not in divisiones:
                        divisiones.append(mes_d)
                    if año not in años:
                        años.append(año)
                        

            numero = numero + 1
        #print(y[1])
        #print(y[2])
        #print(divisiones)

        #print(len(hechos_devolver))

        months = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

        divisiones = sorted(divisiones, key = lambda m: months.index(m))
        años.sort()
        

        return [divisiones, años]

    def enemigo_nombre(self, divisiones_lis):
        divisiones=[]
        divisiones = divisiones_lis
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]

        for x in self.res_calculo_act:
            for y in x:

                if numero == 12 or numero == 13 or numero == 14 or numero == 15 or numero == 16 or numero == 17 or numero == 54 or numero == 98 or numero == 99 or numero == 100 or numero == 101 or numero == 102 or numero == 103:
                    if y[18] not in filtro_hechos:
                        filtro_hechos.append(y[18])
                    if y[8] not in divisiones:
                        divisiones.append(y[8])
                else:
                    if y[26] not in filtro_hechos:
                        filtro_hechos.append(y[26])
                    if y[7] not in divisiones:
                        divisiones.append(y[7])
                        

            numero = numero + 1
        #print(y[1])
        #print(y[2])
        #print(divisiones)

        #print(len(hechos_devolver))


        divisiones.sort()
        for x in divisiones:
            if x == "GAO - Residual Disidencias FARC":
                hechos_devolver.append("GAO-r")
            elif x == "DELINCUENCIA":
                hechos_devolver.append("DELCO")
            elif x == "Amenaza de Naturaleza Cibernetica":
                hechos_devolver.append("ANC")
            elif x == "Delincuencia Organizada Transnacional":
                hechos_devolver.append("DOT")
            elif x == "GAO CAPARROS":
                hechos_devolver.append("GAO-CP")
            elif x == "GAO CLAN DEL GOLFO":
                hechos_devolver.append("GAO-CG")
            elif x == "GAO COMUNEROS DEL SUR":
                hechos_devolver.append("GAO-CS")
            elif x == "GAO PELUSOS":
                hechos_devolver.append("GAO-PEL")
            elif x == "NARCOTRÁFICO":
                hechos_devolver.append("NART.")
            else:
                hechos_devolver.append(x)


        return [divisiones, hechos_devolver]

    def divisiones_nombre(self, divisiones_lis):
        divisiones=[]
        divisiones = divisiones_lis
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]

        for y in self.res_calculo_act:
            if y !=[]:
                if numero == 12 or numero == 13 or numero == 14 or numero == 15 or numero == 16 or numero == 17 or numero == 54 or numero == 98 or numero == 99 or numero == 100 or numero == 101 or numero == 102 or numero == 103:
    
                    filtro_hechos =[x[18] for x in self.res_calculo_act[numero]]
                    filtro_hechos = tuple(set(filtro_hechos))

                    divisiones =[x[2] for x in self.res_calculo_act[numero]]
                    divisiones = list(set(divisiones))
                else:
                    
                    filtro_hechos =[x[26] for x in self.res_calculo_act[numero]]
                    filtro_hechos = tuple(set(filtro_hechos))

                    divisiones =[x[1] for x in self.res_calculo_act[numero]]
                    divisiones = list(set(divisiones))

                        

            numero = numero + 1


        #print(y[1])

        #hechos_devolver = [x for x in hechos if x[18] in filtro_hechos]

        querys_hechos = "SELECT * FROM view_hechos_materializados WHERE fecha_hecho >= '{}'  AND fecha_hecho <= '{} ' and hr in {}  ORDER BY fecha_hecho ASC".format(self.fecha_inicial_u_l, self.fecha_final_u_l, filtro_hechos )
 
        hechos_devolver = conexion_pos.comando_query(querys_hechos)
        #hechos_devolver = list(filter(lambda hechos: hechos[18] in filtro_hechos, hechos))
        hechos_devolver = list(hechos_devolver)
        divisiones.sort()
        return [divisiones, hechos_devolver]

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

    def validar_spoa_unidad_dinamico(self, filtro, res_calculo,  validar):
        spoa=[]
        no_spoa=[]
        
        if validar == "SI":
            
            startdate = pd.to_datetime("2024-06-04").date()
            # startdate = pd.to_datetime("2024-01-01").date()
            
            if filtro[16] == "sin_spoa" or filtro[16] == "res_sin_spoa" :
                for x in res_calculo:
            
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
                spoa =  res_calculo

                

            spoa = spoa
        else:
            spoa =  res_calculo

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
    def comparativo_mapa(self, unidad, posicion):
        valor_mdom = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        valor_mdom_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 5,  "SI") #funcion para filtar el spoa
        
        valor_cap = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 4,  "SI") #funcion para filtar el spoa
        valor_cap_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 4,  "SI") #funcion para filtar el spoa

        datos = [ self.res_calculo_act[0], self.res_calculo_act[2], valor_cap[0], valor_mdom[0]]
        datos_ant = [ self.res_calculo_ante[0], self.res_calculo_ante[2], valor_cap_ant[0], valor_mdom_ant[0]]
        texto=["MENORES RECUPERADOS", "SOMETIMIENTOS A LA JUSTICIA", "CAPTURAS", "MDOM"]

        datos_2 = [self.res_calculo_act[0], self.res_calculo_act[1], valor_cap[0],valor_mdom[0]]
        datos_ant_2 = [self.res_calculo_ante[0], self.res_calculo_ante[1], valor_cap_ant[0],valor_mdom_ant[0]]

        texto_2=["MENORES RECUPERADOS", "PRESENTACIÓN VOLUNTARIA", "CAPTURAS","MDOM"]
        suma=18
        constante=1
        id_enemigo = 7
        rango = [0,3]

        amenaza=["GAO - Residual Disidencias FARC","GAO-r"]
        indicadores = encabezado_comparativo_enemigo_dinamico(datos_ant, datos,  amenaza,  suma, constante, id_enemigo, texto,self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]
  
  
        rango = [4,7]
        amenaza=["GAO ELN","GAO ELN"]
        indicadores = encabezado_comparativo_enemigo_dinamico( datos_ant_2, datos_2,  amenaza, suma, constante, id_enemigo, texto_2, self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]

        rango = [8,11]
 
        if self.filtro[2] == "FUDRA2":
            amenaza=["GAO COMUNEROS DEL SUR","GAO-CS"]
        else:
            amenaza=["GAO CLAN DEL GOLFO","GAO-CG"]

        indicadores = encabezado_comparativo_enemigo_dinamico( datos_ant, datos,  amenaza, suma, constante, id_enemigo, texto,self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]
        rango = [12,15]  
            
        amenaza=["GDO","GDO"]
        indicadores = encabezado_comparativo_enemigo_dinamico(datos_ant, datos,  amenaza,  suma, constante, id_enemigo, texto,self.indicadores, self.obj_2,  rango, unidad, posicion[0])
        self.indicadores = indicadores[0]

        rango = [16,19] 

        valor_armas_largas = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 8,  "SI") #funcion       para filtar el spoa
        valor_armas_largas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 8,  "SI")       #funcion para filtar el spoa

        valor_armas_cortas = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 9,  "SI") #funcion       para filtar el spoa
        valor_armas_cortas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 9,  "SI")       #funcion para filtar el spoa

        valor_armas_acompañamiento = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 10,  "SI")       #funcion para filtar el spoa
        valor_armas_acompañamiento_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 10,  "SI") #funcion para filtar el spoa

        valor_municiones = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 11,  "SI") #funcion        para filtar el spoa
        valor_municiones_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 11,  "SI")        #funcion para filtar el spoa

        datos = [valor_armas_largas[0], valor_armas_cortas[0], valor_armas_acompañamiento[0], valor_municiones[0]]
        datos_ant = [valor_armas_largas_ant[0], valor_armas_cortas_ant[0], valor_armas_acompañamiento_ant[0], valor_municiones_ant[0] ]
        texto=["Armas de largo alcance","Armas de corto alcance", "Armas de acompañamiento", "Municiones"]
        texto = [t.upper() for t in texto]

        suma=[18,18,18,18]
        constante=[1,1,1,1]

        indicadores = encabezado_comparativo_enemigo_dinamico_2(datos_ant, datos,  suma,  constante,  texto, self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]
        
        rango = [20,22] 

        datos = [self.res_calculo_act[12], self.res_calculo_act[13], self.res_calculo_act[14]]
        datos_ant = [self.res_calculo_ante[12], self.res_calculo_ante[13], self.res_calculo_ante[14]]
        texto=["Combates positivos","Combates negativos", "Combates sin resultados"]
        texto = [t.upper() for t in texto]

        #color=[[137, 187, 169],[55, 165, 255],[208, 208, 182],[180, 180, 180]]
        color=[255, 255, 255]
        suma=[14,14,14]
        constante=[1,-1,1]

        indicadores = encabezado_comparativo_enemigo_dinamico_2(datos_ant, datos,  suma, constante,  texto, self.indicadores, self.obj_2, rango,unidad, posicion[1])
        self.indicadores = indicadores[0]
    
        rango = [23,30] 

        datos = [self.res_calculo_act[21], self.res_calculo_act[22], self.res_calculo_act[23], self.res_calculo_act[26], self.res_calculo_act[27], self.res_calculo_act[29], self.res_calculo_act[30], self.res_calculo_act[28]]

        datos_ant = [ self.res_calculo_ante[21], self.res_calculo_ante[22], self.res_calculo_ante[23], self.res_calculo_ante[26], self.res_calculo_ante[27], self.res_calculo_ante[29], self.res_calculo_ante[30], self.res_calculo_ante[28] ]
        texto=["Artefacto explosivo (AE)", "Mina antipersona (MAP)", "Explosivos (Kg)", "Cordón detonante (Mt)", "Cordón Seguridad (Mt)", "Detonadores aneléctricos", "Detonadores eléctricos", "Medios de lanzamiento"]
        texto = [t.upper() for t in texto]
        #color=[[137, 187, 169],[55, 165, 255],[208, 208, 182],[180, 180, 180]]
 
        suma=[18,18,18,18,18,18,18,18]
        constante=[1,1,1,1,1,1,1,1]

        indicadores = encabezado_comparativo_enemigo_dinamico_2(datos_ant, datos,  suma, constante,  texto, self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]
  

        rango = [31,40] 
 
        valor_cocaina = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 32,  "SI") #funcion para filtar el spoa
        valor_cocaina_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 32,  "SI") #funcion para filtar el spoa

        valor_marihuana = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        valor_marihuana_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        
        valor_herohina = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 36,  "SI") #funcion para filtar el spoa
        valor_herohina_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 36,  "SI") #funcion para filtar el spoa

        valor_pbc = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 34,  "SI") #funcion para filtar el spoa
        valor_pbc_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 34,  "SI") #funcion para filtar el spoa

        valor_lab_clor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act,  39,  "SI") #funcion para filtar el spoa
        valor_lab_clor_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 39,  "SI") #funcion para filtar el spoa

        valor_lab_pbc = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 40,  "SI") #funcion para filtar el spoa
        valor_lab_pbc_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 40,  "SI") #funcion para filtar el spoa

        valor_semilleros = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 41,  "SI") #funcion para filtar el spoa
        valor_semilleros_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 41,  "SI") #funcion para filtar el spoa

        valor_matas_semilleros = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 42,  "SI") #funcion para filtar el spoa
        valor_matas_semilleros_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 42,  "SI") #funcion para filtar el spoa

        valor_insumos_liquidos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 43,  "SI") #funcion para filtar el spoa
        valor_insumos_liquidos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 43,  "SI") #funcion para filtar el spoa

        valor_minsumos_solidos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 44,  "SI") #funcion para filtar el spoa
        valor_minsumos_solidos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 44,  "SI") #funcion para filtar el spoa

        datos = [valor_cocaina[0], valor_marihuana[0], valor_herohina[0], valor_pbc[0], valor_lab_clor[0], valor_lab_pbc[0], valor_semilleros[0], valor_matas_semilleros[0], valor_insumos_liquidos[0], valor_minsumos_solidos[0]]
        datos_ant = [valor_cocaina_ant[0], valor_marihuana_ant[0], valor_herohina_ant[0], valor_pbc_ant[0], valor_lab_clor_ant[0], valor_lab_pbc_ant[0], valor_semilleros_ant[0], valor_matas_semilleros_ant[0], valor_insumos_liquidos_ant[0], valor_minsumos_solidos_ant[0]]
        texto=["Cocaína (kg)", "Marihuana (kg)", "Heroína (kg)", "Pasta base de coca (kg)", "Laboratorio clorhidrato de cocaína", "Laboratorio pasta base de coca", "Semilleros", "Matas de coca en semilleros", "Insumos líquidos (gal)", "Insumos sólidos (kg)"]
        texto = [t.upper() for t in texto]

        #color=[[137, 187, 169],[55, 165, 255],[208, 208, 182],[180, 180, 180]]
        color=[255, 255, 255]
        suma=[18,18,18,18,18,18,18,18,18,18]
        constante=[1,1,1,1,1,1,1,1,1,1]

        indicadores = encabezado_comparativo_enemigo_dinamico_2( datos_ant, datos,  suma, constante,  texto, self.indicadores, self.obj_2, rango,  unidad, posicion[0] )
        self.indicadores = indicadores[0]
   
        rango = [41,44] 
       
        valor_capturas_mineria = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 52,  "SI") #funcion para filtar el spoa
        valor_capturas_mineria_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 52,  "SI") #funcion para filtar el spoa

        datos = [valor_capturas_mineria[0], self.res_calculo_act[111], self.res_calculo_act[60], self.res_calculo_act[68]]

        datos_ant = [valor_capturas_mineria_ant[0], self.res_calculo_ante[111], self.res_calculo_ante[60], self.res_calculo_ante[68]]


        suma=[18,18,18,18]
        constante=[1,1,1,1]
    
        texto=["Capturas minería ilegal", "Equipo línea amarilla", "Dragas", "Coltán (Kg)"]
        texto = [t.upper() for t in texto]
        indicadores = encabezado_comparativo_enemigo_dinamico_2( datos_ant, datos, suma, constante,  texto, self.indicadores, self.obj_2, rango,  unidad, posicion[0])
        self.indicadores = indicadores[0]


        rango = [45,47] 

        valor_capturas_extorcion = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 112,  "SI") #funcion para filtar el spoa
        valor_capturas_extorcion_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 112,  "SI") #funcion para filtar el spoa

        datos = [valor_capturas_extorcion[0], self.res_calculo_act[69], self.res_calculo_act[70]]

        datos_ant = [valor_capturas_extorcion_ant[0], self.res_calculo_ante[69], self.res_calculo_ante[70]]

        suma=[18,18,18]
        constante=[1,1,1]

        texto=["Capturas extorsión y secuestro","Liberados", "Rescatados"]
        texto = [t.upper() for t in texto]
        indicadores = encabezado_comparativo_enemigo_dinamico_2( datos_ant, datos,  suma, constante,  texto, self.indicadores, self.obj_2, rango,  unidad, posicion[0])
        self.indicadores = indicadores[0]
     
        rango = [48,50]

        datos = [self.res_calculo_act[84], self.res_calculo_act[85], self.res_calculo_act[82]]
        datos_ant = [self.res_calculo_ante[84], self.res_calculo_ante[85], self.res_calculo_ante[82]]

        color=[255, 255, 255]
        suma=[18,18,18]
        constante=[1,1,1]

        texto=["Válvulas", "Refinerías", "Hidrocarburos (gal)"]
        texto = [t.upper() for t in texto]

        indicadores = encabezado_comparativo_enemigo_dinamico_2(datos_ant, datos,  suma, constante,  texto, self.indicadores, self.obj_2, rango,  unidad, posicion[0])
        self.indicadores = indicadores[0]

        rango = [51,54] 

        valor_capturas_amazonia = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 48,  "SI") #funcion para filtar el spoa
        valor_capturas_amazonia_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 48,  "SI") #funcion para filtar el spoa

        datos = [valor_capturas_amazonia[0], self.res_calculo_act[50], self.res_calculo_act[51], self.res_calculo_act[49]]
        datos_ant = [valor_capturas_amazonia_ant[0], self.res_calculo_ante[50], self.res_calculo_ante[51], self.res_calculo_ante[49]]

        suma=[18,18,18,18]
        constante=[1,1,1,1]

        texto=["Capturas LOE AMAZONÍA", "Madera Incautada (m3)", "Animales incautados", "Plántulas sembradas"]
        texto = [t.upper() for t in texto]

        indicadores = encabezado_comparativo_enemigo_dinamico_2( datos_ant, datos,   suma, constante,  texto, self.indicadores, self.obj_2, rango, unidad, posicion[0])
        self.indicadores = indicadores[0]

    def ordenar_unidad(self, unidades_ordenar, pos):
        unidades_ordenadas = sorted(unidades_ordenar, key =lambda x: x[pos], reverse=True)
        return unidades_ordenadas
   
    def evaluacion(self):
        unidades_evaluadas=[]
        brigadas_evaluadas=[]
        unidades_ut_evaluadas=[]
        validar_bri = []
        validar_und = []
        for agr, divisiones in self.jerarquia_unidades.items():
            unidad_evaluada=""
            self.indicadores=[]
            posicion = [1,2]
            self.validar_obj( agr, 0)
            self.comparativo_mapa(agr, posicion)
            superior = 0
            inferior = 0
            igual = 0

            for x in self.indicadores:
                if x > 0:
                    superior =  superior +1
                elif x < 0:
                    inferior = inferior +1
                else:
                    igual = igual +1

            total = len(self.indicadores)

            por_superior = (superior/total)*100
            por_inferior = (inferior/total)*100
            por_igual = (igual/total)*100
            unidad_evaluada = (agr, total, por_superior, por_igual, por_inferior)
            unidades_evaluadas.append(unidad_evaluada)

            if self.filtro[0] != "---" and self.filtro[0] !="" or self.filtro[31] =="compl":
                   
                for div, brigadas in divisiones.items():
                    pass
                    #print(f"  DIVISIÓN: {div}")

                    for bri, unidades in brigadas.items():
                        if bri not in validar_bri:
                            validar_bri.append(bri)
                                
                            unidad_evaluada=""
                            self.indicadores=[]
                            posicion = [3,4]
                            self.validar_obj( bri, 1)
                            self.comparativo_mapa(bri, posicion)
                            superior = 0
                            inferior = 0
                            igual = 0

                            for x in self.indicadores:
                                if x > 0:
                                    superior =  superior +1
                                elif x < 0:
                                    inferior = inferior +1
                                else:
                                    igual = igual +1

                            total = len(self.indicadores)

                            por_superior = (superior/total)*100
                            por_inferior = (inferior/total)*100
                            por_igual = (igual/total)*100
                            unidad_evaluada = (bri, total, por_superior, por_igual, por_inferior)
                            brigadas_evaluadas.append(unidad_evaluada)


                        for unidad in unidades:
                            if unidad not in validar_und:
                                validar_und.append(unidad)
                                unidad_evaluada=""
                                brigadas = self.buscar_unidad(self.jerarquia_unidades, unidad)
                                self.indicadores=[]
                                posicion = [4,5]
                                self.validar_obj( brigadas[2], 1)
                                self.comparativo_mapa(unidad, posicion)
                                superior = 0
                                inferior = 0
                                igual = 0

                                for x in self.indicadores:
                                    if x > 0:
                                        superior =  superior +1
                                    elif x < 0:
                                        inferior = inferior +1
                                    else:
                                        igual = igual +1

                                total = len(self.indicadores)

                                por_superior = (superior/total)*100
                                por_inferior = (inferior/total)*100
                                por_igual = (igual/total)*100
                                unidad_evaluada = (unidad, total, por_superior, por_igual, por_inferior)
                                unidades_ut_evaluadas.append(unidad_evaluada)

                            #print(f"      UNIDAD: {unidad}")
        fill_pos=False
        fill_neg=False
        
        if self.filtro[30] == "asc":    
            unidades_evaluadas =self.ordenar_unidad(unidades_evaluadas, 2)
            brigadas_evaluadas =self.ordenar_unidad(brigadas_evaluadas, 2)
            unidades_ut_evaluadas =self.ordenar_unidad(unidades_ut_evaluadas, 2)
            fill_pos =True
            color =(152,251,152)
        else:
            unidades_evaluadas =self.ordenar_unidad(unidades_evaluadas, 4)
            brigadas_evaluadas =self.ordenar_unidad(brigadas_evaluadas, 4)
            unidades_ut_evaluadas =self.ordenar_unidad(unidades_ut_evaluadas, 4)
            fill_neg =True
            color =(193,30,38)

        encabezado_coe_div_compa(self.pdf, True, "DIVISIONES")
        self.pdf.set_line_width(0.1)
        self.pdf.set_fill_color(*color)
        self.pdf.set_draw_color(0, 0, 0)
        self.pdf.set_text_color(0,0,0)
        self.pdf.set_font('Arial', 'B', 12)
        for unidades_div in unidades_evaluadas:
            self.pdf.cell(35)
            self.pdf.cell(56,8, str(unidades_div[0]), border=1, align="L", fill=False)
            self.pdf.cell(35,8, str(formato_numero(unidades_div[1])), border=1, align="C", fill=False)
            self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[2])), border=1, align="C", fill=fill_pos)
            self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[3])), border=1, align="C", fill=False)
            self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[4])), border=1, align="C", fill=fill_neg)
            self.pdf.ln()

        self.pdf.ln()
        if brigadas_evaluadas:
                
            encabezado_coe_div_compa(self.pdf, True, "BRIGADAS")
            self.pdf.set_line_width(0.1)
            self.pdf.set_fill_color(*color)
            self.pdf.set_draw_color(0, 0, 0)
            self.pdf.set_text_color(0,0,0)
            self.pdf.set_font('Arial', 'B', 12)
            for unidades_div in brigadas_evaluadas:
                self.pdf.cell(35)
                self.pdf.cell(56,8, str(unidades_div[0]), border=1, align="L", fill=False)
                self.pdf.cell(35,8, str(formato_numero(unidades_div[1])), border=1, align="C", fill=False)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[2])), border=1, align="C", fill=fill_pos)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[3])), border=1, align="C", fill=False)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[4])), border=1, align="C", fill=fill_neg)
                self.pdf.ln()
            
            self.pdf.ln()
            encabezado_coe_div_compa(self.pdf, True, "UNIDADES")
            self.pdf.set_line_width(0.1)
            self.pdf.set_fill_color(*color)
            self.pdf.set_draw_color(0, 0, 0)
            self.pdf.set_text_color(0,0,0)
            self.pdf.set_font('Arial', 'B', 12)
            for unidades_div in unidades_ut_evaluadas:
                self.pdf.cell(35)
                self.pdf.cell(56,8, str(unidades_div[0]), border=1, align="L", fill=False)
                self.pdf.cell(35,8, str(formato_numero(unidades_div[1])), border=1, align="C", fill=False)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[2])), border=1, align="C", fill=fill_pos)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[3])), border=1, align="C", fill=False)
                self.pdf.cell(35,8, str(formato_numero_un_decimal(unidades_div[4])), border=1, align="C", fill=fill_neg)
                self.pdf.ln()

        #2025116010730863



        
