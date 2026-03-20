# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.b_f_power_point_obj2.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.b_f_power_point_obj2.models.funtions.componest.tablas import *

conexion_pos = Databa_bases()
import json
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import psycopg2
import sys

class Calculo_Spoa:

    def __init__(self, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant ):

            self.filtro = filtro
            #leer objectivos por unidades
            ruta = self.filtro[15] 
            json_ruta = '{}static/obj_2_diferencial_divisiones.json'.format(ruta)
            json_ruta_br = '{}static/INDICADORES OBJ_JSON_BR.json'.format(ruta)


            self.obj_2 = ['SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI','SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI']
            
            if filtro[2] != "" and filtro[2] != "---":
                self.obj_2  = validar_indicador_unidad(json, json_ruta_br, filtro[2])
            elif filtro[0] != "" and filtro[0] != "-":

                self.obj_2  = validar_indicador_unidad(json, json_ruta, filtro[0])

            if  self.obj_2 == []:
                self.obj_2 = ['SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI','SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI', 'SI']  

            self.numero =1        
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant
             

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
    
    def validar_rango_si(lista, rango):

        inicio, fin = rango

        for i in range(inicio, fin + 1):

            if i < len(lista):

                if str(lista[i]).strip().upper() == "SI":
                    return True

        return False


    def comparativo_mapa(self):

        data = [
            ["No.","AMENAZA","EVENTO",
            f"{self.anio_ant}",
            f"{self.anio_act}",
            "DIFERENCIA","PORCENTAJE","SEMAFORIZACIÓN"]
        ]

        valor_mdom = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 5, "SI")
        valor_mdom_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 5, "SI")

        valor_cap = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_act, 4, "SI")
        valor_cap_ant = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo_ante, 4, "SI")

        datos = [self.res_calculo_act[0], self.res_calculo_act[2], valor_cap[0], valor_mdom[0]]
        datos_ant = [self.res_calculo_ante[0], self.res_calculo_ante[2], valor_cap_ant[0], valor_mdom_ant[0]]

        texto = [
            "MENORES RECUPERADOS",
            "SOMETIMIENTOS A LA JUSTICIA",
            "CAPTURAS",
            "MDOM"
        ]

        suma = 18
        constante = 1

        # configuración de enemigos
        configuracion = [

            {"rango":[0,3],  "id":7,  "amenaza":["GAO - Residual Disidencias FARC","GAO-r"]},
            {"rango":[4,7],  "id":7,  "amenaza":["GAO ELN","GAO ELN"]},

            {"rango":[8,11], "id":7,
            "amenaza":
            ["GAO COMUNEROS DEL SUR","GAO-CS"]
            if self.filtro[2] == "FUDRA2"
            else ["GAO CLAN DEL GOLFO","GAO-CG"]
            },

            {"rango":[12,15], "id":7,  "amenaza":["GDO","GDO"]},

            {"rango":[16,19], "id":39, "amenaza":["LOS PACHENCA","GAO ACSN"]}
        ]

        indicador = None

        for bloque in configuracion:

            rango = bloque["rango"]

            # 🔎 VALIDAR SI EXISTE "SI" EN EL RANGO
            if not Calculo_Spoa.validar_rango_si(self.obj_2, rango):
                continue

            indicador = encabezado_comparativo_enemigo_dinamico(
                datos_ant,
                datos,
                bloque["amenaza"],
                suma,
                constante,
                bloque["id"],
                texto,
                self.indicadores,
                self.obj_2,
                rango,
                self.numero,
                data
            )

            self.numero = indicador[2]
            self.indicadores = indicador[1]

        return indicador

        
    def comparativo_mapa_2(self):

        resultados = []

        bloques = [

            # BLOQUE 1
            {
                "rango":[20,23],
                "texto":[
                    "ARMAS DE LARGO ALCANCE",
                    "ARMAS DE CORTO ALCANCE",
                    "ARMAS DE ACOMPAÑAMIENTO",
                    "MUNICIONES"
                ],
                "indices":[8,9,10,11],
                "suma":[18,18,18,18],
                "constante":[1,1,1,1],
                "tipo":"spoa"
            },

            # BLOQUE 2
            {
                "rango":[24,27],
                "texto":[
                    "COMBATES POSITIVOS",
                    "COMBATES NEGATIVOS",
                    "COMBATES SIN RESULTADOS",
                    "TOTAL COMBATES"
                ],
                "indices":[12,13,14,15],
                "suma":[14,14,14,14],
                "constante":[1,-1,1,1],
                "tipo":"directo"
            },

            # BLOQUE 3
            {
                "rango":[28,35],
                "texto":[
                    "ARTEFACTO EXPLOSIVO (AE)",
                    "MINA ANTIPERSONA (MAP)",
                    "EXPLOSIVOS (KG)",
                    "CORDÓN DETONANTE (MT)",
                    "CORDÓN SEGURIDAD (MT)",
                    "DETONADORES ANELÉCTRICOS",
                    "DETONADORES ELÉCTRICOS",
                    "MEDIOS DE LANZAMIENTO"
                ],
                "indices":[21,22,23,26,27,29,30,28],
                "suma":[18]*8,
                "constante":[1]*8,
                "tipo":"directo"
            },

            # BLOQUE 4
            {
                "rango":[36,45],
                "texto":[
                    "COCAÍNA (KG)",
                    "MARIHUANA (KG)",
                    "HEROÍNA (KG)",
                    "PASTA BASE DE COCA (KG)",
                    "LABORATORIO CLORHIDRATO DE COCAÍNA",
                    "LABORATORIO PASTA BASE DE COCA",
                    "SEMILLEROS",
                    "MATAS DE COCA EN SEMILLEROS",
                    "INSUMOS LÍQUIDOS (GAL)",
                    "INSUMOS SÓLIDOS (KG)"
                ],
                "indices":[32,33,36,34,39,40,41,42,43,44],
                "suma":[18]*10,
                "constante":[1]*10,
                "tipo":"spoa"
            },

            # BLOQUE 5
            {
                "rango":[46,49],
                "texto":[
                    "CAPTURAS MINERÍA ILEGAL",
                    "EQUIPO LÍNEA AMARILLA",
                    "DRAGAS",
                    "COLTÁN (KG)"
                ],
                "indices":[52,111,60,68],
                "suma":[18]*4,
                "constante":[1]*4,
                "tipo":"spoa"
            },

            # BLOQUE 6
            {
                "rango":[50,52],
                "texto":[
                    "CAPTURAS EXTORSIÓN Y SECUESTRO",
                    "LIBERADOS",
                    "RESCATADOS"
                ],
                "indices":[112,69,70],
                "suma":[18]*3,
                "constante":[1]*3,
                "tipo":"spoa"
            },

            # BLOQUE 7
            {
                "rango":[53,55],
                "texto":[
                    "VÁLVULAS",
                    "REFINERÍAS",
                    "HIDROCARBUROS (GAL)"
                ],
                "indices":[84,85,82],
                "suma":[18]*3,
                "constante":[1]*3,
                "tipo":"directo"
            },

            # BLOQUE 8
            {
                "rango":[56,59],
                "texto":[
                    "CAPTURAS LOE AMAZONÍA",
                    "MADERA INCAUTADA (M3)",
                    "ANIMALES INCAUTADOS",
                    "PLÁNTULAS SEMBRADAS"
                ],
                "indices":[48,50,51,49],
                "suma":[18]*4,
                "constante":[1]*4,
                "tipo":"spoa"
            }

        ]


        for bloque in bloques:

            data = [[
            "No.","AMENAZA","EVENTO",
            f"{self.anio_ant}",
            f"{self.anio_act}",
            "DIFERENCIA","PORCENTAJE","SEMAFORIZACIÓN"
            ]]

            rango = bloque["rango"]

            if not Calculo_Spoa.validar_rango_si(self.obj_2, rango):

                resultados.append(data)
                continue


            datos=[]
            datos_ant=[]

            for idx in bloque["indices"]:

                if bloque["tipo"]=="spoa":

                    val = Calculo_Spoa.validar_spoa_unidad(
                        self,self.filtro,self.res_calculo_act,idx,"SI"
                    )

                    val_ant = Calculo_Spoa.validar_spoa_unidad(
                        self,self.filtro,self.res_calculo_ante,idx,"SI"
                    )

                    datos.append(val[0])
                    datos_ant.append(val_ant[0])

                else:

                    datos.append(self.res_calculo_act[idx])
                    datos_ant.append(self.res_calculo_ante[idx])


            indicadores = encabezado_comparativo_enemigo_dinamico_2(
                datos_ant,
                datos,
                bloque["suma"],
                bloque["constante"],
                bloque["texto"],
                self.indicadores,
                self.obj_2,
                rango,
                self.numero,
                data
            )

            resultados.append(indicadores[0])

            self.numero = indicadores[2]
            self.indicadores = indicadores[1]


        return resultados


    def evaluacion(self):
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
        
        return [total, por_superior, por_inferior, por_igual, superior, inferior, igual]


