
# coding: utf-8
from __init__ import *
from models.conexion_pos import *
from werkzeug.security import generate_password_hash
import psycopg2
from datetime import datetime

from z_z_configuarcion.caligrafia import *
from z_z_configuarcion.fechas import *

from fpdf import FPDF
from math import sqrt, pi, sin, cos
from fpdf.php import sprintf
#Funcion para la creacion del reporte de resultados 
from PyPDF2 import PdfFileMerger, PdfFileReader
import shutil
import PyPDF2
from PyPDF2 import PdfWriter, PdfReader
class PDF(FPDF):
    
    def __init__(self, orientation = 'P', unit = 'mm', format = 'A4'):
        self.ext_gstates = [ ]
        
        super(PDF, self).__init__(orientation, unit, format)

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

def connect():
    conn = psycopg2.connect(" \
        dbname=PLAZOS_SEGUNDO_CDTE \
        user=postgres \
        password=NICval10**")
    return conn

def validar_check(dato):
    if dato=="OK":
        valor =  True
    else:
        valor = False
    return valor
def unidad_texto(pdf,text, numero_x, numero_y, coejc_sejec):
    DIRECION = os.getenv('DIRECION')
    pdf.set_font('BebasNeue', '', 12)
    pdf.rounded_rect(numero_x, numero_y-5, 7, 7, 1,'D', '1234')
    pdf.text(numero_x+8,numero_y,text)
    for x in coejc_sejec:
        if x == text:
            pdf.image(DIRECION+"/static/img/escudos/Imagen1_new.png",numero_x+1,numero_y-5,6,6)
def unidad_texto_text(pdf,text, numero_x, numero_y, tipo_false):
    DIRECION = os.getenv('DIRECION')
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
def guardar_evento(datos, direcion_plazo_fina):
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
    de_respueste =  validar_check(datos["de_respueste"])
    inicie_investigacion =  validar_check(datos["inicie_investigacion"])
    elabore_plan =  validar_check(datos["elabore_plan"])
    traiga_antecedentes =  validar_check(datos["traiga_antecedentes"])
    de_acuerdo_a_sop =  validar_check(datos["de_acuerdo_a_sop"])
    asistir =  validar_check(datos["asistir"])
    reunion_e_m =  validar_check(datos["reunion_e_m"])
    agendar =  validar_check(datos["agendar"])

    coejc_sejec =  datos["coejc_sejec"]

    unidades_que_lideran =  datos["unidades_que_lideran"]
    unidades_que_lapoyan =  datos["unidades_que_lapoyan"]
    unidades_que_coordian =  datos["unidades_que_coordian"]

    id_plazo =  datos["id_plazo"]
    direcion_plazo =  str(datos["direcion_plazo"])
    orfeo =  datos["orfeo"]
    orden_jemop =  datos["orden_jemop"]
    estado_orden = "ORDEN ASIGNADA JURIDICA"
    full_nombre =  datos["full_nombre"]
    unidad_user =  datos["unidad_user"]

    conn = connect()
    cursor = conn.cursor()
    query = """
    SELECT f.name AS folder_name, s.name AS subfolder_name, s.active, s.created_at
    FROM folders f
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS SIN ASIGNAR' and s.active = True
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
    LEFT JOIN subfolders s ON f.id = s.folder_id where f.name = 'PLAZOS ASIGNADOS ASESORA' and s.active = True
    ORDER BY f.id, s.created_at DESC;
    """
    cursor.execute(query_2)
    numero_orden_regitrado_2 = cursor.fetchall()
    carpeta_raiz_2 = numero_orden_regitrado_2[0][0]
    sub_carpeta_2  = numero_orden_regitrado_2[0][1]
    direcion_final = str("/plazos_sejec/{}/{}/").format(carpeta_raiz_2, sub_carpeta_2)
    
    documento_pdf_dir = direcion_plazo.replace(direcion_original, direcion_final)
    

    query = """UPDATE tabla_ordenes SET fecha_cumplimiento = '{}', orden_secej = '{}', estado_orden = '{}', documento_pdf_dir ='{}' WHERE id_tabla_ordenes = '{}' ;""".format(fecha_cumplimiento, orden, estado_orden, documento_pdf_dir, id_plazo)


    cursor.execute(query)
    conn.commit()

    evento_registrar = "Se asigno la orden juridica"

    fecha = datetime.now()

    query = """insert into tabla_log (full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, fecha) values ('{}','{}','{}','{}','{}')""".format(full_nombre, unidad_user, id_plazo, evento_registrar, fecha)

    cursor.execute(query)
    conn.commit()

    query = """insert into tabla_relacion_ordenes (id_tabla_ordenes, ope_imediata, prioritario, de_cumplimiento, trate_conmigo, autorizado, no_autorizado, su_control, res_con_mi_firma, firma_con_coejc, lo_de_su_cargo, resuelva_informa, estudie_recomiende, coordine_con,  de_respueste, inicie_investigacion, elabore_plan, traiga_antecedentes, de_acuerdo_a_sop, asistir, reunion_e_m, agendar ) values ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})""".format(id_plazo, ope_imediata, prioritario, de_cumplimiento, trate_conmigo, autorizado, no_autorizado, su_control, res_con_mi_firma, firma_con_coejc, lo_de_su_cargo, resuelva_informa, estudie_recomiende, coordine_con, de_respueste, inicie_investigacion, elabore_plan, traiga_antecedentes, de_acuerdo_a_sop, asistir, reunion_e_m, agendar)

    cursor.execute(query)
    conn.commit()

    coejc_sejec = coejc_sejec.split(",")
    coejc_sejec = list(coejc_sejec)


    list_of_values = unidades_que_lideran.split(",")
    tuple_of_values = list(list_of_values)
    unidad_lidera  =""

    if tuple_of_values !=['']:
        for x in tuple_of_values:

            unidad="({}, '{}', '{}')".format(id_plazo, x, "LIDERA" )

            unidad_lidera =  unidad_lidera + unidad+","
        unidad_lidera = unidad_lidera.replace("),(", ")*(")
        unidad_lidera = unidad_lidera.replace("),", ")")
        unidad_lidera = unidad_lidera.replace(")*(", "),(")

        query = """insert into tabla_relacion_unidades (id_tabla_ordenes, unidad, relacion_unidad ) values {} """.format(unidad_lidera)

        cursor.execute(query)
        conn.commit()

    unidades_que_lapoyan = unidades_que_lapoyan.split(",")
    unidades_que_lapoyan = list(unidades_que_lapoyan)
    unidad_apoya  =""
    if unidades_que_lapoyan !=['']:
        for x in unidades_que_lapoyan:

            unidad="({}, '{}', '{}')".format(id_plazo, x, "APOYA" )

            unidad_apoya =  unidad_apoya + unidad+","
        unidad_apoya = unidad_apoya.replace("),(", ")*(")
        unidad_apoya = unidad_apoya.replace("),", ")")
        unidad_apoya = unidad_apoya.replace(")*(", "),(")

        
        query = """insert into tabla_relacion_unidades (id_tabla_ordenes, unidad, relacion_unidad ) values {} """.format(unidad_apoya)

        cursor.execute(query)
        conn.commit()

    unidades_que_coordian = unidades_que_coordian.split(",")
    unidades_que_coordian = list(unidades_que_coordian)
    unidad_coordina  =""
    if unidades_que_coordian !=['']:
        for x in unidades_que_coordian:

            unidad="({}, '{}', '{}')".format(id_plazo, x, "COORDINA" )

            unidad_coordina =  unidad_coordina + unidad+","
        unidad_coordina = unidad_coordina.replace("),(", ")*(")
        unidad_coordina = unidad_coordina.replace("),", ")")
        unidad_coordina = unidad_coordina.replace(")*(", "),(")

                

        query = """insert into tabla_relacion_unidades (id_tabla_ordenes, unidad, relacion_unidad ) values {} """.format(unidad_coordina)

        cursor.execute(query)
        conn.commit()
    query_f =  """SELECT DISTINCT 
                                usuarios_sejec.full_nombre,
                                usuarios_sejec.correo, 
                                cargos_plataforma.cargo_sejec,
                                firmas_documentos.firma_numero,   
                                unidades_internas.ABREV_JEFATURA,
                                unidades_internas.DESCRIPCION_JEFATURA
                FROM usuarios_sejec INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = usuarios_sejec.ID_COMAND INNER  JOIN  firmas_documentos on firmas_documentos.di_nombre = usuarios_sejec.id  INNER  JOIN  cargos_plataforma on cargos_plataforma.id_cargos_plataforma = firmas_documentos.id_cargo where estado_firma = 'ACTIVO'; """



    cursor.execute(query_f)
    usuarios = cursor.fetchall()

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
    WHERE tabla_ordenes.estado_orden = 'ORDEN CREADA';
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
    WHERE tabla_ordenes.estado_orden = 'ORDEN CREADA';
    """
    cursor.execute(query_2)
    resultados_2 = cursor.fetchall()

    # Consulta 2: JOIN con directorio_ecp
    query_3 = """
    SELECT *
    FROM tabla_ordenes
    INNER JOIN unidades_externas 
        ON tabla_ordenes.unidad = unidades_externas.ABREV_FUERZA_ENTIDAD
    WHERE tabla_ordenes.estado_orden = 'ORDEN CREADA';
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
    
    # Paso 1: Obtener los IDs de las órdenes creadas
    query_ordenes = """
        SELECT id_tabla_ordenes 
        FROM tabla_ordenes 
        INNER JOIN unidades_internas 
        ON tabla_ordenes.unidad = unidades_internas.ID_COMAND 
        WHERE tabla_ordenes.estado_orden = 'ORDEN CREADA'
    """
    cursor.execute(query_ordenes)
    ordenes_creadas = cursor.fetchall()
    resultados_log = []
    # Extraer solo los IDs como tupla de enteros
    id_ordenes = tuple([fila[0] for fila in ordenes_creadas])

    # Validar que haya resultados para evitar error de SQL vacío
    if not id_ordenes:
        print("No hay órdenes creadas.")
    else:
        # Convertir la lista de IDs a una tupla para usar con placeholders
        id_tuple = tuple(id_ordenes)

        if len(id_tuple) == 1:
            id_tuple += (-1,)  # Evita error de sintaxis en SQL con un solo elemento

        query_log = """
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
            WHERE evento_registrar = %s
            AND tabla_log.id_tabla_ordenes IN %s
        """

        try:
            cursor.execute(query_log, ("Se devolvio a juridica la orden", id_tuple))
            resultados_log = cursor.fetchall()
        except Exception as e:
            print("Error en la consulta de tabla_log:", e)
            resultados_log = []




    conn.close()
    cursor.close



    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [numero_orden_registrado, resultados_log]

