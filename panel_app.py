import panel as pn
import plotly.express as px

# Load the Gapminder dataset from Plotly
gapminder_df = px.data.gapminder()

# Create a function to generate the scatter plot
def create_scatter(x_axis, y_axis, year):
    # Filter the data for the selected year
    filtered_data = gapminder_df[gapminder_df['year'] == year]
    
    # Create the scatter plot
    fig = px.scatter(filtered_data, x=x_axis, y=y_axis, 
                     color='continent', 
                     hover_name='country', size_max=55)
    
    return fig

# Widgets for the X and Y axes selection
x_axis_select = pn.widgets.Select(name='X Axis', options=['gdpPercap', 'lifeExp', 'pop'])
y_axis_select = pn.widgets.Select(name='Y Axis', options=['gdpPercap', 'lifeExp', 'pop'])

# Slider for the year selection
year_slider = pn.widgets.IntSlider(name='Year', start=1952, end=2007, step=5, value=1952)

# Reactive function to update the plot based on widgets' values
@pn.depends(x_axis_select.param.value, y_axis_select.param.value, year_slider.param.value)
def update_plot(x_axis, y_axis, year):
    return create_scatter(x_axis, y_axis, year)

# Create a Panel layout
layout = pn.Column(pn.Row(x_axis_select, y_axis_select, year_slider), update_plot)

# Serve the Panel app
layout.servable()
