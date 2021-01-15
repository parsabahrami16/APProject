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
DF["strength_defence"] = DF['strength_defence_home']//10+DF['strength_defence_away']//10
def posts_eval(post):
     var=globals()[post]
     return var
def app():
     price1=st.slider(label='Choose minimum price!',min_value=3.5,max_value=13.0,step=0.1,format='%s')
     #price2=st.slider(label='Choose maximum price!',min_value=3.5,max_value=13.0,step=0.1,format='%s')
     min=st.slider(label='Choose minimum minutes!',min_value=0,max_value=1620,step=1)
     string_list=['web_name','first_name','second_name','team_code','status','name','team_name','element_type']
     post = st.selectbox('Select Post!',['GK','DF','MF','FW'])
     form=st.checkbox('Show Regression!')
     #if post=='GK':
     df=posts_eval(post)
     new_df=df[(df['now_cost']>=price1*10) & (df['minutes']>=min)]
     #gk.drop(string_list,axis=1,inplace=True)
     menu=[x for x in df.columns if x not in string_list]
     xa=st.selectbox('Select x-axis parameter!',menu)
     ya=st.selectbox('Select y-axis parameter!',menu)
     if len(new_df)==0:
          fig=px.scatter(new_df,x=xa,y=ya)
     else:
          if form:
               fig=px.scatter(new_df,x=xa,y=ya,trendline='ols')
          else:
               fig=px.scatter(new_df,x=xa,y=ya,color='web_name')
     st.write(fig)
     
     #elif post=='DF':
     #     df=DF[(DF['now_cost']>=price1*10) & (DF['minutes']>=min)]
     #     #df.drop(string_list,axis=1,inplace=True)
     #     menu=[x for x in df.columns if x not in string_list]
     #     xa=st.selectbox('Select x-axis parameter!',menu)
     #     ya=st.selectbox('Select y-axis parameter!',menu)
     #     if form:
     #          fig=px.scatter(df,x=xa,y=ya,trendline='ols')
     #          st.write(fig)
     #     else:
     #          try:
     #               fig=px.scatter(df,x=xa,y=ya,color='web_name')
     #               st.write(fig)
     #          except:
     #               st.write('invalid cost/min!')
     #     
     #elif post=='MF':
     #     mf=MF[(MF['now_cost']>=price1*10) & (MF['minutes']>=min)]
     #     #mf.drop(string_list,axis=1,inplace=True)
     #     menu=[x for x in mf.columns if x not in string_list]
     #     xa=st.selectbox('Select x-axis parameter!',menu)
     #     ya=st.selectbox('Select y-axis parameter!',menu)
     #     if form:
     #          fig=px.scatter(mf,x=xa,y=ya,trendline='ols')
     #          st.write(fig)
     #     else:
     #          try:
     #               fig=px.scatter(mf,x=xa,y=ya,color='web_name')
     #               st.write(fig)
     #          except:
     #               st.write('invalid cost/min!')
     #elif post=='FW':
     #     fw=FW[(FW['now_cost']>=price1*10) & (FW['minutes']>=min)]
     #     #fw.drop(string_list,axis=1,inplace=True)
     #     menu=[x for x in fw.columns if x not in string_list]
     #     xa=st.selectbox('Select x-axis parameter!',menu)
     #     ya=st.selectbox('Select y-axis parameter!',menu)
     #     if form:
     #          fig=px.scatter(fw,x=xa,y=ya,trendline='ols')
     #          st.write(fig)
     #     else:
     #          try:
     #               fig=px.scatter(fw,x=xa,y=ya,color='web_name')
     #               st.write(fig)
     #          except:
     #               st.write('invalid cost/min!')
          
