
import sys
import traceback
from anyio import Path
from fastapi import HTTPException
from models.conexion_mysql import *

# from models.conexion import conexion_bd
from models.models import seleciones, close
from models.modelsUser import ModelUser
from models.entities.user import User
import os
from dotenv import load_dotenv

from models.conexion_pos import Databa_bases_posgrest
load_dotenv()
from datetime import timedelta, datetime
from jose import JWTError, jwt

import ephem
from datetime import datetime

db = Databa_bases.conexion_directa()

TOKEN = os.getenv('TOKEN')
import logging
from datetime import datetime

# Configurar logging
logging.basicConfig(
    filename='log.txt',
    level=logging.ERROR,
    format='%(asctime)s [%(levelname)s] %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def create_token(data: dict, time_expire: datetime):
    try:
        SECRETE_KEY = os.getenv('SECRETE')
        ALGORITHM = os.getenv('ALGORITHM')

        if not SECRETE_KEY or not ALGORITHM:
            raise ValueError("SECRETE o ALGORITHM no definidos en el entorno")

        data_copy = data.copy()
        expires = datetime.utcnow() + (time_expire if time_expire else timedelta(minutes=120))
        data_copy.update({"exp": expires})

        return jwt.encode(data_copy, key=SECRETE_KEY, algorithm=ALGORITHM)

    except Exception as e:
        print("⛔ Error al crear el token:")
        logging.error("⛔ Error generando token JWT:\n%s", traceback.format_exc())
        traceback.print_exc()
        raise HTTPException(status_code=500, detail="Error al generar token JWT")


class Ingreso():

    def logui(nombre, password):
        try:
            db = Databa_bases.conexion_directa()
            user = User(user_name=nombre, password=password)
            logged_user = ModelUser.loguin(db, user)

            if not logged_user:
                raise HTTPException(status_code=402, detail="Usuario Incorrecto")
            if not logged_user.disabled:
                raise HTTPException(status_code=402, detail="Contraseña Incorrecta")

            conexion_pos = Databa_bases_posgrest()
            luna = str(round(ephem.Moon(datetime.now()).phase))

            access_token_expire = timedelta(minutes=120)
            query = f"SELECT * FROM usuarios_dirop where id  = {logged_user.id}"
            datos = seleciones(query)

            for dato in datos:
                permiso = dato[6]
                unidad = dato[7]
                roll = dato[5]
                access_token_jwt = create_token({"sub": logged_user.user_name, "code": permiso}, access_token_expire)

            if permiso == "EJC":
                query = "SELECT * FROM view_unidades_materializados"
                query_eventos = "SELECT * FROM view_eventos ORDER BY FECHA ASC"
                query_alertas = "SELECT * FROM alertas ORDER BY FECHA ASC"
                alertas = conexion_pos.comando_query(query_alertas)
            else:
                query = f"SELECT * FROM view_unidades_materializados where {permiso} = '{unidad}'"
                query_eventos = f"SELECT * FROM view_eventos where {permiso} = '{unidad}' ORDER BY FECHA ASC"
                alertas = "---"

            if roll == "AMD":
                usuarios = seleciones("SELECT * FROM usuarios_dirop")
                coordinadores = conexion_pos.comando_query("SELECT * FROM coordinadores ORDER BY id ASC")
            elif roll == "MOVIMIENTOS":
                usuarios = "---"
                coordinadores = conexion_pos.comando_query("SELECT * FROM coordinadores ORDER BY id ASC")
            else:
                usuarios = coordinadores = "---"

            listado_personal = conexion_pos.comando_query("select * from personal ORDER BY valor_grado ASC")
            listado_inventarios = conexion_pos.comando_query("select * from inventarios_unidad")
            unidades = conexion_pos.comando_query(query)
            eventos = conexion_pos.comando_query(query_eventos)
            query_f = conexion_pos.comando_query("SELECT DISTINCT enemigo FROM view_enemigo_materializados ORDER BY enemigo ASC")
            acam_enemigo = conexion_pos.comando_query("SELECT DISTINCT acam_enemigo FROM view_hechos_materializados ORDER BY acam_enemigo ASC")
            acam_estructura = conexion_pos.comando_query("SELECT DISTINCT acam_estructura FROM view_hechos_materializados ORDER BY acam_estructura ASC")
            ene_estructura = conexion_pos.comando_query("SELECT DISTINCT ene_estructura FROM view_hechos_materializados ORDER BY ene_estructura ASC")
            query_g = conexion_pos.comando_query("SELECT DISTINCT hop_operacion FROM view_hop_operacion_materializados ORDER BY hop_operacion ASC")
            query_h = conexion_pos.comando_query("SELECT DISTINCT estrategia_afecta FROM view_hechos_materializados ORDER BY estrategia_afecta ASC")
            query_i = conexion_pos.comando_query("SELECT DISTINCT tipo_operacion FROM view_hechos_materializados ORDER BY tipo_operacion ASC")
            query_j = conexion_pos.comando_query("SELECT DISTINCT hecho FROM view_hechos_materializados ORDER BY hecho ASC")
            fultimo_registro = conexion_pos.comando_query("SELECT * FROM actulizacion_data ORDER BY id DESC LIMIT 1")



            for dato in datos:
                msm = {
                    "access_token": access_token_jwt,
                    "token_type": "bearer",
                    'nombre': dato[1],
                    'usuario': dato[2],
                    'contrasenia': dato[3],
                    'foto': dato[4],
                    'roll': dato[5],
                    'permiso': dato[6],
                    'unidad': dato[7],
                    'per_view': dato[8],
                    'per_select': dato[9],
                    'per_insert': dato[10],
                    'per_update': dato[11],
                    'per_delete': dato[12],
                    'resultados': dato[13],
                    'per_eventos': dato[14],
                    'per_usuarios': dato[15],
                    'chat': dato[16],
                    'conf_narcotrafico': dato[17],
                    'operaciones': dato[18],
                    'personal': dato[19],
                    'orden': dato[20],
                    'afectaciones_fuera_combate': dato[21],
                    'boletin_coe': dato[22],
                    'boletin_cuadros_coe': dato[23],
                    'boletin_res_div': dato[24],
                    'cartilla_presidencial_larga': dato[25],
                    'cartilla_presidencial_corta': dato[26],
                    'boletin_diseo': dato[27],
                    'boletin_diseo_semanal': dato[28],
                    'comando_general': dato[29],
                    'Estadistica_resultados': dato[30],
                    'com_resultados_reducido': dato[31],
                    'narcotrafico': dato[32],
                    'artemisa': dato[33],
                    'artemisa_comparativo': dato[34],
                    'contrabando': dato[35],
                    'contrabando_comparativo': dato[36],
                    'mineria': dato[37],
                    'mineria_comparativo': dato[38],
                    'comparativo_enemigo': dato[39],
                    'comparativo_mapa': dato[40],
                    'comparativo_resultados': dato[41],
                    'afectacion_a_la_amenaza': dato[42],
                    'afectacion_comparativa_p_t': dato[43],
                    'lis_afectaciones': dato[44],
                    'afectaciones_mapa': dato[45],
                    'afectaciones_cuadros': dato[46],
                    'regiones': dato[47],
                    'resaltantes': dato[48],
                    'reslatantes_divisiones': dato[49],
                    'bullets': dato[50],
                    'boltin_dirop': dato[51],
                    'estadistica_eventos': dato[52],
                    'informe_eventos': dato[53],
                    'dependencia': dato[54],
                    'datos': dato[55],
                    'cambio_contrasenia': dato[56],
                    'alerta': dato[57],
                    'movimientos': dato[58],
                    'inventarios': dato[59],
                    'boletin_mapa_comparativa': dato[60],
                    'narcotrafico_metas_per': dato[62],
                    'docna_semanal_per': dato[63],
                    'resaltantes_boletin_per': dato[64],
                    'excel_ut_per': dato[65],
                    'excel_amenaza_per': dato[66],
                    'resaltantes_mapa_per': dato[67],
                    "resultados_excel_tipo_operaciones_per": dato[68],
                    "archivo_spoa_per": dato[69],
                    "mapa_division_dinamico_per": dato[70],
                    "aetcr_permiso": dato[71],
                    "ingreso_aetcr_permiso": dato[72],
                    "listado_aetcr_permiso": dato[73],
                    "alerta_aetcr_permiso": dato[74],
                    "plazos_permiso": dato[75],
                    "asignacion_plazo": dato[76],
                    "reasignacion_plazo": dato[77],
                    "validacion_plaz": dato[78],
                    "creacion_plazo": dato[79],
                    "cumplimiento_plazo": dato[80],
                    "medallas_permiso": dato[81],
                    "excel_anios_permiso": dato[82],
                    "seguimineto_plazos_respueta_per": dato[83],
                    "insitop_per_per": dato[84],
                    "cargue_insitop_per": dato[85],
                    "estadistica_insitop_per": dato[86],
                    "dicte_per": dato[87],
                    "dicte_pasos_fronterizos_per": dato[88],
                    "com_div_mapa_per": dato[89],
                    "comp_div_mapa_bal_per": dato[90],
                    "eventos_relevantes_per": dato[91],
                    "archivo_plano_excel_per": dato[92],
                    "res_lineas_estrategicas_per": dato[93],
                    "configuracion_especial_res_per": dato[94],
                    "res_linea_obj_4_per": dato[95],
                    "linea_estrategica_narcotrafico_per": dato[96],
                    "ayuda_comparativa_consejos_per": dato[97],
                    "registro_Q5_per": dato[98],
                    "obj_1_per": dato[99],
                    "obj_2_per": dato[100],
                    "obj_3_per": dato[101],
                    "obj_4_per": dato[102],
                    "porcentaje_luna": f"Luminosidad: {luna} %",
                    "unidades": unidades,
                    "enemigo": query_f,
                    "op_mayor": query_g,
                    "eventos": eventos,
                    "alertas": alertas,
                    "usuarios": usuarios,
                    "estrategia": query_h,
                    "tipo_operacion": query_i,
                    "coordinadores": coordinadores,
                    "listado_personal": listado_personal,
                    "listado_inventarios": listado_inventarios,
                    "hechos": query_j,
                    "acam_enemigo": acam_enemigo,
                    "acam_estructura": acam_estructura,
                    "ene_estructura": ene_estructura,
                    'fultimo_registro':fultimo_registro
                }

            close()
            return msm

        except HTTPException:
            raise
        except Exception as e:
            print("⛔ Error interno en logui():")
            traceback.print_exc()
            raise HTTPException(status_code=500, detail="Error interno al procesar el ingreso")