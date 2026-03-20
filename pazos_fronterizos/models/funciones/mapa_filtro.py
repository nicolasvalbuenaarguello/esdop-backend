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


def rutas_mapas(filtro):
    unidades = {
        "DIV01": "DIV1", "DIV02": "DIV2", "DIV03": "DIV3",
        "DIV04": "DIV4", "DIV05": "DIV5", "DIV06": "DIV6",
        "DIV07": "DIV7", "DIV08": "DIV8", "FUTCO": "FUTCO", "FUTOM": "FUTCO"
    }

    ruta = filtro[1]
    unidad_codigo = filtro[0]
    unidad = unidades.get(unidad_codigo, "")

    ruta_unidad = unidad_codigo if unidad_codigo != "FUTOM" else "FUTCO"

    divi = f'{ruta}shappes/{ruta_unidad}/{unidad}.shp' if unidad else f'{ruta}shappes/div_2025/DIV_RES_EJC_2025.shp'

    municipios_div = f'{ruta}shappes/divisiones/div_mun.shp'
    municipios = f'{ruta}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'

    if filtro[2] and filtro[2] != "---":
        departamentos = f'{ruta}shappes/DEPARTA/Export_Output_7.shp' if "," in filtro[5] else f'{ruta}shappes/departamentos/{filtro[5]}.shp'
    else:
        departamentos = f'{ruta}shappes/DEPARTA/Export_Output_7.shp'

    return [divi, municipios_div, municipios, departamentos]

#funcion para la creacion de un mapa con las afectaciones con geopandas
def EVENTOS(ruta_f, formal, no_forma, data_2):


    # print(asesinados)
    ruta = rutas_mapas(ruta_f)
    divisiones = gpd.read_file(ruta[0])
    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=0.7, color ="black", )

    di = gpd.GeoDataFrame(formal)
    di.rename(columns={13:"latitud", 14:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)
    point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

    di_f = gpd.GeoDataFrame(no_forma)
    di_f.rename(columns={13:"latitud", 14:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)
    point_no_forma = gpd.GeoDataFrame(di_f, geometry = gpd.points_from_xy(di_f.longitud, di_f.latitud))
    
    unidad = gpd.GeoDataFrame(data_2)
    unidad.rename(columns={37:"latitud", 38:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)

    point_unidad = gpd.GeoDataFrame(unidad, geometry = gpd.points_from_xy(unidad.longitud, unidad.latitud))
    
    crs = {'init': 'epsg:4326'}

    point = point.set_crs(epsg=4326, allow_override=True)
    point_unidad = point_unidad.set_crs(epsg=4326, allow_override=True)
    point_no_forma = point_no_forma.set_crs(epsg=4326, allow_override=True)

    #graficacion de los municipios 
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])
    departamentos = departamentos.boundary
    axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)


    axis = point_no_forma.plot(ax = axis, marker='X', color = "darkred", markersize =60)
     
    axis = point.plot(ax = axis, marker='*', color = "darkgreen", markersize =40)

    axis = point_unidad.plot(ax = axis, marker='s', markersize =40)
    
    axis.axis('off')
    
    imagen = '{}static/img/img_mapas/'.format(ruta_f)
    direccion = str(imagen)+str("PAZOS")+str(".png")
    # plt.savefig(imagen)
    plt.savefig(direccion, transparent=True)



def EVENTOS_id_2(ruta_f, formal, no_forma, data_2, div):

        # print(asesinados)
        ruta = rutas_mapas(ruta_f)
        divisiones = gpd.read_file(ruta[0])
        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=0.7, color ="black", )

        if len(formal)!=0:
            di = gpd.GeoDataFrame(formal)
            di.rename(columns={13:"latitud", 14:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)
            point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

        if len(no_forma)!=0:
            di_f = gpd.GeoDataFrame(no_forma)
            di_f.rename(columns={13:"latitud", 14:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)
            point_no_forma = gpd.GeoDataFrame(di_f, geometry = gpd.points_from_xy(di_f.longitud, di_f.latitud))
        if len(data_2)!=0:
            unidad = gpd.GeoDataFrame(data_2)
            unidad.rename(columns={37:"latitud", 38:"longitud", 7:"name", 11:"tipo",4:"divi_padre"}, inplace=True)
            point_unidad = gpd.GeoDataFrame(unidad, geometry = gpd.points_from_xy(unidad.longitud, unidad.latitud))
        
        crs = {'init': 'epsg:4326'}

        if len(formal)!=0:
            point = point.set_crs(epsg=4326, allow_override=True)
        if len(data_2)!=0:
            point_unidad = point_unidad.set_crs(epsg=4326, allow_override=True)
        if len(no_forma)!=0:
            point_no_forma = point_no_forma.set_crs(epsg=4326, allow_override=True)

        #graficacion de los municipios 
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        departamentos = departamentos.boundary
            # #graficacion de los municipios 


        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

        #agrupacion de los eventos 
        if len(no_forma)!=0:
 
            ponit_agrupados_div = point_no_forma.groupby("divi_padre")["divi_padre"].agg(["count"])
            datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "divi_padre" )
            datos_colombia_div.intersection(point_no_forma)
        
            join =  sjoin(divisiones , point_no_forma)
            join = datos_colombia_div.boundary
            axis = join.plot(color ="darkred", alpha = 0.5)
       
        #datos_colombia_div = divisiones.boundary
            axis = datos_colombia_div.plot(ax = axis, linewidth=0.1, color ="gray", alpha = 0 )

        if len(no_forma)!=0:
            axis = point_no_forma.plot(ax = axis, marker='X', color = "darkred", markersize =60)

        if len(formal)!=0:
            axis = point.plot(ax = axis, marker='*', color = "darkgreen", markersize =60)
        if len(data_2)!=0:
            axis = point_unidad.plot(ax = axis, marker='s', markersize =20)

        
        
        axis.axis('off')
        



        
        imagen = '{}static/img/img_mapas/'.format(ruta_f)
        direccion = str(imagen)+str(div)+str("_pasos.png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)


def PUESTO_VOTACION(ruta_f, formal, no_forma, datos, div):

        # print(asesinados)
        ruta = rutas_mapas(ruta_f)
        divisiones = gpd.read_file(ruta[0])
        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=0.7, color ="black", )
        
        if len(formal)!=0:
            di = gpd.GeoDataFrame(formal)
            di.rename(columns={13:"latitud", 14:"longitud", 6:"name", 15:"tipo",16:"divi_padre"}, inplace=True)
            point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

        if len(no_forma)!=0:
            di_f = gpd.GeoDataFrame(no_forma)
            di_f.rename(columns={13:"latitud", 14:"longitud", 6:"name", 15:"tipo",16:"divi_padre"}, inplace=True)
            point_no_forma = gpd.GeoDataFrame(di_f, geometry = gpd.points_from_xy(di_f.longitud, di_f.latitud))
    
        if len(datos)!=0:
            di_f = gpd.GeoDataFrame(datos)
            di_f.rename(columns={13:"latitud", 14:"longitud", 6:"name", 15:"tipo",16:"divi_padre"}, inplace=True)
            datos = gpd.GeoDataFrame(di_f, geometry = gpd.points_from_xy(di_f.longitud, di_f.latitud))
    
        
        crs = {'init': 'epsg:4326'}

        if len(formal)!=0:
            point = point.set_crs(epsg=4326, allow_override=True)
   
        if len(no_forma)!=0:
            point_no_forma = point_no_forma.set_crs(epsg=4326, allow_override=True)

        if len(datos)!=0:
            datos = datos.set_crs(epsg=4326, allow_override=True)


            

        #graficacion de los municipios 
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        departamentos = departamentos.boundary
            # #graficacion de los municipios 


        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

        #agrupacion de los eventos 
        # --- Agrupación y sombreado por división ---
        #print(datos)
        if datos is not None and len(datos) > 0:
            ponit_agrupados_div = datos.groupby("divi_padre")["divi_padre"].agg(["count"])
            datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on="divi_padre", how="left")

            # Evita geometrías nulas
            datos_colombia_div = datos_colombia_div[~datos_colombia_div.geometry.isna()]

            # Dibujar borde resaltado donde hay datos
            datos_colombia_div.boundary.plot(ax=axis, color="darkred", linewidth=1.2, alpha=0.7)
            datos_colombia_div.plot(ax=axis, linewidth=0.1, color="gray", alpha=0)
        
            #datos_colombia_div = divisiones.boundary
            #axis = datos_colombia_div.plot(ax = axis, linewidth=0.1, color ="gray", alpha = 0 )

        if len(no_forma)!=0:
            axis = point_no_forma.plot(ax = axis, marker='o', color = "darkgreen", markersize =10)

        if len(formal)!=0:
            axis = point.plot(ax = axis, marker='o', color = "goldenrod", markersize =10)

        
        axis.axis('off')
        
        
        imagen = '{}static/img/img_mapas/'.format(ruta_f[1])
        direccion = str(imagen)+str(div)+str("_puesto_votacion.png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)



    
    

    
    

    
    
