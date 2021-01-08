import streamlit as st
import pandas as pd
import plotly_express as px
import plotly.graph_objects as go
from finalapp import*
#posts=pd.read_excel('posts.xlsx')
#mffw=pd.read_excel('mffw.xlsx')
#gk=pd.read_excel('GK.xlsx')
#df=pd.read_excel('DF.xlsx')
#mf=pd.read_excel('MF.xlsx')
#fw=pd.read_excel('FW.xlsx')
def app():
    post = st.selectbox('Select Post!',['GK','DF','MF','FW'])
    if post=='GK':
         xa=st.selectbox('Select x-axis parameter!',list(GK.columns)[1:])
         ya=st.selectbox('Select y-axis parameter!',list(GK.columns)[1:])
         fig=px.scatter(GK,x=xa,y=ya,color='web_name')
         st.write(fig)
    elif post=='DF':
         xa=st.selectbox('Select x-axis parameter!',list(DF.columns)[1:])
         ya=st.selectbox('Select y-axis parameter!',list(DF.columns)[1:])
         fig=px.scatter(DF,x=xa,y=ya,color='web_name')
         st.write(fig)
    elif post=='MF':
         xa=st.selectbox('Select x-axis parameter!',list(MF.columns)[1:])
         ya=st.selectbox('Select y-axis parameter!',list(MF.columns)[1:])
         fig=px.scatter(MF,x=xa,y=ya,color='web_name')
         st.write(fig)
    elif post=='FW':
        xa=st.selectbox('Select x-axis parameter!',list(FW.columns)[1:])
        ya=st.selectbox('Select y-axis parameter!',list(FW.columns)[1:])
        fig=px.scatter(FW,x=xa,y=ya,color='web_name')
        st.write(fig)
