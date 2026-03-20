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

    dato = """DELETE FROM pazos_fronterizos WHERE fecha_pazos = '{}' """.format(FECHA)
    cursor.execute(dato)
    conn.commit()

    dato = 'insert into pazos_fronterizos (fecha_pazos, paso, nombre_paso, tipo_paso, latitud, lat_g, lat_m, lat_s, longitud, lot_g, lot_m, lot_s, pais, departamento, municipio, responsabilidad, div, br, ut, indicativo, cdte, ofi, sub, slp, sl18, latitud_unidad, lat_unidad__g, lat_unidad__m, lat_unidad__s, longitud_unidad, lot_unidad__g, lot_unidad__m, lot_unidad__s, distancia, base, evento_ultimas_horas, x, y, x_2, y_2) values {}'.format(data)

    print("se cargo pazos_fronterizos")

    # print(dato)
    cursor.execute(dato)
    conn.commit()
    cursor.close()
    conn.close()

def save_data_pasos(data,  resultado):
    global dato
    dato=0
    # print("---------------"*5)
    # print(str(data))
    conn = connect()
    cursor = conn.cursor()

    dato = """DELETE FROM pazos_fronterizos_directiva  """
    cursor.execute(dato)
    conn.commit()

    dato = 'insert into pazos_fronterizos_directiva (OID, Codigo, Topologia, Division, Brigada, Batallon, Lugar, Municipio, Departamen, Frontera, Tipo_de_Pa, Responsabi, x, y) values {}'.format(data)

    print("se cargo pazos_fronterizos_directiva")


    # print(dato)
    cursor.execute(dato)
    conn.commit()
    cursor.close()
    conn.close()
