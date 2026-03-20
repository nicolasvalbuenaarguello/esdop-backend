import os
from datetime import datetime
from flask import make_response
from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.models.estadistica.estadistica_boletin_coe import Calculo_Spoa
from tipo_docker.z_z_configuarcion.caligrafia import caligrafia_ingreso
from tipo_docker.z_z_configuarcion.fechas import fecha
from tipo_docker.z_z_configuarcion.header import *
from tipo_docker.z_z_configuarcion.logo import *
from tipo_docker.z_z_configuarcion.titulos import titulos_name_2

def comparativo_comparativo_mapa(
    fecha_inicial_u_l, fecha_final_u_l,
    fecha_inicial_p_l, fecha_final_p_l,
    filtro, dir_archivos, nombre_carpeta
):
    # Crear nombre de PDF
    nombre_pdf = "Ayuda Consejo Seguridad"
    nombre_archivo = f"{nombre_pdf}.pdf"

    # Preparar PDF
    pdf = PDF(orientation='L', unit='mm', format=(190.5, 338.67))
    caligrafia_ingreso(pdf, filtro[15])  # ❗ Mejor si filtro fuera dict o objeto

    # Fechas formateadas
    f1 = fecha(fecha_inicial_u_l)
    f2 = fecha(fecha_final_u_l)
    f3 = fecha(fecha_inicial_p_l)
    f4 = fecha(fecha_final_p_l)

    anio_titulo = f2[2]
    anio_tres = int(anio_titulo) - 1

    titulo_unidad = titulos_name_2(filtro, anio_titulo)
    municipios = tuple(titulo_unidad[1]) if titulo_unidad[1] else ""
    titulo = titulo_unidad[0]

    # Fechas para títulos
    fecha_titulo_1 = f"{f1[0]} {f1[1]} AL {f2[0]} {f2[1]} {f2[2]}".upper()
    fecha_titulo_2 = f"{f3[0]} {f3[1]} AL {f4[0]} {f4[1]} {f4[2]}".upper()
    fecha_titulo_3 = f"{f3[0]} {f3[1]} AL {f4[0]} {f4[1]} {anio_tres}".upper()
    fecha_anio_tres_inicial = f"{anio_tres}-{f3[3]}-{f3[0]}"
    fecha_anio_tres_final = f"{anio_tres}-{f4[3]}-{f4[0]}"

    # Parámetros visuales
    imagen = "static/img/oficio/consejo.jpeg"
    fecha_titulo_sub = 'Debilitar las capacidades de la amenaza'

    pdf.parametros(
        titulo=titulo,
        fecha_titulo=fecha_titulo_sub,
        tamanio="presentacion",
        logo=filtro[11],
        permiso=filtro[12],
        nivel=filtro[13],
        usuario=filtro[14],
        pie_pagina="SI",
        ruta=filtro[15],
        imagen=imagen,
        seguridad="nueva"
    )

    pdf.set_auto_page_break(True, 5)
    pdf.add_page()

    # Cálculos estadísticos
    fechas_final = fecha(fecha_final_u_l)
    fechas_inicial = fecha(fecha_final_p_l)

    calculo = Calculo_Spoa()
    calculo.comparativo_mapa(
        pdf, fecha_inicial_u_l, fecha_final_u_l, fecha_inicial_p_l, fecha_final_p_l,
        filtro, fechas_final[2], fechas_inicial[2],
        fecha_titulo_1, fecha_titulo_2, fecha_titulo_3,
        fecha_anio_tres_inicial, fecha_anio_tres_final, anio_tres, municipios
    )

    # Guardar archivo
    path_final = os.path.join(dir_archivos, nombre_archivo)
    pdf.output(path_final, 'F')

    # Ruta pública
    base_publica = os.getenv("DIRECION_3")
    if not base_publica:
        raise EnvironmentError("DIRECION_3 no está definida en variables de entorno")

    url_archivo = os.path.join(base_publica, nombre_carpeta, nombre_archivo)

    return [url_archivo, nombre_pdf]
