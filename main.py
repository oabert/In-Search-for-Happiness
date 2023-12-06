import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In Search for Happiness')

x_option = st.selectbox('Select the data for the x-axis', ('GDP', 'Happiness', 'Generosity'))
y_option = st.selectbox('Select the data for the y-axis', ('GDP', 'Happiness', 'Generosity'))

st.subheader(f'{x_option} and {y_option}')

df = pd.read_csv('happy.csv')


match x_option:
    case 'GDP':
        x_array = gdp = df['gdp']
    case 'Happiness':
        x_array = df['happiness']
    case 'Generosity':
        x_array = df['generosity']

match y_option:
    case 'GDP':
        y_array = gdp = df['gdp']
    case 'Happiness':
        y_array = df['happiness']
    case 'Generosity':
        y_array = df['generosity']
figure = px.scatter(y=y_array, x=x_array, labels={'x': x_option, 'y': y_option})
st.plotly_chart(figure)