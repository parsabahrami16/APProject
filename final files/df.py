import pandas as pd
import plotly.express as px 
import numpy 
from finalapp import*


#Define value & sort by it
DF['value'] = DF['total_points'] / DF['now_cost']
DF.sort_values(by='value',ascending=False,inplace=True)
best_df=DF.head(20)

#Piechart

#Define parameters & values of them
para_df = ['clean_sheets','goals_scored','assists','games_starts']
val_df = [best_df['clean_sheets'].mean()*4,best_df['goals_scored'].mean()*6,
        best_df['assists'].mean()*3,best_df['games_starts'].mean()*2]#Parameter.mean()
#Draw piechart with plotly express
fig_df = px.pie(values=val_df,names=para_df,title='Defenders parameters',labels=para_df
        ,color=para_df
       ,color_discrete_map={"clean_sheets":'0d2a63','goals_scored':'00a08b',
            'assists':'2e91e5','games_starts':'620042'
            })
fig_df.update_traces(textposition='inside', textinfo='percent+label')



#Sunburst chart
DF["strength_defence"] = DF['strength_defence_home']+DF['strength_defence_away']
#Define parameters
para_adv_ldf=["DF",'clean_sheets','goals_scored','assists','games_starts',"strenght_def","xg","xa","gca"]

#Define parents (the most influential parameters)
para_adv_pdf=["","DF","DF","DF","DF",'clean_sheets','goals_scored','assists','assists']

#Define values based on the relation between parent and child
val_adv_df=[0,best_df['clean_sheets'].mean()*4,best_df['goals_scored'].mean()*6,
        best_df['assists'].mean()*3,best_df['games_starts'].mean()*2
        ,best_df['clean_sheets'].mean()*4*0.2#ParentInfluence.mean()*regression
        ,best_df['goals_scored'].mean()*4
        ,best_df['assists'].mean()*3/2
        ,best_df['assists'].mean()*3*0.62]

#Draw sunburst with px
fig_adv_df = px.sunburst(names=para_adv_ldf,parents=para_adv_pdf, values=val_adv_df
                ,color=val_adv_df
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="Defenders Sunburst chart" 
                ,height=600
                ,width=600 )
#Show piechart & sunburst chart in app
def app():
    st.title('Defenders')
    st.plotly_chart(fig_df)#st.plotly:show plotlychart in app
    st.plotly_chart(fig_adv_df)

