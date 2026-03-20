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
    divi = '{}shappes/DIVISIONES_2022/DIVISIONES_2022.shp'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    
    return[divi, municipios_div, municipios, departamentos]

def mapa_general(dato, filtro):
    
    #configuaracion de los datos 

    # combates = list(filter(lambda hechos :  hechos[0] == "COMBATE", dato))
    di = gpd.GeoDataFrame(dato)

    di.rename(columns={0:'hecho', 1:"fecha_hecho", 2:"agr_div", 3:"division", 4:"brigada", 5:"unidad" , 6:"dpto", 7:"mpio", 8:"enemigo", 9:"estrategia_afecta", 10:"hop_accion_davaa", 11:"hop_apoyo_blica", 12:"hop_apoyo_conat", 13:"hop_hecho_pos", 14:"cantidad", 15:"hop_operacion", 16:"latitud", 17:"longitud"}, inplace=True)

    point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud) )

    #graficacionde las divisiones
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

    #agrupacion de los eventos 
    ponit_agrupados = point.groupby("mpio")["mpio"].agg(["count"])
    ponit_agrupados_div = point.groupby("agr_div")["agr_div"].agg(["count"])


    datos_colombia = municipios.merge(ponit_agrupados, left_on="NOMBRE_ENT", right_on = "mpio", )

    # axis =  municipios.plot(ax = axis)

    datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "agr_div" )
    datos_colombia.intersection(municipios)
    
    # datos_colombia_div['perimetro'] = datos_colombia_div.boundary

    join =  sjoin(point, datos_colombia)
    join_2 =  sjoin(datos_colombia_div, divisiones)
    #graficaion de los eventos

    # if(dato_3 != "'-'"):

    #     axis = join_2.plot(ax = axis, color="grey", alpha =0.5 )
        

    join_3 = sjoin(datos_colombia, point)

    join_3 = join_3.boundary
    axis = join_3.plot(ax = axis, linewidth=0.1, color ="gray")

    axis = point.plot(ax = axis, cmap="YlOrRd", markersize =30 , alpha =0.5  )
    axis = join.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=20, markersize =15, column = "count" )
    # axis = join.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=20, markersize =15, column = "count", legend=True )

    # color = '#80cbc4'

    # img = mpimg.imread('C:/Users/Nicolas.Valbuena/Desktop/mpa/img/fondo.JPG')
    # axes_coords = [0, 0, 1, 1]
    # ax_image = plt.gcf().add_axes(axes_coords)
    # ax_image.imshow(img, alpha =.5)
    # ax_image.axis('off')

    # plt.show()
    # # plt.show()


    foto = '{}static/img/img_mapas/mapa.png'.format(filtro[15])
    plt.savefig(foto, transparent=True)
