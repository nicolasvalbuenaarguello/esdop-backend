from datetime import datetime

def mes(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")

    if date == "01" or date == 1:
        return months[0]
    
    if date == "02" or date == 2:
        return months[1]
    
    if date == "03" or date == 3:
        return months[2]
    
    if date == "04" or date == 4:
        return months[3]
    
    if date == "05" or date == 5:
        return months[4]
        
    if date == "06" or date == 6:
        return months[5]
        
    if date == "07" or date == 7:
        return months[6]
        
    if date == "08" or date == 8:
        return months[7]
        
    if date == "09" or date == 9:
        return months[8]
        
    if date == "10" or date == 10:
        return months[9]
        
    if date == "11" or date == 11:
        return months[10]
        
    if date == "12" or date == 12:
        return months[11]
    
    
def fecha(fecha):
    fecha_dt = datetime.strptime(fecha, '%Y-%m-%d')
    dia_inicial = str(fecha_dt.strftime('%d'))
    mes_inicial = str(fecha_dt.strftime('%m'))
    año_inicial = str(fecha_dt.strftime('%Y'))
    mes_inicial_d = str(mes(mes_inicial))

    return[dia_inicial,mes_inicial_d,año_inicial, mes_inicial]


