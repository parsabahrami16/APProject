import pandas as pd
import plotly.express as px 
from finalapp import*



#mf=pd.read_excel('MF.xlsx')


MF['value'] = MF['total_points'] / MF['now_cost']


MF.sort_values(by='value',ascending=False,inplace=True)
best_mf=MF.head(35)


para_mf = ['clean_sheets','goals_scored','assists','games_starts']
val_mf = [best_mf['clean_sheets'].mean()*1,best_mf['goals_scored'].mean()*5,
        best_mf['assists'].mean()*3,best_mf['games_starts'].mean()*2]



fig_mf = px.pie(values=val_mf,names=para_mf,title='Mildifiers parameters',labels=para_mf
        ,color=para_mf
       ,color_discrete_map={"clean_sheets":'2e91e5','goals_scored':'0d2a63',
            'assists':'00a08b','games_starts':'620042'})
fig_mf.update_traces(textposition='inside', textinfo='percent+label')


para_adv_lmf=["MF",'clean_sheets','goals_scored','assists','games_starts',"xg","goals_pens_per90","xa","gca","sca","assisted_shot"]
para_adv_pmf=["","MF","MF","MF","MF",'goals_scored','goals_scored','assists','assists','assists','assists']
val_adv_mf=[0,best_mf['clean_sheets'].mean()*1,best_mf['goals_scored'].mean()*5,
        best_mf['assists'].mean()*3,best_mf['games_starts'].mean()*2
        ,best_mf['goals_scored'].mean()*4
        ,best_mf['goals_scored'].mean()*2
        ,best_mf['assists'].mean()*2
        ,best_mf['assists'].mean()*1.5
        ,best_mf['assists'].mean()*1
        ,best_mf['assists'].mean()*1.5]


fig_adv_mf = px.sunburst(names=para_adv_lmf,parents=para_adv_pmf, values=val_adv_mf
                ,color=val_adv_mf
                ,color_continuous_scale= px.colors.sequential.dense
                ,title="Midifilers Sunburst chart"
                ,height=600
                ,width=600)


def app():
        st.title('Mildifiers')
        st.plotly_chart(fig_mf)
        st.plotly_chart(fig_adv_mf)