import sys
import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt
from geopandas.tools import sjoin
import os
import shapely


def rutas_mapas(filtro):
    ruta = filtro
    divi = f'{ruta}shappes/div_2024/1_Divisiones_Ejercito.shp'
    municipios_div = f'{ruta}shappes/divisiones/div_mun.shp'
    municipios = f'{ruta}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'
    departamentos = f'{ruta}shappes/DEPARTA/Export_Output_7.shp'
    return [divi, municipios_div, municipios, departamentos]


def mapa_hechos(datos, nombre, filtro):
    ruta = rutas_mapas(filtro)
    
    # === Cargar capas base ===
    divisiones = gpd.read_file(ruta[0])
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])

    # === Convertir a DataFrame si es lista ===
    if isinstance(datos, list):
        if len(datos) > 0:
            if isinstance(datos[0], dict):
                datos = pd.DataFrame(datos)
            else:
                datos = pd.DataFrame(datos)
        else:
            datos = pd.DataFrame()

    # === Validar si hay datos ===
    if datos is not None and not datos.empty:
        hechos = datos.copy()

        # Intentar identificar columnas de coordenadas
        if 16 in hechos.columns and 17 in hechos.columns:
            hechos.rename(columns={16: "latitud", 17: "longitud"}, inplace=True)
        elif {"latitud", "longitud"}.issubset(hechos.columns) is False:
            print("⚠️ No se encontraron columnas de coordenadas")
            departamentos["color"] = "#E0E0E0"
        else:
            pass

        # === Normalizar coordenadas ===
        def limpiar_coord(valor):
            if isinstance(valor, (list, tuple)):
                return valor[0]  # si viene como (x,) o (x,y)
            try:
                return float(valor)
            except (ValueError, TypeError):
                return None

        hechos["latitud"] = hechos["latitud"].apply(limpiar_coord)
        hechos["longitud"] = hechos["longitud"].apply(limpiar_coord)

        # Filtrar solo los que tienen coordenadas válidas
        hechos = hechos.dropna(subset=["latitud", "longitud"])

        if not hechos.empty:
            # Crear geometría
            hechos = gpd.GeoDataFrame(
                hechos,
                geometry=gpd.points_from_xy(hechos["longitud"], hechos["latitud"]),
                crs=departamentos.crs
            )

            # === 🔹 Unión espacial: puntos → departamentos ===
            join_result = gpd.sjoin(hechos, departamentos, how="inner", predicate="intersects")

            # Contar hechos por departamento
            conteo = join_result.groupby("DEPARTAMEN").size().reset_index(name="conteo")

            # Unir conteo a departamentos
            departamentos = departamentos.merge(conteo, on="DEPARTAMEN", how="left")
            departamentos["color"] = departamentos["conteo"].apply(
                lambda x: "darkgreen" if pd.notnull(x) else "#E0E0E0"
            )
        else:
            departamentos["color"] = "#E0E0E0"
    else:
        departamentos["color"] = "#E0E0E0"

    # === 🗺️ Graficar ===
    fig, axis = plt.subplots(figsize=(8, 10))
    departamentos.plot(ax=axis, color=departamentos["color"], edgecolor="black", linewidth=0.5)
    divisiones.boundary.plot(ax=axis, color="black", linewidth=1.2, alpha=0.8)
    municipios.boundary.plot(ax=axis, color="gray", linewidth=0.3, alpha=0.5)

    # === Puntos de hechos ===
    if 'hechos' in locals() and not hechos.empty:
        hechos.plot(ax=axis, marker='o', color="goldenrod", markersize=40, zorder=5)

    axis.axis("off")
    #axis.set_title(f"Mapa de hechos - {nombre}", fontsize=14, fontweight="bold")

    # === Guardar resultado ===
    imagen = f"{filtro}static/img/img_mapas/"
    os.makedirs(imagen, exist_ok=True)
    direccion = f"{imagen}{nombre}.png"
    plt.savefig(direccion, transparent=True, dpi=300, bbox_inches='tight')
    plt.close(fig)

    return direccion
