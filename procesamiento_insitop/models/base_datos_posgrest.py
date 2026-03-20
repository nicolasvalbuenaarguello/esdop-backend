from datetime import datetime
# coding: utf-8
import psycopg2
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def save_data(data,  resultado, FECHA):
    global dato
    dato=0
    # print("---------------"*5)
    # print(str(data))
    conn = connect()
    cursor = conn.cursor()


    dato = """DELETE FROM registro_insitop WHERE FECHA_INSITOP = '{}' """.format(FECHA)
    cursor.execute(dato)
    conn.commit()

    dato = 'insert into registro_insitop( ARMA, FECHA_INSITOP, DEPARTAMENTO, MUNICIPIO, LUGAR, DETALLES_DEL_LUGAR, LATITUD, LONGITUD, SIGLA_DIVISION, SIGLA_BRIGADA, SIGLA_UNIDD, COMPANIA, PELOTON, COMANDANTE, CELULAR_COMANDANTE, OFICIALES, SUBOFICIALES, SLP, SL18, SL12, TOTAL_SOLDADOS, EXDE, LINEA_DE_OPERACIONES, ORD_ESC_BAT, CODE, OPERACION, TAREAS_ACCION_DECISIVA_TTF, TAREA, TECNICAS_ACTIVIDADES, TAREA_ESPECIAL, RELACION_DE_MANDO, OBSERVACIONES) values '+ data
    print("se cargo insitop")


    # print(dato)
    cursor.execute(dato)
    conn.commit()
    cursor.close()
    conn.close()
