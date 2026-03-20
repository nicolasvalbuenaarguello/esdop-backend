import json
import os
import shutil
# from funtions.pdf.resultados.pdf import *
from tipo_docker.a_p_res_mineria_nuew.models.funtions.pdf.boletin_coe import *
#Funcion de resultados nueva ayuda

def pdf_mapa_mineria_completo(datos, link, ruta, puerto):


    nombre_carpeta = "filtrar_pdf{}/".format(puerto)
    link = link+nombre_carpeta
    dirercion_archvios = link
    try:
        os.mkdir(link)
    except FileExistsError:
        print("Directorio %s ya existe" % link)
        for files in os.listdir(dirercion_archvios):
            path = os.path.join(dirercion_archvios, files)
            try:
                shutil.rmtree(path)
            except OSError:
                os.remove(path)
    #permisos

    # print(datos['permiso'])
    permiso = datos['permiso']
    unidad =  datos['unidad']
    fullname = datos['fullname']

    #fechas
    fecha_primer_lapso_inicial = datos['fecha_primer_lapso_inicial']
    fecha_ultimo_lapso_inicial = datos['fecha_ultimo_lapso_inicial']
    fecha_primer_lapso_final = datos['fecha_primer_lapso_final']
    fecha_ultimo_lapso_final = datos['fecha_ultimo_lapso_final']

    #unidades
    agr_div = datos['agr_div']
    Div_FT = datos['Div_FT']
    br = datos['br']
    ut = datos['ut']
    #lugar 
    dpto = datos['dpto']
    mpio = datos['mpio']
    #tipo de filtro
    filtro = datos['filtro']

    #enemigo - op - mayor
    enemigo = datos['enemigo']
    op_mayores = datos['op_mayores']
    #apoyo unidad
    apoyo_unidad = datos['apoyo_unidad']
    #afectaciones y titulo
    afectaciones = datos['afectaciones']
    tipo_titulo = datos['tipo_titulo']
    direcion = []
    #documento
    documento = datos['documento']


    spoa =  datos['spoa']
    delco_cap =  datos['delco_cap']
    estrategia =  datos['estrategia']
    gaulas =  datos['gaulas']
    coordinadas =  datos['coordinadas']
    conjuntas =  datos['conjuntas']
    tipo_afectaciones =  datos['tipo_afectaciones']
     
    tipo_operacion =  datos['tipo_operacion']

    cdte =  datos['cdte']

    hechos =  datos['hechos']
    acam_enemigo =  datos['acam_enemigo']
    acam_estructura =  datos['acam_estructura']
    ene_estructura =  datos['ene_estructura']
    subregion = json.loads(datos['subregion'])
    # print(documento)
    filtros = (agr_div, Div_FT, br, ut, filtro, dpto, mpio, enemigo, op_mayores, apoyo_unidad, afectaciones, tipo_titulo, permiso, unidad, fullname, ruta, spoa, delco_cap, estrategia, gaulas, coordinadas, conjuntas, tipo_afectaciones, tipo_operacion, cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion)

    direcion = pdf_boletin_mineria(fecha_primer_lapso_inicial, fecha_ultimo_lapso_inicial, filtros, dirercion_archvios,nombre_carpeta) 
    
    dir = {
                "direccion":direcion[0],
                "nombre":direcion[1]
            }

    return dir

def pdf_mapa_mineria(datos, link, ruta, puerto):
    try:
        import json
        import traceback

        nombre_carpeta = "filtrar_pdf_{}/".format(puerto)
        link = link+nombre_carpeta
        dirercion_archvios = link
        try:
            os.mkdir(link)
        except FileExistsError:
            print("Directorio %s ya existe" % link)
            for files in os.listdir(dirercion_archvios):
                path = os.path.join(dirercion_archvios, files)
                try:
                    shutil.rmtree(path)
                except OSError:
                    os.remove(path)
        #permisos

        # print(datos['permiso'])
        #fechas

        
        # Obtener todos los campos del formulario
        permiso = datos['permiso']
        unidad = datos['unidad']
        fullname = datos['fullname']

        fechaInicio = datos['fechaInicio']
        fechaFin = datos['fechaFin']
        fechaInicioAnterior= datos['fechaInicioAnterior']
        fechaFinAnterior= datos['fechaFinAnterior']

        fecha = (fechaInicio, fechaFin, fechaInicioAnterior, fechaFinAnterior)

        agr_div = datos['agr_div']
        Div_FT = datos['Div_FT']
        br = datos['br']
        ut = datos['ut']
        dpto = datos['dpto']
        mpio = datos['mpio']
        filtro = datos['filtro']
        enemigo = datos['enemigo']
        op_mayores = datos['op_mayores']
        apoyo_unidad = datos['apoyo_unidad']
        afectaciones = datos['afectaciones']
        tipo_titulo = datos['tipo_titulo']
        documento = datos['documento']
        spoa = datos['spoa']
        delco_cap = datos['delco_cap']
        estrategia = datos['estrategia']
        gaulas = datos['gaulas']
        coordinadas = datos['coordinadas']
        conjuntas = datos['conjuntas']
        tipo_afectaciones = datos['tipo_afectaciones']
        tipo_operacion = datos['tipo_operacion']
        cdte = datos['cdte']
        hechos = datos['hechos']
        acam_enemigo = datos['acam_enemigo']
        acam_estructura = datos['acam_estructura']
        ene_estructura = datos['ene_estructura']
        subregion = json.loads(datos['subregion'])

        # Agrupar filtros
        filtros = (
            agr_div,          # 0
            Div_FT,           # 1
            br,               # 2
            ut,               # 3
            filtro,           # 4
            dpto,             # 5
            mpio,             # 6
            enemigo,          # 7
            op_mayores,       # 8
            apoyo_unidad,     # 9
            afectaciones,     # 10
            tipo_titulo,      # 11
            permiso,          # 12
            unidad,           # 13
            fullname,         # 14
            ruta,             # 15
            spoa,             # 16
            delco_cap,        # 17
            estrategia,       # 18
            gaulas,           # 19
            coordinadas,      # 20
            conjuntas,        # 21
            tipo_afectaciones,# 22
            tipo_operacion,   # 23
            cdte,             # 24
            hechos,           # 25
            acam_enemigo,     # 26
            acam_estructura,  # 27
            ene_estructura,   # 28
            subregion         # 29
        )


        # Llamada principal
        direccion = pdf_boletin_mineria_mapa(
            fecha,
            filtros,
            dirercion_archvios,
            nombre_carpeta
        )
        direccion_f = {
                    "direccion":direccion[0],
                    "nombre":direccion[1]
                }
        return direccion_f

    except KeyError as e:
        print("❌ Campo faltante:", e)
        traceback.print_exc()  # También útil para ver dónde faltó
        raise ValueError(f"Campo requerido faltante: {e}")

    except Exception as e:
        print("❌ Error general en boletin_estadistica_resultados:")
        traceback.print_exc()  # 🔥 Aquí sale la línea exacta
        raise RuntimeError("Error interno en la generación del boletín")


def mapa_resultados(datos):
    import json
    import traceback

    try:
        # Obtener todos los campos del formulario
        permiso = datos['permiso']
        unidad = datos['unidad']
        fullname = datos['fullname']

        fechaInicio = datos['fechaInicio']
        fechaFin = datos['fechaFin']
        fechaInicioAnterior= datos['fechaInicioAnterior']
        fechaFinAnterior= datos['fechaFinAnterior']

        fecha = (fechaInicio, fechaFin, fechaInicioAnterior, fechaFinAnterior)

        agr_div = datos['agr_div']
        Div_FT = datos['Div_FT']
        br = datos['br']
        ut = datos['ut']
        dpto = datos['dpto']
        mpio = datos['mpio']
        filtro = datos['filtro']
        enemigo = datos['enemigo']
        op_mayores = datos['op_mayores']
        apoyo_unidad = datos['apoyo_unidad']
        afectaciones = datos['afectaciones']
        tipo_titulo = datos['tipo_titulo']
        documento = datos['documento']
        spoa = datos['spoa']
        delco_cap = datos['delco_cap']
        estrategia = datos['estrategia']
        gaulas = datos['gaulas']
        coordinadas = datos['coordinadas']
        conjuntas = datos['conjuntas']
        tipo_afectaciones = datos['tipo_afectaciones']
        tipo_operacion = datos['tipo_operacion']
        cdte = datos['cdte']
        hechos = datos['hechos']
        acam_enemigo = datos['acam_enemigo']
        acam_estructura = datos['acam_estructura']
        ene_estructura = datos['ene_estructura']
        subregion = json.loads(datos['subregion'])

        # Agrupar filtros
        filtros = (
            agr_div, Div_FT, br, ut, filtro, dpto, mpio,
            enemigo, op_mayores, apoyo_unidad, afectaciones,
            tipo_titulo, permiso, unidad, fullname, "",
            spoa, delco_cap, estrategia, gaulas, coordinadas,
            conjuntas, tipo_afectaciones, tipo_operacion,
            cdte, hechos, acam_enemigo, acam_estructura, ene_estructura, subregion
        )

        # Llamada principal
        direccion = pdf_mapa(
            fecha,
            filtros
        )

        return direccion

    except KeyError as e:
        print("❌ Campo faltante:", e)
        traceback.print_exc()  # También útil para ver dónde faltó
        raise ValueError(f"Campo requerido faltante: {e}")

    except Exception as e:
        print("❌ Error general en boletin_estadistica_resultados:")
        traceback.print_exc()  # 🔥 Aquí sale la línea exacta
        raise RuntimeError("Error interno en la generación del boletín")
