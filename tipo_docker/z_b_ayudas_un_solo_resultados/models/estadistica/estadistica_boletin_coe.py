# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.z_b_ayudas_un_solo_resultados.models.conexion_pos import Databa_bases
from tipo_docker.z_b_ayudas_un_solo_resultados.models.funtions.funciones import *
from tipo_docker.z_b_ayudas_un_solo_resultados.models.funtions.componest.tablas import *
from tipo_docker.z_b_ayudas_un_solo_resultados.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import json
import pandas as pd
import seaborn as sns
import datetime
import numpy as np
import psycopg2
import sys

class Calculo_Spoa:
    def __init__(self):
            pass
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
    
    def meses_nombre(self, divisiones_lis, resultados, hechos):
        divisiones=[]
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]
        años = []

        for x in resultados:
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

    def enemigo_nombre(self, divisiones_lis, resultados, hechos):
        divisiones=[]
        divisiones = divisiones_lis
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]

        for x in resultados:
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

    def divisiones_nombre(self, divisiones_lis, resultados, hechos, fecha_inicial_u_l, fecha_final_u_l):
        divisiones=[]
        divisiones = divisiones_lis
        numero = 0
        filtro_hechos=[]
        hechos_devolver=[]
        print(len(resultados))
        for y in resultados:
            print(len(y))
            if y !=[]:
                if numero == 12 or numero == 13 or numero == 14 or numero == 15 or numero == 16 or numero == 17 or numero == 54 or numero == 98 or numero == 99 or numero == 100 or numero == 101 or numero == 102 or numero == 103:
    
                    filtro_hechos =[x[18] for x in resultados[numero]]
                    filtro_hechos = tuple(set(filtro_hechos))

                    divisiones =[x[2] for x in resultados[numero]]
                    divisiones = list(set(divisiones))
                    print("-//-")
                else:
                    
                    filtro_hechos =[x[26] for x in resultados[numero]]
                    filtro_hechos = tuple(set(filtro_hechos))
                    print("---")
                    divisiones =[x[1] for x in resultados[numero]]
                    divisiones = list(set(divisiones))

                        

            numero = numero + 1


        #print(y[1])

        #hechos_devolver = [x for x in hechos if x[18] in filtro_hechos]

        querys_hechos = "SELECT * FROM view_hechos_materializados WHERE fecha_hecho >= '{}'  AND fecha_hecho <= '{} ' and hr in {}  ORDER BY fecha_hecho ASC".format(fecha_inicial_u_l, fecha_final_u_l, filtro_hechos )
 
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
    def comparativo_mapa(self, pdf, fecha_inicial_u_l, fecha_final_u_l, filtro):

        ruta = filtro[15] 
        json_ruta = '{}static/MUNICIPIOS filtrados.json'.format(ruta)

        dato =""
        dato_res=""
        filtros_2 = selecion_filtro(filtro, dato, dato_res)
        query_actual_2 = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros_2, filtro)

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
            nueva_2=[]
            departamento_tuple=[]
            for x in data:
                for y in data[x]:
                    if y['AGR_DIV'] == filtro[0]:
                        nueva_2.append(y['MPIO'])
                        departamento_tuple.append(y['DPTO'])
        dato =""
        dato_res=""
        departamento_tuple = list(set(departamento_tuple))
        if len(nueva_2) > 1:
                ids = tuple(nueva_2)
                ids_2 = tuple(departamento_tuple)

                dato = "and dpto in {} and mpio in {}".format(ids_2, ids)
                dato_res= "and hop_depto in {} and hop_mpio in {}".format(ids_2, ids)
        
               
        filtros = selecion_filtro(filtro, dato, dato_res)
        query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)


        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        
        resultados_actual_2 = conexion_pos.comando_query(query_actual_2[0])
        hechos_actual_2 = conexion_pos.comando_query(query_actual_2[1])

        filtros_2

        res_calculo = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        res_calculo_2 = estadistica_resultados(resultados_actual_2, hechos_actual_2, filtro)
        #print(res_calculo)
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

        #cabecera tabla
        divisiones = []
        enemigo_nombre = []
        mes_nombre = []
        año_nombre = []
   
        divisiones_di = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo, hechos_actual, fecha_inicial_u_l, fecha_final_u_l)
        
        enemigo_di = Calculo_Spoa.enemigo_nombre(self, enemigo_nombre, res_calculo, hechos_actual)
    
        mes_di = Calculo_Spoa.meses_nombre(self, mes_nombre, res_calculo, hechos_actual)
      

        divisiones = divisiones_di[0]
        enemigo_nombre = enemigo_di[0]
        enemigo_nombre_r = enemigo_di[1]
        hechos_mapa = divisiones_di[1]

        mes_nombre = mes_di[0]
        año_nombre = mes_di[1]

        hechos=[]

        ruta= filtro[15]
     
        #try:

        if filtro[0]!= "" and filtro[0]!= "---" or filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
                
                if filtro[0]!= "" and filtro[0]!= "---" :

                    if filtro[0] == "DAVAA" or filtro[0] == "DIVFE" or filtro[0] == "TREJC":
                            
                        mapa_general(hechos_mapa, filtro) 
                        mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                        pdf.image(mapa,-62.3,-54,228,309)
                        #convencion(pdf, ruta, 4, 177)
                        
                    else:
                        for x in data:
                            for y in data[x]:
                                if y['AGR_DIV'] == filtro[0]:
                                    for d in hechos_mapa:
                                        if y['MPIO'] == d[7] and y['DPTO'] == d[6]:
                                            
                                            hechos.append(d)
                                            
             
                        mapa_filtrado(hechos, filtro)
                        if filtro[0] == "DIV01":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta,filtro[0])
                            pdf.image(mapa,-23,-34.5,205.5,282.5)
                            #convencion(pdf, ruta, 70, 175)


                        elif filtro[0] == "DIV02":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-39.5,-35,208,282.5)
                            #convencion(pdf, ruta, 80, 188)


                        elif filtro[0] == "DIV03":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-33,-36,205,282)
                            #convencion(pdf, ruta, 90, 175)

                            
                        elif filtro[0] == "DIV04":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25.5,-23,189.7,258)
                            #convencion(pdf, ruta, 70, 175)
                            
                            
                        elif filtro[0] == "DIV05":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-21.5,-24,180,245.5)
                            #convencion(pdf, ruta, 70, 175)

                            
                        elif filtro[0] == "DIV06":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-20,186.5,251)
                            #convencion(pdf, ruta, 70, 175)
                                
                            
                        elif filtro[0] == "DIV07":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-30.4,-24,198.7,268.5)
                            #convencion(pdf, ruta, 70, 175)
                                                            
                            
                        elif filtro[0] == "DIV08":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-26,186.2,251.5)
                            #convencion(pdf, ruta, 70, 175)

                                 
                        elif filtro[0] == "FUTCO" or filtro[0] == "FUTOM":
                            if filtro[0] == "FUTOM":
                                unidad = "FUTCO"
                            else:
                                unidad = "FUTCO"
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, unidad)
                            pdf.image(mapa,-8,-32,176,268)
                            #self.image(self.mapa,-8,-32,176,268)
                            #convencion(pdf, ruta, 4, 175)
                        
                        else:
                            mapa_general(hechos, filtro) 
                            mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                            pdf.image(mapa,-62.3,-54,228,309)
                            #convencion(pdf, ruta, 4, 177)

                            
                else:
   
                    mapa_general(hechos_mapa, filtro) 
                    mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                    pdf.image(mapa,-62.3,-54,228,309)
                    #convencion(pdf, ruta, 4, 177)
     
        else:
                # mapa_general(hechos_actual)

                mapa_general(hechos_mapa, filtro) 
                mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                pdf.image(mapa,-62.3,-54,228,309)
                #pdf.image(label_eventos,5, 175, 60, 15)

                #convencion(pdf, ruta, 4, 177)


        #except:
        #except Exception as e:
         #print(e)
        


        # ruta = filtro[15] 



        # pdf.ln(5)

        pdf.cell(-5)
        fill = True

        numero =  0
        resultado_dinamico = []
        for x in res_calculo_2:
            if x !=[]:
                if numero == 4 or numero ==3:
                    if filtro[17] == "sin_delco":
                        resultado_dinamico = res_calculo_2[4]
                        numero=4
                        break
                    else:
                        resultado_dinamico = res_calculo_2[3]
                        numero=3
                        break
                else:
                    resultado_dinamico = res_calculo_2[numero]
                    break

            numero = numero +1
        encabezado_coe(pdf, fill, divisiones)
        CANTIDAD_2=[]
        CANTIDAD_ENEMIGO=[]
        CANTIDAD_MES=[]
        
        columns=[]

        if numero == 4 or numero == 3 or numero == 5 or numero == 6 or numero == 7 or numero == 8 or numero == 9 or numero == 10 or numero == 11 or numero == 32 or numero == 33 or numero == 34 or numero == 35 or numero == 36 or numero == 37 or numero == 38 or numero == 39 or numero == 40 or numero == 41 or numero == 42 or numero == 43 or numero == 44 or numero == 45 or numero == 46 or numero == 47 or numero == 48 or numero == 52 or numero == 89:
            valor_calculado_filtro = Calculo_Spoa.validar_spoa_unidad_dinamico(self, filtro, resultado_dinamico, "SI" ) #funcion para filtar el spoa
            CANTIDAD_2 = tabla_boletin_coe(pdf, valor_calculado_filtro[0], filtro[26], divisiones, 1)
            CANTIDAD_ENEMIGO = sin_abla_boletin_coe(pdf, valor_calculado_filtro[0], filtro[26], enemigo_nombre, 7)
            CANTIDAD_MES_G = meses_año(pdf, valor_calculado_filtro[0], filtro[26], mes_nombre,año_nombre)
        else:
            if   numero == 12 or  numero == 13 or numero == 14 or  numero == 15:
                tabla_boletin_coe_hechos(pdf, res_calculo[12], "COMBATES POSITIVOS", divisiones)
                tabla_boletin_coe_hechos(pdf, res_calculo[13], "COMBATES NEGATIVOS", divisiones)
                tabla_boletin_coe_hechos(pdf, res_calculo[14], "COMBATES SIN RESULTADOS", divisiones)
                CANTIDAD_2 = tabla_boletin_coe_hechos(pdf, res_calculo[15], "TOTAL DE COMBATES", divisiones)
                CANTIDAD_ENEMIGO = sin_abla_boletin_coe_combate(pdf, resultado_dinamico, filtro[26], enemigo_nombre, 8)
                CANTIDAD_MES_G = meses_año_combate(pdf, resultado_dinamico, filtro[26], mes_nombre, año_nombre)
            else:
                CANTIDAD_2 = tabla_boletin_coe(pdf, resultado_dinamico, filtro[26], divisiones, 1)
                CANTIDAD_ENEMIGO = sin_abla_boletin_coe(pdf, resultado_dinamico, filtro[26], enemigo_nombre, 7)
                CANTIDAD_MES_G = meses_año(pdf, resultado_dinamico, filtro[26], mes_nombre, año_nombre)

        
        CANTIDAD_MES = CANTIDAD_MES_G[0]
        CANTIDAD_ANIO = CANTIDAD_MES_G[1]

        #CALCULO DE RESULTADOS 
        plt.rcParams["figure.figsize"] = (6, 5)
        plt.figure()
        ANIO =[]
        my_palette=[]
        for x in divisiones:
            ANIO.append("DIVISIONES")
            my_palette.append('#FFC000')

        sns.set()
         
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        ax = sns.barplot(x = divisiones, y=CANTIDAD_2, color='#FFC000')
        ax.bar_label(ax.containers[0], fontsize=14, color="black", rotation=90)
        sns.despine()
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

        ax.cla()

        plt.clf()
        plt.cla()
        plt.close()
        
        #CALCULO DE RESULTADOS 
        plt.rcParams["figure.figsize"] = (6, 5)
        plt.figure()

        my_palette = [] #define your preference
        ANIO = []
        for x in enemigo_nombre:
            if x == "GAO - Residual Disidencias FARC":
                my_palette.append("#130101")
            elif x == "DELINCUENCIA":
                my_palette.append("#008190")
            elif x == "Amenaza de Naturaleza Cibernetica":
                my_palette.append("#0C2290")
            elif x == "Delincuencia Organizada Transnacional":
                my_palette.append("#0C9050")
            elif x == "GAO CAPARROS":
                my_palette.append("#3F4d46")
            elif x == "GAO CLAN DEL GOLFO":
                my_palette.append("#875858")
            elif x == "GAO COMUNEROS DEL SUR":
                my_palette.append("#F8be09")
            elif x == "GAO PELUSOS":
                my_palette.append("#B49600")
            elif x == "NARCOTRÁFICO":
                my_palette.append("#259000")
            elif x == "GAO ELN":
                my_palette.append("#900C20")
            elif x == "GDO":
                my_palette.append("#7c02fe")
            else:
                my_palette.append("#101010")
    
        sns.set()

        for x in enemigo_nombre_r:
            ANIO.append(x)
    
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        AX2 = sns.barplot(x = enemigo_nombre_r, y=CANTIDAD_ENEMIGO, palette = my_palette)
        
        for container in AX2.containers:
            AX2.bar_label(container, fontsize=14, color="black", rotation=90)
        #AX2.bar_label(AX2.containers, fontsize=16, color="black")
        sns.despine()
        #sns.color_palette(palette = my_palette)
        
        locs, labels = plt.xticks()
        plt.rcParams["figure.figsize"] = (250, 150)
        font1 = {'family':'serif','color':'black','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}

        #plt.xlabel("Afectaciones a la Amenaza", fontdict = font2)
        plt.rc('xtick', labelsize=35) 
        plt.rc('ytick', labelsize=35) 

        plt.setp(labels, rotation=45)
       
        plt.tight_layout()

        sns.despine(top=True, right=True, left=True, bottom=True)
        
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo2.png", transparent=True)
        AX2.get_figure().clf()


        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo1.png",210,55,120,80)
        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo2.png",130,55,80,80)
            # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        plt.clf()
        plt.cla()
        plt.close()

        plt.rcParams["figure.figsize"] = (6, 5)
        plt.figure()

        Palette = [] #define your preference
        ANIO = []
        for x in mes_nombre:
            Palette.append("darkred")
            ANIO.append("resultados por Meses")
        sns.set()
         
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        AX3 = sns.barplot(x = mes_nombre, y=CANTIDAD_MES, color='darkred')
        
        AX3.bar_label(AX3.containers[0], fontsize=14, color="black", rotation=90)
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
        
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo3.png", transparent=True)
        AX3.get_figure().clf()

        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo3.png",100,140,110,70)
            # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa

 

            # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        plt.clf()
        plt.cla()
        plt.close()

        plt.rcParams["figure.figsize"] = (6, 5)
        plt.figure()

        Palette = [] #define your preference
        ANIO = []
        for x in año_nombre:
            Palette.append("darkblue")
            ANIO.append(x)
        sns.set()
         
        #f, axs = plt.subplots(1, 2, figsize=(8, 4), gridspec_kw=dict(width_ratios=[4, 3]))
        AX4 = sns.lineplot(x = año_nombre, y=CANTIDAD_ANIO, marker='8', markerfacecolor='limegreen', markersize=10, linewidth = 3, color ="darkred")
        AX4 = sns.barplot(x = año_nombre, y=CANTIDAD_ANIO, alpha =0)
        AX4.bar_label(AX4.containers[0], fontsize=14, color="black", rotation=90)
        #AX4.update_traces(textposition = "top center")
    
        sns.despine()
        sns.color_palette("rocket")
        locs, labels = plt.xticks()
        plt.rcParams["figure.figsize"] = (250, 150)
        font1 = {'family':'serif','color':'black','size':20}
        font2 = {'family':'serif','color':'darkred','size':15}

        #plt.xlabel("Afectaciones a la Amenaza", fontdict = font2)
        plt.rc('xtick', labelsize=30) 
        plt.rc('ytick', labelsize=30) 

        plt.setp(labels, rotation=90)
       
        plt.tight_layout()

        sns.despine(top=True, right=True, left=True, bottom=True)
        
        plt.savefig("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo4.png", transparent=True)
        AX4.get_figure().clf()

        pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_docker/k_c_boletin_mapa_div_balance/models/graficas/Ejemplo4.png",200,140,120,70)
            # 

        if res_calculo[16] or res_calculo[17]  or res_calculo[18]  or res_calculo[19] or res_calculo[20] or res_calculo[98] or res_calculo[99]:

            tabla_boletin_coe_hechos(pdf, res_calculo[16], "ATAQUE A LA FUERZA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[17], "NEUTRALIZACIÓN TERRORISTA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[98], "ACTIVACIÓN ART. EXPLOSIVO", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[99], "ACTIVACIÓN ZONA MINADA", divisiones)

            tabla_boletin_coe_hechos(pdf, res_calculo[100], "ACTO DE TERRORISMO", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[101], "A.T. INFRAESTRUCTURA CRITICA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[102], "A.T. POBLACIÓN CIVIL", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[103], "A.T. PROPIAS TROPAS", divisiones)

 
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 52,  "SI") #funcion para filtar el spoa
        if valor[0] or res_calculo[52] or res_calculo[53] or res_calculo[54] or res_calculo[55] or res_calculo[56] or res_calculo[57] or res_calculo[58] or res_calculo[59] or res_calculo[60]  or res_calculo[61] or res_calculo[62] or res_calculo[63] or res_calculo[64] or res_calculo[65] or res_calculo[66] or res_calculo[67] or res_calculo[68]:
            separador_cuadro_coe(pdf, fill, "MINERIA ILEGAL" , numero)
            tabla_boletin_coe_hechos(pdf, res_calculo[54], "EIYM", divisiones)




                        
        if  res_calculo[71] or res_calculo[72] or res_calculo[73] or res_calculo[74] or res_calculo[75] or res_calculo[76]: 
            pdf.ln(15)
            numero_2 = encabezado_coe_2(pdf, fill, divisiones)
            separador_cuadro_coe_2(pdf, fill, "EXTINCIÓN DE DOMINIO" , numero_2)
            tabla_boletin_coe_2(pdf, res_calculo[71], "INCAUTACIÓN PESOS COP", divisiones)

            tabla_boletin_coe_2(pdf, res_calculo[72], "INCAUTACIÓN DE DOLARES", divisiones)
            tabla_boletin_coe_2(pdf, res_calculo[73], "INCAUTACIÓN EUROS", divisiones)
            tabla_boletin_coe_2(pdf, res_calculo[74], "INCAUTACIÓN MUEBLES", divisiones)
            tabla_boletin_coe_2(pdf, res_calculo[75], "INCAUTACIÓN INMUEBLES", divisiones)
            tabla_boletin_coe_2(pdf, res_calculo[76], "INCAUTACIÓN VEHICULOS", divisiones)

        #numero = encabezado_coe(pdf, fill, divisiones)
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