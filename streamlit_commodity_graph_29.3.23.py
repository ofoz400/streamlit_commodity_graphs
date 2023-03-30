import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px


df_commodities = pd.read_csv('kalimati_tarkari_dataset.csv')


Commodities = df_commodities['Commodity'].unique()

# by default- sets to show no commodity graph
selected_commodities = st.multiselect('Select commodity or group',
                                      Commodities, default=None)

# the displayed commodities
df_chosen = df_commodities[df_commodities['Commodity'].isin(selected_commodities)]


# slider- for date range setting 
start_year, end_year = st.select_slider(
    'Select a range of years',
    options=['2013', '2014', '2015', '2016', '2017', '2018', 
             '2019', '2020', '2021'],
    value=('2013', '2021')
)

st.write('You selected dates between', start_year, 'and', end_year)

# data for displayed commodities only to dates in picked years range
df_displayed= df_chosen.loc[ (df_chosen['Date']<end_year) & (df_chosen['Date']>start_year) , :]

fig = px.bar(df_displayed,"Date","Average",color="Commodity", barmode='group')
st.plotly_chart(fig, use_container_width=True)

