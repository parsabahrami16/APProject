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
        ,color_discrete_map={"clean_sheets":'0d2a63','penalties_saved':'85660d'
         ,'saves':'00a08b','games_starts_gk':'620042'})
fig_gk.update_traces(textposition='inside', textinfo='percent+label')


def app():
    st.title('GoalKeepers')
    st.plotly_chart(fig_gk)