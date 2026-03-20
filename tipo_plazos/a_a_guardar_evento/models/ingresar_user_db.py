from datetime import datetime
# coding: utf-8
from __init__ import *
from a_a_guardar_evento.models.conexion_pos import *
from werkzeug.security import generate_password_hash
def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor

def guardar_evento(datos, foto):
    conexion_pos = Databa_bases()

    #datos
    usuario = datos["usuario"]
    contrasenia = generate_password_hash(datos["contrasenia"])
    nombre = datos["nombre"]
    roll = datos["roll"]
    tipo_unidad = datos["tipo_unidad"]
    unidad = datos["unidad"]
    view = validar_check(datos["view"])
    select = validar_check(datos["select"])
    insert = validar_check(datos["insert"])
    update = validar_check(datos["update"])
    deletes = validar_check(datos["deletes"])
    resultados = validar_check(datos["resultados"])
    eventos = validar_check(datos["eventos"])
    usuarios = validar_check(datos["usuarios"])
    unidad_dependencia = validar_check(datos["unidad_dependencia"])
    chat = validar_check(datos["chat"])
    conf_narcotrafico = validar_check(datos["conf_narcotrafico"])
    operaciones = validar_check(datos["operaciones"])
    personal = validar_check(datos["personal"])
    orden = validar_check(datos["orden"])
    afectaciones_fuera_comabte = validar_check(datos["afectaciones_fuera_comabte"])
    boletin_coe = validar_check(datos["boletin_coe"])
    boletin_cuadros_coe = validar_check(datos["boletin_cuadros_coe"])
    boletin_res_div = validar_check(datos["boletin_res_div"])
    cartilla_presidencial_larga = validar_check(datos["cartilla_presidencial_larga"])
    cartilla_presidencial_corta = validar_check(datos["cartilla_presidencial_corta"])
    boletin_diseo = validar_check(datos["boletin_diseo"])
    boletin_diseo_semanal = validar_check(datos["boletin_diseo_semanal"])
    comando_general = validar_check(datos["comando_general"])
    Estadistica_resultados = validar_check(datos["Estadistica_resultados"])
    com_resultados_reducido = validar_check(datos["com_resultados_reducido"])
    narcotrafico = validar_check(datos["narcotrafico"])
    artemisa = validar_check(datos["artemisa"])
    artemisa_comparativo = validar_check(datos["artemisa_comparativo"])
    contrabando = validar_check(datos["contrabando"])
    contrabando_comparativo = validar_check(datos["contrabando_comparativo"])
    mineria = validar_check(datos["mineria"])
    mineria_comparativo = validar_check(datos["mineria_comparativo"])
    comparativo_enemigo = validar_check(datos["comparativo_enemigo"])
    comparativo_mapa = validar_check(datos["comparativo_mapa"])
    comparativo_resultados = validar_check(datos["comparativo_resultados"])
    afectacion_a_la_amenaza = validar_check(datos["afectacion_a_la_amenaza"])
    afectacion_comparativa_p_t = validar_check(datos["afectacion_comparativa_p_t"])
    lis_afectaciones = validar_check(datos["lis_afectaciones"])
    afectaciones_mapa = validar_check(datos["afectaciones_mapa"])
    afectaciones_cuadros = validar_check(datos["afectaciones_cuadros"])
    regiones = validar_check(datos["regiones"])
    resaltantes = validar_check(datos["resaltantes"])
    reslatantes_divisiones = validar_check(datos["reslatantes_divisiones"])
    bullets = validar_check(datos["bullets"])
    boltin_dirop = validar_check(datos["boltin_dirop"])
    estadistica_eventos = validar_check(datos["estadistica_eventos"])
    informe_eventos = validar_check(datos["informe_eventos"])
    dato_e = validar_check(datos["datos"])
    cambio_contrasenia = validar_check(datos["cambio_contrasenia"])


    dato="""('{}', '{}', '{}',	'{}',	'{}',	'{}',	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{},	{}, '{}',{},{})""".format(nombre, usuario, contrasenia, roll, tipo_unidad, unidad, view, select, insert, update, deletes, resultados, eventos, usuarios, chat, conf_narcotrafico, operaciones, personal, orden, afectaciones_fuera_comabte, boletin_coe, boletin_cuadros_coe, boletin_res_div, cartilla_presidencial_larga, cartilla_presidencial_corta, boletin_diseo, boletin_diseo_semanal, comando_general, Estadistica_resultados, com_resultados_reducido, narcotrafico, artemisa, artemisa_comparativo, contrabando, contrabando_comparativo, mineria, mineria_comparativo, comparativo_enemigo, comparativo_mapa, comparativo_resultados, afectacion_a_la_amenaza, afectacion_comparativa_p_t, lis_afectaciones, afectaciones_mapa, afectaciones_cuadros, regiones, resaltantes, reslatantes_divisiones, bullets, boltin_dirop, estadistica_eventos, informe_eventos, unidad_dependencia, dato_e, cambio_contrasenia)

    query="insert into usuarios_dirop (nombre ,usuario ,contrasenia ,roll ,tipo_unidad,unidad ,per_view ,per_select ,per_insert ,per_update ,per_delete ,resultados ,eventos ,usuarios ,chat ,conf_narcotrafico ,operaciones ,personal ,orden ,afectaciones_fuera_comabte ,boletin_coe ,boletin_cuadros_coe ,boletin_res_div ,cartilla_presidencial_larga ,cartilla_presidencial_corta ,boletin_diseo ,boletin_diseo_semanal ,comando_general ,Estadistica_resultados ,com_resultados_reducido ,narcotrafico ,artemisa ,artemisa_comparativo ,contrabando ,contrabando_comparativo ,mineria ,mineria_comparativo ,comparativo_enemigo ,comparativo_mapa ,comparativo_resultados ,afectacion_a_la_amenaza ,afectacion_comparativa_p_t ,lis_afectaciones ,afectaciones_mapa ,afectaciones_cuadros ,regiones ,resaltantes ,reslatantes_divisiones ,bullets ,boltin_dirop ,estadistica_eventos ,informe_eventos, unidad_dependencia, datos, cambio_contrasenia) values"+dato
    
    print(query)
    conexion_pos.conexion_comi(query)

    query = """select id from usuarios_dirop where nombre = '{}' and usuario = '{}' """.format(nombre, usuario)

    datos = conexion_pos.conexion(query)

    for x in datos:
        no_id = x[0]

    nombre_foto = str("/fotos_usurios/")+str(no_id)+"_"+str(foto)
    query = """UPDATE usuarios_dirop SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    conexion_pos.conexion_comi(query)

    query = "select * from usuarios_dirop"
    datos = conexion_pos.conexion(query)

    # for x in datos:
    #     print(x)

    conexion_pos.close()
    #     # data = datos.fetchone()

    return [nombre_foto, datos]

