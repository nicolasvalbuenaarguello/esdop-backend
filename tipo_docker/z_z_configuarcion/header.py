from fpdf import FPDF
from fpdf.php import sprintf
from .logo import *
from math import sqrt, pi, sin, cos, radians
from datetime import datetime
from .fechas import *
import qrcode


class PDF(FPDF):
    
    def __init__(self, orientation = 'P', unit = 'mm', format = 'A4'):
        self.ext_gstates = [ ]
        
        super(PDF, self).__init__(orientation, unit, format)

    def parametros(self, **kwargs):
        self.titulo = ""
        self.tamanio = "oficio"
        self.logo = ""
        self.fecha_titulo = ""
        self.permiso = "EJC"
        self.nivel = ""
        self.usuario = ""
        self.pie_pagina = "NO"
        self.fondo_pagina = "SI"
        self.seguridad = "JEMOP"
        self.precidencial =  "OK"
        self.ruta = ""
        self.imagen = ""
        self.img_qr = ""
        self.fecha_titulo_2=""

        for k in kwargs.items():
            if "titulo" == k[0]:
                self.titulo = k[1]
            if "tamanio" == k[0]:
                self.tamanio = k[1]
            if "logo" == k[0]:
                self.logo = k[1]
            if "fecha_titulo" == k[0]:
                self.fecha_titulo = k[1]
            if "permiso" == k[0]:
                self.permiso = k[1]
            if "nivel" == k[0]:
                self.nivel = k[1]
            if "usuario" == k[0]:
                self.usuario = k[1]
            if "pie_pagina" == k[0]:
                self.pie_pagina = k[1]
                
            if "fondo_pagina" == k[0]:
                self.fondo_pagina = k[1]
            if "seguridad" == k[0]:
                self.seguridad = k[1]
            if "precidencial" == k[0]:
                self.precidencial = k[1]
            if "ruta" == k[0]:
                self.ruta = k[1]
            if "imagen" == k[0]:
                self.imagen = k[1]
            if "img_qr" == k[0]:
                self.img_qr = k[1]
            if "fecha_titulo_2" == k[0]:
                self.fecha_titulo_2 = k[1]
        
    def header(self):
        #imagen
        
        logos = "LOGO JEMOP"
        imagen = self.ruta+self.imagen
        
        if self.fondo_pagina == "SI":
            if self.tamanio == "oficio":
                self.image(imagen,0,0,355.6,215.9)
                if self.logo == logos :
                    logo(self)
                    # Select Arial bold 15
                    self.set_font('Arial', 'B', 16)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Arial', 'B', 10)
                    self.text(160, 24, self.fecha_titulo)
                    print("xxx")
                    
                elif self.logo == "" :
                    # Select Arial bold 15
                    self.set_font('Arial', 'B', 16)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Arial', 'B', 10)
                    self.text(160, 24, self.fecha_titulo)

                else:
                    if self.seguridad =="antigua":
                        titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial', 'B', 16)
                        self.set_text_color(255,255,255)
                        self.text(65, 17, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(255,255,255)
                        self.set_font('Arial', 'B', 12)
                        self.text(65, 22.5, self.fecha_titulo)

                    elif self.seguridad =="nueva_sin_mapa":
                        
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        self.ln(1)
                        self.cell(43)
                        self.multi_cell(240, 7, self.titulo, 0, "L", False)
                        # fecha = strftime(self.fecha, '%y')
           
                        self.set_font('Arial Black', '', 15)
                        #self.text(52, 26, self.fecha_titulo)
                        self.ln(-0.5)
                        self.cell(43)
                        self.multi_cell(250, 5, self.fecha_titulo, 0, "L", False)
                        self.ln(-23.5)

                        self.set_text_color(125,0,0)
                        self.set_font('Arial Narrow', 'B', 12)
                        self.text(180,10,self.fecha_titulo_2)

                        t = "Fuerzas Militares de Colombia"
                        t_1 ="Ejército Nacional"
                        t_2 = "Usuario"
                        t_3 = "Unidad"

                        inf= "Resultados del Dia:"
                        fecha_Elaboracion = datetime.now()
                        inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + self.fecha_titulo +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +self.usuario+" \n" + t_3+" \n" +self.nivel
                        img = qrcode.make(inf_qur)
                        f = open(self.img_qr+"/QR.png", "wb")
                        img.save(f)
                        f.close()
                        self.image(self.img_qr+"/QR.png",330,3,23,23)
                        self.ln(10)


                    elif self.seguridad =="DISEO":
                        
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        self.text(55, 20, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(40,40,40)
                        self.set_font('Arial Black', '', 12)
                        self.text(55, 25.5, self.fecha_titulo)


                    elif self.seguridad =="nueva":
                        if "Diapositiva20" in self.imagen:
                            dis = 122
                            altura = 18
                            altura_2 = 22.5
                        elif "Diapositiva18_DISEO" in self.imagen:
                            dis = 55
                            altura = 18
                            altura_2 = 22.5
                        else:
                            dis = 140
                            altura = 20
                            altura_2 = 26
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.ln()
                        self.set_font('Arial Black', '', 13)
                        self.set_text_color(56,87,35)
                        self.ln(3)
                        self.cell(dis)
                        self.multi_cell(200, 5, self.titulo, 0, "L", False)
                        # fecha = strftime(self.fecha, '%y')
           
                        #self.set_font('Calibri', '', 16)
                        #self.text(52, 26, self.fecha_titulo)
                        self.ln(-0.5)
                        self.cell(dis)
                        self.multi_cell(250, 5, self.fecha_titulo, 0, "L", False)
                        self.ln(-16)

                        t = "Fuerzas Militares de Colombia"
                        t_1 ="Ejército Nacional"
                        t_2 = "Usuario"
                        t_3 = "Unidad"

                        inf= "Resultados del Dia:"
                        fecha_Elaboracion = datetime.now()
                        inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + self.fecha_titulo +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +self.usuario+" \n" + t_3+" \n" +self.nivel
                        #img = qrcode.make(inf_qur)
                        #f = open(self.img_qr+"/QR.png", "wb")
                        #img.save(f)
                        #f.close()
                        #self.image(self.img_qr+"/QR.png",330,3,23,23)

                    else:
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 15)
                        self.set_text_color(56,87,35)
                        self.text(55, 20, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(40,40,40)
                        self.set_font('Arial Black', '', 12)
                        self.text(55, 25.5, self.fecha_titulo)

            elif self.tamanio == "presentacion":
                self.image(imagen,0,0, 338.67, 190.5)
                if self.logo == logos :
                    logo(self)
                    # Select Arial bold 15
                    self.set_font('Arial', 'B', 16)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Calibri', '', 16)
                    self.text(160, 26, self.fecha_titulo)
                    print("xxx")

                elif self.logo == "" :
                    # Select Arial bold 15
                    self.set_font('Arial', 'B', 16)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Arial', 'B', 10)
                    self.text(160, 24, self.fecha_titulo)

                else:
                    if self.seguridad =="antigua":
                        titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial', 'B', 16)
                        self.set_text_color(255,255,255)
                        self.text(65, 17, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(255,255,255)
                        self.set_font('Arial', 'B', 12)
                        self.text(65, 22.5, self.fecha_titulo)

                    elif self.seguridad =="nueva_sin_mapa":
                        
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        self.text(55, 18, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(40,40,40)
                        self.set_font('Arial Black', '', 12)
                        self.text(55, 22.5, self.fecha_titulo)

                        t = "Fuerzas Militares de Colombia"
                        t_1 ="Ejército Nacional"
                        t_2 = "Usuario"
                        t_3 = "Unidad"

                        inf= "Resultados del Dia:"
                        fecha_Elaboracion = datetime.now()
                        inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + self.fecha_titulo +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +self.usuario+" \n" + t_3+" \n" +self.nivel
                        img = qrcode.make(inf_qur)
                        f = open(self.img_qr+"/QR.png", "wb")
                        img.save(f)
                        f.close()
                        self.image(self.img_qr+"/QR.png",330,3,23,23)


                    elif self.seguridad =="DISEO":
                        
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        self.text(55, 20, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(40,40,40)
                        self.set_font('Arial Black', '', 12)
                        self.text(55, 25.5, self.fecha_titulo)


                    elif self.seguridad =="nueva":
                        
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        #self.text(52, 20, self.titulo)
                        self.ln(3)
                        self.cell(42)
                        self.multi_cell(240, 7, self.titulo, 0, "L", False)
                        # fecha = strftime(self.fecha, '%y')
           
                        #self.set_font('Calibri', '', 16)
                        #self.text(52, 26, self.fecha_titulo)
                        self.ln(-0.5)
                        self.cell(42)
                        self.multi_cell(250, 5, self.fecha_titulo, 0, "L", False)
                        self.ln(-21.5)
                        t = "Fuerzas Militares de Colombia"
                        t_1 ="Ejército Nacional"
                        t_2 = "Usuario"
                        t_3 = "Unidad"

                        inf= "Resultados del Dia:"
                        fecha_Elaboracion = datetime.now()
                        inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + self.fecha_titulo +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +self.usuario+" \n" + t_3+" \n" +self.nivel
                        #img = qrcode.make(inf_qur)
                        #f = open(self.img_qr+"/QR.png", "wb")
                        #img.save(f)
                        #f.close()
                        #self.image(self.img_qr+"/QR.png",330,3,23,23)

                    else:
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 15)
                        self.set_text_color(56,87,35)
                        self.text(55, 20, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(40,40,40)
                        self.set_font('Arial Black', '', 12)
                        self.text(55, 25.5, self.fecha_titulo)

            elif self.tamanio == "carta":

                self.image(imagen,0,0,279,216)

                if self.logo == logos :
                    print("1")
                    logo(self)
                    # Select Arial bold 15
                    self.set_font('Arial', 'B', 15)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Arial', 'B', 10)
                    self.text(160, 26, self.fecha_titulo)
                elif self.logo == "" :
               
                     # Select Arial bold 15
                    self.set_font('Arial', 'B', 15)
                    self.set_text_color(255,255,255)
                    self.text(90, 20, self.titulo)
                    # fecha = strftime(self.fecha, '%y')
                    self.set_text_color(70,70,70)
                    self.set_font('Arial', 'B', 10)
                    self.text(160, 26, self.fecha_titulo)
                else:
                    if self.seguridad!="nueva" and self.seguridad!="sin_qr":
                  
                        titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial', 'B', 16)
                        self.set_text_color(255,255,255)
                        self.text(65, 17, self.titulo)
                        # fecha = strftime(self.fecha, '%y')
                        self.set_text_color(255,255,255)
                        self.set_font('Arial', 'B', 12)
                        self.text(65, 22.5, self.fecha_titulo)
                        

                        

                    elif self.seguridad=="sin_qr":
               
                        #titulo_barra(self)
                        # Select Arial bold 15
                        self.set_font('Arial Black', '', 16)
                        self.set_text_color(56,87,35)
                        self.ln(1)
                        self.cell(32)
                        self.multi_cell(240, 7, self.titulo, 0, "L", False)
                        # fecha = strftime(self.fecha, '%y')
           
                        self.set_font('Arial Black', '', 15)
                        #self.text(52, 26, self.fecha_titulo)
                        self.ln(-0.5)
                        self.cell(32)
                        self.multi_cell(250, 5, self.fecha_titulo, 0, "L", False)
                        self.ln(-23.5)

                        self.set_text_color(166,166,166)
                        self.set_font('Arial Narrow', 'B', 11)
                        self.ln(22.5)
                        self.cell(130)
                        self.multi_cell(97, 5, self.fecha_titulo_2, 0, "R", False)
                        self.ln(-7)
                        self.ln(-18.5)
                        self.ln(5)
                      
                       

                    else:
                        #titulo_barra(self)
                        # Select Arial bold 15
                      # Select Arial bold 15
                        self.set_font('Arial Black', '', 15)
                        self.set_text_color(56,87,35)
                        self.ln(1)
                        self.cell(32)
                        self.multi_cell(200, 7, self.titulo, 0, "L", False)
                        # fecha = strftime(self.fecha, '%y')
           
                        self.set_font('Arial Black', '', 15)
                        #self.text(52, 26, self.fecha_titulo)
                        self.ln(-0.5)
                        self.cell(32)
                        self.multi_cell(180, 5, self.fecha_titulo, 0, "L", False)
                        self.ln(-18.5)

                        self.set_text_color(125,0,0)
                        self.set_font('Arial Narrow', 'B', 12)
                        self.text(140,10,self.fecha_titulo_2)

                    
                        t = "Fuerzas Militares de Colombia"
                        t_1 ="Ejército Nacional"
                        t_2 = "Usuario"
                        t_3 = "Unidad"

                        inf= "Resultados del Dia:"
                        fecha_Elaboracion = datetime.now()
                        inf_qur = t+" \n" + t_1+" \n" + inf+" \n" + self.fecha_titulo +" \n" + "Fecha de Elaboración Boletín: \n" +str(fecha_Elaboracion) +" \n" +"--------------------------------------------------- \n"+t_2+" \n" +self.usuario+" \n" + t_3+" \n" +self.nivel
                        img = qrcode.make(inf_qur)
                        f = open(self.img_qr+"/QR.png", "wb")
                        img.save(f)
                        f.close()
                        self.image(self.img_qr+"/QR.png",253,3,23,23)

        
        self.ln(25)

    def footer(self):
        
        if self.pie_pagina =="SI":
            self.set_text_color(80,80,80)
            # Go to 1.5 cm from bottom
            self.set_y(-15)
            # Select Arial italic 8
            self.set_font('Arial', 'B', 10)
            # Print centered page number
            # self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

            dias = datetime.now().day
            meses = datetime.now().month
            anios = datetime.now().year
            # print(datetime.now().month)
            meses = mes(meses)
            meses =str(meses)
            meses = meses.upper()
            # print(meses)   
            fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)

            if self.precidencial == "OK":
                self.text(55, 212, "SECRETO          " + str(fecha_actual))
                self.text(15, 212, 'Fuente: SICOE')
            else:
                self.text(95, 212, "SECRETO ")
                self.text(15, 212, 'Fuente: SICOE')


            if self.seguridad == "JEMOP": 
                self.text(140, 212, '"Se deben verificar los datos con CEDE3 - DISEO"')
            

            if self.permiso != "EJC":
                self.set_text_color(128,0,0)
                self.text(230, 212, "Usuario: '"+str(self.usuario)+" unidad (" + str(self.nivel)+")'")
        elif self.pie_pagina =="SI - SIN FECHA":
            self.set_text_color(80,80,80)
            # Go to 1.5 cm from bottom
            self.set_y(-15)
            # Select Arial italic 8
            self.set_font('Arial', 'B', 10)
            # Print centered page number
            # self.cell(0, 10, 'Page %s' % self.page_no(), 0, 0, 'C')

            dias = datetime.now().day
            meses = datetime.now().month
            anios = datetime.now().year
            # print(datetime.now().month)
            meses = mes(meses)
            meses =str(meses)
            meses = meses.upper()
            # print(meses)   
            fecha_actual = str(dias) +" "+ str(meses) +" "+ str(anios)

            if self.precidencial == "OK":
                self.text(55, 212, "SECRETO          ")
                self.text(15, 212, 'Fuente: SICOE')
            else:
                self.text(95, 212, "SECRETO ")
                self.text(15, 212, 'Fuente: SICOE')


            if self.seguridad == "JEMOP": 
                self.text(140, 212, '"Se deben verificar los datos con CEDE3 - DISEO"')
            

            if self.permiso != "EJC":
                self.set_text_color(128,0,0)
                self.text(230, 212, "Usuario: '"+str(self.usuario)+" unidad (" + str(self.nivel)+")'")


    def draw_circle(self, xc, yc, r, style='S'):
        """
        Dibuja un círculo usando curvas Bézier (vectorial).
        :param xc: coordenada X del centro
        :param yc: coordenada Y del centro
        :param r: radio del círculo
        :param style: 'S' contorno | 'F' relleno | 'FD' contorno + relleno
        """
        k = self.k
        hp = self.h
        op = {'F': 'f', 'FD': 'B', 'DF': 'B'}.get(style, 'S')
        
        # Constante mágica para aproximar el círculo con Bézier
        MyArc = 4/3 * (2**0.5 - 1)

        # Puntos de control
        self._out(f'{(xc + r)*k:.2f} {(hp - yc)*k:.2f} m')

        # Cuatro cuadrantes
        self._arc(xc + r, yc - r*MyArc, xc + r*MyArc, yc - r, xc, yc - r)
        self._arc(xc - r*MyArc, yc - r, xc - r, yc - r*MyArc, xc - r, yc)
        self._arc(xc - r, yc + r*MyArc, xc - r*MyArc, yc + r, xc, yc + r)
        self._arc(xc + r*MyArc, yc + r, xc + r, yc + r*MyArc, xc + r, yc)
        self._out(op)

    def polygon_rounded(self, points, radius=3, style='S'):
        """
        Dibuja un polígono con esquinas redondeadas y contorno cerrado.
        :param points: lista de tuplas [(x1, y1), (x2, y2), ...]
        :param radius: radio de redondeo
        :param style: 'S' = contorno, 'F' = relleno, 'FD' = contorno + relleno
        """
        if len(points) < 3:
            raise ValueError("Se necesitan al menos 3 puntos para un polígono")

        k = self.k
        hp = self.h

        # Determinar operación PDF
        if style == 'F':
            op = 'f'
        elif style in ('FD', 'DF'):
            op = 'B'
        else:
            op = 'S'

        def pdf_point(x, y):
            return f'{x * k:.2f} {(hp - y) * k:.2f}'

        def interpolate(p1, p2, d):
            dx, dy = p2[0] - p1[0], p2[1] - p1[1]
            dist = (dx**2 + dy**2) ** 0.5
            if dist == 0:
                return p1
            t = min(d / dist, 0.5)
            return (p1[0] + dx * t, p1[1] + dy * t)

        n = len(points)
        path_cmds = []

        # Iniciar el trazado
        for i in range(n):
            p1 = points[i - 1]
            p2 = points[i]
            p3 = points[(i + 1) % n]

            # Calcular puntos de entrada/salida para la esquina redondeada
            p2a = interpolate(p2, p1, radius)
            p2b = interpolate(p2, p3, radius)

            if i == 0:
                path_cmds.append(f'{pdf_point(*p2a)} m')
            else:
                path_cmds.append(f'{pdf_point(*p2a)} l')

            # Curva Bézier desde p2a → p2 → p2b
            path_cmds.append(f'{pdf_point(*p2a)} {pdf_point(*p2)} {pdf_point(*p2b)} c')

        # 🔒 Cerrar el polígono
        path_cmds.append('h')
        path_cmds.append(op)

        for cmd in path_cmds:
            self._out(cmd)


    def draw_hexagon_rounded(self, xc, yc, r, radius=3, style='S'):
        """
        Dibuja un hexágono regular con esquinas redondeadas.
        :param xc: coordenada X del centro
        :param yc: coordenada Y del centro
        :param r: radio (distancia del centro a un vértice)
        :param radius: radio de redondeo
        :param style: 'S' = contorno, 'F' = relleno, 'FD' = contorno + relleno
        """
        points = []
        for i in range(6):
            angle = radians(30 + i * 60)
            x = xc + r * cos(angle)
            y = yc + r * sin(angle)
            points.append((x, y))
        self.polygon_rounded(points, radius=radius, style=style)

    def polygon(self, points, style='S'):
        """
        Dibuja una figura poligonal libre conectando los puntos dados.

        :param points: lista de tuplas [(x1, y1), (x2, y2), ...]
        :param style: 'S' = solo contorno, 'F' = relleno, 'FD' o 'DF' = contorno + relleno
        """
        k = self.k
        hp = self.h

        if not points or len(points) < 3:
            raise ValueError("Se necesitan al menos 3 puntos para un polígono")

        # Determinar tipo de operación
        if style == 'F':
            op = 'f'
        elif style in ('FD', 'DF'):
            op = 'B'
        else:
            op = 'S'

        # Moverse al primer punto
        x0, y0 = points[0]
        self._out(f'{x0 * k:.2f} {(hp - y0) * k:.2f} m')

        # Trazar líneas entre los puntos
        for (x, y) in points[1:]:
            self._out(f'{x * k:.2f} {(hp - y) * k:.2f} l')

        # Cerrar figura
        self._out(f'{x0 * k:.2f} {(hp - y0) * k:.2f} l')
        self._out(op)


    def draw_triangle(self, xc, yc, r, style='S'):
        """
        Dibuja un triángulo equilátero centrado en (xc, yc) con radio r.
        :param style: 'S' = contorno, 'F' = relleno, 'FD' = contorno + relleno
        """
        points = []
        for i in range(3):
            angle = radians(90 + i * 120)
            x = xc + r * cos(angle)
            y = yc + r * sin(angle)
            points.append((x, y))
        self.polygon(points, style)


    def draw_hexagon(self, xc, yc, r, style='S'):
        """
        Dibuja un hexágono regular centrado en (xc, yc) con radio r.
        :param style: 'S' = contorno, 'F' = relleno, 'FD' = contorno + relleno
        """
        points = []
        for i in range(6):
            angle = radians(30 + i * 60)
            x = xc + r * cos(angle)
            y = yc + r * sin(angle)
            points.append((x, y))
        self.polygon(points, style)


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