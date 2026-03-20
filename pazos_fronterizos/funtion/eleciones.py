import psycopg2
import matplotlib.pyplot as plt
import numpy as np
        
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Wedge
import matplotlib.pyplot as plt
import numpy as np
import os
from models.funciones.mapa_filtro import *

import matplotlib.pyplot as plt
import numpy as np

    # --- Función auxiliar para rotar en FPDF ---
from contextlib import contextmanager
import math

class Funciones_eleciones:
    def __init__(self, pdf, fecha,  dia, mes, anio):
        self.fecha = fecha
        self.pdf = pdf
        self.dia =  dia 
        self.anio = anio 
        self.mes = mes


    @contextmanager
    def rotated(pdf, angle, x=None, y=None):
        """Permite rotar contenido temporalmente en FPDF"""
        if x is None:
            x = pdf.get_x()
        if y is None:
            y = pdf.get_y()
        pdf._out(f'q {math.cos(math.radians(angle)):.5f} {math.sin(math.radians(angle)):.5f} '
                f'{-math.sin(math.radians(angle)):.5f} {math.cos(math.radians(angle)):.5f} '
                f'{(x * (1 - math.cos(math.radians(angle))) - y * math.sin(math.radians(angle))):.5f} '
                f'{(y * (1 - math.cos(math.radians(angle))) + x * math.sin(math.radians(angle))):.5f} cm')
        yield
        pdf._out('Q')

        #Funcion de resultados nueva ayuda
    def connect():
        conn = psycopg2.connect(" \
            dbname=dirop \
            user=postgres \
            password=NICval10**")
        return conn



    def grafico_reloj(ruta_salida, velocidad=0):
        """
        Genera un velocímetro tipo reloj y guarda la imagen PNG en la ruta indicada.
        Parámetros:
        - ruta_salida: ruta completa del archivo a guardar (sin extensión o con .png)
        - velocidad: valor entre 0 y 100
        """

        velocidad_max = 100
        velocidad = max(0, min(velocidad, velocidad_max))  # límite 0–100

        # --- Cálculo del ángulo ---
        angulo = np.deg2rad(-145 + (velocidad / velocidad_max) * 290)

        # --- Crear figura polar ---
        fig, ax = plt.subplots(figsize=(6, 6), subplot_kw={'projection': 'polar'})
        ax.set_theta_zero_location('N')
        ax.set_theta_direction(-1)
        ax.set_thetamin(-145)
        ax.set_thetamax(145)
        ax.set_ylim(0, 1)
        ax.set_yticklabels([])
        ax.set_xticklabels([])
        ax.grid(False)
        ax.spines['polar'].set_visible(False)

        # --- Fondo gris del arco ---
        theta_full = np.linspace(np.deg2rad(-145), np.deg2rad(145), 500)
        r_inner, r_outer = 0.1, 0.9
        for i in range(len(theta_full) - 1):
            ax.fill_between(
                [theta_full[i], theta_full[i + 1]],
                r_inner, r_outer,
                color="#D0D0D0",
                alpha=0.6
            )

        # --- Colorear según la velocidad ---
        def color_por_velocidad(v):
            if v < 35:
                return "#FF0000"     # rojo
            elif v < 50:
                return "#FFA600"     # naranja
            elif v < 80:
                return "#FFFF00"     # amarillo
            else:
                return "#00FF00"     # verde

        color = color_por_velocidad(velocidad)

        theta_color = np.linspace(
            np.deg2rad(-145),
            np.deg2rad(-145 + (velocidad / velocidad_max) * 290),
            300
        )

        for i in range(len(theta_color) - 1):
            ax.fill_between(
                [theta_color[i], theta_color[i + 1]],
                r_inner, r_outer,
                color=color,
                alpha=0.9
            )

        # --- Líneas divisorias y numeración ---
        for v in range(0, velocidad_max + 1, 10):
            ang = np.deg2rad(-145 + (v / velocidad_max) * 290)
            ax.plot([ang, ang], [r_inner, r_outer], color='white', linewidth=2, zorder=6)

            # Texto de numeración
            r_text = r_outer + 0.08  # posición radial del texto
            ax.text(ang, r_text, str(v), ha='center', va='center',
                    color='gray', fontsize=25, fontweight='bold')

        # --- Aguja ---
        ax.plot([angulo, angulo], [0, 0.85], color='black', linewidth=3, zorder=10)
        ax.scatter(0, 0, color='black', s=120, zorder=11)


        # --- Fondo y guardado ---
        fig.patch.set_facecolor("#00000000")
        ax.set_facecolor("#404040")

        # Asegurar extensión PNG con nombre fijo
        if not ruta_salida.lower().endswith("velocimetro_dicte.png"):
            if not ruta_salida.endswith(("/", "\\")):
                ruta_salida += "_"
            ruta_salida += "velocimetro_dicte.png"

        plt.savefig(ruta_salida, dpi=100, bbox_inches='tight', transparent=True)
        plt.close(fig)

        return ruta_salida


    def lamina_3(self, pdf_temp, division):
        # 🔹 Conexión segura con context manager
        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            if division != "EJC":
                query = """
                SELECT 
                    SUM(total_potencial) AS cantidad,
                    SUM(hombres) AS hombres,
                    SUM(mujeres) AS mujeres,
                    SUM(mesas) AS mesas_votacion,
                    COUNT(*) AS puestos_votacion,
                    SUM(CASE WHEN UPPER(TRIM(rural)) = 'X' THEN 1 ELSE 0 END) AS rural,
                    SUM(CASE WHEN UPPER(TRIM(urbana)) = 'X' THEN 1 ELSE 0 END) AS urbano
                FROM puestos_votacion

                    WHERE division = %s
                """
                cursor.execute(query, (division,))
            else:
                query = """
                    SELECT 
                        SUM(total_potencial) AS cantidad,
                        SUM(hombres) AS hombres,
                        SUM(mujeres) AS mujeres,
                        SUM(mesas) AS mesas_votacion,
                        COUNT(*) AS puestos_votacion,
                        SUM(CASE WHEN UPPER(TRIM(rural)) = 'X' THEN 1 ELSE 0 END) AS rural,
                        SUM(CASE WHEN UPPER(TRIM(urbana)) = 'X' THEN 1 ELSE 0 END) AS urbano
                    FROM puestos_votacion;

                """
                cursor.execute(query)

            row = cursor.fetchone()

        # 🔹 Convertir a números formateados
        def fmt(valor):
            return f"{valor or 0:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

        cantidad, hombres, mujeres, mesas_votacion, puestos_votacion, rural, urbano = map(fmt, row)

        # 🔹 PDF
        pdf_temp.set_text_color(255, 255, 255)
        pdf_temp.set_font("BebasNeue", "", 18)
        pdf_temp.text(37, 28, str(self.mes))

        pdf_temp.set_text_color(3, 88, 39)
        pdf_temp.set_font("BebasNeue", "", 37)
        pdf_temp.text(35, 49, str(self.dia))

        pdf_temp.set_text_color(70, 70, 70)
        pdf_temp.set_font("BebasNeue", "", 16)
        pdf_temp.text(35, 55, str(self.anio))

        pdf_temp.set_text_color(3, 88, 39)
        pdf_temp.set_font("BebasNeue", "", 22)
        pdf_temp.text(60, 38, str(cantidad))

        pdf_temp.set_font("BebasNeue", "", 16)
        pdf_temp.text(88, 46, str(hombres))
        pdf_temp.text(88, 58, str(mujeres))

        pdf_temp.set_font("BebasNeue", "", 22)
        pdf_temp.text(13, 100, str(puestos_votacion))
        pdf_temp.text(85, 107, str(mesas_votacion))

        pdf_temp.set_font("BebasNeue", "", 18)
        pdf_temp.text(31, 112, str(rural))
        pdf_temp.text(31, 128, str(urbano))



    def lamina_4(self):
        div = ["DIV01","DIV02","DIV03","DIV04","DIV05","DIV06","DIV07","DIV08","FUTOM","TOTAL"]

        unidades = []  # lista acumulada
        color = (200, 200, 200)

        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()
            for x in div:
                if x != "TOTAL":
                    query = """
                        SELECT 
                                COUNT(*) AS puestos_votacion,
                                SUM(CASE WHEN UPPER(TRIM(ejercito_nacional)) = 'X' THEN 1 ELSE 0 END) AS ejercito_nacional,
                                SUM(CASE WHEN UPPER(TRIM(policia_nacional)) = 'X' THEN 1 ELSE 0 END) AS policia_nacional,
                                SUM(CASE WHEN UPPER(TRIM(ponal)) = 'X' THEN 1 ELSE 0 END) AS ponal,
                                SUM(CASE WHEN UPPER(TRIM(armada_nacional)) = 'X' THEN 1 ELSE 0 END) AS armada_nacional,
                                SUM(CASE WHEN UPPER(TRIM(cobertura)) = 'SI' THEN 1 ELSE 0 END) AS cobertura,
                                SUM(CASE WHEN UPPER(TRIM(comunidad_indigena)) = 'SI' THEN 1 ELSE 0 END) AS comunidad_indigena,
                                
                                SUM(total) AS total
                            FROM puestos_votacion

                        WHERE division = %s
                    """
                    cursor.execute(query, (x,))
                else:
                    query = """
                            SELECT 
                                COUNT(*) AS puestos_votacion,
                                SUM(CASE WHEN UPPER(TRIM(ejercito_nacional)) = 'X' THEN 1 ELSE 0 END) AS ejercito_nacional,
                                SUM(CASE WHEN UPPER(TRIM(policia_nacional)) = 'X' THEN 1 ELSE 0 END) AS policia_nacional,
                                SUM(CASE WHEN UPPER(TRIM(ponal)) = 'X' THEN 1 ELSE 0 END) AS ponal,
                                SUM(CASE WHEN UPPER(TRIM(armada_nacional)) = 'X' THEN 1 ELSE 0 END) AS armada_nacional,
                                SUM(CASE WHEN UPPER(TRIM(cobertura)) = 'SI' THEN 1 ELSE 0 END) AS cobertura,
                                SUM(CASE WHEN UPPER(TRIM(comunidad_indigena)) = 'SI' THEN 1 ELSE 0 END) AS comunidad_indigena,
                                SUM(total) AS total
                            FROM puestos_votacion;

                    """
                    cursor.execute(query)

                row = cursor.fetchone()

                # 🔹 Convertir a números formateados
                def fmt(valor):
                    return f"{valor or 0:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

                puestos_votacion, ejercito, policia, ponal, arc, cobertura, comunidad_indigena, total = map(fmt, row)

                # 🔹 Alternar colores de fila
                if x != "TOTAL":
                    color_tex =(0,0,0)
                    if color == (200, 200, 200):
                        color = (220, 220, 220)
                    else:
                        color = (200, 200, 200)
                else:
                    color = (55, 86, 36)  # verde oscuro para TOTAL
                    color_tex =(255,255,255)

                # 🔹 Guardar fila
                unidades.append({
                    "nombre": [x, puestos_votacion, ejercito, policia, ponal, arc, cobertura, comunidad_indigena, total],
                    "color": color,
                    "color_tex": color_tex
                    
                })



        # Definir encabezados y ancho de columnas
        headers = ["UNIDAD", "PUESTOS DE \nVOTACIÓN", "EJÉRCITO \nNACIONAL", 
                "POLICÍA \nNACIONAL", "EJC \nPONAL", "SAE", "PUESTOS \nCUBIERTOS", "COMUNIDAD\nINDIGENA", "DISP. \nTROPAS"]

        col_widths = [21, 21, 21, 21, 21, 21, 21, 21, 21]
        row_height = 5

        # Color de relleno (RGB)
        
        self.pdf.set_text_color(255, 255, 255)
        position = 10
        for x in headers:
            if x == 'EJÉRCITO \nNACIONAL':
                self.pdf.set_fill_color(125, 0, 0) 

            elif x == 'POLICÍA \nNACIONAL':
                self.pdf.set_fill_color(0, 170, 0) 
            else:
                self.pdf.set_fill_color(55, 86, 36)  # Rojo


            self.pdf.rect(position, 7, 21, 10, "DF")  # F = Fill (relleno)
            position = position + 21


        #self.pdf.set_fill_color(0, 255, 0)  # Verde
        #self.pdf.rect(70, 20, 50, 30, "FD")  # FD = Fill + Draw (borde + relleno)

        #self.pdf.set_fill_color(0, 0, 255)  # Azul
        #self.pdf.rect(130, 20, 50, 30, "D")  # D = solo bord


        # --- ENCABEZADOS ---
        self.pdf.cell(10)
        self.pdf.ln(-25)
        for i, header in enumerate(headers):
            x_before = self.pdf.get_x()
            y_before = self.pdf.get_y()
            self.pdf.multi_cell(col_widths[i], row_height, header, border=0, align="C")
            self.pdf.set_xy(x_before + col_widths[i], y_before)
        self.pdf.ln(row_height)
        self.pdf.ln()
        # --- FILAS ---



        row_height = 10

 
        # --- Filas ---
        for unidad in unidades:
            r,g,b = unidad["color"]   # color de texto para la fila
            r_tex,g_tex,b_tex = unidad["color_tex"]   # color de texto para la fila
            self.pdf.set_fill_color(r,g,b)
            self.pdf.set_text_color(r_tex,g_tex,b_tex)

            for i, dato in enumerate(unidad["nombre"]):
                self.pdf.cell(col_widths[i], row_height, dato, border=1, align="C", fill = True)
            self.pdf.ln(row_height)



    def lamina_5(self, pdf_temp, division, actualizarMapas):
        
        # 🔹 Convertir a números formateados
        def fmt(valor):
            return f"{valor or 0:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # 🔹 Conexión segura con context manager
        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            if division != "EJC":
                query = """
                        SELECT 
                            COUNT(*) AS puestos_votacion,
                            SUM(CASE WHEN UPPER(TRIM(rural)) = 'X' THEN 1 ELSE 0 END) AS rural,
                            SUM(CASE WHEN UPPER(TRIM(urbana)) = 'X' THEN 1 ELSE 0 END) AS urbana,
                            SUM(mesas) AS mesas_votacion
                        FROM puestos_votacion
                    WHERE division = %s
                """
                cursor.execute(query, (division,))
            else:
                query = """
                    SELECT 
                        COUNT(*) AS puestos_votacion,
                        SUM(CASE WHEN UPPER(TRIM(rural)) = 'X' THEN 1 ELSE 0 END) AS rural,
                        SUM(CASE WHEN UPPER(TRIM(urbana)) = 'X' THEN 1 ELSE 0 END) AS urbana,
                        SUM(mesas) AS mesas_votacion
                    FROM puestos_votacion;
                """
                cursor.execute(query)

            row = cursor.fetchone()

        puestos_votacion, rural, urbano, mesas_votacion  = map(fmt, row)

        # 🔹 Conexión segura con context manager
        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            if division != "EJC":
                query = """
                    SELECT 
                        porcentaje as porcentaje
                    FROM resumen_divisiones
                    WHERE unidad = %s
                """
                cursor.execute(query, (division,))
            else:
                query = """
                    SELECT 
                        porcentaje as porcentaje
                    FROM resumen_divisiones
                """
                cursor.execute(query)

            row = cursor.fetchone()

        # Si no hay resultados, prevenimos error
        if row is None:
            porcentaje_numerico = 0
        else:
            porcentaje_numerico = row[0] or 0

        # ✅ Formatear correctamente el valor
        porcentaje = fmt(round( porcentaje_numerico))

        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            if division != "EJC":
                query = """
                    SELECT * 
                    FROM diviplo
                    WHERE unidad = %s
                """
                cursor.execute(query, (division,))
            else:
                query = """
                    SELECT * 
                    FROM diviplo
                """
                cursor.execute(query)

            rows = cursor.fetchall()  # ← obtiene TODAS las filas

        urbano_puesto = []
        rural_puesto = []
        datos=[]

        for x in rows:
            # Columna tipo_de_pu está en la posición 15 (según tu CREATE TABLE)
            datos.append(x)
            if x[15] == "URBANO":
                urbano_puesto.append(x)
            else:
                rural_puesto.append(x)

        

        pdf_temp.set_text_color(3, 88, 39)
        pdf_temp.set_font("BebasNeue", "", 22)

        # Diccionario con coordenadas (x,y) para cada dato según la división
        imagen_ruta="C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/reloj/"
        reloj_base="reloj.png"
        velocimetro_dicte = "velocimetro_dicte.png"
        Funciones_eleciones.grafico_reloj(imagen_ruta, round(porcentaje_numerico))
        ruta_f = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/"
        ruta_f_MAPA=[division, ruta_f, ""]
        if actualizarMapas =="true":
            PUESTO_VOTACION(ruta_f_MAPA, urbano_puesto, rural_puesto, datos,  division)
        coords = {
            "DIV01": {
                "puestos": (90, 90),
                "rural": (100, 105),
                "urbano": (100, 120),
                "mesas": (88, 145),
                "coordenadas_reloj_base":(88, 163),
                "coordenadas_mapa":(-16, -13.5),
                "tamanio_mpa":(209, 265),
                "angulo":7.5,
            },
            "DIV02": {
                "puestos": (90, 20),
                "rural": (105, 35),
                "urbano": (105, 50),
                "mesas": (8, 70),
                "coordenadas_reloj_base":(90, 170),
                "coordenadas_mapa":(-28, -13),
                "tamanio_mpa":(208, 257),
                "angulo":8,
            },
            "DIV03": {
                "puestos": (37, 48),
                "rural": (30, 61),
                "urbano": (30, 76),
                "mesas": (22, 103),
                "coordenadas_reloj_base":(88, 170),
                "coordenadas_mapa":(-30, -9),
                "tamanio_mpa":(208, 257),
                "angulo":8,
            },
            "DIV04": {
                "puestos": (95, 70),
                "rural": (26, 94),
                "urbano": (26, 110),
                "mesas": (23, 140),
                "coordenadas_reloj_base":(15, 150),
                "coordenadas_mapa":(-1, 2),
                "tamanio_mpa":(166, 208),
                "angulo":8,
            },
            "DIV05": {
                "puestos": (96, 112),
                "rural": (85, 124),
                "urbano": (85, 140),
                "mesas": (96, 168),
                "coordenadas_reloj_base":(55, 170),
                "coordenadas_mapa":(-15, -9),
                "tamanio_mpa":(197, 245),
                "angulo":8,
            },
            "DIV06": {
                "puestos": (93, 76),
                "rural": (26, 117),
                "urbano": (26, 133),
                "mesas": (38, 162),
                "coordenadas_reloj_base":(75, 165),
                "coordenadas_mapa":(-2.5, 9),
                "tamanio_mpa":(170, 218),
                "angulo":8,
            },
            "DIV07": {
                "puestos": (11, 144),
                "rural": (97, 155),
                "urbano": (97, 170),
                "mesas": (16, 171),
                "coordenadas_reloj_base":(88, 175),
                "coordenadas_mapa":(-15, -2),
                "tamanio_mpa":(196, 247),
                "angulo":8,                        
            },
            "DIV08": {
                "puestos": (74, 56.5),
                "rural": (26, 111),
                "urbano": (26, 127),
                "mesas": (22, 158),
                "coordenadas_reloj_base":(17, 170),
                "coordenadas_mapa":(-21, -7),
                "tamanio_mpa":(170, 212),
                "angulo":0.5,
            },
            "FUTOM": {
                "puestos": (54, 38),
                "rural": (98, 27),
                "urbano": (98, 42),
                "mesas": (100, 69),
                "coordenadas_reloj_base":(5, 170),
                "coordenadas_mapa":(5, 15),
                "tamanio_mpa":(167, 208),
                "angulo":9,
            },
        }
        
        # Dibujar según división
        # Dibujar según división
        if division in coords:
            pdf_temp.set_text_color(3, 88, 39)
            pdf_temp.set_font("BebasNeue", "", 22)
            ruta_relo_fondo = imagen_ruta + reloj_base
            ruta_relo = imagen_ruta + velocimetro_dicte

            imagen = '{}static/img/img_mapas/'.format(ruta_f)
            direccion = str(imagen)+str(division)+str("_puesto_votacion.png")

            # --- Extraer coordenadas ---
            coord = coords[division]
            x_base, y_base = coord["coordenadas_reloj_base"]

            x_base_mpa, y_base_mpa = coord["coordenadas_mapa"]
            w_base_mpa, h_base_mpa = coord["tamanio_mpa"]

            # --- Textos dinámicos ---
            pdf_temp.text(*coord["puestos"], str(puestos_votacion))
            pdf_temp.text(*coord["rural"], str(rural))
            pdf_temp.text(*coord["urbano"], str(urbano))
            pdf_temp.text(*coord["mesas"], str(mesas_votacion))

            #---- mapa ------------
            angulo = coord["angulo"]

            with Funciones_eleciones.rotated(pdf_temp, angulo, x_base_mpa + w_base_mpa/2, y_base_mpa + h_base_mpa/2):
                pdf_temp.image(direccion,
                            x_base_mpa,
                            y_base_mpa,
                            w=w_base_mpa,
                            h=h_base_mpa)


            #pdf_temp.image(direccion, x_base_mpa, y_base_mpa, w=w_base_mpa, h=h_base_mpa)
            # --- Imágenes del velocímetro ---
            pdf_temp.image(ruta_relo_fondo, x_base, y_base, w=30, h=30)
            pdf_temp.image(ruta_relo, x_base + 6, y_base + 6, w=18, h=17)
            pdf_temp.set_fill_color(0, 173, 80)
            pdf_temp.rounded_rect(x_base + 9, y_base + 26, 12, 4.3, 1, 'F', '1234')
            pdf_temp.rounded_rect(x_base + 3, y_base + 31, 23, 4.3, 1, 'F', '1234')
            pdf_temp.set_text_color(255, 255, 255)
            pdf_temp.set_font("BebasNeue", "", 14)
            porcentaje = porcentaje +" %"
            pdf_temp.text(x_base + 12, y_base + 30, str(porcentaje))
            pdf_temp.text(x_base + 6, y_base + 35, str("Cobertura"))
            
            pdf_temp.set_text_color(40, 40, 40)

            pdf_temp.set_fill_color(3, 173, 80)
            pdf_temp.rounded_rect(40, 205, 3, 3, 1, 'FD', '1234')
            pdf_temp.text(45, 208, str("Rural"))

            pdf_temp.set_fill_color(250, 173, 80)
            pdf_temp.rounded_rect(70, 205, 3, 3, 1, 'FD', '1234')
            pdf_temp.text(75, 208, str("Urbano"))


        
    def lamina_6(self, pdf_temp, division):
        
        def fmt(valor):
            """Convierte un número a formato 1.234,56"""
            return f"{valor or 0:,.0f}".replace(",", "X").replace(".", ",").replace("X", ".")

        # --- 1. Consulta totales generales por división ---
        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()
            if division != "EJC":
                cursor.execute("""
                        SELECT 
                            SUM(CASE WHEN UPPER(TRIM(ejercito_nacional)) = 'X' THEN 1 ELSE 0 END) AS ejercito_nacional,
                            SUM(CASE WHEN UPPER(TRIM(policia_nacional)) = 'X' THEN 1 ELSE 0 END) AS policia_nacional,
                            SUM(CASE WHEN UPPER(TRIM(ponal)) = 'X' THEN 1 ELSE 0 END) AS ponal,
                            SUM(CASE WHEN UPPER(TRIM(armada_nacional)) = 'X' THEN 1 ELSE 0 END) AS armada_nacional,
                            SUM(total) AS total
                        FROM puestos_votacion
                    WHERE division = %s
                """, (division,))
            else:
                cursor.execute("""
                    SELECT 
                        SUM(CASE WHEN UPPER(TRIM(ejercito_nacional)) = 'X' THEN 1 ELSE 0 END) AS ejercito_nacional,
                        SUM(CASE WHEN UPPER(TRIM(policia_nacional)) = 'X' THEN 1 ELSE 0 END) AS policia_nacional,
                        SUM(CASE WHEN UPPER(TRIM(ponal)) = 'X' THEN 1 ELSE 0 END) AS ponal,
                        SUM(CASE WHEN UPPER(TRIM(armada_nacional)) = 'X' THEN 1 ELSE 0 END) AS armada_nacional,
                        SUM(total) AS total
                    FROM puestos_votacion;
                """)

            ejercito_1, policia_1, ponal_1, arc_1, total_1 = cursor.fetchone()
            ejercito, policia, ponal, arc, total = map(fmt, (ejercito_1, policia_1, ponal_1, arc_1, total_1))

        # --- 2. Consulta discriminada por actividad ---
        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()
            if division != "EJC":
                cursor.execute("""
                    SELECT 
                        SUM(CASE WHEN actividad = 'RESERVA' THEN total ELSE 0 END) AS total_reserva,
                        SUM(CASE WHEN actividad = 'EJES VIALES' THEN total ELSE 0 END) AS total_ejes_viales,
                        SUM(CASE WHEN actividad = 'ACTIVOS ESTRATÉGICOS' THEN total ELSE 0 END) AS total_activos_estrategicos
                    FROM unidades_reserva
                    WHERE division = %s;
                """, (division,))
            else:
                cursor.execute("""
                    SELECT 
                        SUM(CASE WHEN actividad = 'RESERVA' THEN total ELSE 0 END) AS total_reserva,
                        SUM(CASE WHEN actividad = 'EJES VIALES' THEN total ELSE 0 END) AS total_ejes_viales,
                        SUM(CASE WHEN actividad = 'ACTIVOS ESTRATÉGICOS' THEN total ELSE 0 END) AS total_activos_estrategicos
                    FROM unidades_reserva
                """)

            reserva_1, ejes_viales_1, activos_1 = cursor.fetchone()
            total_dis_1 = (reserva_1 or 0) + (ejes_viales_1 or 0) + (activos_1 or 0) + (total_1 or 0)
            reserva_1 = (reserva_1 or 0) + (ejes_viales_1 or 0) + (activos_1 or 0) 
            reserva, ejes_viales, activos, total_dis = map(fmt, (reserva_1, ejes_viales_1, activos_1, total_dis_1))


            

        # --- 2. Consulta por departamentos ---
        unidades_val = []
        color_toggle = True

        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            # 🔹 Obtener lista de departamentos
            if division != "EJC":
                cursor.execute("SELECT DISTINCT departamento FROM puestos_votacion WHERE division = %s", (division,))
            else:
                cursor.execute("SELECT DISTINCT departamento FROM puestos_votacion")

            departamentos = [row[0] for row in cursor.fetchall()]

            unidades_val = []
            color_toggle = True

            # 🔹 Inicializar acumuladores para el total general
            total_general = [0] * 8  # hay 8 campos numéricos en tu SELECT

            for idx, dep in enumerate(departamentos, start=1):  # 👈 numeración inicia en 1
                cursor.execute("""
                    SELECT 
                        COUNT(*) AS puestos_votacion,
                        SUM(CASE WHEN UPPER(TRIM(ejercito_nacional)) = 'X' THEN 1 ELSE 0 END) AS ejercito_nacional,
                        SUM(CASE WHEN UPPER(TRIM(policia_nacional)) = 'X' THEN 1 ELSE 0 END) AS policia_nacional,
                        SUM(CASE WHEN UPPER(TRIM(ponal)) = 'X' THEN 1 ELSE 0 END) AS ponal,
                        SUM(CASE WHEN UPPER(TRIM(armada_nacional)) = 'X' THEN 1 ELSE 0 END) AS armada_nacional,
                        SUM(CASE WHEN UPPER(TRIM(cobertura)) = 'SI' THEN 1 ELSE 0 END) AS cobertura,
                        SUM(CASE WHEN UPPER(TRIM(comunidad_indigena)) = 'SI' THEN 1 ELSE 0 END) AS comunidad_indigena,
                        SUM(total) AS total
                    FROM puestos_votacion
                    WHERE departamento = %s and division = %s
                """, (dep, division))

                row = cursor.fetchone()
                row = [r or 0 for r in row]  # evitar None
                valores = list(map(fmt, row))

                # 🔹 Acumular al total general
                total_general = [t + v for t, v in zip(total_general, row)]

                # 🔹 Alternar color
                color = (240, 240, 240) if color_toggle else (200, 200, 200)
                color_tex = (0, 0, 0)
                color_toggle = not color_toggle

                unidades_val.append({
                    "valores": [idx, dep] + valores,
                    "color": color,
                    "color_tex": color_tex
                })

            # 🔹 Agregar fila de TOTAL general al final
            valores_total = list(map(fmt, total_general))
            unidades_val.append({
                "valores": ["TOTAL"] + valores_total,
                "color": (160, 160, 160),  # color más oscuro para diferenciar
                "color_tex": (0, 0, 0)
            })


        # --- 3. Render tabla ---
        headers = ["No.", "DEPTO", "PUESTOS DE\nVOTACIÓN", "EJÉRCITO \nNACIONAL", 
                "POLICÍA \nNACIONAL", "EJÉRCITO \nPONAL", "SAE", "COVERT.", "INDIGEN", "DISP. \nTROPAS"]

        col_widths = [7,13.5,13.5,13.5,13.5,13.5,10,10,13.5,13.5] 
        col_widths_2 = [20.5,13.5,13.5,13.5,13.5,10,10,13.5,13.5] 
        row_height = 10

        # Encabezados con colores
        header_colors = {
            "EJÉRCITO \nNACIONAL": (125, 0, 0),
            "POLICÍA \nNACIONAL": (0, 170, 0),
        }

        pdf_temp.set_text_color(255, 255, 255)
        pos_x = 7
        pdf_temp.set_font("Arial", "", 5)
        for i, header in enumerate(headers):
            fill_color = header_colors.get(header, (55, 86, 36))
            pdf_temp.set_fill_color(*fill_color)
            pdf_temp.rect(pos_x, 72, col_widths[i], row_height, "DF")
            pos_x += col_widths[i]



        # 🔹 Ajuste de desplazamiento horizontal (en puntos)
        # Usa un valor positivo para mover hacia la derecha o negativo para mover hacia la izquierda.
        desplazamiento_x = -3  # Mueve todo 10 puntos hacia la izquierda
        offset_x = -3  # 👉 aquí defines cuánto quieres correr la tabla hacia la derecha

        # 🔹 Imprimir encabezados
        pdf_temp.cell(1)  # Espaciado mínimo inicial
        pdf_temp.ln(40)   # Salto de línea inicial

        # Mover el cursor un poco a la izquierda antes de comenzar la tabla
        pdf_temp.set_x(pdf_temp.get_x() + desplazamiento_x)

        for i, header in enumerate(headers):
            # Guardar posición inicial del cursor
            x_before, y_before = pdf_temp.get_x(), pdf_temp.get_y()

            # Dibujar el encabezado
            pdf_temp.multi_cell(col_widths[i], 3, header, border=0, align="C")

            # 🔹 Volver a la misma línea, moviendo a la siguiente columna
            pdf_temp.set_xy(x_before + col_widths[i], y_before)

        pdf_temp.ln(row_height)  # Salto después del encabezado
        pdf_temp.set_x(offset_x)  # 👈 mover cursor antes de escribir encabezados


        # 🔹 Dibujar filas con rectángulos y texto centrado
        row_index = 0
        offset_x = 7      # posición X inicial de la tabla
        max_y = 270        # límite inferior de la página
        row_height = 5     # altura base por línea

        for unidad in unidades_val:
            valores = unidad["valores"]
            color_fondo = unidad["color"]
            color_texto = unidad["color_tex"]

            # 1️⃣ Calcular altura máxima de la fila
            max_height = 0
            cell_texts = []
            pdf_temp.set_x(offset_x)

            for i, cell in enumerate(valores):
                # Formatear texto
                if isinstance(cell, float) and cell.is_integer():
                    text = str(int(cell))
                else:
                    text = str(cell) if cell is not None else ""

                # Calcular altura necesaria (simulación sin imprimir)
                lines = pdf_temp.multi_cell(col_widths[i], row_height, text, split_only=True)
                height = len(lines) * row_height
                max_height = max(max_height, height)
                cell_texts.append(text)

            # 2️⃣ Verificar si cabe en la página
            if pdf_temp.get_y() + max_height > max_y:
                pdf_temp.add_page()
                pdf_temp.set_y(30)  # reanudar después del encabezado

            # 3️⃣ Dibujar fondo y texto de cada celda
            y_before = pdf_temp.get_y()
            x_cursor = offset_x
            valor = 0
            for i, text in enumerate(cell_texts):
                if text != "TOTAL":
                    if valor == 0:
                        ancho = col_widths[i]
                    else:
                        ancho = col_widths_2[i]
                else:
                    ancho = col_widths_2[i]
                    valor = 1

                # Fondo y borde del rectángulo
                pdf_temp.set_fill_color(*color_fondo)
                pdf_temp.rect(x_cursor, y_before, ancho, max_height, style="FD")

                # Texto centrado horizontal y verticalmente
                pdf_temp.set_text_color(*color_texto)
                lines = pdf_temp.multi_cell(ancho, row_height, text, split_only=True)
                alto_texto = len(lines) * row_height
                margen_vertical = (max_height - alto_texto) / 2

                # Posicionar texto dentro del rectángulo
                pdf_temp.set_xy(x_cursor, y_before + margen_vertical)
                pdf_temp.multi_cell(ancho, row_height, text, border=0, align="C")

                # Reposicionar X para siguiente celda
                x_cursor += ancho
                pdf_temp.set_xy(x_cursor, y_before)

            # 4️⃣ Avanzar a la siguiente fila
            pdf_temp.ln(max_height)
            row_index += 1


        # --- 4. Resumen en pdf_temp ---
        pdf_temp.set_text_color(3, 88, 39)
        pdf_temp.set_font("BebasNeue", "", 30)

        pdf_temp.text(50, 45, str(ejercito))
        pdf_temp.text(90, 45, str(policia))
        pdf_temp.text(50, 65, str(ponal))
        pdf_temp.text(90, 65, str(arc))

        pdf_temp.set_font("BebasNeue", "", 18)
        pdf_temp.text(17, 191, str(total_dis))
        pdf_temp.text(59, 191, str(total))
        pdf_temp.text(95, 191, str(reserva))

    def lamina_7(self, divicion):

        with Funciones_eleciones.connect() as conn:
            cursor = conn.cursor()

            query = """
                SELECT 
                    ROW_NUMBER() OVER (ORDER BY departamento, municipio) AS num,
                    departamento, 
                    municipio,
                    nombre_del_puesto,
                    brigada,
                    batallon,
                    CASE 
                        WHEN peloton IS NOT NULL AND peloton <> '' THEN peloton
                        WHEN seccion IS NOT NULL AND seccion <> '' THEN seccion
                        WHEN escuadra IS NOT NULL AND escuadra <> '' THEN escuadra
                        ELSE ''
                    END AS unidad_final,
                    grado_cdte,
                    apellido_y_nombre_cdte_responsable_seguridad,
                    TRIM(TRAILING '.0' FROM CAST(numero_de_telefono_cdte AS TEXT)) AS numero_de_telefono_cdte
                FROM puestos_votacion
                WHERE division = %s AND ejercito_nacional = 'X';
            """

            cursor.execute(query, (divicion,))

            rows = cursor.fetchall()   # Trae todas las filas


        # Definir encabezados y ancho de columnas
        headers = ["No.","DPTO", "MPIO", "NOMBRE DEL \nPUESTO", 
                "BR", "BT", "UNIDAD", "GRD", "APELLIDOS Y NOMBRES", "CELULAR"]

        col_widths = [7,22, 19.7, 28, 10, 19.7, 19.7, 7, 27, 17]
        row_height = 5

        offset_x = 2  # 👉 aquí defines cuánto quieres correr la tabla hacia la derecha

        # --- ENCABEZADOS ---
        def imprimir_encabezados(pdf):
            self.pdf.set_text_color(255, 255, 255)
            position = offset_x  # 👈 arranque desplazado

            for i, x in enumerate(headers):
                if x == 'EJÉRCITO \nNACIONAL':
                    self.pdf.set_fill_color(125, 0, 0) 
                elif x == 'POLICÍA \nNACIONAL':
                    self.pdf.set_fill_color(0, 170, 0) 
                else:
                    self.pdf.set_fill_color(55, 86, 36)

                self.pdf.rect(position, 7, col_widths[i], 10, "DF")
                position += col_widths[i]

            self.pdf.set_font("BebasNeue", "", 10)
            self.pdf.ln(-25)
            self.pdf.set_x(offset_x)  # 👈 mover cursor antes de escribir encabezados

            for i, header in enumerate(headers):
                x_before = self.pdf.get_x()
                y_before = self.pdf.get_y()
                self.pdf.multi_cell(col_widths[i], row_height, header, border=0, align="C")
                self.pdf.set_xy(x_before + col_widths[i], y_before)

            self.pdf.ln(row_height)
            self.pdf.ln()
            self.pdf.set_text_color(0, 0, 0)
            self.pdf.set_font("Arial", "", 7)

        
        # --- ENCABEZADOS AL INICIO ---


        imprimir_encabezados(self.pdf)
        max_y = 125   # límite antes de salto de página
        row_height = 4
        fill_colors = [(200, 200, 200), (230, 230, 230)]  # Blanco / Gris claro
        row_index = 0

        for row in rows:
            # 1️⃣ Calcular altura máxima de la fila
            max_height = 0
            cell_texts = []
            self.pdf.set_x(offset_x)  # 👈 mover cursor antes de escribir fila
            
            for i, cell in enumerate(row):
                # ✅ Convertir valores sin mostrar .0 si son enteros
                if isinstance(cell, float) and cell.is_integer():
                    text = str(int(cell))
                else:
                    text = str(cell) if cell is not None else ""
                
                lines = self.pdf.multi_cell(col_widths[i], row_height, text, split_only=True)
                height = len(lines) * row_height
                max_height = max(max_height, height)
                cell_texts.append(text)

            # 2️⃣ Verificar si cabe en la página
            if self.pdf.get_y() + max_height > max_y:
                self.pdf.add_page()
                imprimir_encabezados(self.pdf)

            # 3️⃣ Dibujar fondo de la fila
            y_before = self.pdf.get_y()
            self.pdf.set_fill_color(*fill_colors[row_index % 2])

            # 4️⃣ Dibujar celdas con texto encima
            x_cursor = offset_x  # 👈 Reinicio en cada fila
            for i, text in enumerate(cell_texts):
                # Fondo y borde de la celda
                self.pdf.rect(x_cursor, y_before, col_widths[i], max_height, style="FD")

                # Guardar coordenadas
                x_before = x_cursor
                y_before_cell = y_before

                # Texto dentro de la celda (sin que mueva el cursor de la fila)
                self.pdf.set_xy(x_before, y_before_cell)
                self.pdf.multi_cell(col_widths[i], row_height, text, border=0, align="C")

                # ⚡ Reubicar cursor al final de la celda horizontalmente, manteniendo Y fija
                self.pdf.set_xy(x_before + col_widths[i], y_before_cell)

                # Avanzar posición X al siguiente cuadro
                x_cursor += col_widths[i]

            # 5️⃣ Avanzar fila y alternar color
            self.pdf.ln(max_height)
            row_index += 1
