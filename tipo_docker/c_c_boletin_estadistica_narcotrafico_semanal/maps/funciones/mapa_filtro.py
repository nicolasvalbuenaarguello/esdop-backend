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

#mapa de cocaina
def mapa_narcotrafico(datos, filtro):

    # print(asesinados)
    
    fichero =  rutas_mapas(filtro)
    divisiones = gpd.read_file(fichero[0])
   

    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=0.01,  color ="silver", )
    # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)
    divisiones_municipios = gpd.read_file(fichero[1])

    #graficacion de los municipios 
    municipios = gpd.read_file(fichero[2])
    departamentos = gpd.read_file(fichero[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

               
    if datos[9]:
        semilleros = gpd.GeoDataFrame(datos[9])
        semilleros.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        semilleros = gpd.GeoDataFrame(semilleros, geometry = gpd.points_from_xy(semilleros.longitud, semilleros.latitud) )
        axis = semilleros.plot(ax = axis, marker='8', color = "cyan", markersize =50, alpha = 0.8)  

    if datos[8]:
        lab_pbc = gpd.GeoDataFrame(datos[8])
        lab_pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        lab_pbc = gpd.GeoDataFrame(lab_pbc, geometry = gpd.points_from_xy(lab_pbc.longitud, lab_pbc.latitud) )
        axis = lab_pbc.plot(ax = axis, marker='8', color = "blue", markersize =50, alpha = 0.8)  

    if datos[7]:
        lab_cocaina = gpd.GeoDataFrame(datos[7])
        lab_cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
        axis = lab_cocaina.plot(ax = axis, marker='8', color = "gold", markersize =50, alpha = 0.8)  

    if datos[3]:
        marihuana = gpd.GeoDataFrame(datos[3])
        marihuana.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        marihuana = gpd.GeoDataFrame(marihuana, geometry = gpd.points_from_xy(marihuana.longitud, marihuana.latitud) )
        axis = marihuana.plot(ax = axis, marker='8', color = "green", markersize =50, alpha = 0.8)

    if datos[1]:
        pbc = gpd.GeoDataFrame(datos[1])
        pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        pbc = gpd.GeoDataFrame(pbc, geometry = gpd.points_from_xy(pbc.longitud, pbc.latitud) )
        axis = pbc.plot(ax = axis, marker='8', color = "darkorange", markersize =50, alpha = 0.8)

    if datos[0]:
        cocaina = gpd.GeoDataFrame(datos[0])
        cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        cocaina = gpd.GeoDataFrame(cocaina, geometry = gpd.points_from_xy(cocaina.longitud, cocaina.latitud) )
        # cocaina  =  cocaina.to_crs( epsg=3857)
        axis = cocaina.plot(ax = axis,marker='8',  color = "red", markersize =50, alpha = 0.8)


                    
    # if datos[7]:
    #     lab_cocaina = gpd.GeoDataFrame(datos[7])
    #     lab_cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
    #     lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
    #     axis = lab_cocaina.plot(ax = axis, marker='*', color = "gold", markersize =40, alpha = 0.8)
                
    # if datos[8]:
    #     lab_pbc = gpd.GeoDataFrame(datos[8])
    #     lab_pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
    #     lab_pbc = gpd.GeoDataFrame(lab_pbc, geometry = gpd.points_from_xy(lab_pbc.longitud, lab_pbc.latitud) )
    #     axis = lab_pbc.plot(ax = axis, marker='*', color = "moccasin", markersize =40, alpha = 0.9)
    
    # df_wm = divisiones.to_crs( epsg=3857)
    # ax = df_wm.plot(ax=axis, figsize=(8, 10), alpha=0.5, edgecolor='k')
    # # cx.add_basemap(ax)

    axis.axis('off')

    ruta = filtro[15]
    imagen = '{}static/img/img_mapas/mapa_narcotrafico.png'.format(ruta)
    pdf = '{}static/img/img_mapas/mapa_narcotrafico.pdf'.format(ruta)
    plt.savefig(imagen, transparent=True)
    # plt.savefig(pdf, format="pdf", bbox_inches="tight")
    # base_mapa(axis, filtro)
