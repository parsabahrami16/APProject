import pandas as pd
import plotly.express as px 
import numpy 
from finalapp import*


#df=pd.read_excel('DF.xlsx')


DF['value'] = DF['total_points'] / DF['now_cost']

DF["strength_defence"] = DF['strength_defence_home']+DF['strength_defence_away']

DF.sort_values(by='value',ascending=False,inplace=True)
best_df=DF.head(20)

para_df = ['clean_sheets','goals_scored','assists','games_starts']
val_df = [best_df['clean_sheets'].mean()*4,best_df['goals_scored'].mean()*6,
        best_df['assists'].mean()*3,best_df['games_starts'].mean()*2]


fig_df = px.pie(values=val_df,names=para_df,title='Defenders parameters',labels=para_df
        ,color=para_df
       ,color_discrete_map={"clean_sheets":'0d2a63','goals_scored':'00a08b',
            'assists':'2e91e5','games_starts':'620042'
            })
fig_df.update_traces(textposition='inside', textinfo='percent+label')



#Sunburst chart

para_adv_ldf=["DF",'clean_sheets','goals_scored','assists','games_starts',"strenght_def","xg","xa"]
para_adv_pdf=["","DF","DF","DF","DF",'clean_sheets','goals_scored','assists']
val_adv_df=[0,best_df['clean_sheets'].mean()*4,best_df['goals_scored'].mean()*6,
        best_df['assists'].mean()*3,best_df['games_starts'].mean()*2
        ,best_df['clean_sheets'].mean()*2
        ,best_df['goals_scored'].mean()*4,best_df['assists'].mean()*3/2]


fig_adv_df = px.sunburst(names=para_adv_ldf,parents=para_adv_pdf, values=val_adv_df
                ,color=val_adv_df
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="Defenders Sunburst chart" 
                ,height=600
                ,width=600 )

def app():
    st.title('Defenders')
    st.plotly_chart(fig_df)
    st.plotly_chart(fig_adv_df)

