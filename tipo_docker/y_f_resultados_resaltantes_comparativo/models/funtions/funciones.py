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


def union_filtro(parametros):
        resultados = " and {} = '{}'".format(parametros[0],parametros[3])
        hechos = " and {} = '{}'".format(parametros[1],parametros[3])
        erradicacion = " and {} = '{}'".format(parametros[2],parametros[3])

        return[resultados, hechos, erradicacion]

def union_filtro_doble(parametros):
        resultados = " and {} = '{}' and {} = '{}'".format(parametros[0],parametros[3],parametros[4],parametros[7])
        hechos = " and {} = '{}' and {} = '{}'".format(parametros[1],parametros[3],parametros[5],parametros[7])
        erradicacion = " and {} = '{}' and {} = '{}'".format(parametros[2],parametros[3],parametros[6],parametros[7])

        return[resultados, hechos, erradicacion]

def validacion_cantidad_tupla(tupla):
                  
    if len(tupla) == 1:
        valor = " = '"+tupla[0]+"'"
        
    else:
        tupla = tuple(tupla)
        valor = " in {}" .format(tupla)
    return valor 

def selecion_filtro(filtro):

    amenaza=filtro[7].split(",")
    unidad=filtro[3].split(",")
   

    if filtro[4] == "apoyo":
            if filtro[9] == "APOYO DAAVA":
               parametros = ["hop_accion_davaa", "hop_accion_davaa", "mpio_erradicacion", "SI"]
               res_selecion = union_filtro(parametros)

            elif filtro[9] == "APOYO CONAT":
               parametros = ["hop_apoyo_conat", "hop_apoyo_conat", "mpio_erradicacion", "S"]
               res_selecion = union_filtro(parametros)
               
            elif filtro[9] == "APOYO BLICA":
               parametros = ["hop_apoyo_blica", "hop_apoyo_blica", "mpio_erradicacion", "S"]
               res_selecion = union_filtro(parametros)

            return res_selecion 
         
    if  filtro[4] == "lugar":

            if filtro[5]!="---" and len(unidad[0])>1:
                parametros = ["hop_depto", "dpto", "depto_erradicacion", filtro[5], "hop_enemigo", "enemigo", "mpio_erradicacion", filtro[7]]
                res_selecion = union_filtro_doble(parametros)

            elif filtro[5]!="---" and filtro[8]!="---":
                parametros = ["hop_depto", "dpto", "depto_erradicacion", filtro[5], "hop_operacion", "hop_operacion", "mpio_erradicacion", filtro[8]]
                res_selecion = union_filtro_doble(parametros)

            elif filtro[5]!= "---" :#filtro por departamento
               parametros = ["hop_depto", "dpto", "depto_erradicacion", filtro[5]]
               res_selecion = union_filtro(parametros)

            return res_selecion

    if  filtro[4] == "unidad":
            
            if len(unidad[0])>1 and len(amenaza[0])>1 :
                valor = validacion_cantidad_tupla(amenaza)
                valor_1 = validacion_cantidad_tupla(unidad)

                resultados = " and hop_enemigo {} and hop_unidad {} " .format(valor, valor_1)
                hechos = " and enemigo  {} and unidad {}".format(valor, valor_1)
                erradicacion = " and mpio_erradicacion  {} and hop_unidad {} ".format(valor, valor_1)

                return[resultados, hechos, erradicacion]
            
            elif len(unidad[0])>1 and filtro[8]!="---":

                valor_1 = validacion_cantidad_tupla(unidad)
                resultados = " and hop_operacion {} and hop_unidad {} " .format(filtro[8], valor_1)
                hechos = " and enemhop_operacionigo  {} and unidad {}".format(filtro[8], valor_1)
                erradicacion = " and mpio_erradicacion  {} and hop_unidad {} ".format(filtro[8], valor_1)

                return[resultados, hechos, erradicacion]
                          
            elif filtro[2]!="" and filtro[2]!="---" and len(amenaza[0])>1 :

                valor = validacion_cantidad_tupla(amenaza)
                resultados = " and hop_enemigo {} and hop_br = '{}' " .format(valor, filtro[2])
                hechos = " and enemigo  {} and brigada = '{}'".format(valor, filtro[2])
                erradicacion = " and mpio_erradicacion  {} and hop_br = '{}' ".format(valor, filtro[2])
                return[resultados, hechos, erradicacion]
            
            elif filtro[2]!="" and filtro[2]!="---" and filtro[8]!="---":
                parametros = ["hop_br", "brigada", "hop_br", filtro[2], "hop_operacion", "hop_operacion", "mpio_erradicacion", filtro[8]]
                res_selecion = union_filtro_doble(parametros)
                
            elif filtro[1]!="" and filtro[1]!="---" and len(amenaza[0])>1 :
                valor = validacion_cantidad_tupla(amenaza)
                resultados = " and hop_enemigo {} and hop_div = '{}'" .format(valor, filtro[1])
                hechos = " and enemigo  {} and division = '{}'".format(valor, filtro[1])
                erradicacion = " and mpio_erradicacion  {} and hop_div = '{}' ".format(valor, filtro[1])
                return[resultados, hechos, erradicacion]

            elif filtro[1]!="" and filtro[1]!="---" and filtro[8]!="---":
                parametros = ["hop_div", "division", "hop_div", filtro[1], "hop_operacion", "hop_operacion", "mpio_erradicacion", filtro[8]]
                res_selecion = union_filtro_doble(parametros)

            elif filtro[0]!="" and filtro[0]!="---" and len(amenaza[0])>1 :
                valor = validacion_cantidad_tupla(amenaza)
                resultados = " and hop_enemigo {} and agr_div = '{}' " .format(valor, filtro[0])
                hechos = " and enemigo  {} and agr_div = '{}'".format(valor, filtro[0])
                erradicacion = " and mpio_erradicacion  {} and agr_div = '{}' ".format(valor, filtro[0])
                return[resultados, hechos, erradicacion]

            elif filtro[0]!="" and filtro[0]!="---" and filtro[8]!="---":
                parametros = ["agr_div", "agr_div", "agr_div", filtro[0], "hop_operacion", "hop_operacion", "mpio_erradicacion", filtro[8]]
                res_selecion = union_filtro_doble(parametros)
            #filtro por enemigos
            elif len(amenaza[0])>0 :
                valor = validacion_cantidad_tupla(amenaza)
                resultados = " and hop_enemigo {}" .format(valor)
                hechos = " and enemigo  {} ".format(valor)
                erradicacion = " and mpio_erradicacion  {}".format(valor)

                return[resultados, hechos, erradicacion]

            elif filtro[8]!= "---" :
               parametros = ["hop_operacion", "hop_operacion", "mpio_erradicacion", filtro[8]]
               res_selecion = union_filtro(parametros)
               
            elif len(unidad[0])>0:

                valor_1 = validacion_cantidad_tupla(unidad)
                resultados = "and hop_unidad {} " .format(valor_1)
                hechos = " and unidad {}".format(valor_1)
                erradicacion = "and hop_unidad {} ".format( valor_1)

                return[resultados, hechos, erradicacion]
               
            elif filtro[2]!= "" and filtro[2]!= "---":
               parametros = ["hop_br", "brigada", "hop_br", filtro[2]]
               res_selecion = union_filtro(parametros)
               
            elif filtro[1]!= "" and filtro[1]!= "---":
               parametros = ["hop_div", "division", "hop_div", filtro[1]]
               res_selecion = union_filtro(parametros)
                              
            elif filtro[0]!= "---" :
               parametros = ["agr_div", "agr_div", "agr_div", filtro[0]]
               res_selecion = union_filtro(parametros)
            else:
               res_selecion = ["", "", ""]

    return res_selecion




