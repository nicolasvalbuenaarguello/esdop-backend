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
    # divi = '{}shappes/DIVISIONES_2022/DIVISIONES_2022.shp'.format(ruta)
    divi = '{}shappes/div_2024/1_Divisiones_Ejercito.shp'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    

    return[divi, municipios_div, municipios, departamentos]
#mapa de hechos

#mapa de hechos
def mapa_hechos(datos, nombre, filtro):

    # print(asesinados)
    
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])

    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=1.5,  color ="black", )
    # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)
    divisiones_municipios = gpd.read_file(ruta[1])

    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

        
    if datos:
        hechos = gpd.GeoDataFrame(datos)
        hechos.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='*', color = "darkgreen", markersize =40)

    
    # axis.grid()
    axis.axis('off')
    imagen = '{}static/img/img_mapas/'.format(filtro[15])
    direccion = str(imagen)+str(nombre)+str(".png")
    # plt.savefig(imagen)
    plt.savefig(direccion, transparent=True)

    # df = divisiones.to_crs(epsg=3857)
    # ax = df.plot( figsize=(8, 10), alpha=0, edgecolor="k")
    # ax.axis('off')
    # cx.add_basemap(ax, crs=df.crs)

    # imagen = '{}static/img/img_mapas/'.format(filtro[15])
    # direccion = str(imagen)+str(nombre)+str("_fondo.png")
    # # plt.savefig(imagen)
    # plt.savefig(direccion, transparent=True)
    # # base_mapa(axis, filtro)