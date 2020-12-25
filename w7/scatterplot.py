import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
#posts=pd.read_excel('posts.xlsx')
#mffw=pd.read_excel('mffw.xlsx')
mf=pd.read_excel('mf.xlsx')
xa=st.selectbox('Select x-axis parameter!',list(mf.columns)[1:])
ya=st.selectbox('Select y-axis parameter!',list(mf.columns)[1:])
fig=px.scatter(mf,x=xa,y=ya,color='web_name')
st.write(fig)