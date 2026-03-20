# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.b_f_resultados_lineas_estrategica_4_power.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.b_f_resultados_lineas_estrategica_4_power.models.funtions.componest.tablas import *

conexion_pos = Databa_bases()
import json
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import psycopg2
import sys

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

class Calculo_Spoa:

    def __init__(self, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant, fecha_titulo, fecha_titulo_dos ):

            self.filtro = filtro
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant
            
            self.fecha_titulo = fecha_titulo
            self.fecha_titulo_dos = fecha_titulo_dos
            self.indicadores = []

            self.fecha_inicial_u_l = fecha_inicial_u_l
            self.fecha_final_u_l = fecha_final_u_l

            self.fecha_inicial_p_l = fecha_inicial_p_l
            self.fecha_final_p_l = fecha_final_p_l

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

    def divisiones_nombre(self, id_unidad):

        divisiones = []

        # Extraer divisiones desde los datos
        divisiones_actual_heridos = [x[id_unidad] for x in self.res_calculo_act[7]]
        divisiones_actual_asesinados = [x[id_unidad] for x in self.res_calculo_act[6]]
        divisiones_anterior_heridos = [x[id_unidad] for x in self.res_calculo_ante[7]]
        divisiones_anterior_asesinados = [x[id_unidad] for x in self.res_calculo_ante[6]]

        # Llenar lista solo con valores válidos
        for x in (divisiones_actual_heridos + divisiones_actual_asesinados +
                divisiones_anterior_heridos + divisiones_anterior_asesinados):
            if x != "-":
                divisiones.append(x)

        # Eliminar duplicados
        divisiones = list(set(divisiones))

        # Definir la tabla de orden según filtro
        if self.filtro[0] in ("---", ""):
            unidades = ["DIV01", "DIV02", "DIV03", "DIV04", "DIV05",
                        "DIV06", "DIV07", "DIV08", "DAVAA", "DIVFE",
                        "FUTCO", "FTCEC", "FUTOM", "TREJC"]

        elif self.filtro[0] == "DIV06" and self.filtro[1] !="" and self.filtro[1] !="---"  :
            unidades = ["CODIV6", "BR12", "BR26", "BR27", "FUDRA6"]

        elif self.filtro[0] == "DIV01" and self.filtro[1] !="" and self.filtro[1] !="---"  :
            unidades = ["CODIV1", "BR02", "BR04", "BR10", "BR11",
                        "BR17", "BR19", "FUDRA9", "FTCMA", "FUTAM"]
            

        else:
            # Si el filtro no coincide con nada, ordenar alfabéticamente
            divisiones.sort()
            return [divisiones]

        # --- ORDEN SEGURO ---
        # Unidades no encontradas se envían al final y se ordenan alfabéticamente
        divisiones_ordenadas = sorted(
            divisiones,
            key=lambda m: (unidades.index(m) if m in unidades else 999, m)
        )

        return [divisiones_ordenadas]

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
     
        sepador_mapa_dos(self.pdf, True, "AFECTACIÓN A PROPIAS TROPAS", 10, 220)
        self.pdf.ln()
        encabezado_comparativo_mapa(self.pdf, True,  self.anio_act, self.anio_ant, 10)
        self.pdf.ln()

        valor_heridos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        valor_heridos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        
        valor_asesinados = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        valor_asesinados_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 6,  "SI") #funcion para filtar el spoa


        datos = [valor_heridos[0], valor_asesinados[0]]
        datos_ant = [valor_heridos_ant[0], valor_asesinados_ant[0]]
        texto=["Asesinados","Heridos"]
        divisiones=[]
        if self.filtro[0]!="---" and self.filtro[0]!="":
            divisiones.append(self.filtro[0])
            
        else:
            divisiones=["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","DAVAA","DIVFE","FUTOM", "TREJC"]

        #color=[[137, 187, 169],[55, 165, 255],[208, 208, 182],[180, 180, 180]]
        color=[255, 255, 255]
        suma=[18,18,18,18,18,18,18,18,18,18,18,18]
        constante=[-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
        encabezado_comparativo_enemigo_dinamico(self.pdf, True, datos_ant, datos, divisiones, 10, color, suma, constante, 1, texto, self.indicadores)
        
             
        sepador_mapa_dos(self.pdf, True, "AFECTACIÓN A PROPIAS TROPAS", 10, 220)
        self.pdf.ln()
        encabezado_comparativo_mapa(self.pdf, True,  self.anio_act, self.anio_ant, 10)
        self.pdf.ln()
        encabezado_comparativo_enemigo_dinamico_TOTAL(self.pdf, True, datos_ant, datos, divisiones, 10, color, suma, constante, 1, texto, self.indicadores)
     
    def comparativo(self):

        if self.filtro[0]!="---" and self.filtro[0]!="" and self.filtro[2]=="---" and self.filtro[2]=="":
            id_unidad =3
            id_enemigo = 3
        elif self.filtro[2]!="---" and self.filtro[2]!="":
            id_unidad =4
            id_enemigo = 4
        
        elif self.filtro[0]!="---" and self.filtro[0]!="":
            id_unidad =3
            id_enemigo = 3
        else:
            id_unidad =1
            id_enemigo = 1
    

        divisiones_lis=[]      
        divisiones_lis =  Calculo_Spoa.divisiones_nombre(self, id_unidad)


        divisiones = divisiones_lis[0]
 
        suma=[]
        constante=[]
        for x in divisiones:
            suma.append(18)
            constante.append(1)


        valor_heridos = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        valor_heridos_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        
        valor_asesinados = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        valor_asesinados_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 6,  "SI") #funcion para filtar el spoa


        tamanio = len(divisiones)
        restar= ((tamanio*5)+15)*-1
   
        #color=[[137, 187, 169],[55, 165, 255],[208, 208, 182],[180, 180, 180]]
        color=[255, 255, 255]


        valor = encabezado_comparativo_enemigo_dinamico_1(True, valor_asesinados_ant[0], valor_asesinados[0], divisiones, 1, color, suma, constante, id_enemigo, self.indicadores)

        valor_1 = encabezado_comparativo_enemigo_dinamico_1(True, valor_heridos_ant[0], valor_heridos[0], divisiones, 1, color, suma, constante, id_enemigo, self.indicadores)

 
        return [valor[0],valor_1[0],valor[1],valor_1[1]]