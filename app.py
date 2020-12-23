import pandas as pd
from collections import defaultdict
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
from dash.dependencies import Input, Output, State


currency_of = {}
currency_of["AUSTRALIA"] = "AUD"
currency_of["EURO"] = "EUR"
currency_of["NEW"] = "NZD"
currency_of["UNITED"] = "GBP"
currency_of["BRAZIL"] = "BRL"
currency_of["CANADA"] = "CAD"
currency_of["CHINA"] = "CNY"
currency_of["HONG"] = "HKD"
currency_of["INDIA"] = "INR"
currency_of["KOREA"] = "KRW"
currency_of["MEXICO"] = "MXN"
currency_of["SOUTH"] = "ZAR"
currency_of["SINGAPORE"] = "SGD"
currency_of["DENMARK"] = "DKK"
currency_of["JAPAN"] = "JPY"
currency_of["MALAYSIA"] = "MYR"
currency_of["NORWAY"] = "NOK"
currency_of["SWEDEN"] = "SEK"
currency_of["SRI"] = "LKR"
currency_of["SWITZERLAND"] = "CHF"
currency_of["TAIWAN"] = "TWD"
currency_of["THAILAND"] = "THB"

dataset = "Foreign_Exchange_Rates.csv"
df = pd.read_csv(dataset)
df.columns = [c.replace(' ', '_') for c in df.columns]
df = df.replace("ND" , float("Nan") , regex = True)
col2 = []
for col in df.columns:
    col2.append(col.split()[0])
# print(col2)
temp_name = {
    "Unnamed:_0" : "Unn",
    "Time_Serie" : "Tim",
    "AUSTRALIA_-_AUSTRALIAN_DOLLAR/US$" : "AUD",
    "EURO_AREA_-_EURO/US$" : "EUR",
    "NEW_ZEALAND_-_NEW_ZELAND_DOLLAR/US$" : "NZD",
    "UNITED_KINGDOM_-_UNITED_KINGDOM_POUND/US$" : "GBP",
    "BRAZIL_-_REAL/US$" : "BRL",
    "CANADA_-_CANADIAN_DOLLAR/US$" : "CAD",
    "CHINA_-_YUAN/US$" : "CNY",
    "HONG_KONG_-_HONG_KONG_DOLLAR/US$" : "HKD",
    "INDIA_-_INDIAN_RUPEE/US$" : "INR",
    "OREA_-_WON/US$" : "KRW",
    "MEXICO_-_MEXICAN_PESO/US$" : "MXN",
    "SOUTH_AFRICA_-_RAND/US$" : "ZAR",
    "SINGAPORE_-_SINGAPORE_DOLLAR/US$" : "SGD",
    "DENMARK_-_DANISH_KRONE/US$" : "DKK",
    "JAPAN_-_YEN/US$" : "JPY",
    "MALAYSIA_-_RINGGIT/US$" : "MYR",
    "NORWAY_-_NORWEGIAN_KRONE/US$" : "NOK",
    "SWEDEN_-_KRONA/US$" : "SEK",
    "SRI_LANKA_-_SRI_LANKAN_RUPEE/US$" : "LKR",
    "SWITZERLAND_-_FRANC/US$" : "CHF",
    "TAIWAN_-_NEW_TAIWAN_DOLLAR/US$" : "TWD",
    "THAILAND_-_BAHT/US$" : "THB",
}

# for col in df.columns:
#     print(col[0])
#     temp_name[col] = currency_of[col[0]]
df = df.rename(columns = temp_name)
# print(df.head(20))


election_dates = ['2000-09-07' , '2004-09-02' , '2008-09-04' , '2012-09-06' , '2016-09-08']

days_around_election = {}

for date in election_dates:
    days_around_election[date] = []
    
    
for date in election_dates:
    start_index = -int(df[df['Tim']==date].index.values)

    while(1):
        days_around_election[date].append(start_index)
        start_index += 1
        if len(days_around_election[date]) == df.shape[0]:
            break

for date in election_dates:
    df["days{}".format(date[:4])] = days_around_election[date]

# print(df.head())
    
values = defaultdict(lambda : defaultdict(dict))

for date in election_dates:
    for ccy in df.columns:
        if ccy == "Unn" or ccy == "Tim" or ccy == "days2000" or ccy == "days2004" or ccy == "days2008" or ccy == "days2012" or ccy == "days2016":
            continue
        for i in range(0,df.shape[0]):
            days = "days" + date[:4]
            values[date][ccy][df[days][i]] = (df[ccy][i])  


buffer = 160

# ccy1 = "USD"
# ccy2 = "AUD"
# optiontype = "American"
# strike = "0.2"
# expiry = "3"


def traded_plot(ccy):

    if ccy is None:
        ccy = "CCY2"
        x_val = [0] * 160
        y_val = [0] * 160
        data1 = go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = '2000',
            line = dict(color=('rgb(255,0,0)'))
        )
        
        data2 = go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = '2004',
                line = dict(color=('rgb(36,173,233)'))
        )
        
        data3 = go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = '2008',
                line = dict(color=('rgb(0,120,0)'))
        )
        
        data4 = go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = '2012',
                line = dict(color=('rgb(255,128,0)'))
        )
        
        data5 = go.Scatter(
                x = x_val,
                y = y_val,
                mode = 'lines',
                name = '2016',
                line = dict(color=('rgb(0,0,255)'))
        )
        
        data = [data1,data2,data3,data4,data5]
        
        ccy = 'USD - '+ccy
        title = 'Currency Pair - {} - % Change'.format(ccy)
        
        return {
            'data':data,
            'layout':go.Layout(
            xaxis = {'title':'Days around Election'},
            yaxis = {'title':'% Change'},
            title = title,
            ),
        }



    x_val = []
    for i in range(-buffer,buffer+1):
        x_val.append(i)
    
    y_val = {}
    for date in election_dates:
        y_val[date] = []
        for i in range(-buffer,buffer+1):
            y_val[date].append((round(float(values[date][ccy][i]),6) - round(float(values[date][ccy][0]),6)) / round(float(values[date][ccy][i]),6) * 100 )
#         plt.plot(x_val,y_val[date])
#     plt.show()
#     print(len(y_val[election_dates[1]]))
    data1 = go.Scatter(
            x = x_val,
            y = y_val[election_dates[0]],
            mode = 'lines',
            name = '2000',
            line = dict(color=('rgb(255,0,0)'))
    )
    
    data2 = go.Scatter(
            x = x_val,
            y = y_val[election_dates[1]],
            mode = 'lines',
            name = '2004',
            line = dict(color=('rgb(36,173,233)'))
    )
    
    data3 = go.Scatter(
            x = x_val,
            y = y_val[election_dates[2]],
            mode = 'lines',
            name = '2008',
            line = dict(color=('rgb(0,120,0)'))
    )
    
    data4 = go.Scatter(
            x = x_val,
            y = y_val[election_dates[3]],
            mode = 'lines',
            name = '2012',
            line = dict(color=('rgb(255,128,0)'))
    )
    
    data5 = go.Scatter(
            x = x_val,
            y = y_val[election_dates[4]],
            mode = 'lines',
            name = '2016',
            line = dict(color=('rgb(0,0,255)'))
    )
    
    data = [data1,data2,data3,data4,data5]
    
    ccy = 'USD - '+ccy
    title = 'Currency Pair - {} - % Change'.format(ccy)
    
    return {
        'data':data,
        'layout':go.Layout(
        xaxis = {'title':'Days around Election'},
        yaxis = {'title':'% Change'},
        title = title,
        ),
    }
# traded_plot("CHF")

def options_plot(strike,timespan,optiontype,ccy,year):
    if strike is None:
        x_val = [0] * 160
        y_val = [0] * 160
        required_color = dict(color=('rgb(255,0,0)'))
        year = "Year"
        optiontype = "Option type"
        data1 = go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = '{}'.format(year),
            line = required_color
        )
        data = [data1]
    #     print(data)
        title = 'Digital Option - {} - {}'.format(optiontype,(year[:4]))

        return {
            'data':data,
            'layout':go.Layout(
            xaxis = {'title':'Days around Election'},
            yaxis = {'title':'Trade Worked or Not'},
            title = title,
            ),
        }


    try:
        strike = float(strike)
        timespan = int(timespan)
    except:
        pass
    
    try:
        x_range = timespan*30
    except:
        pass

    european_plot = {}
    american_plot = {}
    
    for date in election_dates:
        european_plot[date] = []
        american_plot[date] = []
    if optiontype == "European":
        for date in election_dates:
            x_val = []
            for i in range(-x_range , x_range+1):
                x_val.append(i)
                if round(float(values[date][ccy][i+30]),6) >= round(float(values[date][ccy][i]),6) * (1 + 0.01 * strike):
                    european_plot[date].append(1)
                else:
                    european_plot[date].append(0)
#             plt.title(date)
#             plt.plot(x_val,european_plot[date])
#             plt.show()
    else:
        for date in election_dates:
            x_val = []
            for i in range(-x_range , x_range + 1):
                x_val.append(i)
                flag = False
                for j in range(i+1,i+31):
#                     print((round(float(values[date][ccy][i]),6) * (1 + (strike/100))))
                    if round(float(values[date][ccy][j]),6) >= (round(float(values[date][ccy][i]),6) * (1 + (0.01 * strike))):
                        flag = True
                if flag == True:
                    american_plot[date].append(1)
                else:
                    american_plot[date].append(0)
#             plt.plot(x_val,american_plot[date])
#             plt.title(date)
#             plt.show()
            
    if(optiontype=='American'):
        y_val = []
        y_val = american_plot[year]
    if(optiontype=='European'):
        y_val = []
        y_val = european_plot[year]
    
    yearno = year[:4]
    required_color = ""
    
    if yearno == "2000":
        required_color = dict(color=('rgb(255,0,0)'))
    elif yearno == "2004":
        required_color = dict(color=('rgb(36,173,233)'))
    elif yearno == "2008":
        required_color = dict(color=('rgb(0,120,0)'))
    elif yearno == "2012":
        required_color = dict(color=('rgb(255,128,0)'))
    elif yearno == "2016":
        required_color = dict(color=('rgb(0,0,255)'))

    data1 = go.Scatter(
            x = x_val,
            y = y_val,
            mode = 'lines',
            name = '{}'.format(year),
            line = required_color
    )
    data = [data1]
#     print(data)
    title = 'Digital Option - {} - {}'.format(optiontype,(year[:4]))
    
    return {
        'data':data,
        'layout':go.Layout(
        xaxis = {'title':'Days around Election'},
        yaxis = {'title':'Trade Worked or Not'},
        title = title,
        ),
    }
# options_plot("0.5","3","American","INR",election_dates[1])

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Forex Analysis'

server = app.server

colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}

app.layout = html.Div(
#     style={'backgroundColor': colors['background']},
        children = [
            
        html.Div([
                html.H2("U.S. Elections | Currency Movement Analysis"),
                html.Img(src="/assets/icon.png")
            ], 
            className="banner",
            style={'margin-bottom': '2em'}
        ),
            
        html.Div([
            html.Label('CCY1 :',style={'margin-right': '6.5em','margin-bottom' : '2em'}),

            dcc.Dropdown(
                id='ccy1',
                options = [
                    {'label':'USD','value':'USD'},
                ],
                style=dict(
                    width='200px',
                    verticalAlign="middle",
                    color='#506784'
                )
#                 style = {'width':'200px','color':'#506784'},
            )
        ],
            style=dict(display='flex')
        ),


        html.Div([
            html.Label('CCY2 :',style={'margin-right': '6.5em'}),
            dcc.Dropdown(
                id='ccy2',
                options = [
                            {'label':'AUD','value':'AUD'},

                            {'label':'BRL','value':'BRL'},

                          {'label':'CAD','value':'CAD'},

                          {'label':'CHF','value':'CHF'},

                          {'label':'EUR','value':'EUR'},

                          {'label':'GBP','value':'GBP'},

                          {'label':'INR','value':'INR'},

                          {'label':'JPY','value':'JPY'},

                          {'label':'KRW','value':'KRW'},

                          {'label':'MXN','value':'MXN'},

                          {'label':'NOK','value':'NOK'},

                          {'label':'NZD','value':'NZD'},

                          {'label':'SEK','value':'SEK'},

                          {'label':'SGD','value':'SGD'},

                          {'label':'TWD','value':'TWD'},

                          {'label':'ZAR','value':'ZAR'},


                ],
                style=dict(
                    width='200px',
                    verticalAlign="middle",
                    color='#506784'
                )
#                 style = {'width':'200px','color':'#506784'},
            )
        ],
            style = {'margin-bottom': '1em' , 'display':'flex'},

#             style=dict(display='flex')
        ),


        html.Div([
            html.Label('Option Type :',style={'margin-right': '3.8em'}),
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
                style=dict(
                    width='200px',
                    verticalAlign="middle",
                    color='#506784'
                )
#                 style = {'width':'200px','color':'#506784'},
            )
        ],
            style = {'margin-bottom': '1em' , 'display':'flex'},

#             style=dict(display='flex')
        ),

        html.Div([
            html.Label('Strike in % :',style={'margin-right': '4.5em'}),
            dcc.Input(id='strike',
                placeholder = 'Eg. 0.6',
                className = "textbox",
                style=dict(
                    width=195,
                    verticalAlign="middle",
                    color='#506784'
                ),
            )
        ],
            style = {'margin-bottom': '1em' , 'display':'flex'},
        ),

        html.Div([
            html.Label('Expiry in Months :',style={'margin-right': '2em'}),
            dcc.Input(id='expiry',
                placeholder = '1,2 or 3',
                className = "textbox",
                style=dict(
                    width=195,
                    verticalAlign="middle",
                    color='#506784'
                ),
            )

        ],
            style = {'margin-bottom': '1em' , 'display':'flex'},

#             style=dict(display='flex')
        ),

        html.Div([
            html.Button('Submit', id='submit',style = {'margin-left': '10em'}),
        ]),

        dcc.Graph(id='plot'),

        dcc.Graph(id='graph_2000'),

        dcc.Graph(id='graph_2004'),

        dcc.Graph(id='graph_2008'),

        dcc.Graph(id='graph_2012'),

        dcc.Graph(id='graph_2016'),
])

@app.callback(Output('plot', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plotfunc(submit,ccy2,optiontype,expiry,strike):
    return traded_plot(ccy2)


@app.callback(Output('graph_2000', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plot2000(submit,ccy2,optiontype,expiry,strike):
    year = election_dates[0]
    return options_plot(strike,expiry,optiontype,ccy2,year)

@app.callback(Output('graph_2004', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plot2004(submit,ccy2,optiontype,expiry,strike):
    year = election_dates[1]
    return options_plot(strike,expiry,optiontype,ccy2,year)

@app.callback(Output('graph_2008', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plot2008(submit,ccy2,optiontype,expiry,strike):
    year = election_dates[2]
    return options_plot(strike,expiry,optiontype,ccy2,year)

@app.callback(Output('graph_2012', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plot2012(submit,ccy2,optiontype,expiry,strike):
    year = election_dates[3]
    return options_plot(strike,expiry,optiontype,ccy2,year)

@app.callback(Output('graph_2016', 'figure'),
              Input('submit', 'n_clicks'),
              
              state=[State('ccy2', 'value'),
              State('optiontype', 'value'),
              State('expiry', 'value'),
              State('strike', 'value')])

def plot2016(submit,ccy2,optiontype,expiry,strike):
    year = election_dates[4]
    return options_plot(strike,expiry,optiontype,ccy2,year)


if __name__ == '__main__':
    app.run_server()