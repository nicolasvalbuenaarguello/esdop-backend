import json
from tipo_docker.b_f_mejor_unidad_obj2.models.funtions.pdf.boletin_coe import (
    comparativo_comparativo_mapa
)


def mejor_unidad_obj2(datos: dict, link: str, ruta: str, puerto: int) -> dict:
    """
    Genera el comparativo de mejor unidad OBJ2 y retorna la dirección del resultado.
    """

    # ---------- EXTRACCIÓN SEGURA DE DATOS ----------
    def get(key, default=None):
        return datos.get(key, default)

    fechas = (
        get('fecha_primer_lapso_inicial'),
        get('fecha_ultimo_lapso_inicial'),
        get('fecha_primer_lapso_final'),
        get('fecha_ultimo_lapso_final'),
    )

    subregion = json.loads(get('subregion', '[]'))

    filtros = (
        get('agr_div'),
        get('Div_FT'),
        get('br'),
        get('ut'),
        get('filtro'),
        get('dpto'),
        get('mpio'),
        get('enemigo'),
        get('op_mayores'),
        get('apoyo_unidad'),
        get('afectaciones'),
        get('tipo_titulo'),
        get('permiso'),
        get('unidad'),
        get('fullname'),
        ruta,
        get('spoa'),
        get('delco_cap'),
        get('estrategia'),
        get('gaulas'),
        get('coordinadas'),
        get('conjuntas'),
        get('tipo_afectaciones'),
        get('tipo_operacion'),
        get('cdte'),
        get('hechos'),
        get('acam_enemigo'),
        get('acam_estructura'),
        get('ene_estructura'),
        subregion,
        get('unidades_asc'),
        get('completa_und'),
    )

    # ---------- PROCESAMIENTO ----------
    resultado = comparativo_comparativo_mapa(
        fechas[0],
        fechas[1],
        fechas[2],
        fechas[3],
        filtros,
        link,
        puerto
    )

    # ---------- RESPUESTA ----------
    return {
        "direccion": resultado[0],
        "nombre": resultado[1]
    }
