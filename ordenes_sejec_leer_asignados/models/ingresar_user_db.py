
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
    estado_orden = "ORDEN ASIGNADA"
    full_nombre =  datos["full_nombre"]
    unidad_user =  datos["unidad_user"]
    
    documento_pdf_dir = direcion_plazo.replace("/plazos_sejec/creados/", "/plazos_sejec/asignados/")

    query = """UPDATE tabla_ordenes SET fecha_cumplimiento = '{}', orden_secej = '{}', estado_orden = '{}', documento_pdf_dir ='{}' WHERE id_tabla_ordenes = '{}' ;""".format(fecha_cumplimiento, orden, estado_orden, documento_pdf_dir, id_plazo)

    conn = connect()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()

    evento_registrar = "Se asigno la orden"

    fecha = datetime.now()

    query = """insert into tabla_log (full_nombre, unidad_user, id_tabla_ordenes, evento_registrar, fecha) values ('{}','{}','{}','{}','{}')""".format(full_nombre, unidad_user, id_plazo, evento_registrar, fecha)

    cursor.execute(query)
    conn.commit()

    query = """insert into tabla_relacion_ordenes (id_tabla_ordenes, ope_imediata, prioritario, de_cumplimiento, trate_conmigo, autorizado, no_autorizado, su_control, res_con_mi_firma, firma_con_coejc, lo_de_su_cargo, resuelva_informa, estudie_recomiende, coordine_con, inicie_investigacion, elabore_plan, traiga_antecedentes, de_acuerdo_a_sop, asistir, reunion_e_m, agendar, de_respueste ) values ({},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{})""".format(id_plazo, ope_imediata, prioritario, de_cumplimiento, trate_conmigo, autorizado, no_autorizado, su_control, res_con_mi_firma, firma_con_coejc, lo_de_su_cargo, resuelva_informa, estudie_recomiende, coordine_con, inicie_investigacion, elabore_plan, traiga_antecedentes, de_acuerdo_a_sop, asistir, reunion_e_m, agendar, de_respueste)

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

        #cursor.execute(query)
        #conn.commit()

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

    #creacion del pdf de la orden emitida 
    pdf = PDF(orientation = 'P', unit = 'mm', format='letter')


    LINK = os.getenv('DIRECION_3_B')
    DIRECION = os.getenv('DIRECION')

    caligrafia_ingreso( pdf, DIRECION)
    pdf.set_auto_page_break(True, 4)
    pdf.add_page()

    pdf.set_fill_color(210, 214, 209)
    pdf.rounded_rect(5, 5, 206, 270, 1,'D', '1234')
    
    pdf.set_text_color(70,70,70)
    pdf.set_font('BebasNeue', '', 14)

    pdf.text(35,15,str("FUERZAS MILITARES DE COLOMBIA"))
    pdf.text(35,20,str("EJERCITO NACIONAL DE COLOMBIA"))
    pdf.text(35,25,str("DESPACHO SEGUNDO COMANDANTE DEL EJÉRCITO"))

    pdf.image("C:/Users/nicolas.valbuena/Documents/programacion 2023/server/static/img/ejc.png",10,9,16,19)

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
    lugar_fecha  = str("Bogota - ")+str(dia)+" - " +str(mes)+" - " +str(anio) 
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
    pdf.text(100,43,"UNIDAD QUE LIDERA")
    pdf.set_text_color(70,70,70)
    responsable = "COEJC"
    numero = 43
    pdf.text(10,numero,responsable)
    numero= numero+7
    unidad_texto(pdf,"CEIGE", 10, numero, coejc_sejec)
    unidad_texto(pdf,"OSMEJ", 30, numero, coejc_sejec)
    unidad_texto(pdf,"DADAE", 50, numero, coejc_sejec)
    unidad_texto(pdf,"COTEF", 70, numero, coejc_sejec)

    pdf.set_font('BebasNeue', '', 14)
    numero = numero+9
    responsable = "SEJEC"
    
    pdf.text(10,numero,responsable)
    numero= numero+7
    unidad_texto(pdf,"CEAYG", 10, numero, coejc_sejec)
    unidad_texto(pdf,"COATE", 30, numero, coejc_sejec)
    unidad_texto(pdf,"DIRIE", 50, numero, coejc_sejec)
    unidad_texto(pdf,"DANTE", 70, numero, coejc_sejec)
    unidad_texto(pdf,"OADAS", 90, numero, coejc_sejec)
    unidad_texto(pdf,"COFIP", 110, numero, coejc_sejec)
    unidad_texto(pdf,"OGENE", 130, numero, coejc_sejec)

    numero= 43
    unidad_texto(pdf,"JEMOP", 180, numero, coejc_sejec)
    numero= numero +8
    unidad_texto(pdf,"JEMPP", 180, numero, coejc_sejec)
    numero= numero +8
    unidad_texto(pdf,"JEMGF", 180, numero, coejc_sejec)
    numero= numero +8
    unidad_texto(pdf,"JEMIC", 180, numero, coejc_sejec)


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
    position = 10
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(128,0,0)
    pdf.text(position,numero,"Fecha de cumplimiento")
    pdf.set_font('BebasNeue', '', 14)
    pdf.set_text_color(70,70,70)
    position = 50
    pdf.text(position,numero,str(fecha_cumplimiento))
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
    pdf.rounded_rect(7, numero, 202, z, 1,'D', '1234')
    
    pdf.line(5, 255, 211, 255)

    pdf.set_font('BebasNeue', '', 12)
    #pdf.text(10,265,"TC. JULIAN PRIETO")
    dato=""
    dato_1=""
    dato_2=""
    for x in usuarios:
        if x[3]=='Firma SEJEC':
            dato = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(10,265,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(10,270,x[2])
        if x[3]=='Firma Ayudante Personal':
            dato_1 = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(75,265,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(75,270,x[2])
        if x[3]=='Firma Juridica':
            dato_2 = x[0]+"\n"+x[2]+"\n"
            pdf.set_font('BebasNeue', '', 12)
            pdf.text(155,265,x[0])
            pdf.set_font('BebasNeue', '', 10)
            pdf.text(155,270,x[2])




    #pip install qrcode
    #pip install pillow
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/qr/"
    import qrcode
    orfeo_qr = orfeo



    inf_qur = orfeo_qr+" \n"+unidades_que_lideran + "\nFecha de Cumplimento "+fecha_cumplimiento +"\n------------------------------------------------------ \nplazos asignado por:\n"+dato+dato_1+dato_2

    img = qrcode.make(inf_qur)
    f = open(dirercion_archvios+"QR.png", "wb")
    img.save(f)
    f.close()
    pdf.image(dirercion_archvios+"QR.png",186,5.5,24,24)
    
    dirercion_archvios = "C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/"
    direcion = dirercion_archvios+str("z")+'.pdf'
    pdf.output(direcion, 'F')
    

        #import os
    listaPdfs = os.listdir('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/')
    merger = PdfFileMerger()



    documento_guardado = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/'+direcion_plazo_fina
    #print(documento_guardado)

    #for file in listaPdfs:
        #print(file)
        #pdf_doc = PdfFileReader('C:/Users/nicolas.valbuena/Documents/programacion 2023/server/tipo_plazos/a_a_guardar_evento/documentos/'+file, strict=False)
        #merger.append(pdf_doc)
    #merger.write(documento_guardado)
    import fitz

    result = fitz.open()

    for pdf in listaPdfs:
        pdf_doc = 'C:/Users/nicolas.valbuena/Documents/programacion 2023/server/ordenes_sejec_leer_asignar/documentos/'+pdf
        with fitz.open(pdf_doc) as mfile:
            result.insert_pdf(mfile)
        
    result.save(documento_guardado)

    documento_eliminar = ["z.pdf"]
    for doc in documento_eliminar:
        path = os.path.join(dirercion_archvios, doc)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

def numero_orden_select(dato):
    unidad_user = dato['unidad_user']  # Ejemplo: 'DIV01', '991', '992'
    estado_orden = 'ORDEN ASIGNADA AYUDANTE'

    conn = connect()
    cursor = conn.cursor()

    # Si unidad_user es 991 o 992, se omite el filtrado jerárquico y por abreviaturas
    if unidad_user in ['991', '992']:
        cursor.execute("""
            SELECT * FROM tabla_ordenes
            WHERE estado_orden = %s
        """, (estado_orden,))
        ordenes_finales = cursor.fetchall()
        columnas = [desc[0] for desc in cursor.description]

        cursor.close()
        conn.close()
        return [ordenes_finales]

    # 1. Verificar si la unidad raíz existe (ID_COMAND)
    cursor.execute("SELECT ID_COMAND FROM unidades_internas WHERE ID_COMAND = %s", (unidad_user,))
    fila_raiz = cursor.fetchone()

    if not fila_raiz:
        #print("Unidad raíz no encontrada.")
        cursor.close()
        conn.close()
        return []

    id_raiz = fila_raiz[0]
    #print("ID_COMAND raíz:", id_raiz)

    # 2. Obtener jerarquía de unidades hijas (ABREV_JEFATURA)
    cursor.execute("""
        WITH RECURSIVE jerarquia AS (
            SELECT ID_COMAND, ABREV_JEFATURA
            FROM unidades_internas
            WHERE ID_COMAND = %s
            UNION ALL
            SELECT u.ID_COMAND, u.ABREV_JEFATURA
            FROM unidades_internas u
            INNER JOIN jerarquia j ON u.ID_FUERZA = j.ID_COMAND
        )
        SELECT ABREV_JEFATURA FROM jerarquia
    """, (id_raiz,))
    abrev_unidades = [r[0] for r in cursor.fetchall()]
    #print("Unidades jerárquicas generadas (ABREV_JEFATURA):", abrev_unidades)

    # 3. Buscar órdenes lideradas por esas unidades (tabla_relacion_unidades)
    resultados_1 = []
    columnas_1 = []

    if abrev_unidades:
        abrev_unidades = [a.strip() for a in abrev_unidades]
        formato_in = ','.join(['%s'] * len(abrev_unidades))
        query = f"""
            SELECT o.*
            FROM tabla_ordenes o
            JOIN tabla_relacion_unidades r ON o.id_tabla_ordenes = r.id_tabla_ordenes
            WHERE o.estado_orden = %s
            AND r.relacion_unidad = 'LIDERA'
            AND TRIM(r.unidad) IN ({formato_in})
        """
        cursor.execute(query, (estado_orden, *abrev_unidades))
        resultados_1 = cursor.fetchall()
        columnas_1 = [desc[0] for desc in cursor.description]
        #print(f"Órdenes encontradas (lidera): {resultados_1}")
    else:
        print("No se encontraron unidades hijas.")

    # 4. Buscar órdenes propias (unidad exacta)
    cursor.execute("""
        SELECT * FROM tabla_ordenes
        WHERE estado_orden = %s AND unidad = %s
    """, (estado_orden, unidad_user))
    resultados_2 = cursor.fetchall()

    # 5. Consolidar resultados únicos
    ordenes_unicas = {}
    if columnas_1:
        id_index = columnas_1.index('id_tabla_ordenes')
    else:
        id_index = None

    for fila in resultados_1 + resultados_2:
        if id_index is None:
            columnas = [desc[0] for desc in cursor.description]
            id_index = columnas.index('id_tabla_ordenes')
        orden_id = fila[id_index]
        ordenes_unicas[orden_id] = fila

    ordenes_finales = sorted(ordenes_unicas.values(), key=lambda x: x[id_index] if id_index is not None else 0)

    cursor.close()
    conn.close()

    return [ordenes_finales]


def numero_orden_select_ver(contents):

       
    conn = connect()
    cursor = conn.cursor()

    id_orden = contents["id_orden"]

    query_tabla_log= """SELECT 
                tabla_log.full_nombre, 
                tabla_log.evento_registrar, 
                tabla_log.fecha,                                 
                unidades_internas.ABREV_JEFATURA,
                unidades_internas.DESCRIPCION_JEFATURA  
                FROM tabla_log 
                INNER  JOIN unidades_internas ON unidades_internas.ID_COMAND = tabla_log.unidad_user
                where id_tabla_ordenes = {} 
                  """.format(id_orden)
    cursor.execute(query_tabla_log)
    tabla_log = cursor.fetchall()

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

    for fila in tabla_relacion_ordenes:
        # De la posición 2 a la 8: prioridad (7 items)
        for i in range(7):
            nivel_prioridad[i].append(fila[i + 0])
        
        # De la posición 9 a la 15: autoridad (7 items)
        for i in range(7):
            nivel_autoridad[i].append(fila[i + 7])
        
        # De la posición 16 a la 22: sop (7 items)
        for i in range(7):
            sop_estado_mayor[i].append(fila[i + 14])


    conn.close()
    cursor.close

    #query = "select * from usuarios_dirop"
    #cursor.execute(query)
    #data = cursor.fetchall()

    conn.close()
    cursor.close

    return [tabla_log, unidad_que_lidera, unidad_que_apoya, unidad_que_cordina, nivel_prioridad, nivel_autoridad, sop_estado_mayor]

