# Import required libraries
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Define external stylesheet
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Initialize the Dash application with external stylesheets
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# Load the Gapminder dataset
df_gapminder = px.data.gapminder()

# Available options for the dropdown
available_indicators = ['lifeExp', 'pop', 'gdpPercap']

# Define the layout of the application
app.layout = html.Div([
    html.H1('Gapminder Data Visualization', className='title'),
    
    html.Div([
        html.Div([
            html.P('Select X-axis features:', className='control_label'),
            dcc.Dropdown(
                id='xaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='gdpPercap',
                className='dcc_control'
            )
        ],
        className='pretty_container four columns'),

        html.Div([
            html.P('Select Y-axis features:', className='control_label'),
            dcc.Dropdown(
                id='yaxis-column',
                options=[{'label': i, 'value': i} for i in available_indicators],
                value='lifeExp',
                className='dcc_control'
            )
        ],
        className='pretty_container four columns')
    ], className='row'),

    html.Div([
        dcc.Graph(id='scatter-plot')
    ], className='pretty_container seven columns'),

    html.Div([
        html.P('Select year:', className='control_label'),
        dcc.Slider(
            id='year-slider',
            min=df_gapminder['year'].min(),
            max=df_gapminder['year'].max(),
            value=df_gapminder['year'].min(),
            marks={str(year): str(year) for year in df_gapminder['year'].unique()},
            step=None,
            className='dcc_control'
        )
    ], className='pretty_container five columns'),

], className='mainContainer')

# Callback to update the scatter plot
@app.callback(
    Output('scatter-plot', 'figure'),
    [Input('xaxis-column', 'value'),
     Input('yaxis-column', 'value'),
     Input('year-slider', 'value')]
)
def update_figure(xaxis_column_name, yaxis_column_name, year_value):
    dff = df_gapminder[df_gapminder['year'] == year_value]
    
    fig = px.scatter(dff, 
                     x=xaxis_column_name, 
                     y=yaxis_column_name,
                     color='continent',  # Coloring by continent
                     template="simple_white")

    fig.update_xaxes(title=xaxis_column_name)
    fig.update_yaxes(title=yaxis_column_name)
    fig.update_layout(transition_duration=500)

    return fig

# Run the application
if __name__ == '__main__':
    app.run_server(debug=True)
