import streamlit as st
import pandas as pd
import plotly_express as px
from finalapp import*


GK["strength_defence"] = GK['strength_defence_home']//10+GK['strength_defence_away']//10
DF["strength_defence"] = DF['strength_defence_home']//10+DF['strength_defence_away']//10
def posts_eval(post):
     var=globals()[post]#Change "post" to post
     return var
def app():
     #define price & minutes sliders
     price1=st.slider(label='Choose minimum price!',min_value=3.5,max_value=13.0,step=0.1,format='%s')
     min=st.slider(label='Choose minimum minutes!',min_value=0,max_value=1620,step=1)
     string_list=['web_name','first_name','second_name','team_code','status','name','team_name','element_type']
     post = st.selectbox('Select Post!',['GK','DF','MF','FW'])
     form=st.checkbox('Show Regression!')#checkbox to show regression
     df=posts_eval(post)
     new_df=df[(df['now_cost']>=price1*10) & (df['minutes']>=min)]#change dataframe by sliders
     #gk.drop(string_list,axis=1,inplace=True)
     menu=[x for x in df.columns if x not in string_list]#remove columns which are not numeric
     #select parameters to compare
     xa=st.selectbox('Select x-axis parameter!',menu)
     ya=st.selectbox('Select y-axis parameter!',menu)
     if len(new_df)==0:#when choose nothing
          fig=px.scatter(new_df,x=xa,y=ya)
     else:
          if form:#choose regression mode
               fig=px.scatter(new_df,x=xa,y=ya,trendline='ols')
          else:
               fig=px.scatter(new_df,x=xa,y=ya,color='web_name')
     st.write(fig)#Draw scatterplot by conditions
     
