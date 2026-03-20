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
# from matplotlib.lines import Line2D
from mpl_toolkits.basemap import Basemap
import numpy as np

plt.rcParams["figure.figsize"] = (8, 10)

#funcion para la creacin de rutas

def rutas_mapas(filtro):
    ruta = filtro[15]
    # divi = '{}shappes/DIVISIONES_2022/DIVISIONES_2022.shp'.format(ruta)
    divi = '{}shappes/div_2024/1_Divisiones_Ejercito.shp'.format(ruta)
    # divi_2 = '{}shappes/div_2024/1_Divisiones_Ejercito'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    

    return[divi, municipios_div, municipios, departamentos]

#graficacion de mapas de dos puntos 
def mapa_dos_puntos(datos,nombre, filtro):

    # print(asesinados)
    
    fichero =  rutas_mapas(filtro)
    divisiones = gpd.read_file(fichero[0])


    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=1.5,  color ="black", )
    # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)
    divisiones_municipios = gpd.read_file(fichero[1])

            

    # cx.add_basemap(ax, source=cx.providers.CartoDB.PositronNoLabels, zoom=12)
    # cx.add_basemap(ax, source=cx.providers.CartoDB.PositronOnlyLabels, zoom=10)
    

    #graficacion de los municipios 
    municipios = gpd.read_file(fichero[2])
    departamentos = gpd.read_file(fichero[3])
    departamentos = departamentos.boundary
    # departamentos = departamentos.to_crs(epsg=3857)
    axis = departamentos.plot(ax = axis, linewidth=0.1, color ="black", alpha =0.8)

    if datos[0]:
        cocaina = gpd.GeoDataFrame(datos[0])
        cocaina.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        cocaina = gpd.GeoDataFrame(cocaina, geometry = gpd.points_from_xy(cocaina.longitud, cocaina.latitud))
        # cocaina  =  cocaina.to_crs( epsg=3857)
        axis = cocaina.plot(ax = axis,marker='*',  color = "darkgreen", markersize =40, alpha = 0.8)
        
        
    if datos[1]:
        pbc = gpd.GeoDataFrame(datos[1])
        pbc.rename(columns={24:"latitud", 25:"longitud"}, inplace=True)
        # print(pbc.longitud)
        pbc = gpd.GeoDataFrame(pbc, geometry = gpd.points_from_xy(pbc.longitud, pbc.latitud))

        # pbc  =  pbc.to_crs( epsg=3857)
        axis = pbc.plot(ax = axis, marker='*', color = "gold", markersize =40, alpha = 0.8)
        
    # axis.grid()
    axis.axis('off')
    imagen = '{}static/img/img_mapas/'.format(filtro[15])
    direccion = str(imagen)+str(nombre)+str(".png")
    # plt.savefig(imagen)
    plt.savefig(direccion, transparent=True)

    # df = gpd.read_file(fichero[0])
    # # df = df.to_file(fichero[0], driver='ESRI Shapefile')
    # df = df.to_crs(epsg=3857)
    # ax = df.plot( figsize=(8, 10), alpha=0, edgecolor="k", color="red")
    # # ax.axis('off')
    # cx.add_basemap(ax, crs=df.crs)

    # imagen = '{}static/img/img_mapas/'.format(filtro[15])
    # direccion = str(imagen)+str(nombre)+str("_fondo.png")
    # # plt.savefig(imagen)
    # plt.savefig(direccion, transparent=True)


    # #-------------------------------------------------------------
    # #inicio del proyecto para el mapa con coordenadas, para seguien con el avanze quitar los comentarios desde el inico al fin 
    # lat_y= 3.250
    # lot_x= -75.2542
    
    # map = Basemap(projection='merc', 
    #               llcrnrlat=-4,
    #               llcrnrlon=-80,

    #               urcrnrlat=14,
    #               urcrnrlon=-65,
    #               resolution='c',
    #               lat_1=-4.,
    #             #   lat_2=55,
    #               lon_0=65,
    #             #   lon_0=-107.,
    #               width=12000000,
    #               height=9000000,
    #               )
    
    # fig     = plt.figure()
    # ax      = fig.add_subplot(111)
    # ax = fig.add_subplot()
    # map.drawcoastlines(ax = ax, linewidth=1.5)
    # shp_info = map.readshapefile(fichero[4], 'Name', name="zone",
    #         ax=ax, linewidth=3)
    # print(shp_info)
    # map.drawparallels(np.arange(-6,15,1),labels=[True, False, False, False])
    # map.drawmeridians(np.arange(-80,-65,1), labels=[0,0,0,1])

    # # parallels = np.arange(0.,81,1.)
    # # # labels = [left,right,top,bottom]
    # # map.drawparallels(parallels,labels=[False,True,True,False])
    # # meridians = np.arange(10.,351.,20.)
    # # map.drawmeridians(meridians,labels=[True,False,False,True])

    # lon, lat = -75.237, 5.125 # Location of Boulder
    # xpt,ypt = map(lon,lat) 
    # lonpt, latpt = map(xpt,ypt,inverse=True)
    # ax =  map.plot(xpt,ypt,'bo')  # plot a blue dot there 

    # plt.text(xpt+100000,ypt+100000,'Boulder (%5.1fW,%3.1fN)' % (lonpt,latpt))

    # # stateshp = gpd.read_file(fichero[0])
    # # #print stateshp1.crs
    # # stateshp.crs={}
    # # stateshp.to_file(fichero[0], driver='ESRI Shapefile')

    # # map.readshapefile(fichero[4], 'Name')

    # # map.scatter(lot_x, lat_y, latlon=True, s=100, c='blue', marker =0, alpha=1,edgecolor="k", linewidth = 1, zorder =2)
    
    # # sites_lat_y
    # # fig     = plt.figure()
    # # ax  = fig.add_subplot(111)

    # map.drawmapboundary(fill_color='aqua')
    # map.fillcontinents(color='coral',lake_color='aqua')

    # # map.readshapefile(fichero[4], 'Name', drawbounds = False)

    # # patches   = []

        
    # #-------------------------------------------------------------
    #fin del proyecto para el mapa con coordenadas 



    # axis.set_xlabel('Longitud')
    # axis.set_ylabel('Latitud')
    # divisiones = gpd.read_file(fichero[0])
    # df = divisiones.to_crs(epsg=3857)
    # ax = df.plot( figsize=(8, 10), alpha=0, edgecolor="k")
    # ax.axis('off')
    # cx.add_basemap(ax, crs=ax.crs)

    # imagen = '{}static/img/img_mapas/'.format(filtro[15])
    # direccion = str(imagen)+str(nombre)+str("_fondo.png")
    # # plt.savefig(imagen)
    # plt.savefig(direccion, transparent=True)
    # # base_mapa(axis, filtro)

