# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.a_a_boletin_estadistica_power_point.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.a_a_boletin_estadistica_power_point.models.funtions.componest.tablas import *
conexion_pos = Databa_bases()
import pandas as pd
import datetime
class Calculo_Spoa:
    def __init__(self, fecha_inicial_u_l, fecha_final_u_l, filtro):

            self.filtro = filtro
            dato = ""
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

            query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)

            resultados = conexion_pos.comando_query(query[0])
            self.hechos = conexion_pos.comando_query(query[1])
            erradicacion = conexion_pos.comando_query(query[2])
            # print(query[2])


            self.res_calculo = estadistica_resultados(resultados, self.hechos, filtro)



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

    def enemigo_nombre(self, id_unidad):


        divisiones = []


        divisiones_actual_heridos =[x[8] for x in self.hechos]

        

        for x in divisiones_actual_heridos:
            if x != "-":
                divisiones.append(x)

        divisiones = list(set(divisiones))
        hechos_devolver = []

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


        divisiones_actual_heridos =[x[id_unidad] for x in self.hechos]


        for x in divisiones_actual_heridos:
            if x != "-":
                divisiones.append(x)


        divisiones = list(set(divisiones))

        if self.filtro[0]=="---" or self.filtro[0]=="":
            unidades = ["DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "DAVAA", "DIVFE", "FUTCO", "FTCEC", "FUTOM", 'TREJC']
            divisiones = sorted(divisiones, key = lambda m: unidades.index(m))
        
        elif self.filtro[0]=="DIV06":
            unidades = ["CODIV6", "BR12", "BR26", "BR27", "FUDRA6"]
            divisiones = sorted(divisiones, key = lambda m: unidades.index(m))
        elif self.filtro[0]=="DIV01":
            unidades = ["CODIV1","BR02","BR04","BR10","BR11","BR17","BR19","FUDRA9","FTCMA","FUTAM"]
            divisiones = sorted(divisiones, key = lambda m: unidades.index(m))
        else:
            divisiones.sort()
   

        return [divisiones]

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


    def calculo_boletin_cuadro(self):
        
        if self.filtro[0]!="---" and self.filtro[0]!="" and self.filtro[2]=="---" and self.filtro[2]=="":
            id_unidad =4
            id_res = 3
            id_enemigo = 8
        elif self.filtro[2]!="---" and self.filtro[2]!="":
            id_unidad =5
            id_res = 4
            id_enemigo = 8
        
        elif self.filtro[0]!="---" and self.filtro[0]!="":
            id_unidad =4
            id_res = 3
            id_enemigo = 4
        else:
            id_unidad =2
            id_res = 1
            id_enemigo = 8
    

        divisiones_lis=[]
        nombre_columna=["DIVISION - RESULTADO"]      
        divisiones_lis =  Calculo_Spoa.divisiones_nombre(self, id_unidad)

        amenaza_lis=[]      
        amenaza_lis =  Calculo_Spoa.enemigo_nombre(self, id_enemigo)


        divisiones = divisiones_lis[0]

        nombre_columna.extend(divisiones_lis[0])
        nombre_columna.append("TOTAL")

        nombre_columna.extend(amenaza_lis[1])

        suma=[]
        constante=[]
        for x in divisiones:
            suma.append(18)
            constante.append(1)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 0,  "NO") #funcion para filtar el spoa
        RME = tabla_boletin_coe( valor[0], "MENORES RECUPERADOS", divisiones,  amenaza_lis[0], id_res)

   
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 1,  "NO") #funcion para filtar el spoa
        PRESENTACION = tabla_boletin_coe( valor[0], "PRESENTACIÓN VOLUNTARIA", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 2,  "NO") #funcion para filtar el spoa
        SOMETIMIENTOS = tabla_boletin_coe( valor[0], "SOMETIMIENTOS", divisiones,  amenaza_lis[0], id_res)

        # print(self.filtro[17], id_res)
        if self.filtro[17] == "sin_delco":
            valor_calculado = Calculo_Spoa.validar_spoa(self, self.filtro, self.res_calculo, 4, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        else:
            valor_calculado = Calculo_Spoa.validar_spoa(self, self.filtro, self.res_calculo, 3, "CAPTURAS", "SI" ) #funcion para filtar el spoa

        # valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 3,  "SI") #funcion para filtar el spoa
        CAPTURAS = tabla_boletin_coe( valor_calculado[0], "CAPTURAS", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 5,  "SI") #funcion para filtar el spoa
        MDOM = tabla_boletin_coe( valor[0], "MDOM", divisiones,  amenaza_lis[0], id_res)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 6,  "SI") #funcion para filtar el spoa
        ASESINADOS = tabla_boletin_coe( valor[0], "ASESINADOS POR ACCIÓN DEL ENEMIGO", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 7,  "SI") #funcion para filtar el spoa
        HERIDOS = tabla_boletin_coe( valor[0], "HERIDOS POR ACCIÓN DEL ENEMIGO", divisiones,  amenaza_lis[0], id_res)

        MUERTO_FUERA = tabla_boletin_coe( self.res_calculo[104], "MUERTO DIFERENTE ACCIÓN DEL ENEMIGO", divisiones,  amenaza_lis[0], id_res)
        HERIDO_FUERA = tabla_boletin_coe( self.res_calculo[105], "LESIONADO DIFERENTE ACCIÓN DEL ENEMIGO", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 8,  "SI") #funcion para filtar el spoa
        ARMAS_LARGAS = tabla_boletin_coe( valor[0], "ARMAS DE LARGO ALCANCE", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 9,  "SI") #funcion para filtar el spoa
        ARMAS_CORTAS = tabla_boletin_coe( valor[0], "ARMAS DE CORTO ALCANCE", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 10,  "SI") #funcion para filtar el spoa
        ARMAS_ACOMPANIAMIENTO = tabla_boletin_coe( valor[0], "ARMAS DE ACOMPAÑAMIENTO", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 11,  "SI") #funcion para filtar el spoa
        MUNICIONES = tabla_boletin_coe( valor[0], "MUNICIONES", divisiones,  amenaza_lis[0], id_res)

        COMABTES_POS = tabla_boletin_coe_hechos( self.res_calculo[12], "COMBATES POSITIVOS", divisiones,  amenaza_lis[0], id_unidad)
        COMBATES_NEG = tabla_boletin_coe_hechos( self.res_calculo[13], "COMBATES NEGATIVOS", divisiones,  amenaza_lis[0], id_unidad)
        COMBATES_SIN = tabla_boletin_coe_hechos( self.res_calculo[14], "COMBATES SIN RESULTADOS", divisiones,  amenaza_lis[0], id_unidad)
        TOTAL_COMATES = tabla_boletin_coe_hechos( self.res_calculo[15], "TOTAL DE COMBATES", divisiones,  amenaza_lis[0], id_unidad)

        ATAQUE_FUERZA_PUBLICA = tabla_boletin_coe_hechos( self.res_calculo[16], "ATAQUE A LA FUERZA PÚBLICA", divisiones,  amenaza_lis[0],id_unidad)

        ACTO_TERRORISMO = tabla_boletin_coe_hechos( self.res_calculo[100], "ACTO DE TERRORISMO", divisiones,  amenaza_lis[0], id_unidad)
        ACTO_TERRORISMO_INFRAESTRUCTURA = tabla_boletin_coe_hechos( self.res_calculo[101], "ACTO DE TERRORISMO CONTRA LA INFRAESTRUCTURA", divisiones,  amenaza_lis[0], id_unidad)
        ACTO_TERRORISMO_POBLACION = tabla_boletin_coe_hechos( self.res_calculo[102], "ACTO DE TERRORISMO CONTRA LA POBLACIÓN CIVIL", divisiones,  amenaza_lis[0], id_unidad)
        ACTO_TERRORISMO_TROPAS = tabla_boletin_coe_hechos( self.res_calculo[103], "ACTO DE TERRORISMO CONTRA LAS PROPIAS TROPAS", divisiones,  amenaza_lis[0], id_unidad)
        
        NEUTRALIZACION_TERRORITA =tabla_boletin_coe_hechos( self.res_calculo[17], "NEUTRALIZACIÓN TERRORISTA", divisiones,  amenaza_lis[0], id_unidad)

        HOSTIGAMIENTOS = tabla_boletin_coe( self.res_calculo[18], "HOSTIGAMIENTOS", divisiones,  amenaza_lis[0], id_res)
        ASONADAS = tabla_boletin_coe( self.res_calculo[19], "ASONADAS", divisiones,  amenaza_lis[0], id_res)
        ATAQUES_DRONS = tabla_boletin_coe( self.res_calculo[106], "ATAQUE CON DRONS", divisiones,  amenaza_lis[0], id_res)
        NEUTRALIZACION_DRONS = tabla_boletin_coe( self.res_calculo[107], "NEUTRALIZACIÓN DE DRONS", divisiones,  amenaza_lis[0], id_res)

        A_E = tabla_boletin_coe( self.res_calculo[21], "A.E", divisiones,  amenaza_lis[0], id_res)
        MAP = tabla_boletin_coe( self.res_calculo[22], "MAP(Mina Anti Persona)", divisiones,  amenaza_lis[0], id_res)
        EXPLOSIVOS = tabla_boletin_coe( self.res_calculo[23], "EXPLOSIVOS kg", divisiones,  amenaza_lis[0], id_res)
        EXPLOSIVOS_M = tabla_boletin_coe( self.res_calculo[24], "EXPLOSIVOS m", divisiones,  amenaza_lis[0], id_res)
        EXPLOSIVOS_UND = tabla_boletin_coe( self.res_calculo[25], "EXPLOSIVOS UND", divisiones,  amenaza_lis[0], id_res)
        CORDON_M = tabla_boletin_coe( self.res_calculo[26], "CORDÓN DETONANTE m", divisiones,  amenaza_lis[0], id_res)
        MECHA_LENTA = tabla_boletin_coe( self.res_calculo[27], "MECHA LENTA m", divisiones,  amenaza_lis[0], id_res)
        MEDIOS_LANZAMIENTOS = tabla_boletin_coe( self.res_calculo[28], "MEDIOS DE LANZAMIENTO", divisiones,  amenaza_lis[0], id_res)
        DECTONADORES = tabla_boletin_coe( self.res_calculo[29], "DECTONADORES ANELECTRICOS", divisiones,  amenaza_lis[0], id_res)
        DECTONADORES_ELECTRICOS = tabla_boletin_coe( self.res_calculo[30], "DECTONADORES ELECTRICOS", divisiones,  amenaza_lis[0], id_res)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 32,  "SI") #funcion para filtar el spoa
        COCAINA = tabla_boletin_coe( valor[0], "COCAÍNA Kg", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 33,  "SI") #funcion para filtar el spoa
        MAROHUANA = tabla_boletin_coe( valor[0], "MARIHUANA Kg ", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 34,  "SI") #funcion para filtar el spoa
        PBC = tabla_boletin_coe( valor[0], "PBC Kg ", divisiones,  amenaza_lis[0],id_res)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 35,  "SI") #funcion para filtar el spoa
        BASUCO = tabla_boletin_coe( valor[0], "BASUCO Kg ", divisiones,  amenaza_lis[0],id_res)
                
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 36,  "SI") #funcion para filtar el spoa
        HEROINA = tabla_boletin_coe( valor[0], "HEROÍNA Kg ", divisiones,  amenaza_lis[0],id_res)
                        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 37,  "SI") #funcion para filtar el spoa
        DROGAS = tabla_boletin_coe( valor[0], "DROGAS SINTETICAS ", divisiones,  amenaza_lis[0],id_res)
                                
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 46,  "SI") #funcion para filtar el spoa
        COCAINA_PROCESO = tabla_boletin_coe( valor[0], "COCAÍNA EN PROCESO ", divisiones,  amenaza_lis[0],id_res)
                                        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 47,  "SI") #funcion para filtar el spoa
        PBC_PROCESO = tabla_boletin_coe( valor[0], "PBC EN PROCESO ", divisiones,  amenaza_lis[0],id_res)
                                     
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 38,  "SI") #funcion para filtar el spoa
        LAB_HEROINA = tabla_boletin_coe( valor[0], "LAB. HEROÍNA", divisiones,  amenaza_lis[0],id_res)
                        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 39,  "SI") #funcion para filtar el spoa
        LAB_COCIANA = tabla_boletin_coe( valor[0], "LAB. CLORHIDRATO DE COCAINA", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 40,  "SI") #funcion para filtar el spoa
        LAB_PBC = tabla_boletin_coe( valor[0], "LAB. PASTA O BASE DE COCA", divisiones,  amenaza_lis[0],id_res)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 41,  "SI") #funcion para filtar el spoa
        SEMILLEROS = tabla_boletin_coe( valor[0], "SEMILLEROS", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 42,  "SI") #funcion para filtar el spoa
        MATAS_COCIANA = tabla_boletin_coe( valor[0], "MATA(S) DE COCA EN SEMILLERO", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 43,  "SI") #funcion para filtar el spoa
        INSUMOS_LIQUIDOS = tabla_boletin_coe( valor[0], "INSUMOS LIQUIDOS Gal", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 44,  "SI") #funcion para filtar el spoa
        INSUMOS_SOLIDOS = tabla_boletin_coe( valor[0], "INSUMOS SOLIDOS Kg ", divisiones,  amenaza_lis[0],id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 45,  "SI") #funcion para filtar el spoa
        COMBUSTIBLES_NARCOTRAFICO = tabla_boletin_coe( valor[0], "COMBUSTIBLES DE NARCOTRÁFICO", divisiones,  amenaza_lis[0],id_res)


        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 48,  "SI") #funcion para filtar el spoa
        CAPTURAS_AMAZONIA = tabla_boletin_coe( valor[0], "CAPTURAS PLAN AMAZONIA ", divisiones,  amenaza_lis[0], id_res)
        PLANTAULAS_SEMBRADAS = tabla_boletin_coe( self.res_calculo[49], "PLANTULAS SEMBRADAS ", divisiones,  amenaza_lis[0], id_res)
        MADERA_INCAUTADA = tabla_boletin_coe( self.res_calculo[50], "MADERA INCAUTADA ", divisiones,  amenaza_lis[0], id_res)
        ANIMALES_INCUATADOS = tabla_boletin_coe( self.res_calculo[51], "ANIMALES RECUPERADOS ", divisiones,  amenaza_lis[0], id_res)


        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 52,  "SI") #funcion para filtar el spoa
        CAPTURAS_MINERIA = tabla_boletin_coe( valor[0], "CAPTURAS MINERÍA ", divisiones,  amenaza_lis[0], id_res)
        MENORES_MINERIA = tabla_boletin_coe( self.res_calculo[53], "MENORES R. MINERÍA ", divisiones,  amenaza_lis[0], id_res)
        EIYM =  tabla_boletin_coe_hechos( self.res_calculo[54], "EIYM", divisiones,  amenaza_lis[0], id_unidad)
        UPM = tabla_boletin_coe( self.res_calculo[55], "UPM ILEGAL ", divisiones,  amenaza_lis[0], id_res)
        MAQUINARIA_PESADA = tabla_boletin_coe( self.res_calculo[56], "MAQUINARIA PESADA", divisiones,  amenaza_lis[0], id_res)
        EXCAVADORAS = tabla_boletin_coe( self.res_calculo[57], "EXCAVADORA(S) ", divisiones,  amenaza_lis[0], id_res)
        RESTRO_ESCAVADOREAS =tabla_boletin_coe( self.res_calculo[58], "RETROEXCAVADORA(S)  ", divisiones,  amenaza_lis[0], id_res)
        BULDOCER = tabla_boletin_coe( self.res_calculo[59], "BULDOCER(ES)  ", divisiones,  amenaza_lis[0], id_res)
        DRAGAS = tabla_boletin_coe( self.res_calculo[60], "DRAGA(S)", divisiones,  amenaza_lis[0], id_res)
        MAQUINARIA_AMARILLA = tabla_boletin_coe( self.res_calculo[111], "MAQUINARIA AMARILLA", divisiones,  amenaza_lis[0], id_res)
        COMBUSTIBLES_MINERIA = tabla_boletin_coe( self.res_calculo[63], "COMBUSTIBLES DE MINERÍA", divisiones,  amenaza_lis[0], id_res)
        EXPLOSIVOS_MINERIA_KG = tabla_boletin_coe( self.res_calculo[64], "EXPLOSIVOS EN MINERÍA kg", divisiones,  amenaza_lis[0], id_res)
        EXPLOSIVOS_MINERIA_M = tabla_boletin_coe( self.res_calculo[65], "EXPLOSIVOS EN MINERÍA m", divisiones,  amenaza_lis[0], id_res)
        MATEIRAL_TRANSPORTE = tabla_boletin_coe( self.res_calculo[67], "EXMATERIAL DE TRANSPORTE MINERÍA", divisiones,  amenaza_lis[0], id_res)
        COLTAN = tabla_boletin_coe( self.res_calculo[68], "COLTAN KG", divisiones,  amenaza_lis[0], id_res)

        LIBERADOS = tabla_boletin_coe( self.res_calculo[69], "LIBERADOS ", divisiones,  amenaza_lis[0], id_res)
        RESCATADOS = tabla_boletin_coe( self.res_calculo[70], "RESCATADOS", divisiones,  amenaza_lis[0], id_res)
        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 112,  "SI") #funcion para filtar el spoa
        CAPTURAS_EXTORCION = tabla_boletin_coe( valor[0], "CAPTURAS POR EXTORCIÓN ", divisiones,  amenaza_lis[0], id_res)
        PERSONAL_MIL_SECUESTRADO = tabla_boletin_coe( self.res_calculo[115], "PERSONAL MILITAR SECUESTRADO", divisiones,  amenaza_lis[0], id_res)
        PERSONAL_CIL_SECUESTRADO = tabla_boletin_coe( self.res_calculo[114], "PERSONAL CIVIL SECUESTRADO", divisiones,  amenaza_lis[0], id_res)

        valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_calculo, 89,  "SI") #funcion para filtar el spoa
        CAPTURAS_CONTRABANDO = tabla_boletin_coe( valor[0], "CAPTURAS DE CONTRABANDO ", divisiones,  amenaza_lis[0], id_res)
        COMBUSTIBLE_CONTRABANDO = tabla_boletin_coe( self.res_calculo[91], "COMBUSTIBLES DE CONTRABANDO", divisiones,  amenaza_lis[0], id_res)
        VEHICULOS_CONTRABANDO = tabla_boletin_coe( self.res_calculo[94], "VEHICULOS DE CONTRABANDO", divisiones,  amenaza_lis[0], id_res)
        INSUMOS_LIQUIDOS_CONTRABANDO = tabla_boletin_coe( self.res_calculo[95], "INSUMOS LIQUIDOS DE CONTRABANDO", divisiones,  amenaza_lis[0], id_res)
        INSUMOS_SOLIDOS_CONTRANDO = tabla_boletin_coe( self.res_calculo[95], "INSUMOS SOLIDOS DE CONTRABANDO", divisiones,  amenaza_lis[0], id_res)
        ANIMALES_CONTRANDO = tabla_boletin_coe( self.res_calculo[95], "ANIMALES DE CONTRABANDO INCAUTADOS", divisiones,  amenaza_lis[0], id_res)

        VALVULAS = tabla_boletin_coe( self.res_calculo[84], "VÁLVULAS", divisiones,  amenaza_lis[0], id_res)
        REFINERIAS = tabla_boletin_coe( self.res_calculo[85], "REFINERIAS ", divisiones,  amenaza_lis[0], id_res)
        PISCINAS = tabla_boletin_coe( self.res_calculo[83], "PISCINAS ", divisiones,  amenaza_lis[0], id_res)
        PETROLEO = tabla_boletin_coe( self.res_calculo[82], "PETROLEO ", divisiones,  amenaza_lis[0], id_res)
        AFECTACION_OLEODUCTO = tabla_boletin_coe( self.res_calculo[77], "AFECTACIÓN AL OLEODUCTO ", divisiones,  amenaza_lis[0], id_res)
        DEPOSITO = tabla_boletin_coe( self.res_calculo[86], "DEPÓSITO ILEGAL ", divisiones,  amenaza_lis[0], id_res)
        CAMPAMENTOS = tabla_boletin_coe( self.res_calculo[87], "CAMPAMENTOS", divisiones,  amenaza_lis[0], id_res)
        PROSELITISMO = tabla_boletin_coe( self.res_calculo[88], "PROSELITISMO ", divisiones,  amenaza_lis[0], id_res)

        return [nombre_columna, RME, PRESENTACION, SOMETIMIENTOS, CAPTURAS, MDOM, ASESINADOS, HERIDOS, MUERTO_FUERA, HERIDO_FUERA, ARMAS_LARGAS, ARMAS_CORTAS, ARMAS_ACOMPANIAMIENTO, MUNICIONES, COMABTES_POS, COMBATES_NEG, COMBATES_SIN, TOTAL_COMATES, ATAQUE_FUERZA_PUBLICA, ACTO_TERRORISMO, ACTO_TERRORISMO_INFRAESTRUCTURA, ACTO_TERRORISMO_POBLACION, ACTO_TERRORISMO_TROPAS, NEUTRALIZACION_TERRORITA, HOSTIGAMIENTOS, ASONADAS, ATAQUES_DRONS, NEUTRALIZACION_DRONS, A_E, MAP, EXPLOSIVOS, EXPLOSIVOS_M, EXPLOSIVOS_UND, CORDON_M, MECHA_LENTA, MEDIOS_LANZAMIENTOS, DECTONADORES, DECTONADORES_ELECTRICOS, COCAINA, MAROHUANA, PBC, BASUCO, HEROINA, DROGAS, COCAINA_PROCESO, PBC_PROCESO, LAB_HEROINA, LAB_COCIANA, LAB_PBC, SEMILLEROS, MATAS_COCIANA, INSUMOS_LIQUIDOS, INSUMOS_SOLIDOS, COMBUSTIBLES_NARCOTRAFICO, CAPTURAS_AMAZONIA, PLANTAULAS_SEMBRADAS, MADERA_INCAUTADA, ANIMALES_INCUATADOS, CAPTURAS_MINERIA, MENORES_MINERIA, EIYM, UPM, MAQUINARIA_PESADA, EXCAVADORAS, RESTRO_ESCAVADOREAS, BULDOCER, DRAGAS, MAQUINARIA_AMARILLA, COMBUSTIBLES_MINERIA, EXPLOSIVOS_MINERIA_KG, EXPLOSIVOS_MINERIA_M, MATEIRAL_TRANSPORTE, COLTAN, LIBERADOS, RESCATADOS, CAPTURAS_EXTORCION, PERSONAL_MIL_SECUESTRADO, PERSONAL_CIL_SECUESTRADO, CAPTURAS_CONTRABANDO, COMBUSTIBLE_CONTRABANDO, VEHICULOS_CONTRABANDO, INSUMOS_LIQUIDOS_CONTRABANDO, INSUMOS_SOLIDOS_CONTRANDO, ANIMALES_CONTRANDO, VALVULAS, REFINERIAS, PISCINAS, PETROLEO, AFECTACION_OLEODUCTO, DEPOSITO, CAMPAMENTOS, PROSELITISMO]
