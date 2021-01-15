import pandas as pd
import plotly.express as px 
from finalapp import*


#gk=pd.read_excel('GK.xlsx')


GK['value'] = GK['total_points'] / GK['now_cost']


GK.sort_values(by='value',ascending=False,inplace=True)
best_gk=GK.head(10)

para_gk = ['clean_sheets','saves','penalties_saved',"games_starts_gk"]
val_gk = [best_gk['clean_sheets'].mean()*4,best_gk['saves'].mean()//3*1,
        best_gk['penalties_saved'].mean()*5,best_gk['games_starts_gk'].mean()*2]



fig_gk = px.pie(values=val_gk,names=para_gk,title='Goal Keepers parameters',labels=para_gk
        ,color=para_gk
        ,color_discrete_map={"clean_sheets":'0d2a63','penalties_saved':'2e91e5'
         ,'saves':'00a08b','games_starts_gk':'620042'})
fig_gk.update_traces(textposition='inside', textinfo='percent+label')


#Sunburst chart
para_adv_lgk=["GK",'clean_sheets','saves','penalties_saved',"games_starts_gk","save_pct","cleen_sheets_pct","psxg"]
para_adv_pgk=["","GK","GK","GK","GK","saves","clean_sheets","saves"]
val_adv_gk=[0,best_gk['clean_sheets'].mean()*4,best_gk['saves'].mean()//3*1,
        best_gk['penalties_saved'].mean()*5,best_gk['games_starts_gk'].mean()*2
        ,best_gk['saves'].mean()//6*1,best_gk['clean_sheets'].mean()*3,best_gk['saves'].mean()//9*1]


fig_adv_gk = px.sunburst(names=para_adv_lgk,parents=para_adv_pgk, values=val_adv_gk
                ,color=val_adv_gk
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="GoalKeepers Sunburst chart"
                ,height=600
                ,width=600)

def app():
    st.title('GoalKeepers')
    st.plotly_chart(fig_gk)
    st.plotly_chart(fig_adv_gk)
    