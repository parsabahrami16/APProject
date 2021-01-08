import pandas as pd
import plotly.express as px 
import numpy 
from finalapp import*



#fw=pd.read_excel('FW.xlsx')


FW['value'] = FW['total_points'] / FW['now_cost']

FW.sort_values(by='value',ascending=False,inplace=True)
best_fw=FW.head(20)


para_fw = ['goals_scored','assists','games_starts']
val_fw = [best_fw['goals_scored'].mean()*4,best_fw['assists'].mean()*3
        ,best_fw['games_starts'].mean()*2]


fig_fw = px.pie(values=val_fw,names=para_fw,title='Forwards parameters',labels=para_fw
        ,color=para_fw
       ,color_discrete_map={'goals_scored':'85660d',
            'assists':'862a16','games_starts':'620042'})
fig_fw.update_traces(textposition='inside', textinfo='percent+label')


def app():
        st.title('Forwards')
        st.plotly_chart(fig_fw)