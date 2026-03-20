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

def rutas_mapas(ruta):
    

    divi = '{}shappes/div_2025/DIV_RES_EJC_2025.shp'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    

    return[divi, municipios_div, municipios, departamentos]

#funcion para la creacion de un mapa con las afectaciones con geopandas
def EVENTOS(datos, ruta_f, data):


    # print(asesinados)
    ruta = rutas_mapas(ruta_f)
    divisiones = gpd.read_file(ruta[0])
    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=0.7, color ="black", )

    di = gpd.GeoDataFrame(data)
    di.rename(columns={29:"latitud", 30:"longitud", 6:"name", 25:"tipo",3:"divi_padre",10:"municipio", 34:"numero"}, inplace=True)
    point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))
    
    crs = {'init': 'epsg:4326'}

    point = point.set_crs(epsg=4686, allow_override=True)



    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

    for x, y, label, tipo in zip(point.longitud, point.latitud, point.name, point.tipo):

        if tipo == "POSITIVO":
            axis = point.plot(ax = axis, marker='*', color = "darkgreen", markersize =100 )
        else:
            axis = point.plot(ax = axis, marker='*', color = "darkred", markersize =100)


    # axis.grid()
    
    bbox = dict(boxstyle ="round", fc ="0.8",  color="tab:green") 
    bbox_1 = dict(boxstyle ="round", fc ="0.8",  color="tab:red") 

    for x, y, label, tipo in zip(point.longitud, point.latitud, point.numero, point.tipo):
        if tipo == "POSITIVO":
            axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox, color='black', fontsize= 10)
        else:
            axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox_1, color='black', fontsize= 10)
    axis.axis('off')
    
    imagen = '{}static/img/img_mapas/'.format(ruta_f)
    direccion = str(imagen)+str("EVENTOS")+str(".png")
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

#funcion para la creacion de un mapa con las afectaciones con geopandas
def EVENTOS_id(datos, ruta_f, data, unidad):


    # print(asesinados)
    ruta = rutas_mapas(ruta_f)
    divisiones = gpd.read_file(ruta[0])
    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=0.7, color ="black", )


    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

    datos_g = gpd.GeoDataFrame(data)
    datos_g.rename(columns={29:"latitud", 30:"longitud", 31:"name", 25:"tipo",3:"divi_padre",10:"municipio"}, inplace=True)
    datos_g = gpd.GeoDataFrame(datos_g, geometry = gpd.points_from_xy(datos_g.longitud, datos_g.latitud) )

    if datos[1]:
        # print("x")
        afectacion = gpd.GeoDataFrame(datos[1])
        afectacion.rename(columns={29:"latitud", 30:"longitud" ,3:"divi_padre",10:"municipio"}, inplace=True)
        afectacion = gpd.GeoDataFrame(afectacion, geometry = gpd.points_from_xy(afectacion.longitud, afectacion.latitud) )
        axis = afectacion.plot(ax = axis, marker='*', color = "darkgreen", markersize =120)
        

    if datos[0]:
        # print("x")
        afectacion = gpd.GeoDataFrame(datos[0])
        afectacion.rename(columns={29:"latitud", 30:"longitud",3:"divi_padre",10:"municipio"}, inplace=True)
        afectacion = gpd.GeoDataFrame(afectacion, geometry = gpd.points_from_xy(afectacion.longitud, afectacion.latitud) )
        axis = afectacion.plot(ax = axis, marker='*',  color = "darkred", markersize =120)# asesinados = gpd.GeoDataFrame(asesinados, geometry = gpd.points_from_xy(asesinados.24, asesinados.25) )
    
    bbox = dict(boxstyle ="round", fc ="0.8",  color="tab:green") 
    bbox_1 = dict(boxstyle ="round", fc ="0.8",  color="tab:red") 

    for x, y, label, tipo in zip(datos_g.longitud, datos_g.latitud, datos_g.name, datos_g.tipo):
        if tipo == "POSITIVO":
            axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox, color='black', fontsize= 10)
        else:
            axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox_1, color='black', fontsize= 10)



    axis.axis('off')
    
    imagen = '{}static/img/img_mapas/'.format(ruta_f)
    direccion = str(imagen)+str(unidad)+str(".png")
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

#funcion para la creacion de un mapa con las afectaciones con geopandas
def EVENTOS_id_2(datos, ruta_f, data, unidad):



        plt.rcParams["figure.figsize"] = (8, 10)
        plt.figure()

        
        ruta = rutas_mapas(ruta_f)
        divisiones = gpd.read_file(ruta[0])
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        #paramtro de tamaño del mapa
        
        #configuaracion de los datos 
        di = gpd.GeoDataFrame(data)
        di.rename(columns={29:"latitud", 30:"longitud", 6:"name", 25:"tipo",3:"divi_padre",10:"municipio"}, inplace=True)

        point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))
    
        crs = {'init': 'epsg:4326'}

        point = point.set_crs(epsg=4686, allow_override=True)
        divisiones = divisiones.set_crs(epsg=4686, allow_override=True)

        # #graficacion de los municipios 


        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

        departamentos["perimetro"] = departamentos.boundary
        municipios["perimetro"] = municipios.boundary

        #agrupacion de los eventos 
        ponit_agrupados = point.groupby("municipio")["municipio"].agg(["count"])
        datos_colombia = municipios.merge(ponit_agrupados, left_on="NOMBRE_ENT", right_on = "municipio", )

   
        ponit_agrupados_div = point.groupby("divi_padre")["divi_padre"].agg(["count"])
        

        ponit_agrupados_municipios = point.groupby("municipio")["municipio"].agg(["count"])
        point_municipios = municipios.merge(ponit_agrupados_municipios, left_on="NOMBRE_ENT", right_on = "municipio" )
    
        datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "divi_padre" )
        datos_colombia_div.intersection(point)
        
        join =  sjoin(divisiones , point)
        join = datos_colombia_div.boundary
        axis = join.plot(color ="darkred", alpha = 0.5)
       
        #datos_colombia_div = divisiones.boundary


        axis = datos_colombia_div.plot(ax = axis, linewidth=0.1, color ="gray", alpha = 0 )

        for x, y, label, tipo in zip(point.longitud, point.latitud, point.name, point.tipo):

            if tipo == "POSITIVO":
                axis = point.plot(ax = axis, marker='*', color = "darkgreen", markersize =100 )
            else:
                axis = point.plot(ax = axis, marker='*', color = "darkred", markersize =100)

                    
        bbox = dict(boxstyle ="round", fc ="0.8",  color="tab:green") 
        bbox_1 = dict(boxstyle ="round", fc ="0.8",  color="tab:red") 

        for x, y, label, tipo in zip(point.longitud, point.latitud, point.name, point.tipo):
            
            if tipo == "POSITIVO":
                axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox, color='black', fontsize= 10)
            else:
                print(x)
                axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox_1, color='black', fontsize= 10)
        
        axis.axis('off')
        



        
        imagen = '{}static/img/img_mapas/'.format(ruta_f)
        direccion = str(imagen)+str(unidad)+str(".png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)



    
    

    
    

    
    
