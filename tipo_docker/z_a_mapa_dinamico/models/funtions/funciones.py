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



def validacion_cantidad_tupla(tupla):
                  
    if len(tupla) == 1:
        valor = " = '"+tupla[0]+"'"
        
    else:
        tupla = tuple(tupla)
        valor = " in {}" .format(tupla)
    return valor 

def selecion_filtro(filtro):
    
    amenaza=filtro[7].split(",")
    brigada=filtro[2].split(",")
    unidad=filtro[3].split(",")
    mpio=filtro[6].split(",")
    dpto=filtro[5].split(",")
    apoyo = ["hop_accion_davaa", "hop_apoyo_conat", "hop_apoyo_blica"]
    apoyo_unidad = ["APOYO DAAVA", "APOYO CONAT", "APOYO BLICA"]

    valor = validacion_cantidad_tupla(dpto)
    valor_1 = validacion_cantidad_tupla(mpio)
    valor_2 = validacion_cantidad_tupla(amenaza)
    valor_unidad = validacion_cantidad_tupla(unidad)
    valor_brigada = validacion_cantidad_tupla(brigada)

    numero = 0
    res_apoyo=""
    res_ope = ""
    res_enemigo=""
    hop_enemigo=""

    res_mpio = ""
    hop_mpio = ""

    res_depto = ""
    hop_dpto = ""
    hop_unidad =""
    res_unidad =""

    hop_br =""
    res_br =""

    hop_div_hija = ""
    res_div_hija = ""

    hop_div_padre = ""
    res_div_padre = ""

    cdte = ""
    cdte_res = ""

    if filtro[24]!="":
        cdte = "and HOP_COMANDANTE = '{}' ".format(filtro[24])
   

    for x in apoyo_unidad:
        if x == filtro[9]:
            res_apoyo = " and "+apoyo[numero] +" like '%S%'"
        numero = numero +1
    
    if filtro[8] != '---':
          res_ope = " and hop_operacion = '{}'".format(filtro[8])

    if len(amenaza[0])>1:
          res_enemigo = "and hop_enemigo {}".format(valor_2)
          hop_enemigo = "and enemigo {}".format(valor_2)

    if len(mpio[0])>1:
          res_mpio = "and hop_mpio {}".format(valor_1)
          hop_mpio = "and mpio {}".format(valor_1)
    
    if len(dpto[0])>1:
          res_depto = "and hop_depto {}".format(valor)
          hop_dpto = "and dpto {}".format(valor)

          
    if len(unidad[0])>1:
        hop_unidad = "and unidad {}".format(valor_unidad) 
        res_unidad = "and hop_unidad {}".format(valor_unidad)
        
    elif len(brigada[0])>1:
        hop_br = "and brigada {}".format(valor_brigada) 
        res_br = "and hop_br {}".format(valor_brigada)

    elif filtro[1]!="" and filtro[1]!="---":
        hop_div_hija = "and division = '{}'".format(filtro[1]) 
        res_div_hija = "and hop_div = '{}'".format(filtro[1])

    elif filtro[0]!="" and filtro[0]!="---":

        if filtro[0] =="FUTCO" or filtro[0]=="FUTOM":
            hop_div_padre = "and agr_div in ('FUTCO', 'FUTOM')".format(filtro[0]) 
            res_div_padre = "and agr_div in ('FUTCO', 'FUTOM')".format(filtro[0])
        else:
            hop_div_padre = "and agr_div = '{}'".format(filtro[0]) 
            res_div_padre = "and agr_div = '{}'".format(filtro[0])

    resultados = " {} {} {} {} {} {} {} {} {} {} " .format(res_depto, res_mpio, res_enemigo, res_ope, res_apoyo, res_unidad, res_br, res_div_hija, res_div_padre, cdte)
    hechos = " {} {} {} {} {} {} {} {} {} {} ".format(hop_dpto, hop_mpio, hop_enemigo, res_ope, res_apoyo, hop_unidad, hop_br, hop_div_hija, hop_div_padre, cdte)

    erradicacion = ""
    return[resultados, hechos, erradicacion]