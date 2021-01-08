import pandas as pd
import plotly.express as px 
import numpy 
#read excels
gk=pd.read_excel('GK.xlsx')
fw=pd.read_excel('FW.xlsx')
df=pd.read_excel('DF.xlsx')
mf=pd.read_excel('MF.xlsx')


#add value column to posts and sort by value
for post in [gk,fw,df,mf]:
    post['value'] = post['total_points'] / post['now_cost']
gk = gk.sort_values(by='value',ascending=False)
df = df.sort_values(by='value',ascending=False)
mf = mf.sort_values(by='value',ascending=False)
fw = fw.sort_values(by='value',ascending=False)

best_fw=fw.head(20)
best_mf=mf.head(35)
best_df=df.head(20)
best_gk=gk.head(10)



#columns wich has a direct influence on points
para_gk = ['clean_sheets','saves','penalties_saved',"games_starts_gk"]
val_gk = [best_gk['clean_sheets'].mean()*4,best_gk['saves'].mean()//3*1,
        best_gk['penalties_saved'].mean()*5,best_gk['games_starts_gk'].mean()*2]

para_df = ['clean_sheets','goals_scored','assists','games_starts']
val_df = [best_df['clean_sheets'].mean()*4,best_df['goals_scored'].mean()*6,
        best_df['assists'].mean()*3,best_df['games_starts'].mean()*2]

para_mf = ['clean_sheets','goals_scored','assists','games_starts']
val_mf = [best_mf['clean_sheets'].mean()*1,best_mf['goals_scored'].mean()*5,
        best_mf['assists'].mean()*3,best_mf['games_starts'].mean()*2]

para_fw = ['goals_scored','assists','games_starts']
val_fw = [best_fw['goals_scored'].mean()*4,best_fw['assists'].mean()*3
        ,best_fw['games_starts'].mean()*2]

#make pie chart for each posts
fig_gk = px.pie(values=val_gk,names=para_gk,title='Goal Keepers parameters',labels=para_gk
        ,color=para_gk
        ,color_discrete_map={"clean_sheets":'0d2a63','penalties_saved':'85660d'
         ,'saves':'00a08b','games_starts_gk':'620042'})
fig_gk.update_traces(textposition='inside', textinfo='percent+label')

fig_df = px.pie(values=val_df,names=para_df,title='Defenders parameters',labels=para_df
        ,color=para_df
       ,color_discrete_map={"clean_sheets":'0d2a63','goals_scored':'85660d',
            'assists':'862a16','games_starts':'620042'
            })
fig_df.update_traces(textposition='inside', textinfo='percent+label')

fig_mf = px.pie(values=val_mf,names=para_mf,title='Mildifiers parameters',labels=para_mf
        ,color=para_mf
       ,color_discrete_map={"clean_sheets":'0d2a63','goals_scored':'85660d',
            'assists':'862a16','games_starts':'620042'})
fig_mf.update_traces(textposition='inside', textinfo='percent+label')

fig_fw = px.pie(values=val_fw,names=para_fw,title='Forwards parameters',labels=para_fw
        ,color=para_fw
       ,color_discrete_map={'goals_scored':'85660d',
            'assists':'862a16','games_starts':'620042'})
fig_fw.update_traces(textposition='inside', textinfo='percent+label')

fig_gk.show()
fig_df.show()
fig_mf.show()
fig_fw.show()