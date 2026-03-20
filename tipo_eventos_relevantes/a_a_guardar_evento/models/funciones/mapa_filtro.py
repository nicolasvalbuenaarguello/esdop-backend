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

def rutas_mapas(filtro, unidad_g):
    unidades = [("DIV01","DIV1"),("DIV02","DIV2"),("DIV03","DIV3"),("DIV04","DIV4"),("DIV05","DIV5"),("DIV06","DIV6"),("DIV07","DIV7"),("DIV08","DIV8"),("FUTCO","FUTCO"),("FUTOM","FUTCO")]
    ruta = filtro
    unidad=""
    ruta_unidad=""

    for x in unidades:
        
        if x[0] == unidad_g:
            unidad=x[1]
            ruta_unidad=x[0]

    if unidad !="":
        divi = '{}shappes/{}/{}.shp'.format(ruta, ruta_unidad,unidad)
    else:
        divi = '{}shappes/div_2025/DIV_RES_EJC_2025.shp'.format(ruta)

    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)

    
    if unidad_g!="" and  unidad_g !="DIV01" and unidad_g !="DIV02" and unidad_g !="DIV03" and unidad_g !="DIV04" and unidad_g !="DIV05" and unidad_g !="DIV06" and unidad_g !="DIV07" and unidad_g !="DIV08" and unidad_g !="FUTCO"and unidad_g !="FUTOM":
        print(unidad_g)
        if "," in filtro[5]:
            departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)
        else:
            departamentos = '{}shappes/departamentos/{}.shp'.format(ruta, unidad_g)
            print("---")
    else:
        departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)


    return[divi, municipios_div, municipios, departamentos]

#funcion para la creacion de un mapa con las afectaciones con geopandas
def EVENTOS(datos, ruta_f, data, unidad_g):


    # print(asesinados)
    ruta = rutas_mapas(ruta_f, unidad_g)
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
def EVENTOS_id_2(datos, ruta_f, data, unidad, unidad_g):

        

        plt.rcParams["figure.figsize"] = (8, 10)
        plt.figure()

        
        ruta = rutas_mapas(ruta_f, unidad)
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
                axis.annotate(label, xy=(float(x), float(y)), xytext=(5, 5), textcoords="offset points",bbox = bbox_1, color='black', fontsize= 10)
        
        axis.axis('off')
        



        
        imagen = '{}static/img/img_mapas/'.format(ruta_f)
        direccion = str(imagen)+str(unidad)+str(".png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)


#funcion para filtrar mapas

def mapa_filtrado_dep(datos, ruta_f, data, unidad, unidad_g):

        

        plt.rcParams["figure.figsize"] = (8, 10)
        plt.figure()

       #------------------


        print(data)
        di = gpd.GeoDataFrame(data)
  
        di.rename(columns={29:"latitud", 30:"longitud", 6:"name", 25:"tipo",3:"divi_padre",9: "departamento",10:"municipio", 34:"numero"}, inplace=True)

        point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

        # #graficacion de los municipios 
        ruta = rutas_mapas(ruta_f, unidad)
        divisiones = gpd.read_file(ruta[0])
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        print(departamentos)
        municipios = municipios.clip(departamentos)
        point = point.clip(departamentos)

        #agrupacion de los eventos 

        ponit_agrupados_dep = point.groupby("departamento")["departamento"].agg(["count"])
        point_departamentos = point.merge(ponit_agrupados_dep, left_on="departamento", right_on = "departamento" )

        ponit_agrupados_municipios = point.groupby("municipio")["municipio"].agg(["count"])
        point_municipios = municipios.merge(ponit_agrupados_municipios, left_on="NOMBRE_ENT", right_on = "municipio" )

        
        # mun = departamentos.groupby("mpio")["mpio"].agg(["count"])
        # print(mun)
        # numici = municipios.merge(mun, left_on="NOMBRE_ENT", right_on = "NOMBRE_ENT" )



        
        # print(ponit_agrupados_dep)
        # join =  sjoin(departamentos, point_departamentos)
        join =  sjoin(municipios, point_departamentos)
        join_1 =  sjoin(departamentos, point_departamentos)
        join_1 = join_1.boundary

        join_2 = sjoin(point, point_municipios)

        # join_4 = sjoin(departamentos, numici)
        # join_4.intersection(municipios)
        

        join = join.boundary
        # join_4 = join_4.boundary

        
        # axis = join_1.plot(linewidth=0.3, color ="black")
        axis = join_1.plot(color ="black", alpha = 0.5)
        axis = join.plot(ax = axis, linewidth=0.3, color ="silver" )


        #-------------------




       
        #datos_colombia_div = divisiones.boundary


        #axis = datos_colombia_div.plot(ax = axis, linewidth=0.1, color ="gray", alpha = 0 )
        filled_marker_style = dict(marker='o', linestyle=':', markersize=15,
                                color='darkgrey',
                                markerfacecolor='tab:blue',
                                markerfacecoloralt='lightsteelblue',
                                markeredgecolor='brown')
        for x, y, label, tipo in zip(point.longitud, point.latitud, point.numero, point.tipo):

            if tipo == "POSITIVO":
                axis = point.plot(ax = axis, marker='*', color = "darkgreen", markersize =100 )
            else:
                axis = point.plot(ax = axis, marker='o', color = "firebrick", markersize =100)

                    
        bbox = dict(boxstyle ="round", fc ="0.8",  color="tab:green") 
        bbox_1 = dict(boxstyle ="round", fc ="0.8",  color="tab:red") 

        for x, y, label, tipo in zip(point.longitud, point.latitud, point.numero, point.tipo):
            
            if tipo == "POSITIVO":
                axis.annotate(label, xy=(float(x), float(y)), xytext=(-4, -4), textcoords="offset points", color='black', fontsize= 12)
            else:
                axis.annotate(label, xy=(float(x), float(y)), xytext=(-4, -4), textcoords="offset points", color='black', fontsize= 12)
        
        axis.axis('off')
        



        
        imagen = '{}static/img/img_mapas/'.format(ruta_f)
        direccion = str(imagen)+str(unidad)+str(".png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)
