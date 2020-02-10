import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
import seaborn as sns
import numpy as np
import dash_table
from dash.dependencies import Input, Output, State

def generate_table(dataframe, page_size=10):
    return dash_table.DataTable(
        id='dataTable',
        columns=[{
            "name": i,
            "id": i
        } for i in dataframe.columns],
        data=dataframe.to_dict('records'),
        page_action="native",
        page_current=0,
        page_size=page_size,
    )

data = pd.read_csv('tsa_claims_ujian.csv')
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    children=[
        html.H1('Ujian Module 2 Dashboard TSA'),
        html.Div(children='''
        Created by: Cornellius
    '''),
        dcc.Tabs(
            children=[
                dcc.Tab(
                    value='DataFrame Table',
                    label='DATAFRAME TSA',
                    children=[
                        html.Div([
                            html.P('Claim Site'),
                    dcc.Dropdown(value='All',
                    id='filter-ClaimSite',
                    options=[{'label':'Checkpoint','value':'Checkpoint'},
                    {'label':'Other','value':'Other'},
                    {'label':'Checked Baggage','value':'Checked Baggage'},
                    {'label':'Motor Vehicle','value':'Motor Vehicle'},
                    {'label':'Bus Station','value':'Bus Station'}])
                ],className='col-4'),
                html.Br(),
                            html.Div([
                                html.P('Max Rows:'),
                                dcc.Input(id ='filter-row',
                                          type = 'number', 
                                          value = 10)
                            ], className = 'row col-3'),
                            html.Div(children =[
                                    html.Button('search',id = 'filter')
                             ],className = 'row col-4'),
                             
                            html.Div(id='div-table',
                                     children=[generate_table(data)])
                dcc.Tab(
                value='Tab2',
                label='Bar-Chart',
                children=[
                    html.Div([
                        html.P('Y1:'),
                    dcc.Dropdown(value='Claim Amount',
                    id='filter-claimAmount',
                    options=[{'label':data['Claim Amount'],'value':data['Claim Amount']},
                            {'label':data['Close Amount'],'value':data['Close Amount']},
                            {'label':data['Claim Type','Claim Site','Disposition'],'value':data['Claim Type','Claim Site','Disposition']}
                    ])
                ],className='col-4'),
                            dcc.Graph(id='example-graph',
                                      figure={
                                          'data': [{
                                              'x': data['Claim Type'],
                                                    data['Claim Site'],
                                                    data['Disposition'],
                                              'y': data,
                                              'type': 'bar',
                                              'name': 'Bar Chart'
                                          }],
                                          'layout': {
                                              'title':
                                              'Tips Dash Data Visualization'
                                          }
                                      })
                    dcc.Tab(
                    value='Tab3',
                    label='Scatter chart',
                    children=[
                        html.Div(children=dcc.Graph(
                            id='graph-scatter',
                            figure={
                                'data': [
                                    go.Scatter(x=data['Claim Amount'],
                                               y=data['Close Amount'],
                                               mode='markers',
                                               name=data[data['Status']]['Claim Type']
                                    
                                ],
                                'layout':
                                go.Layout(
                                    xaxis={'title': 'Claim Amount'},
                                    yaxis={'title': 'Close Amount'},
                                    hovermode='closest')
                            }))
                    ]),
                        ])
                    ]),

@app.callback(
    Output(component_id = 'div-table', component_property = 'children'),
    [Input(component_id = 'filter', component_property = 'n_clicks'),
    Input(component_id = 'filter-claimAmount', component_property = 'value')],
    [State(component_id = 'filter-row', component_property = 'value'), 
    State(component_id = 'filter-ClaimSite', component_property = 'value')]

def update_table(n_clicks,claimAmount, row, ClaimSite):
    data = pd.read_csv('tsa_claims_ujian.csv')
    if claimAmount != '':
        tips = data[data['Claim Amount'] == smoker]
    if ClaimSite != '':
        tips = data[data['Claim Site'] == day]
    children = [generate_table(tips, page_size = row)]
    return children

if __name__ == '__main__':
    app.run_server(debug=True)

