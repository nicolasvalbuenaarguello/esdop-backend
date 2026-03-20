def caligrafia_ingreso( pdf, dirercion_archvios):
    ruta = dirercion_archvios
 
    ruta_c_b='{}static/font/calibri-font-sv/calibri font sv/Calibri Bold/Calibri_Bold.TTF'.format(ruta) 
    ruta_c='{}static/font/calibri-font-sv/calibri font sv/Calibri Light/Calibri_Light.ttf'.format(ruta)
    ruta_b='{}static/font/bebas_neue/bebas/BebasNeue_Regular.ttf'.format(ruta)

    ruta_narro_b='{}/static/font/Arial Narrow/arialnarrow_bold.ttf'.format(ruta)
    ruta_narro_b_i='{}/static/font/Arial Narrow/arialnarrow_bolditalic.ttf'.format(ruta)
    ruta_narro_i='{}/static/font/Arial Narrow/arialnarrow_italic.ttf'.format(ruta)
    ruta_narro='{}/static/font/Arial Narrow/arialnarrow.ttf'.format(ruta)
    ruta_arial_black='{}/static/font/Arial Black/arial_black.ttf'.format(ruta)

    
    pdf.add_font('Calibri', 'B',ruta_c_b , uni=True)
    pdf.add_font('Calibri', '', ruta_c, uni=True)
    pdf.add_font('BebasNeue', '', ruta_b, uni=True)

    pdf.add_font('Arial Narrow', '', ruta_narro, uni=True)
    pdf.add_font('Arial Narrow', 'B', ruta_narro_b, uni=True)
    pdf.add_font('Arial Narrow', 'Bi', ruta_narro_b_i, uni=True)
    pdf.add_font('Arial Narrow', 'i', ruta_narro_i, uni=True)
    
    pdf.add_font('Arial Black', '', ruta_arial_black, uni=True)

def dias_semana(dia):
    dia_semana =""
    if dia == 0:
        dia_semana = "LUNES"
    elif dia == 1:
        dia_semana = "MARTES"
    elif dia == 2:
        dia_semana = "MIERCOLES"
    elif dia == 3:
        dia_semana = "JUEVES"
    elif dia == 4:
        dia_semana = "VIERNES"
    elif dia == 5:
        dia_semana = "SABADO"
    elif dia == 6:
        dia_semana = "DOMINGO"
    else:
        dia_semana = "verifcar codigo"
    return dia_semana
    
