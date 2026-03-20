# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.models.funtions.componest.tablas import *
from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.maps.funciones.mapa_filtro import *
import json

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

    def titulo_validar(filtro):
            
        
        titulo =""
        if filtro[0] != "" and filtro[0] !="---":
            titulo = filtro[0]
        elif filtro[5] != "" and filtro[5] !="---":
            titulo = filtro[5]
        return titulo

#funcion para calcular resultados  

    def comparativo_mapa(self, pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l, filtro, anio_act, anio_ant, fecha_titulo, fecha_titulo_dos, fecha_titulo_tres, fecha_anio_tres_inicial, fecha_anio_tres_final, anio_ant_tres, titulo_unidad):

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
        
        if  filtro[4] == "lugar":
            if filtro[6]!="" and filtro[6]!="---" :#filtro por municipio
                nueva=filtro[6].split(",")
                dato = ""
                dato_res=""
                if len(nueva) > 1:
                        ids = tuple(nueva)
                        if filtro[7] !="" and filtro[7] !="---" and filtro[6]!="---" :
                            dato = "and dpto = '{}' and mpio in {} and enemigo = '{}'".format(filtro[5], ids, filtro[7])
                            dato_res= "and hop_depto = '{}' and hop_mpio in {} and hop_enemigo = '{}'".format(filtro[5], ids, filtro[7])
           
                        else:
                            dato = "and dpto = '{}' and mpio in {} ".format(filtro[5], ids)
                            dato_res= "and hop_depto = '{}' and hop_mpio in {} ".format(filtro[5], ids)
                            print("--///--")

                else:
                    mpio = nueva[0]  

                    if  filtro[7] !="" and filtro[7] !="---"  and filtro[6]!="---":
                        dato = "and {} = '{}' and {} = '{}' and enemigo = '{}'".format("dpto",filtro[5], "mpio",mpio, filtro[7])
                        dato_res = "and {} = '{}' and {} = '{}' and hop_enemigo = '{}'".format("hop_depto", filtro[5], "hop_mpio",mpio, filtro[7])
                    else:
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
        # print(query_actual)
        query_anterior = parametros(fecha_inicial_p_l, fecha_final_p_l, filtros, filtro)
        query_anterior_tres = parametros(fecha_anio_tres_inicial, fecha_anio_tres_final, filtros, filtro)

        resultados_actual = conexion_pos.comando_query(query_actual[0])
        hechos_actual = conexion_pos.comando_query(query_actual[1])
        erradicacion_actual = conexion_pos.comando_query(query_actual[2])

        resultados_anterior = conexion_pos.comando_query(query_anterior[0])
        hechos_anterior = conexion_pos.comando_query(query_anterior[1])
        erradicacion_anterior = conexion_pos.comando_query(query_anterior[2])

        
        resultados_anterior_tres = conexion_pos.comando_query(query_anterior_tres[0])
        hechos_anterior_tres = conexion_pos.comando_query(query_anterior_tres[1])
        erradicacion_anterior_tres = conexion_pos.comando_query(query_anterior_tres[2])

        res_calculo_ante_tres = estadistica_resultados(resultados_anterior_tres, hechos_anterior_tres, filtro)
        res_calculo_ante = estadistica_resultados(resultados_anterior, hechos_anterior, filtro)
        res_calculo_act = estadistica_resultados(resultados_actual, hechos_actual, filtro)

        sece_tres = ""
        sece_dos = ""
        sece_uno = ""
        if anio_ant_tres == "2023":
            sece_tres = "INICIO CESE AL FUEGO"
        if anio_ant == "2023":
            sece_dos = "INICIO CESE AL FUEGO"
        if anio_act == "2023":
            sece_uno = "INICIO CESE AL FUEGO"


        pdf.set_fill_color(193, 30, 38)
        pdf.rounded_rect(114, 37, 70, 14.5, 1,'D', '1234')
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 12)
        pdf.text(119,41,"FECHA INFORMACIÓN")
        pdf.set_font('Arial', 'B', 8)
        # pdf.text(10,42.5,fecha_titulo_tres)
        pdf.text(119,45,fecha_titulo_dos)
        pdf.text(119,49, fecha_titulo)

        pdf.set_text_color(20,62,52)
        pdf.set_font('Calibri', 'B', 16)
        titulo = Calculo_Spoa.titulo_validar(filtro)
        titulo= titulo_unidad
        altura = len(titulo_unidad)
        titulo = str(titulo)
        titulo =  titulo.replace("[", "")
        titulo =  titulo.replace("]", "")
        titulo =  titulo.replace(",", " ")
        titulo =  titulo.replace("'", "")
        titulo =  titulo.replace(")", "")
        titulo =  titulo.replace("(", "")
        if altura < 100:
            pdf.ln(15)
        else:
            pdf.ln(10)
        pdf.cell(22)
        posicion_inicial = pdf.get_y()
        pdf.multi_cell(80, 5, '', 0, "C", False)
        posicion_final = pdf.get_y()
        restar = posicion_inicial-posicion_final

        if restar ==-10:
            pdf.ln(-20.5+(restar/2))
        elif restar ==-15:
            pdf.ln(-22.5+(restar/2))
        elif restar ==-20:
            pdf.ln(-21.5+(restar/2)-3)
        elif restar ==-25:
            pdf.ln(-20.5+(restar/2)-3)
        else:
            pdf.ln(-20.5)

        hechos=[]
        pdf.rounded_rect(32, 71, 80, 100, 1,'D', '1234')
                
        convencion(pdf, ruta, 3, 140)
        rosa_nautica = '{}static/img/img_mapas/rosa_nautica.jpg'.format(ruta)
        pdf.image(rosa_nautica,99, 72, 10, 10)

        try:

            if filtro[0]!= "" and filtro[0]!= "---" or filtro[2]!= "" and filtro[2]!= "---" or filtro[3] != "" and filtro[3] != "---" or filtro[5] != "" and filtro[5] != "---" or filtro[6] != "" and filtro[6] != "---":
                

                if filtro[0]!= "" and filtro[0]!= "---" :

                    if filtro[0] == "DAVAA" or filtro[0] == "DIVFE" or filtro[0] == "TREJC":
                            
                        mapa_general(res_calculo_act[93], filtro) 
                        mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                        pdf.image(mapa,-10,45,145,145)
    
                    else:
                        for x in data:
                            for y in data[x]:
                                if y['AGR_DIV'] == filtro[0]:
                                    for d in res_calculo_act[93]:
                                        if y['MPIO'] == d[7] and y['DPTO'] == d[6]:
                                        
                                            hechos.append(d)
                                            # print("hola")
                        
                        mapa_filtrado(hechos, filtro)
                        nombre_mapa = filtro[0]+"_comparativo_div"
                        if filtro[0] == "DIV01":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta,nombre_mapa)
                            pdf.image(mapa,10,62,125,125)
                            
                        elif filtro[0] == "DIV02":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,10,55,130,130)

                        elif filtro[0] == "DIV03":
                            
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,5,55,130,130)
                            
                        elif filtro[0] == "DIV04":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,12.5,57,116,116)
    
                        elif filtro[0] == "DIV05":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,10,63,125,125)

                        elif filtro[0] == "DIV06":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,15,55,111,111)
     
                        elif filtro[0] == "DIV07":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,6,52,135,135)

                        elif filtro[0] == "DIV08":
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, nombre_mapa)
                            pdf.image(mapa,15.5,60,110,110)

                        elif filtro[0] == "FUTCO" or filtro[0] == "FUTOM":
                            if filtro[0] == "FUTOM":
                                unidad = "FUTCO"+"_comparativo_div"
                              
                            else:
                                unidad = "FUTCO"+"_comparativo_div"
                  
                            mapa = '{}static/img/img_mapas/{}.png'.format(ruta, unidad)
                            pdf.image(mapa,12.5,60,120,120)
   
                        else:
                            mapa_general(res_calculo_act[100], filtro) 
                            mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                            pdf.image(mapa,-10,45,145,145)

                elif filtro[5]!="" and filtro[5]!="-":

                    if  "," in  filtro[5]:
                        print(len(filtro[5]))
                        print(filtro[5])
                            
                        mapa_general(res_calculo_act[93], filtro) 
                        mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                        pdf.image(mapa,-10,45,145,145)
                    else:


                        mapa_filtrado_dep(res_calculo_act[93], filtro)
                        mapa = '{}static/img/img_mapas/{}.png'.format(ruta,filtro[5])
                        if filtro[5] =="AMAZONAS":
                            pdf.image(mapa,17,65,107,107)
                        elif filtro[5] =="ANTIOQUIA":
                            pdf.image(mapa,13,60,116,116)
                        elif filtro[5] =="ARAUCA":
                            pdf.image(mapa,15.5,60,111,111)
                        elif filtro[5] =="ATLÁNTICO":
                            pdf.image(mapa,5,55,130,130)
                        elif filtro[5] =="BOLÍVAR":
                            pdf.image(mapa,5,53,135,135)
                        elif filtro[5] =="BOYACÁ":
                            pdf.image(mapa,17,70,108,108)
                        elif filtro[5] =="CALDAS":
                            pdf.image(mapa,16,65,110,110)
                        elif filtro[5] =="CAQUETÁ":
                            pdf.image(mapa,15,55,111,111)
                        elif filtro[5] =="CASANARE":
                            pdf.image(mapa,16,65,110,110)
                        elif filtro[5] =="CAUCA":
                            pdf.image(mapa,11,60,119,119)
                        elif filtro[5] =="CESAR":
                            pdf.image(mapa,10,53,135,135)
                        elif filtro[5] =="CHOCÓ":
                            pdf.image(mapa,10,53,135,135)
                        elif filtro[5] =="CUNDINAMARCA":
                            pdf.image(mapa,8,55,126,126)
                        elif filtro[5] =="CÓRDOBA":
                            pdf.image(mapa,5,53,132,132)
                        elif filtro[5] =="GUAINÍA":
                            pdf.image(mapa,15.5,55,110,110)
                        elif filtro[5] =="GUAVIARE":
                            pdf.image(mapa,16,55,110,110)
                        elif filtro[5] =="HUILA":
                            pdf.image(mapa,14,67,112,112)
                        elif filtro[5] =="LA GUAJIRA":
                            pdf.image(mapa,15.5,65,110,110)
                        elif filtro[5] =="MAGDALENA":
                            pdf.image(mapa,5,55,130,130)
                        elif filtro[5] =="META":
                            pdf.image(mapa,15.5,65,110,110)
                        elif filtro[5] =="NARIÑO":
                            pdf.image(mapa,14,60,115,115)
                        elif filtro[5] =="NORTE DE SANTANDER":
                            pdf.image(mapa,6,52,137,137)
                        elif filtro[5] =="PUTUMAYO":
                            pdf.image(mapa,15.5,55,110,110)
                        elif filtro[5] =="QUINDÍO":
                            pdf.image(mapa,8,60,128,128)
                        elif filtro[5] =="RISARALDA":
                            pdf.image(mapa,11,55,118,118)
                        elif filtro[5] =="SANTANDER":
                            pdf.image(mapa,10,58,122,122)
                        elif filtro[5] =="SUCRE":
                            pdf.image(mapa,10,55,130,130)
                        elif filtro[5] =="TOLIMA":
                            pdf.image(mapa,7,55,130,130)
                        elif filtro[5] =="VALLE DEL CAUCA":
                            pdf.image(mapa,11.5,59,118,118)
                        elif filtro[5] =="VAUPÉS":
                            pdf.image(mapa,10,58,122,122)
                        elif filtro[5] =="VICHADA":
                            pdf.image(mapa,16,70,110,110)
                        else:
                            pdf.image(mapa,-10,45,145,145)
                
                else:
   
                    mapa_general(res_calculo_act[93], filtro) 
                    mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                    pdf.image(mapa,-10,45,145,145)

            else:

                mapa_general(res_calculo_act[93], filtro) 
                mapa = '{}static/img/img_mapas/mapa.png'.format(ruta)
                pdf.image(mapa,-10,45,145,145)

        except Exception as e:
            print(e)
            print("sin datos")

      
        altura_tri =175
        pos_cell = 104
        ancho_cel =106
        pdf.ln(7)
        
        sepador_mapa(pdf, True, "AFECTACIÓN A LA CAPACIDAD ARMADA DE LA AMENAZA", pos_cell, 12, ancho_cel)
        pdf.ln(-5)
        encabezado_comparativo_mapa_2(pdf, True, anio_act, anio_ant, anio_ant_tres,  pos_cell)
        altura = 61.5
        pos = claculo_mapa_2(pdf, res_calculo_ante[0], res_calculo_act[0], res_calculo_ante_tres[0], "MENORES RECUPERADOS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos


        pos = claculo_mapa_2(pdf, res_calculo_ante[1], res_calculo_act[1], res_calculo_ante_tres[0], "PRESENTACIÓN VOLUNTARIA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[2], res_calculo_act[2],res_calculo_ante_tres[2], "SOMETIMIENTOS",1, 7, 18,  pos_cell, ruta, altura_tri, altura)
        altura =  pos

        if filtro[17] == "sin_delco":
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 61,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 61,  "SI") #funcion para filtar el spoa
            valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 61,  "SI") #funcion para filtar el spoa
        else:
            valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 3,  "SI") #funcion para filtar el spoa
            valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 3,  "SI") #funcion para filtar el spoa
            valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 3,  "SI") #funcion para filtar el spoa


        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "CAPTURAS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 4,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 4,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 4,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "MDOM",1, 7, 18, pos_cell, ruta, altura_tri, altura)

        #sepador_mapa(pdf, True, "AFECTACIÓN A PROPIAS TROPAS ", pos_cell, 1, ancho_cel)
        #pdf.ln(6)



        #altura =  pos+6.9
        #valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 5,  "SI") #funcion para filtar el spoa
        #valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 5,  "SI") #funcion para filtar el spoa
        #valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 5,  "SI") #funcion para filtar el spoa
        #pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "ASESINADOS",-1, 7, 18, pos_cell, ruta, altura_tri, altura)
        #altura =  pos
        #valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 6,  "SI") #funcion para filtar el spoa
        #valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 6,  "SI") #funcion para filtar el spoa
        #valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 6,  "SI") #funcion para filtar el spoa
        #pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "HERIDOS",-1, 7, 18, pos_cell, ruta, altura_tri, altura)

        sepador_mapa(pdf, True, "AFECTACIÓN A LA CAPACIDAD ARMADA DE LA AMENAZA", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  pos+6.5
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 7,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 7,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 7,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "ARMAS DE LARGO ALCANCE",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 8,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 8,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 8,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "ARMAS DE CORTO ALCANCE",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 9,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 9,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 9,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "ARMAS DE ACOMPAÑAMIENTO",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 10,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 10,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 10,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0],valor_ant_tres[0], "MUNICIONES",1, 7, 18, pos_cell, ruta, altura_tri, altura)

        sepador_mapa(pdf, True, "COMBATES", pos_cell, 1, ancho_cel)
        pdf.ln(1)

        altura =  pos+6.5
        pos = claculo_mapa_2(pdf, res_calculo_ante[11], res_calculo_act[11],res_calculo_ante_tres[11], "COMBATES POSITIVOS",1, 8, 14, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[12], res_calculo_act[12],res_calculo_ante_tres[12], "COMBATES NEGATIVOS",-1, 8, 14, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        #pos = claculo_mapa_2(pdf, res_calculo_ante[13], res_calculo_act[13],res_calculo_ante_tres[13], "COMBATES SIN RESULTADOS",-1, 8, 14, pos_cell, ruta, altura_tri, altura)
        #altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[14], res_calculo_act[14],res_calculo_ante_tres[14], "TOTAL DE COMBATES",1, 8, 14, pos_cell, ruta, altura_tri, altura)

        sepador_mapa(pdf, True, "GUERRA DE MINAS", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  altura+9
        pos = claculo_mapa_2(pdf, res_calculo_ante[15], res_calculo_act[15], res_calculo_ante_tres[15], "NEUTRALIZACIÓN TERRORISTA",1, 8, 14, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[16], res_calculo_act[16], res_calculo_ante_tres[16], "A.E",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[17], res_calculo_act[17], res_calculo_ante_tres[17], "MAP ",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[18], res_calculo_act[18], res_calculo_ante_tres[18], "EXPLOSIVOS kg",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[19], res_calculo_act[19], res_calculo_ante_tres[19], "CORDÓN DETONANTE m",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[20], res_calculo_act[20], res_calculo_ante_tres[20], "CORDÓN DE SEGURIDAD m",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[72], res_calculo_act[72], res_calculo_ante_tres[72], "MEDIOS DE LANZAMIENTO",1, 7, 18, pos_cell, ruta, altura_tri, altura)


        #sepador_mapa(pdf, True, "ATAQUES A LA FUERZA PÚBLICA", pos_cell, 1, ancho_cel)
        #pdf.ln(6)
        #altura =  pos+7
        #pos = claculo_mapa_2(pdf, res_calculo_ante[66], res_calculo_act[66],res_calculo_ante_tres[66], "HOSTIGAMIENTOS",-1, 7, 18, pos_cell, ruta, altura_tri, altura)
        #altura =  pos
        #pos = claculo_mapa_2(pdf, res_calculo_ante[67], res_calculo_act[67],res_calculo_ante_tres[67], "ASONADAS",-1, 7, 18, pos_cell, ruta, altura_tri, altura)



        pdf.ln(-144)
        altura_tri =283
        pos_cell = 212
        ancho_cel =106

        altura = 45.2

        sepador_mapa(pdf, True, "AFECTACIÓN A LAS ECONOMÍAS ILÍCITAS - NARCOTRÁFICO", pos_cell, 1, ancho_cel)
        pdf.ln(-5)
        encabezado_comparativo_mapa_2(pdf, True, anio_act, anio_ant, anio_ant_tres,  pos_cell)

        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 21,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 21,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 21,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "COCAÍNA Kg",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 22,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 22,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 22,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "MARIHUANA Kg",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 23,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 23,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 23,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "PBC Kg",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 24,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 24,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 24,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "LAB. DE COCAÍNA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 25,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 25,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 25,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "LAB. BASE DE COCA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 26,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 26,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 26,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "SEMILLEROS",1, 7, 18, pos_cell, ruta, altura_tri, altura)


        sepador_mapa(pdf, True, "AFECTACIÓN A LAS ECONOMÍAS ILÍCITAS - EIYM", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  pos+6.5
        
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 33,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 33,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 33,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "CAPTURAS EIYM",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[35], res_calculo_act[35], res_calculo_ante_tres[35], "EIYM",1, 8, 14, pos_cell, ruta, altura_tri, altura)
        altura =  pos

        maquinaria_anterior = [res_calculo_ante[36], res_calculo_ante[37], res_calculo_ante[38], res_calculo_ante[39], res_calculo_ante[41]]
        maquinaria_anctual = [res_calculo_act[36], res_calculo_act[37], res_calculo_act[38], res_calculo_act[39], res_calculo_act[41]]
        maquinaria_anterior_tres = [res_calculo_ante_tres[36], res_calculo_ante_tres[37], res_calculo_ante_tres[38], res_calculo_ante_tres[39], res_calculo_ante_tres[41]]

        pos = claculo_mapa_mapa_2(pdf, maquinaria_anterior, maquinaria_anctual, maquinaria_anterior_tres, "MAQUINARIA AMARILLA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[65], res_calculo_act[65], res_calculo_ante_tres[65], "COLTÁN kg",1, 7, 18, pos_cell, ruta, altura_tri, altura)


        sepador_mapa(pdf, True, "AFECTACIÓN A LAS ECONOMÍAS ILÍCITAS - CONTRA LA LIBERTAD PERSONAL", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  pos+10
        pos = claculo_mapa_2(pdf, res_calculo_ante[42], res_calculo_act[42], res_calculo_ante_tres[42], "LIBERADOS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[43], res_calculo_act[43], res_calculo_ante_tres[43], "RESCATADOS",1, 7, 18, pos_cell, ruta, altura_tri, altura)


        sepador_mapa(pdf, True, "AFECTACIÓN A LAS ECONOMÍAS ILÍCITAS - HIDROCARBUROS", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  pos+6.5
        pos = claculo_mapa_2(pdf, res_calculo_ante[44], res_calculo_act[44], res_calculo_ante_tres[44], "VÁLVULAS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[45], res_calculo_act[45], res_calculo_ante_tres[45], "REFINERÍAS",1, 7, 18, pos_cell, ruta, altura_tri, altura)


        sepador_mapa(pdf, True, "AFECTACIÓN A LAS ECONOMÍAS ILÍCITAS  - CONTRABANDO", pos_cell, 1, ancho_cel)
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 49,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 49,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 49,  "SI") #funcion para filtar el spoa
        pdf.ln(1)
        altura =  pos+5
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "CAPTURAS CONTRABANDO",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[94], res_calculo_act[94], res_calculo_ante_tres[94], "LICORES CONTRABANDO",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos

        pos = claculo_mapa_2(pdf, res_calculo_ante[96], res_calculo_act[96], res_calculo_ante_tres[96], "TELÉFONOS CONTRABANDO",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[62], res_calculo_act[62], res_calculo_ante_tres[62], "COMBUSTIBLES CONTRABANDO",1, 7, 18, pos_cell, ruta, altura_tri, altura)



        sepador_mapa(pdf, True, "LOE AMAZONÍA", pos_cell, 1, ancho_cel)
        pdf.ln(1)
        altura =  pos+6.5
        valor_ant = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante, 30,  "SI") #funcion para filtar el spoa
        valor_act = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_act, 30,  "SI") #funcion para filtar el spoa
        valor_ant_tres = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo_ante_tres, 30,  "SI") #funcion para filtar el spoa
        pos = claculo_mapa_2(pdf, valor_ant[0], valor_act[0], valor_ant_tres[0], "CAPTURAS LOE AMAZONÍA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[32], res_calculo_act[32], res_calculo_ante_tres[32], "MADERA INCAUTADA",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[63], res_calculo_act[63], res_calculo_ante_tres[63], "ANIMALES INCAUTADOS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
        altura =  pos
        pos = claculo_mapa_2(pdf, res_calculo_ante[31], res_calculo_act[31], res_calculo_ante_tres[31], "PLÁNTULAS SEMBRADAS",1, 7, 18, pos_cell, ruta, altura_tri, altura)
    

        # claculo_mapa(pdf, res_calculo_ante[39], res_calculo_act[39], "BULDOCER(ES)",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[40], res_calculo_act[40], "UPM ILEGAL",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[41], res_calculo_act[41], "DRAGA(S)",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[65], res_calculo_act[65], "COLTAN KG",1, 7, 18)



        # claculo_mapa(pdf, res_calculo_ante[27], res_calculo_act[27], "MATA(S) DE COCA EN SEMILLERO",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[28], res_calculo_act[28], "INSUMOS LIQUIDOS Gal",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[29], res_calculo_act[29], "INSUMOS SOLIDOS Kg",1, 7, 18)




        # sepador_mapa(pdf, True, "PLAN AMAZONÍA")
        # claculo_mapa(pdf, res_calculo_ante[30], res_calculo_act[30], "CAPTURAS PLAN AMAZONIA",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[31], res_calculo_act[31], "PLANTULAS SEMBRADA",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[32], res_calculo_act[32], "MADERA INCAUTADA",1, 7, 18)
        # claculo_mapa(pdf, res_calculo_ante[63], res_calculo_act[63], "ANIMALES INCAUTADOS",1, 7, 18)




        # sepador_mapa(pdf, True, "DEPÓSITOS")
        # claculo_mapa(pdf, res_calculo_ante[46], res_calculo_act[46], "DEPÓSITO ILEGAL",1, 7, 18) 

        # # pdf.image(mapa,25,12,170,210)
        # # pdf.image(rosa_nautica,5, 40, 30, 30)


        # pdf.set_fill_color(193, 30, 38)
        # pdf.rounded_rect(65, 26, 115, 12, 1,'D', '1234')
        # pdf.set_text_color(0,0,0)
        # pdf.set_font('Arial', 'B', 10)
        # pdf.text(70,30,"FECHA INFORMACIÓN")
        # pdf.set_font('Arial', 'B', 8)
        # pdf.text(70,33.5,fecha_titulo)
        # pdf.text(70,37,fecha_titulo_dos)
    


