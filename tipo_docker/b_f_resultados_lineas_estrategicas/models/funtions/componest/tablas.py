import math
import pandas as pd
class Calculo_Spoa:
    def __init__(self):
            self.archivo = "RESULTADO SIN SPOA" +".txt"              
            self.f = open("doc_sin_spoa/"+self.archivo, "w")
            self.f.write(str("RESULTADO")+", " + str("HR")+", " +str("FECHA")+", "+str("SPOA")+", "+str("DIV")+"\n")

    def validar_spoa_unidad(filtro, res_calculo, numero, validar):
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


 
def encabezado_coe(pdf, fill):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 9)

    pdf.cell(50,5,"DIVISIONES",1,0, 'C',fill)
    pdf.cell(15,10,"DIV01",1,0, 'C',fill)
    pdf.cell(15,10,"DIV02",1,0, 'C',fill)
    pdf.cell(15,10,"DIV03",1,0, 'C',fill)
    pdf.cell(15,10,"DIV04",1,0, 'C',fill)
    pdf.cell(15,10,"DIV05",1,0, 'C',fill)
    pdf.cell(15,10,"DIV06",1,0, 'C',fill)
    pdf.cell(15,10,"DIV07",1,0, 'C',fill)
    pdf.cell(15,10,"DIV08",1,0, 'C',fill)
    pdf.cell(15,10,"DAVAA",1,0, 'C',fill)
    pdf.cell(15,10,"DIVFE",1,0, 'C',fill)
    pdf.cell(15,10,"FUTCO",1,0, 'C',fill)
    pdf.cell(15,10,"FTCEC",1,0, 'C',fill)
    pdf.cell(20,10,"TOTAL",1,0, 'C',fill)
    pdf.cell(16,10,"GAO-r",1,0, 'C',fill)
    pdf.cell(16,10,"GDO",1,0, 'C',fill)
    pdf.cell(16,10,"GAO-ELN",1,0, 'C',fill)
    pdf.cell(16,10,"GAO-CG",1,0, 'C',fill)
    pdf.cell(16,10,"NARCO",1,0, 'C',fill)
    pdf.cell(16,10,"DELCO",1,0, 'C',fill)

    pdf.set_fill_color(227, 227, 211)
    pdf.set_text_color(0,0,0)
    pdf.ln(5)
    pdf.cell(-5)
    pdf.cell(50,5,"EVENTO",1,0, 'C',fill)

def encabezado_coe_regiones(pdf, fill):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 9)

    pdf.cell(70,5,"REGIONES",1,0, 'C',fill)
    pdf.cell(23,10,"AMAZÓNICA",1,0, 'C',fill)
    pdf.cell(23,10,"ANDINA",1,0, 'C',fill)
    pdf.cell(23,10,"CARIBE",1,0, 'C',fill)
    pdf.cell(23,10,"ORINOQUÍA",1,0, 'C',fill)
    pdf.cell(23,10,"PACÍFICA",1,0, 'C',fill)
    
    pdf.cell(23,10,"TOTAL",1,0, 'C',fill)

    pdf.cell(23,10,"GAO-r",1,0, 'C',fill)
    pdf.cell(23,10,"GDO",1,0, 'C',fill)
    pdf.cell(23,10,"GAO-ELN",1,0, 'C',fill)
    pdf.cell(23,10,"GAO-CG",1,0, 'C',fill)
    pdf.cell(23,10,"NARCO",1,0, 'C',fill)
    pdf.cell(23,10,"DELCO",1,0, 'C',fill)

    pdf.set_fill_color(227, 227, 211)
    pdf.set_text_color(0,0,0)
    pdf.ln(5)
    pdf.cell(-5)
    pdf.cell(70,5,"EVENTO",1,0, 'C',fill)

def separador_cuadro_coe(pdf, fill, text):
    pdf.ln(5)
    pdf.cell(-5)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(227, 227, 211)
    pdf.cell(346,5,text,1,0, 'C',fill)
 
def estadistica_resultados(datos_res, hechos, filtro):
    
    if filtro[18] != "---" :
        # print(filtro[18])
        datos_res = list(filter(lambda datos_res: str(filtro[18]) in datos_res[17], datos_res))
        hechos = list(filter(lambda hechos: str(filtro[18]) in hechos[9], hechos))
   
    if filtro[19] == "gaulas" :
        datos_res = list(filter(lambda datos_res: str("GG") in datos_res[4], datos_res))
        hechos = list(filter(lambda hechos: str("GG" ) in hechos[5], hechos))
           
    if filtro[20] != "---" and filtro[20] !="":
        datos_res = list(filter(lambda datos_res: str(filtro[20]) in datos_res[30], datos_res))
        hechos = list(filter(lambda hechos: str(filtro[20]) in hechos[25], hechos))
    
    if filtro[21] != "---" and filtro[21] !="":
        datos_res = list(filter(lambda datos_res: str(filtro[21]) in datos_res[31], datos_res))
        hechos = list(filter(lambda hechos: str(filtro[21]) in hechos[26], hechos))
           
    if filtro[23] != "---" and filtro[23] !="":
        datos_res = list(filter(lambda datos_res: str(filtro[23]) in datos_res[32], datos_res))
        hechos = list(filter(lambda hechos: str(filtro[23]) in hechos[27], hechos))
                       
    #filtar por hechos
    if filtro[25] != "---" and filtro[25] !="":
        datos_res = list(filter(lambda datos_res: str(filtro[25]) in datos_res[28], datos_res))
        hechos = list(filter(lambda hechos: str(filtro[25]) in hechos[0], hechos))
     
    #variable para calcular los heridos y asesinados fuera de comabte 
    asesinado_direfente_al_enemigo ="MUERTE POR CAUSAS AJENAS AL SERVICIO EN DESCANSO" 
    asesinado_direfente_al_enemigo_v1 ="MUERTO POR CAUSAS DEL SERVICIO- DIFERENTES A LAS ACCIONES DIRECTAS DEL ENEMIGO" 
    asesinado_direfente_al_enemigo_v2 ="MUERTE POR CAUSAS DEL SERVICIO EN ENTRENAMIENTO" 

    #asesinados

    asesinados_fuera_combate = list(filter(lambda datos_res:  asesinado_direfente_al_enemigo == datos_res[28] or asesinado_direfente_al_enemigo_v1 == datos_res[28] or asesinado_direfente_al_enemigo_v2 == datos_res[28], datos_res))

    asesinados_fuera_combate_f = list(filter(lambda asesinados_fuera_combate: "EJERCITO" in asesinados_fuera_combate[12], asesinados_fuera_combate))

    herido_direfente_al_enemigo ="HERIDO(A) POR CAUSAS DEL SERVICIO- DIFERENTES A LAS ACCIONES DIRECTAS DEL ENEMIGO" 
    herido_direfente_al_enemigo_v1 ="HERIDO(A) POR CAUSAS AJENAS AL SERVICIO EN DESCANSO" 
    herido_direfente_al_enemigo_v2 ="HERIDO(A) POR CAUSAS DEL SERVICIO- EN ENTRENAMIENTO" 
    
    #heridos 

    herido_fuera_combate = list(filter(lambda datos_res: herido_direfente_al_enemigo in datos_res[28] or herido_direfente_al_enemigo_v1 in datos_res[28] or herido_direfente_al_enemigo_v2 in datos_res[28], datos_res))
    herido_fuera_combate_f = list(filter(lambda herido_fuera_combate: "EJERCITO" in herido_fuera_combate[12], herido_fuera_combate))


    #MENORES RECUPERADOS
    rme = list(filter(lambda datos_res: "RME" in datos_res[9], datos_res))
    # print(rme[1])
    #PRESENTACIONES VOLUNTARIAS
    presentacion_voluntaria = list(filter(lambda datos_res: "PRESENTACIONES" in datos_res[9] or "ENTREGA" in datos_res[9] and datos_res[7] != "DELINCUENCIA" , datos_res))
    presentacion_voluntaria = list(filter(lambda presentacion_voluntaria: "RME" not in presentacion_voluntaria[9] , presentacion_voluntaria))
    #SOMETIMIENTOS
    sometimientos = list(filter(lambda datos_res: "SOMETIMIENTO" in datos_res[9]  and datos_res[7] != "GAO ELN" and datos_res[7] != "DELINCUENCIA"  , datos_res))
    sometimientos = list(filter(lambda sometimientos: "RME" not in sometimientos[9] , sometimientos))
    #res accion capturas
    res_capturas = list(filter(lambda datos_res: "CAPTURADO(A)" in datos_res[9], datos_res))
    #capturas 
    capturas = list(filter(lambda res_capturas: "CAPTURADO(A)" in res_capturas[9]  and res_capturas[7] != "NO APLICA", res_capturas))
    capturas = list(filter(lambda capturas: "RME" not in capturas[9] , capturas))

    capturas_extorcion = list(filter(lambda capturas:  capturas[17] == "Extorsión y Secuestro" , capturas))


    capturas_sin_delco = list(filter(lambda capturas: "CAPTURADO(A)" in capturas[9]  and capturas[7] != "DELINCUENCIA", capturas))
    capturas_sin_delco = list(filter(lambda capturas_sin_delco: "RME" not in capturas_sin_delco[9] , capturas_sin_delco))
    #mdom
    mdom = list(filter(lambda datos_res: "MUERTOS EN DESARROLLO" in datos_res[9]  and datos_res[7] != "NO APLICA" , datos_res))
    # mdom = list(filter(lambda mdom: "RME" not in mdom[9] , mdom))
        
    if filtro[22] != "---" and filtro[22] !="":
        variable_ase_1 = "ASESINADO(A)" + " "+str(filtro[22])
        variable_ase_2 = "ASESINADO(S)" + " "+str(filtro[22])
        variable_her_1 = "HERIDO(A)" + " "+str(filtro[22])
        variable_her_2 = "HERIDO(S)" + " "+str(filtro[22])
    else:
        variable_ase_1 = "ASESINADO(A)"
        variable_ase_2 = "ASESINADO(S)"
        variable_her_1 = "HERIDO(A)"
        variable_her_2 = "HERIDO(S)"

    #asesinados
    asesinados = list(filter(lambda datos_res: variable_ase_1 in datos_res[9] or variable_ase_2 in datos_res[9], datos_res))
    asesinados = list(filter(lambda asesinados: asesinados[28] != "FUEGO AMIGO", asesinados))
    asesinados = list(filter(lambda asesinados: "EJERCITO" in asesinados[12], asesinados))
    # print(asesinados)
    #heridos 
    heridos = list(filter(lambda datos_res: variable_her_1 in datos_res[9] or variable_her_2 in datos_res[9],  datos_res))
    heridos = list(filter(lambda heridos: heridos[28] != "FUEGO AMIGO",  heridos))
    heridos = list(filter(lambda heridos: "EJERCITO" in heridos[12], heridos))
    #MATERIAL DE GUERRA
    armas_largas = list(filter(lambda datos_res:  datos_res[11] == "ARMAS DE LARGO ALCANCE" , datos_res))
    armas_largas = list(filter(lambda armas_largas: "INCAUTADO(A)" in armas_largas[9]  or "DESTRUIDO(A)" in armas_largas[9] or "RECUPERADO(A)" in armas_largas[9]  , armas_largas))
    #armas cortgas
    armas_cortas = list(filter(lambda datos_res:  datos_res[11] == "ARMAS DE CORTO ALCANCE" , datos_res))
    armas_cortas = list(filter(lambda armas_cortas: "INCAUTADO(A)" in armas_cortas[9]  or "DESTRUIDO(A)" in armas_cortas[9] or "RECUPERADO(A)" in armas_cortas[9]  , armas_cortas))
    #armas de acompañamiento
    armas_acompaniamiento = list(filter(lambda datos_res:  datos_res[11] == "ARMAS DE ACOMPAÑAMIENTO" , datos_res))
    armas_acompaniamiento = list(filter(lambda armas_acompaniamiento: "INCAUTADO(A)" in armas_acompaniamiento[9]  or "DESTRUIDO(A)" in armas_acompaniamiento[9] or "RECUPERADO(A)" in armas_acompaniamiento[9]  , armas_acompaniamiento))
    #municiones
    municiones = list(filter(lambda datos_res:  datos_res[11] == "MUNICION" , datos_res))
    municiones = list(filter(lambda municiones: "INCAUTADO(A)" in municiones[9]  or "DESTRUIDO(A)" in municiones[9] or "RECUPERADO(A)" in municiones[9]  , municiones))
    #COMATES
    combates_pos = list(filter(lambda hechos :  hechos[0] == "COMBATE" and hechos[13] == "SI" , hechos))
    comates_neg = list(filter(lambda hechos :  hechos[0] == "COMBATE" and hechos[13] == "NO" , hechos))
    combates_sin = list(filter(lambda hechos :  hechos[0] == "COMBATE" and hechos[13] == "SR" , hechos))
    combates = list(filter(lambda hechos :  hechos[0] == "COMBATE", hechos))
    #ATAQUE FUERZA PUBLICA
    ataque_fuerza = list(filter(lambda hechos :  hechos[0] == "ATAQUE FUERZA PUBLICA", hechos))
    #EXPLOSIVOS
    neutralizacion_terrorista = list(filter(lambda hechos :  hechos[0] == "NEUTRALIZACIONES ACCIONES TERRORISTAS" , hechos))
    #hostigamientos
    hostigamientos = list(filter(lambda datos_res: "HOSTIGAMIENTO" in datos_res[9], datos_res))
    hostigamientos = list(filter(lambda hostigamientos: "UNIDAD MILITAR" in hostigamientos[10], hostigamientos))
    hostigamientos = list(filter(lambda hostigamientos: "EJERCITO" in hostigamientos[12], hostigamientos))
    #hostigamientos
    asonadas = list(filter(lambda datos_res: "ASONADA" in datos_res[9], datos_res))
    asonadas = list(filter(lambda asonadas: "UNIDAD MILITAR" in asonadas[10], asonadas))
    asonadas = list(filter(lambda asonadas: "EJERCITO" in asonadas[12], asonadas))
    #a.e
    ae = list(filter(lambda datos_res:  datos_res[12] == "A.E" , datos_res))
    ae = list(filter(lambda ae: "INCAUTADO(A)" in ae[9]  or "DESTRUIDO(A)" in ae[9] or "RECUPERADO(A)" in ae[9]  , ae))
    #map
    map_anti_perosna = list(filter(lambda datos_res:  datos_res[12] == "MAP(Mina Anti Persona)" , datos_res))
    map_anti_perosna = list(filter(lambda map_anti_perosna: "INCAUTADO(A)" in map_anti_perosna[9]  or "DESTRUIDO(A)" in map_anti_perosna[9] or "RECUPERADO(A)" in map_anti_perosna[9]  , map_anti_perosna))
    #explosivos
    explosivos = list(filter(lambda datos_res:  datos_res[11] == "EXPLOSIVOS" , datos_res))
    explosivos = list(filter(lambda explosivos:  explosivos[17] != "Explotación Ilícita de Yacimientos Mineros" , explosivos))
    explosivos_kg = list(filter(lambda explosivos: explosivos[13] == 'Kg', explosivos))
    #explosivos metros
    explosivos_m = list(filter(lambda explosivos: explosivos[13] == 'M', explosivos))
    #explosivos unidad
    explosivos_und = list(filter(lambda explosivos: explosivos[13] == 'Und(s)', explosivos))
    #cordon detonante
    cordon = list(filter(lambda datos_res:  datos_res[12] == "CORDÓN DETONANTE" , datos_res))
    cordon = list(filter(lambda cordon: cordon[13] == 'M', cordon))
    #mecha lenta
    mecha = list(filter(lambda datos_res:  datos_res[12] == "MECHA LENTA" , datos_res))
    mecha = list(filter(lambda mecha: mecha[13] == 'M', mecha))
    #medios de lanzamientos
    medios_lanzamientos = list(filter(lambda datos_res: datos_res[12] == "MEDIOS DE LANZAMIENTO" and datos_res[13] == "Und(s)" and datos_res[11] == "MEDIOS DE LANZAMIENTO (FCI)", datos_res) )
    #detonadores anelectricos
    detonador_ini_electrico= list(filter(lambda datos_res: datos_res[12] == "DETONADOR(ES) IN ELECTRICO(S)" and datos_res[13] == "Und(s)" and datos_res[11] == "EXPLOSIVOS", datos_res) )
    #detonadores electricos
    detonador_electrico= list(filter(lambda datos_res: datos_res[12] == "DETONADORES ELÉCTRICOS" and datos_res[13] == "Und(s)" and datos_res[11] == "EXPLOSIVOS", datos_res) )
    #artefactos explosivos 
    artefactos_explosivos = list(filter(lambda datos_res:  datos_res[11] == "ARTEFACTOS EXPLOSIVOS" , datos_res))
    artefactos_explosivos = list(filter(lambda artefactos_explosivos:  artefactos_explosivos[12] != "CILINDRO(S) VACIOS" , artefactos_explosivos))

    
    #narcotrafico
    #capturas
    capturas_narcotrafico = list(filter(lambda res_capturas:  res_capturas[17] == "Narcotráfico" , res_capturas))
    #cocaina
    cocaina = list(filter(lambda datos_res: datos_res[12] == "COCAÍNA" and datos_res[13] == "Kg" and datos_res[11] == "DROGA", datos_res) )
    #marihuana
    marihuana = list(filter(lambda datos_res: datos_res[12] == "MARIHUANA" and datos_res[13] == "Kg" and datos_res[11] == "DROGA", datos_res) )
    #pbc
    pbc = list(filter(lambda datos_res: datos_res[12] == "PASTA DE COCA" or datos_res[12] == "BASE DE COCA" and datos_res[13] == "Kg" and datos_res[11] == "DROGA", datos_res) )
    #basuco
    basuco = list(filter(lambda datos_res: datos_res[12] == "BASUCO" and datos_res[13] == "Kg" and datos_res[11] == "DROGA", datos_res) )
    #HEROÍNA
    herohina = list(filter(lambda datos_res: datos_res[12] == "HEROÍNA" and datos_res[13] == "Kg" and datos_res[11] == "DROGA", datos_res) )
    #DROGAS SINTETICAS
    drogas_sinteticas = list(filter(lambda datos_res: datos_res[11] == "DROGAS SINTETICAS", datos_res) )
    #lab clorhidrato
    lab_heroina = list(filter(lambda datos_res: datos_res[12] == "LABORATORIO MORFINA Y HEROINA", datos_res))
    #lab clorhidrato
    lab_cocaina = list(filter(lambda datos_res: datos_res[12] == "LABORATORIO CLORHIDRATO DE COCAINA", datos_res))
    #lab pbc
    lab_pbc = list(filter(lambda datos_res: datos_res[12] == "LABORATORIO PASTA O BASE DE COCA", datos_res))
    #semilleros
    semilleros = list(filter(lambda datos_res: datos_res[12] == "SEMILLERO", datos_res))
    #matas coca
    matas_coca = list(filter(lambda datos_res: "MATA(S) DE COCA EN SEMILLERO" in datos_res[12] or "MATAS DE COCA" in datos_res[12] , datos_res))
    #insumos liquidos
    afectacion_narcotrafico = list(filter(lambda datos_res: "Narcotráfico" in datos_res[17], datos_res))
    insumos = list(filter(lambda afectacion_narcotrafico: "INSUMOS" in afectacion_narcotrafico[10],  afectacion_narcotrafico))
    insumos_liquidos = list(filter(lambda insumos:  insumos[13] == "Gal", insumos))
    insumos_solidos = list(filter(lambda insumos:  insumos[13] == "Kg", insumos))
    #combustible_narcotrafico
    combustibles_narcotrafico = list(filter(lambda afectacion_narcotrafico: 'COMBUSTIBLES' in afectacion_narcotrafico[10], afectacion_narcotrafico))
    # combustibles_narcotrafico = list(filter(lambda combustibles_narcotrafico:  combustibles_narcotrafico[12] != "PETROLEO", combustibles_narcotrafico))
    combustibles_narcotrafico = list(filter(lambda combustibles_narcotrafico:  combustibles_narcotrafico[13] == "Gal", combustibles_narcotrafico))
    #cocaina proseso
    tipo = list(filter(lambda datos_res: datos_res[10] == "NARCOTRAFICO" and datos_res[11] == "DROGA", datos_res))
    cocaina_proceso = list(filter(lambda tipo: tipo[12] == "COCAÍNA EN PROCESO", tipo))
    #pbc en proceso
    pbc_proceso = list(filter(lambda tipo: tipo[12] == "BASE DE COCA EN PROCESO" or tipo[12] == "PASTA DE COCA EN PROCESO",  tipo))
    #plan amazonia
    #capturas
    capturas_artemisa = list(filter(lambda res_capturas: "Afectación Recursos Naturales y Medio Ambiente" in res_capturas[17], res_capturas))
    #plantulas sembradas
    plantulas_sembradas = list(filter(lambda datos_res: "SEMBRADO(S)" in datos_res[9], datos_res))
    #madera incautada
    madera = list(filter(lambda datos_res: "DESTRUIDO(A)" in datos_res[9] or "INCAUTADO(A)" in datos_res[9] or "RECUPERADO(A)" in datos_res[9], datos_res))
    madera = list(filter(lambda madera: "MADERA" in madera[12], madera))
    especies_aninales = list(filter(lambda datos_res: 'Afectación Recursos Naturales y Medio Ambiente' in datos_res[17], datos_res))
    especies_aninales = list(filter(lambda especies_aninales: 'INCAUTADO(A)' in especies_aninales[9] or 'RECUPERADO(A)' in especies_aninales[9], especies_aninales))
    especies_aninales = list(filter(lambda especies_aninales: 'ANIMAL(ES)' in especies_aninales[10] or 'ESPECIES EN VIA DE EXTINCIÓN' in especies_aninales[10], especies_aninales))
    especies_aninales = list(filter(lambda especies_aninales: 'SEMOVIENTES' != especies_aninales[11] and 'ESPECIES SILVESTRES FLORA' != especies_aninales[11], especies_aninales))
    especies_aninales = list(filter(lambda especies_aninales: 'Kg' != especies_aninales[13], especies_aninales))
    #mineria ilegal 
    #capturas
    capturas_mineria = list(filter(lambda res_capturas:  res_capturas[17] == "Explotación Ilícita de Yacimientos Mineros" , res_capturas))
    afectacion_mineria = list(filter(lambda datos_res:  datos_res[17] == "Explotación Ilícita de Yacimientos Mineros" , datos_res))
    #rme
    rme_mineria = list(filter(lambda afectacion_mineria: 'RME' in afectacion_mineria[9] , afectacion_mineria))
    #EIYM
    eiym = list(filter(lambda hechos :  hechos[0] == "EXPLORACIÓN Y EXPLOTACIÓN ILÍCITA" , hechos))
    #upm
    upm = list(filter(lambda afectacion_mineria: 'UPM ILEGAL' in afectacion_mineria[12] or 'UPM LEGAL' in afectacion_mineria[12] or 'SOCAVON' in afectacion_mineria[12] , afectacion_mineria))
    
    
    #maquinaria pesada
    maquinaria_pesada = list(filter(lambda afectacion_mineria: 'MAQUINARIA PESADA' in afectacion_mineria[12] or 'CLASIFICADORA(S)' in afectacion_mineria[12] or 'TRITURADORA(S)' in afectacion_mineria[12] or 'MEZCLADORA(S)' in afectacion_mineria[12], afectacion_mineria))
    #excavadoras
    excavadoras = list(filter(lambda afectacion_mineria: 'EXCAVADORA(S)' == afectacion_mineria[12] , afectacion_mineria))
    #retroexcavadoras
    retroexcavadoras = list(filter(lambda afectacion_mineria: 'RETROEXCAVADORA(S)' == afectacion_mineria[12] , afectacion_mineria))
    #buldicer
    buldocer = list(filter(lambda afectacion_mineria: 'BULDOCER(ES)' in afectacion_mineria[12] , afectacion_mineria))
    #dragas
    dragas = list(filter(lambda afectacion_mineria: 'DRAGA(S)' in afectacion_mineria[12] or 'DRAGON(ES)' in afectacion_mineria[12] , afectacion_mineria))
    
    maquinaria_amarilla = list(filter(lambda afectacion_mineria: 'BULDOCER(ES)' in afectacion_mineria[12] or 'EXCAVADORA(S)' in afectacion_mineria[12] or 'RETROEXCAVADORA(S)' in afectacion_mineria[12] or 'MOTONIVELADORA(S)' in afectacion_mineria[12], afectacion_mineria))
    
    maquinaria_linea_amarilla = list(filter(lambda afectacion_mineria: 'MAQUINARIA PESADA' in afectacion_mineria[12] or 'CLASIFICADORA(S)' in afectacion_mineria[12] or 'TRITURADORA(S)' in afectacion_mineria[12] or 'MEZCLADORA(S)' in afectacion_mineria[12] or 'EXCAVADORA(S)' in afectacion_mineria[12] or 'RETROEXCAVADORA(S)' in afectacion_mineria[12] or 'BULDOCER(ES)' in afectacion_mineria[12] or 'MOTONIVELADORA(S)' in afectacion_mineria[12], afectacion_mineria))
    
    
    #motores
    motores = list(filter(lambda afectacion_mineria: 'MOTORES' in afectacion_mineria[12] or 'MOTOBOMBA(S)' in afectacion_mineria[12] or 'PLANTA ELÉCTRICA' in afectacion_mineria[12] or 'MOTOR FUERA DE BORDA' in afectacion_mineria[12], afectacion_mineria))
    
    #Combustibles
    combustibles_mineria = list(filter(lambda afectacion_mineria: 'COMBUSTIBLES' in afectacion_mineria[10], afectacion_mineria))
    # combustibles_mineria = list(filter(lambda combustibles_mineria:  combustibles_mineria[12] != "PETROLEO", combustibles_mineria))
    combustibles_mineria = list(filter(lambda combustibles_mineria:  combustibles_mineria[13] == "Gal", combustibles_mineria))
    #explosivos mineria
    explosivos_mineria = list(filter(lambda datos_res:  datos_res[11] == "EXPLOSIVOS" , datos_res))
    explosivos_mineria = list(filter(lambda explosivos_mineria:  explosivos_mineria[17] == "Explotación Ilícita de Yacimientos Mineros" , explosivos_mineria))
    explosivos_mineria_kg = list(filter(lambda explosivos_mineria: explosivos_mineria[13] == 'Kg', explosivos_mineria))
    #explosivos metros
    explosivos_mineria_m = list(filter(lambda explosivos_mineria: explosivos_mineria[13] == 'M', explosivos_mineria))
    #explosivos unidad
    explosivos_mineria_und = list(filter(lambda explosivos_mineria: explosivos_mineria[13] == 'Und(s)', explosivos_mineria))
    #material de transporte
    material_transporte =  list(filter(lambda afectacion_mineria: 'MATERIAL DE TRANSPORTE' in afectacion_mineria[10], afectacion_mineria))
    material_transporte =  list(filter(lambda material_transporte: 'ACCESORIOS'  not in material_transporte[11], material_transporte))
    #economias ilicitas
    #liberados
    liberados = list(filter(lambda datos_res: "LIBERADO" in datos_res[9] , datos_res))
    #rescatados
    rescatados = list(filter(lambda datos_res: "RESCATADO" in datos_res[9] , datos_res))
    #afectacion al olecducto
    #oleoducto
    oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    #petroleo
    petroleo = list(filter(lambda datos_res: "COMBUSTIBLES" in datos_res[10], datos_res))
    petroleo = list(filter(lambda petroleo:  petroleo[13] == "Gal", petroleo))
    #piscina
    # piscina = list(filter(lambda datos_res: 'COMBUSTIBLES' in datos_res[10], datos_res))
    piscina = list(filter(lambda datos_res: "PISCINA(S)" in datos_res[12] or  "PISCINA PARA ALMACENAMIENTO" in datos_res[12],  datos_res))

    
    #valvulas
    valvula = list(filter(lambda datos_res: "VALVULA" in datos_res[12] or "VÁLVULA" in datos_res[12] , datos_res))
    #refinerias
    refineria = list(filter(lambda datos_res: "REFINERIA" in datos_res[12], datos_res))
    #depositos
    depositos = list(filter(lambda datos_res: "DEPÓSITO ILEGAL" in datos_res[12], datos_res)) 
    dolares= list(filter(lambda datos_res: datos_res[12] == "DÓLARES", datos_res) )
    pesos_colombianos= list(filter(lambda datos_res: datos_res[12] == "PESOS COLOMBIANOS" , datos_res) )
    euros= list(filter(lambda datos_res: datos_res[12] == "EUROS" , datos_res) )
    #mineria contrabando
    #capturas
    capturas_contrabando = list(filter(lambda res_capturas:  res_capturas[17] == "Contrabando" , res_capturas))
    estrategia_contrabando = list(filter(lambda datos_res:  datos_res[17] == "Contrabando" , datos_res))
    gasolina_contrabando = list(filter(lambda estrategia_contrabando:  "GASOLINA" in estrategia_contrabando[12] and estrategia_contrabando[13] == "Gal" , estrategia_contrabando))
    acpm_contrabando = list(filter(lambda estrategia_contrabando:  "ACPM" in estrategia_contrabando[12] and estrategia_contrabando[13] == "Gal" , estrategia_contrabando)) 
    insumos_liquidos_contrabando = list(filter(lambda estrategia_contrabando:  "INSUMOS" in estrategia_contrabando[10] or "COMBUSTIBLES" in estrategia_contrabando[10] and estrategia_contrabando[13] == "Gal" , estrategia_contrabando))
    vehiculos_contrabando = list(filter(lambda estrategia_contrabando:  "TERRESTRE" in estrategia_contrabando[11] and "MATERIAL DE TRANSPORTE" in estrategia_contrabando[10], estrategia_contrabando))
    animales_incautados_contrabando = list(filter(lambda estrategia_contrabando:  "SEMOVIENTES" in estrategia_contrabando[11] and "ANIMALES" in estrategia_contrabando[10], estrategia_contrabando))
    elementos_escolares_contrabando = list(filter(lambda estrategia_contrabando:  "ELEMENTOS ESCOLARES" in estrategia_contrabando[12] and "BIENES" in estrategia_contrabando[10], estrategia_contrabando))
    jugueteria_contrabando = list(filter(lambda estrategia_contrabando:  "JUGUETERÍA" in estrategia_contrabando[12] and "BIENES" in estrategia_contrabando[10], estrategia_contrabando))
    prendas_vestir_contrabando = list(filter(lambda estrategia_contrabando:  "PRENDAS DE VESTIR" in estrategia_contrabando[12] and "BIENES" in estrategia_contrabando[10], estrategia_contrabando))
    #Combustibles
    combustibles_contrabando = list(filter(lambda estrategia_contrabando: 'COMBUSTIBLES' in estrategia_contrabando[10], estrategia_contrabando))
    # combustibles_contrabando = list(filter(lambda combustibles_contrabando:  combustibles_contrabando[12] != "PETROLEO", combustibles_contrabando))
    combustibles_contrabando = list(filter(lambda combustibles_contrabando:  combustibles_contrabando[13] == "Gal", combustibles_contrabando))
    hechos_contrabando = list(filter(lambda hechos :  hechos[9] == "Contrabando" , hechos))
    coltan = list(filter(lambda datos_res: datos_res[12] == "COLTAN" and datos_res[13] == "Kg" and datos_res[11] == "METALES", datos_res) )

    # extincion de dominio

    # extincion de dominio
    afectacion_extincion_dominio = list(filter(lambda datos_res: 'EXTINCIÓN DE DOMINIO' in datos_res[28], datos_res))
    vehiculos = list(filter(lambda afectacion_extincion_dominio: 'MATERIAL DE TRANSPORTE' == afectacion_extincion_dominio[10], afectacion_extincion_dominio))
    afectacion_extincion_dominio = list(filter(lambda afectacion_extincion_dominio: 'BIENES' in afectacion_extincion_dominio[10], afectacion_extincion_dominio))

    inmuebles = list(filter(lambda afectacion_extincion_dominio: 'INMUEBLES' == afectacion_extincion_dominio[11], afectacion_extincion_dominio))
    muebles = list(filter(lambda afectacion_extincion_dominio: 'MUEBLES' == afectacion_extincion_dominio[11], afectacion_extincion_dominio))

    ataque_con_drons = list(filter(lambda datos_res: "ATAQUE CON UAS (SISTEMA AÉREO NO TRIPULADO) ADECUADO CON EXPLOSIVOS" in datos_res[9], datos_res))
    ataque_con_drons = list(filter(lambda ataque_con_drons: "UNIDAD MILITAR" in ataque_con_drons[10], ataque_con_drons))
    ataque_con_drons_f = list(filter(lambda ataque_con_drons: "EJERCITO" in ataque_con_drons[12], ataque_con_drons))

    derribado_con_drons = list(filter(lambda datos_res: "DERRIBADO(A)" in datos_res[9] or "INUTILIZADO(A)" in datos_res[9] or "DESTRUIDO(A)" in datos_res[9] or "INCAUTADO(A)" in datos_res[9], datos_res))
    derribado_con_drons_f = list(filter(lambda derribado_con_drons: "VEHICULO AEREO NO TRIPULADO VANT" in derribado_con_drons[10], derribado_con_drons))


    incidente_cibernetico_contenido = list(filter(lambda datos_res :  datos_res[28] == "INCIDENTE CIBERNÉTICO CONTENIDO", datos_res))
    ataque_cibernetico_contenido = list(filter(lambda datos_res :  datos_res[28] == "ATAQUE CIBERNÉTICO CONTENIDO", datos_res))
    ataque_cibernetico_materializado = list(filter(lambda datos_res :  datos_res[28] == "ATAQUE CIBERNÉTICO MATERIALIZADO", datos_res))

    campamentos = list(filter(lambda datos_res: "INFRAESTRUCTURA" in datos_res[10], datos_res))
    campamentos = list(filter(lambda campamentos: "CRIMINAL" in campamentos[11], campamentos))
    campamentos = list(filter(lambda campamentos: "CAMPAMENTO(S)" in campamentos[12], campamentos)) 

    proselitismo = list(filter(lambda datos_res: "PROPAGANDA ALUSIVA GRUPOS ARMADOS" in datos_res[12] or "PANFLETO" in datos_res[12], datos_res))


    afectacion_oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "HIDROCARBUROS" in afectacion_oleoducto[11], afectacion_oleoducto))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "INFRAESTRUCTURA" in afectacion_oleoducto[10], afectacion_oleoducto))

    afectacion_oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "HIDROCARBUROS" in afectacion_oleoducto[11], afectacion_oleoducto))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "INFRAESTRUCTURA" in afectacion_oleoducto[10], afectacion_oleoducto))
    aboyadura = list(filter(lambda afectacion_oleoducto: "ABOLLADURA(A)" in afectacion_oleoducto[9], afectacion_oleoducto)) 

    afectacion_oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "HIDROCARBUROS" in afectacion_oleoducto[11], afectacion_oleoducto))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "INFRAESTRUCTURA" in afectacion_oleoducto[10], afectacion_oleoducto))
    apique = list(filter(lambda afectacion_oleoducto: "APIQUE" in afectacion_oleoducto[9], afectacion_oleoducto)) 

    afectacion_oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "HIDROCARBUROS" in afectacion_oleoducto[11], afectacion_oleoducto))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "INFRAESTRUCTURA" in afectacion_oleoducto[10], afectacion_oleoducto))
    destruido = list(filter(lambda afectacion_oleoducto: "DESTRUIDO(A)" in afectacion_oleoducto[9], afectacion_oleoducto))

    afectacion_oleoducto = list(filter(lambda datos_res: "OLEODUCTO" in datos_res[12], datos_res))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "HIDROCARBUROS" in afectacion_oleoducto[11], afectacion_oleoducto))
    afectacion_oleoducto = list(filter(lambda afectacion_oleoducto: "INFRAESTRUCTURA" in afectacion_oleoducto[10], afectacion_oleoducto))
    saboteado = list(filter(lambda afectacion_oleoducto: "SABOTEADO(A)" in afectacion_oleoducto[9], afectacion_oleoducto))

    estrategia_contrabando = list(filter(lambda datos_res:  datos_res[17] == "Contrabando" , datos_res))
    rme_contrabando = list(filter(lambda estrategia_contrabando: 'RME' in estrategia_contrabando[9] , estrategia_contrabando))


    ataque_fuerza = list(filter(lambda hechos :  hechos[0] == "ATAQUE FUERZA PUBLICA", hechos))
    neutralizacion_terrorista = list(filter(lambda hechos :  hechos[0] == "NEUTRALIZACIONES ACCIONES TERRORISTAS" , hechos))
    activacion_explosivos = list(filter(lambda hechos :  hechos[0] == "ACTIVACIÓN ARTEFACTO EXPLOSIVO" , hechos))
    activacion_zona_minada = list(filter(lambda hechos :  hechos[0] == "ACTIVACIÓN ZONA MINADA" , hechos))
    acto_terrorismo_ = list(filter(lambda hechos :  hechos[0] == "ACTO DE TERRORISMO" , hechos))
    acto_terrorismo_infraestrucra = list(filter(lambda hechos :  hechos[0] == "ACTO DE TERRORISMO EN CONTRA DE INFRAESTRUCTURA CRITICA" , hechos))
    acto_terrorismo_poblacion = list(filter(lambda hechos :  hechos[0] == "ACTO DE TERRORISMO EN CONTRA DE POBLACIÓN CIVIL" , hechos))
    acto_terrorismo_tropas = list(filter(lambda hechos :  hechos[0] == "ACTO DE TERRORISMO EN CONTRA DE PROPIAS TROPAS" , hechos))

    
    return[rme, presentacion_voluntaria, sometimientos, capturas, capturas_sin_delco, mdom, asesinados , heridos , armas_largas, armas_cortas, armas_acompaniamiento, municiones, combates_pos, comates_neg, combates_sin, combates, ataque_fuerza , neutralizacion_terrorista , hostigamientos , asonadas , ataque_con_drons , ae , map_anti_perosna , explosivos_kg , explosivos_m , explosivos_und , cordon , mecha , medios_lanzamientos , detonador_ini_electrico , detonador_electrico , artefactos_explosivos , cocaina , marihuana , pbc , basuco , herohina , drogas_sinteticas , lab_heroina , lab_cocaina , lab_pbc , semilleros , matas_coca , insumos_liquidos , insumos_solidos , combustibles_narcotrafico , cocaina_proceso , pbc_proceso , capturas_artemisa , plantulas_sembradas , madera , especies_aninales , capturas_mineria , rme_mineria , eiym , upm , maquinaria_pesada , excavadoras , retroexcavadoras , buldocer , dragas , maquinaria_amarilla , motores , combustibles_mineria , explosivos_mineria_kg , explosivos_mineria_m , explosivos_mineria_und , material_transporte , coltan , liberados, rescatados, pesos_colombianos, dolares, euros, muebles, inmuebles, vehiculos, afectacion_oleoducto , aboyadura , apique , destruido , saboteado , petroleo , piscina , valvula , refineria , depositos, campamentos, proselitismo, capturas_contrabando , rme_contrabando , combustibles_contrabando , gasolina_contrabando , acpm_contrabando , vehiculos_contrabando , insumos_liquidos_contrabando , insumos_liquidos_contrabando , animales_incautados_contrabando, activacion_explosivos, activacion_zona_minada, acto_terrorismo_ , acto_terrorismo_infraestrucra , acto_terrorismo_poblacion, acto_terrorismo_tropas, asesinados_fuera_combate_f, herido_fuera_combate_f, ataque_con_drons_f, derribado_con_drons_f, incidente_cibernetico_contenido, ataque_cibernetico_contenido, ataque_cibernetico_materializado, maquinaria_linea_amarilla, capturas_extorcion]

def funcion_mayor(numeros):

    altura = 0
    for numero in numeros:
        if numero > altura:
            altura = numero
    return altura

def conversor_de_cordenadas(numero, constante):
        numero = float(numero)
        numero = numero * constante
        coordenas_n_m, coordenada_n_g =    math.modf(numero)
        coordenas_n_m_c = coordenas_n_m*60
        coordenas_n_s_c, coordenada_n_m =    math.modf(coordenas_n_m_c)
        coordenas_n_s = coordenas_n_s_c*60
        coordenada_n = str(int(coordenada_n_g))+"° "+str(int(coordenada_n_m))+"'"+str(int(coordenas_n_s)) 
        return coordenada_n          
#funcion para dar formato a los numeros
def formato_numero(numero):
    if numero !=0:
        if numero < 0.5 and numero > -0.5 :
            numero = format(numero, '0,.3f')
            numero = numero.replace(',','.')
        else:
            numero = format(numero, '0,.0f')
            numero = numero.replace(',','.')
    else:
        numero = "-"
    return numero
def formato_numero_un_decimal(numero):
    if numero !=0:
        numero = format(numero, '0,.2f')
        numero = numero.replace(',','.')
    else:
        numero = "-"
    return numero
def formato_numero_decimal(numero):
    if numero !=0:
        if numero < 0.5 and numero > -0.5 :
            numero = format(numero, '0,.1f')
            numero = numero.replace(',','.')
        else:
            numero = format(numero, '0,.0f')
            numero = numero.replace(',','.')
    # else:
    #     numero = "-"
    return numero

#funcion para redondear numeros grandes
def round_grandes(numero):
    if numero !=0:
        numero =  numero / 1000
        numero = format(numero, '0,.1f')
        numero = numero.replace(',','.')
    else:
        numero = "-"
    return numero

def calculo(datos_res, parametro, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if parametro == dato[identificador]:
            numero =  numero + float(dato[identificador_suma])

    numero = formato_numero(numero)
    return numero
#calculo comparativo sin formatoto de numero
def calculo_comprativo_total_sin_formato_tipo(datos_res_ant, datos_res_act, parametro, identificador, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        if parametro == dato[identificador]:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        if parametro == dato[identificador]:
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)
    porcentaje = formato_numero_un_decimal(porcentaje)
    return [numero_ant, numero_act, porcentaje]
def calculo_comprativo_total_sin_formato_tipo_t(datos_res_ant, datos_res_act, parametro, parametro_2, parametro_3, identificador, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        if parametro == dato[identificador] or parametro_2 == dato[identificador] or parametro_3 == dato[identificador]:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        if parametro == dato[identificador] or parametro_2 == dato[identificador] or parametro_3 == dato[identificador]:
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)
    porcentaje = formato_numero_un_decimal(porcentaje)
    return [numero_ant, numero_act, porcentaje]

#calculo comparativo sin formatoto de numero
def calculo_comprativo_total_sin_formato_tipo_r(datos_res_ant, datos_res_act, parametro,parametro_dos, identificador,identificador_dos, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        if parametro == dato[identificador] and parametro_dos != dato[identificador_dos]:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        if parametro == dato[identificador] and parametro_dos != dato[identificador_dos]:
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)
    porcentaje = formato_numero_un_decimal(porcentaje)
    return [numero_ant, numero_act, porcentaje]

def calculo_por_lista(datos_res, parametro, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:

        for parametro_f in parametro:
            
            if dato[identificador] == parametro_f:
                numero =  numero + float(dato[identificador_suma])
                
    numero = formato_numero(numero)

    return numero
#calculo diferencia doble 
def calculo_doble(datos_res, parametro, parametro_dos, identificador, identificador_dos, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if parametro == dato[identificador] and parametro_dos != dato[identificador_dos]:
            numero =  numero + float(dato[identificador_suma])

    numero = formato_numero(numero)
    return numero
def porcentajes(numero_ant, numero_act, constante):
    porcentaje = 0
    if numero_ant >0:
        if numero_act >0:
            porcentaje = numero_act/numero_ant *100 -100
        else:
            porcentaje = -100
    elif numero_act > 0:
        porcentaje = 100
    else:
        porcentaje = 0

    porcentaje = porcentaje * constante
    return  porcentaje

#calculo comparativo
def calculo_comprativo_total(datos_res_ant, datos_res_act, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        
            numero_act =  numero_act + float(dato[identificador_suma])

    diferencia = (numero_act - numero_ant)*constante
    diferencia_2 = diferencia *constante
    porcentaje = porcentajes(numero_ant, numero_act, constante)
    numero_ant = formato_numero(numero_ant)
    numero_act = formato_numero(numero_act)
    porcentaje2 = formato_numero(porcentaje)
    diferencia_v = formato_numero(diferencia_2)
    
    return [numero_ant, numero_act, porcentaje2, diferencia_v,  diferencia, diferencia_2, porcentaje]

#calculo comparativo sin formatoto de numero
def calculo_comprativo_total_sin_formato(datos_res_ant, datos_res_act, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)

    return [numero_ant, numero_act, porcentaje]

# comparativo metas 
def comparativo_metas(datos_res_act, identificador_suma, constante, meta, conversion):
    numero_act = 0
    

    for dato in datos_res_act:
        
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(meta, numero_act, constante)

    if conversion == "Toneladas":
        meta = round_grandes(meta)
        numero_act = round_grandes(numero_act)
    else:
        meta = formato_numero(meta)
        numero_act = formato_numero(numero_act)
    porcentaje = formato_numero(porcentaje)
    
    return [numero_act, meta, porcentaje]
# comparativo metas 
def comparativo_redondo(datos_res_ant, datos_res_act, identificador_suma, constante,  conversion):
    numero_act = 0
    numero_ant = 0
    

    for dato in datos_res_act:
        
            numero_act =  numero_act + float(dato[identificador_suma])
            
    for dato_ant in datos_res_ant:
        
            numero_ant =  numero_ant + float(dato_ant[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)

    if conversion == "Toneladas":
        numero_ant = round_grandes(numero_ant)
        numero_act = round_grandes(numero_act)
    else:
        numero_ant = formato_numero(numero_ant)
        numero_act = formato_numero(numero_act)

    porcentaje = formato_numero(porcentaje)
    
    return [numero_ant, numero_act, porcentaje]
#funcion que suma resultados y da estilo a  numeros grandes
def resultados_tabla_mapa_indicador(datos_res_act, identificador_suma,  conversion):
    numero_act = 0

    for dato in datos_res_act:
        
            numero_act =  numero_act + float(dato[identificador_suma])

    if conversion == "Toneladas":
        numero_act = round_grandes(numero_act)
    else:
        numero_act = formato_numero(numero_act)

    
    return [numero_act]

#total
def calculo_total_sin_filtro(datos_res, identificador_suma):
    numero_ant = 0
    for dato in datos_res:
        
            numero_ant =  numero_ant + float(dato[identificador_suma])

    numero_ant = formato_numero(numero_ant)

    return numero_ant

def calculo_total_sin_filtro_b(datos_res, identificador_suma):
    numero_ant = 0
    for dato in datos_res:
        
            numero_ant =  numero_ant + float(dato[identificador_suma])

    

    return numero_ant

#calculo comparativo parametros
def calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_parametro, parametro, parametro_dos, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        if dato[id_parametro] == parametro or dato[id_parametro] == parametro_dos:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        if dato[id_parametro] == parametro or dato[id_parametro] == parametro_dos:
            numero_act =  numero_act + float(dato[identificador_suma])

    diferencia = numero_act - numero_ant 
    porcentaje = porcentajes(numero_ant, numero_act, constante)
    numero_ant = formato_numero(numero_ant)
    numero_act = formato_numero(numero_act)
    porcentaje = formato_numero(porcentaje)
    porcentaje_V = formato_numero(diferencia)
    
    return [numero_ant, numero_act, porcentaje, porcentaje_V, diferencia]

#calculo comparativo parametros
def calculo_comprativo_total_enemigo_tres(datos_res_ant, datos_res_act, id_parametro, parametro, parametro_dos, parametro_tres, identificador_suma, constante):
    numero_ant = 0
    numero_act = 0
    
    for dato in datos_res_ant:
        if dato[id_parametro] == parametro or dato[id_parametro] == parametro_dos or dato[id_parametro] == parametro_tres:
            numero_ant =  numero_ant + float(dato[identificador_suma])

    for dato in datos_res_act:
        if dato[id_parametro] == parametro or dato[id_parametro] == parametro_dos or dato[id_parametro] == parametro_tres:
            numero_act =  numero_act + float(dato[identificador_suma])

    porcentaje = porcentajes(numero_ant, numero_act, constante)
    numero_ant = formato_numero(numero_ant)
    numero_act = formato_numero(numero_act)
    porcentaje = formato_numero(porcentaje)
    
    return [numero_ant, numero_act, porcentaje]

def calculo_dos(datos_res, parametro, parametro_2, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if parametro == dato[identificador] or parametro_2 == dato[identificador] :
            numero =  numero + float(dato[identificador_suma])

    numero = formato_numero(numero)
    return numero

def calculo_tres(datos_res, parametro, parametro_2,parametro_3, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if parametro == dato[identificador] or parametro_2 == dato[identificador] or parametro_3 == dato[identificador] :
            numero =  numero + float(dato[identificador_suma])

    numero = formato_numero(numero)
    return numero

def calculo_tres_b(datos_res, parametro, parametro_2,parametro_3, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if parametro == dato[identificador] or parametro_2 == dato[identificador] or parametro_3 == dato[identificador] :
            numero =  numero + float(dato[identificador_suma])

    return numero
def calculo_total(datos_res, identificador, identificador_suma):
    numero = 0
    
    for dato in datos_res:
        if dato[1] != "TREJC":
            numero =  numero + float(dato[identificador_suma])

    numero = formato_numero(numero)
    return numero

  
       
def encabezado_coe_div_compa(pdf, fill, anio_act, anio_ant):

    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 9)

    pdf.cell(45,5,"DIVISIONES",1,0, 'C',fill)
    pdf.cell(20,10,str(anio_ant),1,0, 'C',fill)
    pdf.cell(20,10,str(anio_act),1,0, 'C',fill)
    pdf.cell(15,10,"%",1,0, 'C',fill)
    pdf.cell(41,5,"GAO-r",1,0, 'C',fill)
    pdf.cell(41,5,"GDO",1,0, 'C',fill)
    pdf.cell(41,5,"GAO-ELN",1,0, 'C',fill)
    pdf.cell(41,5,"GAO-CG",1,0, 'C',fill)
    pdf.cell(41,5,"NARCO.",1,0, 'C',fill)
    pdf.cell(41,5,"DELCO",1,0, 'C',fill)

    pdf.set_fill_color(227, 227, 211)
    pdf.set_text_color(0,0,0)

    pdf.ln(5)
    pdf.cell(-5)
    pdf.cell(45,5,"EVENTO",1,0, 'C',fill)
    
    pdf.cell(55)
    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

    pdf.cell(15,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(15,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(11,5,"%",1,0, 'C',fill)

#funcion que dibuja las gaos en cuadro del  boletin del coe 
def calculo_comparativo_enemigo(pdf, datos_res_ant,  datos_res_act, text, constante, id_enemigo, suma):
    pdf.set_fill_color(227, 227, 211)
    pdf.set_font('Calibri', 'B', 8)
    pdf.set_text_color(0,0,0)
    pdf.ln(5)
    pdf.cell(-5)
    pdf.cell(45,5,text,1,0, 'L',True)
    pdf.set_font('Calibri', 'B', 8)

    total = 0
    resultados  = calculo_comprativo_total(datos_res_ant, datos_res_act, suma, constante)

    pdf.cell(20,5,resultados[0],1,0, 'C',False)
    pdf.cell(20,5,resultados[1],1,0, 'C',False)
    pdf.cell(15,5,resultados[2],1,0, 'C',False)

    resultados = calculo_comprativo_total_enemigo_tres(datos_res_ant, datos_res_act, id_enemigo, "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", suma, constante)
    pdf.set_fill_color(211, 202, 200)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)

    resultados = calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_enemigo, "GDO","GDO", suma, constante)
    pdf.set_fill_color(61, 225, 166)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)

    resultados = calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_enemigo, "GAO ELN","GAO ELN", suma, constante)
    pdf.set_fill_color(255, 170, 170)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)

    resultados = calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_enemigo, "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", suma, constante)
    pdf.set_fill_color(174, 187, 174)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)
    
    resultados = calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_enemigo, "NARCOTRÁFICO","NARCOTRÁFICO", suma, constante)
    pdf.set_fill_color(255, 253, 201)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)
        
    resultados = calculo_comprativo_total_enemigo(datos_res_ant, datos_res_act, id_enemigo, "DELINCUENCIA","DELINCUENCIA", suma, constante)
    pdf.set_fill_color(240, 240, 240)
    pdf.cell(15,5,resultados[0],1,0, 'C',True)
    pdf.cell(15,5,resultados[1],1,0, 'C',True)
    pdf.cell(11,5,resultados[2],1,0, 'C',True)

def encabezado_comparativo(pdf, fill, fecha_anterior, fecha_actual, cell):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 10)

    y = pdf.get_y()

    variable =  cell + 75
    pdf.cell(variable)
    pdf.multi_cell(30, 5, str(fecha_anterior), 1, "C", fill)
    x = pdf.get_y()
    z = (x-y)
    pdf.ln(-z)

    variable = variable + 30
    pdf.cell(variable)
    pdf.multi_cell(30, 5, str(fecha_actual), 1, "C", fill)

    pdf.ln(-z)

    variable = variable + 30

  
    pdf.cell(variable)
    pdf.cell(25,z,"%",1,0, 'C',fill)

    variable = variable + 20

    pdf.ln(-0)

    pdf.cell(cell-5)
    
    # pdf.cell(60,10,"RESULTADOS",1,0, 'C',fill)
    pdf.multi_cell(80, z-5, str("RESULTADOS"), 1, "L", fill)


    pdf.set_fill_color(94,119,89)
    


    pdf.ln(-0)
    pdf.cell(cell-5)
    pdf.multi_cell(80, 5, str("EVENTO"), 1, "L", fill)
    pdf.set_fill_color(240, 240, 240)
    pdf.set_text_color(0,0,0)
    return z

def tabla_comparativa_linea(pdf, datos, datos_ant, id_enemigo, amenaza, suma, constante, cel, fill, texto, color, indicadores):

    datos_res = calculo_comprativo_total_enemigo(datos, datos_ant, id_enemigo, amenaza, amenaza, suma, constante)
    pdf.cell(cel+20+10)
    pdf.cell(65,5,texto,1,0, 'L',fill)
    pdf.cell(27.5,5,datos_res[0],1,0, 'C',fill)
    pdf.cell(27.5,5,datos_res[1],1,0, 'C',fill)
    if datos_res[4] < 0:
        pdf.set_text_color(125,0,0)
    else:
        pdf.set_text_color(0,0,0)

    pdf.cell(25,5,datos_res[3],1,0, 'C',fill)
    if datos_res[4] < 0:
        pdf.set_text_color(125,0,0)
    else:
        pdf.set_text_color(0,0,0)
    dato_res = str(datos_res[2])+" %"
    pdf.cell(25,5,str(dato_res),1,0, 'C',fill)
    if datos_res[4] < 0:
        pdf.set_fill_color(125,0,0)
        pdf.set_text_color(255,255,255)
        signo="-"
    elif datos_res[4] > 0:
        pdf.set_fill_color(20,62,52)
        pdf.set_text_color(255,255,255)
        signo="+"
    else:
        pdf.set_fill_color(255,192,0)
        pdf.set_text_color(255,255,255)
        signo="="
    pdf.cell(30,5,str(signo),1,0, 'C',fill)
    pdf.ln()
    pdf.set_fill_color(color[0],color[1],color[2])
    pdf.set_text_color(0,0,0)
    indicadores.append(datos_res[4])
    return indicadores

def tabla_comparativa_linea_2(pdf, datos, datos_ant, suma, constante, cel, fill, texto, color, indicadores):

    datos_res = calculo_comprativo_total(datos, datos_ant,  suma, constante)
    pdf.cell(cel+20+10)
    pdf.cell(65,5,texto,1,0, 'L',fill)
    pdf.cell(27.5,5,datos_res[0],1,0, 'C',fill)
    pdf.cell(27.5,5,datos_res[1],1,0, 'C',fill)
    #print(datos_res[1])
    if datos_res[5] < 0:
        pdf.set_text_color(125,0,0)
    else:
        pdf.set_text_color(0,0,0)
    pdf.cell(25,5,datos_res[3],1,0, 'C',fill)

    if texto != "COMBATES SIN RESULTADOS"  and texto != "CAPTURAS LOE AMAZONÍA" and texto != "MADERA INCAUTADA (M3)"and texto != "ANIMALES INCAUTADOS" and texto != "PLÁNTULAS SEMBRADAS":
        if datos_res[6] < 0:
            pdf.set_text_color(125,0,0)
        else:
            pdf.set_text_color(0,0,0)
        dato_por = str(datos_res[2])+" %"
        pdf.cell(25,5,str(dato_por),1,0, 'C',fill)
    
        if datos_res[4] < 0:
            pdf.set_fill_color(125,0,0)
            pdf.set_text_color(255,255,255)
            signo="-"
        elif datos_res[4] > 0:
            pdf.set_fill_color(20,62,52)
            pdf.set_text_color(255,255,255)
            signo="+"
        else:
            pdf.set_fill_color(255,192,0)
            pdf.set_text_color(255,255,255)
            signo="="
        pdf.cell(30,5,str(signo),1,0, 'C',fill)
        indicadores.append(datos_res[4])
    else:
        pdf.cell(25,5,"",1,0, 'C',fill)
        pdf.cell(30,5,"",1,0, 'C',fill)
        indicadores = indicadores

    pdf.ln()
    pdf.set_fill_color(color[0],color[1],color[2])
    pdf.set_text_color(0,0,0)
    
    return indicadores

#separado para el mapa
def sepador_mapa(pdf, fill, text):
    
    pdf.ln(5)
    pdf.cell(176)
    pdf.set_text_color(0,0,0)
    pdf.cell(165,5,text,1,0, 'C',fill)

    #separado para el mapa
def sepador_mapa_dos(pdf, fill, text, cell, ancho):
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 9)
    #pdf.ln(5)
    pdf.cell(cell)
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(255,255,255)
    pdf.cell(ancho,5,text,1,0, 'C',fill)
    #pdf.set_fill_color(240,240,240)
def validar_indicador_unidad(json, json_ruta, unidad):
        obj_2 = []
        with open(json_ruta, "rb") as read_file:
            data = dict(json.load(read_file))

            for x in data:
                for y in data[x]:
                    if y['UNIDAD'] == unidad:
                        obj_2.append(y['APLICA'])
        return obj_2
def encabezado_comparativo_mapa(pdf, fill, anio_act, anio_ant, cel):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(255,255,255)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 9)

    pdf.cell(cel)
    pdf.cell(10,5,"No.",1,0, 'C',fill)
    pdf.cell(20,5,"AMENAZA",1,0, 'C',fill)
    pdf.cell(65,5,"EVENTO",1,0, 'C',fill)
    pdf.cell(27.5,5,str(anio_ant),1,0, 'C',fill)
    pdf.cell(27.5,5,str(anio_act),1,0, 'C',fill)
    pdf.cell(25,5,"DIFERENCIA",1,0, 'C',fill)
    pdf.cell(25,5,"PORCENTAJE",1,0, 'C',fill)
    pdf.cell(30,5,"SEMAFORIZACIÓN",1,0, 'C',fill)

    pdf.set_fill_color(227, 227, 211)
    pdf.set_text_color(0,0,0)

    
def encabezado_comparativo_enemigo_dinamico(pdf, fill, datos, datos_ant, amenaza, cel, color, suma, constante, id_enemigo, texto, indicadores, objectivos, rango, numeros):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(color[0],color[1],color[2])
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 8)

    i = rango[0]
    numero = 0
    texto_evaluado = []
    if objectivos !=[]:
        while i <= rango[1]:
            if objectivos[i] == "SI":
                indicadores = tabla_comparativa_linea(pdf, datos[numero], datos_ant[numero], id_enemigo, amenaza[0], suma, constante, cel, fill,texto[numero] , color, indicadores)
                texto_evaluado.append("SI")
            numero +=1
            i += 1
            
    else:
        for y in texto:
            if objectivos[i] == "SI":
                indicadores = tabla_comparativa_linea(pdf, datos[numero], datos_ant[numero], id_enemigo, amenaza[0], suma, constante, cel, fill,texto[numero] , color, indicadores)
                texto_evaluado.append("SI")
            numero +=1
            
    altura =  len(texto_evaluado)
    altura_2 =  len(texto_evaluado)

    if altura >0:
        altura =  altura *5
        
        pdf.ln(-altura)
        pdf.cell(cel+10)
        pdf.cell(20,altura,str(amenaza[1]),1,0, 'C',fill)
        pdf.ln()

        pdf.ln(-altura)

        for x in texto_evaluado:
            numeros = numeros +1
            pdf.cell(cel)
            pdf.cell(10,5,str(numeros),1,0, 'C',fill)
            pdf.ln()

    
    return [indicadores, numeros]

    
def encabezado_comparativo_enemigo_dinamico_2(pdf, fill, datos, datos_ant, cel, color, suma, constante, texto, indicadores, objectivos, rango, numeros):


    numero = 0

    i = rango[0]
    numero = 0
    textos_len =[]
    if objectivos !=[]:
        while i <= rango[1]:
            if objectivos[i] == "SI":
                pdf.set_line_width(0.1)

                pdf.set_fill_color(color[0],color[1],color[2])
                pdf.set_draw_color(0, 0, 0)
                pdf.set_text_color(0,0,0)
                pdf.set_font('Arial', 'B', 8)
                
                if texto[numero] != "COMBATES SIN RESULTADOS" and texto[numero] != "CAPTURAS LOE AMAZONÍA" and texto[numero] != "MADERA INCAUTADA (M3)"and texto[numero] != "ANIMALES INCAUTADOS" and texto[numero] != "PLÁNTULAS SEMBRADAS":
                    indicadores = tabla_comparativa_linea_2(pdf, datos[numero], datos_ant[numero], suma[numero], constante[numero], cel, fill,texto[numero] , color, indicadores)
    

                else:
                    tabla_comparativa_linea_2(pdf, datos[numero], datos_ant[numero], suma[numero], constante[numero], cel, fill,texto[numero] , color, indicadores)

                
                textos_len.append("SI")
                
            numero +=1
            i += 1
            

    else:
        for x in texto:
            pdf.set_line_width(0.1)

            pdf.set_fill_color(color[0],color[1],color[2])
            pdf.set_draw_color(0, 0, 0)
            pdf.set_text_color(0,0,0)
            pdf.set_font('Arial', 'B', 9)
            if texto[numero] != "COMBATES SIN RESULTADOS" and texto[numero] != "CAPTURAS LOE AMAZONÍA" and texto[numero] != "MADERA INCAUTADA (M3)"and texto[numero] != "ANIMALES INCAUTADOS" and texto[numero] != "PLÁNTULAS SEMBRADAS":
                indicadores = tabla_comparativa_linea_2(pdf, datos[numero], datos_ant[numero], suma[numero], constante[numero], cel, fill,texto[numero] , color, indicadores)


            else:
                tabla_comparativa_linea_2(pdf, datos[numero], datos_ant[numero], suma[numero], constante[numero], cel, fill,texto[numero] , color, indicadores)


            numero = numero +1
            textos_len.append("SI")

    altura = len(textos_len)
    altura = altura * 5

    pdf.ln(-altura)
    pdf.cell(cel+10)
    pdf.cell(20,altura,str("TOTAL"),1,0, 'C',fill)
    pdf.ln()


    pdf.ln(-altura)

    for x in textos_len:
        numeros = numeros +1
        pdf.cell(cel)
        pdf.cell(10,5,str(numeros),1,0, 'C',fill)
        pdf.ln()

    
    
    return [indicadores, numeros]






def claculo_mapa(pdf, datos_res_ant,  datos_res_act, text, constante, id_enemigo, suma):
    pdf.ln(5)
    pdf.cell(176)
    pdf.set_text_color(0,0,0)
    pdf.cell(60,5,text,1,0, 'C',True)

    resultados  = calculo_comprativo_total(datos_res_ant, datos_res_act, suma, constante)
    pdf.cell(40,5,resultados[0],1,0, 'C',False)
    pdf.cell(40,5,resultados[1],1,0, 'C',False)
    pdf.cell(25,5,resultados[2],1,0, 'C',False)
    
def claculo_mapa_dos(pdf, datos_res_ant,  datos_res_act, text, constante, id_enemigo, suma, cell):
    pdf.ln(5)
    pdf.cell(cell)
    pdf.set_text_color(0,0,0)
    pdf.cell(80,5,text,1,0, 'L',True)

    resultados  = calculo_comprativo_total(datos_res_ant, datos_res_act, suma, constante)
    pdf.cell(30,5,resultados[0],1,0, 'C',False)
    pdf.cell(30,5,resultados[1],1,0, 'C',False)
    pdf.cell(25,5,resultados[2],1,0, 'C',False)
    
def claculo_maquinaria_amarialla_mapa_dos( datos_res_ant,  datos_res_act,  constante,  suma):

    maquinari_amarialla_anterior= 0
    maquinari_amarialla_actual= 0
    res = 0
    res = calculo_total_sin_filtro_b(datos_res_ant[0], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res
    res = calculo_total_sin_filtro_b(datos_res_ant[1], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res


    res = 0
    res = calculo_total_sin_filtro_b(datos_res_act[0], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[1], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res



    # resultados  = calculo_comprativo_total(maquinari_amarialla_anterior, maquinari_amarialla_actual, suma, constante)
    resultados = porcentajes(maquinari_amarialla_anterior, maquinari_amarialla_actual, constante)

    maquinari_amarialla_anterior = formato_numero(maquinari_amarialla_anterior)
    maquinari_amarialla_actual = formato_numero(maquinari_amarialla_actual)
    # resultados = formato_numero(resultados)

    return[maquinari_amarialla_anterior, maquinari_amarialla_actual, resultados]


def claculo_maquinaria_amarialla_mapa(pdf,  datos_res_act, suma):

    maquinari_amarialla_actual= 0
    res = 0


    res = 0
    res = calculo_total_sin_filtro_b(datos_res_act[0], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[1], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res


    maquinari_amarialla_actual = formato_numero(maquinari_amarialla_actual)
    # resultados = formato_numero(resultados)

    return maquinari_amarialla_actual


def celda_afectaciones(pdf, ln, cel,text,rango, id):
    pdf.ln(ln)
    pdf.cell(cel)

    numero = 2
    for rang in range(rango) :
        pdf.cell(text[0][rang],text[1][rang],text[numero],1,0, text[id[0]][rang],text[id[1]][rang])
        numero = numero +1
               
def suma_h_a(resultado_asesinados, resultado_heridos ):
    if resultado_asesinados == "-":
        res_asesinado = 0
    else:
        res_asesinado = resultado_asesinados

    if resultado_heridos == "-":
        res_herido = 0
    else:
        res_herido = resultado_heridos

    total = float(res_herido) + float(res_asesinado)
    total = formato_numero(total)
    return total
def suma_h_a_sin_formato(resultado_asesinados, resultado_heridos ):
    if resultado_asesinados == "-":
        res_asesinado = 0
    else:
        res_asesinado = resultado_asesinados

    if resultado_heridos == "-":
        res_herido = 0
    else:
        res_herido = resultado_heridos

    total = float(res_herido) + float(res_asesinado)

    return total

#cuadro de heridos y asesinados por grados y enemigos
def calcular_comparativo_res(datos, text, indicador, suma, constante):
    asesinados_oficiales = calculo_comprativo_total_sin_formato_tipo(datos[0], datos[1], text, indicador, suma, constante)
    heridos_oficiales = calculo_comprativo_total_sin_formato_tipo(datos[2], datos[3], text, indicador, suma, constante)

    total_ant_ofi = suma_h_a_sin_formato(asesinados_oficiales[0], heridos_oficiales[0])
    total_act_ofi = suma_h_a_sin_formato(asesinados_oficiales[1], heridos_oficiales[1])
    porcentajes_total_ofi =  porcentajes(total_ant_ofi, total_act_ofi, -1)
     
    total_ant_ofi =  formato_numero(total_ant_ofi)
    total_act_ofi =  formato_numero(total_act_ofi)
    porcentajes_total_ofi =  formato_numero_un_decimal(porcentajes_total_ofi)

    return [asesinados_oficiales[0], asesinados_oficiales[1],asesinados_oficiales[2], heridos_oficiales[0], heridos_oficiales[1], heridos_oficiales[2],total_ant_ofi,total_act_ofi,porcentajes_total_ofi]

def calcular_comparativo_res_r(datos, text, text_1, indicador, indicador_1, suma, constante):
    asesinados_oficiales = calculo_comprativo_total_sin_formato_tipo_r(datos[0], datos[1], text, text_1, indicador, indicador_1, suma, constante)
    heridos_oficiales = calculo_comprativo_total_sin_formato_tipo_r(datos[2], datos[3], text, text_1, indicador, indicador_1, suma, constante)

    total_ant_ofi = suma_h_a_sin_formato(asesinados_oficiales[0], heridos_oficiales[0])
    total_act_ofi = suma_h_a_sin_formato(asesinados_oficiales[1], heridos_oficiales[1])
    porcentajes_total_ofi =  porcentajes(total_ant_ofi, total_act_ofi, -1)
     
    total_ant_ofi =  formato_numero(total_ant_ofi)
    total_act_ofi =  formato_numero(total_act_ofi)
    porcentajes_total_ofi =  formato_numero_un_decimal(porcentajes_total_ofi)

    return [asesinados_oficiales[0], asesinados_oficiales[1],asesinados_oficiales[2], heridos_oficiales[0], heridos_oficiales[1], heridos_oficiales[2],total_ant_ofi,total_act_ofi,porcentajes_total_ofi]
def calcular_comparativo_res_t(datos, text, text_1, text_2, indicador, suma, constante):
    asesinados_oficiales = calculo_comprativo_total_sin_formato_tipo_t(datos[0], datos[1], text, text_1, text_2, indicador, suma, constante)
    heridos_oficiales = calculo_comprativo_total_sin_formato_tipo_t(datos[2], datos[3], text, text_1, text_2, indicador, suma, constante)

    total_ant_ofi = suma_h_a_sin_formato(asesinados_oficiales[0], heridos_oficiales[0])
    total_act_ofi = suma_h_a_sin_formato(asesinados_oficiales[1], heridos_oficiales[1])
    porcentajes_total_ofi =  porcentajes(total_ant_ofi, total_act_ofi, -1)
     
    total_ant_ofi =  formato_numero(total_ant_ofi)
    total_act_ofi =  formato_numero(total_act_ofi)
    porcentajes_total_ofi =  formato_numero_un_decimal(porcentajes_total_ofi)

    return [asesinados_oficiales[0], asesinados_oficiales[1],asesinados_oficiales[2], heridos_oficiales[0], heridos_oficiales[1], heridos_oficiales[2],total_ant_ofi,total_act_ofi,porcentajes_total_ofi]
def cuadro_heridos_asesinados_comparativos(pdf, datos, filtro):

    #-----------------------------------//----------------------------
    pdf.set_line_width(0.1)
    pdf.set_fill_color(94, 119, 88)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    pdf.ln(30)
    pdf.cell(-5)
    pdf.cell(169.5,10,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(-5)
    x = (66,34.5,34.5,34.5)
    y= (10,5,5,5)
    rango =4
    a = ("C","C","C","C") 
    fill = ( True, True, True, True)
    text = (x, y, "GRADO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (6,7)
    
    celda_afectaciones(pdf, 10, -5, text, rango, id)
    pdf.set_fill_color(208, 208, 182)
    pdf.set_text_color(0,0,0)
    pdf.ln()
    pdf.cell(61)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)

    #-----------------------------------//----------------------------
    # pdf.ln()
    pdf.set_font('Arial', 'B', 10)

    x = (66,11,11,12.5,11,11,12.5,11,11,12.5)
    y= (10,10,10,10,10,10,10,10,10,10)
    rango =10
    a = ("L","C","C","C","C","C","C","C","C","C") 
    fill = (False, False, False, True, False, False, True, False, False, True)
    id = (12,13)

    datos_oficial = calcular_comparativo_res(datos, "OFICIALES", 11, 18, -1)
    text = (x, y, "OFICIALES", str(formato_numero(datos_oficial[0])), str(formato_numero(datos_oficial[1])), str(datos_oficial[2]), str(formato_numero(datos_oficial[3])), str(formato_numero(datos_oficial[4])), str(datos_oficial[5]), str(datos_oficial[6]), str(datos_oficial[7]), str(datos_oficial[8]) , a, fill )
    
    celda_afectaciones(pdf, 5, -5, text, rango, id)

    datos_subocial = calcular_comparativo_res(datos, "SUBOFICIALES", 11, 18, -1)
    text = (x, y, "SUBOFICIALES", str(formato_numero(datos_subocial[0])), str(formato_numero(datos_subocial[1])), str(datos_subocial[2]), str(formato_numero(datos_subocial[3])), str(formato_numero(datos_subocial[4])), str(datos_subocial[5]), str(datos_subocial[6]), str(datos_subocial[7]), str(datos_subocial[8]) , a, fill )
    
    celda_afectaciones(pdf, 10, -5, text, rango, id)


    datos_slp = calcular_comparativo_res(datos, "SLP", 19, 18, -1)
    text = (x, y, "SOLDADOS PROFESIONALES", str(formato_numero(datos_slp[0])), str(formato_numero(datos_slp[1])), str(datos_slp[2]), str(formato_numero(datos_slp[3])), str(formato_numero(datos_slp[4])), str(datos_slp[5]), str(datos_slp[6]), str(datos_slp[7]), str(datos_slp[8]) , a, fill )
    
    celda_afectaciones(pdf, 10, -5, text, rango, id)

    datos_slp_18 = calcular_comparativo_res_r(datos, "SOLDADOS", "SLP", 11, 19, 18, -1)
    text = (x, y, "SOLDADOS SL18", str(formato_numero(datos_slp_18[0])), str(formato_numero(datos_slp_18[1])), str(datos_slp_18[2]), str(formato_numero(datos_slp_18[3])), str(formato_numero(datos_slp_18[4])), str(datos_slp_18[5]), str(datos_slp_18[6]), str(datos_slp_18[7]), str(datos_slp_18[8]) , a, fill )
    celda_afectaciones(pdf, 10, -5, text, rango, id)

    total_asesinados_2022 = datos_oficial[0] + datos_subocial[0] + datos_slp[0] + datos_slp_18[0]
    total_asesinados_2023 = datos_oficial[1] + datos_subocial[1] + datos_slp[1] + datos_slp_18[1]
    total_porcentaje_asinados = porcentajes(total_asesinados_2022, total_asesinados_2023,-1)

    total_heridos_2022 = datos_oficial[3] + datos_subocial[3] + datos_slp[3] + datos_slp_18[3]
    total_heridos_2023 = datos_oficial[4] + datos_subocial[4] + datos_slp[4] + datos_slp_18[4]
    total_porcentaje_heridos = porcentajes(total_heridos_2022, total_heridos_2023,-1)

    total_2022 = total_asesinados_2022 + total_heridos_2022
    total_2023 = total_asesinados_2023 + total_heridos_2023
    total_porcentaje = porcentajes(total_2022, total_2023,-1)

    pdf.set_line_width(0.1)
    pdf.set_fill_color(94, 119, 88)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    fill = (True, True, True, True, True, True, True, True, True, True)

    text = (x, y, "TOTAL", str(formato_numero(total_asesinados_2022)), str(formato_numero(total_asesinados_2023)), str(formato_numero_un_decimal(total_porcentaje_asinados)), str(formato_numero(total_heridos_2022)), str(formato_numero(total_heridos_2023)), str(formato_numero_un_decimal(total_porcentaje_heridos)), str(formato_numero(total_2022)), str(formato_numero(total_2023)), str(formato_numero_un_decimal(total_porcentaje)) , a, fill )
    celda_afectaciones(pdf, 10, -5, text, rango, id)



    pdf.ln(-60)
    pdf.cell(172)
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(167.5,10,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_font('Arial', 'B', 10)

    
    x = (64,34.5,34.5,34.5)
    y= (10,5,5,5)
    rango =4
    a = ("c","C","C","C") 
    fill = ( True, True, True, True)
    text = (x, y,"ENEMIGO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (6,7)

    celda_afectaciones(pdf, 10, 172, text, rango, id)

    pdf.set_fill_color(208, 208, 182)
    pdf.set_text_color(0,0,0)
    pdf.ln()
    pdf.cell(236)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)

    pdf.cell(11,5,str(datos[4]),1,0, 'C',True)
    pdf.cell(11,5,str(datos[5]),1,0, 'C',True)
    pdf.cell(12.5,5,str("%"),1,0, 'C',True)
    pdf.ln(-5)
    a = ("L","C","C","C") 
    fill = (False, False, False, False)
    numero = 0


    x = (64,11,11,12.5,11,11,12.5,11,11,12.5)
    y= (10,10,10,10,10,10,10,10,10,10)
    rango =10
    a = ("L","C","C","C","C","C","C","C","C","C") 
    fill = (False, False, False, True, False, False, True, False, False, True)
    id = (12,13)

    datos_eln = calcular_comparativo_res(datos, "GAO ELN", 7, 18, -1)

    if datos_eln[6] != "-" or datos_eln[7] != "-":
        text = (x, y, "GAO-ELN", str(formato_numero(datos_eln[0])), str(formato_numero(datos_eln[1])), str(datos_eln[2]), str(formato_numero(datos_eln[3])), str(formato_numero(datos_eln[4])), str(datos_eln[5]), str(datos_eln[6]), str(datos_eln[7]), str(datos_eln[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)

    datos_gaor = calcular_comparativo_res_t(datos, "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", 7, 18, -1)
    if datos_gaor[6] != "-" or datos_gaor[7] != "-":
        text = (x, y, "GAO-r", str(formato_numero(datos_gaor[0])), str(formato_numero(datos_gaor[1])), str(datos_gaor[2]), str(formato_numero(datos_gaor[3])), str(formato_numero(datos_gaor[4])), str(datos_gaor[5]), str(datos_gaor[6]), str(datos_gaor[7]), str(datos_gaor[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)

    datos_cg = calcular_comparativo_res(datos, "GAO CLAN DEL GOLFO", 7, 18, -1)

    if datos_cg[6] != "-" or datos_cg[7] != "-":
        text = (x, y, "GAO-CG", str(formato_numero(datos_cg[0])), str(formato_numero(datos_cg[1])), str(datos_cg[2]), str(formato_numero(datos_cg[3])), str(formato_numero(datos_cg[4])), str(datos_cg[5]), str(datos_cg[6]), str(datos_cg[7]), str(datos_cg[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)


    gdo = calcular_comparativo_res(datos, "GDO", 7, 18, -1)
    if gdo[6] != "-" or gdo[7] != "-":
        text = (x, y, "GDO", str(formato_numero(gdo[0])), str(formato_numero(gdo[1])), str(gdo[2]), str(formato_numero(gdo[3])), str(formato_numero(gdo[4])), str(gdo[5]), str(gdo[6]), str(gdo[7]), str(gdo[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                

    gao_cap = calcular_comparativo_res(datos, "GAO CAPARROS", 7, 18, -1)
    if gao_cap[6] != "-" or gao_cap[7] != "-":
        text = (x, y, "GAO CAPARROS", str(formato_numero(gao_cap[0])), str(formato_numero(gao_cap[1])), str(gao_cap[2]), str(formato_numero(gao_cap[3])), str(formato_numero(gao_cap[4])), str(gao_cap[5]), str(gao_cap[6]), str(gao_cap[7]), str(gao_cap[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                        
    gao_pel = calcular_comparativo_res(datos, "GAO PELUSOS", 7, 18, -1)
    if gao_pel[6] != "-" or gao_pel[7] != "-":
        text = (x, y, "GAO PELUSOS", str(formato_numero(gao_pel[0])), str(formato_numero(gao_pel[1])), str(gao_pel[2]), str(formato_numero(gao_pel[3])), str(formato_numero(gao_pel[4])), str(gao_pel[5]), str(gao_pel[6]), str(gao_pel[7]), str(gao_pel[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                                
    narcotrafico = calcular_comparativo_res(datos, "NARCOTRÁFICO", 7, 18, -1)
    if narcotrafico[6] != "-" or narcotrafico[7] != "-":
        text = (x, y, "NARCOTRÁFICO", str(formato_numero(narcotrafico[0])), str(formato_numero(narcotrafico[1])), str(narcotrafico[2]), str(formato_numero(narcotrafico[3])), str(formato_numero(narcotrafico[4])), str(narcotrafico[5]), str(narcotrafico[6]), str(narcotrafico[7]), str(narcotrafico[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
    

    delco = calcular_comparativo_res(datos, "DELINCUENCIA", 7, 18, -1)
    if delco[6] != "-" or delco[7] != "-":
        text = (x, y, "DELINCUENCIA", str(formato_numero(delco[0])), str(formato_numero(delco[1])), str(delco[2]), str(formato_numero(delco[3])), str(formato_numero(delco[4])), str(delco[5]), str(delco[6]), str(delco[7]), str(delco[8]) , a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)




    total_asesinados_2022 = datos_eln[0] + datos_gaor[0] + datos_cg[0] + gdo[0] + gao_cap[0] + gao_pel[0] + narcotrafico[0] + delco[0]
    total_asesinados_2023 = datos_eln[1] + datos_gaor[1] + datos_cg[1] + gdo[1] + gao_cap[1] + gao_pel[1] + narcotrafico[1] + delco[1]
    total_porcentaje_asinados = porcentajes(total_asesinados_2022, total_asesinados_2023,-1)

    total_heridos_2022 = datos_eln[3] + datos_gaor[3] + datos_cg[3] + gdo[3] + gao_cap[3] + gao_pel[3] + narcotrafico[3] + delco[3]
    total_heridos_2023 = datos_eln[4] + datos_gaor[4] + datos_cg[4] + gdo[4] + gao_cap[4] + gao_pel[4] + narcotrafico[4] + delco[4]
    total_porcentaje_heridos = porcentajes(total_heridos_2022, total_heridos_2023,-1)

    total_2022 = total_asesinados_2022 + total_heridos_2022
    total_2023 = total_asesinados_2023 + total_heridos_2023
    total_porcentaje = porcentajes(total_2022, total_2023,-1)

    pdf.set_line_width(0.1)
    pdf.set_fill_color(94, 119, 88)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    fill = (True, True, True, True, True, True, True, True, True, True)

    text = (x, y, "TOTAL", str(formato_numero(total_asesinados_2022)), str(formato_numero(total_asesinados_2023)), str(formato_numero_un_decimal(total_porcentaje_asinados)), str(formato_numero(total_heridos_2022)), str(formato_numero(total_heridos_2023)), str(formato_numero_un_decimal(total_porcentaje_heridos)), str(formato_numero(total_2022)), str(formato_numero(total_2023)), str(formato_numero_un_decimal(total_porcentaje)) , a, fill )
    celda_afectaciones(pdf, 10, 172, text, rango, id)

#cuadro de heridos y asesinados por grados y enemigos

def cuadro_heridos_asesinados(pdf, asesinados, heridos):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    pdf.ln(30)
    pdf.cell(5)
    pdf.cell(163.5,10,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_fill_color(180, 180, 180)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 12)

    x = (10,68,28.5,28.5,28.5)
    y= (10,10,10,10,10)
    rango =5
    a = ("C","C","C","C","C") 
    fill = (True, True, True, True, True)
    text = (x, y, "No.","GRADO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (7,8)

    celda_afectaciones(pdf, 10, 5, text, rango, id)

    a = ("C","L","C","C","C") 
    fill = (False, False, False, False, False)

    res_asesinados = calculo(asesinados, "OFICIALES", 11, 18)
    res_heridos = calculo(heridos, "OFICIALES", 11, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "1","OFICIALES", str(res_asesinados), str(res_heridos), str(total), a, fill )

    celda_afectaciones(pdf, 10, 5, text, rango, id)

    res_asesinados = calculo(asesinados, "SUBOFICIALES", 11, 18)
    res_heridos = calculo(heridos, "SUBOFICIALES", 11, 18)
    total = suma_h_a(res_asesinados, res_heridos)


    text = (x, y, "2","SUBOFICIALES", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 10, 5, text, rango, id)


    res_asesinados = calculo(asesinados, "SLP", 19, 18)
    res_heridos = calculo(heridos, "SLP", 19, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "3","SOLDADOS PROFESIONALES", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 10, 5, text, rango, id)


    res_asesinados = calculo_doble(asesinados, "SOLDADOS", "SLP", 11, 19, 18)
    res_heridos = calculo_doble(heridos, "SOLDADOS", "SLP", 11, 19, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "4","SOLDADOS SL18", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 10, 5, text, rango, id)

    rango =4
    pdf.set_fill_color(193, 30, 38)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    x = (78,28.5,28.5,28.5)
    y= (10,10,10,10)
    resultado_asesinados = calculo_total_sin_filtro(asesinados, 18)
    resultado_heridos = calculo_total_sin_filtro(heridos, 18)
    a = ("C","C","C","C") 
    fill = (True, True, True, True)
    id = (6,7)

    total = suma_h_a(resultado_asesinados, resultado_heridos)

    text = (x, y, "TOTAL", str(resultado_asesinados), str(resultado_heridos), str(total), a, fill  )
    celda_afectaciones(pdf, 10, 5, text, rango, id)

    
    pdf.ln(-60)
    pdf.cell(172)
    pdf.cell(163.5,10,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_fill_color(180, 180, 180)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 12)

    
    x = (10,68,28.5,28.5,28.5)
    y= (10,10,10,10,10)
    rango =5
    a = ("C","C","C","C","C") 
    fill = (True, True, True, True, True)
    text = (x, y, "No.","ENEMIGO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (7,8)

    celda_afectaciones(pdf, 10, 172, text, rango, id)

    a = ("C","L","C","C","C") 
    fill = (False, False, False, False, False)
    numero = 0

    res_asesinados = calculo(asesinados, "GAO ELN", 7, 18)
    res_heridos = calculo(heridos, "GAO ELN", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-ELN", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)

    res_asesinados = calculo_tres(asesinados,"GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", 7, 18)
    res_heridos = calculo_tres(heridos,"GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-r", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)

    res_asesinados = calculo(asesinados, "GAO CLAN DEL GOLFO", 7, 18)
    res_heridos = calculo(heridos, "GAO CLAN DEL GOLFO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-CG", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
        
    res_asesinados = calculo(asesinados, "GDO", 7, 18)
    res_heridos = calculo(heridos, "GDO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GDO", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                
    res_asesinados = calculo(asesinados, "GAO CAPARROS", 7, 18)
    res_heridos = calculo(heridos, "GAO CAPARROS", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-CAP", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                        
    res_asesinados = calculo(asesinados, "GAO PELUSOS", 7, 18)
    res_heridos = calculo(heridos, "GAO PELUSOS", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-PEL", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
                                
    res_asesinados = calculo(asesinados, "NARCOTRÁFICO", 7, 18)
    res_heridos = calculo(heridos, "NARCOTRÁFICO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"NARCOTRÁFICO", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)
    
    res_asesinados = calculo(asesinados, "DELINCUENCIA", 7, 18)
    res_heridos = calculo(heridos, "DELINCUENCIA", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"DELINCUENCIA", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 10, 172, text, rango, id)

    rango =4
    pdf.set_fill_color(193, 30, 38)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    x = (78,28.5,28.5,28.5)
    y= (10,10,10,10)
    resultado_asesinados = calculo_total_sin_filtro(asesinados, 18)
    resultado_heridos = calculo_total_sin_filtro(heridos, 18)
    a = ("C","C","C","C") 
    fill = (True, True, True, True)
    id = (6,7)

    total = suma_h_a(resultado_asesinados, resultado_heridos)

    text = (x, y, "TOTAL", str(resultado_asesinados), str(resultado_heridos), str(total), a, fill  )
    celda_afectaciones(pdf, 10, 172, text, rango, id)

   #cuadros de heridos y asesinados por grados y enemigos

def cuadros_heridos_asesinados(pdf, asesinados, heridos):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    pdf.ln(20)
    pdf.cell(5)
    pdf.cell(163.5,8,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_fill_color(208,208,182)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 11)

    x = (10,68,28.5,28.5,28.5)
    y= (5,5,5,5,5)
    rango =5
    a = ("C","C","C","C","C") 
    fill = (True, True, True, True, True)
    text = (x, y, "No.","GRADO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (7,8)
    pdf.set_font('Arial', 'B', 12)
    celda_afectaciones(pdf, 8, 5, text, rango, id)
    pdf.set_font('Arial', 'B', 11)
    a = ("C","L","C","C","C") 
    fill = (False, False, False, False, False)

    res_asesinados = calculo(asesinados, "OFICIALES", 11, 18)
    res_heridos = calculo(heridos, "OFICIALES", 11, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "1","OFICIALES", str(res_asesinados), str(res_heridos), str(total), a, fill )

    celda_afectaciones(pdf, 5, 5, text, rango, id)

    res_asesinados = calculo(asesinados, "SUBOFICIALES", 11, 18)
    res_heridos = calculo(heridos, "SUBOFICIALES", 11, 18)
    total = suma_h_a(res_asesinados, res_heridos)


    text = (x, y, "2","SUBOFICIALES", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 5, 5, text, rango, id)


    res_asesinados = calculo(asesinados, "SLP", 19, 18)
    res_heridos = calculo(heridos, "SLP", 19, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "3","SOLDADOS PROFESIONALES", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 5, 5, text, rango, id)


    res_asesinados = calculo_doble(asesinados, "SOLDADOS", "SLP", 11, 19, 18)
    res_heridos = calculo_doble(heridos, "SOLDADOS", "SLP", 11, 19, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    text = (x, y, "4","SOLDADOS SL18", str(res_asesinados), str(res_heridos), str(total), a, fill )
    celda_afectaciones(pdf, 5, 5, text, rango, id)

    rango =4
    pdf.set_fill_color(94,119,89)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    x = (78,28.5,28.5,28.5)
    y= (7,7,7,7)
    resultado_asesinados = calculo_total_sin_filtro(asesinados, 18)
    resultado_heridos = calculo_total_sin_filtro(heridos, 18)
    a = ("C","C","C","C") 
    fill = (True, True, True, True)
    id = (6,7)

    total = suma_h_a(resultado_asesinados, resultado_heridos)

    text = (x, y, "TOTAL", str(resultado_asesinados), str(resultado_heridos), str(total), a, fill  )
    celda_afectaciones(pdf, 5, 5, text, rango, id)
    
    pdf.set_font('Arial', 'B', 14)
    
    pdf.ln(-33)
    pdf.cell(172)
    pdf.cell(163.5,7,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_fill_color(208,208,182)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 11)

    
    x = (10,68,28.5,28.5,28.5)
    y= (5,5,5,5,5)
    rango =5
    a = ("C","C","C","C","C") 
    fill = (True, True, True, True, True)
    text = (x, y, "No.","ENEMIGO", "ASESINADOS", "HERIDOS", "TOTAL", a, fill )
    id = (7,8)
    pdf.set_font('Arial', 'B', 12)
    celda_afectaciones(pdf, 7, 172, text, rango, id)
    pdf.set_font('Arial', 'B', 11)
    a = ("C","L","C","C","C") 
    fill = (False, False, False, False, False)
    numero = 0

    res_asesinados = calculo(asesinados, "GAO ELN", 7, 18)
    res_heridos = calculo(heridos, "GAO ELN", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-ELN", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)

    res_asesinados = calculo_tres(asesinados,"GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", 7, 18)
    res_heridos = calculo_tres(heridos,"GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-r", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)

    res_asesinados = calculo(asesinados, "GAO CLAN DEL GOLFO", 7, 18)
    res_heridos = calculo(heridos, "GAO CLAN DEL GOLFO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-CG", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)
        
    res_asesinados = calculo(asesinados, "GDO", 7, 18)
    res_heridos = calculo(heridos, "GDO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GDO", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)
                
    res_asesinados = calculo(asesinados, "GAO CAPARROS", 7, 18)
    res_heridos = calculo(heridos, "GAO CAPARROS", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-CAP", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)
                        
    res_asesinados = calculo(asesinados, "GAO PELUSOS", 7, 18)
    res_heridos = calculo(heridos, "GAO PELUSOS", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"GAO-PEL", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)
                                
    res_asesinados = calculo(asesinados, "NARCOTRÁFICO", 7, 18)
    res_heridos = calculo(heridos, "NARCOTRÁFICO", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"NARCOTRÁFICO", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)
    
    res_asesinados = calculo(asesinados, "DELINCUENCIA", 7, 18)
    res_heridos = calculo(heridos, "DELINCUENCIA", 7, 18)
    total = suma_h_a(res_asesinados, res_heridos)

    if total != "-":
        numero = numero +1
        text = (x, y, str(numero),"DELINCUENCIA", str(res_asesinados), str(res_heridos), str(total), a, fill )
        celda_afectaciones(pdf, 5, 172, text, rango, id)

    rango =4
    pdf.set_fill_color(94, 119, 89)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)

    x = (78,28.5,28.5,28.5)
    y= (7,7,7,7)
    resultado_asesinados = calculo_total_sin_filtro(asesinados, 18)
    resultado_heridos = calculo_total_sin_filtro(heridos, 18)
    a = ("C","C","C","C") 
    fill = (True, True, True, True)
    id = (6,7)

    total = suma_h_a(resultado_asesinados, resultado_heridos)
    pdf.set_font('Arial', 'B', 12)
    text = (x, y, "TOTAL", str(resultado_asesinados), str(resultado_heridos), str(total), a, fill  )
    celda_afectaciones(pdf, 5, 172, text, rango, id)

def variables_acciones(pdf, datos, cell, posicion_inicial_final):
    acciones_asecinados  =[]
    posicion_inicial = pdf.get_y()
    
    # print(posicion_inicial)

    for dato in datos:
        if  dato[9] not in acciones_asecinados:
            acciones_asecinados.append(dato[9])

    if posicion_inicial_final == -1:
        if posicion_inicial < 68:

            pdf.ln(35)
        else:
            pdf.ln(30)
    else:
        if posicion_inicial == 114.00125:

            posicion_inicial_2 = 12
            
        else:
            posicion_inicial_2 =  (posicion_inicial_final * 5)+12

        # print(posicion_inicial_2)
        pdf.ln(-posicion_inicial_2)

    
    pdf.set_font('Arial', 'B', 14)

    pdf.cell(cell)
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.cell(163.5,7,"AFECTACIONES POR ACCIÓN DIRECTA DEL ENEMIGO",1,0, 'C',True)
    pdf.set_fill_color(208,208,182)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 12)

    x = (10,125,28.5)
    y= (5,5,5)
    rango =3
    a = ("C","C","C") 
    fill = (True, True, True)
    pdf.set_font('Arial', 'B', 12)
    text = (x, y, "No.","AFECTACION", "CANTIDAD", a, fill )
    id = (5,6)

    pdf.set_font('Arial', 'B', 12)
    celda_afectaciones(pdf, 7, cell, text, rango, id)
    pdf.set_font('Arial', 'B', 11)
    numero = 0
    fill = (False, False, False)
    a = ("C","L","C") 
    for accion in acciones_asecinados:
        numero = numero +1
        asesinado = 0   
        asesinado = calculo(datos, accion, 9, 18)

        text = (x, y, str(numero),str(accion), str(asesinado), a, fill )
        id = (5,6)
        celda_afectaciones(pdf, 5, cell, text, rango, id)

    total = calculo_total_sin_filtro(datos, 18)
    #total de la celda
    x = (135,28.5)
    y= (7,7)
    rango =2
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    a = ("C","C") 
    fill = (True, True)
    pdf.set_font('Arial', 'B', 12)
    text = (x, y, "TOTAL", str(total), a, fill )
    id = (4,5)
    celda_afectaciones(pdf, 5, cell, text, rango, id)
    return numero
    
#cabecera de las afectaciones
def cabecera_afectaciones(pdf):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 9)

    pdf.cell(-5)
    pdf.cell(20,5,"ENEMIGO.",1,0, 'C',True)
    pdf.cell(10,5,"No.",1,0, 'C',True)
    pdf.cell(20,5,"FECHA",1,0, 'C',True)
    pdf.cell(10,5,"GRD",1,0, 'C',True)
    pdf.cell(70,5,"NOMBRES Y APELLIDOS",1,0, 'C',True)
    pdf.cell(50,5,"DEPTO",1,0, 'C',True)
    pdf.cell(50,5,"LUGAR",1,0, 'C',True)
    pdf.cell(22,5,"DIV",1,0, 'C',True)
    pdf.cell(22,5,"BR",1,0, 'C',True)
    pdf.cell(22,5,"UNIDAD",1,0, 'C',True)
    pdf.cell(50,5,"AFECTACIÓN",1,0, 'C',True)

#listados
def listados_pdf(pdf, resultados, parametro, parametro_dos, parametro_tres, text, id_parametro):
    # pdf.cell(-5)
    numero = 0
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 9)

    validacion =""
    posicion_inicial = pdf.get_y()
    for res in resultados:
        if res[id_parametro] == parametro or res[id_parametro] == parametro_dos or res[id_parametro] == parametro_tres :
            validacion= res[id_parametro]
            numero =  numero +1
            pdf.cell(15)
            pdf.multi_cell(10, 5, str(numero), 0, "C", False)
            num = pdf.get_x()
            
            pdf.ln(-num+5)
            pdf.cell(25)
            pdf.multi_cell(20, 5, str(res[0]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(45)
            pdf.multi_cell(10, 5, str(res[19]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(55)
            pdf.multi_cell(70, 5, str(res[20]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(125)
            pdf.multi_cell(50, 5, str(res[5]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(175)
            pdf.multi_cell(50, 5, str(res[6]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(225)
            pdf.multi_cell(22, 5, str(res[1]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(247)
            pdf.multi_cell(22, 5, str(res[3]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(269)
            pdf.multi_cell(22, 5, str(res[4]), 0, "C", False)
            num = pdf.get_x()
            pdf.ln(-num+5)
            pdf.cell(291)
            pdf.multi_cell(50, 5, str(res[9]), 0, "C", False)
            posicion_final = pdf.get_y()
            # print(num1)
            # num1 = num1-num2
            pdf.set_line_width(0.1)
            pdf.set_draw_color(140, 140, 140)
            pdf.line(25, posicion_final, 350, posicion_final)

            if posicion_final > 200 :
                num2 = ((posicion_final-posicion_inicial)/2)+posicion_inicial
                pdf.text(5,num2+1, text)

    if validacion != "":
        # ln = 5 * numero
        # pdf.ln(-10)
        
        if posicion_final > posicion_inicial:
            num2 = ((posicion_final-posicion_inicial)/2)+posicion_inicial
            pdf.text(5,num2+1, text)
        else:
            pass
            num3 = ((posicion_final-30)/2)+30
            pdf.text(5,num3, text)

        pdf.cell(-5)

        

        pdf.ln(-5)

        pdf.set_line_width(0.5)
        pdf.set_draw_color(125, 0, 0)
        # pdf.line(5, posicion_inicial, 350, posicion_inicial)
        pdf.line(5, posicion_final, 350, posicion_final)
        pdf.set_line_width(0.1)
        pdf.set_draw_color(0, 0, 0)
        pdf.ln(5)
        # pdf.ln(5)
        return posicion_final
    
#funcion para pintar el listado de las afectaciona

def listado_afectacion(pdf, resultados, text):
    
    separador_cuadro_coe(pdf, True, text)
    pdf.ln(10)

    cabecera_afectaciones(pdf)
    pdf.ln()

    listados_pdf(pdf, resultados, "GAO ELN", "GAO ELN", "GAO ELN", "GAO-ELN", 7)

    listados_pdf(pdf, resultados, "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC","GAO-r", 7)

    listados_pdf(pdf, resultados, "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO-CG", 7)


    listados_pdf(pdf, resultados, "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS","GAO-CAP", 7)


    listados_pdf(pdf, resultados, "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS","GAO-PEL", 7)


    listados_pdf(pdf, resultados, "GDO","GDO","GDO","GDO", 7)


    listados_pdf(pdf, resultados, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCO.", 7)


    listados_pdf(pdf, resultados, "DELINCUENCIA","DELINCUENCIA","DELINCUENCIA","DELCO", 7)

#encabezado de interdiccion
def encabezado_interdicion(pdf):

    pdf.set_line_width(0.1)
    pdf.set_fill_color(94, 119, 89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    pdf.ln(20)
    pdf.cell(176)
    pdf.cell(165,10,"RESULTADOS INTERDICCIÓN",1,0, 'C',True)
    pdf.set_fill_color(208, 208, 182)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.cell(176)
    pdf.cell(65,10,"INDICADOR",1,0, 'C',True)
    pdf.cell(25,10,"CANTIDAD",1,0, 'C',True)
    pdf.cell(25,10,"META",1,0, 'C',True)
    pdf.cell(25,10,"%",1,0, 'C',True)
    pdf.cell(25,10,"INDICADOR",1,0, 'C',True)

    # pdf.set_fill_color(227, 227, 211)
    # pdf.set_text_color(0,0,0)

    # pdf.ln(5)
    # pdf.cell(176)
    # pdf.cell(60,5,"EVENTO",1,0, 'C',True)
#FUNCION PARA CALCULAR RESULTADOS DE INTEWRDICIOIN 
def calculo_de_interdion(pdf,text, datos_res_act, meta, unidad):
    pdf.set_line_width(0.1)
    pdf.cell(176)
    pdf.set_text_color(0,0,0)
    res  = comparativo_metas(datos_res_act, 18, 1, meta, unidad)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(65,10,text,1,0, 'L',False)
    pdf.set_font('Arial', '', 12)
    pdf.cell(25,10,res[0],1,0, 'C',False)
    pdf.cell(25,10,res[1],1,0, 'C',False)
    pdf.cell(25,10,res[2],1,0, 'C',False)
    pdf.cell(25,10,unidad,1,0, 'C',False)

#Funcion para encabezado de resultados tabal con mapa
def encabezado_tabla_resultados_mapa(pdf, text):
    
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    pdf.ln(20)
    pdf.cell(176)
    pdf.cell(165,10,text,1,0, 'C',True)
    pdf.ln(10)
    pdf.cell(176)
    pdf.cell(65,10,"INDICADOR",1,0, 'C',True)
    pdf.cell(50,10,"CANTIDAD",1,0, 'C',True)
    pdf.cell(50,10,"INDICADOR",1,0, 'C',True)
#tabla de resultados 
def tabla_resultados_con_mapa(pdf,text,datos_res_act, unidad, suma):
    pdf.set_line_width(0.1)
    pdf.cell(176)
    pdf.set_text_color(0,0,0)
    res  = resultados_tabla_mapa_indicador(datos_res_act, suma,  unidad)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(65,10,text,1,0, 'L',False)
    pdf.set_font('Arial', '', 12)
    pdf.cell(50,10,res[0],1,0, 'C',False)
    pdf.cell(50,10,unidad,1,0, 'C',False)

#Funcion para encabezado de resultados tabal con mapa
def encabezado_tabla_resultados_mapa_compa(pdf, text, anio_act, anio_ant):
    
    pdf.set_line_width(0.1)
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    pdf.ln(20)
    pdf.cell(147)
    pdf.cell(191,10,text,1,0, 'C',True)
    pdf.set_fill_color(208,208,182)
    pdf.set_text_color(0,0,0)
    pdf.ln(10)
    pdf.cell(147)
    pdf.cell(65,10,"INDICADOR",1,0, 'C',True)
    pdf.cell(33,10,str(anio_ant),1,0, 'C',True)
    pdf.cell(33,10,str(anio_act),1,0, 'C',True)
    pdf.cell(30,10,"%",1,0, 'C',True)
    pdf.cell(30,10,"INDICADOR",1,0, 'C',True)

#tabla de resultados 
def tabla_resultados_con_mapa_comp(pdf,text,datos_res_ant, datos_res_act, unidad, suma, constante):
    pdf.set_line_width(0.1)
    pdf.cell(147)
    pdf.set_text_color(0,0,0)
    res = comparativo_redondo(datos_res_ant, datos_res_act, suma, constante, unidad )

    pdf.set_font('Arial', 'B', 12)
    pdf.cell(65,10,text,1,0, 'L',False)
    pdf.set_font('Arial', '', 12)
    pdf.cell(33,10,str(res[0]),1,0, 'C',False)
    pdf.cell(33,10,str(res[1]),1,0, 'C',False)
    pdf.cell(30,10,str(res[2]),1,0, 'C',False)
    pdf.cell(30,10,unidad,1,0, 'C',False)
#tabla de resultados 
def tabla_resultados_con_mapa_comp_maquinaria(pdf, datos_res_ant,  datos_res_act, text, constante, id_enemigo, suma, unidad):
    pdf.set_line_width(0.1)
    pdf.cell(147)
    pdf.set_text_color(0,0,0)
    
#funcion para titulos de resutados 

    maquinari_amarialla_anterior= 0
    maquinari_amarialla_actual= 0
    res = 0
    res = calculo_total_sin_filtro_b(datos_res_ant[0], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res
    res = calculo_total_sin_filtro_b(datos_res_ant[1], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res
    res = calculo_total_sin_filtro_b(datos_res_ant[2], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res
    res = calculo_total_sin_filtro_b(datos_res_ant[3], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res
    res = calculo_total_sin_filtro_b(datos_res_ant[4], suma)
    maquinari_amarialla_anterior = maquinari_amarialla_anterior + res

    res = 0
    res = calculo_total_sin_filtro_b(datos_res_act[0], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[1], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[2], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[3], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res
    res = calculo_total_sin_filtro_b(datos_res_act[4], suma)
    maquinari_amarialla_actual = maquinari_amarialla_actual + res


    # resultados  = calculo_comprativo_total(maquinari_amarialla_anterior, maquinari_amarialla_actual, suma, constante)
    resultados = porcentajes(maquinari_amarialla_anterior, maquinari_amarialla_actual, constante)

    maquinari_amarialla_anterior = formato_numero(maquinari_amarialla_anterior)
    maquinari_amarialla_actual = formato_numero(maquinari_amarialla_actual)
    resultados = formato_numero(resultados)

    # pdf.cell(30,5,str(maquinari_amarialla_anterior),1,0, 'C',False)
    # pdf.cell(30,5,str(maquinari_amarialla_actual),1,0, 'C',False)
    # pdf.cell(25,5,str(resultados),1,0, 'C',False)

    
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(65,10,text,1,0, 'L',False)
    pdf.set_font('Arial', '', 12)
    pdf.cell(33,10,str(maquinari_amarialla_anterior),1,0, 'C',False)
    pdf.cell(33,10,str(maquinari_amarialla_actual),1,0, 'C',False)
    pdf.cell(30,10,str(resultados),1,0, 'C',False)
    pdf.cell(30,10,unidad,1,0, 'C',False)

def cabecera_tabla_dinamica(pdf, text, ln, cell):
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    pdf.ln(ln)
    pdf.cell(cell)
    pdf.cell(165,5,text,1,0, 'C',True)

    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(227, 227, 211)

    pdf.ln(ln)
    pdf.cell(cell)
    pdf.cell(85,5,"EVENTO",1,0, 'C',True)
    pdf.cell(40,5,"CANTIDAD",1,0, 'C',True)
    pdf.cell(40,5,"INDICADOR",1,0, 'C',True)

#FUNCION PARA CALCULAR RESULTADOS
def resultados_tabla_dinamica(pdf, datos_res_act, text, suma, unidad, cell):
    
    pdf.set_line_width(0.1)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(0,0,0)
    pdf.set_fill_color(227, 227, 211)
    pdf.cell(cell)
    res  = resultados_tabla_mapa_indicador(datos_res_act, suma,  unidad)
    pdf.set_font('Arial', 'B', 11)
    pdf.cell(85,5,text,1,0, 'L',True)
    pdf.set_font('Arial', '', 11)
    pdf.cell(40,5,res[0],1,0, 'R',False)
    pdf.cell(40,5,unidad,1,0, 'C',False)
    pdf.ln()

def separador_boletin_tabla_resultados(pdf,cell, text):
        
    pdf.cell(cell)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(165,6,text,1,0, 'C',True)
    pdf.ln()
#cuadro afectaciones propias tropas

def cuadro_afectaciones(pdf, datos, filtro):

    ruta = filtro[15]
    pdf.ln(60)
    pdf.set_line_width(0.1)
    pdf.set_fill_color(94,119,89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)


    pdf.cell(175)

    pdf.cell(24,10,"EVENTO",1,0, 'C',True)
    pdf.cell(44,10,"ASESINADOS",1,0, 'C',True)
    pdf.cell(44,10,"HERIDOS",1,0, 'C',True)
    pdf.cell(44,10,"TOTAL NOVEDADES",1,0, 'C',True)
    pdf.set_text_color(0,0,0)
    pdf.ln()
    pdf.cell(175)
    pdf.cell(24,10,"AÑO",1,0, 'C',False)
    pdf.cell(22,10,datos[4],1,0, 'C',False)
    pdf.cell(22,10,datos[5],1,0, 'C',False)
    pdf.cell(22,10,datos[4],1,0, 'C',False)
    pdf.cell(22,10,datos[5],1,0, 'C',False)
    pdf.cell(22,10,datos[4],1,0, 'C',False)
    pdf.cell(22,10,datos[5],1,0, 'C',False)
    pdf.ln()
    pdf.cell(175)
    pdf.cell(24,10,"CANTIDAD",1,0, 'C',False)

    res_ase_ant  = calculo_total_sin_filtro(datos[0], 18)


    pdf.cell(22,10,res_ase_ant,1,0, 'C',False)
    res_ase_act  = calculo_total_sin_filtro(datos[1], 18)
    pdf.cell(22,10,res_ase_act,1,0, 'C',False)
    res_heri_ant  = calculo_total_sin_filtro(datos[2], 18)
    pdf.cell(22,10,res_heri_ant,1,0, 'C',False)
    res_heri_act  = calculo_total_sin_filtro(datos[3], 18)
    pdf.cell(22,10,res_heri_act,1,0, 'C',False)

    if res_ase_ant == "-":
        res_ase_ant_1 = 0
    else:
     res_ase_ant_1 = int(res_ase_ant)

     
    if res_heri_ant == "-":
        res_heri_ant_1 = 0
    else:
     res_heri_ant_1 = int(res_heri_ant)

    total_afect = res_ase_ant_1+res_heri_ant_1

    pdf.cell(22,10,str(total_afect),1,0, 'C',False)
    
    
    if res_ase_act == "-":
        res_ase_act_1 = 0
    else:
     res_ase_act_1 = int(res_ase_act)

     
    if res_heri_act == "-":
        res_heri_act_1 = 0
    else:
        res_heri_act_1 = int(res_heri_act)
     
    
    
    total_afect = res_ase_act_1+res_heri_act_1

    pdf.cell(22,10,str(total_afect),1,0, 'C',False)

    asesinados = '{}static/img/img_mapas/asesinados.jpg'.format(ruta)
    heridos = '{}static/img/img_mapas/heridos.jpg'.format(ruta)
    soldados = '{}static/img/img_mapas/soldados.jpg'.format(ruta)

    pdf.image(asesinados,200,140,10,10)
    pdf.text(212,145,str(res_ase_act)+" ASESINADOS")
    pdf.image(heridos,270,140,10,10)
    pdf.text(282,145,str(res_heri_act)+" HERIDOS")
    pdf.image(soldados,240,160,20,20)
    pdf.text(265,170,str(total_afect)+" TOTAL AFECTACIONES")

    pdf.set_fill_color(94, 119, 89)
    pdf.rounded_rect(190, 40, 150, 30, 1,'F', '1234')
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)
    pdf.text(240,45,"FECHA INFORMACION")
    pdf.set_font('Arial', 'B', 12)
    pdf.text(210,55,datos[7])
    pdf.text(210,60,datos[6])
    
def cuadro_men_res(pdf, datos_res, enemigo, gao, gao_1, gao_2):

    rme_resul = calculo_tres_b(datos_res, gao, gao_1, gao_2, 7, 18)
    rme_resul = formato_numero(rme_resul)
    if rme_resul != "-":
        pdf.ln(5)
        pdf.cell(-5)
        pdf.cell(33,5,str(enemigo),1,0, 'L',False)
        pdf.cell(17,5,str(rme_resul),1,0, 'C',False)
        return 5
    else:
        return 0
     
def cuadro_men_res_of(pdf, datos_res, enemigo, gao, gao_1, gao_2, flecha):

    rme_resul = calculo_tres_b(datos_res, gao, gao_1, gao_2, 7, 18)
    rme_resul = formato_numero(rme_resul)
    if rme_resul != "-":
        pdf.ln(5)
        pdf.cell(-5)
        pdf.cell(28,5,str(enemigo),0,0, 'L',False)
        pdf.cell(20,5,str(rme_resul),0,0, 'C',False)
            #separador

        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 52
        a = 5
        while a < lineas:
            pdf.line(a, flecha, a+1, flecha)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        return 5
    else:
        return 0       
def cuadro_afect_enemigo(pdf, datos_res, enemigo, gao, gao_1, gao_2):

    pre = calculo_tres_b(datos_res[0], gao, gao_1, gao_2, 7, 18)
    some = calculo_tres_b(datos_res[1], gao, gao_1, gao_2, 7, 18)
    capt = calculo_tres_b(datos_res[2], gao, gao_1, gao_2, 7, 18)
    mdom = calculo_tres_b(datos_res[3], gao, gao_1, gao_2, 7, 18)
    
 
    total = pre + some + capt + mdom

    pre = formato_numero(pre)
    some = formato_numero(some)
    capt = formato_numero(capt)
    mdom = formato_numero(mdom)
    total = formato_numero(total)

    if total != "-":
        pdf.ln(5)
        pdf.cell(49)
        pdf.cell(30,5,str(enemigo),1,0, 'L',False)
        pdf.cell(19,5,str(pre),1,0, 'C',False)
        pdf.cell(19,5,str(some),1,0, 'C',False)
        pdf.cell(19,5,str(capt),1,0, 'C',False)
        pdf.cell(19,5,str(mdom),1,0, 'C',False)
        pdf.cell(19,5,str(total),1,0, 'C',False)

        return 5
    else:
        return 0

def cuadro_afect_enemigo_oficio(pdf, datos_res, enemigo, gao, gao_1, gao_2, flecha):

    pre = calculo_tres_b(datos_res[0], gao, gao_1, gao_2, 7, 18)
    some = calculo_tres_b(datos_res[1], gao, gao_1, gao_2, 7, 18)
    capt = calculo_tres_b(datos_res[2], gao, gao_1, gao_2, 7, 18)
    mdom = calculo_tres_b(datos_res[3], gao, gao_1, gao_2, 7, 18)
    
 
    total = pre + some + capt + mdom

    pre = formato_numero(pre)
    some = formato_numero(some)
    capt = formato_numero(capt)
    mdom = formato_numero(mdom)
    total = formato_numero(total)

    if total != "-":
        pdf.ln(5)
        pdf.cell(45)
        pdf.cell(28,5,str(enemigo),0,0, 'L',False)
        pdf.cell(33,5,str(pre),0,0, 'C',False)
        pdf.cell(33,5,str(some),0,0, 'C',False)
        pdf.cell(33,5,str(capt),0,0, 'C',False)
        pdf.cell(33,5,str(mdom),0,0, 'C',False)
        pdf.cell(33,5,str(total),0,0, 'C',False)

        
        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 247
        a = 56
        while a < lineas:
            pdf.line(a, flecha, a+1, flecha)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------
        return 5
    else:
        return 0

def cuadro_afectaciones_tropas(pdf, datos_res, enemigo, gao, gao_1, gao_2):

    ases = calculo_tres_b(datos_res[0], gao, gao_1, gao_2, 7, 18)
    heridos = calculo_tres_b(datos_res[1], gao, gao_1, gao_2, 7, 18)

    total = ases + heridos 

    ases = formato_numero(ases)
    heridos = formato_numero(heridos)
    total = formato_numero(total)

    if total != "-":
        pdf.ln(5)
        pdf.cell(178)

        pdf.cell(30,5,str(enemigo),1,0, 'C',False)
        pdf.cell(19,5,str(ases),1,0, 'C',False)
        pdf.cell(19,5,str(heridos),1,0, 'C',False)
        pdf.cell(19,5,str(total),1,0, 'C',False)
    
        return 5
    else:
        return 0 
def cuadro_afectaciones_tropas_oficio(pdf, datos_res, enemigo, gao, gao_1, gao_2, flecha):

    if gao != "NO APLICA":
        ases = calculo_tres_b(datos_res[0], gao, gao_1, gao_2, 7, 18)
        heridos = calculo_tres_b(datos_res[1], gao, gao_1, gao_2, 7, 18)
    else:
        ases = calculo_tres_b(datos_res[2], gao, gao_1, gao_2, 7, 18)
        heridos = calculo_tres_b(datos_res[3], gao, gao_1, gao_2, 7, 18)

    total = ases + heridos 

    ases = formato_numero(ases)
    heridos = formato_numero(heridos)
    total = formato_numero(total)

    if total != "-":
        pdf.ln(5)
        pdf.cell(240)

        pdf.cell(28,5,str(enemigo),0,0, 'L',False)
        pdf.cell(25,5,str(ases),0,0, 'C',False)
        pdf.cell(25,5,str(heridos),0,0, 'C',False)
        pdf.cell(25,5,str(total),0,0, 'C',False)

        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 353
        a = 251
        while a < lineas:
            pdf.line(a, flecha, a+1, flecha)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------
        return 5
    else:
        return 0

def cuadro_menores_edad(pdf, datos_res):
    rme_resul = calculo_total_sin_filtro(datos_res, 18)
    
    pdf.ln(5)
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', 'B', 10)

    posicion = 0
    pdf.cell(-5)
    if rme_resul != "-":

        pdf.cell(50,5,"MENORES RECUPERADOS",1,0, 'C',False)
        pdf.set_font('Arial', '', 9)
        posicion = 5 + posicion
        posi = cuadro_men_res(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN")
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC")
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO")
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS")
        posicion = posi + posicion        
        posi = cuadro_men_res(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS",)
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "GDO","GDO","GDO","GDO")
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO")
        posicion = posi + posicion
        posi = cuadro_men_res(pdf, datos_res, "DELINCUENCIA","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA")
        posicion = posi + posicion
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        pdf.cell(-5)
        pdf.cell(33,5,"TOTAL",1,0, 'C',False)
        pdf.cell(17,5,rme_resul,1,0, 'C',False)
        posicion = posicion + 5
        pdf.ln(5)

    return posicion

#oficio
def cuadro_menores_edad_ofico(pdf, datos_res):
    rme_resul = calculo_total_sin_filtro(datos_res, 18)
    
    pdf.ln(5)
    pdf.set_line_width(0.5)
    pdf.set_fill_color(106, 78, 64)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_font('Arial', 'B', 10)

    posicion = 0
    flecha = 40
    pdf.cell(-5)
    pdf.set_text_color(255,255,255)
    pdf.line(5, flecha, 53, flecha)
    pdf.cell(48,5,"MENORES RECUPERADOS",0,0, 'C',True)
    pdf.line(5, flecha+5, 53, flecha+5)
    flecha = 5 + flecha
    pdf.set_text_color(0,0,0)
    pdf.set_font('Arial', '', 9)
    
    if rme_resul != "-":
        posicion = 5 + posicion
        posi = cuadro_men_res_of(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", flecha)
        posicion = posi + posicion 
        flecha = posi + flecha       
        posi = cuadro_men_res_of(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS",flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "GDO","GDO","GDO","GDO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
        posi = cuadro_men_res_of(pdf, datos_res, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", flecha)
        posicion = posi + posicion
        flecha = posi + flecha
    pdf.set_font('Arial', 'B', 10)
    pdf.ln(5)
    pdf.cell(-5)
    pdf.set_fill_color(217, 217, 217)
    pdf.cell(28,5,"TOTAL",0,0, 'C',True)
    pdf.cell(20,5,rme_resul,0,0, 'C',True)
    posicion = posicion + 5
    flecha = 5 + flecha
    pdf.line(5, flecha, 53, flecha)
    pdf.ln(5)

    return posicion

#funcion para calcular las afectaciones del enemigo cuadro
def cuadro_enemigo_afectaciones(pdf, posicion_inicial, datos_res):
    # posicion_inicial = pdf.get_x()

    
    pres = calculo_total_sin_filtro_b(datos_res[0], 18)
    some = calculo_total_sin_filtro_b(datos_res[1], 18)
    capt = calculo_total_sin_filtro_b(datos_res[2], 18)
    mdom = calculo_total_sin_filtro_b(datos_res[3], 18)

    total = pres + some + capt + mdom

    pres = formato_numero(pres)
    some = formato_numero(some)
    capt = formato_numero(capt)
    mdom = formato_numero(mdom)
    total = formato_numero(total)
    posicion = 0
    if total != "-":
        
        pdf.ln(-posicion_inicial)
        pdf.set_line_width(0.1)
        pdf.set_fill_color(193, 30, 38)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)

        pdf.cell(49)

        pdf.cell(30,5,"ENEMIGO",1,0, 'C',False)
        pdf.cell(19,5,"PRE.VOL",1,0, 'C',False)
        pdf.cell(19,5,"SOME.",1,0, 'C',False)
        pdf.cell(19,5,"CAPT.",1,0, 'C',False)
        pdf.cell(19,5,"MDOM",1,0, 'C',False)
        pdf.cell(19,5,"TOTAL",1,0, 'C',False)
        posicion = 5 + posicion
        pdf.set_font('Arial', '', 9)

        posi = cuadro_afect_enemigo(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN")
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC")
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO")
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS")
        posicion = posi + posicion         
        posi = cuadro_afect_enemigo(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS",)
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "GDO","GDO","GDO","GDO")
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO")
        posicion = posi + posicion
        posi = cuadro_afect_enemigo(pdf, datos_res, "DELINCUENCIA","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA")
        posicion = posi + posicion
        pdf.set_font('Arial', 'B', 10)
        pdf.ln (5)
        pdf.cell(49)
        pdf.cell(30,5,"TOTAL",1,0, 'C',False)
        pdf.cell(19,5,str(pres),1,0, 'C',False)
        pdf.cell(19,5,str(some),1,0, 'C',False)
        pdf.cell(19,5,str(capt),1,0, 'C',False)
        pdf.cell(19,5,str(mdom),1,0, 'C',False)
        pdf.cell(19,5,str(total),1,0, 'C',False)
        posicion = 5 + posicion
        pdf.ln (5)

    return posicion

#funcion para calcular las afectaciones del enemigo cuadro
def cuadro_enemigo_afectaciones_oficio(pdf, posicion_inicial, datos_res):
    # posicion_inicial = pdf.get_x()

    pres = calculo_total_sin_filtro_b(datos_res[0], 18)
    some = calculo_total_sin_filtro_b(datos_res[1], 18)
    capt = calculo_total_sin_filtro_b(datos_res[2], 18)
    mdom = calculo_total_sin_filtro_b(datos_res[3], 18)

    total = pres + some + capt + mdom

    pres = formato_numero(pres)
    some = formato_numero(some)
    capt = formato_numero(capt)
    mdom = formato_numero(mdom)
    total = formato_numero(total)
    posicion = 0
    flecha = 40

            
    pdf.line(55, flecha, 248, flecha)
    pdf.line(55, flecha+5, 248, flecha+5)
    pdf.ln(-posicion_inicial)
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 10)

    pdf.cell(45)

    pdf.cell(28,5,"ENEMIGO",0,0, 'C',True)
    pdf.cell(33,5,"PRE. VOLUNTARIA",0,0, 'C',True)
    pdf.cell(33,5,"SOMETIMIENTOS",0,0, 'C',True)
    pdf.cell(33,5,"CAPTURAS",0,0, 'C',True)
    pdf.cell(33,5,"MDOM",0,0, 'C',True)
    pdf.cell(33,5,"TOTAL",0,0, 'C',True)
    posicion = 5 + posicion
    flecha = 5 + flecha
    pdf.set_font('Arial', '', 9)
    pdf.set_text_color(0,0,0)
    
    if total != "-":


        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "GDO","GDO","GDO","GDO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

        posi = cuadro_afect_enemigo_oficio(pdf, datos_res, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", flecha)
        posicion = posi + posicion
        flecha = posi + flecha

    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(217, 217, 217)
    pdf.ln (5)
    pdf.cell(45)
    pdf.cell(28,5,"TOTAL",0,0, 'C',True)
    pdf.cell(33,5,str(pres),0,0, 'C',True)
    pdf.cell(33,5,str(some),0,0, 'C',True)
    pdf.cell(33,5,str(capt),0,0, 'C',True)
    pdf.cell(33,5,str(mdom),0,0, 'C',True)
    pdf.cell(33,5,str(total),0,0, 'C',True)

    posicion = 5 + posicion
    flecha = 5 + flecha
    pdf.line(55, flecha, 248, flecha)
    pdf.ln (5)

    return posicion

def cuadro_afectaciones_tropas_combate (pdf, posicion_inicial, datos_res ):

    asesinados = calculo_total_sin_filtro_b(datos_res[0], 18)
    heridos = calculo_total_sin_filtro_b(datos_res[1], 18)

    total = asesinados + heridos 

    asesinados = formato_numero(asesinados)
    heridos = formato_numero(heridos)
    total = formato_numero(total)
    posicion = 0
    if total != "-":
        pdf.ln(-posicion_inicial)
        pdf.set_line_width(0.1)
        pdf.set_fill_color(193, 30, 38)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 10)

        pdf.cell(178)

        pdf.cell(30,5,"ENEMIGO",1,0, 'C',False)
        pdf.cell(19,5,"ASES..",1,0, 'C',False)
        pdf.cell(19,5,"HERI.",1,0, 'C',False)
        pdf.cell(19,5,"TOTAL",1,0, 'C',False)
        posicion = posicion + 5
        pdf.set_font('Arial', '', 9)
    
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN")
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC")
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO")
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS")
        posicion = posi + posicion      
        posi = cuadro_afectaciones_tropas(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS",)
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "GDO","GDO","GDO","GDO")
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO")
        posicion = posi + posicion
        posi = cuadro_afectaciones_tropas(pdf, datos_res, "DELINCUENCIA","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA")
        posicion = posi + posicion

        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        pdf.cell(178)

        pdf.cell(30,5,"TOTAL",1,0, 'C',False)
        pdf.cell(19,5,str(asesinados),1,0, 'C',False)
        pdf.cell(19,5,str(heridos),1,0, 'C',False)
        pdf.cell(19,5,str(total),1,0, 'C',False)
        posicion = 5 + posicion
        pdf.ln (5)
    return posicion

def cuadro_afectaciones_tropas_combate_oficio (pdf, posicion_inicial, datos_res ):

    asesinados = calculo_total_sin_filtro_b(datos_res[0], 18)
    heridos = calculo_total_sin_filtro_b(datos_res[1], 18)

    asesinados_fuera = calculo_total_sin_filtro_b(datos_res[2], 18)
    heridos_fuera = calculo_total_sin_filtro_b(datos_res[3], 18)

    total = asesinados + heridos + asesinados_fuera +heridos_fuera

    asesinados = formato_numero(asesinados + asesinados_fuera )
    heridos = formato_numero(heridos + heridos_fuera)

    total = formato_numero(total)
    flecha = 40
    posicion = 0
    pdf.ln(-posicion_inicial)
    pdf.line(250, flecha, 353, flecha)
    pdf.line(250, flecha+5, 353, flecha+5)
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 10)

    pdf.cell(240)

    pdf.cell(28,5,"ENEMIGO",0,0, 'C',True)
    pdf.cell(25,5,"ASESINADOS",0,0, 'C',True)
    pdf.cell(25,5,"HERIDOS",0,0, 'C',True)
    pdf.cell(25,5,"TOTAL",0,0, 'C',True)
    pdf.set_text_color(0,0,0)
    flecha = 5 + flecha
    posi=5
    if total != "-":


        pdf.set_font('Arial', '', 9)
    
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
                 
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "GDO","GDO","GDO","GDO", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", flecha)
        flecha = posi + flecha
        posicion = posi + posicion
        
        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", flecha)
        flecha = posi + flecha
        posicion = posi + posicion

        posi = cuadro_afectaciones_tropas_oficio(pdf, datos_res, "DIF. AMENAZA","NO APLICA","NO APLICA","NO APLICA", flecha)
        flecha = posi + flecha
        posicion = posi + posicion

    pdf.set_font('Arial', 'B', 10)
    pdf.ln(5)
    pdf.cell(240)
    pdf.set_fill_color(217, 217, 217)
    pdf.cell(28,5,"TOTAL",0,0, 'C',True)
    pdf.cell(25,5,str(asesinados),0,0, 'C',True)
    pdf.cell(25,5,str(heridos),0,0, 'C',True)
    pdf.cell(25,5,str(total),0,0, 'C',True)

    flecha = 5 + flecha
    posicion = 5 + posicion
    pdf.line(250, flecha, 353, flecha)
    return posicion

def grupo_result_resal_dos(pdf, pos_vert, pos, elemento, datos_res, suma, imagen, filtro):
    ruta = '{}static/img/resultados/'.format(filtro[15])
    resultado = datos_res
    direccion = str(ruta) + str(imagen)
    inicio = str(ruta) + str("triangulo_verde_invertido_ayuda.png")
    final = str(ruta) + str("final_resultado_ayuda.png")
    if resultado != "-":
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image(direccion,pos_vert[2],pos-4,6,6)

        pdf.image(inicio,pos_vert[3],pos-3,2,3)
        
        # pdf.text(pos_vert[0], pos, str(elemento) )    
        # pdf.text(pos_vert[1], pos, str(resultado) )
        pdf.cell(pos_vert[2])
        pdf.cell(pos_vert[1],6,str(elemento),0,0, 'L',False)
        pdf.cell(pos_vert[5],6,str(resultado),0,0, 'R',False)
        pdf.ln()

                
        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = pos_vert[4]+3
        a = pos_vert[0]-2
        while a < lineas:
            pdf.line(a, pos+2, a+1, pos+2)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        pdf.image(final,pos_vert[4],pos-3,3,3.5)
        pos = pos + 6
    return pos
def grupo_result_resal(pdf, pos_vert, pos, elemento, datos_res, suma, imagen, filtro):
    ruta = '{}static/img/resultados/'.format(filtro[15])
    resultado = calculo_total_sin_filtro(datos_res, suma)
    direccion = str(ruta) + str(imagen)
    inicio = str(ruta) + str("triangulo_verde_invertido_ayuda.png")
    final = str(ruta) + str("final_resultado_ayuda.png")
    if resultado != "-":
        pdf.set_font('Arial', '', 10)
        pdf.set_text_color(0, 0, 0)
        pdf.image(direccion,pos_vert[2],pos-4,6,6)

        pdf.image(inicio,pos_vert[3],pos-3,2,3)
        
        # pdf.text(pos_vert[0], pos, str(elemento) )    
        # pdf.text(pos_vert[1], pos, str(resultado) )
        pdf.cell(pos_vert[2])
        pdf.cell(pos_vert[1],6,str(elemento),0,0, 'L',False)
        pdf.cell(pos_vert[5],6,str(resultado),0,0, 'R',False)
        pdf.ln()

                
        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = pos_vert[4]+3
        a = pos_vert[0]-2
        while a < lineas:
            pdf.line(a, pos+2, a+1, pos+2)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        pdf.image(final,pos_vert[4],pos-3,3,3.5)
        pos = pos + 6
    return pos

#funcion para el calculo de los resultados 
def calculo_boletin_afectaciones(pdf, titulo, ln, datos_res_ant, datos_res_act, identificador_suma, constante, posicionamiento):
        
     
    pdf.set_text_color(0,0,0)#color del texto
    pdf.set_font('Arial', '', 8)#tipografia de la fuente de los textos

    numero =  calculo_comprativo_total_sin_formato(datos_res_ant, datos_res_act, identificador_suma, constante)

    pdf.set_line_width(0.3)#grueso de las lineas
    numero_anterior = numero[0]
    numero_actual = numero[1]
    porcentaje = numero[2]

    #formato de numero

    numero_anterior =  formato_numero(numero_anterior)
    numero_actual =  formato_numero(numero_actual)
    porcentaje =  formato_numero(porcentaje)

    porcentaje = str(porcentaje) + str(" %")
    pdf.ln(ln+0.2)
    pdf.cell(posicionamiento[0])
    y = pdf.get_y()
    pdf.multi_cell(posicionamiento[4],3,titulo,0,"L", False)

    x = pdf.get_y()
    z = (x-y)
    xy = (x-y)/1.3
    
    pdf.line(posicionamiento[0]+12, x+1, posicionamiento[3]+20, x+1)#linea 
    pdf.ln(-xy)
    
    y = pdf.get_y()
    pdf.cell(posicionamiento[1])

    pdf.multi_cell(posicionamiento[5],3,str(numero_anterior),0,"C", False)
    
    x = pdf.get_y()
    xy = (x-y)
    pdf.ln(-xy)
    y = pdf.get_y()

    pdf.cell(posicionamiento[2])
    pdf.multi_cell(posicionamiento[5],3,str(numero_actual),0,"C", False)

    x = pdf.get_y()
    xy = (x-y)
    pdf.ln(-xy)
    y = pdf.get_y()

    if numero[2]> 0:
        pdf.set_text_color(0,176,80)#color del texto
    elif numero[2]<0:
        pdf.set_text_color(192,0,0)#color del texto
    else:
        pdf.set_text_color(255,192,0)#color del texto

    pdf.cell(posicionamiento[3])
    pdf.multi_cell(posicionamiento[6],3,porcentaje,0,"L", False)
    x = pdf.get_y()
    f=(x-y)
    if z == f:
        f = 1
    pdf.set_text_color(0,0,0)#color del texto

    return(f, numero[0],numero[1])

#suma
def calculo_boletin_afectaciones_total(pdf, titulo, ln, datos_res_ant, datos_res_act,  constante, posicion, filtro, posicionamiento):

    numero =  porcentajes(datos_res_ant, datos_res_act, constante)
    pdf.set_line_width(0.5)#grueso de las lineas
    pdf.set_text_color(0,0,0)#color del texto
    pdf.set_font('Arial', 'B', 8)#tipografia de la fuente de los textos
    
    pdf.set_fill_color(217, 217, 217)
    pdf.rounded_rect(posicion[2], posicion[3], 82, 4.3, 1, 'F', '1234')
    numero_anterior = datos_res_ant
    numero_actual = datos_res_act
    porcentaje = numero

    #formato de numero

    numero_anterior =  formato_numero(numero_anterior)
    numero_actual =  formato_numero(numero_actual)
    porcentaje =  formato_numero(porcentaje)

    porcentaje = str(porcentaje) + str(" %")
    pdf.ln(ln)
    pdf.cell(posicionamiento[0])
    y = pdf.get_y()
    pdf.multi_cell(25,3,titulo,0,"J", False)

    x = pdf.get_y()
    z = (x-y)
    xy = (x-y)/1.3

    pdf.line(posicionamiento[0]+12, x+1, posicionamiento[3]+20, x+1)#linea 
    pdf.ln(-xy)
    y = pdf.get_y()
    pdf.cell(posicionamiento[1])

    pdf.multi_cell(posicionamiento[5],3,str(numero_anterior),0,"C", False)
    
    x = pdf.get_y()
    xy = (x-y)
    pdf.ln(-xy)
    y = pdf.get_y()
    pdf.cell(posicionamiento[2])
    pdf.multi_cell(posicionamiento[5],3,str(numero_actual),0,"C", False)

    x = pdf.get_y()
    xy = (x-y)
    pdf.ln(-xy)
    y = pdf.get_y()

    if numero> 0:
        pdf.set_text_color(0,176,80)#color del texto
        imagen = "cuadro_pos_boletin"
        altura = [10, 15]
        h = posicion[0]+2
        v = posicion[1]+10
    elif numero<0:
        pdf.set_text_color(192,0,0)#color del texto
        imagen = "cuadro_neg_boletin"
        altura = [10, 15]
        h = posicion[0]+2
        v = posicion[1]+7
    else:
        pdf.set_text_color(255,192,0)#color del texto
        imagen = "cuadro_neutro_boletin"
        altura = [15, 10]
        h = posicion[0]+3
        v = posicion[1]+6

    ruta_b='{}static/img/{}.png'.format(filtro[15],imagen)
    # scr\static\img\cuadro_neg_boletin.png
    # E:\bakeng_api_\scr\static\img\cuadro_neg_boletin.png

    pdf.image(ruta_b, posicion[0], posicion[1], altura[0], altura[1] )#imagenes 

    pdf.cell(posicionamiento[3])
    pdf.multi_cell(posicionamiento[6],3,porcentaje,0,"L", False)

    pdf.set_font('Arial', 'B', 7)#tipografia de la fuente de los textos
    pdf.text(h, v, porcentaje)
    x = pdf.get_y()
    f=(x-y)

    f=(x-y)
    if z == f:
        f = 1

    pdf.set_text_color(0,0,0)#color del texto
 
    return(f)

#titulos de las ayudas del boltin de la dirop
def titulo_boletin_dirop(pdf, filtro):


    #-------------------------------------------------------------
    #------------------componentes rectangulos e imagenes ---------
    #-------------------------------------------------------------
    pdf.set_fill_color(17, 63, 52)
    pdf.rounded_rect(63, 33, 100, 7, 1, 'F', '1234')
    
    pdf.rounded_rect(1, 274, 214, 5, 2, 'F', '1234')
    ruta_b='{}static/img/cabecera_boletin_dirop.png'.format(filtro[15])

    pdf.image(ruta_b,0,0,220,30)#imagenes 

    ruta_b='{}static/img/jemop.png'.format(filtro[15])
    pdf.image(ruta_b,205,0.2,10,10)#imagenes 

    ruta_b='{}static/img/cuadro.png'.format(filtro[15])
    pdf.image(ruta_b,62,35.5,13,4.5)#imagenes 

    ruta_b='{}static/img/cuadro_dos.png'.format(filtro[15])
    pdf.image(ruta_b,151,35.5,13,4.5)#imagenes 

    ruta_b='{}static/img/cuadro.png'.format(filtro[15])
    pdf.image(ruta_b,0,274.5,13,4.5)#imagenes 

    ruta_b='{}static/img/cuadro_dos.png'.format(filtro[15])
    pdf.image(ruta_b,204,274.5,13,4.5)#imagenes 


    pdf.set_fill_color(104, 76, 64)

    #-------------------------------------------------------------
    #-------------------------------titulo---------------------
    #-------------------------------------------------------------

    pdf.set_fill_color(20, 61, 51)#color de rellenos
    pdf.set_text_color(255,255,255)#color de textos

    pdf.set_font('Arial', 'B', 14)#tipografia de la fuente
    pdf.text(78, 38, 'AFECTACIÓN A LA AMENAZA')#titulo

    pdf.set_font('Arial', 'B', 11)#tipografia de la fuente de los textos
    pdf.text(85, 278, 'PATRIA HONOR LEALTAD')

    #-------------------------------------------------------------
    #-----------------------------sub titulo----------------------
    #-------------------------------------------------------------


    pdf.set_fill_color(17, 63, 52)
    pdf.set_text_color(255,255,255)#color de textos

    pdf.rounded_rect(104, 168, 108, 5, 2, 'F', '1234')
    pdf.rounded_rect(104, 218, 108, 5, 2, 'F', '1234')
    pdf.rounded_rect(104, 243, 108, 5, 2, 'F', '1234')

    pdf.rounded_rect(1, 168, 103, 5, 2, 'F', '1234')
    pdf.rounded_rect(1, 211.5, 103, 5, 2, 'F', '1234')

    # pdf.set_fill_color(20, 61, 51)#color de rellenos

    pdf.set_font('Arial', 'B', 10)#tipografia de la fuente

    pdf.text(130, 172, 'AFECTACIÓN MINERÍA CRIMINAL')#titulo
    pdf.text(109.5, 222, 'NEUTRALIZACIÓN A.E, MAP Y ACCIONES TERRORISTAS')#titulo
    pdf.text(135, 247, 'NEUTRALIZACIÓN EXPLOSIVOS')#titulo

    pdf.text(5, 172, 'AFECTACIÓN NARCOTRÁFICO (José Inocencio Chincá)')#titulo
    
    pdf.set_font('Arial', 'B', 9.5)#tipografia de la fuente
    pdf.text(2, 215, 'AFECTACIÓN ECONOMIAS ILÍCITAS (Pedro Pascasio Martínez)')#titulo

#lineas boletin boletin
def lineas_boletin_dirop(pdf):
    
    #bloque para crear lineas verticales de los resultados
    pdf.line(159, 41.5, 159, 157)#linea vertical 
    pdf.line(174, 41.5, 174, 157)#linea vertical 
    pdf.line(188, 41.5, 188, 157)#linea vertical 
    
    #bloque para crear lineas verticales de los resultados
    pdf.line(159, 174, 159, 265)#linea vertical 
    pdf.line(174, 174, 174, 265)#linea vertical 
    pdf.line(188, 174, 188, 265)#linea vertical 

    #bloque para crear lineas verticales de los resultados
    pdf.line(40, 174, 40, 230)#linea vertical 
    pdf.line(55, 174, 55, 230)#linea vertical 
    pdf.line(69, 174, 69, 230)#linea vertical 

#funcion para la creacion de cuadros
def cuadro_resultados(pdf, resultados):

                    

    no = 1
    numero = 5
    posicion_inicial = pdf.get_y()
    for resultado in resultados:

        pdf.set_line_width(0.1)
        pdf.set_fill_color(193, 30, 38)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial', 'B', 12)

        coordenada_n = conversor_de_cordenadas(resultado[16],1)
        coordenada_w = conversor_de_cordenadas(resultado[17],-1)
        pdf.ln(numero)

        coodenadas = "N " +str(coordenada_n)+" W "+str(coordenada_w)
        inicial = pdf.get_y() 
        if inicial >= 195:
            pdf.ln(10)

        pdf.cell(25, 5, "No.", 1,0, "C", True)
        pdf.cell(50, 5, "DIVISIÓN", 1,0, "C", True)
        pdf.cell(50, 5, "BRIGADA", 1,0, "C", True)
        pdf.cell(50, 5, "BATALLÓN", 1,0, "C", True)
        pdf.cell(50, 5, "DEPARTAMENTO", 1,0, "C", True)
        pdf.cell(50, 5, "MUNICIPIO", 1,0, "C", True)
        pdf.cell(60, 5, "COORDENADAS" , 1,0, "C", True)
        pdf.ln(5)

        y = pdf.get_y()    
        pdf.set_font('Arial', '', 9)
        pdf.set_text_color(0,0,0)

        pdf.multi_cell(25,5,str(no),0,"C", False )
        x_1 = pdf.get_y()
        a = (x_1-y)
        pdf.ln(-a)
        pdf.cell(25)
        pdf.multi_cell(50,5,resultado[2],0,"C", False )
        x_2 = pdf.get_y()
        b = (x_2-y)
        pdf.ln(-b)
        pdf.cell(75)
        pdf.multi_cell(50,5,resultado[4],0,"C", False )
        x_3 = pdf.get_y()
        c = (x_3-y)
        pdf.ln(-c)
        pdf.cell(125)
        pdf.multi_cell(50,5,resultado[5],0,"C", False )
        x_4 = pdf.get_y()
        d = (x_4-y)
        pdf.ln(-d)
        pdf.cell(175)
        pdf.multi_cell(50,5,resultado[6],0,"C", False )
        x_5 = pdf.get_y()
        e = (x_5-y)
        pdf.ln(-d)
        pdf.cell(225)
        pdf.multi_cell(50,5,resultado[7],0,"C", False )
        x_6 = pdf.get_y()
        f = (x_6-y)
        pdf.ln(-f)
        pdf.cell(275)
        pdf.multi_cell(60,5,coodenadas,0,"C", False )
        x_7 = pdf.get_y()
        g = (x_7-y)
        pdf.ln(-g)


        altura = [a, b, c, d, e, f,g]
        linea = [x_1, x_2, x_3, x_4, x_5, x_6, x_7]
        numero = funcion_mayor(altura)
        linea = funcion_mayor(linea)
        
        if linea >= 195:
            pdf.ln(10)

        # pdf.line(10, linea, 345, linea)
        # pdf.line(10, altura, 345, altura)
        

        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial', 'B', 12)
        pdf.ln(numero)
        pdf.cell(90, 5, "LOO / LOE", 1,0, "C", True)
        pdf.cell(155, 5, "HECHOS", 1,0, "C", True)
        pdf.cell(90, 5, "IMPACTO", 1,0, "C", True)
        pdf.ln(5)

        y = pdf.get_y()    

        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', '', 9)

        pdf.multi_cell(90,5,resultado[15],0,"C", False )
        x_1 = pdf.get_y()
        a = (x_1-y)
        pdf.ln(-a)

        pdf.cell(245)
        pdf.multi_cell(90,5,resultado[9],0,"C", False )
        x_3 = pdf.get_y()
        c = (x_3-y)

        pdf.ln(-c)

        pdf.cell(90)
        pdf.multi_cell(155,5,resultado[19],0,"J", False )
        x_2 = pdf.get_y()
        b = (x_2-y)

        altura_2 = [a, b, c]
        numero = funcion_mayor(altura_2)

         
        linea = [x_1, x_2, x_3]
        linea = funcion_mayor(linea)
  
  
        if x_1 < x_2:
            pdf.ln(-b)
            pdf.line(10, linea, 345, linea)


            pdf.ln(5)
            
        else:
            ln = 40
            ln = x_2 - ln
            pdf.line(10, x_2, 345, x_2)
            pdf.ln()



        
        no = no + 1

#funcion para calcular las afectaciones del enemigo cuadro
def funcion_celda_comparativa(pdf,dato_ant, dato_act, ruta, flecha, posi, celda, conts, fill):
        dato_por = porcentajes(dato_ant, dato_act, conts)

        dato_ant = formato_numero(dato_ant)
        dato_act = formato_numero(dato_act)
        
        pdf.cell(celda[0],5,str(dato_ant),0,0, 'C',fill)
        pdf.cell(celda[0],5,str(dato_act),0,0, 'C',fill)
   
        if dato_por > 0:
            pdf.set_text_color(0,128,0)
            triangulo = '{}static/img/tri_verde_new.png'.format(ruta)

        elif dato_por < 0:
            pdf.set_text_color(128,0,0)
            triangulo = '{}static/img/tri_rojo_new.png'.format(ruta)

        else:
            pdf.set_text_color(232,172,2)
            triangulo = '{}static/img/tri_amarillo_new.png'.format(ruta)

        
        if dato_ant == "-" and dato_act == "-":
            dato_por = "-"
        else:
            dato_por = formato_numero_decimal(dato_por)

        pdf.cell(celda[1],5,str(dato_por),0,0, 'R',fill)
        pdf.set_text_color(0,0,0)
        pdf.image(triangulo,posi,flecha,2.25,2.25)#imagenes 

#cuadro comparativo de menores de edad
def cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, enemigo, gao, gao_1, gao_2, ruta, flecha):

    rme_resul_ant = calculo_tres_b(datos_res_ant, gao, gao_1, gao_2, 7, 18)
    rme_resul_act = calculo_tres_b(datos_res_actu, gao, gao_1, gao_2, 7, 18)
    
    dato_ant_1 = formato_numero(rme_resul_ant)
    dato_act_1 = formato_numero(rme_resul_act)

    if dato_ant_1 != "-" or dato_act_1 != "-" :
        pdf.ln(5)
        pdf.cell(-8.5)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(14.5,5,str(enemigo),0,0, 'L',False)
        pdf.set_font('Arial', '', 9)

        celda = [11,12.5]
        funcion_celda_comparativa(pdf,rme_resul_ant, rme_resul_act, ruta, flecha, 38.5, celda, 1, False)

                        
        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 49
        a = 2
        while a < lineas:
            pdf.line(a, flecha+4, a+1, flecha+4)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        return 5
    else:
        return 0
    
#cuadro comparativo de menores de edad
def cuadro_menores_edad_comparativo(pdf, datos_res_ant, datos_res_actu, filtro, anio_act, anio_ant):

    rme_resul_1 = calculo_total_sin_filtro_b(datos_res_actu, 18)
    rme_resul_ant_1 = calculo_total_sin_filtro_b(datos_res_ant, 18)

    ruta = filtro[15]
    # formato_numero(numero_ant)
    
    rme_resul_act = formato_numero(rme_resul_1)
    rme_resul_ant = formato_numero(rme_resul_ant_1)

    pdf.ln(5)
    pdf.set_line_width(0.1)
    pdf.set_fill_color(193, 30, 38)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 10)

    posicion = 0
    pdf.cell(-8.5)

    if rme_resul_act != "-" or rme_resul_ant != "-":
        flecha = 46.25
        pdf.cell(14.5,5,"ENE.",0,0, 'C',True)
        pdf.cell(11,5,anio_ant,0,0, 'C',True)
        pdf.cell(11,5,anio_act,0,0, 'C',True)
        pdf.cell(12.5,5,"%",0,0, 'C',True)
        pdf.set_text_color(0,0,0)

        posicion = 5 + posicion
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", ruta, flecha)
        posicion = posi + posicion   
        flecha = flecha + posi     
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "GDO","GDO","GDO","GDO", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "NARCO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_men_res_comparativo(pdf, datos_res_ant, datos_res_actu, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", ruta, flecha)
        posicion = posi + posicion
        flecha = flecha + posi

        pdf.set_fill_color(217, 217, 217)
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        pdf.cell(-8.5)
        pdf.cell(14.5,5,"TOTAL",0,0, 'C',True)

        celda = [11,12.5]
        funcion_celda_comparativa(pdf,rme_resul_ant_1, rme_resul_1, ruta, flecha, 38.5, celda, 1, True)
        posicion = 5 + posicion
       
        pdf.ln(5)

    return [posicion+5, rme_resul_ant_1, rme_resul_1]

def cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_act, enemigo, gao, gao_1, gao_2, ruta, flecha, filtro):

    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 0, "NO") #funcion para filtar el spoa
    pre_ant = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 1, "NO") #funcion para filtar el spoa
    some_ant = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 2, "SI") #funcion para filtar el spoa
    capt_ant = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 3, "SI") #funcion para filtar el spoa
    mdom_ant = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_act, 0, "NO") #funcion para filtar el spoa
    pre_act = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_act, 1, "NO") #funcion para filtar el spoa
    some_act = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_act, 2, "NO") #funcion para filtar el spoa
    capt_act = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_act, 3, "NO") #funcion para filtar el spoa
    mdom_act = calculo_tres_b(valor_calculado_act[0], gao, gao_1, gao_2, 7, 18)
 
    total_ant_1 = pre_ant + some_ant + capt_ant + mdom_ant
    total_act_1 = pre_act + some_act + capt_act + mdom_act

    total_ant = formato_numero(total_ant_1)

    total_act = formato_numero(total_act_1)


    if total_ant != "-" or total_act != "-":

        pdf.ln(5)
        pdf.cell(41.5)
        pdf.set_font('Arial', 'B', 8)
        pdf.cell(14.5,5,str(enemigo),0,0, 'L',False)
        pdf.set_font('Arial', '', 9)
        celda = [11.2,12.1]

        funcion_celda_comparativa(pdf,pre_ant, pre_act, ruta, flecha, 89, celda,1, False)
        funcion_celda_comparativa(pdf,some_ant, some_act, ruta,  flecha, 123.5, celda,1, False)
        funcion_celda_comparativa(pdf,capt_ant, capt_act, ruta,  flecha, 158, celda,1, False)
        funcion_celda_comparativa(pdf,mdom_ant, mdom_act, ruta,  flecha, 192.5, celda,1, False)
        funcion_celda_comparativa(pdf,total_ant_1, total_act_1, ruta,  flecha, 227, celda,1, False)

                                
        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 238
        a = 52
        while a < lineas:
            pdf.line(a, flecha+4, a+1, flecha+4)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        return 5
    else:
        return 0
def cuadro_enemigo_afectaciones_comparativo(pdf,posicion_inicial, datos_res_ant, datos_res_actu, filtro, anio_act, anio_ant):

    # posicion_inicial = pdf.get_x()
    ruta = filtro[15]
    flecha = 46.25
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 0, "NO") #funcion para filtar el spoa
    pre_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 1, "NO") #funcion para filtar el spoa
    some_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 2, "SI") #funcion para filtar el spoa
    capt_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_ant, 3, "SI") #funcion para filtar el spoa
    mdom_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)

    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_actu, 0, "NO") #funcion para filtar el spoa
    pre_act = calculo_total_sin_filtro_b(valor_calculado_act[0], 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_actu, 1, "NO") #funcion para filtar el spoa
    some_act = calculo_total_sin_filtro_b(valor_calculado_act[0], 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_actu, 2, "SI") #funcion para filtar el spoa
    capt_act = calculo_total_sin_filtro_b(valor_calculado_act[0], 18)
    valor_calculado_act = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_actu, 3, "SI") #funcion para filtar el spoa
    mdom_act = calculo_total_sin_filtro_b(valor_calculado_act[0], 18)

    total_ant_1 = pre_ant + some_ant + capt_ant + mdom_ant
    
    total_act_1 = pre_act + some_act + capt_act + mdom_act


    total_act = formato_numero(total_act_1)
    total_ant = formato_numero(total_ant_1)

    posicion = 0
    if total_ant != "-" or total_act != "-":
        
        pdf.ln(-posicion_inicial)
        pdf.set_line_width(0.1)
        pdf.set_fill_color(193, 30, 38)
        pdf.set_draw_color(217, 217, 217)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial', 'B', 10)

        pdf.cell(41.5)

        pdf.cell(14.5,10,"ENE.",0,0, 'C',True)
        pdf.cell(34.5,5,"PRE. VOLUNTARIA",0,0, 'C',True)

        pdf.cell(34.5,5,"SOMETIMIENTOS",0,0, 'C',True)
        pdf.cell(34.5,5,"CAPTURAS",0,0, 'C',True)
        pdf.cell(34.5,5,"MDOM",0,0, 'C',True)
        pdf.cell(34.5,5,"TOTAL",0,0, 'C',True)
       
        posicion = 5 + posicion
        pdf.set_font('Arial', '', 9)

        pdf.ln()
        pdf.cell(56)
        pdf.cell(11.2,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(11.2,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.1,5,"%",1,0, 'C',True)

        pdf.cell(11.2,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(11.2,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.1,5,"%",1,0, 'C',True)

        pdf.cell(11.2,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(11.2,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.1,5,"%",1,0, 'C',True)

        pdf.cell(11.2,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(11.2,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.1,5,"%",1,0, 'C',True)

        pdf.cell(11.2,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(11.2,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.1,5,"%",1,0, 'C',True)

        pdf.set_text_color(0,0,0)

        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi
        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi

        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", ruta, flecha, filtro)
        posicion = posi + posicion  
        flecha = flecha + posi
              
        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi

        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "GDO","GDO","GDO","GDO", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi

        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "NARCO.","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi

        posi = cuadro_afect_enemigo_com(pdf, datos_res_ant, datos_res_actu, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", ruta, flecha, filtro)
        posicion = posi + posicion
        flecha = flecha + posi
        pdf.set_fill_color(217, 217, 217)
        pdf.set_font('Arial', 'B', 10)
        pdf.ln (5)
        pdf.cell(41.5)
        pdf.cell(14.5,5,"TOTAL",0,0, 'C',True)
        celda = [11.2,12.1]
        funcion_celda_comparativa(pdf,pre_ant, pre_act, ruta, flecha, 89, celda,1, True)
        funcion_celda_comparativa(pdf,some_ant, some_act, ruta,  flecha, 123.5, celda,1, True)
        funcion_celda_comparativa(pdf,capt_ant, capt_act, ruta,  flecha, 158, celda,1, True)
        funcion_celda_comparativa(pdf,mdom_ant, mdom_act, ruta,  flecha, 192.5, celda,1, True)
        funcion_celda_comparativa(pdf,total_ant_1, total_act_1, ruta,  flecha, 227, celda,1, True)

        posicion = 10 + posicion

        pdf.ln (5)

    return [posicion, total_ant_1, total_act_1]

#funcion para calcular las afectaciones del enemigo cuadro
def cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, enemigo, gao, gao_1, gao_2, ruta, flecha, filtro):
    
    if gao != "NO APLICA":
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 0, "SI") #funcion para filtar el spoa
        ases_ant = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 0, "SI") #funcion para filtar el spoa
        ases_act = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)

        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 1, "SI") #funcion para filtar el spoa
        heridos_ant = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 1, "SI") #funcion para filtar el spoa
        heridos_act = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)
    else:
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 2, "NO") #funcion para filtar el spoa
        ases_ant = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 2, "NO") #funcion para filtar el spoa
        ases_act = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)

        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 3, "NO") #funcion para filtar el spoa
        heridos_ant = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)
        valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 3, "NO") #funcion para filtar el spoa
        heridos_act = calculo_tres_b(valor_calculado_ant[0], gao, gao_1, gao_2, 7, 18)

    total_ant_1 = ases_ant + heridos_ant 
    total_act_1 = ases_act + heridos_act 


    total_ant = formato_numero(total_ant_1)
    total_act = formato_numero(total_act_1)
    
    if total_ant != "-" or total_act != "-":
        pdf.ln(5)
        pdf.cell(229.5)
        pdf.set_font('Arial', 'B', 6)
        pdf.cell(15,5,str(enemigo),0,0, 'L',False)
        pdf.set_font('Arial', '', 9)

        celda = [10,12.5]
        funcion_celda_comparativa(pdf, ases_ant, ases_act, ruta, flecha, 275.5, celda, -1, False)
        funcion_celda_comparativa(pdf, heridos_ant, heridos_act, ruta, flecha, 309, celda, -1, False)
        funcion_celda_comparativa(pdf, total_ant_1, total_act_1, ruta, flecha, 342.5, celda, -1, False)

        #---------------------------------
        pdf.set_draw_color(140, 140, 140)
        pdf.set_line_width(0.3)
        lineas = 354
        a = 240
        while a < lineas:
            pdf.line(a, flecha+4, a+1, flecha+4)
            a = a+2

        pdf.set_line_width(0.5)
        pdf.set_draw_color(0, 0, 0)
        #---------------------------------

        return 5
    else:
        return 0

def cuadro_afectaciones_tropas_combate_comparativo (pdf, posicion_inicial, datos_res_afectaciones_ant, datos_res_afectaciones_act, filtro, anio_act, anio_ant ):

    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 0, "SI") #funcion para filtar el spoa
    asesinados_act = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_act, 1, "SI") #funcion para filtar el spoa
    heridos_act = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)

    muertos_fuera_act = calculo_total_sin_filtro_b(datos_res_afectaciones_act[2], 18)
    heridos_fuera_act = calculo_total_sin_filtro_b(datos_res_afectaciones_act[3], 18)

    asesinados_act = asesinados_act + muertos_fuera_act
    heridos_act = heridos_act + heridos_fuera_act

    total_act_1 = asesinados_act + heridos_act 

    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 0, "SI") #funcion para filtar el spoa
    asesinados_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)
    valor_calculado_ant = Calculo_Spoa.validar_spoa_unidad(filtro, datos_res_afectaciones_ant, 1, "SI") #funcion para filtar el spoa
    heridos_ant = calculo_total_sin_filtro_b(valor_calculado_ant[0], 18)

    muertos_fuera_ant = calculo_total_sin_filtro_b(datos_res_afectaciones_ant[2], 18)
    heridos_fuera_ant = calculo_total_sin_filtro_b(datos_res_afectaciones_ant[3], 18)

    asesinados_ant = asesinados_ant + muertos_fuera_ant
    heridos_ant = heridos_ant +heridos_fuera_ant

    total_ant_1 = asesinados_ant + heridos_ant 

    total_act = formato_numero(total_act_1)
    total_ant = formato_numero(total_ant_1)

    ruta = filtro[15]
    flecha = 46.25
    posicion = 0
    if total_act != "-" or total_ant != "-":
        pdf.ln(-posicion_inicial)
        pdf.set_line_width(0.1)
        pdf.set_fill_color(193, 30, 38)
        pdf.set_draw_color(217, 217, 217)
        pdf.set_text_color(255,255,255)
        pdf.set_font('Arial', 'B', 10)

        pdf.cell(229.5)

        pdf.cell(14.5,10,"ENE.",0,0, 'C',True)
        pdf.cell(33.5,5,"ASESINADOS",0,0, 'C',True)
        pdf.cell(33.5,5,"HERIDOS",0,0, 'C',True)
        pdf.cell(33.5,5,"TOTAL",0,0, 'C',True)

        pdf.ln()
        pdf.cell(244)
        pdf.cell(10.5,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(10.5,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.5,5,"%",1,0, 'C',True)

        pdf.cell(10.5,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(10.5,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.5,5,"%",1,0, 'C',True)
        
        pdf.cell(10.5,5,str(anio_ant),1,0, 'C',True)
        pdf.cell(10.5,5,str(anio_act),1,0, 'C',True)
        pdf.cell(12.5,5,"%",1,0, 'C',True)

        pdf.set_text_color(0,0,0)

        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "GAO-ELN", "GAO ELN", "GAO ELN", "GAO ELN", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "GAO-r", "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC",ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "GAO-CG", "GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO","GAO CLAN DEL GOLFO", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "GAO-CAP", "GAO CAPARROS","GAO CAPARROS","GAO CAPARROS", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion    
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act,"GAO-PEL", "GAO PELUSOS","GAO PELUSOS","GAO PELUSOS", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "GDO","GDO","GDO","GDO", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "NARCO","NARCOTRÁFICO","NARCOTRÁFICO","NARCOTRÁFICO", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "DELCO","DELINCUENCIA","DELINCUENCIA","DELINCUENCIA", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pos = cuadro_afectaciones_tropas_comparativo(pdf, datos_res_afectaciones_ant, datos_res_afectaciones_act, "DIF. AMENA.","NO APLICA","NO APLICA","NO APLICA", ruta, flecha, filtro)
        flecha = flecha + pos
        posicion = pos + posicion
        pdf.set_font('Arial', 'B', 10)
        pdf.ln(5)
        pdf.cell(229.5)


        pdf.set_fill_color(217, 217, 217)
        pdf.cell(14.5,5,"TOTAL",0,0, 'C',True)
        



        celda = [10.5,12.5]
        funcion_celda_comparativa(pdf, asesinados_ant, asesinados_act, ruta, flecha, 275.5, celda, -1, True)
        funcion_celda_comparativa(pdf, heridos_ant, heridos_act, ruta, flecha, 309, celda, -1, True)
        funcion_celda_comparativa(pdf, total_ant_1, total_act_1, ruta, flecha, 342.5, celda, -1, True)
        pdf.ln()
    
        posicion = posicion + 15
    else:
        posicion = posicion_inicial

    return [posicion, total_ant, total_act]


#funcion para el grupo de resultados comparativos para la lamina de los muñecos
def grupo_result_resal_comparativa_dos (pdf, pos_vert, pos, elemento, datos_res_ant, datos_res_act, porcentaje, imagen, filtro, const):

    dato_por = -25

    posi = pos - pos_vert[12]

    ruta = '{}static/img/resultados/'.format(filtro[15])
    resultado_ant = datos_res_ant
    resultado_act = datos_res_act
    
    dato_por = porcentaje
    
    # resultado_act = formato_numero(resultado_act)
    # resultado_ant = formato_numero(resultado_ant)

    

    direccion = str(ruta) + str(imagen)
    altura = pos + pos_vert[7]
    # if resultado != "-":
    pdf.cell(pos_vert[1])
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.image(direccion,pos_vert[0], pos+2,5,5)

    pdf.cell(pos_vert[2],6,str(elemento),0,0, 'L',False)
    pdf.cell(pos_vert[3],6,str(resultado_ant),0,0, 'C',False)
    pdf.cell(pos_vert[3],6,str(resultado_act),0,0, 'C',False)

    if dato_por > 0:
        pdf.set_text_color(0,128,0)
        triangulo = '{}static/img/tri_verde_new.png'.format(filtro[15])

    elif dato_por < 0:
        pdf.set_text_color(128,0,0)
        triangulo = '{}static/img/tri_rojo_new.png'.format(filtro[15])

    else:
        pdf.set_text_color(232,172,2)
        triangulo = '{}static/img/tri_amarillo_new.png'.format(filtro[15])

    dato_por = formato_numero(dato_por)

        
    pdf.image(triangulo,pos_vert[11],posi,2.25,2.25)#imagenes 


    pdf.cell(pos_vert[4],6,str(dato_por),0,0, 'R',False)
    pdf.set_text_color(0,0,0)

    a = pos_vert[5]
    
    
    #---------------------------------
    pdf.set_draw_color(140, 140, 140)
    pdf.set_line_width(0.3)
    lineas = pos_vert[11]+15
    a = pos_vert[0]+10
    while a < lineas:
        pdf.line(a, pos+2, a+1, pos+2)
        a = a+2

    pdf.set_line_width(0.5)
    pdf.set_draw_color(0, 0, 0)
    #---------------------------------

    # while a < pos_vert[6]:
    #     pdf.line(a, altura, a+1, altura)
    #     a = a+3

    pdf.ln()
    pos = pos + 6
    
    # else:
    #     pdf.ln(-6)
        
        

    return pos

#funcion para el grupo de resultados comparativos para la lamina de los muñecos
def grupo_result_resal_comparativa (pdf, pos_vert, pos, elemento, datos_res_ant, datos_res_act, suma, imagen, filtro, const):

    dato_por = -25

    posi = pos - pos_vert[12]

    ruta = '{}static/img/resultados/'.format(filtro[15])
    resultado_ant = calculo_total_sin_filtro_b(datos_res_ant, suma)
    resultado_act = calculo_total_sin_filtro_b(datos_res_act, suma)
    
    
    dato_por = porcentajes(resultado_ant, resultado_act, const)
    
    resultado_act = formato_numero(resultado_act)
    resultado_ant = formato_numero(resultado_ant)

    

    direccion = str(ruta) + str(imagen)
    altura = pos + pos_vert[7]
    
    # if resultado != "-":
    pdf.cell(pos_vert[1])
    pdf.set_font('Arial', '', 10)
    pdf.set_text_color(0, 0, 0)
    pdf.image(direccion,pos_vert[0], pos-2,5,5)

    pdf.cell(pos_vert[2],5,str(elemento),0,0, 'L',False)
    pdf.cell(pos_vert[3],5,str(resultado_ant),0,0, 'C',False)
    pdf.cell(pos_vert[3],5,str(resultado_act),0,0, 'C',False)

    if dato_por > 0:
        pdf.set_text_color(0,128,0)
        triangulo = '{}static/img/tri_verde_new.png'.format(filtro[15])

    elif dato_por < 0:
        pdf.set_text_color(128,0,0)
        triangulo = '{}static/img/tri_rojo_new.png'.format(filtro[15])

    else:
        pdf.set_text_color(232,172,2)
        triangulo = '{}static/img/tri_amarillo_new.png'.format(filtro[15])

    dato_por = formato_numero(dato_por)

        
    pdf.image(triangulo,pos_vert[11],posi,2.25,2.25)#imagenes 


    pdf.cell(pos_vert[4],5,str(dato_por),0,0, 'R',False)
    pdf.set_text_color(0,0,0)

        
    
    #---------------------------------
    pdf.set_draw_color(140, 140, 140)
    pdf.set_line_width(0.3)
    lineas = pos_vert[11]+16
    a = pos_vert[0]+10
    while a < lineas:
        pdf.line(a, pos+2, a+1, pos+2)
        a = a+2

    pdf.set_line_width(0.5)
    pdf.set_draw_color(0, 0, 0)
    #---------------------------------

    # while a < pos_vert[6]:
    #     pdf.line(a, altura, a+1, altura)
    #     a = a+3

    pdf.ln()
    pos = pos + 5
    
    # else:
    #     pdf.ln(-6)
        
        

    return pos

def titulo_comparatibo_muñecos(pdf, pos_vert, pos, anio_ant, anio_act, text, filtro, largo ):
        
        ruta = '{}static/img/resultados/'.format(filtro[15])
        final = str(ruta) + str("triangulo_titulo_ayuda.png")
        pdf.image(final,pos_vert[0]+3,pos-3,3.5,4)
        
        pdf.set_fill_color(193, 31, 37)
        pdf.rounded_rect(pos_vert[0]+8, pos-4, largo, 5, 1,'F', '1234')

        pdf.set_font('Arial', 'B', 10)
        pdf.set_text_color(255, 255, 255)
        pdf.text(pos_vert[0]+9, pos, text )
        pdf.text(pos_vert[8], pos, anio_ant )
        pdf.text(pos_vert[9], pos, anio_act )
        pdf.text(pos_vert[10], pos, "%" )
        pdf.set_fill_color(0, 0, 0)
        pdf.set_line_width(0.5)
        pdf.line(pos_vert[0]+8, pos-4, pos_vert[6]+1, pos-4)
        # pdf.line(pos_vert[0], pos+1, pos_vert[6], pos+1)
        pdf.set_line_width(0.3)
        pdf.set_fill_color(0, 0, 0)

#El presente bloque de las funciones es para crear la cartilla diaria de las divisiones 
#resultados con enemigo
def res_afectaciones(pdf, datos, division, enemigo_evaluar, posicion_division, suma, evento, celdas):

    datos_division = list(filter(lambda datos: division in datos[posicion_division], datos))
    enemigo = []

    celda = celdas[1]
    posicion = celdas[2]
    cell = celdas[3]

    for dato in datos_division:
        # print(dato[7])
        if  dato[7] not in enemigo:
            enemigo.append(dato[7])
    valor_retorno = celdas[0]
    
    for ene in enemigo:
        if ene != enemigo_evaluar:        
            numero = 0
            for  datos in datos_division:
                if datos[7] == ene:
                    numero =  numero + float(datos[suma])
                    
            if valor_retorno < 10:
                valor_retorno = valor_retorno + 1
                numero = formato_numero(numero)
                if ene == "GAO CLAN DEL GOLFO":
                    ene = "GAO-CG"
                if ene == "GAO - Residual Disidencias FARC":
                    ene = "GAO-r"

                # valor = "* "+ str(numero) + " - "+ str(evento) + " (" + str(ene)+ ")"
                texto = str(evento) + " (" + str(ene)+ ")"
                # print(texto)
                pdf.set_text_color(0,0,0)
                pdf.set_font('Arial', 'B', 8)

                pdf.cell(cell)
                pdf.cell(45,4,str(texto),0,0, 'L',False)
                pdf.cell(17,4,str(numero),0,0, 'R',False)
                pdf.ln()

                celda = celda +4

                # print(valor)

    return [valor_retorno, celda]
#resultados sin enemigo
def res_afectaciones_sin_enemigo(pdf, datos, division, enemigo_evaluar, posicion_division, suma, evento, celdas):
    celda = celdas[1]
    posicion = celdas[2]
    cell = celdas[3]

    datos_division = list(filter(lambda datos: division in datos[posicion_division], datos))
    enemigo = []

    valor_retorno = celdas[0]
    numero = 0
    
    if datos_division:
        for  datos in datos_division:
            if datos[7] != enemigo_evaluar:
                numero =  numero + float(datos[suma])  
        valor_retorno = valor_retorno + 1

        if evento == "Kg Cocaína" or evento == "Kg Marihuana" or evento == "Kg P.B.C":

            numero = formato_numero(numero)
            
        else:
            numero = formato_numero(numero)
            
        
        # valor = "° "+str(numero) + " - "+ str(evento)
        valor = "* "+str(numero) + " - "+ str(evento)
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 8)
        # pdf.text(posicion,celda,str(valor))

        texto = str(evento) 
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 8)

        pdf.cell(cell)
        pdf.cell(45,4,str(texto),0,0, 'L',False)
        pdf.cell(17,4,str(numero),0,0, 'R',False)
        pdf.ln()
        
        celda = celda +4
    # print(valor)

    return [valor_retorno, celda]

def llamado_afectacion(pdf, dato, division, enemigo, num_di, suma, evaluacion, numeros):
    numero = numeros[0]
    celda = numeros[1]
    posicion = numeros[2]
    cell = numeros[3]
    if numero <= 10:
        res = res_afectaciones(pdf, dato, division, enemigo, num_di, suma, evaluacion, numeros)
        numero = res[0]
        celda = res[1]

        # print("----y")
        # print(numero)
        
    return [numero, celda, posicion, cell]

def llamado_afectacion_sin_enemigo(pdf, dato, division, enemigo, num_di, suma, evaluacion, numeros):
    numero = numeros[0]
    celda = numeros[1]
    posicion = numeros[2]
    cell = numeros[3]

    if numero < 10:
        res = res_afectaciones_sin_enemigo(pdf, dato, division, enemigo, num_di, suma, evaluacion, numeros)
        
        numero = res[0]
        celda = res[1]
        # print("----x")
        # print(numero)
    return [numero, celda, posicion, cell]
def resultados_diarios_divisiones_coe(pdf, res_calculo_act, division, posiciones):

    numeros = 0 #numero matriz que me permite avanzar en los grupos 
    celda = posiciones[0]
    posicion = posiciones[1]
    ln=posiciones[2]
    cell=posiciones[3]

    numero=[numeros, celda, posicion, cell]

    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)
    pdf.text(posicion+25,celda-6.25,division)
    pdf.set_font('Arial', 'B', 8)
    pdf.ln(ln)
    # pdf.cell(5)
    
    #menores
    numero = llamado_afectacion(pdf, res_calculo_act[0], division, "NO APLICA", 1, 18, "RME", numero)

    #PRESEMTACIONES 
    numero = llamado_afectacion(pdf, res_calculo_act[1], division, "NO APLICA", 1, 18, "Pres. Volt.", numero)
    #SOMETETIMIENTOS
    numero = llamado_afectacion(pdf, res_calculo_act[2], division, "NO APLICA", 1, 18, "Sometimientos.", numero)
    #CAPTURAS
    numero = llamado_afectacion(pdf, res_calculo_act[3], division, "NO APLICA", 1, 18, "Captura", numero)
    #MDOM
    numero = llamado_afectacion(pdf, res_calculo_act[4], division, "NO APLICA", 1, 18, "MDOM", numero)

    #ASESINADOS
    numero = llamado_afectacion(pdf, res_calculo_act[5], division, "NO APLICA", 1, 18, "Asesinado", numero)
    #HERIDOS
    numero = llamado_afectacion(pdf, res_calculo_act[6], division, "NO APLICA", 1, 18, "Herido", numero)

    #COCAINA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[93], division, "", 1, 18, "Muerto DIF Amenaza", numero)
    #COCAINA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[94], division, "", 1, 18, "Herido DIF Amenaza", numero)
    #COCAINA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[21], division, "", 1, 18, "Kg Cocaína", numero)
    #MARIHUANA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[22], division, "", 1, 18, "Kg Marihuana", numero)
    #MARIHUANA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[23], division, "", 1, 18, "Kg P.B.C", numero)
    #Laboratorios de Cocaína
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[24], division, "", 1, 18, "Laboratorios de Cocaína", numero)
    #Laboratorios de PBC
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[25], division, "", 1, 18, "Laboratorios de PBC", numero)
    #Semilleros
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[26], division, "", 1, 18, "Semilleros", numero)

    #Depósito Ilegal
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[46], division, "", 1, 18, "Depósito Ilegal", numero)

    #Armas de Largo Alcance
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[7], division, "", 1, 18, "Armas de Largo Alcance", numero)
    #Armas de Corto Alcance
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[8], division, "", 1, 18, "Armas de Corto Alcance", numero)
    #Armas de Acompañamiento
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[9], division, "", 1, 18, "Armas de Acompañamiento", numero)
    #Municiones
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[10], division, "", 1, 18, "Municiones", numero)

    #Neutralización AE
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[16], division, "", 1, 18, "Neutralización AE", numero)
    #Neutralización MAP
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[17], division, "", 1, 18, "Neutralización MAP", numero)
    #Explosivos Destruidos kg 
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[18], division, "", 1, 18, "Kg Explosivos Destruidos", numero)
    #Cordón Detonante m
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[19], division, "", 1, 18, "Cordón Detonante m", numero)
    #Mecha Lenta m
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[20], division, "", 1, 18, "Mecha Lenta m", numero)
    #Neutralización Terrorista
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[15], division, "", 2, 14, "Neutralización Terrorista", numero)

    #Combates
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[14], division, "", 2, 14, "Combates", numero)
    
    #ATAQUE FUERZA PUBLICA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[64], division, "", 2, 14, "Ataque Fuerza Publica", numero)

    #Ataque UAS
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[95], division, "", 1, 18, "Ataque UAS", numero)

    #Ataque UAS
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[96], division, "", 1, 18, "Neutralización UAS", numero)

    #Liberados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[42], division, "", 1, 18, "Liberados", numero)
    #Rescatados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[43], division, "", 1, 18, "Rescatados", numero)
    #Válvulas Ilícitas Destruidas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[44], division, "", 1, 18, "Válvulas Ilícitas Destruidas", numero)
    #Refinerias Ilegales Destruidas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[45], division, "", 1, 18, "Refinerias Ilegales Destruidas", numero)
    
    # #Capturas LOE Amazonía
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[30], division, "", 1, 18, "Capturas LOE Amazonía", numero)
    #Plantulas Sembradas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[31], division, "", 1, 18, "Plantulas Sembradas", numero)
    #Incautacion Madera m3
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[32], division, "", 1, 18, "Incautacion Madera m3", numero)
    #Especies Animales Incautados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[63], division, "", 1, 18, "Fauna Recuperada", numero)

    #Especies Animales Incautados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[97], division, "", 2, 14, "Incidente Cibernético", numero)

    #Especies Animales Incautados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[98], division, "", 2, 14, "Ataque Cibernético", numero)
    #Especies Animales Incautados

    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[99], division, "", 2, 14, "Ata. Cibernético Mate.", numero)
    
    # #Capturas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[33], division, "", 1, 18, "Capturas Mineria", numero)
    # #Menores Recuperados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[34], division, "", 1, 18, "Menores Recuperados Mineria", numero)
    #EIYM Minas Ilegales
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[35], division, "", 2, 14, "EIYM Minas Ilegales", numero)
    #Excavadoras
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[36], division, "", 1, 18, "Excavadoras", numero)
    #Retroexcavadoras
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[37], division, "", 1, 18, "Retroexcavadoras", numero)
    #Maquinaria Pesada
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[38], division, "", 1, 18, "Maquinaria Pesada", numero)
    #Tractor con Uruga
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[39], division, "", 1, 18, "Tractor con Uruga", numero)
    # Unidad Producción Minera
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[40], division, "", 1, 18, "Unidad Producción Minera", numero)
    #Dragas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[41], division, "", 1, 18, "Dragas", numero)
    #coltan
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[65], division, "", 1, 18, "Coltan Kg", numero)

    #Insumos Iiquidos
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[28], division, "", 1, 18, "Gal Insumos Iiquidos", numero)
    #Insumos Solidos
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[29], division, "", 1, 18, "Kg Insumos Solidos", numero)
    #Combustible Incautado Gal
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[62], division, "", 1, 18, "Combustible Incautado Gal", numero)
    #Matas de Coca en Semilleros
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[27], division, "", 1, 18, "Matas de Coca en Semilleros", numero)

    # print("------")
    # print(str(numero[0]) + " -" +division)
    if numero[0] == 0:

        valor = "° SIN EVENTOS"
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 8)
        pdf.text(posicion,celda,valor)
    celdas =  numero[0] * 4

    return celdas

def resultados_diarios_divisiones_coe_tropas(pdf, res_calculo_act, division, posiciones, filtro, hechos_actual):
 
    # datos_division = list(filter(lambda res_calculo_act: division in res_calculo_act[1], res_calculo_act))
    datos_division = list(filter(lambda hechos_actual: division in hechos_actual[2], hechos_actual))
    # print(datos_division)
    if datos_division !=[]:
        division = division
        divfe_ayuda = '{}static/img/diviciones/divfe_ayuda.png'.format(filtro[15])
        pdf.image(divfe_ayuda,267,156,20,20)
        
    else: 
        divfe_ayuda = '{}static/img/diviciones/ejc.png'.format(filtro[15])
        division = "TREJC"
        pdf.image(divfe_ayuda,267,156,18,22)

    numeros = 0 #numero matriz que me permite avanzar en los grupos 
    celda = posiciones[0]
    posicion = posiciones[1]
    ln=posiciones[2]
    cell=posiciones[3]

    numero=[numeros, celda, posicion, cell]

    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 14)
    pdf.text(posicion+25,celda-6.25,division)
    pdf.set_font('Arial', 'B', 8)
    pdf.ln(ln)
    # pdf.cell(5)
    
    #menores
    numero = llamado_afectacion(pdf, res_calculo_act[0], division, "NO APLICA", 1, 18, "RME", numero)

    #PRESEMTACIONES 
    numero = llamado_afectacion(pdf, res_calculo_act[1], division, "NO APLICA", 1, 18, "Pres. Volt.", numero)
    #SOMETETIMIENTOS
    numero = llamado_afectacion(pdf, res_calculo_act[2], division, "NO APLICA", 1, 18, "Sometimientos.", numero)
    #CAPTURAS
    numero = llamado_afectacion(pdf, res_calculo_act[3], division, "NO APLICA", 1, 18, "Captura", numero)
    #MDOM
    numero = llamado_afectacion(pdf, res_calculo_act[4], division, "NO APLICA", 1, 18, "MDOM", numero)

    #ASESINADOS
    numero = llamado_afectacion(pdf, res_calculo_act[5], division, "NO APLICA", 1, 18, "Asesinado", numero)
    #HERIDOS
    numero = llamado_afectacion(pdf, res_calculo_act[6], division, "NO APLICA", 1, 18, "Herido", numero)

    #COCAINA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[21], division, "", 1, 18, "Kg Cocaína", numero)
    #MARIHUANA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[22], division, "", 1, 18, "Kg Marihuana", numero)
    #MARIHUANA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[23], division, "", 1, 18, "Kg P.B.C", numero)
    #Laboratorios de Cocaína
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[24], division, "", 1, 18, "Laboratorios de Cocaína", numero)
    #Laboratorios de PBC
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[25], division, "", 1, 18, "Laboratorios de PBC", numero)
    #Semilleros
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[26], division, "", 1, 18, "Semilleros", numero)

    #Depósito Ilegal
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[46], division, "", 1, 18, "Depósito Ilegal", numero)

    #Armas de Largo Alcance
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[7], division, "", 1, 18, "Armas de Largo Alcance", numero)
    #Armas de Corto Alcance
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[8], division, "", 1, 18, "Armas de Corto Alcance", numero)
    #Armas de Acompañamiento
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[9], division, "", 1, 18, "Armas de Acompañamiento", numero)
    #Municiones
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[10], division, "", 1, 18, "Municiones", numero)

    #Neutralización AE
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[16], division, "", 1, 18, "Neutralización AE", numero)
    #Neutralización MAP
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[17], division, "", 1, 18, "Neutralización MAP", numero)
    #Explosivos Destruidos kg 
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[18], division, "", 1, 18, "Kg Explosivos Destruidos", numero)
    #Cordón Detonante m
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[19], division, "", 1, 18, "Cordón Detonante m", numero)
    #Mecha Lenta m
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[20], division, "", 1, 18, "Mecha Lenta m", numero)
    #Neutralización Terrorista
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[15], division, "", 2, 14, "Neutralización Terrorista", numero)

    #Combates
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[14], division, "", 2, 14, "Combates", numero)
    
    #ATAQUE FUERZA PUBLICA
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[64], division, "", 2, 14, "Ataque Fuerza Publica", numero)

    #Liberados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[42], division, "", 1, 18, "Liberados", numero)
    #Rescatados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[43], division, "", 1, 18, "Rescatados", numero)
    #Válvulas Ilícitas Destruidas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[44], division, "", 1, 18, "Válvulas Ilícitas Destruidas", numero)
    #Refinerias Ilegales Destruidas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[45], division, "", 1, 18, "Refinerias Ilegales Destruidas", numero)
    
    # #Capturas LOE Amazonía
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[30], division, "", 1, 18, "Capturas LOE Amazonía", numero)
    #Plantulas Sembradas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[31], division, "", 1, 18, "Plantulas Sembradas", numero)
    #Incautacion Madera m3
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[32], division, "", 1, 18, "Incautacion Madera m3", numero)
    #Especies Animales Incautados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[63], division, "", 1, 18, "Fauna Recuperada", numero)
    
    # #Capturas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[33], division, "", 1, 18, "Capturas Mineria", numero)
    # #Menores Recuperados
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[34], division, "", 1, 18, "Menores Recuperados Mineria", numero)
    #EIYM Minas Ilegales
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[35], division, "", 2, 14, "EIYM Minas Ilegales", numero)
    #Excavadoras
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[36], division, "", 1, 18, "Excavadoras", numero)
    #Retroexcavadoras
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[37], division, "", 1, 18, "Retroexcavadoras", numero)
    #Maquinaria Pesada
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[38], division, "", 1, 18, "Maquinaria Pesada", numero)
    #Tractor con Uruga
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[39], division, "", 1, 18, "Tractor con Uruga", numero)
    # Unidad Producción Minera
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[40], division, "", 1, 18, "Unidad Producción Minera", numero)
    #Dragas
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[41], division, "", 1, 18, "Dragas", numero)
    #coltan
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[65], division, "", 1, 18, "Coltan Kg", numero)

    #Insumos Iiquidos
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[28], division, "", 1, 18, "Gal Insumos Iiquidos", numero)
    #Insumos Solidos
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[29], division, "", 1, 18, "Kg Insumos Solidos", numero)
    #Combustible Incautado Gal
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[62], division, "", 1, 18, "Combustible Incautado Gal", numero)
    #Matas de Coca en Semilleros
    numero = llamado_afectacion_sin_enemigo(pdf, res_calculo_act[27], division, "", 1, 18, "Matas de Coca en Semilleros", numero)

    # print("------")
    # print(str(numero[0]) + " -" +division)
    if numero[0] == 0:

        valor = "° SIN EVENTOS"
        pdf.set_text_color(0,0,0)
        pdf.set_font('Arial', 'B', 8)
        pdf.text(posicion,celda,valor)
    celdas =  numero[0] * 4

    return celdas


def titulos_resultados_dia_diseo(pdf, pos_vert, pos, text):
    #--------------------------------------------
        pdf.set_line_width(0.3)
        pdf.set_draw_color(0, 0, 0)
        pdf.set_fill_color(193, 31, 37)
        pdf.rounded_rect(pos_vert[0]-5, pos-5, 95, 7, 1,'F', '1234')      
        pdf.set_font('Arial', 'B', 12) 
        pdf.set_text_color(255, 255, 255)
        pdf.text(pos_vert[0], pos, text)
        pdf.set_text_color(0,0,0)
        pos = pos +6
    #--------------------------------------------
        return pos

def claculo_afectacion_amenaza_cabecera(pdf):
    pdf.ln(10)
    pdf.cell(30)
    pdf.set_fill_color(94, 119, 89)
    pdf.set_draw_color(0, 0, 0)
    pdf.set_text_color(255,255,255)
    pdf.set_font('Arial', 'B', 12)

    lista_enemigo = ["GAO ELN","GAO-r","GAO CG","GAO CAP","GDO","NARCO","DELCO", "TOTAL"]

    for enemigo in lista_enemigo:
        if enemigo != "TOTAL":
            pdf.cell(39,10,str(enemigo),1,0, 'C',True)
        else:
            pdf.set_fill_color(20, 62, 52)
            pdf.cell(39,10,str(enemigo),1,0, 'C',True)
    pdf.ln()

    pdf.set_font('Arial', 'B', 10)
    pdf.set_fill_color(94, 119, 89)

    pdf.cell(30)

    for enemigo in lista_enemigo:
        if enemigo != "TOTAL":
            pdf.cell(12.5,5,"2022",1,0, 'C',True)
            pdf.cell(12.5,5,"2023",1,0, 'C',True)
            pdf.cell(14,5,"%",1,0, 'C',True)
        else:
            pdf.set_fill_color(20, 62, 52)
            pdf.cell(12.5,5,"2022",1,0, 'C',True)
            pdf.cell(12.5,5,"2023",1,0, 'C',True)
            pdf.cell(14,5,"%",1,0, 'C',True)
    pdf.ln()

def celda_afectacion(pdf, dato_ant, dato_act, ruta, vert, altu ):
            num_ant = formato_numero(dato_ant)
            num_act = formato_numero(dato_act)
            pdf.cell(12.5,10,str(num_ant),0,0, 'C',False)
            pdf.cell(12.5,10,str(num_act),0,0, 'C',False)

            porcentaje = porcentajes(dato_ant, dato_act, 1)
            porcentaje_b = formato_numero_decimal(porcentaje)
            if porcentaje < 0:
                pdf.set_text_color(125,0,0)
                triangulo = '{}static/img/tri_rojo_new.png'.format(ruta)
            elif porcentaje > 0:
                pdf.set_text_color(20,62,52)
                triangulo = '{}static/img/tri_verde_new.png'.format(ruta)
                
            else:
                pdf.set_text_color(0,0,0)
                triangulo = '{}static/img/tri_amarillo_new.png'.format(ruta)

            pdf.cell(14,10,str(porcentaje_b),0,0, 'C',False)
            pdf.image(triangulo,vert, altu ,3,3)#imagenes 
            pdf.set_text_color(0,0,0)

def afectacion_ameneza_enemigo(pdf, afectacion, ln, ln2, cell, datos_res_ant, datos_res_act, suma, constante, id_enemigo, ruta, alt):
        # pdf.text(5,num2+1, text)
    pdf.ln(ln)
    pdf.cell(cell)
    pdf.set_font('Arial', 'B', 10)
    pdf.set_text_color(255,255,255)
    pdf.multi_cell(35, 5, str(afectacion), 0, "C", False)
    pdf.ln(-ln2)
    pdf.cell(30)
    pdf.set_text_color(0,0,0)

    lista_enemigo = ["GAO ELN","GAO-r","GAO CLAN DEL GOLFO","GAO CAPARROS","GDO","NARCOTRÁFICO","DELINCUENCIA", "TOTAL"]
    vert = 52.5
    lista_act = []
    lista_ant = []

    for enemigo in lista_enemigo:
        
        pdf.set_line_width(0.5)
        pdf.set_draw_color(255, 255, 255)
        pdf.line(vert, 55, vert, 176.5)
        vert = vert + 12.5
        pdf.line(vert, 55, vert, 176.5)
        vert = vert + 14
        pdf.set_line_width(1.5)
        pdf.line(vert, 45, vert, 176.5)
        vert = vert + 12.5

        if enemigo != "GAO-r" and enemigo != "TOTAL":
            
            resultados = calculo_comprativo_total_sin_formato_tipo_t(datos_res_ant, datos_res_act, enemigo, enemigo, enemigo, id_enemigo, suma, constante)
            celda_afectacion(pdf, resultados[0], resultados[1], ruta, vert-20, alt )
            lista_act.append(resultados[1])
            lista_ant.append(resultados[0])
        elif enemigo == "GAO-r":
            
            resultados = calculo_comprativo_total_sin_formato_tipo_t(datos_res_ant, datos_res_act,  "GAO-RESIDUAL","GAO-r disidencias FARC","GAO - Residual Disidencias FARC",id_enemigo, suma, constante)
            celda_afectacion(pdf, resultados[0], resultados[1], ruta, vert-20, alt )
            lista_act.append(resultados[1])
            lista_ant.append(resultados[0])

        else:
            total_act=0
            total_ant=0
            for x in lista_act:
                if x != "-":
                    total_act = total_act + float(x)

            for x in lista_ant:
                if x != "-":
                    total_ant = total_ant + float(x)

            celda_afectacion(pdf, total_ant, total_act, ruta, vert-20, alt )

            


    pdf.ln(ln)


