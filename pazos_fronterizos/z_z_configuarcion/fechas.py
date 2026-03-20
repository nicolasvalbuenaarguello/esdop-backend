from datetime import datetime

def mes_2(date):
    months = ("ENE", "FEB", "MAR", "ABR", "MAY", "JUN", 
              "JUL", "AGO", "SEP", "OCT", "NOV", "DIC")
    # Convertimos a int para cubrir "01" y 1
    return months[int(date) - 1]

def mes(date):
    months = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
              "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
    return months[int(date) - 1]

def fecha(fecha_str):
    fecha_dt = datetime.strptime(fecha_str, "%Y-%m-%d")
    dia_inicial = fecha_dt.strftime("%d")
    mes_inicial = fecha_dt.strftime("%m")
    año_inicial = fecha_dt.strftime("%Y")

    mes_inicial_d = mes(mes_inicial)      # Nombre completo
    mes_inicial_d_2 = mes_2(mes_inicial)  # Abreviado

    return [dia_inicial, mes_inicial_d, año_inicial, mes_inicial, mes_inicial_d_2]
