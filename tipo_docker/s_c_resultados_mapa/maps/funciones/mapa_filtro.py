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

    # Configurar figura
    plt.rcParams["figure.figsize"] = (10, 10)

    # Asegurar que solo se tomen las primeras 18 columnas si vienen más
    eventos = [fila[:18] for fila in eventos]

    columnas = [
        'hecho', 'fecha_hecho', 'agr_div', 'division', 'brigada', 'unidad',
        'dpto', 'mpio', 'enemigo', 'estrategia_afecta', 'hop_accion_davaa',
        'hop_apoyo_blica', 'hop_apoyo_conat', 'hop_hecho_pos', 'cantidad',
        'hop_operacion', 'latitud', 'longitud'
    ]
    df = pd.DataFrame(eventos, columns=columnas)

    # Crear GeoDataFrame de eventos
    gdf_eventos = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.longitud, df.latitud), crs="EPSG:4326")

    # Rutas de shapefiles
    ruta = rutas_mapas(filtro)
    municipios = gpd.read_file(ruta[2]).to_crs("EPSG:4326")
    departamentos = gpd.read_file(ruta[3]).to_crs("EPSG:4326")

    # Unión espacial eventos → municipios
    gdf_eventos = gdf_eventos.set_geometry("geometry")
    eventos_mpio = sjoin(gdf_eventos, municipios[['NOMBRE_ENT', 'geometry']], how="left", predicate="intersects")
    eventos_mpio = eventos_mpio.rename(columns={"NOMBRE_ENT": "municipio"})

    # Contar eventos por municipio
    conteo = eventos_mpio.groupby("municipio").size().reset_index(name="conteo_eventos")

    # Agregar cantidad de eventos a cada punto
    eventos_coloreados = eventos_mpio.merge(conteo, on="municipio", how="left")

    # --- Pintar mapa ---
    ax = departamentos.boundary.plot(linewidth=1, color="black")  # Mantener departamentos
    municipios.boundary.plot(ax=ax, linewidth=0.3, color="gray", alpha=0.5)

    # Puntos coloreados según conteo (más eventos = color más fuerte)
    eventos_coloreados.plot(
        ax=ax,
        column="conteo_eventos",
        cmap="YlOrRd",
        scheme="quantiles",
        k=6,
        markersize=eventos_coloreados["conteo_eventos"].clip(upper=100) / 2 + 10,
        alpha=0.85,
        legend=False
    )

    ax.axis("off")

    # Guardar imagen
    salida = f'{filtro[15]}static/img/img_mapas/mapa_resaltante.png'
    plt.savefig(salida, transparent=True, dpi=100)
    plt.close()


def mapa_filtrado(dato, filtro):
    plt.rcParams["figure.figsize"] = (10, 10)

    # Sanear FUTOM → FUTCO
    dato_nuevo = [tuple(list(x[:2]) + ['FUTCO'] + list(x[3:18])) if x[2] == "FUTOM" else x[:18] for x in dato]

    # Crear GeoDataFrame con columnas válidas
    di = gpd.GeoDataFrame(dato_nuevo)
    di.rename(columns={
        0: 'hecho', 1: "fecha_hecho", 2: "agr_div", 3: "division", 4: "brigada",
        5: "unidad", 6: "dpto", 7: "mpio", 8: "enemigo", 9: "estrategia_afecta",
        10: "hop_accion_davaa", 11: "hop_apoyo_blica", 12: "hop_apoyo_conat",
        13: "hop_hecho_pos", 14: "cantidad", 15: "hop_operacion",
        16: "latitud", 17: "longitud"
    }, inplace=True)

    point = gpd.GeoDataFrame(di, geometry=gpd.points_from_xy(di.longitud, di.latitud))
    point.set_crs("EPSG:4326", inplace=True)

    # Cargar capas base
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0]).to_crs(point.crs)
    municipios = gpd.read_file(ruta[2]).to_crs(point.crs)
    departamentos = gpd.read_file(ruta[3]).to_crs(point.crs)

    # Recortar a divisiones si aplica
    municipios_clip = municipios.clip(divisiones)

    # Agrupar eventos
    agrupado_div = point.groupby("agr_div")["agr_div"].agg(["count"])
    agrupado_mpio = point.groupby("mpio")["mpio"].agg(["count"])

    divisiones_eventos = divisiones.merge(agrupado_div, left_on="DIV", right_on="agr_div", how="left")
    municipios_eventos = municipios_clip.merge(agrupado_mpio, left_on="NOMBRE_ENT", right_on="mpio", how="left")

    # Join espacial
    join_puntos_mpios = sjoin(point, municipios_eventos, how="inner", predicate="intersects")

    # Graficar
    base = divisiones.boundary.plot(linewidth=1.5, color="black")
    municipios_clip.boundary.plot(ax=base, linewidth=0.3, color="gray", alpha=0.5)
    join_puntos_mpios.plot(ax=base, column="count", cmap="YlOrRd", markersize=30, alpha=0.5, legend=False)
    point.plot(ax=base, color="red", markersize=10, alpha=0.5)

    base.axis('off')

    # Guardar mapa
    unidad = "FUTCO" if filtro[0] == "FUTOM" else filtro[0]
    ruta_final = f'{filtro[15]}static/img/img_mapas/mapa_resaltante.png'
    plt.savefig(ruta_final, format="png", transparent=True, dpi=100)

#funcion para filtrar mapas

def mapa_filtrado_dep(dato, filtro):
    import warnings
    warnings.filterwarnings("ignore", category=UserWarning)

    plt.rcParams["figure.figsize"] = (10, 10)

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
    foto = f"{filtro[15]}static/img/img_mapas/mapa_resaltante.png"
    plt.savefig(foto, format="png", transparent=True, dpi=100)



