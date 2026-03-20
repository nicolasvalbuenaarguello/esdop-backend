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

#mapa de cocaina
def mapa_narcotrafico(datos, filtro, nombre):

    # print(asesinados)
    
    fichero =  rutas_mapas(filtro)
    divisiones = gpd.read_file(fichero[0])
   

    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=1.5,  color ="black", )
    # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)
    divisiones_municipios = gpd.read_file(fichero[1])

    #graficacion de los municipios 
    municipios = gpd.read_file(fichero[2])
    departamentos = gpd.read_file(fichero[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

    if datos[0]:
        cocaina = gpd.GeoDataFrame(datos[0])
        cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        cocaina = gpd.GeoDataFrame(cocaina, geometry = gpd.points_from_xy(cocaina.longitud, cocaina.latitud) )
        # cocaina  =  cocaina.to_crs( epsg=3857)
        axis = cocaina.plot(ax = axis,marker='8',  color = "darkred", markersize =40, alpha = 0.8)
        

    if datos[1]:
        pbc = gpd.GeoDataFrame(datos[1])
        pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        pbc = gpd.GeoDataFrame(pbc, geometry = gpd.points_from_xy(pbc.longitud, pbc.latitud) )
        axis = pbc.plot(ax = axis, marker='8', color = "indigo", markersize =40, alpha = 0.8)
    
    if datos[3]:
        marihuana = gpd.GeoDataFrame(datos[3])
        marihuana.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        marihuana = gpd.GeoDataFrame(marihuana, geometry = gpd.points_from_xy(marihuana.longitud, marihuana.latitud) )
        axis = marihuana.plot(ax = axis, marker='8', color = "limegreen", markersize =40, alpha = 0.8)
                    
    if datos[7]:
        lab_cocaina = gpd.GeoDataFrame(datos[7])
        lab_cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
        axis = lab_cocaina.plot(ax = axis, marker='8', color = "gold", markersize =40, alpha = 0.8)
                
    if datos[8]:
        lab_pbc = gpd.GeoDataFrame(datos[8])
        lab_pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        lab_pbc = gpd.GeoDataFrame(lab_pbc, geometry = gpd.points_from_xy(lab_pbc.longitud, lab_pbc.latitud) )
        axis = lab_pbc.plot(ax = axis, marker='8', color = "moccasin", markersize =40, alpha = 0.9)
    
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
