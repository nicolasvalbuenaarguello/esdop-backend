# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.o_c_listado_afectaciones.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.o_c_listado_afectaciones.models.funtions.componest.tablas import *
conexion_pos = Databa_bases()
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            pass

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

    
    #cuadro de afectaciones, heridos  y asesinados 
    def cuadro_afectaciones_pdf(self, pdf, fecha_inicial_u_l, fecha_final_u_l, filtro):
        
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

        valor_a = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        valor_s = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        cuadro_heridos_asesinados(pdf, valor_a[0], valor_s[0])
        #cuadro de afectaciones, heridos  y asesinados 
        #cuadro de afectaciones, heridos  y asesinados 


    #listado de afectaciones del personal afectado
    def listados_afectaciones_pdf(self, pdf, fecha_inicial_u_l, fecha_final_u_l, filtro):
        
        dato =""

        filtros = selecion_filtro(filtro)
          
        query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])

        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
        valor_a = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        valor_s = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 6,  "SI") #funcion para filtar el spoa

        if filtro[10] == "ASESINADOS":

            listado_afectacion(pdf, valor_a[0], "ASESINADOS PROPIAS TROPAS")  
            
        elif filtro[10] == "HERIDOS":
            pdf.ln(10)
            listado_afectacion(pdf, valor_s[0], "HERIDOS PROPIAS TROPAS")  
            
        else:
            listado_afectacion(pdf, valor_a[0], "ASESINADOS PROPIAS TROPAS") 
            
            pdf.ln(10)
            listado_afectacion(pdf, valor_s[0], "HERIDOS PROPIAS TROPAS")  


    