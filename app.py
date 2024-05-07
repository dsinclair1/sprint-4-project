import pandas as pd
import streamlit as st
import plotly.express as px

cars = pd.read_csv(r"\sprint-4-project\vehicles_us.csv")

st.header('price by mileage')
mp_hist = px.histogram(cars, x='price', y='odometer')
st.write(mp_hist)

st.header('price by type')
type_hist = px.histogram(cars, x='price', y='type')
st.write(type_hist)

toggle = st.checkbox('Show model year', value=False)
if toggle:
    st.header('price by year')
    year_scatt = px.scatter(cars, x='price', y='days_listed', color='model_year')
    st.write(year_scatt)
else:
    st.header('price by list time')
    time_hist = px.histogram(cars, x='price', y='days_listed')
    st.write(time_hist)