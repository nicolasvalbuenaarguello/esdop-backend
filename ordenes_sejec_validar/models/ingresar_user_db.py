# coding: utf-8
from __init__ import * # type: ignore
#from _init_ import *
from models.conexion_pos import *
from werkzeug.security import generate_password_hash
import psycopg2
from datetime import datetime, date

from z_z_configuarcion.caligrafia import *
from z_z_configuarcion.fechas import *

from fpdf import FPDF
from math import sqrt, pi, sin, cos
from fpdf.php import sprintf
#Funcion para la creacion del reporte de resultados 
from PyPDF2 import PdfMerger
import shutil
import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
class PDF(FPDF):
    
    def __init__(self, orientation = 'P', unit = 'mm', format = 'A4'):
        super(PDF, self).__init__(orientation, unit, format)
        self.ext_gstates = [ ]
        

            


    def rounded_rect(self, x, y, w, h, r, style = '', corners = '1234'):
    
        k = self.k
        hp = self.h
        if(style=='F'):
            op='f'
        elif(style=='FD' or style=='DF'):
            op='B'
        else:
            op='S'
        myArc = 4/3 * (sqrt(2) - 1)
        self._out('%.2F %.2F m' % ((x+r)*k,(hp-y)*k))

        xc = x+w-r
        yc = y+r
        self._out('%.2F %.2F l' % (xc*k,(hp-y)*k))
        if '2' not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k,(hp-y)*k))
        else:
            self._arc(xc + r*myArc, yc - r, xc + r, yc - r*myArc, xc + r, yc)

        xc = x+w-r
        yc = y+h-r
        self._out('%.2F %.2F l' % ((x+w)*k,(hp-yc)*k))
        if '3' not in corners:
            self._out('%.2F %.2F l' % ((x+w)*k,(hp-(y+h))*k))
        else:
            self._arc(xc + r, yc + r*myArc, xc + r*myArc, yc + r, xc, yc + r)

        xc = x+r
        yc = y+h-r
        self._out('%.2F %.2F l' % (xc*k,(hp-(y+h))*k))
        if '4' not in corners:
            self._out('%.2F %.2F l' % (x*k,(hp-(y+h))*k))
        else:
            self._arc(xc - r*myArc, yc + r, xc - r, yc + r*myArc, xc - r, yc)

        xc = x+r 
        yc = y+r
        self._out('%.2F %.2F l' % (x*k,(hp-yc)*k))
        if '1' not in corners:
            self._out('%.2F %.2F l' % (x*k,(hp-y)*k))
            self._out('%.2F %.2F l' % ((x+r)*k,(hp-y)*k))
        else:
            self._arc(xc - r, yc - r*myArc, xc - r*myArc, yc - r, xc, yc - r)
        self._out(op)
    
    def _arc(self, x1, y1, x2, y2, x3, y3):
    
        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c ' % (x1*self.k, (h-y1)*self.k,
            x2*self.k, (h-y2)*self.k, x3*self.k, (h-y3)*self.k))
        
    def sector(self, xc, yc, r, a, b, style='FD', cw=True, o=90):
    
        d0 = a - b
        if cw:
            d = b
            b = o - a
            a = o - d
        else:
            b += o
            a += o
        
        while a<0:
            a += 360
        while a>360:
            a -= 360
        while b<0:
            b += 360
        while b>360:
            b -= 360
        if a > b:
            b += 360
        b = b/360*2*pi
        a = a/360*2*pi
        d = b - a
        if d == 0 and d0 != 0:
            d = 2*pi
        k = self.k
        hp = self.h
        if sin(d/2):
            myArc = 4/3*(1-cos(d/2))/sin(d/2)*r
        else:
            myArc = 0
        #first put the center
        self._out('%.2F %.2F m' % ((xc)*k,(hp-yc)*k))
        #put the first point
        self._out('%.2F %.2F l' % ((xc+r*cos(a))*k,((hp-(yc-r*sin(a)))*k)))
        #draw the arc
        if d < pi/2:
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
        else:
            b = a + d/4
            myArc = 4/3*(1-cos(d/8))/sin(d/8)*r
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
           
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
            a = b
            b = a + d/4
            self.sector_arc(xc+r*cos(a)+myArc*cos(pi/2+a),
                        yc-r*sin(a)-myArc*sin(pi/2+a),
                        xc+r*cos(b)+myArc*cos(b-pi/2),
                        yc-r*sin(b)-myArc*sin(b-pi/2),
                        xc+r*cos(b),
                        yc-r*sin(b)
                        )
        
        #terminate drawing
        if style=='F':
            op='f'
        elif style=='FD' or style=='DF':
            op='b'
        else:
            op='s'
        self._out(op)
    
    def sector_arc(self, x1, y1, x2, y2, x3, y3 ):
    
        h = self.h
        self._out('%.2F %.2F %.2F %.2F %.2F %.2F c' %
            (x1*self.k,
            (h-y1)*self.k,
            x2*self.k,
            (h-y2)*self.k,
            x3*self.k,
            (h-y3)*self.k))
 
    def set_alpha(self, alpha, bm='Normal'):
        state = {
            'ca': alpha,
            'CA': alpha,
            'BM': '/' + bm
        }
        self.ext_gstates.append(state)
        self._set_ext_gstate(len(self.ext_gstates))

    def _set_ext_gstate(self, gstate_index):
        self._out(sprintf('/GS%d gs', gstate_index))

    def _enddoc(self):
        if len(self.ext_gstates) > 0 and self.pdf_version < '1.4':
            self.pdf_version = '1.4'
        super(PDF, self)._enddoc()

    def _putextgstates(self):
        for gstate in self.ext_gstates:
            self._newobj()
            gstate['n'] = self.n
            self._out('<</Type /ExtGState')
            self._out(sprintf('/ca %.3F', gstate['ca']))
            self._out(sprintf('/CA %.3F', gstate['CA']))
            self._out('/BM ' + gstate['BM'])
            self._out('>>')
            self._out('endobj')

    def _putresourcedict(self):
        super(PDF, self)._putresourcedict()
        self._out('/ExtGState <<')
        for index, gstate in enumerate(self.ext_gstates):
            self._out('/GS' + str(index+1) + ' ' + str(gstate['n']) +' 0 R')
        self._out('>>')

    def _putresources(self):
        self._putextgstates()
        super(PDF, self)._putresources()


# Cargar las variables de entorno (usa nombres correctos o los que tengas definidos)
POSTGRES_USER = os.getenv('POSTGRES_USER')
POSTGRES_PASSWORD = os.getenv('POSTGRES_KEY')  # Asumo que 'KEY' es la contraseña
POSTGRES_DB = os.getenv('POSTGRES_BD')

def connect():
    try:
        conn = psycopg2.connect(
            dbname=POSTGRES_DB,
            user=POSTGRES_USER,
            password=POSTGRES_PASSWORD,
            host='localhost',   # Puedes cambiar a la IP o nombre del host si es necesario
            port='5432'         # Cambia si tu base usa otro puerto
        )
        return conn
    except Exception as e:
        print("Error de conexión a la base de datos:", e)
        return None



def validar_check(dato):

    if dato=="true":
        valor =  True
    else:
        valor = False
    return valor
def unidad_texto(pdf,text, numero_x, numero_y, coejc_sejec, tipo_orden, numero):
    DIRECION = os.getenv('DIRECION_BAKENG')
    pdf.set_font('BebasNeue', '', numero)
    pdf.rounded_rect(numero_x, numero_y-5, 7, 7, 1,'D', '1234')
    pdf.text(numero_x+8,numero_y,text)
    for x in coejc_sejec:
        if x == text:
            if tipo_orden == "LIDERA":
                pdf.image(DIRECION+"/static/img/escudos/Imagen1_new.png",numero_x,numero_y-5,6,6)
                pdf.image(DIRECION+"/static/img/escudos/Imagen1_new.png",numero_x+2,numero_y-5,6,6)
            elif  tipo_orden == "APOYA":
                pdf.image(DIRECION+"/static/img/escudos/Imagen1_new.png",numero_x+1,numero_y-5,6,6)

def unidad_texto_text(pdf,text, numero_x, numero_y, tipo_false):
    DIRECION = os.getenv('DIRECION_BAKENG')
    pdf.set_font('BebasNeue', '', 12)
    pdf.rounded_rect(numero_x, numero_y-5, 7, 7, 1,'D', '1234')
    pdf.text(numero_x+8,numero_y,text)

    if tipo_false==True:
            pdf.image(DIRECION+"/static/img/escudos/Imagen1_new.png",numero_x+1,numero_y-5,6,6)

def transformar(dato):
    dato = str(dato)
    # dato = dato.replace("datetime.time(",  " '")
    dato = dato.replace("?",  ' ')
    dato = dato.replace("#",  ' ')
    dato = dato.replace("/",  ' ')
    dato = dato.replace("*",  ' ')
    dato = dato.replace(",",  '-')
    # dato = dato.replace("datetime.datetime(", " '")
    dato = dato.replace("(",  ' ')
    dato = dato.replace("),",  "',")
    dato = dato.replace(")",  ' ')
    dato = dato.replace("$",  ' ')
    dato = dato.replace("%",  ' ')
    dato = dato.replace("{",  ' ')
    dato = dato.replace("}",  ' ')
    dato = dato.replace("[",  ' ')
    dato = dato.replace("]",  ' ')
    dato = dato.replace("<",  ' ')
    dato = dato.replace(">",  ' ')
    dato = dato.replace("¨",  ' ')
    dato = dato.replace("^",  ' ')
    dato = dato.replace("~",  ' ')
    dato = dato.replace("`",  ' ')
    dato = dato.replace("'",  ' ')
    dato = dato.replace('"',  ' ')
    
    
    return dato



import fitz
import os


from PyPDF2 import PdfMerger

def merge_pdfs(pdf_list, directory, output_filename="merged_alt.pdf"):
    merger = PdfMerger()
    for pdf in pdf_list:
        pdf_path = os.path.join(directory, pdf)
        merger.append(pdf_path)
    output_path = os.path.join(directory, output_filename)
    merger.write(output_path)
    merger.close()
    print(f"Merged PDF (PyPDF2) saved to: {output_path}")

# Example usage:
# merge_pdfs(listaPdfs, dirercion_archvios, "x.pdf")

def guardar_evento(datos, direcion_plazo_fina):
    # excel_amenaza
    id_plazo =  datos["id_plazo"]
    direcion_plazo =  str(datos["direcion_plazo"])
    orfeo =  datos["orfeo"]
    orden_jemop =  datos["orden_jemop"]
    full_nombre =  datos["full_nombre"]
    unidad_user =  datos["unidad_user"]
    mensaje =  datos["mensaje"]
    
    
    estado_orden = "ORDEN CREADA"
    
    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS ASESORA' and s.active = True
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query)
    numero_orden_regitrado = cursor.fetchall()
    carpeta_raiz = numero_orden_regitrado[0][0]
    sub_carpeta  = numero_orden_regitrado[0][1]
    direcion_original = str("/plazos_sejec/{}/{}/").format(carpeta_raiz, sub_carpeta)
    
    query_2 = """
    SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS SIN ASIGNAR' and s.active = True
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query_2)
    numero_orden_regitrado_2 = cursor.fetchall()
    carpeta_raiz_2 = numero_orden_regitrado_2[0][0]
    sub_carpeta_2  = numero_orden_regitrado_2[0][1]
    direcion_final = str("/plazos_sejec/{}/{}/").format(carpeta_raiz_2, sub_carpeta_2)

    documento_pdf_dir = direcion_plazo.replace(direcion_original, direcion_final)

    query = """UPDATE tabla_ordenes SET  estado_orden = '{}', documento_pdf_dir ='{}' WHERE id_tabla_ordenes = '{}' ;""".format( estado_orden, documento_pdf_dir, id_plazo)


    cursor.execute(query)
    conn.commit()

    evento_registrar = "Se devolvio a juridica la orden"
    
    fecha = datetime.now()

    query = """insert into tabla_log (full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, mensaje, fecha) values ('{}','{}','{}','{}','{}','{}')""".format(full_nombre, unidad_user, id_plazo, evento_registrar, mensaje, fecha)

    cursor.execute(query)
    conn.commit()


    conn.close()
    cursor.close

    return [documento_pdf_dir, direcion_original]
   
def numero_orden_select():

        
    conn = connect()
    cursor = conn.cursor()
    # Consulta 1: JOIN con unidades_internas
    query_1 = """
    SELECT *
    FROM tabla_ordenes
    INNER JOIN unidades_internas 
        ON tabla_ordenes.unidad = unidades_internas.ID_COMAND
    WHERE tabla_ordenes.estado_orden = 'ORDEN ASIGNADA JURIDICA';
    """
    cursor.execute(query_1)
    resultados_1 = cursor.fetchall()
    columnas_1 = [desc[0] for desc in cursor.description]  # Guardar columnas por si las necesitas

    # Consulta 2: JOIN con directorio_ecp
    query_2 = """
    SELECT *
    FROM tabla_ordenes
    INNER JOIN directorio_ecp 
        ON tabla_ordenes.unidad = directorio_ecp.razon_social
    WHERE tabla_ordenes.estado_orden = 'ORDEN ASIGNADA JURIDICA';
    """
    cursor.execute(query_2)
    resultados_2 = cursor.fetchall()

    # Consulta 2: JOIN con directorio_ecp
    query_3 = """
    SELECT *
    FROM tabla_ordenes
    INNER JOIN unidades_externas 
        ON tabla_ordenes.unidad = unidades_externas.ABREV_FUERZA_ENTIDAD
    WHERE tabla_ordenes.estado_orden = 'ORDEN ASIGNADA JURIDICA';
    """
    cursor.execute(query_3)
    resultados_3 = cursor.fetchall()

    # Combinar y eliminar duplicados por id_tabla_ordenes
    ordenes_unicas = {}
    id_index = columnas_1.index('id_tabla_ordenes')  # Obtener el índice de id_tabla_ordenes

    for fila in resultados_1 + resultados_2 + resultados_3:
        orden_id = fila[id_index]
        ordenes_unicas[orden_id] = fila  # Sobrescribe duplicados

    # Convertir a lista ordenada por id_tabla_ordenes
    numero_orden_registrado = sorted(ordenes_unicas.values(), key=lambda x: x[id_index])

   
    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [numero_orden_registrado]

def numero_orden_select_ver(contents):

       
    conn = connect()
    cursor = conn.cursor()

    id_orden = contents["id_orden"]

    # Validar que haya resultados para evitar error de SQL vacío
    if not id_orden:
        print("No hay órdenes creadas.")
    else:
        # Paso 2: Consultar la tabla_log usando los IDs filtrados
        query_log = f"""
            SELECT 
                tabla_log.full_nombre, 
                tabla_log.evento_registrar, 
                tabla_log.mensaje, 
                tabla_log.fecha,                                
                unidades_internas.ABREV_JEFATURA,
                unidades_internas.DESCRIPCION_JEFATURA,
                tabla_log.id_tabla_ordenes,
                tabla_ordenes.orfeo,
                tabla_ordenes.numero_orden    
            FROM tabla_log 
            INNER JOIN unidades_internas 
            ON unidades_internas.ID_COMAND = tabla_log.unidad_user
            INNER JOIN tabla_ordenes 
            ON tabla_ordenes.id_tabla_ordenes = tabla_log.id_tabla_ordenes
            WHERE evento_registrar = 'Se devolvio a juridica la orden'
            AND tabla_log.id_tabla_ordenes = {id_orden}
        """
        cursor.execute(query_log)
        resultados_log = cursor.fetchall()

    query_tabla_unidades= """SELECT 
                tabla_relacion_unidades.unidad, 
                tabla_relacion_unidades.relacion_unidad,                                
                unidades_internas.DESCRIPCION_JEFATURA  
                FROM tabla_relacion_unidades 
                INNER  JOIN unidades_internas ON unidades_internas.ABREV_JEFATURA = tabla_relacion_unidades.unidad
                where id_tabla_ordenes = {} 
                  """.format(id_orden)
    cursor.execute(query_tabla_unidades)
    tabla_unidades = cursor.fetchall()
    unidad_que_lidera = []
    unidad_que_apoya=[]
    unidad_que_cordina=[]
    for x in tabla_unidades:
        if x[1] == "LIDERA":
            unidad_que_lidera.append(x[0])
    for x in tabla_unidades:
        if x[1] == "APOYA":
            unidad_que_apoya.append(x[0])
    for x in tabla_unidades:
        if x[1] == "COORDINA":
            unidad_que_cordina.append(x[0])
            

    query_tabla_relacion_ordeness= """SELECT 
                ope_imediata, prioritario, de_cumplimiento, trate_conmigo, autorizado, no_autorizado, su_control, res_con_mi_firma, firma_con_coejc, lo_de_su_cargo, resuelva_informa, estudie_recomiende, coordine_con,  de_respueste, inicie_investigacion, elabore_plan, traiga_antecedentes, de_acuerdo_a_sop, asistir, reunion_e_m, agendar 
                FROM tabla_relacion_ordenes 
                where id_tabla_ordenes = {} 
                  """.format(id_orden)
    cursor.execute(query_tabla_relacion_ordeness)
    tabla_relacion_ordenes = cursor.fetchall()
 
    nivel_prioridad = [
        ["Operación Inmediata", "ope_imediata"],
        ["Prioritario", "prioritario"],
        ["De Cumplimiento", "de_cumplimiento"],
        ["Trate Conmigo", "trate_conmigo"],
        ["Autorizado", "autorizado"],
        ["No Autorizado", "no_autorizado"],
        ["Su Control y Seguimiento", "su_control"]
    ]

    nivel_autoridad = [
        ["Respuesta con mi Firma", "res_con_mi_firma"],
        ["Respuesta con Firma COEJC", "firma_con_coejc"],
        ["Lo de Su Cargo", "lo_de_su_cargo"],
        ["Resuelva e Informa", "resuelva_informa"],
        ["Estudie y Recomiende", "estudie_recomiende"],
        ["Coordine con", "coordine_con"],
        ["De Respuesta", "de_respueste"]
    ]

    sop_estado_mayor = [
        ["Inicie Investigación", "inicie_investigacion"],
        ["Elabore Plan", "elabore_plan"],
        ["Traiga Antecedentes", "traiga_antecedentes"],
        ["De Acuerdo a SOP", "de_acuerdo_a_sop"],
        ["Favor Asistir", "asistir"],
        ["Tratar Reunión E.M", "reunion_e_m"],
        ["Agendar", "agendar"]
    ]

    # Suponiendo que tabla_relacion_ordenes es una lista de listas, cada sublista con al menos 22 elementos
    for fila in tabla_relacion_ordenes:
        # Columna 2 a 8 (inclusive) → nivel_prioridad
        for i in range(7):
            if len(fila) > 0 + i:
                nivel_prioridad[i].append(fila[0 + i])

        # Columna 9 a 15 (inclusive) → nivel_autoridad
        for i in range(7):
            if len(fila) > 7 + i:
                nivel_autoridad[i].append(fila[7 + i])

        # Columna 16 a 22 (inclusive) → sop_estado_mayor
        for i in range(7):
            if len(fila) > 14 + i:
                sop_estado_mayor[i].append(fila[14 + i])


    conn.close()
    cursor.close

    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [resultados_log, unidad_que_lidera, unidad_que_apoya, unidad_que_cordina, nivel_prioridad, nivel_autoridad, sop_estado_mayor]

def guardar_evento_asignar(datos, direcion_plazo_fina):
    # excel_amenaza

    fecha_cumplimiento =  datos["fecha_cumplimiento"]
    
    orden =  transformar(datos["orden"])
    orden =orden.upper()

    ope_imediata =  validar_check(datos["ope_imediata"])
    prioritario =  validar_check(datos["prioritario"])
    de_cumplimiento =  validar_check(datos["de_cumplimiento"])
    trate_conmigo =  validar_check(datos["trate_conmigo"])
    autorizado =  validar_check(datos["autorizado"])
    no_autorizado =  validar_check(datos["no_autorizado"])
    su_control =  validar_check(datos["su_control"])
    res_con_mi_firma =  validar_check(datos["res_con_mi_firma"])
    firma_con_coejc =  validar_check(datos["firma_con_coejc"])
    lo_de_su_cargo =  validar_check(datos["lo_de_su_cargo"])
    resuelva_informa =  validar_check(datos["resuelva_informa"])
    estudie_recomiende =  validar_check(datos["estudie_recomiende"])
    coordine_con =  validar_check(datos["coordine_con"])
    de_respueste  =  validar_check(datos["de_respueste"])
    inicie_investigacion =  validar_check(datos["inicie_investigacion"])
    elabore_plan =  validar_check(datos["elabore_plan"])
    traiga_antecedentes =  validar_check(datos["traiga_antecedentes"])
    de_acuerdo_a_sop =  validar_check(datos["de_acuerdo_a_sop"])
    asistir =  validar_check(datos["asistir"])
    reunion_e_m =  validar_check(datos["reunion_e_m"])
    agendar =  validar_check(datos["agendar"])



    unidades_que_lideran =  datos["unidades_que_lideran"]
    unidades_que_lapoyan =  datos["unidades_que_lapoyan"]
    unidades_que_coordian =  datos["unidades_que_coordian"]

    id_plazo =  datos["id_plazo"]
    direcion_plazo =  str(datos["direcion_plazo"])
    orfeo =  datos["orfeo"]
    orden_jemop =  datos["orden_jemop"]
    estado_orden = "ORDEN ASIGNADA AYUDANTE"
    full_nombre =  datos["full_nombre"]
    unidad_user =  datos["unidad_user"]

    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS ASESORA' and s.active = True
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query)
    numero_orden_regitrado = cursor.fetchall()
    carpeta_raiz = numero_orden_regitrado[0][0]
    sub_carpeta  = numero_orden_regitrado[0][1]
    direcion_original = str("/plazos_sejec/{}/{}/").format(carpeta_raiz, sub_carpeta)
    
    query_2 = """
    SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS AYUDANTE' and s.active = True
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query_2)
    numero_orden_regitrado_2 = cursor.fetchall()
    carpeta_raiz_2 = numero_orden_regitrado_2[0][0]
    sub_carpeta_2  = numero_orden_regitrado_2[0][1]
    direcion_final = str("/plazos_sejec/{}/{}/").format(carpeta_raiz_2, sub_carpeta_2)
    
    documento_pdf_dir = direcion_plazo.replace(direcion_original, direcion_final)
    

    query = """UPDATE tabla_ordenes SET  estado_orden = '{}', documento_pdf_dir ='{}' WHERE id_tabla_ordenes = '{}' ;""".format(estado_orden, documento_pdf_dir, id_plazo)


    cursor.execute(query)
    conn.commit()

    evento_registrar = "Se asigno por parte del ayudante"

    fecha = datetime.now()
    
    
    query = """insert into tabla_log (full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, fecha) values ('{}','{}','{}','{}','{}')""".format(full_nombre, unidad_user, id_plazo, evento_registrar, fecha)

    cursor.execute(query)
    conn.commit()

    list_of_values = unidades_que_lideran.split(",")
    tuple_of_values = list(list_of_values)
    unidad_lidera  =""


    unidades_que_lapoyan = unidades_que_lapoyan.split(",")
    unidades_que_lapoyan = list(unidades_que_lapoyan)
    unidad_apoya  =""

    unidades_que_coordian = unidades_que_coordian.split(",")
    unidades_que_coordian = list(unidades_que_coordian)
    unidad_coordina  =""

    query_f =  """SELECT DISTINCT 
                                usuarios_sejec.full_nombre,
                                usuarios_sejec.correo, 
                                cargos_plataforma.cargo_sejec,
                                firmas_documentos.firma_numero,   
                                unidades_internas.ABREV_JEFATURA,
                                unidades_internas.DESCRIPCION_JEFATURA,
                                firmas_documentos.firma 
                FROM usuarios_sejec INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = usuarios_sejec.ID_COMAND INNER  JOIN  firmas_documentos on firmas_documentos.di_nombre = usuarios_sejec.id  INNER  JOIN  cargos_plataforma on cargos_plataforma.id_cargos_plataforma = firmas_documentos.id_cargo where estado_firma = 'ACTIVO'; """

    cursor.execute(query_f)
    usuarios = cursor.fetchall()
 

    conn.close()
    cursor.close

    #creacion de la tirilla

    
    #creacion del pdf de la orden emitida 
    pdf = PDF(orientation = 'P', unit = 'mm', format='letter')

    DIRECION_BAKENG = os.getenv('DIRECION_BAKENG')
    RUTA_SERVER_DOCUMENTOS= os.getenv('RUTA_SERVER_DOCUMENTOS')
    DIRECION_BAKENG

    caligrafia_ingreso( pdf, DIRECION_BAKENG)
    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.set_fill_color(210, 214, 209)
    pdf.rounded_rect(5, 5, 206, 270, 1,'D', '1234')
    
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)

    pdf.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
    pdf.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
    pdf.text(35,25,str("DESPACHO SEGUNDO COMANDANTE DEL EJÉRCITO"))
    DIRECION_BAKENG = os.getenv('DIRECION_BAKENG')
    ruta_img=DIRECION_BAKENG+"static/img/ejc.png"
    pdf.image(ruta_img,10,9,16,19)

    pdf.set_line_width(0.1)
    pdf.line(5, 30, 211, 30)
    pdf.set_font('BebasNeue', '', 12)
    pdf.text(7,35,str("LUGAR Y FECHA:"))
    pdf.set_font('BebasNeue', '', 10)
    dia = datetime.now().day
    mes = datetime.now().month
    anio = datetime.now().year
    hour = datetime.now().hour
    minute = datetime.now().minute
    segun = datetime.now().second
    lugar_fecha  = str("Bogotá - ")+str(dia)+" - " +str(mes)+" - " +str(anio) 
    hora = str(hour)+":" +str(minute)+":" +str(segun) 

    lugar_fecha= lugar_fecha +" - "+hora
    pdf.text(30,35,lugar_fecha)
    pdf.set_font('BebasNeue', '', 12)

    radicado = "ORFEO: "+orfeo
    pdf.text(90,35,radicado)

    
    radicado = "No. ORDEN: "+orden_jemop
    pdf.text(170,35,radicado)

    pdf.set_font('BebasNeue', '', 14)
    pdf.line(5, 37, 211, 37)
    pdf.set_text_color(128,0,0)
    pdf.text(100,43,"")
    pdf.set_text_color(70,70,70)
    responsable = "COEJC"
    pdf.set_font('BebasNeue', '', 16)
    numero = 43
    pdf.text(10,numero,responsable)
    pdf.set_font('BebasNeue', '', 14)
    numero= numero+7
    unidad_texto(pdf,"CEIGE", 10, numero, tuple_of_values, "LIDERA", 12)
    unidad_texto(pdf,"OSMEJ", 30, numero, tuple_of_values, "LIDERA", 12)
    unidad_texto(pdf,"DADAE", 50, numero, tuple_of_values, "LIDERA", 12)
    unidad_texto(pdf,"COTEF", 70, numero, tuple_of_values, "LIDERA", 12)
    #unidades que apoya
    unidad_texto(pdf,"CEIGE", 10, numero, unidades_que_lapoyan, "APOYA", 12)
    unidad_texto(pdf,"OSMEJ", 30, numero, unidades_que_lapoyan, "APOYA", 12)
    unidad_texto(pdf,"DADAE", 50, numero, unidades_que_lapoyan, "APOYA", 12)
    unidad_texto(pdf,"COTEF", 70, numero, unidades_que_lapoyan, "APOYA", 12)

    pdf.set_font('BebasNeue', '', 16)
    numero = numero+9
    responsable = "SEJEC"
    
    pdf.text(10,numero,responsable)
    pdf.set_font('BebasNeue', '', 14)
    numero= numero+7
    unidad_texto(pdf,"CEAYG", 10, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"COATE", 30, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"DIRIE", 50, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"DANTE", 70, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"OADAS", 90, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"COFIP", 110, numero, tuple_of_values, "LIDERA",12)
    unidad_texto(pdf,"OGENE", 130, numero, tuple_of_values, "LIDERA",12)

    unidad_texto(pdf,"CEAYG", 10, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"COATE", 30, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"DIRIE", 50, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"DANTE", 70, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"OADAS", 90, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"COFIP", 110, numero, unidades_que_lapoyan, "APOYA",12)
    unidad_texto(pdf,"OGENE", 130, numero, unidades_que_lapoyan, "APOYA",12)

    numero= 43
    unidad_texto(pdf,"JEMOP", 180, numero, tuple_of_values, "LIDERA",14)
    unidad_texto(pdf,"JEMOP", 180, numero, unidades_que_lapoyan, "APOYA",14)
    numero= numero +8
    unidad_texto(pdf,"JEMPP", 180, numero, tuple_of_values, "LIDERA",14)
    unidad_texto(pdf,"JEMPP", 180, numero, unidades_que_lapoyan, "APOYA",14)
    numero= numero +8
    unidad_texto(pdf,"JEMGF", 180, numero, tuple_of_values, "LIDERA",14)
    unidad_texto(pdf,"JEMGF", 180, numero, unidades_que_lapoyan, "APOYA",14)
    numero= numero +8
    unidad_texto(pdf,"JEMIC", 180, numero, tuple_of_values, "LIDERA",14)
    unidad_texto(pdf,"JEMIC", 180, numero, unidades_que_lapoyan, "APOYA",14)


    #pdf.set_font('BebasNeue', '', 16)
    #res_ponsable = "RESPONSABLE: "
    #pdf.text(7,55, res_ponsable)
    #res_cargo = "CARGO: "
    #pdf.text(7,61, res_cargo)
    #fecha_plazo_cumplimiento = dato = fecha_cumplimiento.replace("T",  ' HORA ')
    #res_fecha = "FECHA DE CUMPLIMIENTO: "
    #pdf.text(7,67, res_fecha)

    #pdf.set_text_color(125,0,0)
    #pdf.text(55,55, str(unidades_que_lideran))
    #pdf.text(55,61, "cargo")
    #pdf.text(55,67, fecha_plazo_cumplimiento)

    pdf.line(5, 70, 211, 70)

    
    pdf.set_font('BebasNeue', '', 14)
    numero= 75
    position = 10
    pdf.set_text_color(128,0,0)

    pdf.rounded_rect(7, 70, 60, 6, 1,'DF', '1234')
    pdf.rounded_rect(77, 70, 60, 6, 1,'DF', '1234')
    pdf.rounded_rect(155, 70, 53, 6, 1,'DF', '1234')
    pdf.text(position,numero,"Nivel de Prioridad")
    
    pdf.set_text_color(70,70,70)

    numero = numero +7
    unidad_texto_text(pdf,"Operación Inmediata", position, numero, ope_imediata)
    numero = numero +7
    unidad_texto_text(pdf,"Prioritario", position, numero, prioritario)
    numero = numero +7
    unidad_texto_text(pdf,"De Cumplimiento", position, numero, de_cumplimiento)
    numero = numero +7
    unidad_texto_text(pdf,"Trate Conmigo", position, numero, trate_conmigo)
    numero = numero +7
    unidad_texto_text(pdf,"Autorizado", position, numero, autorizado)
    numero = numero +7
    unidad_texto_text(pdf,"No Autorizado", position, numero, no_autorizado)
    numero = numero +7
    unidad_texto_text(pdf,"Su Control y Seguimiento", position, numero, su_control)

    numero= 75
    position = 80
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(128,0,0)
    pdf.text(position,numero,"Nivel de Autoridad")
    
    pdf.set_text_color(70,70,70)

    numero = numero +7
    unidad_texto_text(pdf,"Respuesta con mi Firma", position, numero, res_con_mi_firma)
    numero = numero +7
    unidad_texto_text(pdf,"Respuesta con Firma COEJC", position, numero, firma_con_coejc)
    numero = numero +7
    unidad_texto_text(pdf,"Lo de Su Cargo", position, numero, lo_de_su_cargo)
    numero = numero +7
    unidad_texto_text(pdf,"Resuelva e Informa", position, numero, resuelva_informa)
    numero = numero +7
    unidad_texto_text(pdf,"Estudie y Recomiende", position, numero, estudie_recomiende)
    numero = numero +7
    unidad_texto_text(pdf,"Coordine con", position, numero, coordine_con)
    numero = numero +7
    unidad_texto_text(pdf,"De Respuesta", position, numero, de_respueste)


    numero= 75
    position = 160
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(128,0,0)
    pdf.text(position,numero,"SOP Estado Mayor")
    
    pdf.set_text_color(70,70,70)

    numero = numero +7
    unidad_texto_text(pdf,"Inicie Investigación", position, numero, inicie_investigacion)
    numero = numero +7
    unidad_texto_text(pdf,"Elabore Plan", position, numero, elabore_plan)
    numero = numero +7
    unidad_texto_text(pdf,"Traiga Antecedentes", position, numero, traiga_antecedentes)
    numero = numero +7
    unidad_texto_text(pdf,"De Acuerdo a SOP", position, numero, de_acuerdo_a_sop)
    numero = numero +7
    unidad_texto_text(pdf,"Favor Asistir", position, numero, asistir)
    numero = numero +7
    unidad_texto_text(pdf,"Tratar Reunión E.M", position, numero, reunion_e_m)
    numero = numero +7
    unidad_texto_text(pdf,"Agendar", position, numero, agendar)


    pdf.line(5, 128, 211, 128)
    numero= 135
    position = 10
    if unidades_que_coordian !=[""]:
        pdf.set_font('BebasNeue', '', 14)
        pdf.set_text_color(128,0,0)
        pdf.text(position,numero,"Coordinadar con")
        pdf.set_font('BebasNeue', '', 12)
        
        pdf.set_text_color(70,70,70)
        pdf.ln(127)
        y = pdf.get_y()
        pdf.multi_cell(195, 5, str(unidades_que_coordian), 0, "J", False)

        x = pdf.get_y()
        z = (x-y)+5
        pdf.rounded_rect(7, 135, 202, z, 1,'D', '1234')

        numero= numero +z+7
    else:
        z = pdf.get_y()
        pdf.ln(112)
    position = 150
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(128,0,0)
    pdf.text(position,numero,"Fecha de cumplimiento")
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(70,70,70)
    position = 190
    pdf.text(position,numero,str(fecha_cumplimiento))

    fecha_a_validar = date.fromisoformat(fecha_cumplimiento)
    # Obtener la fecha actual del sistema
    fecha_actual = date.today()
    
    # Comparar fechas
    if fecha_a_validar == fecha_actual:
        position = 80
        pdf.set_text_color(125,0,0)
        pdf.set_font('BebasNeue', '', 20)
        pdf.text(position,numero,str("DE CUMPLIMIENTO INMEDIATO"))
        pdf.set_text_color(70,70,70)
        pdf.set_font('BebasNeue', '', 14)
    numero=numero+7


    pdf.ln(z+10)
    position = 10
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(128,0,0)
    y = pdf.get_y()
    pdf.text(position,numero,"OBSERVACIONES")
    pdf.set_font('BebasNeue', '', 12)
    pdf.set_text_color(70,70,70)

    pdf.multi_cell(195, 5, str(orden), 0, "J", False)
    x = pdf.get_y()
    z = (x-y)+5
    pdf.rounded_rect(7, numero, 202, 90, 1,'D', '1234')
    
    #pdf.line(5, 255, 211, 255)

    pdf.set_font('BebasNeue', '', 12)
    #pdf.text(10,265,"TC. JULIAN PRIETO")
    dato=""
    dato_1=""
    dato_2=""

    dirercion_archvios= "{}ordenes_sejec_validar/firmas/".format(DIRECION_BAKENG)
    for x in usuarios:

        directorio_doc = RUTA_SERVER_DOCUMENTOS + x[6]
        
        if x[3]=='Firma SEJEC':
            dato = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(75,237,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(75,241,x[2])
            if x[6] and isinstance(x[6], str) and os.path.exists(directorio_doc):
                pdf.image(directorio_doc,80,220,60,50)
        if x[3]=='Firma Ayudante Personal':
            dato_1 = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(10,237,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(10,241,x[2])
            if x[6] and isinstance(x[6], str) and os.path.exists(directorio_doc):
                pdf.image(directorio_doc,10,220,60,50)
        if x[3]=='Firma Juridica':
            dato_2 = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(155,237,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(155,241,x[2])
            if x[6] and isinstance(x[6], str) and os.path.exists(directorio_doc):
                pdf.image(directorio_doc,150,220,60,50)
    
    # Altura de la página (incluyendo márgenes)
    alto_pagina = pdf.h
    margen_inferior = pdf.b_margin

    # Texto de compromiso
    compromiso_reserva = """COMPROMISO DE RESERVA: La información contenida en el presente documento goza de reserva legal, razón por la cual todo servidor público que tenga acceso a su contenido, deberá cumplir con las obligaciones de reserva impuestas en la Ley Estatutaria 1621 de 2013, Capítulo VI, al igual que las normas que lo modifiquen o deroguen, así como, las normas concordantes en la materia; su divulgación o uso no autorizado, conllevará las sanciones disciplinarias y/o penales preestablecidas en los códigos vigentes por revelación ilícita de la información."""

    titulo = "COMPROMISO DE RESERVA: "
    cuerpo = compromiso_reserva.replace(titulo, "")

    # Definir ancho del cuadro (ajustado a la página con márgenes)
    x_inicio = 10
    ancho_cuadro = pdf.w - 2 * x_inicio
    alto_linea = 5

    # Primero medimos altura del texto
    pdf.set_font('BebasNeue', '', 12)
    pdf.set_text_color(255, 0, 0)
    h_titulo = pdf.get_string_width(titulo) / (ancho_cuadro/alto_linea) * alto_linea

    pdf.set_font('BebasNeue', '', 10)
    pdf.set_text_color(70, 70, 70)
    n_lineas = len(pdf.multi_cell(ancho_cuadro, alto_linea, cuerpo, 0, "J", split_only=True))
    h_cuerpo = n_lineas * alto_linea

    # Altura total del cuadro
    h_total = h_titulo + h_cuerpo + 8  # +8 para espacio extra

    # Coordenada Y para que quede al final (antes del margen inferior)
    y_inicio = alto_pagina - margen_inferior - h_total

    # Dibujar borde
    pdf.rounded_rect(x_inicio-3, y_inicio, ancho_cuadro+6, h_total-3, 1, 'D', '1234')

    # Escribir título
    pdf.set_xy(x_inicio, y_inicio)
    pdf.set_font('BebasNeue', '', 12)
    pdf.set_text_color(255, 0, 0)
    pdf.multi_cell(ancho_cuadro, alto_linea, titulo, 0, "J")

    # Escribir cuerpo
    pdf.set_xy(x_inicio, y_inicio+5)
    pdf.set_font('BebasNeue', '', 10)
    pdf.set_text_color(70, 70, 70)
    pdf.multi_cell(ancho_cuadro, alto_linea, cuerpo, 0, "J")

    #pip install qrcode
    #pip install pillow
    DIRECION = os.getenv('DIRECION_BAKENG')
    dirercion_archvios = "{}ordenes_sejec_leer_asignar/qr/".format(DIRECION)
    import qrcode
    orfeo_qr = orfeo


    inf_qur = orfeo_qr+" \n"+unidades_que_lideran + "\nFecha de Cumplimento "+fecha_cumplimiento +"\n------------------------------------------------------ \nplazos asignado por:\n"+dato+dato_1+dato_2

    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    DIRECION = os.getenv('DIRECION_BAKENG')
    dirercion_archvios = "{}ordenes_sejec_validar/documentos/".format(DIRECION)
    direcion = dirercion_archvios+str("z_1")+'.pdf'
    pdf.output(direcion, 'F')
    
    #import os
    listaPdfs = os.listdir(dirercion_archvios)

    merger = PdfMerger()
    

    #documento_pdf_dir

    

    #for file in listaPdfs:
        #print(file)
        #pdf_doc = PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file, strict=False)
        #merger.append(pdf_doc)
    #merger.write(documento_guardado)


    merge_pdfs(listaPdfs, dirercion_archvios, output_filename="x.pdf")
    print("direcion_original-1")

    direcion_plazo_fina = direcion_plazo_fina.replace("/", "")
    documento_eliminar = ["z_1.pdf", direcion_plazo_fina]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)
    print(direcion_original)
    return [documento_pdf_dir, direcion_original]