import pandas as pd

def estadistica_resultados_mineria_global(datos_res, hechos):
    """
    Versión optimizada con pandas.
    Recibe: datos_res (lista de listas), hechos (lista de listas)
    Devuelve: lista con 21 listas de resultados (idéntico formato al original).
    """

    # Convertir a DataFrame para vectorización
    columnas = [f"c{i}" for i in range(max(len(r) for r in datos_res))]  # nombres genéricos
    df = pd.DataFrame(datos_res, columns=columnas).fillna("")

    # --- Filtros base ---
    es_mineria = df["c17"] == "Explotación Ilícita de Yacimientos Mineros"
    es_captura = df["c9"].str.contains("CAPTURADO", na=False)
    es_rme = df["c9"].str.contains("RME", na=False)
    no_delco = df["c7"] != "DELINCUENCIA"

    # Subconjuntos mineros
    df_mineria = df[es_mineria]
    df_explosivos = df_mineria[df_mineria["c11"] == "EXPLOSIVOS"]
    df_combustibles = df_mineria[df_mineria["c10"].str.contains("COMBUSTIBLES", na=False)]

    # --- Filtros rápidos con máscaras ---
    def contains_any(col, words):
        pattern = "|".join(words)
        return col.str.contains(pattern, case=False, na=False, regex=True)

    # === CATEGORÍAS ===
    capturas_mineria = df_mineria[df_mineria["c9"].str.contains("CAPTURADO", na=False)].values.tolist()
    rme_mineria = df_mineria[df_mineria["c9"].str.contains("RME", na=False)].values.tolist()
    
    eiym = [h for h in hechos if h[9] == "Explotación Ilícita de Yacimientos Mineros"]#ok

    excavadoras = df_mineria[df_mineria["c12"].str.contains("EXCAVADORA", na=False)].values.tolist()
    retroexcavadoras = df_mineria[df_mineria["c12"] == "RETROEXCAVADORA(S)"].values.tolist()
    maquinaria_pesada = df_mineria[contains_any(df_mineria["c12"], ["MAQUINARIA PESADA", "BULDOCER", "EXCAVADORA", "RETROEXCAVADORA", "MOTONIVELADORA"])].values.tolist()
    buldocer = df_mineria[df_mineria["c12"].str.contains("BULDOCER", na=False)].values.tolist()
    upm = df_mineria[contains_any(df_mineria["c12"], ["UPM ILEGAL", "UPM LEGAL", "SOCAVON", "BOCAMINA"])].values.tolist()#ok
    dragas = df_mineria[df_mineria["c12"].str.contains("DRAGA", na=False)].values.tolist()
    motores = df_mineria[contains_any(df_mineria["c12"], ["MOTORES", "MOTOBOMBA"])].values.tolist()
    combustibles_mineria = df_combustibles[df_combustibles["c13"] == "Gal"].values.tolist()
    capturas_sin_delco = df[es_captura & no_delco & ~es_rme].values.tolist()
    maquinaria_amarilla = df_mineria[contains_any(df_mineria["c12"], ["BULDOCER", "EXCAVADORA", "RETROEXCAVADORA", "MOTONIVELADORA"])].values.tolist()
    explosivos_mineria_kg = df_explosivos[df_explosivos["c13"] == "Kg"].values.tolist()
    explosivos_mineria_m = df_explosivos[df_explosivos["c13"] == "M"].values.tolist()
    explosivos_mineria_und = df_explosivos[df_explosivos["c13"] == "Und(s)"].values.tolist()
    material_transporte = df_mineria[(df_mineria["c10"].str.contains("MATERIAL DE TRANSPORTE", na=False)) & (~df_mineria["c11"].str.contains("ACCESORIOS", na=False))].values.tolist()
    dragones = df_mineria[df_mineria["c12"].str.contains("DRAGON(ES)", na=False, regex=False)].values.tolist()
    oro =  [h for h in datos_res if h[12] == "ORO"]
    mercurio = df_mineria[df_mineria["c12"].str.contains("MERCURIO", na=False)].values.tolist()
    cianuro = df_mineria[df_mineria["c12"].str.contains("CIANURO", na=False)].values.tolist()
    motobomba = df_mineria[contains_any(df_mineria["c12"], ["MOTOBOMBA"])].values.tolist()
    planta_electrica = df_mineria[contains_any(df_mineria["c12"], ["PLANTA ELÉCTRICA"])].values.tolist()
    carbon = df_mineria[df_mineria["c12"].str.contains("CARBÓN ACTIVADO", "CARBON MINERAL", na=False)].values.tolist()
    coltan = df_mineria[df_mineria["c12"].str.contains("COLTAN", na=False)].values.tolist()
    
    # === Retornar igual que versión original ===
    return [
        capturas_mineria, # 0
        rme_mineria, # 1
        eiym, # 2
        excavadoras, # 3
        retroexcavadoras, # 4
        maquinaria_pesada, # 5
        buldocer, # 6
        upm, # 7
        dragas, # 8
        motores, # 9
        combustibles_mineria, # 10
        capturas_sin_delco, # 11
        maquinaria_amarilla, # 12
        explosivos_mineria_kg, # 13
        explosivos_mineria_m, # 14
        explosivos_mineria_und, # 15
        material_transporte, # 16
        dragones, # 17
        oro, # 18
        mercurio, # 19
        cianuro, # 20
        motobomba, # 21
        carbon, # 22
        coltan, #23
        planta_electrica #24
    ]
