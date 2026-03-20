# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.f_c_boletin_estadistica_contrabando.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.f_c_boletin_estadistica_contrabando.models.funtions.componest.tablas import *
from tipo_docker.f_c_boletin_estadistica_contrabando.maps.funciones.mapa_filtro import *
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


    #resultados de contrabando del ejecirto nacional 
    def resultados_contrabando_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):
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

        datos = [res_calculo[0], res_calculo[1], res_calculo[2], res_calculo[3], res_calculo[4], res_calculo[5], res_calculo[9], res_calculo[10], res_calculo[11], res_calculo[12], res_calculo[13], res_calculo[14]]

        #encabezado de interdicion

        encabezado_tabla_resultados_mapa(pdf, "RESULTADOS CONTRABANDO")
        pdf.ln(10)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 0,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa(pdf,"Capturas",valor[0], "Personas", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Gasolina",datos[1], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"ACPM",datos[2], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Insumos Líquidos",datos[3], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Vehículos",datos[4], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Animales incautados",datos[5], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Combustible de Contrabando",datos[7], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Licores",datos[8], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Cigarrillos",datos[9], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Telefonos",datos[10], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Muebles Incautados",datos[11], "Unidades", 18)

        nombre = "contrabando"
        mapa_hechos(datos[6], nombre, filtro)

        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

    #fu

