# El presente modulo es para el manejo de la estadística de la Dirección de operaciones del Ejército Nacional 
from tipo_docker.a_p_res_mineria_nuew.models.conexion_pos import Databa_bases
from tipo_docker.z_z_z_funtions.funciones import *
from tipo_docker.z_z_z_funtions.tablas_global import *
from tipo_docker.a_p_res_mineria_nuew.models.funtions.componest.tablas import *
from tipo_docker.a_p_res_mineria_nuew.maps.funciones.mapa_filtro import *
conexion_pos = Databa_bases()

import pandas as pd
class Calculo_Spoa:
    def __init__(self, filtro=None, fecha_anio=None, ruta=None, mes=None,fecha_anio_actual=None, pdf=None, permisos=None ):
        self.fecha_inicial, self.fecha_final, self.fecha_inicial_anterior, self.fecha_final_anterior = filtro
        self.filtro = "sin_spoa"
        self.filtros = ["", "", ""]
        self.fecha_anio = fecha_anio
        self.fecha_anio_actual = fecha_anio_actual
        self.mes = mes
        self.pdf = pdf
        self.ruta = permisos[15]
        self.permisos = permisos
        

        self.filtros = selecion_filtro(self.permisos)

        # Función interna para evitar duplicación
        def obtener_resultados(fecha_ini, fecha_fin):
            query_res, query_hechos, erradicacion = parametros(fecha_ini, fecha_fin, self.filtros, permisos)
            resultados = conexion_pos.comando_query(query_res)
            hechos = conexion_pos.comando_query(query_hechos)
            
            return estadistica_resultados_mineria_global(resultados, hechos)

        # Cálculos actuales y anteriores
        self.resultados_mineria = obtener_resultados(self.fecha_inicial, self.fecha_final)
        self.resultados_mineria_anterior = obtener_resultados(self.fecha_inicial_anterior, self.fecha_final_anterior)
                
        def obtener_resultados_por_anio(anio):
            query_hechos = f"""
                SELECT * FROM view_hechos_materializados
                WHERE DATE_PART('year', fecha_hecho) = {anio}
                ORDER BY fecha_hecho ASC;
            """
            query_resultados = f"""
                SELECT * FROM view_resultados_materializados
                WHERE DATE_PART('year', hop_fecha_hecho) = {anio}
                ORDER BY hop_fecha_hecho ASC;
            """
            hechos = conexion_pos.comando_query(query_hechos)
            resultados = conexion_pos.comando_query(query_resultados)
            return estadistica_resultados_mineria_global(resultados, hechos)
        self.res_anterior = obtener_resultados_por_anio(self.fecha_anio)

        query_relementos = """
            SELECT variable, valor_cop FROM valor_material;
        """
        self.variable = conexion_pos.comando_query(query_relementos)

        query_valor_dolar = """
            SELECT valor_usd, fecha_cotizacion
            FROM valor_dolar
            WHERE fecha_cotizacion = (
                SELECT MAX(fecha_cotizacion) FROM valor_dolar
            );
        """
        resultado = conexion_pos.comando_query(query_valor_dolar)

        # Asegurar que haya resultado
        if resultado and len(resultado) > 0:
            self.valor_dolar = resultado[0][0]
            self.fecha_dolar = resultado[0][1]
        else:
            self.valor_dolar = None
            self.fecha_dolar = None


        # Extraer solo los nombres de las variables (materiales)
        self.materiales = [x[0] for x in self.variable]

        # Preparar la lista de materiales para la cláusula SQL IN
        # (Asegura que los elementos se conviertan a formato SQL válido)
        materiales_str = ", ".join([f"'{m}'" for m in self.materiales])

        # Construir la consulta principal
        query_resultados_valor = f"""
            SELECT *
            FROM view_resultados_materializados
            WHERE res_clase IN ({materiales_str})
            AND hop_fecha_hecho >= '{self.fecha_inicial}'
            AND hop_fecha_hecho <= '{self.fecha_final}'
            ORDER BY hop_fecha_hecho ASC;
        """

        # Ejecutar la consulta
        self.valor_material = conexion_pos.comando_query(query_resultados_valor)


        # Construir la consulta principal
        query_resultados_valor_ant = f"""
            SELECT *
            FROM view_resultados_materializados
            WHERE res_clase IN ({materiales_str})
            AND hop_fecha_hecho >= '{self.fecha_inicial_anterior}'
            AND hop_fecha_hecho <= '{self.fecha_final_anterior}'
            ORDER BY hop_fecha_hecho ASC;
        """

        # Ejecutar la consulta
        self.valor_material_ant = conexion_pos.comando_query(query_resultados_valor_ant)
 
        
    def validar_spoa_unidad(self, filtro, res_calculo, numero, validar):
        spoa=[]
        no_spoa=[]
        
        if validar == "SI":
            
            startdate = pd.to_datetime("2024-06-04").date()
            # startdate = pd.to_datetime("2024-01-01").date()
            
            if filtro == "sin_spoa" or filtro == "res_sin_spoa" :
                for x in res_calculo[numero]:
                    if x[0] >= startdate:

                        # if x[29] =="-" or  x[29] =="" or  x[29] =="0":
                        if x[29] =="-" or  x[29] =="" or len(x[29]) != 21 or  x[29] =="0":
                            no_spoa.append(x)
                            # print(x[29])
                        else: 
                            numero_dep = x[29][0:5]
                                
                            # if numero_dep == "00000":
                            #     no_spoa.append(x)
                            # else:
                            #     spoa.append(x)
                            spoa.append(x)

                    else: 
                        spoa.append(x)      
            else:
                spoa =  res_calculo[numero]

                

            spoa = spoa
        else:
            spoa =  res_calculo[numero]

        if filtro == "res_sin_spoa":
                    # print(len(no_spoa))
                    spoa = no_spoa
        #DOCUMENTOS SIN SPOA

        return[spoa, no_spoa]

    def validar_spoa(self, filtro, res_calculo, numero, nombre, validar):
        spoa=[]
        no_spoa=[]
        
        startdate = pd.to_datetime("2024-06-04").date()
        # startdate = pd.to_datetime("2024-01-01").date()
        
        if filtro[16] == "sin_spoa" or filtro[16] == "res_sin_spoa" :
            for x in res_calculo[numero]:
        
                if x[0] >= startdate:

                    if x[29] =="-" or  x[29] =="" or  x[29] =="0":
                    # if x[29] =="-" or  x[29] =="" or len(x[29]) != 21 or  x[29] =="0":
                        no_spoa.append(x)
                        # print(x[29])
                    else: 
                        numero_dep = x[29][0:5]
                            
                        # if numero_dep == "00000":
                        #     no_spoa.append(x)
                        # else:
                        #     spoa.append(x)
                        spoa.append(x)

                else: 
                    spoa.append(x)      
        else:
            spoa =  res_calculo[numero]

        if filtro[16]== "res_sin_spoa":
                    # print(len(no_spoa))
                    spoa = no_spoa
        #DOCUMENTOS SIN SPOA

        
        # f.write(str(nombre)+"\n")
        # f.write("-----------------------------------------------------"+"\n")
        
        numero_id = 1
        

        # f.write("-----------------------------------------------------"+"\n")
        # f.write(str(numero_id-1)+" Resultados sin SPOA"+"\n")

        if validar == "SI":
            spoa = spoa
        else:
            spoa =  res_calculo[numero]
            

        return[spoa, no_spoa]


    #funcion de para generar estadistica mineria 
    def resultados_mineria_boletin(self, fecha_inicial_u_l, fecha_final_u_l, filtro, pdf):
        
        dato =""

        filtros = selecion_filtro(filtro)

        query = parametros(fecha_inicial_u_l, fecha_final_u_l, filtros, filtro) #querys modificados

        resultados = conexion_pos.comando_query(query[0]) #resultados de la base de datos
        hechos = conexion_pos.comando_query(query[1]) #resultados de la base de datos
        erradicacion = conexion_pos.comando_query(query[2]) #resultados de la base de datos
        res_calculo = estadistica_resultados_mineria(resultados, hechos, filtro)

        datos = [res_calculo[33], res_calculo[35], res_calculo[40], res_calculo[38], res_calculo[39], res_calculo[36], res_calculo[37], res_calculo[41], res_calculo[59], res_calculo[60], res_calculo[65]]

        
        datos_prueba = [res_calculo[0], res_calculo[1], res_calculo[2], res_calculo[3], res_calculo[4], res_calculo[7], res_calculo[8], res_calculo[9], res_calculo[16], res_calculo[17], res_calculo[35], res_calculo[41], res_calculo[36], res_calculo[37], res_calculo[38], res_calculo[39], res_calculo[21], res_calculo[22], res_calculo[23], res_calculo[24], res_calculo[25]]

        #encabezado de interdicion
        encabezado_tabla_resultados_mapa(pdf, "RESULTADOS MINERÍA ILEGAL ")
        pdf.ln(10)
        valor = Calculo_Spoa.validar_spoa_unidad(self, filtro, res_calculo, 33,  "SI") #funcion para filtar el spoa
        tabla_resultados_con_mapa(pdf,"Capturas",valor[0], "Personas",18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Yacimientos Mineros ",datos[1], "Unidades", 14)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Unidad Producción Minera",datos[2], "Galones", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Maquinaria Pesada ",datos[3], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Tractor Con Uruga ",datos[4], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Excavadoras",datos[5], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Retroexcavadoras",datos[6], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Dragas",datos[7], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Motores",datos[8], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Combustibles",datos[9], "Unidades", 18)
        pdf.ln()
        tabla_resultados_con_mapa(pdf,"Coltan",datos[10], "Kilos", 18)

        nombre = "mineria"
        # mapa_hechos_p(datos_prueba, nombre, filtro)
        # mapa_hechos(hechos, nombre, filtro)
        mapa_hechos(datos[1], nombre, filtro)
        
        
        
        contrabando  = '{}static/img/img_mapas/{}.png'.format(filtro[15],nombre)
        convecion_artmisa_fondo  = '{}static/img/img_mapas/{}_fondo.png'.format(filtro[15],nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(filtro[15])
        pdf.image(convecion_artmisa_fondo,13,18.7,162.1,199)
        pdf.image(contrabando,-8,5,180,220)
        pdf.image(rosa_nautica,120, 60, 25, 25)

    def dinamico(self):
        """
        Calcula valores dinámicos para los hexágonos del tablero minero.
        Usa los resultados preprocesados en self.resultados_mineria.
        Devuelve una lista con los 7 hexágonos (idéntico formato al original).
        """

        # === Extracción de valores optimizada ===
        # Usamos una función auxiliar con manejo seguro
        # --- Función auxiliar genérica ---
        def total(origen, idx, col):
            try:
                return calculo_total_sin_filtro(origen[idx], col)
            except Exception:
                return 0

        # --- Datos actuales ---
        dragas = total(self.resultados_mineria, 8, 18)
        upm = total(self.resultados_mineria, 7, 18)
        maquinaria_pesada = total(self.resultados_mineria, 5, 18)
        operaciones = total(self.resultados_mineria, 2, 14)
        motores = total(self.resultados_mineria, 9, 18)
        dragones = total(self.resultados_mineria, 17, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria, 0, "SI")
            capturas = total(valor, 0, 18)
        except Exception:
            capturas = 0

        # --- Hexágonos ---
        exagono = [
            {"id": "06", "numero": "06", "cantidad": dragas, "titulo": "DRAGAS", "color": "color-6", "fila": 1, "icono": "bi bi-fan"},
            {"id": "01", "numero": "01", "cantidad": upm, "titulo": "UPM", "color": "color-1", "fila": 1, "icono": "bi bi-minecart-loaded"},
            {"id": "05", "numero": "05", "cantidad": maquinaria_pesada, "titulo": "MAQUINARIA<br>PESADA", "color": "color-5", "fila": 2, "icono": "bi bi-truck-flatbed"},
            {"id": "CENTRAL", "numero": "", "cantidad": operaciones, "titulo": "OPERACIONES", "color": "central-content", "fila": 2, "icono": "bi bi-yelp"},
            {"id": "02", "numero": "02", "cantidad": motores, "titulo": "MOTORES<br>MOTOBOMBAS", "color": "color-2", "fila": 2, "icono": "bi bi-gear-fill"},
            {"id": "04", "numero": "04", "cantidad": dragones, "titulo": "DRAGONES", "color": "color-4", "fila": 3, "icono": "bi bi-perplexity"},
            {"id": "03", "numero": "03", "cantidad": capturas, "titulo": "CAPTURAS", "color": "color-3", "fila": 3, "icono": "bi bi-person"},
        ]

        # --- Datos del año anterior ---
        dragas_anio = total(self.res_anterior, 8, 18)
        upm_anio = total(self.res_anterior, 7, 18)
        maquinaria_pesada_anio = total(self.res_anterior, 5, 18)
        operaciones_anio = total(self.res_anterior, 2, 14)
        motores_anio = total(self.res_anterior, 9, 18)
        dragones_anio = total(self.res_anterior, 17, 18)
        motobomba_anio = total(self.res_anterior, 21, 18)
        carbon_anio = total(self.res_anterior, 22, 18)
        combustibles_mineria_anio = total(self.res_anterior, 10, 18)
        oro_anio = total(self.res_anterior, 18, 18)
        mercurio_anio = total(self.res_anterior, 19, 18)
        coltan_anio = total(self.res_anterior, 23, 18)
        planta_electrica_anio = total(self.res_anterior, 24, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_anterior, 0, "SI")
            capturas_anio = total(valor, 0, 18)
        except Exception:
            capturas_anio = 0


        # --- Datos  anterior  ---
        dragas_anterior = total(self.resultados_mineria_anterior, 8, 18)
        upm_anterior = total(self.resultados_mineria_anterior, 7, 18)
        maquinaria_pesada_anterior = total(self.resultados_mineria_anterior, 5, 18)
        operaciones_anterior = total(self.resultados_mineria_anterior, 2, 14)
        motores_anterior = total(self.resultados_mineria_anterior, 9, 18)
        dragones_anterior = total(self.resultados_mineria_anterior, 17, 18)
        motobomba_anterior = total(self.resultados_mineria_anterior, 21, 18)
        carbon_anterior = total(self.resultados_mineria_anterior, 22, 18)
        combustibles_mineria_anterior = total(self.resultados_mineria_anterior, 10, 18)
        oro_anterior = total(self.resultados_mineria_anterior, 18, 18)
        mercurio_anterior = total(self.resultados_mineria_anterior, 19, 18)
        coltan_anterior = total(self.resultados_mineria_anterior, 23, 18)
        planta_electrica_anterior = total(self.resultados_mineria_anterior, 24, 18)
 
        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria_anterior, 0, "SI")
            capturas_anterior = total(valor, 0, 18)
        except Exception:
            capturas_anterior = 0
            
        # --- Datos  actual  ---
        dragas_actual = total(self.resultados_mineria, 8, 18)
        upm_actual = total(self.resultados_mineria, 7, 18)
        maquinaria_pesada_actual = total(self.resultados_mineria, 5, 18)
        operaciones_actual = total(self.resultados_mineria, 2, 14)
        motores_actual = total(self.resultados_mineria, 9, 18)
        dragones_actual = total(self.resultados_mineria, 17, 18)
        motobomba_actual = total(self.resultados_mineria, 21, 18)
        carbon_actual = total(self.resultados_mineria, 22, 18)
        combustibles_mineria_actual = total(self.resultados_mineria, 10, 18)
        oro_actual = total(self.resultados_mineria, 18, 18)
        mercurio_actual = total(self.resultados_mineria, 19, 18)
        coltan_actual = total(self.resultados_mineria, 23, 18)
        planta_electrica_actual = total(self.resultados_mineria, 24, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria, 0, "SI")
            capturas_actual = total(valor, 0, 18)
        except Exception:
            capturas_actual = 0

        # --- Resumen comparativo ---
        
        valor = 0



        for x in self.variable:
            for y in self.valor_material:
                if x[0]==y[12]:
                    valor = valor + (y[18]*float(x[1]))


        valor_ant = 0
        
        for x in self.variable:
            for y in self.valor_material_ant:
                if x[0]==y[12]:
                    valor_ant = valor_ant + (y[18]*float(x[1]))

        cuadros_exagono = {
                    "valor_maquinaria": {
                        "cop": valor,
                        "usd": valor/float(self.valor_dolar)
                    },
                    "valor_economia": {
                        "cop": (valor*0.10),
                        "usd": (valor/float(self.valor_dolar)*0.10)
                    },
                    "detalles": {
                        "mercurio": mercurio_actual,
                        "combustible": combustibles_mineria_actual,
                        "oro": oro_actual,
                        "hectareas": 0
                    },
                    "trm": {
                        "valor": self.valor_dolar,
                        "fecha": self.fecha_dolar
                    },
                    "valor_maquinaria_anterior": {
                        "cop": valor_ant,
                        "usd": valor_ant*float(self.valor_dolar)
                    },
                    
                }

        datos = [
        {
            'icono': 'bi-bullseye',
            'nombre': 'OPERACIONES',
            'total2024': operaciones_anio,
            'oct2024': operaciones_anterior,
            'oct2025': operaciones_actual,
            'diarioCV': porcentajes(operaciones_anterior, operaciones_actual, 1),
            'diarioCVUp':  calcular_direccion(operaciones_actual, operaciones_anterior),
            'anualCV': porcentajes(operaciones_anio, operaciones_actual, 1),
            'anualCVUp': calcular_direccion(operaciones_actual, operaciones_anio)
        },
        {
            'icono': 'bi-truck-flatbed',
            'nombre': 'MAQUINARIA PESADA (DESTRUIDA Y/O INCAUTADA)',
            'total2024': maquinaria_pesada_anio,
            'oct2024': maquinaria_pesada_anterior,
            'oct2025': maquinaria_pesada_actual,
            'diarioCV': porcentajes(maquinaria_pesada_anterior, maquinaria_pesada_actual, 1),
            'diarioCVUp':  calcular_direccion(maquinaria_pesada_actual, maquinaria_pesada_anterior),
            'anualCV': porcentajes(maquinaria_pesada_anio, maquinaria_pesada_actual, 1),
            'anualCVUp':  calcular_direccion(maquinaria_pesada_actual, maquinaria_pesada_anio)
        },
        {
            'icono': 'bi-droplet-half',
            'nombre': 'DRAGAS',
            'total2024': dragas_anio,
            'oct2024': dragas_anterior,
            'oct2025': dragas_actual,
            'diarioCV': porcentajes(dragas_anterior, dragas_actual, 1),
            'diarioCVUp':  calcular_direccion(dragas_actual, dragas_anterior),
            'anualCV': porcentajes(dragas_anio, dragas_actual, 1),
            'anualCVUp': calcular_direccion(dragas_actual, dragas_anio)
        },
        {
            'icono': 'bi-rocket-takeoff',
            'nombre': 'DRAGONES BRASILEÑO',
            'total2024': dragones_anio,
            'oct2024': dragones_anterior,
            'oct2025': dragones_actual,
            'diarioCV': porcentajes(dragones_anterior, dragones_actual, 1),
            'diarioCVUp':  calcular_direccion(dragones_actual, dragones_anterior),
            'anualCV': porcentajes(dragones_anio, dragones_actual, 1),
            'anualCVUp':  calcular_direccion(dragones_actual, dragones_anio)
        },
                
                
        {
            'icono': 'bi-bullseye',
            'nombre': 'CAPTURAS PERS',
            'total2024': capturas_anio,
            'oct2024': capturas_anterior,
            'oct2025': capturas_actual,
            'diarioCV': porcentajes(capturas_anterior, capturas_actual, 1),
            'diarioCVUp':  calcular_direccion(capturas_actual, capturas_anterior),
            'anualCV': porcentajes(capturas_anio, capturas_actual, 1),
            'anualCVUp': calcular_direccion(capturas_actual, capturas_anio)
        },
        {
            'icono': 'bi-truck-flatbed',
            'nombre': 'MOTORES UND',
            'total2024': motores_anio,
            'oct2024': motores_anterior,
            'oct2025': motores_actual,
            'diarioCV': porcentajes(motores_anterior, motores_actual, 1),
            'diarioCVUp':  calcular_direccion(motores_actual, motores_anterior),
            'anualCV': porcentajes(motores_anio, motores_actual, 1),
            'anualCVUp': calcular_direccion(motores_actual, motores_anio)
        },
        {
            'icono': 'bi-droplet-half',
            'nombre': 'MOTOBOMBAS',
            'total2024': motobomba_anio,
            'oct2024': motobomba_anterior,
            'oct2025': motobomba_actual,
            'diarioCV': porcentajes(motobomba_anterior, motobomba_actual, 1),
            'diarioCVUp':  calcular_direccion(motobomba_actual, motobomba_anterior),
            'anualCV': porcentajes(motobomba_anio, motobomba_actual, 1),
            'anualCVUp':  calcular_direccion(motobomba_actual, motobomba_anio)
        },
        {
            'icono': 'bi-rocket-takeoff',
            'nombre': 'UPM UND',
            'total2024': upm_anio,
            'oct2024': upm_anterior,
            'oct2025': upm_actual,
            'diarioCV': porcentajes(upm_anterior, upm_actual, 1),
            'diarioCVUp': calcular_direccion(upm_actual, upm_anterior),
            'anualCV': porcentajes(upm_anio, upm_actual, 1),
            'anualCVUp': calcular_direccion(upm_actual, upm_anio)
        },     
        {
            'icono': 'bi-bullseye',
            'nombre': 'CARBÓN TN',
            'total2024': carbon_anio,
            'oct2024': carbon_anterior,
            'oct2025': carbon_actual,
            'diarioCV': porcentajes(carbon_anterior, carbon_actual, 1),
            'diarioCVUp':  calcular_direccion(carbon_actual, carbon_anterior),
            'anualCV': porcentajes(carbon_anio, carbon_actual, 1),
            'anualCVUp': calcular_direccion(carbon_actual, carbon_anio)
        },
        
        {
            'icono': 'bi-truck-flatbed',
            'nombre': 'MERCURIO KG',
            'total2024': mercurio_anio,
            'oct2024': mercurio_anterior,
            'oct2025': mercurio_actual,
            'diarioCV': porcentajes(mercurio_anterior, mercurio_actual, 1),
            'diarioCVUp': calcular_direccion(mercurio_actual, mercurio_anterior),
            'anualCV': porcentajes(mercurio_anio, mercurio_actual, 1),
            'anualCVUp': calcular_direccion(mercurio_actual, mercurio_anio)
        },
        {
            'icono': 'bi-droplet-half',
            'nombre': 'COMBUSTIBLE GLN',
            'total2024': combustibles_mineria_anio,
            'oct2024': combustibles_mineria_anterior,
            'oct2025': combustibles_mineria_actual,
            'diarioCV': porcentajes(combustibles_mineria_anterior, combustibles_mineria_actual, 1),
            'diarioCVUp': calcular_direccion(combustibles_mineria_actual, combustibles_mineria_anterior),
            'anualCV': porcentajes(combustibles_mineria_anio, combustibles_mineria_actual, 1),
            'anualCVUp': calcular_direccion(combustibles_mineria_actual, combustibles_mineria_anio)
        },
        {
            'icono': 'bi-rocket-takeoff',
            'nombre': 'ORO KG ',
            'total2024': oro_anio,
            'oct2024': oro_anterior,
            'oct2025': oro_actual,
            'diarioCV': porcentajes(oro_anterior, oro_actual, 1),
            'diarioCVUp': calcular_direccion(oro_actual, oro_anterior),
            'anualCV': porcentajes(oro_anio, oro_actual, 1),
            'anualCVUp': calcular_direccion(oro_actual, oro_anio)
        },{
            'icono': 'bi-rocket-takeoff',
            'nombre': 'TIERRAS RARAS (COLTAN)',
            'total2024': coltan_anio,
            'oct2024': coltan_anterior,
            'oct2025': coltan_actual,
            'diarioCV': porcentajes(coltan_anterior, coltan_actual, 1),
            'diarioCVUp': calcular_direccion(coltan_actual, coltan_anterior),
            'anualCV': porcentajes(coltan_anio, coltan_actual, 1),
            'anualCVUp': calcular_direccion(coltan_actual, coltan_anio)
        },{
            'icono': 'bi-rocket-takeoff',
            'nombre': 'PLANTA ELECTRICA',
            'total2024': planta_electrica_anio,
            'oct2024': planta_electrica_anterior,
            'oct2025': planta_electrica_actual,
            'diarioCV': porcentajes(planta_electrica_anterior, planta_electrica_actual, 1),
            'diarioCVUp': calcular_direccion(planta_electrica_actual, planta_electrica_anterior),
            'anualCV': porcentajes(planta_electrica_anio, planta_electrica_actual, 1),
            'anualCVUp': calcular_direccion(planta_electrica_actual, planta_electrica_anio)
        },
        ]

        return [exagono, datos, cuadros_exagono, self.resultados_mineria[2]]


        #print(self.hechos)

    def resultados_mapamineria(self):
        nombre = "mineria_mapa"
        mapa_hechos(self.resultados_mineria[2], nombre, self.ruta)
        mineria  = '{}static/img/img_mapas/{}.png'.format(self.ruta,nombre)

        rosa_nautica = '{}static/img/img_mapas/rosa_nautica_2024_new.png'.format(self.ruta)
    
        self.pdf.image(mineria,-10,30,150,180)
        self.pdf.image(rosa_nautica,120, 60, 25, 25)

        """
        Calcula valores dinámicos para los hexágonos del tablero minero.
        Usa los resultados preprocesados en self.resultados_mineria.
        Devuelve una lista con los 7 hexágonos (idéntico formato al original).
        """

        # === Extracción de valores optimizada ===
        # Usamos una función auxiliar con manejo seguro
        # --- Función auxiliar genérica ---
        def total(origen, idx, col):
            try:
                return calculo_total_sin_filtro(origen[idx], col)
            except Exception:
                return 0

        # --- Datos actuales ---
        dragas = total(self.resultados_mineria, 8, 18)
        upm = total(self.resultados_mineria, 7, 18)
        maquinaria_pesada = total(self.resultados_mineria, 5, 18)
        operaciones = total(self.resultados_mineria, 2, 14)
        motores = total(self.resultados_mineria, 9, 18)
        dragones = total(self.resultados_mineria, 17, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria, 0, "SI")
            capturas = total(valor, 0, 18)
        except Exception:
            capturas = 0

        # --- Hexágonos ---
        self.pdf.set_text_color(0,0,0)

        

        combustibles_mineria_actual = total(self.resultados_mineria, 10, 18)
        oro_actual = total(self.resultados_mineria, 18, 18)
        mercurio_actual = total(self.resultados_mineria, 19, 18)
        valor = 0
        for x in self.variable:
            for y in self.valor_material:
                if x[0]==y[12]:
                    valor = valor + (y[18]*float(x[1]))


        def exagono( x, y, texto, texto_2):
            """
            Dibuja texto centrado dentro de un hexágono.
            :param x: posición X del centro del hexágono
            :param y: posición Y del centro del hexágono
            :param texto: texto principal
            :param texto_2: texto secundario
            """
            # Texto principal
            self.pdf.set_text_color(40,40,40)
            self.pdf.set_font('Arial', 'B', 14)
            ancho_texto = self.pdf.get_string_width(texto)
            self.pdf.text(x - ancho_texto / 2, y, texto)

            # Texto secundario (debajo)
            self.pdf.set_font('Arial', '', 10)
            ancho_texto_2 = self.pdf.get_string_width(texto_2)
            self.pdf.text(x - ancho_texto_2 / 2, y + 5, texto_2)

        
        def position_triangulo(y,x, color, datos):
            triangle=[(y, x), (y+21, x+13), (y-21, x+13)]

            # Hexágono con puntas redondeadas
            self.pdf.set_fill_color(150, 150, 150)
            self.pdf.draw_hexagon_rounded(y+1, x+23, 23, radius=3, style='F')
            self.pdf.set_fill_color(255, 255, 255)
            self.pdf.draw_hexagon_rounded(y, x+22, 22, radius=3, style='F')
            self.pdf.set_draw_color(color[0], color[1], color[2])
            self.pdf.set_fill_color(color[0], color[1], color[2])
            self.pdf.polygon_rounded(triangle, radius=4, style='F')
            self.pdf.draw_circle(y, x+13, 7, style='F')
            self.pdf.set_font('Arial', 'B', 14)
            self.pdf.set_text_color(255,255,255)
            self.pdf.text((y-3),(x+15), str(datos[0]))
            exagono(y, x+27, datos[1],datos[2])
            
            img  = '{}static/img/resultados/{}.jpg'.format(self.ruta, datos[3])
            self.pdf.image(img,y-2,x+34,7,7)

        
        datos = ["06",dragas,"DRAGAS", "dragas"]
        position_triangulo(175,68, [6, 60, 43],datos)
        datos = ["01", upm, "UPM", "upm"]
        position_triangulo(218,68, [137, 199, 183],datos)
        datos = ["02", motores, "MOTORES", "combate_rs"]
        position_triangulo(240,105, [224, 224, 191],datos)
        datos = ["03", capturas, "CAPTURAS", "capturas"]
        position_triangulo(218,140, [107, 73, 56],datos)
        datos = ["04", dragones, "DRAGONES", "dragas"]
        position_triangulo(175,140, [186, 9, 34],datos)
        datos = ["05", maquinaria_pesada, "MAQ. PESADA", "maquinaria"]
        position_triangulo(155,105, [88, 127, 90],datos)
        
        self.pdf.set_line_width(1)
        self.pdf.set_draw_color(140, 140, 140)
        self.pdf.draw_hexagon_rounded(197, 105+23, 22, radius=3, style='D')
        exagono(197, 127, operaciones, "OPERACIONES")

        img  = '{}static/img/{}.png'.format(self.ruta, "jemop")
        #self.pdf.image(img, 280,60,30,30)
        self.pdf.set_fill_color(94, 119, 89)
        self.pdf.rounded_rect(265, 45, 60, 145, 1,'D', '1234')


        # Datos del rectángulo
        x_rect = 265
        y_rect = 45
        ancho_rect = 60
        def safe_float(value, default=0.0):
            """
            Convierte valor a float de forma segura.
            Maneja casos: '-', '', None, 'N/A', '5,430', etc.
            """
            if value is None:
                return default

            if isinstance(value, (int, float)):
                return float(value)

            value = str(value).strip()

            if value in ("", "-", "N/A", "NA", "None"):
                return default

            # quitar separadores de miles
            value = value.replace(",", "")

            try:
                return float(value)
            except Exception:
                return default

        # Lista de líneas con formato (texto, estilo)
        lineas = [
            ("Valor aproximado de la", ''),              # normal
            ("maquinaria inutilizada y/o", ''),          # normal
            ("incautada:", ''),                          # normal
            ("", ''),                                    # espacio visual

            (f"COP $ {valor:,.0f}", 'B'),                 # negrita
            (f"USD $ {valor / safe_float(self.valor_dolar):,.2f}", 'B'),

            ("", ''),                                    # espacio visual
            ("Valor Aproximado dejado de", ''),          # normal
            ("percibir por esta economía Ilícita.", ''), # normal

            (f"COP $ {(valor*0.10):,.0f}", 'B'),
            (f"USD $ {(valor / safe_float(self.valor_dolar) * 0.10):,.2f}", 'B'),

            ("", ''),

            ("Incautación mercurio :", ''),                                    
            (f"{safe_float(mercurio_actual):,.0f} Kg", 'B'),

            ("Incautación Combustible :", ''),                                    
            (f"{safe_float(combustibles_mineria_actual):,.0f} Gal", 'B'),

            ("Incautación de Oro", ''),                                    
            (f"{safe_float(oro_actual):,.0f} Kg", 'B'),

            ("Hectáreas Intervenidas", ''),                                    
            (f"{safe_float(0):,.0f}", 'B'),

            ("", ''),

            (f"Valor USD $ {safe_float(self.valor_dolar):,.2f}", 'B'),
            (f"Fecha: {self.fecha_dolar}", ''),
        ]



        # Altura inicial
        y_text = y_rect + 10
        line_height = 6  # separación entre líneas

        for texto, estilo in lineas:
            if not texto:
                y_text += line_height
                continue

            # Configurar fuente según estilo
            self.pdf.set_font('Arial', estilo, 10)

            # Calcular centrado horizontal
            ancho_texto = self.pdf.get_string_width(texto)
            x_centrada = x_rect + (ancho_rect - ancho_texto) / 2

            # Dibujar texto
            self.pdf.text(x_centrada, y_text, texto)
            y_text += line_height


    def resultados_cuadro_mineria(self):

        # === Extracción de valores optimizada ===
        # Usamos una función auxiliar con manejo seguro
        # --- Función auxiliar genérica ---
        def total(origen, idx, col):
            try:
                return calculo_total_sin_filtro(origen[idx], col)
            except Exception:
                return 0
        # Color de relleno y rectángulo redondeado
        def titulo_cuadro( lineas, x_rect, y_rect, ancho_rect, alto_rect):
            # Dibuja un recuadro redondeado con texto centrado (vertical y horizontal)
            self.pdf.set_line_width(0.5)
            self.pdf.set_fill_color(6, 60, 43)
            self.pdf.rect(x_rect, y_rect, ancho_rect, alto_rect, 'DF')  # DF = Dibujo + Relleno

            # Configuración base
            self.pdf.set_text_color(255, 255, 255)

            # Parámetros del texto
            font_size = 10
            line_height = 5  # separación entre líneas
            total_height = len(lineas) * line_height
            y_inicio = y_rect + (alto_rect - total_height) / 2 + 3  # centrado vertical

            # Dibujar cada línea
            for i, (texto, estilo) in enumerate(lineas):
                self.pdf.set_font('Arial', estilo, font_size)
                ancho_texto = self.pdf.get_string_width(texto)
                x_centrada = x_rect + (ancho_rect - ancho_texto) / 2
                y_text = y_inicio + i * line_height
                self.pdf.text(x_centrada, y_text, texto)

        # Cuadro 1
        lineas = [("RESULTADO", 'B')]
        titulo_cuadro(lineas, 40, 45, 60, 20)

        # Cuadro 2 (varias líneas centradas)
        lineas = [
            (f"TOTAL {self.fecha_anio}", 'B'),
            ("(X1)", 'B')
        ]
        titulo_cuadro(lineas, 100, 45, 30, 20)
        lineas = [(f"{self.mes}", 'B')]
        titulo_cuadro(lineas, 130, 45, 30, 10)
        lineas = [(f"{self.fecha_anio} (X1)", 'B')]
        titulo_cuadro(lineas, 130, 55, 30, 10)
        
        lineas = [(f"{self.mes}", 'B')]
        titulo_cuadro(lineas, 160, 45, 30, 10)
        lineas = [(f"{self.fecha_anio_actual} (X1)", 'B')]
        titulo_cuadro(lineas, 160, 55, 30, 10)

        lineas = [
            (f"DIARIO", 'B'),
            ("CV (%)", 'B')
        ]
        titulo_cuadro(lineas, 190, 45, 30, 20)
        
        lineas = [
            (f"ANUAL", 'B'),
            ("CV (%)", 'B')
        ]
        titulo_cuadro(lineas, 220, 45, 30, 20)


        # --- Datos del año anterior ---
        dragas_anio = total(self.res_anterior, 8, 18)
        upm_anio = total(self.res_anterior, 7, 18)
        maquinaria_pesada_anio = total(self.res_anterior, 5, 18)
        operaciones_anio = total(self.res_anterior, 2, 14)
        motores_anio = total(self.res_anterior, 9, 18)
        dragones_anio = total(self.res_anterior, 17, 18)
        motobomba_anio = total(self.res_anterior, 21, 18)
        carbon_anio = total(self.res_anterior, 22, 18)
        combustibles_mineria_anio = total(self.res_anterior, 10, 18)
        oro_anio = total(self.res_anterior, 18, 18)
        mercurio_anio = total(self.res_anterior, 19, 18)
        coltan_anio = total(self.res_anterior, 23, 18)
        planta_electrica_anio = total(self.res_anterior, 24, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.res_anterior, 0, "SI")
            capturas_anio = total(valor, 0, 18)
        except Exception:
            capturas_anio = 0


        # --- Datos  anterior  ---
        dragas_anterior = total(self.resultados_mineria_anterior, 8, 18)
        upm_anterior = total(self.resultados_mineria_anterior, 7, 18)
        maquinaria_pesada_anterior = total(self.resultados_mineria_anterior, 5, 18)
        operaciones_anterior = total(self.resultados_mineria_anterior, 2, 14)
        motores_anterior = total(self.resultados_mineria_anterior, 9, 18)
        dragones_anterior = total(self.resultados_mineria_anterior, 17, 18)
        motobomba_anterior = total(self.resultados_mineria_anterior, 21, 18)
        carbon_anterior = total(self.resultados_mineria_anterior, 22, 18)
        combustibles_mineria_anterior = total(self.resultados_mineria_anterior, 10, 18)
        oro_anterior = total(self.resultados_mineria_anterior, 18, 18)
        mercurio_anterior = total(self.resultados_mineria_anterior, 19, 18)
        coltan_anterior = total(self.resultados_mineria_anterior, 23, 18)
        planta_electrica_anterior = total(self.resultados_mineria_anterior, 24, 18)
 
        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria_anterior, 0, "SI")
            capturas_anterior = total(valor, 0, 18)
        except Exception:
            capturas_anterior = 0
            
        # --- Datos  actual  ---
        dragas_actual = total(self.resultados_mineria, 8, 18)
        upm_actual = total(self.resultados_mineria, 7, 18)
        maquinaria_pesada_actual = total(self.resultados_mineria, 5, 18)
        operaciones_actual = total(self.resultados_mineria, 2, 14)
        motores_actual = total(self.resultados_mineria, 9, 18)
        dragones_actual = total(self.resultados_mineria, 17, 18)
        motobomba_actual = total(self.resultados_mineria, 21, 18)
        carbon_actual = total(self.resultados_mineria, 22, 18)
        combustibles_mineria_actual = total(self.resultados_mineria, 10, 18)
        oro_actual = total(self.resultados_mineria, 18, 18)
        mercurio_actual = total(self.resultados_mineria, 19, 18)
        coltan_actual = total(self.resultados_mineria, 23, 18)
        planta_electrica_actual = total(self.resultados_mineria, 24, 18)

        try:
            valor = Calculo_Spoa.validar_spoa_unidad(self, self.filtro, self.resultados_mineria, 0, "SI")
            capturas_actual = total(valor, 0, 18)
        except Exception:
            capturas_actual = 0
            
        datos = [
        {
            'icono': 'ejc.jpg',
            'nombre': 'OPERACIONES',
            'total2024': operaciones_anio,
            'oct2024': operaciones_anterior,
            'oct2025': operaciones_actual,
            'diarioCV': porcentajes(operaciones_anterior, operaciones_actual, 1),
            'diarioCVUp':  calcular_direccion(operaciones_actual, operaciones_anterior),
            'anualCV': porcentajes(operaciones_anio, operaciones_actual, 1),
            'anualCVUp': calcular_direccion(operaciones_actual, operaciones_anio)
        },
        {
            'icono': 'buldocer.jpg',
            'nombre': 'MAQUINARIA PESADA ',
            'total2024': maquinaria_pesada_anio,
            'oct2024': maquinaria_pesada_anterior,
            'oct2025': maquinaria_pesada_actual,
            'diarioCV': porcentajes(maquinaria_pesada_anterior, maquinaria_pesada_actual, 1),
            'diarioCVUp':  calcular_direccion(maquinaria_pesada_actual, maquinaria_pesada_anterior),
            'anualCV': porcentajes(maquinaria_pesada_anio, maquinaria_pesada_actual, 1),
            'anualCVUp':  calcular_direccion(maquinaria_pesada_actual, maquinaria_pesada_anio)
        },
        {
            'icono': 'dragas.jpg',
            'nombre': 'DRAGAS',
            'total2024': dragas_anio,
            'oct2024': dragas_anterior,
            'oct2025': dragas_actual,
            'diarioCV': porcentajes(dragas_anterior, dragas_actual, 1),
            'diarioCVUp':  calcular_direccion(dragas_actual, dragas_anterior),
            'anualCV': porcentajes(dragas_anio, dragas_actual, 1),
            'anualCVUp': calcular_direccion(dragas_actual, dragas_anio)
        },
        {
            'icono': 'dragas.jpg',
            'nombre': 'DRAGONES BRASILEÑO',
            'total2024': dragones_anio,
            'oct2024': dragones_anterior,
            'oct2025': dragones_actual,
            'diarioCV': porcentajes(dragones_anterior, dragones_actual, 1),
            'diarioCVUp':  calcular_direccion(dragones_actual, dragones_anterior),
            'anualCV': porcentajes(dragones_anio, dragones_actual, 1),
            'anualCVUp':  calcular_direccion(dragones_actual, dragones_anio)
        },
                
                
        {
            'icono': 'capturas.jpg',
            'nombre': 'CAPTURAS PERS',
            'total2024': capturas_anio,
            'oct2024': capturas_anterior,
            'oct2025': capturas_actual,
            'diarioCV': porcentajes(capturas_anterior, capturas_actual, 1),
            'diarioCVUp':  calcular_direccion(capturas_actual, capturas_anterior),
            'anualCV': porcentajes(capturas_anio, capturas_actual, 1),
            'anualCVUp': calcular_direccion(capturas_actual, capturas_anio)
        },
        {
            'icono': 'combate_neg.jpg',
            'nombre': 'MOTORES UND',
            'total2024': motores_anio,
            'oct2024': motores_anterior,
            'oct2025': motores_actual,
            'diarioCV': porcentajes(motores_anterior, motores_actual, 1),
            'diarioCVUp':  calcular_direccion(motores_actual, motores_anterior),
            'anualCV': porcentajes(motores_anio, motores_actual, 1),
            'anualCVUp': calcular_direccion(motores_actual, motores_anio)
        },
        {
            'icono': 'combate_neg.jpg',
            'nombre': 'MOTOBOMBAS',
            'total2024': motobomba_anio,
            'oct2024': motobomba_anterior,
            'oct2025': motobomba_actual,
            'diarioCV': porcentajes(motobomba_anterior, motobomba_actual, 1),
            'diarioCVUp':  calcular_direccion(motobomba_actual, motobomba_anterior),
            'anualCV': porcentajes(motobomba_anio, motobomba_actual, 1),
            'anualCVUp':  calcular_direccion(motobomba_actual, motobomba_anio)
        },
        {
            'icono': 'upm.jpg',
            'nombre': 'UPM UND',
            'total2024': upm_anio,
            'oct2024': upm_anterior,
            'oct2025': upm_actual,
            'diarioCV': porcentajes(upm_anterior, upm_actual, 1),
            'diarioCVUp': calcular_direccion(upm_actual, upm_anterior),
            'anualCV': porcentajes(upm_anio, upm_actual, 1),
            'anualCVUp': calcular_direccion(upm_actual, upm_anio)
        },     
        {
            'icono': 'coltan.jpg',
            'nombre': 'CARBÓN TN',
            'total2024': carbon_anio,
            'oct2024': carbon_anterior,
            'oct2025': carbon_actual,
            'diarioCV': porcentajes(carbon_anterior, carbon_actual, 1),
            'diarioCVUp':  calcular_direccion(carbon_actual, carbon_anterior),
            'anualCV': porcentajes(carbon_anio, carbon_actual, 1),
            'anualCVUp': calcular_direccion(carbon_actual, carbon_anio)
        },
        
        {
            'icono': 'coltan.jpg',
            'nombre': 'MERCURIO KG',
            'total2024': mercurio_anio,
            'oct2024': mercurio_anterior,
            'oct2025': mercurio_actual,
            'diarioCV': porcentajes(mercurio_anterior, mercurio_actual, 1),
            'diarioCVUp': calcular_direccion(mercurio_actual, mercurio_anterior),
            'anualCV': porcentajes(mercurio_anio, mercurio_actual, 1),
            'anualCVUp': calcular_direccion(mercurio_actual, mercurio_anio)
        },
        {
            'icono': 'combustible.jpg',
            'nombre': 'COMBUSTIBLE GLN',
            'total2024': combustibles_mineria_anio,
            'oct2024': combustibles_mineria_anterior,
            'oct2025': combustibles_mineria_actual,
            'diarioCV': porcentajes(combustibles_mineria_anterior, combustibles_mineria_actual, 1),
            'diarioCVUp': calcular_direccion(combustibles_mineria_actual, combustibles_mineria_anterior),
            'anualCV': porcentajes(combustibles_mineria_anio, combustibles_mineria_actual, 1),
            'anualCVUp': calcular_direccion(combustibles_mineria_actual, combustibles_mineria_anio)
        },
        {
            'icono': 'coltan.jpg',
            'nombre': 'ORO KG ',
            'total2024': oro_anio,
            'oct2024': oro_anterior,
            'oct2025': oro_actual,
            'diarioCV': porcentajes(oro_anterior, oro_actual, 1),
            'diarioCVUp': calcular_direccion(oro_actual, oro_anterior),
            'anualCV': porcentajes(oro_anio, oro_actual, 1),
            'anualCVUp': calcular_direccion(oro_actual, oro_anio)
        },{
            'icono': 'coltan.jpg',
            'nombre': 'TIERRAS RARAS (COLTAN)',
            'total2024': coltan_anio,
            'oct2024': coltan_anterior,
            'oct2025': coltan_actual,
            'diarioCV': porcentajes(coltan_anterior, coltan_actual, 1),
            'diarioCVUp': calcular_direccion(coltan_actual, coltan_anterior),
            'anualCV': porcentajes(coltan_anio, coltan_actual, 1),
            'anualCVUp': calcular_direccion(coltan_actual, coltan_anio)
        },{
            'icono': 'combate_neg.jpg',
            'nombre': 'PLANTA ELECTRICA',
            'total2024': planta_electrica_anio,
            'oct2024': planta_electrica_anterior,
            'oct2025': planta_electrica_actual,
            'diarioCV': porcentajes(planta_electrica_anterior, planta_electrica_actual, 1),
            'diarioCVUp': calcular_direccion(planta_electrica_actual, planta_electrica_anterior),
            'anualCV': porcentajes(planta_electrica_anio, planta_electrica_actual, 1),
            'anualCVUp': calcular_direccion(planta_electrica_actual, planta_electrica_anio)
        },
        ]

        # === Configuración inicial de posición ===
        x_icono = 30
        x_nombre = 40
        x_total2024 = 100
        x_oct2024 = 130
        x_oct2025 = 160
        x_diarioCV = 190
        x_anualCV = 220

        y_inicial = 65
        alto_fila = 8

        # === Fuente y colores ===
        self.pdf.set_font('Arial', '', 8)
        self.pdf.set_text_color(0, 0, 0)

        # === Dibujar cada fila ===
        y = y_inicial
        for fila in datos:
            # --- Columna 1: Imagen ---
            try:
                self.pdf.image(
                    f"{self.ruta}static/img/resultados/{fila['icono']}",
                    x_icono, y + 1,
                    10, alto_fila - 2
                )
            except:
                # Si no hay imagen, dibuja recuadro vacío
                self.pdf.rect(x_icono, y, 10, alto_fila)

            # --- Columna 2: Nombre ---
            self.pdf.set_xy(x_nombre, y)
            self.pdf.cell(60, alto_fila, fila['nombre'], border=1, align='L')

            # --- Columna 3: Total 2024 ---
            self.pdf.set_xy(x_total2024, y)
            self.pdf.cell(30, alto_fila, str(fila['total2024']), border=1, align='C')

            # --- Columna 4: Nov 2024 ---
            self.pdf.set_xy(x_oct2024, y)
            self.pdf.cell(30, alto_fila, str(fila['oct2024']), border=1, align='C')

            # --- Columna 5: Nov 2025 ---
            self.pdf.set_xy(x_oct2025, y)
            self.pdf.cell(30, alto_fila, str(fila['oct2025']), border=1, align='C')

            # --- Columna 6: Diario CV (%) ---
            diario_texto = f"{fila['diarioCV']}%"
            self.pdf.set_xy(x_diarioCV, y)
            self.pdf.cell(30, alto_fila, diario_texto, border=1, align='C')

            # --- Columna 7: Anual CV (%) ---
            anual_texto = f"{fila['anualCV']}%"
            self.pdf.set_xy(x_anualCV, y)
            self.pdf.cell(30, alto_fila, anual_texto, border=1, align='C')

            # Avanza a la siguiente fila
            y += alto_fila

            # Salto de página automático
            if y > 270:
                self.pdf.add_page()
                y = 20

        valor = 0
        for x in self.variable:
            for y in self.valor_material:
                if x[0]==y[12]:
                    valor = valor + (y[18]*float(x[1]))

        valor_ant = 0
        
        for x in self.variable:
            for y in self.valor_material_ant:
                if x[0]==y[12]:
                    valor_ant = valor_ant + (y[18]*float(x[1]))

        self.pdf.set_fill_color(255, 255, 255)
        self.pdf.rounded_rect(265, 45, 60, 145, 1,'F', '1234')


        # Datos del rectángulo
        x_rect = 265
        y_rect = 45
        ancho_rect = 60

        # Lista de líneas con formato (texto, estilo)
        lineas = [
            ("VALOR DE LA MAQUINARIA", ''),              # normal
            ("", ''),          # normal
            (f"{self.fecha_anio}:", 'B'),                          # normal
            (f"COP $: {valor_ant:,.0f}", 'B'), 
            ("", ''),                
                            
            (f"{self.fecha_anio_actual}:", 'B'),                          # normal
            (f"COP $: {valor:,.0f}", 'B'), 
            ("", ''),              
                     
            ("-----------------------------", ''),    
            ("", ''),                 
            ("VALOR DE LA", ''),    
            ("AFECTACIÓN ECONÓMICA", ''),
            ("EN DOLARES", ''),            # normal
            ("", ''),          # normal
            (f"{self.fecha_anio}:", 'B'),                          # normal
            (f"COP $: {valor_ant/float(self.valor_dolar):,.0f}", 'B'), 
            ("", ''),                
                            
            ("", ''),          # normal
            (f"{self.fecha_anio_actual}:", 'B'),                          # normal
            (f"COP $: {valor/float(self.valor_dolar):,.0f}", 'B'), 
            ("", ''),              
                                                             # negrita
                             # espacio visual             
        ]


        # Altura inicial
        y_text = y_rect + 10
        line_height = 6  # separación entre líneas

        for texto, estilo in lineas:
            if not texto:
                y_text += line_height
                continue

            # Configurar fuente según estilo
            self.pdf.set_font('Arial', estilo, 10)

            # Calcular centrado horizontal
            ancho_texto = self.pdf.get_string_width(texto)
            x_centrada = x_rect + (ancho_rect - ancho_texto) / 2

            # Dibujar texto
            self.pdf.text(x_centrada, y_text, texto)
            y_text += line_height


      