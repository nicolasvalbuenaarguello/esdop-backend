
def titulos_name_2(filtro, anio):
    catatumbo =['CESAR', 'NORTE DE SANTANDER', 'ABREGO', 'CONVENCIÓN', 'CÚCUTA', 'EL CARMEN', 'EL TARRA', 'EL ZULIA', 'GONZÁLEZ', 'HACARÍ', 'LA PLAYA', 'LOS PATIOS', 'OCAÑA', 'PUERTO SANTANDER', 'RÍO DE ORO', 'SAN CALIXTO', 'SAN CAYETANO', 'SARDINATA', 'TEORAMA', 'TIBÚ', 'VILLA DEL ROSARIO', 'ÁBREGO']
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    validar_mpio_dpto = dpto + mpio
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format('2025')
    dato = dato.upper()

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, titulo_2)
    
    elif validar_mpio_dpto == catatumbo:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, "CATATUMBO")

    elif "," not in mpio[0] and mpio[0] != "" and validar_mpio_dpto != catatumbo:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, mpio[0])
    elif "," not in dpto[0] :
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, dpto[0])

    elif "," not in amenaza[0]:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 - EJÉRCITO"

    
        
    if validar_mpio_dpto == catatumbo:
        titulo_compuesto.append("CATATUMBO")
    else:

        if len(mpio[0])==1:
            titulo_compuesto.append(mpio[0])
        else:
            titulo_compuesto = mpio  

        if len(dpto[0])==1:
            titulo_compuesto.append(dpto[0])
        else:
            titulo_compuesto = dpto + titulo_compuesto




    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_cartilla(filtro):
    catatumbo =['CESAR', 'NORTE DE SANTANDER', 'ABREGO', 'CONVENCIÓN', 'CÚCUTA', 'EL CARMEN', 'EL TARRA', 'EL ZULIA', 'GONZÁLEZ', 'HACARÍ', 'LA PLAYA', 'LOS PATIOS', 'OCAÑA', 'PUERTO SANTANDER', 'RÍO DE ORO', 'SAN CALIXTO', 'SAN CAYETANO', 'SARDINATA', 'TEORAMA', 'TIBÚ', 'VILLA DEL ROSARIO', 'ÁBREGO']
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    validar_mpio_dpto = dpto + mpio
    acam_enemigo=filtro[26].split(",")
    acam_estructura=filtro[27].split(",")
    ene_estructura=filtro[28].split(",")

    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[0])
    elif len(unidad[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(titulo_2)
    elif len(mpio[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(mpio[0])
    elif len(dpto[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(dpto[0])
    elif len(amenaza[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(amenaza[0])
    else:
        titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

    
    if validar_mpio_dpto == catatumbo:
        titulo_compuesto.append("CATATUMBO")
    else:

        if len(mpio[0])==1:
            titulo_compuesto.append(mpio[0])
        else:
            titulo_compuesto = mpio  

        if len(dpto[0])==1:
            titulo_compuesto.append(dpto[0])
        else:
            titulo_compuesto = dpto + titulo_compuesto


    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if len(acam_enemigo[0])==1:
        titulo_compuesto.append(acam_enemigo[0])
        
    else:
        titulo_compuesto = acam_enemigo + titulo_compuesto 
                
    if len(acam_estructura[0])==1:
        titulo_compuesto.append(acam_estructura[0])
    else:
        titulo_compuesto = acam_estructura  + titulo_compuesto
                
    if len(ene_estructura[0])==1:
        titulo_compuesto.append(ene_estructura[0])
    else:
        titulo_compuesto = ene_estructura + titulo_compuesto 

    if filtro[2] !="" and filtro[2] !="---":
        titulo_compuesto.append(filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo_compuesto.append(filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo_compuesto.append(filtro[0])
    else:
        titulo_compuesto.append("")
    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    else:
        titulo_compuesto.append("")
    

    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "" or titulo_compuesto[4] != "" or titulo_compuesto[5] != "" or titulo_compuesto[6] != ""  or titulo_compuesto[7] != "" or titulo_compuesto[8] != "" or titulo_compuesto[9] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

    for x in titulo_compuesto:

        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name(filtro):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    catatumbo =['CESAR', 'NORTE DE SANTANDER', 'ABREGO', 'CONVENCIÓN', 'CÚCUTA', 'EL CARMEN', 'EL TARRA', 'EL ZULIA', 'GONZÁLEZ', 'HACARÍ', 'LA PLAYA', 'LOS PATIOS', 'OCAÑA', 'PUERTO SANTANDER', 'RÍO DE ORO', 'SAN CALIXTO', 'SAN CAYETANO', 'SARDINATA', 'TEORAMA', 'TIBÚ', 'VILLA DEL ROSARIO', 'ÁBREGO']
    validar_mpio_dpto = dpto+ mpio 

    acam_enemigo=filtro[26].split(",")
    acam_estructura=filtro[27].split(",")
    ene_estructura=filtro[28].split(",")

    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(filtro[0])
    elif len(unidad[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "RESULTADOS OPERACIONALES - {}".format(titulo_2)
    elif len(mpio[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(mpio[0])
    elif len(dpto[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(dpto[0])
    elif len(amenaza[0])==1:
        titulo = "RESULTADOS OPERACIONALES - {}".format(amenaza[0])
    else:
        titulo = "RESULTADOS OPERACIONALES DEL EJÉRCITO NACIONAL"

        
    if validar_mpio_dpto == catatumbo:
        titulo_compuesto.append("CATATUMBO")
    else:

        if len(mpio[0])==1:
            titulo_compuesto.append(mpio[0])
        else:
            titulo_compuesto = mpio  

        if len(dpto[0])==1:
            titulo_compuesto.append(dpto[0])
        else:
            titulo_compuesto = dpto + titulo_compuesto
           

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if len(acam_enemigo[0])==1:
        titulo_compuesto.append(acam_enemigo[0])
        
    else:
        titulo_compuesto = acam_enemigo + titulo_compuesto 
                
    if len(acam_estructura[0])==1:
        titulo_compuesto.append(acam_estructura[0])
    else:
        titulo_compuesto = acam_estructura  + titulo_compuesto
                
    if len(ene_estructura[0])==1:
        titulo_compuesto.append(ene_estructura[0])
    else:
        titulo_compuesto = ene_estructura + titulo_compuesto 

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "" or titulo_compuesto[4] != "" or titulo_compuesto[5] != "" or titulo_compuesto[6] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_afectaciones(filtro, anio):

    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")

    acam_enemigo=filtro[26].split(",")
    acam_estructura=filtro[27].split(",")
    ene_estructura=filtro[28].split(",")
 

    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    catatumbo =['CESAR', 'NORTE DE SANTANDER', 'ABREGO', 'CONVENCIÓN', 'CÚCUTA', 'EL CARMEN', 'EL TARRA', 'EL ZULIA', 'GONZÁLEZ', 'HACARÍ', 'LA PLAYA', 'LOS PATIOS', 'OCAÑA', 'PUERTO SANTANDER', 'RÍO DE ORO', 'SAN CALIXTO', 'SAN CAYETANO', 'SARDINATA', 'TEORAMA', 'TIBÚ', 'VILLA DEL ROSARIO', 'ÁBREGO']
    validar_mpio_dpto = dpto+ mpio 
                
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format('2025')
    dato = dato.upper()

    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {}".format(dato)

        
    if validar_mpio_dpto == catatumbo:
        titulo_compuesto.append("CATATUMBO")
    else:

        if len(mpio[0])==1:
            titulo_compuesto.append(mpio[0])
        else:
            titulo_compuesto = mpio  

        if len(dpto[0])==1:
            titulo_compuesto.append(dpto[0])
        else:
            titulo_compuesto = dpto + titulo_compuesto
           

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if len(acam_enemigo[0])==1:
        titulo_compuesto.append(acam_enemigo[0])
        
    else:
        titulo_compuesto = acam_enemigo + titulo_compuesto 
                
    if len(acam_estructura[0])==1:
        titulo_compuesto.append(acam_estructura[0])
    else:
        titulo_compuesto = acam_estructura  + titulo_compuesto
                
    if len(ene_estructura[0])==1:
        titulo_compuesto.append(ene_estructura[0])
    else:
        titulo_compuesto = ene_estructura + titulo_compuesto 

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "" or titulo_compuesto[4] != "" or titulo_compuesto[5] != "" or titulo_compuesto[6] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_lineas_estrategicas(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 {} - EJÉRCITO".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_lineas_estrategicas_resaltantes(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    


    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()
    dato = ""
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {} {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 2 CONSOLIDADO EJÉRCITO NACIONAL {}".format(dato)


    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    
    item = filtro[29]
    if isinstance(item, dict) and "nombre" in item:
        titulo_compuesto.append(item["nombre"])
    else:
        titulo_compuesto.append("")


    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != ""  or titulo_compuesto[4] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

     
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_lineas_estrategicas_obj1(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 1 {}".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    

def titulos_name_lineas_estrategicas_obj3(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()

    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 3 {}".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]

def titulos_name_lineas_estrategicas_obj4(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
            
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, amenaza[0])
    else:
        titulo = "EVALUACIÓN OBJETIVO ESTRATÉGICO No. 4 {}".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]



def titulo_sub(pdf, municipios, filtro):
    if municipios !="":
        pdf.set_text_color(70,70,70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(45,35,str(municipios))

    if filtro[24]:
        pdf.set_text_color(70,70,70)
        pdf.set_font('BebasNeue', '', 14)
        
        pdf.text(45,35,str(filtro[24]))
   
  
def titulo_sub_2(pdf, municipios, filtro):
    if municipios !="":
        pdf.set_text_color(70,70,70)
        if len(municipios) <= 110:
            pdf.set_font('BebasNeue', '', 14)
        else:
            pdf.set_font('BebasNeue', '', 12)
        pdf.text(55,27,str(municipios))

    if filtro[24]:
        pdf.set_text_color(70,70,70)
        pdf.set_font('BebasNeue', '', 14)
        
        pdf.text(55,27,str(filtro[24]))
    
def titulos_name_lineas_estrategicas_evaluacion(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
        
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()

    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - {}".format(dato, amenaza[0])
    else:
        titulo = "CONSOLIDADO  OBJETIVO ESTRATÉGICO No. 2 {} - EJÉRCITO".format(dato )

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    
    
def titulos_name_lineas_estrategicas_evaluacion_obj1(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()
    
    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 1 {} {}".format(dato, amenaza[0])
    else:
        titulo = "CONSOLIDADO EVALUACIÓN OBJETIVO No. 1 {} ".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]


     
def titulos_name_lineas_estrategicas_evaluacion_obj3(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
        
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()

    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {} {}".format(dato, amenaza[0])
    else:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 3 {}".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    
   
def titulos_name_lineas_estrategicas_evaluacion_obj4(filtro, anio):
    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]
    titulo = ""
    titulo_2 =""
    numero =0
    apoyo=""
    cdte=""
    indicador=""
    
    titulo_compuesto=[]
    titulo_compuesto_fina=[]
                
    dato = 'Plan de Campaña "Ayacucho PLUS" {}'.format(anio)
    dato = dato.upper()

    for x in apoyo_unidad:
        if x == filtro[9]:
            titulo_2 = apoyo_unidad[numero]
        numero = numero +1

    if filtro[2] !="" and filtro[2] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[2])
    elif filtro[1] !="" and filtro[1] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[1])
    elif filtro[0] !="" and filtro[0] !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, filtro[0])
    elif len(unidad[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, unidad[0])
    elif titulo_2!="" and titulo_2 !="---":
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, titulo_2)
    elif len(mpio[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, mpio[0])
    elif len(dpto[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, dpto[0])
    elif len(amenaza[0])==1:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {} {}".format(dato, amenaza[0])
    else:
        titulo = "CONSOLIDADO OBJETIVO ESTRATÉGICO No. 4 {}".format(dato)

        
    if len(mpio[0])==1:
        titulo_compuesto.append(mpio[0])
    else:
        titulo_compuesto = mpio  

    if len(dpto[0])==1:
        titulo_compuesto.append(dpto[0])
    else:
        titulo_compuesto = dpto + titulo_compuesto

    if len(unidad[0])==1:
        titulo_compuesto.append(unidad[0])
    else:
        titulo_compuesto = unidad + titulo_compuesto

    if len(amenaza[0])==1:
        titulo_compuesto.append(amenaza[0])
    else:
        titulo_compuesto = amenaza + titulo_compuesto

    if titulo_2!="":
        titulo_compuesto.append(titulo_2)
    
    if titulo_compuesto[0] != "" or titulo_compuesto[1] != "" or titulo_compuesto[2] != "" or titulo_compuesto[3] != "":

        titulo_compuesto = titulo_compuesto
    else:
        titulo_compuesto = ""

        
    for x in titulo_compuesto:
        if x != "":

            titulo_compuesto_fina.append(x) 

    return[titulo, titulo_compuesto_fina]
    
   
