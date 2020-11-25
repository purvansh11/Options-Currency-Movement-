import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

app.layout = html.Div([
    html.Label('City Names'),
    dcc.Dropdown(
        options = [
            {
                'label' : 'New York City','value' : 'NYC'
            },
            {
                'label' : 'Montreal' , 'value' : 'MON'
            },
            {
                'label' : 'Ahmedabad' , 'value' : 'AHM'
            }
        ],
        value = 'AHM'
    ),

    html.Label('Multiple Dropdown'),
    dcc.Dropdown(
        options = [
            {
                'label' : 'New York City','value' : 'NYC'
            },
            {
                'label' : 'Montreal' , 'value' : 'MON'
            },
            {
                'label' : 'Ahmedabad' , 'value' : 'AHM'
            }
        ],
        value = ['AHM' , 'MON'],
        multi = True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
      options=[
         {'label': 'New York City', 'value': 'NYC'},
         {'label': u'Montréal', 'value': 'MTL'},
         {'label': 'San Francisco', 'value': 'SF'}
      ],
      value='SF'
   ),
	
   html.Label('Checkboxes'),
   dcc.Checklist(
      options=[
         {'label': 'New York City', 'value': 'NYC'},
         {'label': u'Montréal', 'value': 'MTL'},
         {'label': 'San Francisco', 'value': 'SF'}
      ],
      value=['MTL', 'SF']
   ),
   html.Label('Text Input'),
   dcc.Input(value = 'MTL' , type = 'text'),

    html.Label('Slider'),
    dcc.Slider(
        min = 0,
        max = 10,
        marks = {
            i: 'Label {}'.format(i) if i==1 else 'Label ' + str(i) for i in range(1,12)
        },
        value = 9
    )        
], style = {'columnCount' : 1}
)


if __name__ == '__main__':
    app.run_server(debug = True)