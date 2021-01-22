import pandas as pd
import plotly.express as px 
import numpy 
from finalapp import*



#Define value & sort by it
FW['value'] = FW['total_points'] / FW['now_cost']
FW.sort_values(by='value',ascending=False,inplace=True)
best_fw=FW.head(20)

#Piechart

#Define parameters & values of them
para_fw = ['goals_scored','assists','games_starts']
val_fw = [best_fw['goals_scored'].mean()*4,best_fw['assists'].mean()*3
        ,best_fw['games_starts'].mean()*2]#Parameter.mean()
#Draw piechart with plotly express
fig_fw = px.pie(values=val_fw,names=para_fw,title='Forwards parameters',labels=para_fw
        ,color=para_fw
       ,color_discrete_map={'goals_scored':'0d2a63',
            'assists':'00a08b','games_starts':'620042'})
fig_fw.update_traces(textposition='inside', textinfo='percent+label')


#Sunburst chart

#Define parameters
para_adv_lfw=["FW",'goals_scored','assists','games_starts',
                "xg","GoalPer90","GoalPerShot",
                "xa","gca","sca"]

#Define parents (the most influential parameters)
para_adv_pfw=["","FW","FW","FW",'goals_scored','goals_scored','goals_scored','assists','assists','assists']

#Define values based on the relation between parent and child
val_adv_fw=[0,best_fw['goals_scored'].mean()*4,best_fw['assists'].mean()*3
        ,best_fw['games_starts'].mean()*2
        ,best_fw['goals_scored'].mean()*4*0.75#ParentInfluence.mean()
        ,best_fw['goals_scored'].mean()*4*0.65
        ,best_fw['goals_scored'].mean()*4*0.88
        ,best_fw['assists'].mean()*3*0.62
        ,best_fw['assists'].mean()*3*0.89
        ,best_fw['assists'].mean()*3*0.44]

#Draw sunburst with px
fig_adv_fw = px.sunburst(names=para_adv_lfw,parents=para_adv_pfw, values=val_adv_fw
                ,color=val_adv_fw
                ,color_continuous_scale= px.colors.sequential.BuPu
                ,title="Forwards Sunburst chart"
                ,height=600#size chart
                ,width=600)

#Show piechart & sunburst chart in app
def app():
        st.title('Forwards')
        st.plotly_chart(fig_fw)#st.plotly:show plotlychart in app
        st.plotly_chart(fig_adv_fw)