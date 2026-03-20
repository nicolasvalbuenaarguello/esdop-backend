import json
from tipo_docker.b_f_resultados_lineas_estrategicas_paya_power.models.funtions.pdf.boletin_coe import comparativo_comparativo_mapa


def res_linea_estrategica_narcotrafico_power_point(datos: dict, link: str, ruta: str, puerto: int):

    try:

        # ================================
        # PERMISOS
        # ================================
        permiso = datos.get('permiso')
        unidad = datos.get('unidad')
        fullname = datos.get('fullname')

        # ================================
        # FECHAS
        # ================================
        fecha_primer_lapso_inicial = datos.get('fecha_primer_lapso_inicial')
        fecha_ultimo_lapso_inicial = datos.get('fecha_ultimo_lapso_inicial')
        fecha_primer_lapso_final = datos.get('fecha_primer_lapso_final')
        fecha_ultimo_lapso_final = datos.get('fecha_ultimo_lapso_final')

        # ================================
        # UNIDADES
        # ================================
        agr_div = datos.get('agr_div')
        Div_FT = datos.get('Div_FT')
        br = datos.get('br')
        ut = datos.get('ut')

        # ================================
        # UBICACIÓN
        # ================================
        dpto = datos.get('dpto')
        mpio = datos.get('mpio')
        filtro = datos.get('filtro')

        # ================================
        # ENEMIGO / OPERACIONES
        # ================================
        enemigo = datos.get('enemigo')
        op_mayores = datos.get('op_mayores')
        apoyo_unidad = datos.get('apoyo_unidad')

        # ================================
        # AFECTACIONES
        # ================================
        afectaciones = datos.get('afectaciones')
        tipo_titulo = datos.get('tipo_titulo')
        tipo_afectaciones = datos.get('tipo_afectaciones')

        # ================================
        # DOCUMENTOS / SISTEMAS
        # ================================
        documento = datos.get('documento')
        spoa = datos.get('spoa')
        delco_cap = datos.get('delco_cap')

        # ================================
        # ESTRATEGIA
        # ================================
        estrategia = datos.get('estrategia')
        gaulas = datos.get('gaulas')
        coordinadas = datos.get('coordinadas')
        conjuntas = datos.get('conjuntas')

        # ================================
        # OPERACIÓN
        # ================================
        tipo_operacion = datos.get('tipo_operacion')
        cdte = datos.get('cdte')

        # ================================
        # DATOS RESULTADOS
        # ================================
        hechos = datos.get('hechos')
        datos_resultados = datos.get('datos_resultados')

        # ================================
        # ESTRUCTURAS
        # ================================
        acam_enemigo = datos.get('acam_enemigo')
        acam_estructura = datos.get('acam_estructura')
        ene_estructura = datos.get('ene_estructura')

        # ================================
        # SUBREGIÓN
        # ================================
        subregion = json.loads(datos.get('subregion', '[]'))

        # ================================
        # FILTROS
        # ================================
        filtros = (
            agr_div, Div_FT, br, ut,
            filtro, dpto, mpio,
            enemigo, op_mayores,
            apoyo_unidad, afectaciones,
            tipo_titulo, permiso, unidad,
            fullname, ruta, spoa,
            delco_cap, estrategia, gaulas,
            coordinadas, conjuntas,
            tipo_afectaciones, tipo_operacion,
            cdte, hechos, acam_enemigo,
            acam_estructura, ene_estructura,
            subregion
        )

        # ================================
        # GENERAR MAPA
        # ================================
        direccion = comparativo_comparativo_mapa(
            fecha_primer_lapso_inicial,
            fecha_ultimo_lapso_inicial,
            fecha_primer_lapso_final,
            fecha_ultimo_lapso_final,
            filtros,
            link,
            puerto
        )

        return {
            "direccion": direccion[0],
            "nombre": direccion[1]
        }

    except Exception as e:

        print("ERROR EN GENERACIÓN POWERPOINT:", str(e))

        return {
            "error": True,
            "mensaje": str(e)
        }