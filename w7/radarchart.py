import plotly_express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
#create 2 menus for selecting players
mf=pd.read_excel('MF.xlsx')
option1 = st.selectbox(
    'Select player 1 for comparison!',
     mf['name'].unique())
st.write('You selected: ', option1)
option2= st.selectbox(
    'Select player 2 for comparison!',
     mf['name'].unique())
st.write('You selected: ', option2)
if option1 and option2:
    pl1=mf[mf['name']==option1]#find the player row in dataframe
    pl2=mf[mf['name']==option2]
    pl1.set_index('name',inplace=True)
    pl2.set_index('name',inplace=True)
    elements=['goals_scored','assists','xg','xa','npxg'] # elements of comparison
    pl1=pl1[elements]
    pl2=pl2[elements]
    row1=list(pl1.loc[option1]) #create a list of values in comparison for 2 players
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
    fig.update_layout(
    polar=dict(
        radialaxis=dict(
        visible=True,
        range=[0,max(row1+row2)]
        )),
    showlegend=True
    )

    st.write(fig)
