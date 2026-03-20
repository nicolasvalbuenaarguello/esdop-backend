from __init__ import *
from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from tipo_docker.k_c_boletin_mapa_div_comparativo_consejos.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_c_boletin_estadistica.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_e_cartilla_ejc_cdt.models.descarga_resultados.boltin_coe import *
from tipo_docker.k_c_boletin_mapa_div_comparativo.models.descarga_resultados.boltin_coe import *
from tipo_docker.q_c_afectaciones_cuadro.models.descarga_resultados.boltin_coe import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico.models.descarga_resultados.boltin_coe import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_metas.models.descarga_resultados.boltin_coe import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_semanal.models.descarga_resultados.boltin_coe import *
from tipo_docker.c_c_boletin_estadistica_narcotrafico_power_point.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_m_resultados_excel_resultados.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_k_resultados_excel_plano.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_i_resultados_excel.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_j_resultados_excel_amenaza.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_j_resultados_excel_operaciones.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_l_resultados_excel_anios.models.descarga_resultados.boltin_coe import *
#DISEO
from tipo_docker.y_g_resultados_resaltantes_comparativo_div.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_f_resultados_diseo_diario.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_d_cartilla_ejc_cdt_r.models.descarga_resultados.boltin_coe import *
from tipo_docker.a_c_boletin_estadistica_resultados.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_c_boletin_comparativo_r.models.descarga_resultados.boltin_coe import *
from   tipo_docker.d_c_artemisa.models.descarga_resultados.boltin_coe import *
from tipo_docker.e_c_boletin_estadistica_artemisa_comp.models.descarga_resultados.boltin_coe import *
from tipo_docker.f_c_boletin_estadistica_contrabando.models.descarga_resultados.boltin_coe import *
from tipo_docker.g_c_boletin_estadistica_contrabando_comp.models.descarga_resultados.boltin_coe import *
from tipo_docker.h_c_boletin_estadistica_mineria.models.descarga_resultados.boltin_coe import *
from tipo_docker.i_c_boletin_estadistica_mineria_comparativo.models.descarga_resultados.boltin_coe import *
from tipo_docker.j_c_boletin_comparativo_enemigo.models.descarga_resultados.boltin_coe import *
from tipo_docker.k_c_boletin_comparativo_mapa.models.descarga_resultados.boltin_coe import *
from tipo_docker.l_c_boletin_comparativo.models.descarga_resultados.boltin_coe import *
from tipo_docker.z_b_ayudas_un_solo_resultados.models.descarga_resultados.boltin_coe import *
from tipo_docker.n_c_cuadro_compartivo_afectaciones.models.descarga_resultados.boltin_coe import *
from tipo_docker.o_c_listado_afectaciones.models.descarga_resultados.boletin_coe import *
from tipo_docker.p_c_afectaciones_mapa.models.descarga_resultados.boltin_coe import *
from tipo_docker.r_c_regiones_colombia.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_f_resultados_resaltantes_comparativo.models.descarga_resultados.boltin_coe import *
from tipo_docker.k_c_boletin_mapa_comparativo.models.descarga_resultados.boltin_coe import *
from tipo_docker.z_a_mapa_dinamico.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_resultados_lineas_estrategicas.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_resultados_lineas_estrategica_4.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_resultados_lineas_estrategicas_sin_comparar.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_resultados_lineas_estrategicas_paya.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_n_resultados_lineas_obj1_plan.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_o_resultados_lineas_obj2_plan.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_p_resultados_lineas_obj3_plan.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_resultados_lineas_estrategica_4_power.models.descarga_resultados.boltin_coe import *
from tipo_docker.y_r_resultados_dash.models.descarga_resultados.boltin_coe import *
from tipo_docker.a_a_boletin_estadistica_power_point.models.descarga_resultados.boltin_coe import *
from tipo_docker.s_c_resultados_resaltantes.models.descarga_resultados.boltin_coe import *
from tipo_docker.t_c_resultados_resaltantes_div.models.descarga_resultados.boltin_coe import *
from tipo_docker.s_c_resultados_mapa.models.descarga_resultados.boltin_coe import *
from tipo_docker.k_c_boletin_mapa_div_balance.models.descarga_resultados.boltin_coe import *
from tipo_docker.b_f_mejor_unidad_obj2.models.descarga_resultados.boltin_coe import *
from tipo_docker.a_p_res_mineria_nuew.models.descarga_resultados.boltin_coe import *
from tipo_docker.a_p_res_mineria_nuew.models.model.database import get_db
from tipo_docker.b_f_power_point_obj2.models.descarga_resultados.boltin_coe import *
from sqlalchemy.orm import Session
from sqlalchemy import text
from tipo_docker.b_f_resultados_lineas_estrategicas_paya_power.models.descarga_resultados.boltin_coe import *
from tipo_docker.k_c_boletin_comparativo_power_point.models.descarga_resultados.boltin_coe import *


from auth import verificar_token
import os
from dotenv import load_dotenv

# Carga variables del .env
load_dotenv()

# Inicializa la app FastAPI
app = FastAPI(
    title="Centro Estadístico",
    version="2.0.0"
)

# ✅ Habilita CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Cambia a ["https://tu-dominio.com"] en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/a_w_boletin_mapa_div_comparativo")# Concejos de seguiridad
async def descarga(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = a_w_boletin_mapa_div_comparativo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/a_a_boletin_estadistica_token_replicas")#resultados cuadros
async def a_a_boletin_estadistica_token(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        #resultados cuadros
        resultado = a_a_boletin_estadistica_token_replicas(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
    
@app.post("/a_b_cartilla_ejc_cdt_token_replicas")#a_b_cartilla_ejc_cdt_token_replicas
async def a_b_cartilla_ejc_cdt_token(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()#a_b_cartilla_ejc_cdt_token_replicas
        resultado = a_b_cartilla_ejc_cdt_token_replicas(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/cartilla_ejc_cdt_r")#a_b_cartilla_ejc_cdt_token_replicas
async def a_b_cartilla_ejc_cdt_token(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()#a_b_cartilla_ejc_cdt_token_replicas
        resultado = boletin_coe_cartilla_reducida(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/a_w_boletin_mapa_div_comparativo_div")#comparativo mapas ayudas
async def a_w_boletin_mapa_div_comparativo_div_empoin(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = a_w_boletin_mapa_div_comparativo_div(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
       
@app.post("/b_a_afectaciones_cuadro_token")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = b_a_afectaciones_cuadro_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
#CARTILLAS DE DISEO
@app.post("/boletin_coe_semanal_diseo")# cartilla semanal DISEO
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_semanal_diseo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
#CARTILLAS DE DISEO
@app.post("/boletin_coe_semanal_diseo")# cartilla semanal DISEO
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_semanal_diseo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_coe_diario_diseo")# cartilla diaria DISEO
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_diario_diseo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_estadistica_resultados")# boletin_estadistica_resultados
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_consejos(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

#docna
@app.post("/a_i_boletin_estadistica_narcotrafico_token")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = a_i_boletin_estadistica_narcotrafico_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
    
@app.post("/c_c_boletin_estadistica_narcotrafico_metas")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = c_c_boletin_estadistica_narcotrafico_metas(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
         
@app.post("/c_c_boletin_estadistica_narcotrafico_semanal")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = c_c_boletin_estadistica_narcotrafico_semanal(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")


@app.post("/configuracion_paya_narcotrafico")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
    ):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = res_linea_estrategica_narcotrafico_power_point(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")


@app.post("/narcotrafico_metas_power")
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
    ):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = c_c_boletin_estadistica_narcotrafico_power_point(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

#archivo plano
@app.post("/archivo_plano_excel")#archivo_plano_excel
async def archivo_plano_excel(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = archivo_plano_excel_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/archivo_spoas_error")#archivo_spoas_error
async def archivo_spoas_error(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = archivo_spoas_error_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/excel_ut")#excel_ut
async def excel_ut(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = excel_ut_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/excel_amenaza")#excel_amenaza
async def excel_amenaza(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = excel_amenaza_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/resultados_excel_tipo_operaciones")#resultados_excel_tipo_operaciones
async def resultados_excel_tipo_operaciones(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = resultados_excel_tipo_operaciones_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/excel_anios_permiso")#excel_anios_permiso
async def excel_anios_permiso(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = excel_anios_permiso_excel(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")


@app.post("/boletin_comparativo_r")# boletin_estadistica_resultados
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_reducido(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/artemisa")# artemisa
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_artemisa(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
    
@app.post("/boletin_estadistica_artemisa_comp")# boletin_estadistica_artemisa_comp
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_artemisa_comparativo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_estadistica_contrabando")# boletin_estadistica_contrabando
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_comtrabando(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
    
@app.post("/boletin_estadistica_contrabando_comp")# boletin_estadistica_contrabando_comp
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = contrabando_comparativo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
@app.post("/boletin_estadistica_mineria")# boletin_estadistica_mineria
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_mineria(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
 
@app.post("/boletin_estadistica_mineria_comparativo")# boletin_estadistica_mineria_comparativo
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_comparativo_mineria(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")
  
@app.post("/boletin_comparativo_enemigo")# boletin_comparativo_enemigo
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_coe_comparativo_amenaza(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_comparativo_mapa")# boletin_comparativo_mapa
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_comparativo_mapa(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_comparativo")# boletin_comparativo
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_comparativo(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/resultados_una_ayuda")# resultados_una_ayuda
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = resultados_una_ayuda(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/cuadro_compartivo_afectaciones")# cuadro_compartivo_afectaciones
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = cuadro_compartivo_afectaciones_v(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/listado_afectaciones")# listado_afectaciones
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = listado_afectaciones_boletin(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/afectaciones_mapa")# afectaciones_mapa
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = afectaciones_mapa(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/regiones_colombia")# regiones_colombia
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = regiones_colombia_v(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/resultados_resaltantes_comparativo")# resultados_resaltantes_comparativo
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = resultados_resaltantes_comparativo_v(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/boletin_mapa_comparativa")# boletin_mapa_comparativa
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_mapa_comparativa(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/mapa_dinamico_divisiones")# mapa_dinamico_divisiones
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = mapa_dinamico_divisiones(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/configuracion_especial_res_pdf")# cResultados obj dos rejoj, 
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
    ):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = configuracion_especial_res(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/configuracion_especial_res")# cResultados obj dos power_poin reloj, 
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
    ):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = configuracion_especial_res_power_poin(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/resultados_comparativos_ejc_power_point")# cResultados obj dos power_poin reloj, 
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
    ):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = compartivo_power_point(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")


@app.post("/id_mejor_unidadboj2")# mejores unidades de acuerdo al obj2, 
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = mejor_unidad_obj2(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/res_linea_obj_4")# res_linea_obj_4
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")
        print("---")
        form_data = await datos.form()
        resultado = ayuda_comparativa_obj_4(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/configuracion_especial_res_sin_Comparar")# configuracion_especial_res_sin_Comparar
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = configuracion_especial_res_sin_Comparar(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/res_linea_estrategica_narcotrafico")# res_linea_estrategica_narcotrafico
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = res_linea_estrategica_narcotrafico(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/ayuda_comparativa_obj_1")# ayuda_comparativa_obj_1
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = ayuda_comparativa_obj_1(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/ayuda_comparativa_obj_2")# ayuda_comparativa_obj_2
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = ayuda_comparativa_obj_2(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/ayuda_comparativa_obj_3")# ayuda_comparativa_obj_3
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = ayuda_comparativa_obj_3(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/ayuda_comparativa_obj_4")# ayuda_comparativa_obj_4
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = ayuda_comparativa_obj_4(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/url_ver_inf_resultados_dash")# url_ver_inf_resultados_dash
async def b_a_afectaciones_cuadro(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = url_ver_inf_resultados_dash(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/resultados_c_power_point")#resultados en power point
async def descarga(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = boletin_estadistica_resultados(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/b_c_resultados_resaltantes_token")#resaltantes
async def b_c_resultados_resaltantes(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = b_c_resultados_resaltantes_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/b_d_resultados_resaltantes_div_token")#resultados resaltantes divisiones
async def b_d_resultados_resaltantes_div(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = b_d_resultados_resaltantes_div_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/b_e_resultados_mapa_token")
async def b_e_resultados_mapa(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = b_e_resultados_mapa_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/b_f_boletin_mapa_div_balance")
async def b_f_boletin_mapa_div_balance(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = b_f_boletin_mapa_div_balance_token(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

#mineria ilegal nueva
@app.post("/api/filtrar_pdf")#pdf mapa mineria nueva pdf
async def b_f_boletin_mapa_div_balance(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = pdf_mapa_mineria(
            form_data,
            os.getenv("DIRECION_3_B"),
            os.getenv("DIRECION"),
            puerto
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

@app.post("/api/filtrar_da_mapa")#pdf mapa mineria nueva
async def b_f_boletin_mapa_div_balance(
    datos: Request,
    token_data: dict = Depends(verificar_token)
):
    try:
        user = token_data["user_name"]
        puerto = os.getenv("PUERTO")
        print(f"Puerto recibido: {puerto}")

        form_data = await datos.form()
        resultado = mapa_resultados(
            form_data,
        )
        return resultado

    except Exception as e:
        print(f"❌ Error procesando la solicitud: {e}")
        raise HTTPException(status_code=500, detail="Error interno al generar el boletín")

#mineria ilegal nueva
@app.get("/api/resultados_parametro_con_variables")#apis de mineria 
def obtener_resultados_unicos(db: Session = Depends(get_db)):
    """
    Retorna todos los valores únicos de res_clase desde view_resultados_materializados.
    """
    query = text("""
        SELECT DISTINCT res_clase
        FROM view_resultados_materializados
        WHERE res_clase IS NOT NULL
        ORDER BY res_clase;
    """)

    result = db.execute(query).fetchall()

    # Convertir a lista simple de strings
    clases = [row.res_clase for row in result]

    return {"total": len(clases), "res_clases": clases}

@app.post("/api/guardar")#apis de mineria 
def guardar_item(
    material: str = Form(...),
    valor: str = Form(...),
    columna: int = Form(...),
    db: Session = Depends(get_db)
):
    """
    Recibe datos de Angular y los guarda en la tabla correspondiente.
    Si columna = 1 → valor_material
    Si columna = 2 → valor_dolar
    Luego retorna las listas actualizadas de ambas tablas.
    """

    try:
        if columna == 1:
            # 🟩 Guardar en valor_material
            query = text("""
                INSERT INTO valor_material (variable, valor_cop)
                VALUES (:variable, :valor_cop)
            """)
            db.execute(query, {"variable": material, "valor_cop": float(valor)})

        elif columna == 2:
            # 🟦 Guardar en valor_dolar
            fecha = None
            try:
                fecha = datetime.strptime(valor, "%Y-%m-%d").date()
            except:
                raise ValueError("El formato de fecha debe ser YYYY-MM-DD")

            query = text("""
                INSERT INTO valor_dolar (valor_usd, fecha_cotizacion)
                VALUES (:valor_usd, :fecha_cotizacion)
            """)
            db.execute(query, {"valor_usd": float(material), "fecha_cotizacion": fecha})

        else:
            raise ValueError("Columna no válida. Debe ser 1 o 2.")

        db.commit()

        # 🔄 Obtener las dos listas actualizadas
        lista_materiales = db.execute(text("""
            SELECT id, variable AS material, valor_cop AS valor, fecha_registro
            FROM valor_material
            ORDER BY fecha_registro DESC
        """)).fetchall()

        lista_dolares = db.execute(text("""
            SELECT id, valor_usd AS material, fecha_cotizacion AS fecha, fecha_registro
            FROM valor_dolar
            ORDER BY fecha_cotizacion DESC
        """)).fetchall()

        # Convertir a listas de diccionarios
        materiales = [dict(row._mapping) for row in lista_materiales]
        dolares = [dict(row._mapping) for row in lista_dolares]

        return {
            "mensaje": "✅ Registro guardado correctamente",
            "lista_material": materiales,
            "lista_dolar": dolares
        }

    except Exception as e:
        db.rollback()
        return {"error": f"❌ Error al guardar: {str(e)}"}

@app.get("/api/valores")#apis de mineria 
def obtener_valores(db: Session = Depends(get_db)):
    """
    Retorna todos los registros de las tablas valor_material y valor_dolar.
    """
    # --- Tabla valor_material ---
    query_material = text("""
        SELECT 
            id, 
            variable AS material, 
            valor_cop AS valor, 
            fecha_registro
        FROM valor_material
        ORDER BY fecha_registro DESC;
    """)
    materiales = [dict(row._mapping) for row in db.execute(query_material).fetchall()]

    # --- Tabla valor_dolar ---
    query_dolar = text("""
        SELECT 
            id, 
            valor_usd AS material, 
            fecha_cotizacion AS fecha, 
            fecha_registro
        FROM valor_dolar
        ORDER BY fecha_registro DESC;
    """)
    dolares = [dict(row._mapping) for row in db.execute(query_dolar).fetchall()]

    return {
        "total_material": len(materiales),
        "total_dolar": len(dolares),
        "lista_material": materiales,
        "lista_dolar": dolares
    }

@app.post("/api/eliminar_valor")#apis de mineria 
def eliminar_valor(
    columna: int = Form(...),
    material: str = Form(""),
    valor: str = Form(...),
    db: Session = Depends(get_db)
):
    try:
        valor_float = float(valor)
    except ValueError:
        raise HTTPException(status_code=400, detail=f"El valor '{valor}' no es numérico")

    if columna == 1:
        query = text("""
            DELETE FROM valor_material
            WHERE variable = :material AND valor_cop = :valor
        """)
        params = {"material": material, "valor": valor_float}
    elif columna == 2:
        query = text("""
            DELETE FROM valor_dolar
            WHERE valor_usd = :valor
        """)
        params = {"valor": valor_float}
    else:
        raise HTTPException(status_code=400, detail="Columna no válida")

    result = db.execute(query, params)
    db.commit()

    if result.rowcount == 0:
        raise HTTPException(status_code=404, detail="Registro no encontrado")

    return {"mensaje": "✅ Registro eliminado correctamente", "columna": columna}











