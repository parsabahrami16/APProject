import requests
import pandas as pd
import numpy as np
import time
from bsoup import*
from columns import*
url = 'https://fantasy.premierleague.com/api/bootstrap-static/'
r = requests.get(url)
json = r.json()
json.keys()
i+=7
my_bar.progress(i)
#st.write('Fantasy Loaded!')
elements_df = pd.DataFrame(json['elements'])
teams_df = pd.DataFrame(json['teams'])


def del_id_pl(df):#removing identical players from dataframes
    df.sort_values('player',inplace=True)
    df.reset_index(inplace=True,drop=True)
    for row in df.index:
        if row>0:
            try:
                if df['player'][row]==df['player'][row-1]:
                    if df['minutes_90s'][row]>df['minutes_90s'][row-1]:#checking minutes per 90
                        df.drop(index=row-1,inplace=True)
                    else:
                        df.drop(index=row,inplace=True)                    
            except:
                try:
                    if df['minutes'][row]>df['minutes'][row-1]: #checking minutes
                        df.drop(index=row-1,inplace=True)
                    else:
                        df.drop(index=row,inplace=True)
                except:
                    continue
    df.reset_index(inplace=True,drop=True)
for df in df_fbref_list:
    del_id_pl(df)


def del_null_fbref(df):#remove players who haven't played (fbref)
    for row in df.index:
        if df['games'][row]==0:
            df.drop(index=row,inplace=True)
    df.reset_index(inplace=True,drop=True)
del_null_fbref(pl_time)



pd.options.mode.chained_assignment = None
def correct_team_names(teams_df):
    for row in teams_df.index: #changing team names in fantasy stats to use in fbref
        team_name=teams_df['name'][row]
        if team_name=='Leicester':
            teams_df['name'][row]='Leicester City'
        if team_name=='Man City':
            teams_df['name'][row]='Manchester City'
        if team_name=='Man Utd':
            teams_df['name'][row]='Manchester Utd'
        if team_name=='Newcastle':
            teams_df['name'][row]='Newcastle Utd'
        if team_name=='Spurs':
            teams_df['name'][row]='Tottenham'
        if team_name=='Leeds':
            teams_df['name'][row]='Leeds United'
correct_team_names(teams_df)



teams_list=[]
for team in teams_df['name']:
    teams_list.append(team)



def add_team_name(df):#adding team name
    df['team_name']='' 
    for row in df.index: 
        team_id=df['team'][row]
        team_row=teams_df.loc[teams_df['id']==team_id]
        team_row.index=[0]
        team_name=team_row['name'][0]
        df['team_name'][row]=team_name



def remove_null_players(df):# remove players who haven't played yet (fantasy)
    for row in df.index: 
        if df['minutes'][row]==0.:
            df.drop(index=row,inplace=True)
    df.reset_index(inplace=True,drop=True)
    return df
global players
players=remove_null_players(elements_df)
add_team_name(players)




def update_position(df):#Updating position slot
    for row in df.index: 
        pos=df['element_type'][row]
        if pos==1:
            df['element_type'][row]='GK'
        if pos==2:
            df['element_type'][row]='DF'
        if pos==3:
            df['element_type'][row]='MF'
        if pos==4:
            df['element_type'][row]='FW'
update_position(players)




def add_full_name(df):#add full name to players
    df['name']=''
    for row in df.index:
        first_name=df['first_name'][row]
        web_name=df['web_name'][row]
        if first_name in web_name: #build a name for checking
            name=web_name
        else:
            name=first_name+" "+web_name
        df['name'][row]=name
add_full_name(players)



def correct_bad_names(df):
    df.loc[df['player']=='Jóhann Berg Guðmundsson','player']='Johann Berg Gudmundsson'
    df.loc[df['player']=='İlkay Gündoğan','player']='Ilkay Gündogan'
    df.loc[df['player']=='Carlos Vinícius','player']='Carlos Vinicius'
    df.loc[df['player']=='Łukasz Fabiański','player']='Lukasz Fabianski'
    df.loc[df['player']=='Tomáš Souček','player']='Tomas Soucek'
    df.loc[df['player']=='Dan Nlundulu','player']="Daniel N'Lundulu"



#merging
b.empty()
b.write('Merging Dataframes!')
pl_df_list=[pl_goal,pl_msc,pl_pass_type,pl_pass,pl_time,pl_pos,pl_shot,pl_std]
def find_names(df,players):
    df['id']=0
    correct_bad_names(df)
    df_groups=df.groupby('squad')
    pl_groups=players.groupby('team_name')    
    for team in teams_list:
        fbref=df_groups.get_group(team)
        fantasy=pl_groups.get_group(team)
        for row in fantasy.index:
            checked=False
            player_id=fantasy['id'][row]
            team_name=fantasy['team_name'][row]
            name=fantasy['name'][row]
            first_name=fantasy['first_name'][row]
            second_name=fantasy['second_name'][row]
            web_name=fantasy['web_name'][row]
            pos=fantasy['element_type'][row]
            for s_row in fbref.index:
                fb_name=fbref['player'][s_row]              
                fb_team=fbref['squad'][s_row]
                fb_pos=fbref['position'][s_row]
                if name==fb_name or first_name+' '+second_name==fb_name: #find names which are totally equal
                    checked=True
                    df.loc[df['player']==fb_name,'id']=player_id
                    fantasy.drop(index=row,inplace=True)
                    fbref.drop(index=s_row,inplace=True)
                    break
            if checked==False: #find names which are not totally equal
                for s_row in fbref.index:
                    fb_name=fbref['player'][s_row]              
                    fb_team=fbref['squad'][s_row]
                    fb_pos=fbref['position'][s_row]
                    if web_name in fb_name or second_name in fb_name:
                        df.loc[df['player']==fb_name,'id']=player_id
                        checked=True
                    elif (first_name in fb_name or fb_name in first_name) and pos in fb_pos:
                        df.loc[df['player']==fb_name,'id']=player_id
                        checked=True
            if checked==False:#winter transfers!
                df.loc[df['player']==name,'id']=player_id

for df in pl_df_list:#finding names
    find_names(df,players)
i+=11
my_bar.progress(i)



posts = players.groupby('element_type')
GK = posts.get_group('GK')
DF = posts.get_group('DF')
MF = posts.get_group('MF')
FW = posts.get_group('FW')



#find names for gk
gk_df_list=[pl_gk,pl_adv_gk] 
for df in gk_df_list:
    find_names(df,GK)



pd.options.mode.chained_assignment = None 
def add_cl(post,df,cl): #add columns from teams_df to players
    post[cl] = 0 
    for row in post.index:
        team_id = post['team'][row] 
        team_row = df.loc[df['id'] == team_id]  
        post[cl][row] = team_row[cl]




stg_list=['strength_attack_home','strength_attack_away','strength_defence_home','strength_defence_away']
for stg in stg_list: #adding strength defence & attack to DF & MF
    add_cl(DF,teams_df,stg)
    add_cl(MF,teams_df,stg)
add_cl(FW,teams_df,stg_list[0])#add to GK
add_cl(FW,teams_df,stg_list[1])
add_cl(GK,teams_df,stg_list[2])#add to FW
add_cl(GK,teams_df,stg_list[3])



def add_cl_fbref(post,fbref,cl_list): #add columns from fbref to fantasy
    for cl in cl_list:
        post[cl]=0.0
    for row in post.index:
        for cl in cl_list:
            player_id=post['id'][row]
            fb_row=fbref.loc[fbref['id']==player_id]
            fb_row.index=[0]
            post[cl][row]=fb_row[cl][0]

b.empty()
b.write('Finalizing!')
fbref_cl=[[pl_std,std_cl],[pl_shot,shot_cl],[pl_pass,pass_cl],[pl_pass_type,pass_type_cl] 
    ,[pl_pos,pos_cl], [pl_goal,goal_cl], [pl_msc,msc_cl] ,  [pl_time,time_cl]] #fbref dataframes with desired columns

fbref_gk_cl=[[pl_gk,gk_cl],[pl_adv_gk,adv_gk_cl]]
post_list=[DF,MF,FW]
for post in post_list: #updating posts with fbref data
    for cl in fbref_cl:
        add_cl_fbref(post,cl[0],cl[1])
    i+=3
    my_bar.progress(i)
    
for cl in fbref_gk_cl:
    add_cl_fbref(GK,cl[0],cl[1])
i+=3
my_bar.progress(i)
time.sleep(2)
my_bar.empty()
b.empty()
GK=GK[gk_list]
MF=MF[mf_list]
FW=FW[fw_list]
DF=DF[df_list]
all_posts=GK.append([DF,MF,FW])

