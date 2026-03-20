# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.b_f_resultados_lineas_estrategicas_paya_power.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.b_f_resultados_lineas_estrategicas_paya_power.models.funtions.componest.tablas import *

conexion_pos = Databa_bases()
import json
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import psycopg2
import sys

class Calculo_Spoa:

    def __init__(self,  fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant, fecha_titulo, fecha_titulo_dos ):

            self.filtro = filtro
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant

            self.fecha_titulo = fecha_titulo
            self.fecha_titulo_dos = fecha_titulo_dos
            self.indicadores = []

            self.fecha_inicial_u_l = fecha_inicial_u_l
            self.fecha_final_u_l = fecha_final_u_l

            query_actual = parametros(self.fecha_inicial_u_l, self.fecha_final_u_l, filtros, filtro)
            query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)

            resultados_actual = conexion_pos.comando_query(query_actual[0])
            
            self.hechos_actual = conexion_pos.comando_query(query_actual[1])
            erradicacion_actual = conexion_pos.comando_query(query_actual[2])

            resultados_anterior = conexion_pos.comando_query(query_anterior[0])
            self.hechos_anterior = conexion_pos.comando_query(query_anterior[1])
            erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

            self.res_calculo_ante = estadistica_resultados(resultados_anterior, self.hechos_anterior, filtro)
            self.res_calculo_act = estadistica_resultados(resultados_actual, self.hechos_actual, filtro)

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

    def comparativo_mapa(self):
       
        valor_capturas = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 111,  "SI") #funcion para filtar el spoa
        valor_capturas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 111,  "SI") #funcion para filtar el spoa

        valor_capturas_internas = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 112,  "SI") #funcion para filtar el spoa
        valor_capturas_internas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 112,  "SI") #funcion para filtar el spoa

        valor_cocaina = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 32,  "SI") #funcion para filtar el spoa
        valor_cocaina_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 32,  "SI") #funcion para filtar el spoa
        
        valor_marihuana = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        valor_marihuana_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 33,  "SI") #funcion para filtar el spoa

        valor_pbc = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 34,  "SI") #funcion para filtar el spoa
        valor_pbc_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 34,  "SI") #funcion para filtar el spoa
        
        valor_lab_clor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act,  39,  "SI") #funcion para filtar el spoa
        valor_lab_clor_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 39,  "SI") #funcion para filtar el spoa
                        
        valor_lab_pbc = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 40,  "SI") #funcion para filtar el spoa
        valor_lab_pbc_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 40,  "SI") #funcion para filtar el spoa
                        
        valor_cocaina_proceso = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 46,  "SI") #funcion para filtar el spoa
        valor_cocaina_proceso_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 46,  "SI") #funcion para filtar el spoa
                        
                            
        valor_semilleros= Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 41,  "SI") #funcion para filtar el spoa
        valor_semilleros_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 41,  "SI") #funcion para filtar el spoa

        valor_matas_semilleros= Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 42,  "SI") #funcion para filtar el spoa
        valor_matas_semilleros_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 42,  "SI") #funcion para filtar el spoa

                                        
        valor_insumos_liquidas= Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 43,  "SI") #funcion para filtar el spoa
        valor_insumos_liquidas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 43,  "SI") #funcion para filtar el spoa
                                                
        valor_insumos_solidas= Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 44,  "SI") #funcion para filtar el spoa
        valor_insumos_solidas_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 44,  "SI") #funcion para filtar el spoa
                                                         
        valor_herohina_= Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 36,  "SI") #funcion para filtar el spoa
        valor_herohina__ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 36,  "SI") #funcion para filtar el spoa
        capturas = valor_capturas[0] +  valor_capturas_internas[0]
        capturas_ant = valor_capturas_ant[0] + valor_capturas_internas_ant[0]
        
        datos = [capturas, valor_cocaina[0], valor_marihuana[0],  valor_pbc[0], valor_lab_clor[0], valor_lab_pbc[0], valor_cocaina_proceso[0], valor_semilleros[0], valor_matas_semilleros[0]]

        datos_ant = [capturas_ant, valor_cocaina_ant[0], valor_marihuana_ant[0], valor_pbc_ant[0], valor_lab_clor_ant[0], valor_lab_pbc_ant[0], valor_cocaina_proceso_ant[0], valor_semilleros_ant[0], valor_matas_semilleros_ant[0]]

        self.indicadores = encabezado_comparativo_enemigo_dinamico_2( datos_ant, datos)

        return self.indicadores
        


 