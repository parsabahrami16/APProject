import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from finalapp import*


def posts_eval(post):
     var=globals()[post]#convert "post" to post
     return var

GK['save_pct']=GK['save_pct']*100
def app():
    post=st.selectbox(
    'Select Post!',['GK','DF','MF','FW'])
    df=posts_eval(post)
    #Select players by name
    option1 = st.selectbox(
    'Select player 1 for comparison!',
    df['name'].unique())
    option2= st.selectbox(
    'Select player 2 for comparison!',
    df['name'].unique())
    if option1 and option2:
      pl1=df[df['name']==option1]#find the player row in dataframe
      pl2=df[df['name']==option2]
      pl1.set_index('name',inplace=True)
      pl2.set_index('name',inplace=True)
      if post=='FW' or post=='MF':
        elements=['goals_scored','assists','xg','xa','npxg'] # elements of comparison
      elif post=='GK':
        elements=['clean_sheets_pct','saves','goals_conceded','save_pct','total_points']
      elif post=='DF':
        elements=['assists','clean_sheets','bonus','shots_on_target','gca']
      pl1=pl1[elements]
      pl2=pl2[elements]
      row1=list(pl1.loc[option1]) #create a list of parameters in comparison for 2 players
      row2=list(pl2.loc[option2])
      row1.append(row1[0]) # last value = first value 
      row2.append(row2[0])
      elements.append(elements[0])
      fig=go.Figure()
       #radar chart player1
      fig.add_trace(go.Scatterpolar(
           r=row1,
         theta=elements,
         name=option1
      ))
     #radar chart player2
      fig.add_trace(go.Scatterpolar(
          r=row2,
          theta=elements,
          name=option2
      ))
      #update range from 0 to max
      fig.update_layout(polar=dict( radialaxis=dict( visible=True, range=[0,max(row1+row2)] )),showlegend=True )  
      st.write(fig) 