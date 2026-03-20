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

    
    # df_wm = divisiones.to_crs( epsg=3857)
    # ax = df_wm.plot(ax=axis, figsize=(8, 10), alpha=0.5, edgecolor='k')
    # # cx.add_basemap(ax)
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
    # # base_mapa(axis, filtro)
#mapa de hechos
def mapa_hechos_p(datos, nombre, filtro):

    # print(asesinados)
    
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])

    divisiones["perimetro"] = divisiones.boundary
    # axis = divisiones["perimetro"].plot( linewidth=0.8,  color ="black", )
    axis = divisiones["perimetro"].plot( linewidth=0.1,  color ="silver", )
    # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)
    divisiones_municipios = gpd.read_file(ruta[1])

    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    # axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="silver", alpha =0.1)

        
    if datos[0]:
        hechos = gpd.GeoDataFrame(datos[0])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkred", markersize =40)

    if datos[1]:
        hechos = gpd.GeoDataFrame(datos[1])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkred", markersize =40)
                        
    if datos[2]:
        hechos = gpd.GeoDataFrame(datos[2])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkred", markersize =40)
                        
    if datos[3]:
        if datos[3][8] != "DELINCUENCIA" and datos[3][8] != "DELINCUENCIA":
            hechos = gpd.GeoDataFrame(datos[3])
            hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
            hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
            axis = hechos.plot(ax = axis, marker='8', color = "darkred", markersize =40)
                                
    if datos[4]:
        hechos = gpd.GeoDataFrame(datos[4])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkred", markersize =40)

                                        
    if datos[16]:
        hechos = gpd.GeoDataFrame(datos[16])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkgreen", markersize =40)

                                        
    if datos[17]:
        hechos = gpd.GeoDataFrame(datos[17])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkgreen", markersize =40)
        
                                        
    if datos[18]:
        hechos = gpd.GeoDataFrame(datos[18])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "darkgreen", markersize =40)
                                                
    if datos[10]:
        hechos = gpd.GeoDataFrame(datos[10])
        hechos.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)
                                                        
    if datos[11]:
        hechos = gpd.GeoDataFrame(datos[11])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)
                                                                
    if datos[12]:
        hechos = gpd.GeoDataFrame(datos[12])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)
                                                                        
    if datos[13]:
        hechos = gpd.GeoDataFrame(datos[13])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)
                                                                                
    if datos[14]:
        hechos = gpd.GeoDataFrame(datos[14])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)

                                                                                
    if datos[15]:
        hechos = gpd.GeoDataFrame(datos[15])
        hechos.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        hechos = gpd.GeoDataFrame(hechos, geometry = gpd.points_from_xy(hechos.longitud, hechos.latitud) )
        axis = hechos.plot(ax = axis, marker='8', color = "orange", markersize =40)
    

    axis.axis('off')
    # df_wm = divisiones.to_crs( epsg=3857)
    # ax = df_wm.plot(ax=axis, figsize=(8, 10), alpha=0.5, edgecolor='k')
    # # cx.add_basemap(ax)
    imagen = '{}static/img/img_mapas/'.format(filtro[15])
    direccion = str(imagen)+str("nombre")+str(".png")
    plt.savefig(direccion, transparent=True)
    # base_mapa(axis, filtro)