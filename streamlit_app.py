import streamlit as st
import pandas as pd
import plotly.express as px

# Load the Gapminder data using the new caching function
@st.cache_data
def load_data():
    df = px.data.gapminder()
    return df

df = load_data()

# Streamlit user interface
st.title("Gapminder Data Scatter Plot")

# User selects x and y axes
x_axis_options = df.select_dtypes(include=[float, int]).columns.tolist()  # Numeric columns for the axes
x_axis = st.selectbox("Choose a variable for the x-axis", x_axis_options, index=x_axis_options.index("gdpPercap"))
y_axis = st.selectbox("Choose a variable for the y-axis", x_axis_options, index=x_axis_options.index("lifeExp"))

# User selects year with a slider in increments of 5 years
min_year = int(df['year'].min())
max_year = int(df['year'].max())
year_step = 5
year = st.slider("Select Year", min_year, max_year, step=year_step, value=min_year)

# Filtering the data by the selected year
df_year = df[df['year'] == year]

# Create the scatter plot for the selected year
fig = px.scatter(df_year, x=x_axis, y=y_axis,
                 hover_data=['country', 'continent'], 
                 color='continent', 
                 title=f"Scatter Plot of {y_axis} vs {x_axis} for the year {year}")

# Display the plot
st.plotly_chart(fig)

