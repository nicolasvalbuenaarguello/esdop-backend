import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from   geopandas.tools import sjoin
import fiona
import os
import contextily as cx
import xyzservices.providers as xyz
import shapely



#funcion para la creacin de rutas

def rutas_mapas(filtro):
    unidades = {
        "DIV01": "DIV1", "DIV02": "DIV2", "DIV03": "DIV3",
        "DIV04": "DIV4", "DIV05": "DIV5", "DIV06": "DIV6",
        "DIV07": "DIV7", "DIV08": "DIV8", "FUTCO": "FUTCO", "FUTOM": "FUTCO"
    }

    ruta = filtro[15]
    unidad_codigo = filtro[0]
    unidad = unidades.get(unidad_codigo, "")
    ruta_unidad = unidad_codigo if unidad_codigo != "FUTOM" else "FUTCO"

    divi = f'{ruta}shappes/{ruta_unidad}/{unidad}.shp' if unidad else f'{ruta}shappes/div_2025/DIV_RES_EJC_2025.shp'
    municipios_div = f'{ruta}shappes/divisiones/div_mun.shp'
    municipios = f'{ruta}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'

    if filtro[5] and filtro[5] != "---":
        departamentos = f'{ruta}shappes/DEPARTA/Export_Output_7.shp' if "," in filtro[5] else f'{ruta}shappes/departamentos/{filtro[5]}.shp'
    else:
        departamentos = f'{ruta}shappes/DEPARTA/Export_Output_7.shp'

    return [divi, municipios_div, municipios, departamentos]

def mapa_general(eventos, filtro):
    import matplotlib.pyplot as plt
    import geopandas as gpd
    import pandas as pd
    from geopandas.tools import sjoin

    ffig, ax = plt.subplots(figsize=(10, 12), facecolor='black')

    # Asegurar que solo se tomen las primeras 18 columnas
    eventos = [fila[:18] for fila in eventos]
    columnas = [
        'hecho', 'fecha_hecho', 'agr_div', 'division', 'brigada', 'unidad',
        'dpto', 'mpio', 'enemigo', 'estrategia_afecta', 'hop_accion_davaa',
        'hop_apoyo_blica', 'hop_apoyo_conat', 'hop_hecho_pos', 'cantidad',
        'hop_operacion', 'latitud', 'longitud'
    ]
    df = pd.DataFrame(eventos, columns=columnas)

    # Crear GeoDataFrame
    gdf_eventos = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitud, df.latitud), crs="EPSG:4326")

    # Cargar shapefiles
    ruta = rutas_mapas(filtro)
    municipios = gpd.read_file(ruta[2]).to_crs("EPSG:4326")
    departamentos = gpd.read_file(ruta[3]).to_crs("EPSG:4326")

    # Unión espacial para asignar municipio
    eventos_mpio = sjoin(gdf_eventos, municipios[['NOMBRE_ENT', 'geometry']], how="left", predicate="intersects")
    eventos_mpio = eventos_mpio.rename(columns={"NOMBRE_ENT": "municipio"})

    # Conteo de eventos por municipio
    conteo = eventos_mpio.groupby("municipio").size().reset_index(name="conteo_eventos")

    # Unir conteo a los eventos
    eventos_coloreados = eventos_mpio.merge(conteo, on="municipio", how="left")

    # --- Plot ---
    ax = departamentos.boundary.plot(linewidth=1, color="black")
    municipios.boundary.plot(ax=ax, linewidth=0.3, color="gray", alpha=0.5)

    eventos_coloreados.plot(
        ax=ax,
        column="conteo_eventos",
        cmap="YlOrRd",
        scheme="quantiles",
        k=6,
        markersize=30,
        alpha=0.85,
        legend=False
    )

    ax.axis("off")

    # Guardar
    salida = f'{filtro[15]}static/img/img_mapas/mapa.png'
    plt.savefig(salida, transparent=True, dpi=120, bbox_inches='tight')
    plt.close()

def mapa_filtrado(dato, filtro):
    import matplotlib.pyplot as plt
    import geopandas as gpd
    from geopandas.tools import sjoin
    from mapclassify import Quantiles
    import os

    fig, ax = plt.subplots(figsize=(10, 12), facecolor='black')
    ax.set_facecolor('black')

    # Corrección de nombre de unidad
    dato_nuevo = [
        tuple(list(x[:2]) + ['FUTCO'] + list(x[3:18])) if x[2] == "FUTOM" else x[:18]
        for x in dato
    ]

    columnas = [
        'hecho', 'fecha_hecho', 'agr_div', 'division', 'brigada', 'unidad',
        'dpto', 'mpio', 'enemigo', 'estrategia_afecta', 'hop_accion_davaa',
        'hop_apoyo_blica', 'hop_apoyo_conat', 'hop_hecho_pos', 'cantidad',
        'hop_operacion', 'latitud', 'longitud'
    ]

    di = gpd.GeoDataFrame(dato_nuevo, columns=columnas)
    di["latitud"] = di["latitud"].astype(float)
    di["longitud"] = di["longitud"].astype(float)
    di = di.set_geometry(gpd.points_from_xy(di.longitud, di.latitud), crs="EPSG:4326")

    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0]).to_crs(di.crs)
    municipios = gpd.read_file(ruta[2]).to_crs(di.crs)

    # Filtrar solo divisiones con eventos
    divisiones_eventos = divisiones.merge(
        di.groupby("agr_div").size().reset_index(name="count"),
        left_on="DIV", right_on="agr_div", how="left"
    )
    divisiones_eventos["count"] = divisiones_eventos["count"].fillna(0)
    divisiones_con_eventos = divisiones_eventos[divisiones_eventos["count"] > 0]
    if divisiones_con_eventos.empty:
        print("⚠️ No hay divisiones con eventos.")
        return

    # Recorte geográfico
    geometria_union = divisiones_con_eventos.unary_union
    municipios = municipios.clip(geometria_union)
    di = di.clip(geometria_union)

    # Agrupar eventos por municipio y unir con puntos
    agrupado_mpio = di.groupby("mpio").size().reset_index(name="count")
    di = di.merge(agrupado_mpio, on="mpio", how="left")
    di["count"] = di["count"].fillna(0).astype(int)

    # Pintar puntos con color según el `count` del municipio
    num_clases = max(4, min(9, di["count"].nunique()))
    try:
        di.plot(
            ax=ax,
            column="count",       # ← Color según cantidad de eventos por municipio
            cmap="Reds",          # ← Gradiente de color
            scheme="quantiles",   # ← Clasificación por percentiles
            classification_kwds={'k': num_clases},
            markersize=30,
            alpha=0.9,
            legend=False,         # ← IMPORTANTE: Sin leyenda
            edgecolor='black',
            linewidth=0,
            zorder=3
        )
    except Exception as e:
        print("🎨 Error al graficar con esquema:", e)
        di.plot(ax=ax, color="red", alpha=0.7, markersize=40)

    # Límites municipales y divisionales
    municipios.boundary.plot(ax=ax, color="lightgray", linewidth=0.4, alpha=0.5)
    divisiones_con_eventos.plot(
        ax=ax,
        edgecolor="black",
        facecolor="none",
        linewidth=1.5,
        linestyle="-",
        alpha=0.9
    )

    ax.axis("off")

    unidad = "FUTCO" if filtro[0] == "FUTOM" else filtro[0]
    ruta_final = f'{filtro[15]}static/img/img_mapas/{unidad}_heatmap.png'
    os.makedirs(os.path.dirname(ruta_final), exist_ok=True)
    plt.savefig(ruta_final, format="png", transparent=True, dpi=100, bbox_inches='tight')
    plt.close()


#funcion para filtrar mapas

def mapa_filtrado_dep(dato, filtro):
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)

    plt.rcParams["figure.figsize"] = (8, 10)

    # Convertir lista a GeoDataFrame
    di = gpd.GeoDataFrame(dato)
    di.rename(columns={
        0:'hecho', 1:"fecha_hecho", 2:"agr_div", 3:"division", 4:"brigada",
        5:"unidad", 6:"dpto", 7:"mpio", 8:"enemigo", 9:"estrategia_afecta",
        10:"hop_accion_davaa", 11:"hop_apoyo_blica", 12:"hop_apoyo_conat",
        13:"hop_hecho_pos", 14:"cantidad", 15:"hop_operacion", 16:"latitud", 17:"longitud"
    }, inplace=True)

    # Crear geometría de puntos
    point = gpd.GeoDataFrame(di, geometry=gpd.points_from_xy(di.longitud, di.latitud))

    # Cargar capas base
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])

    # Asegurar que CRS coincidan
    crs_ref = departamentos.crs
    if point.crs != crs_ref:
        point = point.set_crs("EPSG:4326") if point.crs is None else point
        point = point.to_crs(crs_ref)
    municipios = municipios.to_crs(crs_ref)
    divisiones = divisiones.to_crs(crs_ref)

    # Recortar
    municipios = municipios.clip(departamentos)
    point = point.clip(departamentos)

    # Agrupaciones
    agrup_dep = point.groupby("dpto")["dpto"].agg(["count"])
    point_dep = point.merge(agrup_dep, left_on="dpto", right_on="dpto")

    agrup_mpio = point.groupby("mpio")["mpio"].agg(["count"])
    point_mpio = municipios.merge(agrup_mpio, left_on="NOMBRE_ENT", right_on="mpio")

    # Join espacial
    join = sjoin(municipios, point_dep)
    join_1 = sjoin(departamentos, point_dep).boundary
    join_2 = sjoin(point, point_mpio)

    # Gráfica
    join = join.boundary
    axis = join_1.plot(color="black", alpha=0.5)
    axis = join.plot(ax=axis, linewidth=0.3, color="silver")

    axis = join_2.plot(ax=axis, color="black", alpha=0.1)
    axis = point.plot(ax=axis, cmap="YlOrRd", markersize=30, alpha=0.5)

    # Ajuste dinámico de clases
    k_real = min(30, agrup_mpio["count"].nunique())

    try:
        axis = join_2.plot(
            ax=axis,
            cmap="YlOrRd",
            scheme="QUANTILES",
            k=k_real,
            column="count",
            alpha=0.5,
            legend=False  # <== leyenda desactivada
        )
    except Exception as e:
        print(f"Advertencia al graficar join_2: {e}")
        axis = join_2.plot(ax=axis, color="orange", alpha=0.5)

    axis.axis('off')

    # Guardar imagen
    foto = f"{filtro[15]}static/img/img_mapas/{filtro[5]}.png"
    plt.savefig(foto, format="png", transparent=True, dpi=100)



