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

import time



#funcion para la creacin de rutas

def rutas_mapas(filtro):
    unidades = [("DIV01","DIV1"),("DIV02","DIV2"),("DIV03","DIV3"),("DIV04","DIV4"),("DIV05","DIV5"),("DIV06","DIV6"),("DIV07","DIV7"),("DIV08","DIV8"),("FUTCO","FUTCO"),("FUTOM","FUTCO")]
    ruta = filtro[15]
    unidad=""
    ruta_unidad=""

    for x in unidades:
        
        if x[0] == filtro[0]:
            unidad=x[1]
            ruta_unidad=x[0]

    if ruta_unidad == "FUTOM":
        ruta_unidad="FUTCO"


    if unidad !="":
        divi = '{}shappes/{}/{}.shp'.format(ruta, ruta_unidad,unidad)
    else:
        divi = '{}shappes/div_2025/DIV_RES_EJC_2025.shp'.format(ruta)

    municipios_div = '{}shappes/divisiones/div_mun.shp'.format(ruta)
    municipios = '{}shappes/MUNICIPIOS COLOMBIA/Export_Output_195.shp'.format(ruta)
    departamentos = '{}shappes/DEPARTA/Export_Output_7.shp'.format(ruta)

    
    return[divi, municipios_div, municipios, departamentos]

def mapa_general(dato, filtro):
    try:
  
        plt.rcParams["figure.figsize"] = (8, 10)
        
        #configuaracion de los datos 

   
        # print(asesinados)
        
        fichero =  rutas_mapas(filtro)
        divisiones = gpd.read_file(fichero[0])

        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=0.5,  color ="black", alpha =0.5)
        # axis = divisiones.plot(ax = axis, color ="silver", alpha = 0.5)

        divisiones_municipios = gpd.read_file(fichero[1])

        #graficacion de los municipios 
        municipios = gpd.read_file(fichero[2])
        departamentos = gpd.read_file(fichero[3])
        departamentos = departamentos.boundary
        axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)
   
        gaor=[]
        delco=[]
        eln=[]
        ant=[]
        dot=[]
        cap=[]
        cg=[]
        cs=[]
        pel=[]
        narc =[]
        otro=[]
        gdo=[]
        farc=[]

        gaor_var = "GAO - Residual Disidencias FARC"
        delco_var = "DELINCUENCIA"
        eln_var = "GAO ELN"
        ant_var = "Amenaza de Naturaleza Cibernetica"
        dot_var = "Delincuencia Organizada Transnacional"
        cap_var = "GAO CAPARROS"
        cg_var = "GAO CLAN DEL GOLFO"
        cs_var = "GAO COMUNEROS DEL SUR"
        pel_var = "GAO PELUSOS"
        narc_var = "NARCOTRÁFICO"
        gdo_var = "GDO"
        farc_var = "FARC"


        gaor = list(filter(lambda dato: str(gaor_var) == dato[8], dato))
        delco = list(filter(lambda dato: str(delco_var) == dato[8], dato))
        ant  = list(filter(lambda dato: str(ant_var) == dato[8], dato))
        dot  = list(filter(lambda dato: str(dot_var) == dato[8], dato))
        cap = list(filter(lambda dato: str(cap_var) == dato[8], dato))
        cg = list(filter(lambda dato: str(cg_var) == dato[8], dato))
        cs = list(filter(lambda dato: str(cs_var) == dato[8], dato))
        pel = list(filter(lambda dato: str(pel_var) == dato[8], dato))
        narc = list(filter(lambda dato: str(narc_var) == dato[8], dato))
        eln = list(filter(lambda dato: str(eln_var) == dato[8], dato))
        gdo = list(filter(lambda dato: str(gdo_var) == dato[8], dato))
        farc = list(filter(lambda dato: str(farc_var) == dato[8], dato))

        otro = list(filter(lambda dato: str(gaor_var) != dato[8], dato))
        otro = list(filter(lambda otro: str(delco_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(ant_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(dot_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cap_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cg_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cs_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(pel_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(narc_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(eln_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(gdo_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(farc_var) != otro[8], otro))

        if farc:
            lab_cocaina = gpd.GeoDataFrame(farc)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#130101", markersize =30, alpha = 0.5)
        if otro:
            lab_cocaina = gpd.GeoDataFrame(otro)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#101010", markersize =30, alpha = 0.5)
        if gaor:
            x = gpd.GeoDataFrame(gaor)
            x.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            x = gpd.GeoDataFrame(x, geometry = gpd.points_from_xy(x.longitud, x.latitud) )
            x = x.clip(divisiones)
            axis = x.plot(ax = axis, marker='d', color = "#130101", markersize =30)
        if eln:
            lab_cocaina = gpd.GeoDataFrame(eln)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#900c20", markersize =30)
        if ant:
            lab_cocaina = gpd.GeoDataFrame(ant)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#0c2290", markersize =30)
            
        if dot:
            lab_cocaina = gpd.GeoDataFrame(dot)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#0c9050", markersize =30)
                        
        if cap:
            lab_cocaina = gpd.GeoDataFrame(cap)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#3f4d46", markersize =30)
                        
        if cg:
            lab_cocaina = gpd.GeoDataFrame(cg)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#875858", markersize =30)
                                    
        if cs:
            lab_cocaina = gpd.GeoDataFrame(cs)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#f8be09", markersize =30)
                                    
        if pel:
            lab_cocaina = gpd.GeoDataFrame(pel)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#b49600", markersize =30)
                                    
        if narc:
            lab_cocaina = gpd.GeoDataFrame(narc)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#259000", markersize =30)

                                                
        if delco:
            lab_cocaina = gpd.GeoDataFrame(delco)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#008190", markersize =30)
        
        if gdo:
            lab_cocaina = gpd.GeoDataFrame(gdo)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#7c02fe", markersize =30)
                                                            



        axis.axis('off')

        axis.axis('off')
        imagen = '{}static/img/img_mapas/'.format(filtro[15])
        direccion = str(imagen)+str("filtro_dep")+str(".png")
  
        plt.savefig(direccion, transparent=True)


    except:
        plt.rcParams["figure.figsize"] = (8, 10)
        
        #configuaracion de los datos 


        #graficacionde las divisiones
        ruta = rutas_mapas(filtro)
        divisiones = gpd.read_file(ruta[0])
        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=1, color ="black", )

        divisiones_municipios = gpd.read_file(ruta[1])


        #graficacion de los municipios 
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        departamentos = departamentos.boundary
        axis = departamentos.plot(ax = axis, linewidth=0.3, color ="black", alpha =0.8)

        #agrupacion de los eventos 



        # axis =  municipios.plot(ax = axis)


        # if(dato_3 != "'-'"):

        #     axis = join_2.plot(ax = axis, color="grey", alpha =0.5 )

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
        direccion = str(imagen)+str("filtro_dep")+str(".png")
        # plt.savefig(imagen)
        plt.savefig(direccion, transparent=True)

    #funcion para filtrar mapas
def mapa_filtrado(dato, filtro):


        plt.rcParams["figure.figsize"] = (8, 10)
        #paramtro de tamaño del mapa
        ruta = rutas_mapas(filtro)
        divisiones = gpd.read_file(ruta[0])
        municipios = gpd.read_file(ruta[2])
        departamentos = gpd.read_file(ruta[3])
        
        
        divisiones = divisiones.set_crs(epsg=4686, allow_override=True)
        municipios = municipios.set_crs(epsg=4686, allow_override=True)
        departamentos = departamentos.set_crs(epsg=4686, allow_override=True)

        divisiones["perimetro"] = divisiones.boundary
        axis = divisiones["perimetro"].plot( linewidth=1.5, color ="black", )

        departamentos["perimetro"] = departamentos.boundary
        municipios["perimetro"] = municipios.boundary
        axis = municipios["perimetro"].plot(ax = axis, linewidth=1.5, color ="black", )

        #configuaracion de los datos 

        dato_nuevo=[]
        for x in dato:
            if x[2]=="FUTOM":
                x = list(x)
                x[2]="FUTCO"
                x =tuple(x)
                dato_nuevo.append(x)

        if dato_nuevo !=[]:
            dato = dato_nuevo
        
        di = gpd.GeoDataFrame(dato)
        di.rename(columns={0:'hecho', 1:"fecha_hecho", 2:"agr_div", 3:"division", 4:"brigada", 5:"unidad" , 6:"dpto", 7:"mpio", 8:"enemigo", 9:"estrategia_afecta", 10:"hop_accion_davaa", 11:"hop_apoyo_blica", 12:"hop_apoyo_conat", 13:"hop_hecho_pos", 14:"cantidad", 15:"hop_operacion", 16:"latitud", 17:"longitud"}, inplace=True)


        point = gpd.GeoDataFrame(di, geometry = gpd.points_from_xy(di.longitud, di.latitud))
        point = point.set_crs(epsg=4686, allow_override=True)
        point = point.clip(divisiones)


        # #graficacion de los municipios 




        #agrupacion de los eventos 

        
        ponit_agrupados_div = point.groupby("agr_div")["agr_div"].agg(["count"])
        


        datos_colombia_div = divisiones.merge(ponit_agrupados_div, left_on="DIV", right_on = "agr_div" )

        # print(ponit_agrupados_dep)
        #join =  sjoin(municipios , point)
        join_1 =  sjoin(datos_colombia_div, divisiones)

        join_1 = join_1.boundary
 

 
        axis = join_1.plot(color ="darkred", alpha = 0.5)
 

        gaor=[]
        delco=[]
        eln=[]
        ant=[]
        dot=[]
        cap=[]
        cg=[]
        cs=[]
        pel=[]
        narc =[]
        otro=[]
        gdo=[]
        farc=[]

        gaor_var = "GAO - Residual Disidencias FARC"
        delco_var = "DELINCUENCIA"
        eln_var = "GAO ELN"
        ant_var = "Amenaza de Naturaleza Cibernetica"
        dot_var = "Delincuencia Organizada Transnacional"
        cap_var = "GAO CAPARROS"
        cg_var = "GAO CLAN DEL GOLFO"
        cs_var = "GAO COMUNEROS DEL SUR"
        pel_var = "GAO PELUSOS"
        narc_var = "NARCOTRÁFICO"
        gdo_var = "GDO"
        farc_var = "FARC"


        gaor = list(filter(lambda dato: str(gaor_var) == dato[8], dato))
        delco = list(filter(lambda dato: str(delco_var) == dato[8], dato))
        ant  = list(filter(lambda dato: str(ant_var) == dato[8], dato))
        dot  = list(filter(lambda dato: str(dot_var) == dato[8], dato))
        cap = list(filter(lambda dato: str(cap_var) == dato[8], dato))
        cg = list(filter(lambda dato: str(cg_var) == dato[8], dato))
        cs = list(filter(lambda dato: str(cs_var) == dato[8], dato))
        pel = list(filter(lambda dato: str(pel_var) == dato[8], dato))
        narc = list(filter(lambda dato: str(narc_var) == dato[8], dato))
        eln = list(filter(lambda dato: str(eln_var) == dato[8], dato))
        gdo = list(filter(lambda dato: str(gdo_var) == dato[8], dato))
        farc = list(filter(lambda dato: str(farc_var) == dato[8], dato))

        otro = list(filter(lambda dato: str(gaor_var) != dato[8], dato))
        otro = list(filter(lambda otro: str(delco_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(ant_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(dot_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cap_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cg_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(cs_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(pel_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(narc_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(eln_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(gdo_var) != otro[8], otro))
        otro = list(filter(lambda otro: str(farc_var) != otro[8], otro))

        if farc:
            lab_cocaina = gpd.GeoDataFrame(farc)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#130101", markersize =30, alpha = 0.5)
        if otro:
            lab_cocaina = gpd.GeoDataFrame(otro)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#101010", markersize =30, alpha = 0.5)
        if gaor:
            x = gpd.GeoDataFrame(gaor)
            x.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            x = gpd.GeoDataFrame(x, geometry = gpd.points_from_xy(x.longitud, x.latitud) )
            x = x.clip(divisiones)
            axis = x.plot(ax = axis, marker='d', color = "#130101", markersize =30)
        if eln:
            lab_cocaina = gpd.GeoDataFrame(eln)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#900c20", markersize =30)
        if ant:
            lab_cocaina = gpd.GeoDataFrame(ant)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#0c2290", markersize =30)
            
        if dot:
            lab_cocaina = gpd.GeoDataFrame(dot)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#0c9050", markersize =30)
                        
        if cap:
            lab_cocaina = gpd.GeoDataFrame(cap)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#3f4d46", markersize =30)
                        
        if cg:
            lab_cocaina = gpd.GeoDataFrame(cg)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#875858", markersize =30)
                                    
        if cs:
            lab_cocaina = gpd.GeoDataFrame(cs)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#f8be09", markersize =30)
                                    
        if pel:
            lab_cocaina = gpd.GeoDataFrame(pel)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#b49600", markersize =30)
                                    
        if narc:
            lab_cocaina = gpd.GeoDataFrame(narc)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#259000", markersize =30)

                                                
        if delco:
            lab_cocaina = gpd.GeoDataFrame(delco)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#008190", markersize =30)
        
        if gdo:
            lab_cocaina = gpd.GeoDataFrame(gdo)
            lab_cocaina.rename(columns={16:"latitud", 17:"longitud"}, inplace=True)
            lab_cocaina = gpd.GeoDataFrame(lab_cocaina, geometry = gpd.points_from_xy(lab_cocaina.longitud, lab_cocaina.latitud) )
            lab_cocaina = lab_cocaina.clip(divisiones)
            axis = lab_cocaina.plot(ax = axis, marker='d', color = "#7c02fe", markersize =30)
                                                            
        axis.axis('off')

        #plt.show()

        if filtro[0] == "FUTOM":
            unidad = "FUTCO"
        else:
            unidad = filtro[0]

        foto = '{}static/img/img_mapas/{}.png'.format(filtro[15],unidad)
        plt.savefig(foto,format="png", transparent=True, dpi = 100)


