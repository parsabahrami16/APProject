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
       ,color_discrete_map={"clean_sheets":'0d2a63','goals_scored':'85660d',
            'assists':'862a16','games_starts':'620042'})
fig_mf.update_traces(textposition='inside', textinfo='percent+label')


def app():
        st.title('Mildifiers')
        st.plotly_chart(fig_mf)