

from __init__ import *


# df = pd.read_csv('server/tipo_docker_alertas/dash/Covid19VacunasAgrupadas.csv')
# print(df)
# print(df.vacuna_nombre.nunique())
# print(df.vacuna_nombre.unique())

def estadistica():



    alertas_cantidad = estadisitca_cantidad()

    df_alertas=[]
    for x in alertas_cantidad:
        # print(x)
        for y in x:
            # print(y)

            if y[30] == "GAO - Residual Disidencias FARC" or y[30] == "GAO-r disidencias FARC" or y[30] == "GAO-RESIDUAL" or y[30] == "GAO - RESIDUAL DISIDENCIAS FARC" or y[30] == "GAO-R DISIDENCIAS FARC" or y[30] == "GAO-r" :
                enemigo = "GAO-r"
            else:
                enemigo = y[30]

            df_alertas.append([str(y[2]), y[5], y[14], enemigo, 1])

    alertas_cantidad = pd.DataFrame(df_alertas, columns=['fecha', 'division', 'departamento', 'enemigo', 'cantidad'])
    return alertas_cantidad
# test_df = pd.DataFrame(alertas_cantidad)
# print(alertas_cantidad)


def division():
    # print(alertas[5])
    alertas = estadisitca()
    opciones_divisiones = []
    enemigo=[]
    numero=0
    alertas_cantidad = estadisitca_cantidad()
    for x in alertas[1]:

        numero=0
        for w in alertas_cantidad:
            for y in w:
                if y[5] == x[0]:
                    numero = numero + 1
                unidad_di = (x[0],numero)

            opciones_divisiones.append(unidad_di)
            # opciones_divisiones.append(numero)
    div = pd.DataFrame(opciones_divisiones, columns=['division', 'cantidad'])

    return div
     
def enemigos():
    # print(alertas[5])
    alertas = estadisitca()
    enemigo_cant=[]
    numero=0
    
    alertas_cantidad = estadisitca_cantidad()
    
    for x in alertas[3]:
        numero=0
        # print(x)
        for w in alertas_cantidad:
            for y in w:
                if y[30] == x[0]:
                    
                    numero = numero + 1        
                    if y[30] == "GAO - Residual Disidencias FARC" or y[30] == "GAO-r disidencias FARC" or y[30] == "GAO-RESIDUAL" or y[30] == "GAO - RESIDUAL DISIDENCIAS FARC" or y[30] == "GAO-R DISIDENCIAS FARC" or y[30] == "GAO-r":
                        enemigo = "GAO-r"
                        
                    else:
                        enemigo = y[30]


            unidad_di = (enemigo,numero)
            # print(unidad_di)
            enemigo_cant.append(unidad_di)
    # print(enemigo_cant)
    enemigo_total=[]

    from itertools import groupby

    enemigo_total = [(k, sum([e[1] for e in g])) for k, g in groupby(enemigo_cant, lambda x:x[0])]

    # print(enemigo_total)
    ene = pd.DataFrame(enemigo_total, columns=['enemigo', 'cantidad'])
    
    fecha=[]
    for x in alertas[0]:
        numero=0
        # print(x)
        for w in alertas_cantidad:
            for y in w:
                if y[2] == x[0]:  
                    numero = numero + 1 
                    unidad_di = (str(y[2]),numero)
            fecha.append(unidad_di)

    fecha = pd.DataFrame(fecha, columns=['fecha', 'cantidad'])  
    
    departamento=[]
    for x in alertas[2]:
        numero=0
        # print(x)
        for w in alertas_cantidad:
            for y in w:
                if y[14] == x[0]:  
                    numero = numero + 1 
                    unidad_di = (str(y[14]),numero)
            departamento.append(unidad_di)

    departamento = pd.DataFrame(departamento, columns=['departamento', 'cantidad'])  
    # print(fecha)
    return  [ene, fecha, departamento]  


# print(opciones_divisiones)
app = dash.Dash(__name__)

app.layout = html.Div([
    
    # html.Div([
    #     # html.H1('Vacunados por covid'),
    #     # html.Img(src='assets/vacuna.png')
    # ], className = 'banner'),

    html.Div([
        html.Div([
            html.P('ALERTAS', className = 'fix_label', style={'color':'black', 'margin-top': '2px'}),
            dcc.RadioItems(id = 'dosis-radioitems', 
                            labelStyle = {'display': 'inline-block'},
                            options = [
                                {'label' : 'DIVISION', 'value' : "division"},
                                {'label' : 'DEPARTAMENTO', 'value' : "departamento"},
                                {'label' : 'ENEMIGO', 'value' : "enemigo"},
                                {'label' : 'FECHA', 'value' : "fecha"}
                            ], value = "division",
                            style = {'text-aling':'center', 'color':'black'}, className = 'dcc_compon'),
        ], className = 'create_container2 five columns', style = {'margin-bottom': '20px'}),
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph', figure = {})
        ], className = 'create_container2 eight columns'),
        html.Div([
            dcc.Graph(id = 'pie_graph', figure = {})
        ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),

    html.Div([
        html.Div([
            dcc.Graph(id = 'my_graph_3', figure = {})
        ], className = 'create_container2 eight columns')

        # html.Div([
        #     dcc.Graph(id = 'pie_graph_2', figure = {})
        # ], className = 'create_container2 five columns')
    ], className = 'row flex-display'),
], id='mainContainer', style={'display':'flex', 'flex-direction':'column'})

@app.callback(
    Output('my_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):
    alertas_cantidad = estadistica()
    if value == 'division':
        fig = px.bar(
            data_frame = alertas_cantidad,
            x = 'division',
            y = 'cantidad',
            color = "enemigo",
            title = "Alertas División"
            # histfunc='avg'
            )
        
        
    elif value == 'departamento':
        fig = px.bar(
            data_frame = alertas_cantidad,
            x = 'departamento',
            y = 'cantidad',
            color = "enemigo",
            title = "Alertas Departamento"
            )
        
    elif value == 'enemigo':
        fig = px.bar(
            data_frame = alertas_cantidad,
            x = 'enemigo',
            y = 'cantidad',
            color = "division",
            title = "Alertas Enemigo"
            )
                
    elif value == 'fecha':
        
        fig = px.bar(
            data_frame = alertas_cantidad,
            x = 'fecha',
            y = 'cantidad',
            color = "enemigo",
            title = "Alertas Fecha"
            )
                
    return fig

@app.callback(
    Output('pie_graph', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph_pie(value):
    alertas_cantidad = estadistica()
    # alertas_total()
    if value == 'division':
        fig2 = px.pie(
            data_frame = alertas_cantidad,
            names = 'division',
            hole=0.3,
            values = 'cantidad'
            )
    elif value == 'departamento':
        fig2 = px.pie(
            data_frame = alertas_cantidad,
            names = 'departamento',
            hole=0.3,
            values = 'cantidad')
        
    elif value == 'enemigo':
        fig2 = px.pie(
            data_frame = alertas_cantidad,
            names = 'enemigo',
            hole=0.3,
            values = 'cantidad'
            )
    elif value == 'fecha':
        fig2 = px.pie(
            data_frame = alertas_cantidad,
            names = 'fecha',
            hole=0.3,
            values = 'cantidad')

    return fig2

@app.callback(
    Output('my_graph_3', component_property='figure'),
    [Input('dosis-radioitems', component_property='value')])

def update_graph(value):
    alertas_cantidad = division()
    alertas_cantidad_enemigo = enemigos()

    if value == 'division':
        fig_3 = px.bar(
            data_frame = alertas_cantidad,
            x = 'division',
            y = 'cantidad',
            text_auto=True,
            title = "Alertas División",

            # histfunc='avg'
            )
        
        
    elif value == 'departamento':
        fig_3 = px.bar(
            data_frame = alertas_cantidad_enemigo[2],
            x = 'departamento',
            y = 'cantidad',
            text_auto=True,
            title = "Alertas Departamento"
            )
        
    elif value == 'enemigo':
        fig_3 = px.bar(
            data_frame = alertas_cantidad_enemigo[0],
            x = 'enemigo',
            y = 'cantidad',
            text_auto=True,
            title = "Alertas Enemigo"
            )
                
    elif value == 'fecha':
        # fig_3 = px.line(alertas_cantidad, x='fecha', y="cantidad")
        fig_3 = px.line(
            data_frame = alertas_cantidad_enemigo[1],
            x = 'fecha',
            y = 'cantidad',
            # color = "enemigo",
            title = "Alertas Fecha"
            )
                
    return fig_3
import datetime
# app.layout = html.H1('The time is: ' + str(datetime.datetime.now()))

if __name__ == ('__main__'):
    # app.run_server(host = "0.0.0.0", port=5050, debug=True)
    app.run_server(host = "0.0.0.0", port=5050)