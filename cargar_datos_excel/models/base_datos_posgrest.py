from datetime import datetime
# coding: utf-8
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def save_data(data, resultado):
    from psycopg2.extras import execute_values

    conn = connect()
    cursor = conn.cursor()

    if resultado == "HECHOS":
        query = '''
            INSERT INTO hechos(
                HR, HECHO, BOLETIN, FECHA_HECHO, ACCION_ENEMIGA, DIVISION, BRIGADA, UNIDAD, DPTO, MPIO, SITIO, LUGAR,
                ENEMIGO, RESUMEN_HECHOS, LATITUD, LONGITUD, ESTRATEGIA_AFECTA, HOP_ACCION_DAVAA, HOP_HECHO_POS,
                AGR_DIV, HOP_INICIATIVA, CANTIDAD, HOP_OPERACION, HOP_APOYO_BLICA, HOP_APOYO_CONAT, HOP_ORDOP,
                HOP_COMANDANTE, HOP_COMPANIA, HOP_PELOTON, HOP_CLASE_SOLDADO, HOP_PROC_INFO, HOP_EXITO, HOP_HORA_HECHO,
                coordinada, conjunta, tipo_operacion, acam_enemigo, acam_estructura, ene_estructura, HOP_ACCION_CCOES, 
                HOP_APOYO_AEREO, HOP_APOYO_ART, HOP_APOYO_BAFUR, HOP_APOYO_BRCMI, HOP_APOYO_BRCOM, HOP_APOYO_DIVFE, 
                HOP_APOYO_EXDE, HOP_APOYO_FUDAT, HOP_APOYO_GROIC, 	hop_asalto_aereo, apoyo_coeej, unidad_brcmi
            ) VALUES %s
        '''
    elif resultado == "RESULTADOS":
        query = '''
            INSERT INTO resultados(
                HR, RES_BOLETIN, HOP_HECHO, HOP_HORA_HECHO, HOP_FECHA_HECHO, HOP_MES_HECHO, HOP_DEPTO, HOP_MPIO,
                HOP_LUGAR, HOP_SITIO, HOP_DIV, HOP_BR, HOP_UNIDAD, HOP_ENEMIGO, CANTIDAD, HOP_CUADRILLA, HOP_OPERACION,
                HOP_ORDOP, RES_ACCION, HOP_ACCION_ENEMIGA, RES_TIPO, RES_SUBTIPO, RES_CLASE, RES_NUMDOC, RES_GRADO,
                RES_NOMBRE, RES_EDAD, RES_SEXO, RES_ESPECIALIDAD, RES_NIVEL_JER, RES_ARMA, HOP_COMANDANTE,
                HOP_RESUMEN_HECHOS, HOP_LAT, HOP_LON, RES_JUDIC, RES_FECHA_JUDIC, UNIDAD, RES_SPOA, RES_SIGAHD,
                HOP_APOYO_BLICA, HOP_APOYO_CONAT, HOP_ACCION_DAVAA, FENOMENO_DE_CRIMINALIDAD, AGR_DIV, HOP_TIPO_OP,
                HOP_HECHO_POS, coordinada, conjunta, tipo_operacion, acam_enemigo, acam_estructura, ene_estructura, 
                HOP_ACCION_CCOES, HOP_APOYO_AEREO, HOP_APOYO_ART, HOP_APOYO_BAFUR, HOP_APOYO_BRCMI, HOP_APOYO_BRCOM, 
                HOP_APOYO_DIVFE, HOP_APOYO_EXDE, HOP_APOYO_FUDAT, HOP_APOYO_GROIC, HOP_APOYO_PJ, HOP_ASALTO_AEREO, apoyo_coeej, unidad_brcmi
            ) VALUES %s
        '''
    elif resultado == "ERRADICACION":
        query = '''
            INSERT INTO erradicacion(
                UNIDAD, AGR_DIV, HOP_DIV, HOP_BR, HOP_UNIDAD, FASE, MPIO_ERRADICACION, SITIO_ERRADICACION,
                DEPTO_ERRADICACION, METODO, ENTIDAD, CANTIDAD
            ) VALUES %s
        '''
    else:
        raise ValueError("Tipo de resultado no válido")

    try:
        execute_values(cursor, query, data)
        conn.commit()
        print(f"Se cargó {resultado}")
    except Exception as e:
        conn.rollback()
        print(f"Error insertando {resultado}: {e}")
        raise
    finally:
        cursor.close()
        conn.close()
