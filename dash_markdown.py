import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State
import pandas as pd
import generator
import region_converter

dataset = "Foreign_Exchange_Rates.csv"
df = pd.read_csv(dataset)
cnt_rows = df.shape[0]
election_dates = ['2000-09-07' , '2004-09-02' , '2008-09-04' , '2012-09-06' , '2016-09-08']

# Cleaning
updated_df_without_nd = df[df.columns.values[2]]!="ND" 
df = df[updated_df_without_nd]
df.dropna(axis=0,inplace=True)

regions = generator.regions(df.columns)
# col_head["NEW ZEALAND"] = "NEW" 
col_head = generator.col_heads(regions,df.columns)
year_to_date = generator.year_to_date(election_dates)
dates = generator.dates_and_hashes(cnt_rows,df,col_head)[0]
hash_value_dates = generator.dates_and_hashes(cnt_rows,df,col_head)[1]
hash_value_dataframe = generator.dates_and_hashes(cnt_rows,df,col_head)[2]
# cost['2004-09-02']["THAILAND"] = 41.52
cost = generator.cost(dates,regions,df,col_head,hash_value_dataframe)

# Conversion of Region -> It's Currency
region_of = region_converter.convert(regions)[1]
currency_of = region_converter.convert(regions)[0]

election_year = "2016"
date = year_to_date[election_year]


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    html.Label('Currency'),
    dcc.Dropdown(
        id='ccy',
        options = [
            {
                'label' : 'USD','value' : 'USD'
            },
            {
                'label' : 'EUR' , 'value' : 'EUR'
            },
            {
                'label' : 'CAD' , 'value' : 'CAD'
            }
        ],
    ),

    

    html.Label('Option Type'),
    dcc.Dropdown(
        id='optiontype',
        options = [
            {
                'label' : 'American','value' : 'American'
            },
            {
                'label' : 'European' , 'value' : 'European'
            }
        ],
    ),

    html.Div([
    html.Label('Expiry'),
    dcc.Input(id='expiry'),
]),

    html.Div([
    html.Label('Strike'),
    dcc.Input(id='strike'),
    ]),

    html.Button('Submit', id='submit'),

    dcc.Graph(id='plot')
])

@app.callback(Output('plot', 'figure'),
              Input('submit', 'n_clicks'),
              [State('ccy', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plotfunc(submit,ccy,optiontype,expiry,strike):

    buffer_plot = 120
    plot_start_index = hash_value_dates[date]-buffer_plot
    # plot_start_date = dates[plot_start_index]
    plot_end_index = hash_value_dates[date]+buffer_plot
    # plot_end_date = dates[plot_end_index]
    traded_at = []
    x_values = []
    x_val = -buffer_plot

    for i in range(plot_start_index,plot_end_index+1):
        try:
            traded_at.append(round((float(cost[dates[i]][region_of[currency]])),10))
    #         traded_at.append(round(float(cost[dates[i]][region_of[currency]]) - float(cost[date][region_of[currency]]),10))
            x_values.append(x_val)
            x_val += 1
        except:
            continue
    
    trace0 = go.Scatter(x=x_values, 
                   y=traded_at, 
                   mode="lines",)

    fig = dict(data=[trace0])

    print(fig)
    return fig


if __name__ == '__main__':
    app.run_server(debug = True)