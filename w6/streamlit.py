import streamlit as st
import pandas as pd
import plotly_express as px
x=st.slider('x')
st.write(x,'squared is',x*x)
#st.slider('abcd', min_value=3, max_value=None, value=None, step=2, format=None)
player=st.text_input('Enter Player')
st.write('The entered Player is',player)
gk=pd.read_excel('GK.xlsx')
fw=pd.read_excel('FW.xlsx')
df=pd.read_excel('DF.xlsx')
mf=pd.read_excel('MF.xlsx')
if st.checkbox('Show dataframe'):
    st.write(df)
#pos=st.multiselect('Show players with pos?',mf['position'].unique())
team=st.multiselect('Show players with team?',mf['team'].unique())
new_df=df[(df['team'].isin(team))]#&(mf['position'].isin(pos))]
st.write(new_df)
fig=px.scatter(mf,x='total_points',y='now_cost',color='web_name')
st.write(fig)

