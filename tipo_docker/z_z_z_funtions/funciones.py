
def union_filtro(parametros):
        resultados = " and {} = '{}'".format(parametros[0],parametros[3])
        hechos = " and {} = '{}'".format(parametros[1],parametros[3])
        erradicacion = " and {} = '{}'".format(parametros[2],parametros[3])

        return[resultados, hechos, erradicacion]
def allo_file(file):
    ALLOWED_EXTENSIONS = set(['png', 'jpg','jpeg', 'jfif'])
    file = file.split('.')
    if file[1] in ALLOWED_EXTENSIONS:
        return True
    else:
        False
    
def validar_chec(dato):
        dato = dato
        if dato == True:
            dato = "OK"
        else:
            dato = "--"
        return dato

def selecion(permiso, unidad):
    if permiso == "EJC":
        query =  "SELECT DISTINCT agr_div FROM view_unidades_materializados ORDER BY agr_div ASC"
        
        query_a =  "SELECT DISTINCT  division FROM view_unidades_materializados ORDER BY division ASC"
        query_b =  "SELECT DISTINCT brigada FROM view_unidades_materializados ORDER BY brigada ASC"
        query_c =  "SELECT DISTINCT unidad FROM view_unidades_materializados ORDER BY unidad ASC"
        query_d =  "SELECT DISTINCT dpto FROM view_unidades_materializados ORDER BY dpto ASC"
        query_e =  "SELECT DISTINCT mpio FROM view_unidades_materializados ORDER BY mpio ASC"
        query_f =  "SELECT DISTINCT enemigo FROM view_enemigo_materializados ORDER BY enemigo ASC"
        query_g =  "SELECT DISTINCT hop_operacion FROM view_hop_operacion_materializados ORDER BY hop_operacion ASC"
      
    else:
            query =  "SELECT DISTINCT agr_div FROM view_unidades_materializados where {} = '{}' ORDER BY agr_div ASC".format(permiso, unidad)
            
            query_a =  "SELECT DISTINCT division FROM view_unidades_materializados WHERE {} = '{}' ORDER BY division ASC".format(permiso, unidad)

            query_b =  "SELECT DISTINCT brigada FROM view_unidades_materializados WHERE  {} = '{}' ORDER BY brigada ASC".format(permiso, unidad)

            query_c =  "SELECT DISTINCT unidad FROM view_unidades_materializados WHERE {} = '{}' ORDER BY unidad ASC".format(permiso, unidad)

            query_d =  "SELECT DISTINCT dpto FROM view_unidades_materializados WHERE {} = '{}' ORDER BY dpto ASC".format(permiso, unidad)

            query_e =  "SELECT DISTINCT mpio FROM view_unidades_materializados WHERE {} = '{}' ORDER BY mpio ASC".format(permiso, unidad)

            query_f =  "SELECT DISTINCT enemigo FROM view_enemigo_materializados ORDER BY enemigo ASC"
            
            query_g =  "SELECT DISTINCT hop_operacion FROM view_hop_operacion_materializados ORDER BY hop_operacion ASC"
            
    return [query, query_a, query_b, query_c, query_d, query_e, query_f, query_g]

#Parámetros para realizar el query a la base de datos y poder realzar el cálculo de la estadística 
def parametros(fecha_inicial_u_l, fecha_final_u_l, filtro, filtros):

    campo_resultados = filtro[0]
    campo_hechos = filtro[1]
    campo_erradicacion = filtro[2]

    if filtros[12] == "EJC":
        unidad_hechos = ""
        unidad_resultados = ""
        unidad_erradicacion = ""
    elif filtros[12] == "agr_div":
        unidad_hechos = " and agr_div = '{}'".format(filtros[13])
        unidad_resultados = " and agr_div = '{}'".format(filtros[13])
        unidad_erradicacion = ""
    elif filtros[12] == "division ":
        unidad_hechos = " and division = '{}'".format(filtros[13])
        unidad_resultados = " and hop_div = '{}'".format(filtros[13])
        unidad_erradicacion = ""
    elif filtros[12] == "brigada":
        unidad_hechos = " and brigada = '{}'".format(filtros[13])
        unidad_resultados = " and hop_br  = '{}'".format(filtros[13])
        unidad_erradicacion = ""
    elif filtros[12] == "unidad":
        unidad_hechos = " and unidad = '{}'".format(filtros[13])
        unidad_resultados = " and hop_unidad  = '{}'".format(filtros[13])
        unidad_erradicacion = ""
    
    query_resultados = "SELECT * FROM view_resultados_materializados WHERE hop_fecha_hecho >= '{}'  AND hop_fecha_hecho <= '{}' {}  {} ORDER BY hop_fecha_hecho ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_resultados,unidad_resultados)
         
    querys_hechos = "SELECT * FROM view_hechos_materializados WHERE fecha_hecho >= '{}'  AND fecha_hecho <= '{}' {}   {} ORDER BY fecha_hecho ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_hechos, unidad_hechos)
         
    querys_erradicacion = "SELECT * FROM view_erradicacion_materializados WHERE unidad >= '{}'  AND unidad <= '{}' {}   {} ORDER BY unidad ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_erradicacion,unidad_erradicacion)
    return [query_resultados, querys_hechos, querys_erradicacion]

#Parámetros para realizar el query a la base de datos y poder realzar el cálculo de la estadística solo trae ls siglas de las unidades 
def parametros_unidades(fecha_inicial_u_l, fecha_final_u_l, filtro, filtros):
    """
    Construye el query para obtener las siglas de las unidades según filtros aplicados.
    """

    campo_hechos = filtro[1]

    tipo_filtro = filtros[12]
    valor_filtro = filtros[13]

    # Mapeo de filtros a campos BD
    filtros_unidad = {
        "EJC": ("", ""),
        "agr_div": ("agr_div", "agr_div"),
        "division": ("division", "hop_div"),
        "brigada": ("brigada", "hop_br"),
        "unidad": ("unidad", "hop_unidad"),
    }

    # Obtener campos según tipo
    campo_hecho, _ = filtros_unidad.get(tipo_filtro, ("", ""))

    # Construir condición unidad
    unidad_condicion = (
        f" AND {campo_hecho} = '{valor_filtro}'"
        if campo_hecho else ""
    )

    query_hechos = f"""
        SELECT DISTINCT
            agr_div,
            division,
            brigada,
            unidad
        FROM view_hechos_materializados
        WHERE fecha_hecho >= '{fecha_inicial_u_l}'
          AND fecha_hecho <= '{fecha_final_u_l}'
          {campo_hechos}
          {unidad_condicion}
          AND agr_div NOT IN ('-', 'FTCEC')
        ORDER BY agr_div ASC
    """

    return [query_hechos.strip()]

def parametros_mineria(fecha_inicial_u_l, fecha_final_u_l, filtro, filtros):

    campo_resultados = filtro[0]
    campo_hechos = filtro[1]
    campo_erradicacion = filtro[2]


    query_resultados = "SELECT * FROM view_resultados_materializados WHERE hop_fecha_hecho >= '{}'  AND hop_fecha_hecho <= '{}' {}   ORDER BY hop_fecha_hecho ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_resultados)
         
    querys_hechos = "SELECT * FROM view_hechos_materializados WHERE fecha_hecho >= '{}'  AND fecha_hecho <= '{}' {}    ORDER BY fecha_hecho ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_hechos )
         
    querys_erradicacion = "SELECT * FROM view_erradicacion_materializados WHERE unidad >= '{}'  AND unidad <= '{}' {}   ORDER BY unidad ASC".format(fecha_inicial_u_l, fecha_final_u_l, campo_erradicacion)

    return [query_resultados, querys_hechos, querys_erradicacion]

def tipo_permiso(permiso):
    if permiso == "agr_div":
          resultados = "agr_div"
          hechos = "agr_div"
          erradicacion = "agr_div"

    elif permiso == "division":
          resultados = "hop_div"
          hechos = "division"
          erradicacion = "hop_div"
          
    elif permiso == "brigada":
          resultados = "hop_br"
          hechos = "brigada"
          erradicacion = "hop_br"
                    
    elif permiso == "unidad":
          resultados = "hop_unidad"
          hechos = "unidad"
          erradicacion = "hop_unidad"
                    
    return[resultados,hechos,erradicacion]



def validacion_cantidad_tupla(lista):
    if len(lista) == 1:
        return f"'{lista[0]}'"
    else:
        return str(tuple(lista))  # e.g., ('A', 'B')

def generar_filtro(campo, valor):
    if valor.startswith("("):  # más de un valor
        return f"and {campo} in {valor}"
    else:
        return f"and {campo} = {valor}"

def mineria(filtro):

    numero = 0
    res_apoyo = res_ope = res_enemigo = hop_enemigo = ""
    res_mpio = hop_mpio = res_depto = hop_dpto = ""
    hop_unidad = res_unidad = hop_br = res_br = ""
    hop_div_hija = res_div_hija = hop_div_padre = res_div_padre = ""
    cdte = res_acam_enemigo = res_acam_estructura = res_ene_estructura = ""

    amenaza = filtro[7].split(",")
    brigada = filtro[2].split(",")
    unidad = filtro[3].split(",")
    mpio = filtro[6].split(",")
    dpto = filtro[5].split(",")
    acam_enemigo = filtro[26].split(",")
    acam_estructura = filtro[27].split(",")
    ene_estructura = filtro[28].split(",")

    apoyo = ["hop_accion_davaa", "hop_apoyo_conat", "hop_apoyo_blica",	 "hop_accion_ccoes",	 "hop_apoyo_aereo",	 "hop_apoyo_aereo",	 "hop_apoyo_aereo",	 "hop_apoyo_art",	 "hop_apoyo_bafur",	 "hop_apoyo_brcmi",	 "hop_apoyo_brcom",	 "hop_apoyo_divfe",	 "hop_apoyo_exde",	 "hop_apoyo_fudat",	 "hop_apoyo_groic",	 "hop_apoyo_pj", "hop_asalto_aereo"	]
    
    res_apoyo_valor = ["S", "S", "S", "S", "MISIÓN ALFA", "MISIÓN BETA", "MISIÓN CHARLIE", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S"]

    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA" "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO"]


    item = filtro[29]
    if isinstance(item, dict) and "nombre" in item:
        valor = validacion_cantidad_tupla([d["nombre"] for d in item["departamentos"]])
        valor_1 = validacion_cantidad_tupla([
            m for d in item["departamentos"] for m in d["municipios"]
        ])
        res_mpio = generar_filtro("hop_mpio", valor_1)
        hop_mpio = generar_filtro("mpio", valor_1)
        res_depto = generar_filtro("hop_depto", valor)
        hop_dpto = generar_filtro("dpto", valor)
    else:
        valor = validacion_cantidad_tupla(dpto)
        valor_1 = validacion_cantidad_tupla(mpio)

    valor_2 = validacion_cantidad_tupla(amenaza)
    valor_unidad = validacion_cantidad_tupla(unidad)
    valor_brigada = validacion_cantidad_tupla(brigada)
    valor_acam_enemigo = validacion_cantidad_tupla(acam_enemigo)
    valor_acam_estructura = validacion_cantidad_tupla(acam_estructura)
    valor_ene_estructura = validacion_cantidad_tupla(ene_estructura)

    if filtro[24]:
        cdte = f"and HOP_COMANDANTE = '{filtro[24]}'"

    for x in apoyo_unidad:
        if x == filtro[9]:
            res_apoyo = f"and {apoyo[numero]} like '%{res_apoyo_valor[numero]}%'"
        numero += 1
    

    if filtro[8] != '---':
        res_ope = f"and hop_operacion = '{filtro[8]}'"

    if len(amenaza[0]) > 1:
        res_enemigo = generar_filtro("hop_enemigo", valor_2)
        hop_enemigo = generar_filtro("enemigo", valor_2)

    if len(mpio[0]) > 1 and not res_mpio:
        res_mpio = generar_filtro("hop_mpio", valor_1)
        hop_mpio = generar_filtro("mpio", valor_1)

    if len(dpto[0]) > 1 and not res_depto:
        res_depto = generar_filtro("hop_depto", valor)
        hop_dpto = generar_filtro("dpto", valor)

    if len(acam_enemigo[0]) > 1:
        res_acam_enemigo = generar_filtro("acam_enemigo", valor_acam_enemigo)

    if len(acam_estructura[0]) > 1:
        res_acam_estructura = generar_filtro("acam_estructura_unidad", valor_acam_estructura)

    if len(ene_estructura[0]) > 1:
        res_ene_estructura = generar_filtro("ene_estructura", valor_ene_estructura)

    if len(unidad[0]) > 1:
        hop_unidad = generar_filtro("unidad", valor_unidad)
        res_unidad = generar_filtro("hop_unidad", valor_unidad)
    elif len(brigada[0]) > 1:
        hop_br = generar_filtro("brigada", valor_brigada)
        res_br = generar_filtro("hop_br", valor_brigada)
    elif filtro[1] and filtro[1] != "---":
        hop_div_hija = f"and division = '{filtro[1]}'"
        res_div_hija = f"and hop_div = '{filtro[1]}'"
    elif filtro[0] and filtro[0] != "---":
        if filtro[0] in ("FUTCO", "FUTOM"):
            hop_div_padre = "and agr_div in ('FUTCO', 'FUTOM')"
            res_div_padre = "and agr_div in ('FUTCO', 'FUTOM')"
        else:
            hop_div_padre = f"and agr_div = '{filtro[0]}'"
            res_div_padre = f"and agr_div = '{filtro[0]}'"

    resultados = " ".join(filter(None, [
        res_depto, res_mpio, res_enemigo, res_ope, res_apoyo,
        res_unidad, res_br, res_div_hija, res_div_padre,
        cdte, res_acam_enemigo, res_acam_estructura, res_ene_estructura
    ]))

    hechos = " ".join(filter(None, [
        hop_dpto, hop_mpio, hop_enemigo, res_ope, res_apoyo,
        hop_unidad, hop_br, hop_div_hija, hop_div_padre,
        cdte, res_acam_enemigo, res_acam_estructura, res_ene_estructura
    ]))

    erradicacion = ""

    return [resultados, hechos, erradicacion]

def selecion_filtro(filtro):

    numero = 0
    res_apoyo = res_ope = res_enemigo = hop_enemigo = ""
    res_mpio = hop_mpio = res_depto = hop_dpto = ""
    hop_unidad = res_unidad = hop_br = res_br = ""
    hop_div_hija = res_div_hija = hop_div_padre = res_div_padre = ""
    cdte = res_acam_enemigo = res_acam_estructura = res_ene_estructura = hop_cuadrilla=""

    amenaza = filtro[7].split(",")
    brigada = filtro[2].split(",")
    unidad = filtro[3].split(",")
    mpio = filtro[6].split(",")
    dpto = filtro[5].split(",")
    acam_enemigo = filtro[26].split(",")
    acam_estructura = filtro[27].split(",")
    ene_estructura = filtro[28].split(",")
    


    apoyo = ["hop_accion_davaa", "hop_apoyo_conat", "hop_apoyo_blica",	 "hop_accion_ccoes",	 "hop_apoyo_aereo",	 "hop_apoyo_aereo",	 "hop_apoyo_aereo",	 "hop_apoyo_art",	 "hop_apoyo_bafur",	 "hop_apoyo_brcmi",	 "hop_apoyo_brcom",	 "hop_apoyo_divfe",	 "hop_apoyo_exde",	 "hop_apoyo_fudat",	 "hop_apoyo_groic",	 "hop_apoyo_pj", "hop_asalto_aereo", "apoyo_coeej", "unidad_brcmi"]

    

    
    res_apoyo_valor = ["S", "S", "S", "S", "MISIÓN ALFA", "MISIÓN BETA", "MISIÓN CHARLIE", "S", "S", "S", "S", "S", "S", "S", "S", "S", "S", "SI", "BRCMI"]

    apoyo_unidad = ["APOYO DAVAA", "APOYO CONAT", "APOYO BLICA", "Apoyo CCOES", "Apoyo AÉREO MISIÓN ALFA", "Apoyo AÉREO MISIÓN BETA", "Apoyo AÉREO MISIÓN CHARLIE", "Apoyo ART", "Apoyo BAFUR", "Apoyo BRCMI", "Apoyo BRCOM", "Apoyo DIVFE", "Apoyo EXDE", "Apoyo FUDAT", "Apoyo GROIC", "Apoyo PJ", "Apoyo AÉREO", "Apoyo COEEJ", "UNIDAD BRCMI"]


    item = filtro[29]
    if isinstance(item, dict) and "nombre" in item:
        valor = validacion_cantidad_tupla([d["nombre"] for d in item["departamentos"]])
        valor_1 = validacion_cantidad_tupla([
            m for d in item["departamentos"] for m in d["municipios"]
        ])
        res_mpio = generar_filtro("hop_mpio", valor_1)
        hop_mpio = generar_filtro("mpio", valor_1)
        res_depto = generar_filtro("hop_depto", valor)
        hop_dpto = generar_filtro("dpto", valor)
    else:
        valor = validacion_cantidad_tupla(dpto)
        valor_1 = validacion_cantidad_tupla(mpio)

    valor_2 = validacion_cantidad_tupla(amenaza)
    valor_unidad = validacion_cantidad_tupla(unidad)
    valor_brigada = validacion_cantidad_tupla(brigada)
    valor_acam_enemigo = validacion_cantidad_tupla(acam_enemigo)
    valor_acam_estructura = validacion_cantidad_tupla(acam_estructura)
    valor_ene_estructura = validacion_cantidad_tupla(ene_estructura)

    if filtro[24]:
        cdte = f"and HOP_COMANDANTE = '{filtro[24]}'"

    for x in apoyo_unidad:
        if x == filtro[9]:
            res_apoyo = f"and {apoyo[numero]} like '%{res_apoyo_valor[numero]}%'"
        numero += 1
    

    if filtro[8] != '---' and filtro[8]:
        res_ope = f"and hop_operacion = '{filtro[8]}'"

    if len(amenaza[0]) > 1:
        res_enemigo = generar_filtro("hop_enemigo", valor_2)
        hop_enemigo = generar_filtro("enemigo", valor_2)

    if len(mpio[0]) > 1 and not res_mpio:
        res_mpio = generar_filtro("hop_mpio", valor_1)
        hop_mpio = generar_filtro("mpio", valor_1)

    if len(dpto[0]) > 1 and not res_depto:
        res_depto = generar_filtro("hop_depto", valor)
        hop_dpto = generar_filtro("dpto", valor)

    if len(acam_enemigo[0]) > 1:
        res_acam_enemigo = generar_filtro("acam_enemigo", valor_acam_enemigo)

    if len(acam_estructura[0]) > 1:
        res_acam_estructura = generar_filtro("acam_estructura_unidad", valor_acam_estructura)

    if len(ene_estructura[0]) > 1:
        res_ene_estructura = generar_filtro("ene_estructura", valor_ene_estructura)
        hop_cuadrilla  = generar_filtro("hop_cuadrilla", valor_ene_estructura)

    if len(unidad[0]) > 1:
        hop_unidad = generar_filtro("unidad", valor_unidad)
        res_unidad = generar_filtro("hop_unidad", valor_unidad)
    elif len(brigada[0]) > 1:
        hop_br = generar_filtro("brigada", valor_brigada)
        res_br = generar_filtro("hop_br", valor_brigada)
    elif filtro[1] and filtro[1] != "---":
        hop_div_hija = f"and division = '{filtro[1]}'"
        res_div_hija = f"and hop_div = '{filtro[1]}'"
    elif filtro[0] and filtro[0] != "---":
        if filtro[0] in ("FUTCO", "FUTOM"):
            hop_div_padre = "and agr_div in ('FUTCO', 'FUTOM')"
            res_div_padre = "and agr_div in ('FUTCO', 'FUTOM')"
        else:
            hop_div_padre = f"and agr_div = '{filtro[0]}'"
            res_div_padre = f"and agr_div = '{filtro[0]}'"

    resultados = " ".join(filter(None, [
        res_depto, res_mpio, res_enemigo, res_ope, res_apoyo,
        res_unidad, res_br, res_div_hija, res_div_padre,
        cdte, res_acam_enemigo, res_acam_estructura, hop_cuadrilla
    ]))

    hechos = " ".join(filter(None, [
        hop_dpto, hop_mpio, hop_enemigo, res_ope, res_apoyo,
        hop_unidad, hop_br, hop_div_hija, hop_div_padre,
        cdte, res_acam_enemigo, res_acam_estructura, res_ene_estructura
    ]))

    erradicacion = ""

    return [resultados, hechos, erradicacion]
