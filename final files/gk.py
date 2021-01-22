import pandas as pd
import plotly.express as px 
from finalapp import*


#Define value & sort by it
GK['value'] = GK['total_points'] / GK['now_cost']
GK.sort_values(by='value',ascending=False,inplace=True)
best_gk=GK.head(10)

#Piechart

#Define parameters & values of them
para_gk = ['clean_sheets','saves','penalties_saved',"games_starts_gk"]
val_gk = [best_gk['clean_sheets'].mean()*4,best_gk['saves'].mean()//3*1,#Parameter.mean()
        best_gk['penalties_saved'].mean()*5,best_gk['games_starts_gk'].mean()*2]
#Draw piechart with plotly express
fig_gk = px.pie(values=val_gk,names=para_gk,title='Goal Keepers parameters',labels=para_gk
        ,color=para_gk
        ,color_discrete_map={"clean_sheets":'0d2a63','penalties_saved':'2e91e5'
         ,'saves':'00a08b','games_starts_gk':'620042'})
fig_gk.update_traces(textposition='inside', textinfo='percent+label')


#Sunburst chart

GK["strength_defence"] = GK['strength_defence_home']//10+GK['strength_defence_away']//10
#Define parameters
para_adv_lgk=["GK",'clean_sheets','saves','penalties_saved',"games_starts_gk","save_pct","shoot_target","cleen_sheets_pct","strenght_def","psxg"]

#Define parents (the most influential parameters)
para_adv_pgk=["","GK","GK","GK","GK","saves","saves","clean_sheets","clean_sheets","saves"]

#Define values based on the relation between parent and child
val_adv_gk=[0,best_gk['clean_sheets'].mean()*4,best_gk['saves'].mean()//3*1,
        best_gk['penalties_saved'].mean()*5,best_gk['games_starts_gk'].mean()*2
        ,best_gk['saves'].mean()//3*0.13#ParentInfluence.mean()*regression
        ,best_gk['saves'].mean()//3*0.94
        ,best_gk['clean_sheets'].mean()*4*0.95
        ,best_gk['clean_sheets'].mean()*4*0.4
        ,best_gk['saves'].mean()//3*0.66]
#Draw sunburst with px
fig_adv_gk = px.sunburst(names=para_adv_lgk,parents=para_adv_pgk, values=val_adv_gk
                ,color=val_adv_gk
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="GoalKeepers Sunburst chart"
                ,height=600
                ,width=600)
#Show piechart & sunburst chart in app
def app():
    st.title('GoalKeepers')
    st.plotly_chart(fig_gk)
    st.plotly_chart(fig_adv_gk)
    