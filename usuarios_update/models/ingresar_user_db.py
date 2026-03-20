from datetime import datetime
# coding: utf-8
from __init__ import *
from models.conexion_pos import *
from werkzeug.security import check_password_hash, generate_password_hash
def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor

def update_evento(datos, foto, acta_reserva_file_nombres):
    conexion_pos = Databa_bases()

    #datos
    usuario = datos["usuario"]
    id_user = datos["id_user"]
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
    narcotrafico_metas = validar_check(datos["narcotrafico_metas"])
    docna_semanal = validar_check(datos["docna_semanal"])
    
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
    dato = validar_check(datos["datos"])
    cambio_contrasenia = validar_check(datos["cambio_contrasenia"])
    alerta = validar_check(datos["alerta"])
    movimientos = validar_check(datos["movimientos"])
    inventarios = validar_check(datos["inventarios"])
    boletin_mapa_comparativa = validar_check(datos["boletin_mapa_comparativa"])
    resaltantes_boletin = validar_check(datos["resaltantes_boletin"])

    excel_ut = validar_check(datos["excel_ut"])
    excel_amenaza = validar_check(datos["excel_amenaza"])

    resaltantes_mapa = validar_check(datos["excel_amenaza"])

    resultados_excel_tipo_operaciones = validar_check(datos["resultados_excel_tipo_operaciones"])

    archivo_spoa = validar_check(datos["archivo_spoa"])
    mapa_division_dinamico = validar_check(datos["mapa_division_dinamico"])

    aetcr = validar_check(datos["aetcr"])
    ingreso_aetcr = validar_check(datos["ingreso_aetcr"])
    listado_aetcr = validar_check(datos["listado_aetcr"])
    alerta_aetcr = validar_check(datos["alerta_aetcr"])

    plazos = validar_check(datos["plazos"])

    asignacion_plazo = validar_check(datos["asignacion_plazo"])
    reasignacion_plazo = validar_check(datos["reasignacion_plazo"])
    validacion_plazo = validar_check(datos["validacion_plazo"])
    creacion_plazo = validar_check(datos["creacion_plazo"])
    cumplimiento_plazo = validar_check(datos["cumplimiento_plazo"])
    medallas = validar_check(datos["medallas"])
    excel_anios = validar_check(datos["excel_anios"])

    seguimineto_plazos_respueta = validar_check(datos["seguimineto_plazos_respueta"])

    insitop_per = validar_check(datos["insitop_per"])
    cargue_insitop = validar_check(datos["cargue_insitop"])
    estadistica_insitop = validar_check(datos["estadistica_insitop"])

    dicte = validar_check(datos["dicte"])
    dicte_pasos_fronterizos = validar_check(datos["dicte_pasos_fronterizos"])

    com_div_mapa = validar_check(datos["com_div_mapa"])
    comp_div_mapa_bal = validar_check(datos["comp_div_mapa_bal"])

    eventos_relevantes = validar_check(datos["eventos_relevantes"])
    archivo_plano_excel = validar_check(datos["archivo_plano_excel"])
    res_lineas_estrategicas = validar_check(datos["res_lineas_estrategicas"])

    configuracion_especial_res  = validar_check(datos["configuracion_especial_res"])

    res_linea_obj_4   = validar_check(datos["res_linea_obj_4"])
    linea_estrategica_narcotrafico = validar_check(datos["linea_estrategica_narcotrafico"])
    ayuda_comparativa_consejos = validar_check(datos["ayuda_comparativa_consejos"])

    registro_Q5 = validar_check(datos["registro_Q5"])
    
    obj_1 = validar_check(datos["obj_1"])
    obj_2 = validar_check(datos["obj_2"])
    obj_3 = validar_check(datos["obj_3"])
    obj_4 = validar_check(datos["obj_4"])

    query="""UPDATE `usuarios_dirop` SET `roll`='{}',`tipo_unidad`='{}',`unidad`='{}',`per_view`={},`per_select`={},`per_insert`={},`per_update`={},`per_delete`={},`resultados`={},`eventos`={},`usuarios`={},`chat`={},`conf_narcotrafico`={},`operaciones`={},`personal`={},`orden`={},`afectaciones_fuera_comabte`={},`boletin_coe`={},`boletin_cuadros_coe`={},`boletin_res_div`={},`cartilla_presidencial_larga`={},`cartilla_presidencial_corta`={},`boletin_diseo`={},`boletin_diseo_semanal`={},`comando_general`={},`Estadistica_resultados`={},`com_resultados_reducido`={},`narcotrafico`={}, `artemisa`={},`artemisa_comparativo`={},`contrabando`={},`contrabando_comparativo`={},`mineria`={},`mineria_comparativo`={},`comparativo_enemigo`={},`comparativo_mapa`={},`comparativo_resultados`={},`afectacion_a_la_amenaza`={},`afectacion_comparativa_p_t`={},`lis_afectaciones`={},`afectaciones_mapa`={},`afectaciones_cuadros`={},`regiones`={},`resaltantes`={},`reslatantes_divisiones`={},`bullets`={},`boltin_dirop`={},`estadistica_eventos`={},`informe_eventos`={}, datos={}, cambio_contrasenia={}, alerta={}, movimientos={},inventarios={}, boletin_mapa_comparativa ={}, narcotrafico_metas ={}, docna_semanal ={}, resaltantes_boletin ={} , excel_ut ={}, excel_amenaza={}, resaltantes_mapa ={}, tipo_operacion ={} , archivo_spoa ={} , mapa_division_dinamico ={} , aetcr ={}, ingreso_aetcr ={}, listado_aetcr ={}, alerta_aetcr ={}, plazos = {} , asignacion_plazo = {} , reasignacion_plazo = {} , validacion_plazo = {} , creacion_plazo = {} , cumplimiento = {}, medallas ={}, excel_anios={}, seguimineto_plazos_respueta = {}, insitop_per = {}, cargue_insitop = {}, estadistica_insitop = {}, dicte = {}, dicte_pasos_fronterizos = {} , com_div_mapa = {}, comp_div_mapa_bal = {}, eventos_relevantes = {}, archivo_plano_excel = {}, res_lineas_estrategicas = {}, configuracion_especial_res = {}, res_linea_obj_4={}, linea_estrategica_narcotrafico={} , ayuda_comparativa_consejos={}, q5={}, obj_1={}, obj_2={}, obj_3={}, obj_4={}  WHERE `id`={}""".format(roll, tipo_unidad, unidad, view, select, insert, update, deletes, resultados, eventos, usuarios, chat, conf_narcotrafico, operaciones, personal, orden, afectaciones_fuera_comabte, boletin_coe, boletin_cuadros_coe, boletin_res_div, cartilla_presidencial_larga, cartilla_presidencial_corta, boletin_diseo, boletin_diseo_semanal, comando_general, Estadistica_resultados, com_resultados_reducido, narcotrafico, artemisa, artemisa_comparativo, contrabando, contrabando_comparativo, mineria, mineria_comparativo, comparativo_enemigo, comparativo_mapa, comparativo_resultados, afectacion_a_la_amenaza, afectacion_comparativa_p_t, lis_afectaciones, afectaciones_mapa, afectaciones_cuadros, regiones, resaltantes, reslatantes_divisiones, bullets, boltin_dirop, estadistica_eventos, informe_eventos, dato,cambio_contrasenia,alerta, movimientos,inventarios, boletin_mapa_comparativa, narcotrafico_metas, docna_semanal, resaltantes_boletin, excel_ut, excel_amenaza, resaltantes_mapa, resultados_excel_tipo_operaciones,archivo_spoa, mapa_division_dinamico, aetcr, ingreso_aetcr, listado_aetcr, alerta_aetcr, plazos, asignacion_plazo, reasignacion_plazo, validacion_plazo, creacion_plazo, cumplimiento_plazo, medallas, excel_anios, seguimineto_plazos_respueta, insitop_per, cargue_insitop, estadistica_insitop, dicte, dicte_pasos_fronterizos, com_div_mapa, comp_div_mapa_bal, eventos_relevantes, archivo_plano_excel, res_lineas_estrategicas, configuracion_especial_res, res_linea_obj_4, linea_estrategica_narcotrafico, ayuda_comparativa_consejos, registro_Q5, obj_1, obj_2, obj_3, obj_4, id_user)

    
    conexion_pos.conexion_comi(query)

    
    query = """select id from usuarios_dirop where nombre = '{}' and usuario = '{}' """.format(nombre, usuario)

    data = conexion_pos.conexion(query)

    for x in data:
        no_id = x[0]
    if foto !="validar":
        nombre_foto = str("/fotos_usurios/")+str(no_id)+"_"+str(foto)
    else:
        nombre_foto = datos["foto_2"]

    if acta_reserva_file_nombres !="validar":
        nombre_actas_reserva = str("/actas_reserva/")+str(no_id)+"_"+str(acta_reserva_file_nombres)
    else:
        nombre_actas_reserva = datos["acta_reserva_2"]

    query = """UPDATE usuarios_dirop SET foto = '{}' WHERE id = '{}' ;""".format(nombre_foto, no_id)
    conexion_pos.conexion_comi(query)

    query = """UPDATE usuarios_dirop SET acta_reserva_file = '{}' WHERE id = '{}' ;""".format(nombre_actas_reserva, no_id)
    conexion_pos.conexion_comi(query)

    query = "select * from usuarios_dirop"
    datos = conexion_pos.conexion(query)

    # for x in datos:
    #     print(x)

    conexion_pos.close()

    return [nombre_foto, nombre_actas_reserva, datos]


def delete_evento(datos):
    conexion_pos = Databa_bases()

    #datos

    id_user = datos["id_user"]

    query="""DELETE FROM `usuarios_dirop` WHERE id = {}""".format(id_user)
    # print(query)
    
    conexion_pos.conexion_comi(query)

    query = "select * from usuarios_dirop"
    datos = conexion_pos.conexion(query)

    # for x in datos:
    #     print(x)

    conexion_pos.close()
    #     # data = datos.fetchone()

    return [datos]
@staticmethod
def check_password(hashed_password: str, plain_password: str) -> bool:
        try:
            return check_password_hash(hashed_password, plain_password)
        except Exception as e:
            print(f"Error al verificar contraseña: {e}")
            return False



def cambio_contrasena(datos):
    """
    Actualiza la contraseña de un usuario solo si:
    - La contraseña actual es correcta
    - El user_name coincide
    - La unidad coincide
    """

    # 🔹 Extraer datos recibidos
    contrasenia_actual = datos.get("actual")
    contrasenia_nueva = datos.get("nueva")
    user_name = datos.get("fullname")
    unidad = datos.get("unidad")

    conexion_pos = Databa_bases()

    try:
        # 🔹 Buscar el usuario en la base de datos
        query = f"""
        SELECT id, contrasenia, unidad 
        FROM usuarios_dirop 
        WHERE nombre = '{user_name}'
        """
        resultado = conexion_pos.conexion(query)

        if not resultado:
            return {"success": False, "msg": "Usuario no encontrado"}

        # 🔹 Suponiendo que resultado es una lista de tuplas y tomamos la primera fila
        row = resultado[0]
        id_user = row[0]
        hash_actual = row[1]
        unidad_db = row[2]

        # 🔹 Validar unidad
        if unidad != unidad_db:
            return {"success": False, "msg": "Unidad no coincide"}

        # 🔹 Validar contraseña actual
        if not check_password_hash(hash_actual, contrasenia_actual):
            return {"success": False, "msg": "Contraseña actual incorrecta"}

        # 🔹 Actualizar la contraseña
        nueva_hash = generate_password_hash(contrasenia_nueva)
        update_query = f"""
        UPDATE usuarios_dirop
        SET contrasenia = '{nueva_hash}'
        WHERE id = {id_user}
        """
        conexion_pos.conexion_comi(update_query)

        return {"success": True, "msg": "Contraseña actualizada correctamente"}

    except Exception as e:
        return {"success": False, "msg": str(e)}

    finally:
        conexion_pos.close()
