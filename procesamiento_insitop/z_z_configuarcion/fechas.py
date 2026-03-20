from datetime import datetime

def mes(date):
    months = (
        "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
        "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
    )

    try:
        mes = int(date)  # acepta "01", "1", 1, etc.
        return months[mes - 1]
    except (ValueError, IndexError):
        return None  # o lanzar una excepción si prefieres
    
def mes_2(date):
    months = (
        "Ene", "Feb", "Mar", "Abr", "May", "Jun",
        "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"
    )

    try:
        mes = int(date)  # acepta "01", "1", 1, etc.
        return months[mes - 1]
    except (ValueError, IndexError):
        return None  # o lanzar una excepción si prefieres
    
from datetime import datetime, date

def fecha(fecha):
    # Asegurar tipo correcto
    if isinstance(fecha, date):
        fecha_dt = fecha
    else:
        fecha_dt = datetime.strptime(fecha, '%Y-%m-%d').date()

    dia_inicial = fecha_dt.strftime('%d')
    mes_inicial = fecha_dt.strftime('%m')
    año_inicial = fecha_dt.strftime('%Y')

    mes_inicial_d = mes(mes_inicial)     # nombre del mes
    mes_inicial_2 = mes_2(mes_inicial)           # número del mes (corregido)

    return [
        dia_inicial,
        mes_inicial_d,
        año_inicial,
        mes_inicial,
        mes_inicial_2
    ]



