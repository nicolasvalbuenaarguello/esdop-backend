# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.c_c_boletin_estadistica_narcotrafico.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico.models.funtions.componest.tablas import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico.maps.funciones.mapa_filtro import *
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



    # resultados por enemigo 
    def resultados_narcotrafico_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):

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

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro) #querys modificados

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos
        erradicacion = conexion_pos.comando_query(query[2]) #resultados de la base de datos
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        #encabezado de interdicion
        encabezado_interdicion(pdf)
        pdf.ln()

        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
        valor_3 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "SI") #funcion para filtar el spoa
        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 69,  "SI") #funcion para filtar el spoa
        valor_11 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 68,  "SI") #funcion para filtar el spoa
        valor_12 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 70,  "SI") #funcion para filtar el spoa
        valor_13 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 71,  "SI") #funcion para filtar el spoa


        datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]

        # datos = [res_calculo[21],res_calculo[23],res_calculo[29],res_calculo[22],res_calculo[47],res_calculo[48], res_calculo[28], res_calculo[24], res_calculo[25], res_calculo[26], res_calculo[65], res_calculo[66], res_calculo[67], res_calculo[68]]

        # datos = [valor[0], valor_1[0], valor_2[0], valor_3[0], valor_4[0], valor_5[0], valor_6[0], valor_7[0], valor_8[0], valor_9[0], valor_10[0], valor_11[0], valor_12[0], valor_13[0]]
        
        calculo_de_interdion(pdf,"Clorhidrato de Cocaína", datos[0], 0, "Toneladas")
        
        pdf.ln()
        calculo_de_interdion(pdf,"Pasta Base de Coca", datos[1], 0, "Toneladas")

        pdf.ln()
        calculo_de_interdion(pdf,"Heroína", datos[10], 0, "Kilos")
        
        pdf.ln()
        calculo_de_interdion(pdf,"Basuco", datos[11], 0, "Kilos")
        
        pdf.ln()
        calculo_de_interdion(pdf,"Drogas Sinteticas", datos[12], 0, "Unidades")

        pdf.ln()
        calculo_de_interdion(pdf,"Insumos Sólidos ", datos[2], 0, "Toneladas")
        
        pdf.ln()
        calculo_de_interdion(pdf,"Marihuana", datos[3], 0, "Toneladas")
            
        pdf.ln()
        calculo_de_interdion(pdf,"CLHC en proceso", datos[4], 0, "Galones")
                
        pdf.ln()
        calculo_de_interdion(pdf,"PBC en proceso ", datos[5], 0, "Galones")
                    
        pdf.ln()
        calculo_de_interdion(pdf,"Insumos Líquidos  ", datos[6], 0, "Galones")
                
        pdf.ln()
        calculo_de_interdion(pdf,"Laboratorios CLHC ", datos[7], 0, "Unidades")
                    
        pdf.ln()
        calculo_de_interdion(pdf,"Laboratorios PBC", datos[8], 0, "Unidades")
                        
        pdf.ln()
        calculo_de_interdion(pdf,"Laboratorios Heroína", datos[13], 0, "Unidades")
                        
        pdf.ln()
        calculo_de_interdion(pdf,"Semilleros", datos[9], 0, "Unidades")

        nombre = "mapa_narcotrafico"
        mapa_narcotrafico(datos, filtro, nombre)

        ruta = filtro[15]
        convecion_narcotrafico = '{}static/img/img_mapas/convecion_narcotrafico.jpg'.format(ruta)

        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])

        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(convecion_narcotrafico,5, 175, 51, 32)

        
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)
        
        
