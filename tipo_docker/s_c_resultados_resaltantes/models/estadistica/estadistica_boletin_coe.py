# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.s_c_resultados_resaltantes.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.s_c_resultados_resaltantes.models.funtions.componest.tablas import *
conexion_pos = Databa_bases()
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            pass

    def  validar_spoa_unidad(self, filtro, res_calculo, numero, validar):
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


        # f.write("-----------------------------------------------------"+"\n")
        # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

        if validar == "SI":
            spoa = spoa
        else:
            spoa =  res_calculo[numero]
            

        return[spoa, no_spoa]


    # cuadro de resultados resaltantes 
    def resultados_resaltantes_pdf(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf, dato):

        dato =""
        filtros_y=[]

        filtros = selecion_filtro(filtro)
        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro)
        #print(query[1])
        resultados = conexion_pos.comando_query(query[0])
        hechos = conexion_pos.comando_query(query[1])
        erradicacion = conexion_pos.comando_query(query[2])
        
        res_calculo = estadistica_resultados(resultados, hechos, filtro)

        pdf.set_font('Arial', 'B', 9) 
        pdf.set_text_color(0, 0, 0)
        x, y, ang =4, 75, 90
        pdf.rotate(ang,x,y)
        pdf.text(x, y, "MENORES RECUPERADOS" )
        x, y, ang =58, 80.5, 90
        pdf.rotate(ang,x,y)
        pdf.text(x, y, "AFECTACIONES A LA AMENAZA" )
        x, y, ang =187.5, 89, 90
        pdf.rotate(ang,x,y)
        pdf.text(x, y, "AFECTACIONES PROPIAS TROPAS")
        pdf.rotate(0,x,y)

        # pdf.text(210, 200, "Oficial Centro de Operaciones de Ejército (Entrante) " )

        posicion_inicial =0
        posicion_inicial = cuadro_menores_edad(pdf, res_calculo[0])

        posicion_inicial_rme =0
        valor_cap = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 3,  "SI") #funcion para filtar el spoa
        valor_mdom = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 4,  "SI") #funcion para filtar el spoa
        datos_res =[res_calculo[1],res_calculo[2],valor_cap[0],valor_mdom[0]]
        posicion_inicial_rme = cuadro_enemigo_afectaciones(pdf, posicion_inicial, datos_res)



        posicion = 0
        valor_a = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 5,  "SI") #funcion para filtar el spoa
        valor_h = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 6,  "SI") #funcion para filtar el spoa
        datos_res_afectaciones = [valor_a[0], valor_h[0]]
        posicion = cuadro_afectaciones_tropas_combate (pdf, posicion_inicial_rme, datos_res_afectaciones )
        
        if filtro[30] == "sin":
            # cuadro_afectaciones(pdf, datos, filtro)
            pdf.set_fill_color(255, 255, 255)
            pdf.set_draw_color(0, 0, 0)
            pdf.rounded_rect(185, 30, 92, 59, 1,'F', '1234')

        pdf.ln(10)
        #separador
        pdf.set_line_width(1)
        pdf.line(4, 90, 263, 90)
        pdf.set_line_width(0.3)

        #calculo por grupos de resultados 
        pos = 98
        pos_vert = [20,40,10,17, 90, 30]

        if posicion == 0:
            if posicion_inicial_rme == 0:

                if posicion_inicial == 0:
                    numero = 60
                else:
                    pdf.ln(-posicion_inicial)
                    numero = 60
            else:
                pdf.ln(-posicion_inicial_rme)
                numero = 60
        else:

            pdf.ln(-posicion)
            numero = 60

            
        pdf.ln(numero)
        y = pdf.get_y()

        if res_calculo[7] or res_calculo[8] or res_calculo[9]  or res_calculo[10] :
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "MATERIAL DE GUERRA" )
            pos = pos + 6

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 7,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Largo Alcance", valor[0], 18, 'fusil.jpg', filtro)
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 8,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Corto Alcance", valor[0], 18, 'pistola.jpg', filtro)
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 9,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Armas de Acompañamiento", valor[0], 18, 'mortero.jpg', filtro)
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 10,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Municiones", valor[0], 18, 'municion.jpg', filtro)
            pos = pos + 4
            pdf.ln(10)


        if res_calculo[15] or res_calculo[16] or res_calculo[17] or res_calculo[18]  or res_calculo[19] or res_calculo[20]:
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(20, pos, "MATERIAL DE EXPLOSIVOS" )
            pos = pos + 6

            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización AE", res_calculo[16], 18, 'ae1.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización MAP", res_calculo[17], 18, 'map.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Explosivos Destruidos kg ", res_calculo[18], 18, 'esplosivos.jpg', filtro)

            pos = grupo_result_resal(pdf, pos_vert, pos, "Cordón Detonante m", res_calculo[19], 18, 'cordon.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Cordón de Seguridad m", res_calculo[20], 18, 'mecha.jpg', filtro)
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Neutralización Terrorista", res_calculo[15], 14, 'neutralizacion.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)



        if res_calculo[11] or res_calculo[12] or res_calculo[13] or res_calculo[14] :
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "COMBATES" )
            pos = pos + 6
            
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates con Resultados", res_calculo[11], 14, 'combate.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates sin Resultados", res_calculo[13], 14, 'combate_rs.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combates Negativos", res_calculo[12], 14, 'combate_neg.jpg', filtro)    
            pos = grupo_result_resal(pdf, pos_vert, pos, "Total de Combates", res_calculo[14], 14, 'combate.jpg', filtro)



        pdf.set_line_width(0.3)
        pdf.line(95, 95, 95, 205)
        

        #calculo por grupos de resultados 
        pos = 96
        pos_vert = [108,40,96,104, 175,28]
                    
        y = pdf.get_y()
    
        if y == 100.00125:
            pdf.ln(-numero)
            pdf.ln(56)

        else: 
            x = 100.00125 - y
            numero =  x -2
            pdf.ln(numero)

        

        if res_calculo[21] or res_calculo[22] or res_calculo[23] or res_calculo[24] or res_calculo[25] or res_calculo[26] or res_calculo[27] or res_calculo[28] or res_calculo[29] or res_calculo[47] or res_calculo[48]:
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "NARCOTRÁFICO" )
            pos = pos + 6
            
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 21,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Cocaína Kg", valor[0], 18, 'cocaina.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 47,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Cocaína en Proceso Gal", valor[0], 18, 'cocaina_pbc.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 22,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Marihuana Kg", valor[0], 18, 'marihuana.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 23,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Pasta Base de Coca Kg", valor[0], 18, 'pbc.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 48,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "P.B.C en Proceso Gal", valor[0], 18, 'pbc_proceso.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 24,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Laboratorios de Cocaína", valor[0], 18, 'lab_cocaina.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 25,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Laboratorios de PBC", valor[0], 18, 'lab_pbc.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 26,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Semilleros", valor[0], 18, 'semilleros.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 27,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Matas de Coca en Semilleros", valor[0], 18, 'erradicacion.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 28,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Insumos Iíquidos", valor[0], 18, 'liquidos.jpg', filtro)

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 29,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Insumos Sólidos", valor[0], 18, 'solidos.jpg', filtro)

            pos = pos + 4
            pdf.ln(8)

            
        if res_calculo[30] or res_calculo[31] or res_calculo[32] or res_calculo[63]:
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pos = pos - 2
            pdf.text(pos_vert[0], pos, "LOE AMAZONÍA" )
            pos = pos + 6
            
            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 30,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Capturas LOE Amazonía", valor[0], 18, 'capturas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Plántulas Sembradas", res_calculo[31], 18, 'plantulas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Incautacion Madera m3", res_calculo[32], 18, 'madera.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Especies Animales Incautados", res_calculo[63], 18, 'loro.jpg', filtro)

            pos = pos + 4
            pdf.ln(7)
        
        if res_calculo[46] :
            pos = pos - 2
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "DEPÓSITO ILEGAL")
            pos = pos + 5

            pos = grupo_result_resal(pdf, pos_vert, pos, "Depósito Ilegal", res_calculo[46], 18, 'deposito.jpg', filtro)

        pdf.set_line_width(0.3)
        pdf.line(179, 95, 179, 205)
        

        #calculo por grupos de resultados 
        pos = 98
        pos_vert = [202,42,181,188, 256.5, 23.5]

        y = pdf.get_y()
        if y == 100.00125:
            pdf.ln(-numero)
            pdf.ln(60)
        else: 
            x = 100.00125 - y
            numero =  x 
            pdf.ln(numero)

        
        if res_calculo[33] or res_calculo[34] or res_calculo[35] or res_calculo[36] or res_calculo[37] or res_calculo[38] or res_calculo[39] or res_calculo[40] or res_calculo[41] or res_calculo[65]:
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "MINERÍA ILEGAL")
            pos = pos + 6

            valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
            pos = grupo_result_resal(pdf, pos_vert, pos, "Capturas", valor[0], 18, 'capturas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Menores Recuperados", res_calculo[34], 18, 'rme.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "EIYM Minas Ilegales", res_calculo[35], 14, 'ejc.jpg', filtro)
            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Excavadoras", res_calculo[36], 18, 'excavadoras.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Retroexcavadoras", res_calculo[37], 18, 'retroexcavadoras.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Maquinaria Pesada", res_calculo[38], 18, 'maquinaria.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Tractor con Uruga", res_calculo[39], 18, 'buldocer.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Unidad Producción Minera", res_calculo[40], 18, 'upm.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Dragas", res_calculo[41], 18, 'dragas.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Coltán KG", res_calculo[65], 18, 'coltan.jpg', filtro)

            pos = pos + 4
            pdf.ln(10)
        
        if res_calculo[42] or res_calculo[43] or res_calculo[44] or res_calculo[45] or res_calculo[62] :
            
            pdf.set_font('Arial', 'B', 12)
            pdf.set_text_color(0, 0, 0)
            pdf.text(pos_vert[0], pos, "ECONOMÍAS ILÍCITAS")
            pos = pos + 6

            
            pos = grupo_result_resal(pdf, pos_vert, pos, "Liberados", res_calculo[42], 18, 'cadena.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Rescatados", res_calculo[43], 18, 'cadena2.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Válvulas Ilícitas Destruidas", res_calculo[44], 18, 'valvula.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Refinerías Ilegales Destruidas", res_calculo[45], 18, 'refineria.jpg', filtro)
            pos = grupo_result_resal(pdf, pos_vert, pos, "Combustible Incautado Gal", res_calculo[62], 18, 'combustible.jpg', filtro)


            pos = pos + 4
            pdf.ln(10)


