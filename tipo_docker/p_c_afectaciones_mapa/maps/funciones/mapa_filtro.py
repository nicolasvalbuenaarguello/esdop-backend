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

plt.rcParams["figure.figsize"] = (8, 10)

#funcion para la creacin de rutas

def rutas_mapas(filtro):
    ruta = filtro[15]

    divi = '{}shappes/div_2024/1_Divisiones_Ejercito.shp'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    

    return[divi, municipios_div, municipios, departamentos]

#funcion para la creacion de un mapa con las afectaciones con geopandas
def afecataciones_propias_tropas(datos, filtro):


    # print(asesinados)
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])
    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

    divisiones_municipios = gpd.read_file(ruta[1])


    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

    if datos[1]:
        # print("x")
        heridos = gpd.GeoDataFrame(datos[1])
        heridos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        heridos = gpd.GeoDataFrame(heridos, geometry = gpd.points_from_xy(heridos.longitud, heridos.latitud) )
        axis = heridos.plot(ax = axis, marker='*', color = "orange", markersize =40)

    if datos[0]:
        # print("x")
        asesinados = gpd.GeoDataFrame(datos[0])
        asesinados.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        asesinados = gpd.GeoDataFrame(asesinados, geometry = gpd.points_from_xy(asesinados.longitud, asesinados.latitud) )
        axis = asesinados.plot(ax = axis,marker='*',  color = "darkred", markersize =40)# asesinados = gpd.GeoDataFrame(asesinados, geometry = gpd.points_from_xy(asesinados.24, asesinados.25) )


    # axis.grid()
    axis.axis('off')
    imagen = '{}static/img/img_mapas/'.format(filtro[15])
    direccion = str(imagen)+str("afectaciones")+str(".png")
    # plt.savefig(imagen)
    plt.savefig(direccion, transparent=True)

    # df = divisiones.to_crs(epsg=3857)
    # ax = df.plot( figsize=(8, 10), alpha=0, edgecolor="k")
    # ax.axis('off')
    # cx.add_basemap(ax, crs=df.crs)

    # imagen = '{}static/img/img_mapas/'.format(filtro[15])
    # direccion = str(imagen)+str("afectaciones")+str("_fondo.png")
    # # plt.savefig(imagen)
    # plt.savefig(direccion, transparent=True)
    # # base_mapa(axis, filtro)


    

    
    
