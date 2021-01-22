import pandas as pd
import plotly.express as px 
from finalapp import*



#Define value & sort by it
MF['value'] = MF['total_points'] / MF['now_cost']
MF.sort_values(by='value',ascending=False,inplace=True)
best_mf=MF.head(35)

#Piechart

#Define parameters & values of them
para_mf = ['clean_sheets','goals_scored','assists','games_starts']
val_mf = [best_mf['clean_sheets'].mean()*1,best_mf['goals_scored'].mean()*5,
        best_mf['assists'].mean()*3,best_mf['games_starts'].mean()*2]#Parameter.mean()
#Draw piechart with plotly express
fig_mf = px.pie(values=val_mf,names=para_mf,title='Mildifiers parameters',labels=para_mf
        ,color=para_mf
       ,color_discrete_map={"clean_sheets":'2e91e5','goals_scored':'0d2a63',
            'assists':'00a08b','games_starts':'620042'})
fig_mf.update_traces(textposition='inside', textinfo='percent+label')


#SunBurst chart

#Define parameters
para_adv_lmf=["MF",'clean_sheets','goals_scored','assists','games_starts',"xg","pen_90","xa","gca","sca","ast_shot"]

#Define parents (the most influential parameters)
para_adv_pmf=["","MF","MF","MF","MF",'goals_scored','goals_scored','assists','assists','assists','assists']

#Define values based on the relation between parent and child
val_adv_mf=[0,best_mf['clean_sheets'].mean()*1,best_mf['goals_scored'].mean()*5,
        best_mf['assists'].mean()*3,best_mf['games_starts'].mean()*2
        ,best_mf['goals_scored'].mean()*5*0.72#ParentInfluence.mean()*regression
        ,best_mf['goals_scored'].mean()*5*0.70
        ,best_mf['assists'].mean()*3*0.64
        ,best_mf['assists'].mean()*3*0.76
        ,best_mf['assists'].mean()*3*0.66
        ,best_mf['assists'].mean()*3*0.62]

#Draw sunburst with px
fig_adv_mf = px.sunburst(names=para_adv_lmf,parents=para_adv_pmf, values=val_adv_mf
                ,color=val_adv_mf
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="Midfielders Sunburst chart"
                ,height=600
                ,width=600)

#Show piechart & sunburst chart in app
def app():
        st.title('Midfielders')
        st.plotly_chart(fig_mf)#st.plotly:show plotlychart in app
        st.plotly_chart(fig_adv_mf)