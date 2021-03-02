import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

st.title('Features Related to Bankruptcy')

@st.cache
def load_data():
    df = pd.read_csv('data.csv')
    df['Bankrupt?'].replace({0:'No', 1: 'Yes'}, inplace=True)
    return df

data_load_state = st.text('Loading data...')
data = load_data()
data_load_state.text('Loading data done!')

if st.button('Show raw data'):
    st.subheader('Raw data')
    st.dataframe(data)

st.subheader('Visualization')
x = st.sidebar.selectbox(
    'The first feature:',
    data.columns.tolist()[1:],
    1)
y = st.sidebar.selectbox(
    'The second feature:',
    data.columns.tolist()[1:],
    2)
if x == y:
    st.write('Please select features different from each other.')
else:
    c = alt.Chart(data).mark_circle().encode(
        x=x,
        y=y,
        color='Bankrupt?',
        opacity=alt.value(0.3),
        tooltip=[x, y, 'Bankrupt?']
    ).interactive()

    st.altair_chart(c, use_container_width=True)