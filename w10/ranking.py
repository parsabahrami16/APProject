import pandas as pd
import streamlit as st
import plotly_express as px
import plotly.figure_factory as ff
from finalapp import*

gk=GK[GK['minutes']>700]
df=DF[DF['minutes']>700]
fw=FW[FW['minutes']>700]
mf=MF[MF['minutes']>700]
gk['rank']=0.04*gk['clean_sheets_pct']+(1/3)*(gk['saves']/gk['games_starts_gk'])-(1/2)*(gk['goals_conceded']/gk['games_starts_gk'])
mf['rank']=5*(mf['goals_scored']/mf['games_starts'])+3*(mf['assists']/mf['games_starts'])
df['rank']=4*(df['clean_sheets']/df['games_starts'])+6*(df['goals_scored']/df['games_starts'])+3*(df['assists']/df['games_starts'])-(1/2)*(df['goals_conceded']/df['games_starts'])
fw['rank']=4*(fw['goals_scored']/fw['games_starts'])+3*(fw['assists']/fw['games_starts'])


bestGK=gk[['web_name','rank']].sort_values('rank',ascending=False).head(10)
del bestGK['rank']
bestGK=ff.create_table(bestGK)
bestDF=df[['web_name','rank']].sort_values('rank',ascending=False).head(10)
del bestDF['rank']
bestDF=ff.create_table(bestDF)
bestMF=mf[['web_name','rank']].sort_values('rank',ascending=False).head(10)
del bestMF['rank']
bestMF=ff.create_table(bestMF)
bestFW=fw[['web_name','rank']].sort_values('rank',ascending=False).head(10)
del bestFW['rank']
bestFW=ff.create_table(bestFW)
def app():
    #post=st.selectbox('Select Post!',['gk','df','mf','fw'])
    #df=posts_eval(post)
    #df=df[['web_name','rank']].sort_values('rank',ascending=False).head(20)
    #st.write("Best"+post)
    #fig=px.bar(df,x='web_name',y="rank",color='web_name',color_discrete_sequence=px.colors.qualitative.G10)
    #st.plotly_chart(fig)
    
    col1, col2= st.beta_columns(2)
    with col1:
        st.write('Best Goalkeepers')
        st.plotly_chart(bestGK)
        st.write('Best Defenders')
        st.plotly_chart(bestDF)
    with col2:
        st.write('Best Midfielders')
        st.plotly_chart(bestMF)
        st.write('Best Forwards')
        st.plotly_chart(bestFW)