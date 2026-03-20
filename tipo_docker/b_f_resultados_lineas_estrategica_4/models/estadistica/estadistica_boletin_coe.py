# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.b_f_resultados_lineas_estrategica_4.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.b_f_resultados_lineas_estrategica_4.models.funtions.componest.tablas import *

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

    def __init__(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro,  anio_act, anio_ant, fecha_titulo, fecha_titulo_dos ):
            self.filtro = filtro
            filtros = selecion_filtro(self.filtro)
            self.anio_act = anio_act
            self.anio_ant = anio_ant
            self.pdf =pdf
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

        divisiones_actual_heridos =[x[id_unidad] for x in self.res_calculo_act[7]]
        divisiones_actual_asesinados =[x[id_unidad] for x in self.res_calculo_act[6]]
        
        divisiones_anterior_heridos =[x[id_unidad] for x in self.res_calculo_ante[7]]
        divisiones_anterior_asesinados =[x[id_unidad] for x in self.res_calculo_ante[6]]

        for x in divisiones_actual_heridos:
            if x != "-":
                divisiones.append(x)

        for x in divisiones_actual_asesinados:
            if x != "-":
                divisiones.append(x)
                
        for x in divisiones_anterior_heridos:
            if x != "-":
                divisiones.append(x)
                
        for x in divisiones_anterior_asesinados:
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


        encabezado_comparativo_mapa_dos(self.pdf, True,  self.anio_act, self.anio_ant, 1, "ASESINADOS")
        self.pdf.ln()
        valor = encabezado_comparativo_enemigo_dinamico_1(self.pdf, True, valor_asesinados_ant[0], valor_asesinados[0], divisiones, 1, color, suma, constante, id_enemigo, self.indicadores)

        self.pdf.ln(restar)
        encabezado_comparativo_mapa_dos(self.pdf, True,  self.anio_act, self.anio_ant, 130, "HERIDOS")
        self.pdf.ln()
        valor_2 = encabezado_comparativo_enemigo_dinamico_1(self.pdf, True, valor_heridos_ant[0], valor_heridos[0], divisiones, 130, color, suma, constante, id_enemigo, self.indicadores)

        plt.clf()
        plt.cla()
        plt.close()
        plt.rcParams["figure.figsize"] = (10, 10)
        plt.figure()     
        try:

            # declaring data 
            data_pie = [] 
            keys = [] 
            colors = []

            ANIO=[]
            columns=[]
            explode = []

            data_pie.append(int(valor[0]))
            keys.append(self.anio_ant)
            explode.append(0)
            colors.append('#abebc6')


            data_pie.append(int(valor[1]))
            keys.append(self.anio_act)
            explode.append(0)
            colors.append('#196f3d')

            # declaring exploding pie 
            
            # define Seaborn color palette to use 
            palette_color = sns.color_palette('dark') 
            
            # plotting data on chart 
            font2 = {'family':'serif','color':'darkred','size':15}

            #sns.set(font_scale = 1.2)
            #plt.figure(figsize=(8,8))

            if valor[0]>1 and valor[1] >0:
                ax = plt.pie(data_pie, labels=keys, colors=colors, 
                    explode=explode, autopct=lambda p:f'{p*sum(data_pie)/100 :.0f} Ase.', pctdistance=1.2, labeldistance=1.4, textprops={'fontsize':40, 'weight':'bold'}, shadow=True, wedgeprops=dict(width=0.5)) 
            else:
                ax = plt.pie(data_pie, labels=keys, colors=colors, 
                    explode=explode, autopct=lambda p:f'{p*sum(data_pie)/100 :.0f} Ase.', pctdistance=0.7, labeldistance=1.1, textprops={'fontsize':40, 'weight':'bold'}, shadow=True, wedgeprops=dict(width=0.5),startangle=-50 ) 
            
            sns.despine()
            sns.color_palette("rocket")
            locs, labels = plt.xticks()
            plt.rcParams["figure.figsize"] = (200, 200)
            font1 = {'family':'serif','color':'darkred','size':40}
            

            #plt.title("CODE", fontdict = font1)


            plt.setp(labels)
            plt.tight_layout()
            
            # plotting data on chart 
            #plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code.png",  transparent=True )

            plt.clf()
        except:
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code.png",  transparent=True )

            plt.clf()
        self.pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code.png",55,120,75,75)
        #heridos 
           
        plt.clf()
        plt.cla()
        plt.close()
        plt.rcParams["figure.figsize"] = (10, 10)
        plt.figure()           
        try:

            # declaring data 
            data_pie = [] 
            keys = [] 
            colors = []

            ANIO=[]
            columns=[]
            explode = []


            data_pie.append(int(valor_2[0]))
            keys.append(self.anio_ant)
            explode.append(0)
            colors.append('#abebc6')


            data_pie.append(int(valor_2[1]))
            keys.append(self.anio_act)
            explode.append(0)
            colors.append('#196f3d')

            # declaring exploding pie 
            
            # define Seaborn color palette to use 
            palette_color = sns.color_palette('dark') 
            
            # plotting data on chart 
            font2 = {'family':'serif','color':'darkred','size':15}

            #sns.set(font_scale = 1.2)
            #plt.figure(figsize=(8,8))
            if valor_2[0]>1 and valor_2[1] >0:
                ax = plt.pie(data_pie, labels=keys, colors=colors, 
                    explode=explode, autopct=lambda p:f'{p*sum(data_pie)/100 :.0f} Her', pctdistance=1.2, labeldistance=1.4, textprops={'fontsize':40, 'weight':'bold'}, shadow=True, wedgeprops=dict(width=0.5)) 
            else:
                ax = plt.pie(data_pie, labels=keys, colors=colors, 
                    explode=explode, autopct=lambda p:f'{p*sum(data_pie)/100 :.0f} Her', pctdistance=0.7, labeldistance=1.1, textprops={'fontsize':40, 'weight':'bold'}, shadow=True, wedgeprops=dict(width=0.5),startangle=-50) 
            
            sns.despine()
            sns.color_palette("rocket")
            locs, labels = plt.xticks()
            plt.rcParams["figure.figsize"] = (200, 200)
            font1 = {'family':'serif','color':'darkred','size':40}
            

            #plt.title("CODE", fontdict = font1)

            plt.setp(labels)
            plt.tight_layout()
            
            # plotting data on chart 
            #plt.pie(data, labels=keys, colors=palette_color, autopct='%.0f%%')
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code_1.png",  transparent=True )
            plt.clf()

        except:
            plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code_1.png",  transparent=True )
            plt.clf()

        self.pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/b_f_resultados_lineas_estrategica_4/models/tortas/torta_code_1.png",185,120,75,75)
        ruta = self.filtro[15]
        if valor[2] < 0:
            self.pdf.set_text_color(0,128,0)
            triangulo = '{}static/img/tri_verde_new_neg_con.png'.format(ruta)

        elif valor[2] > 0:
            self.pdf.set_text_color(128,0,0)
            triangulo = '{}static/img/tri_rojo_new_pos_con.png'.format(ruta)

        else:
            self.pdf.set_text_color(232,172,2)
            triangulo = '{}static/img/tri_amarillo_new.png'.format(ruta)
        self.pdf.image(triangulo,88,160,10,10)#imagenes 

        if valor_2[2] < 0:
            self.pdf.set_text_color(0,128,0)
            triangulo = '{}static/img/tri_verde_new_neg_con.png'.format(ruta)

        elif valor_2[2] > 0:
            self.pdf.set_text_color(128,0,0)
            triangulo = '{}static/img/tri_rojo_new_pos_con.png'.format(ruta)

        else:
            self.pdf.set_text_color(232,172,2)
            triangulo = '{}static/img/tri_amarillo_new.png'.format(ruta)
        self.pdf.image(triangulo,218,160,10,10)#imagenes 

        asesinados = '{}static/img/asesinados.jpeg'.format(ruta)
        heridos = '{}static/img/heridos.jpeg'.format(ruta)

        self.pdf.image(asesinados,5,140,15,15)#imagenes 
        self.pdf.image(heridos,140,140,15,15)#imagenes 

        self.pdf.set_font('Calibri', 'B', 16)
        self.pdf.set_text_color(0,0,0)
        self.pdf.text(20, 150, "ASESINADOS")
        self.pdf.text(160, 150, "HERIDOS")

        ase = str(valor[3])+" %"
 
        her = str(valor_2[3])+" %"
        tan= len(ase)
        inicio = 80
        final = 95
        mita = (((final-inicio)/2)-(tan/2)+inicio)+2
        self.pdf.text(mita, 158, str(ase))

        tan= len(her)
        inicio = 209
        final = 224
        mita = (((final-inicio)/2)-(tan/2)+inicio)+2
        self.pdf.text(mita, 158, str(her))


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


   
        if por_superior == 0:
            img_verde = "cero"
        elif por_superior > 0 and por_superior <= 10:
            img_verde = "10 verde"
        elif por_superior > 10 and por_superior <= 20:
            img_verde = "20 verde"
        elif por_superior > 20 and por_superior <= 30:
            img_verde = "30 verde"
        elif por_superior > 30 and por_superior <= 40:
            img_verde = "40 verde"
        elif por_superior > 40 and por_superior <= 50:
            img_verde = "50 verde"
        elif por_superior > 50 and por_superior <= 60:
            img_verde = "60 verde"
        elif por_superior > 60 and por_superior <= 70:
            img_verde = "70 verde"
        elif por_superior > 70 and por_superior <= 80:
            img_verde = "80 verde"
        elif por_superior > 80 and por_superior <= 90:
            img_verde = "90 verde"
        elif por_superior > 90 and por_superior <= 100:
            img_verde = "100 verde"

               
        if por_igual == 0:
            img_amarillo = "cero"
        elif por_igual > 0 and por_igual <= 10:
            img_amarillo = "10 amarillo"
        elif por_igual > 10 and por_igual <= 20:
            img_amarillo = "20 amarillo"
        elif por_igual > 20 and por_igual <= 30:
            img_amarillo = "30 amarillo"
        elif por_igual > 30 and por_igual <= 40:
            img_amarillo = "40 amarillo"
        elif por_igual > 40 and por_igual <= 50:
            img_amarillo = "50 amarillo"
        elif por_igual > 50 and por_igual <= 60:
            img_amarillo = "60 amarillo"
        elif por_igual > 60 and por_igual <= 70:
            img_amarillo = "70 amarillo"
        elif por_igual > 70 and por_igual <= 80:
            img_amarillo = "80 amarillo"
        elif por_igual > 80 and por_igual <= 90:
            img_amarillo = "90 amarillo"
        elif por_igual > 90 and por_igual <= 100:
            img_amarillo = "100 amarillo"

               
        if por_inferior == 0:
            img_rojo = "cero"
        elif por_inferior > 0 and por_inferior <= 10:
            img_rojo = "10 rojo"
        elif por_inferior > 10 and por_inferior <= 20:
            img_rojo = "20 rojo"
        elif por_inferior > 20 and por_inferior <= 30:
            img_rojo = "30 rojo"
        elif por_inferior > 30 and por_inferior <= 40:
            img_rojo = "40 rojo"
        elif por_inferior > 40 and por_inferior <= 50:
            img_rojo = "50 rojo"
        elif por_inferior > 50 and por_inferior <= 60:
            img_rojo = "60 rojo"
        elif por_inferior > 60 and por_inferior <= 70:
            img_rojo = "70 rojo"
        elif por_inferior > 70 and por_inferior <= 80:
            img_rojo = "80 rojo"
        elif por_inferior > 80 and por_inferior <= 90:
            img_rojo = "90 rojo"
        elif por_inferior > 90 and por_inferior <= 100:
            img_rojo = "100 rojo"


        titulo = "COMPARATIVO RESULTADOS {}/{}".format(self.anio_ant, self.anio_act)

        self.pdf.cell(30)
        self.pdf.cell(120,10,str(titulo),1,0,"C",True)
        self.pdf.cell(40,10,str("CANTIDAD"),1,0,"C",True)
        self.pdf.cell(40,10,str("%"),1,0,"C",True)
        
        titulo = "TOTAL INDICADORES SUPERIORES".format(self.anio_ant)
        self.pdf.ln()
        self.pdf.cell(30)
        self.pdf.cell(120,10,str(titulo),1,0,"L",False)
        self.pdf.cell(40,10,str(superior),1,0,"C",False)
        self.pdf.cell(40,10,str(formato_numero_un_decimal((superior/total)*100)),1,0,"C",False)

                            
        titulo = "TOTAL INDICADORES IGUALES".format(self.anio_ant)
        self.pdf.ln()
        self.pdf.cell(30)
        self.pdf.cell(120,10,str(titulo),1,0,"L",False)
        self.pdf.cell(40,10,str(igual),1,0,"C",False)
        self.pdf.cell(40,10,str(formato_numero_un_decimal((igual/total)*100)),1,0,"C",False)
            
        titulo = "TOTAL INDICADORES INFERIORES".format(self.anio_ant)
        self.pdf.ln()
        self.pdf.cell(30)
        self.pdf.cell(120,10,str(titulo),1,0,"L",False)
        self.pdf.cell(40,10,str(inferior),1,0,"C",False)
        self.pdf.cell(40,10,str(formato_numero_un_decimal((inferior/total)*100)),1,0,"C",False)


                   
        titulo = "TOTAL INDICADORES EVALUADOS".format(self.anio_ant)
        self.pdf.ln(125)
        self.pdf.cell(30)
        self.pdf.cell(120,10,str(titulo),1,0,"L",True)
        self.pdf.cell(40,10,str(len(self.indicadores)),1,0,"C",True)
        self.pdf.cell(40,10,str("100%"),1,0,"C",True)

        ruta = self.filtro[15]
        reloj = '{}static/img/reloj/reloj.png'.format(ruta)
        verde = '{}static/img/reloj/verde.png'.format(ruta)
        amrillo = '{}static/img/reloj/amarillo.png'.format(ruta)
        rojo = '{}static/img/reloj/rojo.png'.format(ruta)

        indicador_verde_reloj = '{}static/img/reloj/{}.png'.format(ruta, img_verde)
        indicador__amarillo_reloj = '{}static/img/reloj/{}.png'.format(ruta, img_amarillo)
        indicador__rojo_reloj = '{}static/img/reloj/{}.png'.format(ruta, img_rojo)

 


        self.pdf.image(reloj,10,100,80,80)
        self.pdf.image(indicador_verde_reloj,26,115.5,47,47)
        self.pdf.image(reloj,100,100,80,80)
        self.pdf.image(indicador__amarillo_reloj,116,115.5,47,47)
        self.pdf.image(reloj,190,100,80,80)
        self.pdf.image(indicador__rojo_reloj,206,115.5,47,47)

        self.pdf.image(verde,35,170,30,10)
        

        self.pdf.image(amrillo,125,170,30,10)
        self.pdf.image(rojo,215,170,30,10)

        self.pdf.set_text_color(10,10,10)
        self.pdf.set_font('Arial', 'B', 14)

        por_superior = formato_numero_un_decimal(por_superior)
        por_inferior = formato_numero_un_decimal(por_inferior)
        por_igual = formato_numero_un_decimal(por_igual) 

        por_superior = str(por_superior)+" %"
        por_inferior =  str(por_inferior)+" %"
        por_igual = str(por_igual)+" %"

        self.pdf.text(42, 177, str(por_superior))

        self.pdf.text(133, 177, str(por_igual))

        self.pdf.text(222, 177, str(por_inferior))

     



        
