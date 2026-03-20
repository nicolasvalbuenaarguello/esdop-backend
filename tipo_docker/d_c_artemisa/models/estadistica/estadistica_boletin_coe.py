# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.d_c_artemisa.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from  tipo_docker.d_c_artemisa.models.funtions.componest.tablas import *
from  tipo_docker.d_c_artemisa.maps.funciones.mapa_filtro import *
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
    def resultados_artemisa_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):
        
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

        encabezado_tabla_resultados_mapa(pdf, "RESULTADOS LOE AMAZONIA")
        pdf.ln(10)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa 
        tabla_resultados_con_mapa(pdf,"Capturas LOE Amazonía",valor[0], "Personas", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Plantulas Sembradas",res_calculo[31], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Incautacion Madera m3",res_calculo[32], "Metros Cubicos", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Animales Incautados",res_calculo[63], "Unidades", 18)

        datos = [res_calculo[30], res_calculo[63]]

        nombre = "artemisa"
        mapa_dos_puntos(datos, nombre, filtro)
        # pdf.image("scr/static/img/img_mapas/base_map.png",25,12,170,210)
        convecion_artmisa = '{}static/img/img_mapas/convecion_artmisa.jpg'.format(filtro[15])
        
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.8,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

        pdf.image(convecion_artmisa,155, 165, 65, 30)
