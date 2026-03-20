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



#funcion para la creacin de rutas

def rutas_mapas(filtro):
    
    ruta = filtro[15]
    divi = '{}shappes/div_2024/1_Divisiones_Ejercito.shp'.format(ruta)
    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    
    return[divi, municipios_div, municipios, departamentos]

def mapa_general(dato, filtro):
    plt.rcParams["figure.figsize"] = (8, 10)
    
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
    # print(divisiones)

    datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="Name", right_on = "agr_div" )
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
    axis = join.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=20, markersize =15, column = "count")
    axis.axis('off')
    # axis = join.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=20, markersize =15, column = "count", legend=True )

    # color = '#80cbc4'

    # img = mpimg.imread('C:/Users/Nicolas.Valbuena/Desktop/mpa/img/fondo.JPG')
    # axes_coords = [0, 0, 1, 1]
    # ax_image = plt.gcf().add_axes(axes_coords)
    # ax_image.imshow(img, alpha =.5)
    # ax_image.axis('off')

    # plt.show()
    # # plt.show()


    # axis.grid()
    axis.axis('off')
    imagen = '{}static/img/img_mapas/'.format(filtro[15])
    direccion = str(imagen)+str("mapa")+str(".png")
    # plt.savefig(imagen)
    plt.savefig(direccion, transparent=True)

    # df = divisiones.to_crs(epsg=3857)
    # ax = df.plot( figsize=(8, 10), alpha=0, edgecolor="k")
    # ax.axis('off')
    # cx.add_basemap(ax, crs=df.crs)

    # imagen = '{}static/img/img_mapas/'.format(filtro[15])
    # direccion = str(imagen)+str("mapa_fondo")+str(".png")
    # # plt.savefig(imagen)
    # plt.savefig(direccion, transparent=True)
    # # base_mapa(axis, filtro)


    #funcion para filtrar mapas
def mapa_filtrado(dato, filtro):
    plt.rcParams["figure.figsize"] = (8, 10)
    #paramtro de tamaño del mapa
    


    #configuaracion de los datos 
    di = gpd.GeoDataFrame(dato)
    di.rename(columns={0:'hecho', 1:"fecha_hecho", 2:"agr_div", 3:"division", 4:"brigada", 5:"unidad" , 6:"dpto", 7:"mpio", 8:"enemigo", 9:"estrategia_afecta", 10:"hop_accion_davaa", 11:"hop_apoyo_blica", 12:"hop_apoyo_conat", 13:"hop_hecho_pos", 14:"cantidad", 15:"hop_operacion", 16:"latitud", 17:"longitud"}, inplace=True)

   

    point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

    # #graficacion de los municipios 

    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])

    divisiones["perimetro"] = divisiones.boundary
    axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

    departamentos["perimetro"] = departamentos.boundary
    municipios["perimetro"] = municipios.boundary

    #agrupacion de los eventos 
    ponit_agrupados = point.groupby("mpio")["mpio"].agg(["count"])
    datos_colombia = municipios.merge(ponit_agrupados, left_on="NOMBRE_ENT", right_on = "mpio", )

    ponit_agrupados_dep = point.groupby("dpto")["dpto"].agg(["count"])
    point_departamentos = point.merge(ponit_agrupados_dep, left_on="dpto", right_on = "dpto" )
    
    ponit_agrupados_div = point.groupby("agr_div")["agr_div"].agg(["count"])
    

    ponit_agrupados_municipios = point.groupby("mpio")["mpio"].agg(["count"])
    point_municipios = municipios.merge(ponit_agrupados_municipios, left_on="NOMBRE_ENT", right_on = "mpio" )

    datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "agr_div" )
    datos_colombia.intersection(municipios)

    
    # mun = departamentos.groupby("mpio")["mpio"].agg(["count"])
    # print(mun)
    # numici = municipios.merge(mun, left_on="NOMBRE_ENT", right_on = "NOMBRE_ENT" )



    
    # print(ponit_agrupados_dep)
    join =  sjoin(municipios , point)
    join_1 =  sjoin(datos_colombia_div, datos_colombia)

    join_2 = sjoin(point, point_municipios)
    join_1 = join_1.boundary
    # join_4 = sjoin(departamentos, numici)
    # join_4.intersection(municipios)
    

    join = join.boundary
    # join_4 = join_4.boundary

    
    # axis = join_1.plot(linewidth=0.3, color ="black")
    axis = join_1.plot(color ="gray", alpha = 0.5)
    axis = join.plot(ax = axis, linewidth=0.3, color ="black" )

    # axis = join_4.plot(linewidth=0.3, color ="gray" )


    # join_3 = sjoin(point_municipios, point)

    # join_3 = join_3.boundary
    # axis = join_3.plot(ax = axis, linewidth=0.1, color ="black")
    # axis = join_3.plot(ax = axis, linewidth=0.1, color ="black")

    

    # departamentos_POIN = departamentos.merge(ponit_agrupados_municipios, left_on="DEPARTAMEN", right_on = "mpio" )

    # 

    # axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.5)




    # axis =  municipios.plot(ax = axis)

    # datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "agr_div" )
    # datos_colombia.intersection(municipios)
    # datos_colombia_div['perimetro'] = datos_colombia_div.boundary

    # join =  sjoin(point, datos_colombia)
    # join_2 =  sjoin(datos_colombia_div, divisiones)
    #graficaion de los eventos

    # if(dato_3 != "'-'"):

    axis = join_2.plot(ax = axis, color="black", alpha =0.5 )
        


    # join.plot(cmap="YlOrRd", scheme= "QUANTILES", k=24, markersize =15, column = "count" )

    # if(dato_3 != "'-'"):

    axis = point.plot(ax = axis, cmap="YlOrRd", markersize =5  ,  alpha =0.1 )


    # if(dato_3 != "'-'"):
    # ponit_agrupados = point.groupby("mpio")["mpio"].agg(["count"])  
    # datos_colombia = municipios.merge(ponit_agrupados, left_on="NOMBRE_ENT", right_on = "mpio", )
    # datos_colombia.intersection(municipios)
    # join =  sjoin(point, datos_colombia)
    # join = join.boundary
    # axis = join.plot(ax = axis, cmap="YlOrRd", markersize =15  ,  alpha =0.5 )

    # point.plot(ax = axis, cmap="YlOrRd", markersize =30  ,  alpha =0.5 )
    axis = point.plot(ax = axis, cmap="YlOrRd", markersize =30 , alpha =0.5  )
    axis = join_2.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=30, markersize =30, column = "count", alpha =0.5 )
    axis.axis('off')


    # cx.add_basemap(axis, source=cx.providers.Stamen.TonerLite)

    

    # plt.show()
    # figure = plt.gcf() # get current figure
    # figure.set_size_inches(4, 5)
    foto = '{}static/img/img_mapas/mapa.png'.format(filtro[15])
    plt.savefig(foto,format="png", transparent=True, dpi = 100)
    # plt.savefig("scr/static/img/img_mapas/mapa.png")



#funcion para filtrar mapas
def mapa_filtrado_dep(dato, filtro):
    #paramtro de tamaño del mapa
    
    plt.rcParams["figure.figsize"] = (8, 10)    

    #configuaracion de los datos 
    di = gpd.GeoDataFrame(dato)
    di.rename(columns={0:'hecho', 1:"fecha_hecho", 2:"agr_div", 3:"division", 4:"brigada", 5:"unidad" , 6:"dpto", 7:"mpio", 8:"enemigo", 9:"estrategia_afecta", 10:"hop_accion_davaa", 11:"hop_apoyo_blica", 12:"hop_apoyo_conat", 13:"hop_hecho_pos", 14:"cantidad", 15:"hop_operacion", 16:"latitud", 17:"longitud"}, inplace=True)

   

    point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))

    # #graficacion de los municipios 
    ruta = rutas_mapas(filtro)
    divisiones = gpd.read_file(ruta[0])
    municipios = gpd.read_file(ruta[2])
    departamentos = gpd.read_file(ruta[3])




    #agrupacion de los eventos 

    ponit_agrupados_dep = point.groupby("dpto")["dpto"].agg(["count"])
    point_departamentos = point.merge(ponit_agrupados_dep, left_on="dpto", right_on = "dpto" )

    ponit_agrupados_municipios = point.groupby("mpio")["mpio"].agg(["count"])
    point_municipios = municipios.merge(ponit_agrupados_municipios, left_on="NOMBRE_ENT", right_on = "mpio" )

    
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

    # axis = join_4.plot(linewidth=0.3, color ="gray" )


    # join_3 = sjoin(point_municipios, point)

    # join_3 = join_3.boundary
    # axis = join_3.plot(ax = axis, linewidth=0.1, color ="black")
    # axis = join_3.plot(ax = axis, linewidth=0.1, color ="black")

    

    # departamentos_POIN = departamentos.merge(ponit_agrupados_municipios, left_on="DEPARTAMEN", right_on = "mpio" )

    # 

    # axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.5)




    # axis =  municipios.plot(ax = axis)

    # datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "agr_div" )
    # datos_colombia.intersection(municipios)
    # datos_colombia_div['perimetro'] = datos_colombia_div.boundary

    # join =  sjoin(point, datos_colombia)
    # join_2 =  sjoin(datos_colombia_div, divisiones)
    #graficaion de los eventos

    # if(dato_3 != "'-'"):

    axis = join_2.plot(ax = axis, color="black", alpha =0.1 )
        

    # point.plot(ax = axis, cmap="YlOrRd", markersize =30  ,  alpha =0.5 )
    axis = point.plot(ax = axis, cmap="YlOrRd", markersize =30 , alpha =0.5  )
    axis = join_2.plot(ax = axis, cmap="YlOrRd", scheme= "QUANTILES", k=30, markersize =30, column = "count", alpha =0.5 )
    axis.axis('off')


    # cx.add_basemap(axis, source=cx.providers.Stamen.TonerLite)

    

    # plt.show()
    # figure = plt.gcf() # get current figure
    # figure.set_size_inches(4, 5)
    foto = '{}static/img/img_mapas/mapa.png'.format(filtro[15])
    plt.savefig(foto,format="png", transparent=True, dpi = 100)
