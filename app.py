import pandas as pd
import streamlit as st
import plotly.express as px

cars = pd.read_csv(r"vehicles_us.csv")

st.header('price by mileage')
mp_hist = px.histogram(cars, x='price', y='odometer', nbins=10)
st.write(mp_hist)

st.header('price by type')
type_hist = px.histogram(cars, x='price', y='type', nbins=10)
st.write(type_hist)

toggle = st.checkbox('Show model year', value=False)
if toggle:
    st.header('price by year')
    year_scatt = px.scatter(cars, x='price', y='days_listed', color='model_year')
    st.write(year_scatt)
else:
    st.header('price by list time')
    time_hist = px.histogram(cars, x='price', y='days_listed', nbins=10)
    st.write(time_hist)
