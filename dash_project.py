import dash
import dash_core_components as dcc
import dash_html_components as html
app = dash.Dash()
app.layout = html.Div(children = [
    html.H1('Hello Web App'),
    html.Div('''Dash Web App: Python'''),
    dcc.Graph(
        id = 'example-graph',
        figure = {
            'data' : [
                {
                    'x' : [1,2,3], 'y': [4,2,1] , 'type':'bar' , 'name':'Ahmd'
                },
                {
                    'x' : [2,1,3], 'y': [1,4,2] , 'type':'bar' , 'name':'Mumbai'
                }
            ],
            'layout' :{
                'title' : 'Dash Data Visualization'
            }
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug = True)