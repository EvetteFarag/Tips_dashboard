import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="Tips dashboard",
                    page_icon=None,
                    layout="wide",
                    initial_sidebar_state="expanded")

df = pd.read_csv("tip.csv")
st.sidebar.image("glass-jar.jpg")
st.sidebar.header("Tips dashboard")
st.sidebar.write("This dashboard is using Tips dataset drom seaborn for educational purposes.")
st.sidebar.write("")
st.sidebar.write("Filter your data :")
cat_filter = st.sidebar.selectbox("Categorical filtering",[None,'sex','smoker','day','time'])
num_filter = st.sidebar.selectbox("numerical filtering",[None,'total_bill','tip'])
Row_filter = st.sidebar.selectbox("Row filtering",[None,'sex','smoker','day','time'])
Col_filter = st.sidebar.selectbox("Col filtering",[None,'sex','smoker','day','time'])



st.sidebar.write("")
st.sidebar.markdown("Made with :heart_eyes: by [Evette Farag](www.linkedin.com/in/evette-farag-7505151b6)")
#body
#row a
a1 ,a2 ,a3 ,a4 = st.columns(4)

a1.metric("Max.Total Bill",df['total_bill'].max())
a2.metric("Max.Tip",df['tip'].max())
a3.metric("Min.Total Bill",df['total_bill'].min())
a4.metric("Min.Tip Bill",df['tip'].min())

#row b
st.subheader("***Total_bill   VS . Tips***")

fig = px.scatter(data_frame=df,
                 x='total_bill',
                 y='tip',
                 color=cat_filter,
                 size=num_filter,
                 facet_col=Col_filter,
                 facet_row=Row_filter)
st.plotly_chart(fig, use_container_width=True)

#row c

c1 ,c2 , c3 = st.columns((4,3,3))

with c1:
    st.write("Sex VS Total Bills")
    fig = px.bar(data_frame=df ,x='sex',y='total_bill',color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.write("Smoker / Non-Smoker VS Tips")
    fig = px.pie(data_frame=df ,names='smoker',values='tip',color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)

with c3:
    st.write("Days VS Tips")
    fig = px.pie(data_frame=df ,names='day',values='tip',hole=.4,color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
    