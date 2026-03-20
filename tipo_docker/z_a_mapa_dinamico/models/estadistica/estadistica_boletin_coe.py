# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.z_a_mapa_dinamico.models.conexion_pos import Databa_bases
from tipo_docker.z_a_mapa_dinamico.models.funtions.funciones import *
from tipo_docker.z_a_mapa_dinamico.models.funtions.componest.tablas import *
from tipo_docker.z_a_mapa_dinamico.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()
import json
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            pass

    def divisiones_nombre(self, divisiones_lis, resultados, hechos):
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
                    if y[2] not in divisiones:
                        divisiones.append(y[2])
                else:
                    if y[26] not in filtro_hechos:
                        filtro_hechos.append(y[26])
                    if y[1] not in divisiones:
                        divisiones.append(y[1])
                        

            numero = numero + 1
        #print(y[1])
        #print(y[2])
        #print(divisiones)
        for x in hechos:
            for y in filtro_hechos:
                if x[18] == y:
                    hechos_devolver.append(x)
        #print(len(hechos_devolver))
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

        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))
            nueva_2=[]
            departamento_tuple=[]
            for x in data:
                for y in data[x]:
                    if y['AGR_DIV'] == filtro[0]:
                        nueva_2.append(y['MPIO'])
                        departamento_tuple.append(y['DPTO'])

        if len(nueva_2) > 1:
                ids = tuple(nueva_2)
                ids_2 = tuple(departamento_tuple)

                dato = "and dpto = '{}' and mpio in {}".format(ids_2, ids)
                dato_res= "and hop_depto = '{}' and hop_mpio in {}".format(ids_2, ids)
                         

        dato =""
        filtros = selecion_filtro(filtro)
        query_actual = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)

        

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        res_calculo = estadistica_resultados(resultados_actual, hechos_actual, filtro)
        
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
        divisiones_di = Calculo_Spoa.divisiones_nombre(self, divisiones, res_calculo, hechos_actual)

        divisiones = divisiones_di[0]
        hechos_mapa = divisiones_di[1]
        
 
        
        hechos=[]

        ruta= filtro[15]
     
        try:

            if filtro[0]!= "" and filtro[0]!= "---" or filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
                
                if filtro[0]!= "" and filtro[0]!= "---" :

                    if filtro[0] == "DAVAA" or filtro[0] == "DIVFE" or filtro[0] == "TREJC":
                            
                        mapa_general(hechos_mapa, filtro) 
                        mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                        pdf.image(mapa,-62.3,-54,228,309)
                        convencion(pdf, ruta, 4, 177)
                        
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
                            convencion(pdf, ruta, 70, 175)


                        elif filtro[0] == "DIV02":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-40.5,-35,208,282.5)
                            convencion(pdf, ruta, 80, 188)


                        elif filtro[0] == "DIV03":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-33,-36,205,282)
                            convencion(pdf, ruta, 90, 175)

                            
                        elif filtro[0] == "DIV04":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25.5,-23,189.7,258)
                            convencion(pdf, ruta, 70, 175)
                            
                            
                        elif filtro[0] == "DIV05":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-21.5,-24,180,245.5)
                            convencion(pdf, ruta, 70, 175)

                            
                        elif filtro[0] == "DIV06":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-20,186.5,251)
                            convencion(pdf, ruta, 70, 175)
                                
                            
                        elif filtro[0] == "DIV07":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-32.4,-30,204.7,276.5)
                            convencion(pdf, ruta, 70, 175)
                                                            
                            
                        elif filtro[0] == "DIV08":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-25,-26,186.2,251.5)
                            convencion(pdf, ruta, 70, 175)

                                 
                        elif filtro[0] == "FUTCO":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, filtro[0])
                            pdf.image(mapa,-44,-149,315,476)
                            convencion(pdf, ruta, 4, 175)
                        
                        else:
                            mapa_general(hechos, filtro) 
                            mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                            pdf.image(mapa,-62.3,-54,228,309)
                            convencion(pdf, ruta, 4, 177)

                            
                else:
   
                    mapa_general(hechos_mapa, filtro) 
                    mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                    pdf.image(mapa,-62.3,-54,228,309)
                    convencion(pdf, ruta, 4, 177)
                    print("z")

            else:
                # mapa_general(hechos_actual)

                mapa_general(hechos_mapa, filtro) 
                mapa = '{}static/img/img_mapas/filtro_dep.png'.format(ruta)
                pdf.image(mapa,-62.3,-54,228,309)
                #pdf.image(label_eventos,5, 175, 60, 15)

                convencion(pdf, ruta, 4, 177)
                print("x")

        #except:
        except Exception as e:
         print(e)
        


        # ruta = filtro[15] 



      
      

        # pdf.ln(5)

        pdf.cell(-5)
        fill = True



        #calculo de resultados

        valor_0 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 0,  "NO") #funcion para filtar el spoa
        valor_1 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 1,  "NO") #funcion para filtar el spoa
        valor_2 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 2,  "NO") #funcion para filtar el spoa
        valor_4 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa

                # print(filtro[17])
        if filtro[17] == "sin_delco":
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 4, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        else:
            valor_calculado = Calculo_Spoa.validar_spoa(self, filtro, res_calculo, 3, "CAPTURAS", "SI" ) #funcion para filtar el spoa
        # print(divisiones) or 

        if valor_0[0] or valor_1[0] or valor_2[0] or valor_calculado[0] or valor_4[0] or res_calculo[6] or res_calculo[7] or res_calculo[8] or res_calculo[9] or res_calculo[10] or res_calculo[11] or res_calculo[12] or res_calculo[13] or res_calculo[14] or res_calculo[15] or res_calculo[16] or res_calculo[17] or res_calculo[18] or res_calculo[19] or res_calculo [20] or res_calculo [21] or res_calculo [22] or res_calculo [23] or res_calculo[24] or res_calculo[25] or res_calculo[26] or res_calculo[27] or res_calculo[28] or res_calculo[29] or res_calculo[30] or res_calculo[31] or res_calculo[32] or res_calculo[33] or res_calculo[34] or res_calculo[35] or res_calculo[36] or res_calculo[37] or res_calculo[38] or res_calculo[39] or res_calculo[40] or res_calculo[41] or res_calculo[42] or res_calculo[43] or res_calculo[44] or res_calculo[45] or res_calculo[46] or res_calculo[47] or res_calculo[48] or res_calculo[49] or res_calculo[50] or res_calculo[51] or res_calculo[52] or res_calculo[53] or res_calculo[54] or res_calculo[55] or res_calculo[56] or res_calculo[57] or res_calculo[58] or res_calculo[59] or res_calculo[60] or res_calculo[61] or res_calculo[62] or res_calculo[63] or res_calculo[64] or res_calculo[65] or res_calculo[66] or res_calculo[67] or res_calculo[68] or res_calculo[69] or res_calculo[70]  or res_calculo[77] or res_calculo[78] or res_calculo[79] or res_calculo[80] or res_calculo[81] or res_calculo[82] or res_calculo[83] or res_calculo[84] or res_calculo[85] or res_calculo[86] or res_calculo[87] or res_calculo[88] or res_calculo[89] or res_calculo[90] or res_calculo[91] or res_calculo[92] or res_calculo[93] or res_calculo[94] or res_calculo[95] or res_calculo[96] or res_calculo[97] or res_calculo[98] or res_calculo[99] or res_calculo[100] or res_calculo[101] or res_calculo[102] or res_calculo[103]:
            numero = encabezado_coe(pdf, fill, divisiones)

        if valor_0[0] or valor_1[0] or valor_2[0] or valor_calculado[0] or valor_4[0]:
        #separador
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA AMENAZA" , numero)
            #tabla de resultados
            #estadistica
        
            tabla_boletin_coe(pdf, valor_0[0], "MENORES RECUPERADOS", divisiones)
            tabla_boletin_coe(pdf, valor_1[0], "PRESENTACIÓN VOLUNTARIA", divisiones)
            tabla_boletin_coe(pdf, valor_2[0], "SOMETIMIENTOS", divisiones)
            # valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
            tabla_boletin_coe(pdf, valor_calculado[0], "CAPTURAS", divisiones)
            tabla_boletin_coe(pdf, valor_4[0], "MDOM", divisiones)


        valor_5 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 6,  "SI") #funcion para filtar el spoa
        valor_6 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa

        if valor_5[0] or valor_6[0]:
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A PROPIAS TROPAS" , numero)

            tabla_boletin_coe(pdf, valor_5[0], "ASESINADOS", divisiones)
            tabla_boletin_coe(pdf, valor_6[0], "HERIDOS", divisiones)


        valor_7 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
        valor_8 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
        valor_9 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa
        valor_10 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 11,  "SI") #funcion para filtar el spoa

        if valor_7[0] or valor_8[0]  or valor_9[0]  or valor_10[0]:
            separador_cuadro_coe(pdf, fill, "MATERIAL DE GUERRA" , numero)

            tabla_boletin_coe(pdf, valor_7[0], "ARMAS DE LARGO ALCANCE", divisiones)
            tabla_boletin_coe(pdf, valor_8[0], "ARMAS DE CORTO ALCANCE", divisiones)
            tabla_boletin_coe(pdf, valor_9[0], "ARMAS DE ACOMPAÑAMIENTO", divisiones)
            tabla_boletin_coe(pdf, valor_10[0], "MUNICIONES", divisiones)


        if res_calculo[12] or res_calculo[13]  or res_calculo[14]  or res_calculo[15]:
            separador_cuadro_coe(pdf, fill, "COMBATES" , numero)
            tabla_boletin_coe_hechos(pdf, res_calculo[12], "COMBATES POSITIVOS", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[13], "COMBATES NEGATIVOS", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[14], "COMBATES SIN RESULTADOS", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[15], "TOTAL DE COMBATES", divisiones)

        if res_calculo[16] or res_calculo[17]  or res_calculo[18]  or res_calculo[19] or res_calculo[20] or res_calculo[98] or res_calculo[99]:
            separador_cuadro_coe(pdf, fill, "ATAQUE A LA FUERZA" , numero)
            
            tabla_boletin_coe_hechos(pdf, res_calculo[16], "ATAQUE A LA FUERZA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[17], "NEUTRALIZACIÓN TERRORISTA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[98], "ACTIVACIÓN ART. EXPLOSIVO", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[99], "ACTIVACIÓN ZONA MINADA", divisiones)

            tabla_boletin_coe_hechos(pdf, res_calculo[100], "ACTO DE TERRORISMO", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[101], "A.T. INFRAESTRUCTURA CRITICA", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[102], "A.T. POBLACIÓN CIVIL", divisiones)
            tabla_boletin_coe_hechos(pdf, res_calculo[103], "A.T. PROPIAS TROPAS", divisiones)


            tabla_boletin_coe(pdf, res_calculo[18], "HOSTIGAMIENTOS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[19], "ASONADAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[20], "ATAQUE CONS DRONS", divisiones)


        if res_calculo[21] or res_calculo[22]  or res_calculo[23]  or res_calculo[24] or res_calculo[25] or res_calculo[26] or res_calculo[27] or res_calculo[28] or res_calculo[29] or res_calculo[30] or res_calculo[31]:
            separador_cuadro_coe(pdf, fill, "MATERIAL DE EXPLOSIVOS" , numero)

            tabla_boletin_coe(pdf, res_calculo[21], "A.E", divisiones)
            tabla_boletin_coe(pdf, res_calculo[22], "MAP(Mina Anti Persona)", divisiones)
            tabla_boletin_coe(pdf, res_calculo[23], "EXPLOSIVOS kg", divisiones)
            tabla_boletin_coe(pdf, res_calculo[24], "EXPLOSIVOS m", divisiones)
            tabla_boletin_coe(pdf, res_calculo[25], "EXPLOSIVOS UND", divisiones)
            tabla_boletin_coe(pdf, res_calculo[26], "CORDÓN DETONANTE m", divisiones)
            tabla_boletin_coe(pdf, res_calculo[27], "MECHA LENTA m", divisiones)
            tabla_boletin_coe(pdf, res_calculo[28], "MEDIOS DE LANZAMIENTO", divisiones)
            tabla_boletin_coe(pdf, res_calculo[29], "DECTONADOR ANELECTRICO", divisiones)
            tabla_boletin_coe(pdf, res_calculo[30], "DECTONADOR ELECTRICO", divisiones)
            tabla_boletin_coe(pdf, res_calculo[31], "ARTEFACTOS EXPLOSIVOS", divisiones)

        valor_32 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 32,  "SI") #funcion para filtar el spoa
        valor_33 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        valor_34 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 34,  "SI") #funcion para filtar el spoa
        valor_35 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 35,  "SI") #funcion para filtar el spoa
        valor_36 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 36,  "SI") #funcion para filtar el spoa
        valor_37 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 37,  "SI") #funcion para filtar el spoa
        valor_38 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 38,  "SI") #funcion para filtar el spoa
        valor_39 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 39,  "SI") #funcion para filtar el spoa
        valor_40 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 40,  "SI") #funcion para filtar el spoa
        valor_41 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 41,  "SI") #funcion para filtar el spoa
        valor_42 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 42,  "SI") #funcion para filtar el spoa
        valor_43 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 43,  "SI") #funcion para filtar el spoa
        valor_44 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 44,  "SI") #funcion para filtar el spoa
        valor_45 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 45,  "SI") #funcion para filtar el spoa
        valor_46 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 46,  "SI") #funcion para filtar el spoa
        valor_47 = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "SI") #funcion para filtar el spoa


        if valor_32[0] or valor_33[0] or valor_34[0] or valor_35[0] or valor_36[0] or valor_37[0] or valor_38[0] or valor_39[0] or valor_40[0] or valor_41[0] or valor_42[0] or valor_43[0] or valor_44[0] or valor_45[0] or valor_46[0] or valor_47[0]:
            separador_cuadro_coe(pdf, fill, "NARCOTRÁFICO" , numero)

            tabla_boletin_coe(pdf, valor_32[0], "COCAÍNA Kg", divisiones)
            tabla_boletin_coe(pdf, valor_46[0], "COCAÍNA PROCESO GAL", divisiones)
            tabla_boletin_coe(pdf, valor_33[0], "MARIHUANA Kg ", divisiones)
            tabla_boletin_coe(pdf, valor_34[0], "PBC Kg ", divisiones)
            tabla_boletin_coe(pdf, valor_47[0], "PBC PROCESO GAL ", divisiones)
            tabla_boletin_coe(pdf, valor_35[0], "BASUCO", divisiones)
            tabla_boletin_coe(pdf, valor_36[0], "HEROHINA", divisiones)
            tabla_boletin_coe(pdf, valor_37[0], "DROGAS SINTETICAS", divisiones)
            tabla_boletin_coe(pdf, valor_39[0], "LAB. CLORHIDRATO DE COCAINA", divisiones)
            tabla_boletin_coe(pdf, valor_40[0], "LAB. PASTA O BASE DE COCA", divisiones)
            tabla_boletin_coe(pdf, valor_38[0], "LAB. HEROHINA - MORFINA", divisiones)
            tabla_boletin_coe(pdf, valor_41[0], "SEMILLEROS", divisiones)
            tabla_boletin_coe(pdf, valor_42[0], "MATA(S) DE COCA EN SEMILLERO", divisiones)
            tabla_boletin_coe(pdf, valor_43[0], "INSUMOS LIQUIDOS Gal", divisiones) 
            tabla_boletin_coe(pdf, valor_44[0], "INSUMOS SOLIDOS Kg ", divisiones)
            tabla_boletin_coe(pdf, valor_45[0], "COMBUSTIBLE NARCOTRAFICO ", divisiones)
        

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "SI") #funcion para filtar el spoa
        if valor[0] or res_calculo[49] or res_calculo[50] or res_calculo[51]:
            separador_cuadro_coe(pdf, fill, "LOE AMAZONÍA" , numero)
            tabla_boletin_coe(pdf, valor[0], "CAPTURAS AMAZONÍA ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[49], "PLANTULAS SEMBRADAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[50], "MADERA INCAUTADA", divisiones)
            tabla_boletin_coe(pdf, res_calculo[51], "ANIMALES INCAUTADOS", divisiones)
        
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 52,  "SI") #funcion para filtar el spoa
        if valor[0] or res_calculo[52] or res_calculo[53] or res_calculo[54] or res_calculo[55] or res_calculo[56] or res_calculo[57] or res_calculo[58] or res_calculo[59] or res_calculo[60]  or res_calculo[61] or res_calculo[62] or res_calculo[63] or res_calculo[64] or res_calculo[65] or res_calculo[66] or res_calculo[67] or res_calculo[68]:
            separador_cuadro_coe(pdf, fill, "MINERIA ILEGAL" , numero)
            tabla_boletin_coe_hechos(pdf, res_calculo[54], "EIYM", divisiones)
            tabla_boletin_coe(pdf, valor[0], "CAPTURAS MINERIA ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[53], "RME MINERIA ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[55], "UPM ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[56], "MAQUINARIA PESADA", divisiones)
            tabla_boletin_coe(pdf, res_calculo[57], "EXCAVADORAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[58], "RETROEXCAVADORAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[59], "TRACTOR CON ORUGA", divisiones)
            tabla_boletin_coe(pdf, res_calculo[60], "DRAGAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[61], "MAQUINARIA AMARILLA", divisiones)
            tabla_boletin_coe(pdf, res_calculo[62], "MOTORES", divisiones)
            tabla_boletin_coe(pdf, res_calculo[63], "COMBUSTIBLE MINERIA", divisiones)
            tabla_boletin_coe(pdf, res_calculo[64], "EXPLOSIVOS KG", divisiones)
            tabla_boletin_coe(pdf, res_calculo[65], "EXPLOSIVOS M", divisiones)
            tabla_boletin_coe(pdf, res_calculo[66], "EXPLOSIVOS GAL", divisiones)
            tabla_boletin_coe(pdf, res_calculo[67], "MATERIAL DE TRANSPORTE", divisiones)
            tabla_boletin_coe(pdf, res_calculo[68], "COLTAN KG", divisiones)
        


        if res_calculo[69] or res_calculo[70] : 
            separador_cuadro_coe(pdf, fill, "LIBERADOS Y RESCATADOS" , numero)
            tabla_boletin_coe(pdf, res_calculo[69], "LIBERADOS ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[70], "RESCATADOS", divisiones)



        if res_calculo[77] or res_calculo[78] or res_calculo[79] or res_calculo[80] or res_calculo[81] or res_calculo[82] or res_calculo[83] or res_calculo[84] or res_calculo[85]:
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN A LA INFRAESTRUCTURA CRÍTICA" , numero)
            tabla_boletin_coe(pdf, res_calculo[77], "AFECTACIÓN A OLEODUCTO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[78], "ABOYADURAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[79], "APIQUES ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[80], "ROTURAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[81], "SABOTAJES ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[82], "PETROLEO", divisiones)
            tabla_boletin_coe(pdf, res_calculo[83], "APISCINAS ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[84], "VALVULAS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[85], "REFINERIAS", divisiones)

        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 89,  "SI") #funcion para filtar el spoa
        
        if valor[0] or res_calculo[90] or res_calculo[91] or res_calculo[92] or res_calculo[93] or res_calculo[94] or res_calculo[95] or res_calculo[96] or res_calculo[97]:
            separador_cuadro_coe(pdf, fill, "AFECTACIÓN AL CONTRABANDO" , numero)

            tabla_boletin_coe(pdf, valor[0], "CAPTURAS CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[90], "RME CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[91], "COMBUSTIBLE CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[92], "GASOLINA CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[93], "ACPM CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[94], "VEHICULOS CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[95], "INSUMOS LIQUIDOS CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[96], "INSUMOS SOLIDOS CONTRABANDO ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[97], "SEMOVIENTES DE CONTRABANDO ", divisiones)
                
        if res_calculo[86] or res_calculo[87] or res_calculo[88]:
            separador_cuadro_coe(pdf, fill, "OTROS EVENTOS" , numero)
            tabla_boletin_coe(pdf, res_calculo[86], "DEPÓSITO ILEGAL ", divisiones)
            tabla_boletin_coe(pdf, res_calculo[87], "CAMPAMENTOS", divisiones)
            tabla_boletin_coe(pdf, res_calculo[88], "PROSELITISMO", divisiones)

                        
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