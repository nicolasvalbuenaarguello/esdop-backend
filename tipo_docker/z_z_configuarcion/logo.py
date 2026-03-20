def logo(self):
    TOTAL = -30
    self.set_line_width(0.3)
    self.set_draw_color(140, 140, 140)
    self.set_fill_color(140, 140, 140)
    self.rounded_rect(75, 15.5, 80, 10.5, 1,'FD', '1234')

    self.set_fill_color(255, 255, 255)
    self.rounded_rect(75, 15, 81, 10, 1,'FD', '1234')

    self.set_line_width(0.3)
    self.set_draw_color(193, 30, 38)
    self.rounded_rect(75, 14, 100, 9, 1,'FD', '1234')

    self.set_fill_color(193, 30, 38)
    self.rounded_rect(75, 15.5, 170, 6, 1,'FD', '1234')

    xc = 74
    yc = 20
    r = 11

    dato = TOTAL
    dato = 360 * dato / 100

    self.set_line_width(0.1)
    self.set_fill_color(255, 255, 255)
    self.set_draw_color(255, 255, 255)
    re = r+8
    self.ellipse(xc-(re/2),yc-(re/2),re,re,'FD')

    self.set_fill_color(80, 80, 80)
    self.sector(xc,yc,r,dato-2, 0, 'F')

    if dato >=0:
        self.set_fill_color(16, 158, 48)
        self.sector(xc,yc,r,0, dato, 'F')
    else:
        self.set_fill_color(193, 30, 38)
        self.sector(xc,yc,r,dato,0,'F')

    self.set_line_width(0.3)
    self.set_fill_color(255, 255, 255)
    self.set_draw_color(140, 140, 140)
    re = r+5
    self.ellipse(xc-(re/2),yc-(re/2),re,re,'FD')

    self.set_fill_color(80, 80, 80)
    re = r+1
    self.ellipse(xc-(re/2),yc-(re/2),re,re,'FD')

    self.set_fill_color(193, 30, 38)
    re = r+0.5
    self.ellipse(xc-(re/2),yc-(re/2),re,re,'FD')

    self.image("src/static/img/mayor.JPG",84,16,5.5,5.5)
    self.image("src/static/img/soldado.JPG",xc-(re/3),yc-(re/3),7,7)

def titulo_barra(self):
    self.set_fill_color(193, 30, 38)
    self.rounded_rect(63, 10, 220, 15, 1,'F', '1234')
