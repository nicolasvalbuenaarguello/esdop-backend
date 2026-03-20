from datetime import datetime
# coding: utf-8
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def save_data(data,  resultado):
    global dato
    dato=0
    print("---------------")
    # print(str(data))
    conn = connect()
    cursor = conn.cursor()
    query = "delete from formulario_1_dipse"
    cursor.execute(query)
    conn.commit()

    dato = 'insert into formulario_1_dipse (NIT_institucion  , 	NIT_iContratista , 	Institucion_a_la_que_pertenece , 	Clasificacion_de_la_novedad , 	Si_eligio_otro_diga_cual , 	Tipo_de_vinculación_del_Accidentado_Lesionado , 	Jefatura_de_Estado_Mayor_organico , 	Division_organico , 	Comando_organico , 	Fuerza_de_tarea_organico , 	CEDE_organico , 	Brigada_Dirección_Regimiento_organico , 	Unidad_organico , 	Jefatura_de_Estado_Mayor_actual , 	Division_actual , 	Comando_actual , 	Fuerza_de_tarea_actual , 	CEDE_actual , 	Brigada_Dirección_Regimiento_actual , 	Unidad_actual , 	EPS_a_la_que_pertenece , 	ARL_a_la_que_pertenece , 	Fecha_del_evento , 	Hora , 	Ciudad_Municipio , 	Departamento , 	Vereda_corregimiento_o_barrio , 	grd_lat , 	min_lat , 	seg_lat , 	grd_lot , 	min_lot , 	seg_lot , 	Caracteristicas_del_lugar , 	Sitio_especifico , 	Grado_cdte_directo , 	Nombre_cdte_directo , 	Cargo_cdte_directo , 	Grado_cdte_segundo_nivel , 	Nombre_cdte_segundo_nivel , 	Cargo_cdte_segundo_nivel , 	Documento_de_identidad , 	Grado , 	Nombre_y_apellido , 	Ciudad_afectado , 	Departamento_afectado , 	Dirección_de_la_persona_afectado , 	Fecha_de_ingreso_a_la_institución_afectado , 	Cargo_afectado , 	Tiempo_total_de_servicio_anio , 	Tiempo_total_de_servicio_meses , 	Telefono_de_contacto_lesionado , 	Telefono_de_contacto_acudiente , 	Salarios_u_Honorarios_Mensual_PERSONAL_DE_PLANTA , 	Atencion_inmediata_que_se_dio_al_evento , 	Sexo , 	Fecha_de_nacimiento , 	Edad , 	Parte_del_cuerpo_aparentemente_afectada , 	Descipcion_parte_del_cuerpo_afectada , 	Tiempo_de_Experiencia_anio , 	Tiempo_de_Experiencia_meses , 	Resumen , 	Actividad_realizada_en_el_momento_del_evento , 	CLASE_NOVEDAD , 	TIPO_DE_NOVEDAD , 	Estaba_realizando_su_actividad_habitua , 	Si_eligio_cual , 	Tiempo_laborado_el_día_de_la_novedad , 	Causo_la_muerte_de_la_persona , 	Identificacion_del_peligro_o_amenaza , 	Agente_de_la_lesion , 	Mecanismo_de_la_lesion , 	Otro_cual , 	Informacion_Vehiculo , 	Tipo_de_Vehiculo , 	Placas_o_sigla , 	Marca , 	Nombre_testigo , 	Telefono_testigo , 	Nombre_quien_reporta_arl , 	Grado_quien_reporta_arl , 	Cargo_quien_reporta_arl , 	Nombre_quien_reporta , 	Grado_quien_reporta , 	Cargo_quien_reporta , 	Nombre_cdte , 	Grado_cdte , 	OBSERVACIONES , 	FECHA_REPORTE , 	NUMERO_DE_RADICADO_ARL  , 	DIAS_DE_INCAPACIDAD , 	RECUPERADO_SI_NO , 	OBSERVACION_RECUPERADO , 	RADICADO_SIJEN_INVESTIGACION_DISCIPLINARIA  , 	ESTADO_INVESTIGACION_DISCIPLINARIA , 	OBSERVACIONES_INVESTIGACIONES_DISCIPLINARIAS , 	RADICADO_SIJEN_INVESTIGACION_ADMINISTRATIVAS  , 	ESTADO_INVESTIGACION_ADMINISTRATIVA , 	OBSERVACIONES_INVESTIGACIONES_ADMINISTRATIVAS , 	LITERAL_INFORMATIVO_ADMINISTRATIVO_POR_LESION , 	OBSERVACION_INFORMATIVOS_ADMINISTRATIVOS_POR_LESION , 	TIPO_NOVEDAD ) values '+ data
    
    print("se cargo dispse")


    # print(dato)
    cursor.execute(dato)
    conn.commit()
    cursor.close()
    conn.close()
