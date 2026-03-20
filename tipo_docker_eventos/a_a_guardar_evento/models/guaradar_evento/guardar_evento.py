from datetime import datetime
# coding: utf-8
import psycopg2
import base64 

from os import getcwd
import os
import shutil
from dotenv import load_dotenv
load_dotenv()


#Funcion de resultados nueva ayuda
def connect():
    conn = psycopg2.connect(" \
        dbname=dirop \
        user=postgres \
        password=NICval10**")
    return conn

def guardar_foto(foto):
    with open('DOCUMENTO.ZIP', 'wb') as f:
        f.write(foto)

def guardar_evento(datos, nom_boletin, nom_radiograma, nom_denuncia, nom_inf_cdte_batallon):

    #datos

    numero_boletin_div = datos["numero_boletin_div"]
    fecha_evento = datos["fecha_evento"]
    hora_evento = datos["hora_evento"]
    divi_padre = datos["divi_padre"]
    divi_hija = datos["divi_hija"]
    brigada = datos["brigada"]
    batallon = datos["batallon"]
    amenaza = datos["amenaza"]
    subestructura = datos["subestructura"]
    departamento = datos["departamento"]
    municipios = datos["municipios"]
    sitio = datos["sitio"]
    lati = datos["lati"]
    coodnadas_lat_gr = datos["coodnadas_lat_gr"]
    coodnadas_lat_min = datos["coodnadas_lat_min"]
    coodnadas_lat_seg = datos["coodnadas_lat_seg"]
    loti = datos["loti"]
    coodnadas_lot_gr = datos["coodnadas_lot_gr"]
    coodnadas_lot_min = datos["coodnadas_lot_min"]
    coodnadas_lot_seg = datos["coodnadas_lot_seg"]
    evento = datos["evento"]
    resumen = datos["resumen"]
    denuncia = datos["denuncia"]
    numero_de_denuncia = datos["numero_de_denuncia"]
    fiscalia = datos["fiscalia"]
    estado = datos["estado"]

    numero_boletin_div = numero_boletin_div.upper()
    fecha_evento = fecha_evento.upper()
    hora_evento = hora_evento.upper()
    divi_padre = divi_padre.upper()
    divi_hija = divi_hija.upper()
    brigada = brigada.upper()
    batallon = batallon.upper()
    amenaza = amenaza.upper()
    subestructura = subestructura.upper()
    departamento = departamento.upper()
    municipios = municipios.upper()
    sitio = sitio.upper()

    evento = evento.upper()
    resumen = resumen.upper()
    denuncia = denuncia.upper()
    numero_de_denuncia = numero_de_denuncia.upper()
    fiscalia = fiscalia.upper()
    estado = estado.upper()

    permiso = datos["permiso"]
    unidad = datos["unidad"]

    if lati =="LN":
        cordenada_x= ((int(coodnadas_lat_gr)+int(coodnadas_lat_min)/60)+(float(coodnadas_lat_seg)/3600))*1
    else:
        cordenada_x= ((int(coodnadas_lat_gr)+int(coodnadas_lat_min)/60)+(float(coodnadas_lat_seg)/3600))-1

    if loti=="LW":

        cordenada_y= ((int(coodnadas_lot_gr)+int(coodnadas_lot_min)/60)+(float(coodnadas_lot_seg)/3600))*-1
    else:
        cordenada_y= ((int(coodnadas_lot_gr)+int(coodnadas_lot_min)/60)+(float(coodnadas_lot_seg)/3600))*1


    # print(documento)

    # image_64_encode = base64.encode(documento)

    dato="""('{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}','{}', '{}',{}, {},'{}', '{}','{}', '{}','{}', '{}')""".format(numero_boletin_div, fecha_evento, hora_evento, divi_padre, divi_hija, brigada, batallon, amenaza, subestructura, departamento, municipios, sitio, lati, coodnadas_lat_gr, coodnadas_lat_min, coodnadas_lat_seg, loti, coodnadas_lot_gr, coodnadas_lot_min, coodnadas_lot_seg,cordenada_x, cordenada_y, evento, resumen, denuncia, numero_de_denuncia, fiscalia, estado)

    query="insert into eventos (boletin_interno, fecha, hora, agr_div, division, brigada, unidad, amenaza, subestructura, departamento, municipio, sitio, latitud, gr_n, m_n, s_n, longitud, gr_l, m_l, s_l, coordenadas_x, coordenadas_y, tipo_evento, resumen, denuncia, numero_denuncia, fiscalia, estado ) values"+dato

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    query = """select id_no from view_eventos where boletin_interno = '{}' and fecha = '{}' and agr_div = '{}' and division = '{}' and brigada = '{}' and unidad = '{}'""".format(numero_boletin_div, fecha_evento, divi_padre, divi_hija, brigada, batallon)

    # conn = connect()
    # cursor = conn.cursor()

    cursor.execute(query)
    
    data = cursor.fetchall()
    for x in data:
        id = x[0]
        if nom_boletin != "falta":
            nom_boletin =str("Boletin_EJC_No_")+ str(id) +"_"+ str(divi_padre)+str("_Boletin_int_No_")+str(numero_boletin_div)+str("_")+str(fecha_evento) +"_boletin.pdf"

        if nom_radiograma != "falta":
            nom_radiograma =str("Boletin_EJC_No_")+ str(id) +"_"+ str(divi_padre)+str("_Boletin_int_No_")+str(numero_boletin_div)+str("_")+str(fecha_evento) +"_radiograma.pdf"
        
        if nom_denuncia != "falta":
            nom_denuncia =str("Boletin_EJC_No_")+ str(id) +"_"+ str(divi_padre)+str("_Boletin_int_No_")+str(numero_boletin_div)+str("_")+str(fecha_evento) +"_denuncia.pdf"
        
        if nom_inf_cdte_batallon != "falta":
            nom_inf_cdte_batallon =str("Boletin_EJC_No_")+ str(id) +"_"+ str(divi_padre)+str("_Boletin_int_No_")+str(numero_boletin_div)+str("_")+str(fecha_evento) +"_informe_bat.pdf"


        DIRECION_EVENTOS = os.getenv('DIRECION_EVENTOS')
        unidades =["DAVAA", "DIV01", "DIV02", "DIV03", "DIV04", "DIV05", "DIV06", "DIV07", "DIV08", "DIVFE", "FTCEC", "FUTCO", "TREJC"]
        for div in unidades:
            if div == divi_padre :
                    
                    direcion = DIRECION_EVENTOS + str("/") + str(div)  + str("/") 
                    direcion_serve = str("/documentos_eventos/") + str(div)  + str("/" )

                    query = """UPDATE eventos SET direcion = '{}', nom_boletin = '{}', nom_radiograma = '{}', nom_denuncia = '{}', nom_inf_cdte_batallon = '{}' WHERE id_no = {}""".format(direcion_serve, nom_boletin, nom_radiograma, nom_denuncia, nom_inf_cdte_batallon, id)
                    cursor.execute(query)
                    conn.commit()
                    
        if  permiso == "EJC":

            query_eventos =  "SELECT * FROM view_eventos ORDER BY FECHA ASC"
        else:

            query_eventos =  "SELECT * FROM view_eventos where {} = '{}' ORDER BY FECHA ASC".format(permiso, unidad)
            
        cursor.execute(query_eventos)
        data = cursor.fetchall()
        conn.close()
        cursor.close

        return [nom_boletin, nom_radiograma, nom_denuncia, nom_inf_cdte_batallon, direcion, data]