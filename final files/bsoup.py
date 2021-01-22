import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import streamlit as st

my_bar=st.progress(0)#bar for loading progress

def read_fbref(url,columns):
    res=requests.get(url)
    comm=re.compile("<!--|-->")
    soup = BeautifulSoup(comm.sub("",res.text),'lxml')#remove comments in html code
    all_tables=soup.findAll("tbody")#find tables
    player_table=all_tables[1]#player data is in second table
    pre_df_player = dict()#dict for saving data
    rows_player = player_table.find_all('tr')#find rows
    for row in rows_player:
        if(row.find('th',{"scope":"row"}) != None):#check if row is found correctly
            for cl in columns:
                try:
                    cell = row.find("td",{"data-stat": cl})
                    a = cell.text.strip().encode()
                    text=a.decode("utf-8")
                    if text=='':
                        text=0
                    elif text.isdigit():
                        text=int(text)
                    elif '.' in text:
                        text=float(text)
                    elif type(text)==str:
                        if text[1]==',':#if text was 1,234 convert it to 1234
                            text=int(text.replace(',',''))
                    if cl in pre_df_player:
                        pre_df_player[cl].append(text)
                    else:
                        pre_df_player[cl] = [text]
                except:
                    continue
    df_player = pd.DataFrame.from_dict(pre_df_player)#dict to dataframe
    return df_player[columns]


url_main='https://fbref.com/en/comps/9/Premier-League-Stats'
url_std='https://fbref.com/en/comps/9/stats/Premier-League-Stats#all_stats_standard'#standard
url_gk='https://fbref.com/en/comps/9/keepers/Premier-League-Stats#all_stats_keeper'#gk
url_time='https://fbref.com/en/comps/9/playingtime/Premier-League-Stats#all_stats_playing_time'#playing time
url_adv_gk='https://fbref.com/en/comps/9/keepersadv/Premier-League-Stats#all_stats_keeper_adv'#advanced_gk
url_shot='https://fbref.com/en/comps/9/shooting/Premier-League-Stats#all_stats_shooting'#shooting
url_pass='https://fbref.com/en/comps/9/passing/Premier-League-Stats#all_stats_passing'#passing
url_pass_tp='https://fbref.com/en/comps/9/passing_types/Premier-League-Stats#all_stats_passing_types'#pass types
url_gca='https://fbref.com/en/comps/9/gca/Premier-League-Stats#all_stats_gca'#goal & shot creation
url_def='https://fbref.com/en/comps/9/defense/Premier-League-Stats#all_stats_defense'#defensive actions
url_pos='https://fbref.com/en/comps/9/possession/Premier-League-Stats#all_stats_possession'#possession
url_msc='https://fbref.com/en/comps/9/misc/Premier-League-Stats#all_stats_misc'#miscellaneous
url_list=[url_std,url_gk,url_time,url_adv_gk,url_shot,url_pass,url_pass_tp,url_gca,url_def,url_pos,url_msc]



#columns for loading dataframes from fbref
std_cl=["player","position","squad","games","games_starts","minutes","goals","assists","pens_made","pens_att","goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90","xg","npxg","xa","xg_per90","xa_per90","xg_xa_per90","npxg_per90","npxg_xa_per90"]
gk_cl=["player","position","squad","games_gk","games_starts_gk","minutes_gk","goals_against_gk","goals_against_per90_gk","shots_on_target_against","saves","save_pct","clean_sheets","clean_sheets_pct","pens_att_gk","pens_allowed"]
gk_adv_cl=["player","position","squad","minutes_90s","psxg_gk","psnpxg_per_shot_on_target_against","psxg_net_gk","psxg_net_per90_gk"]
shot_cl=["player","position","squad","minutes_90s","shots_on_target","shots_on_target_pct","shots_on_target_per90","goals_per_shot_on_target"]
pass_cl=["player","position","squad","minutes_90s","assisted_shots","passes_into_penalty_area","crosses_into_penalty_area"]
pass_type_cl=["player","position","squad","minutes_90s","passes_free_kicks","through_balls","crosses","corner_kicks"]
pos_cl=["player","position","squad","minutes_90s","touches_att_3rd","touches_att_pen_area"]
gca_cl=["player","position","squad","minutes_90s","sca","sca_per90","sca_passes_live","sca_passes_dead","sca_fouled","gca","gca_per90","gca_passes_live","gca_passes_dead","gca_fouled"]
msc_cl=["player","position","squad","minutes_90s","pens_won","pens_conceded","aerials_won_pct"]
time_cl=["player","position","squad","games","minutes","minutes_per_game","minutes_pct","minutes_90s","games_starts","games_complete","games_subs","minutes_per_sub","unused_subs","points_per_match","on_goals_for","on_goals_against","on_xg_for","on_xg_against","xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"]
cl_list=[std_cl,gk_cl,gk_adv_cl,shot_cl,pass_cl,pass_type_cl,pos_cl,gca_cl,msc_cl,time_cl]




i=0
b=st.empty()
b.write('Downloading Data!')
pl_adv_gk=read_fbref(url_adv_gk,gk_adv_cl)
i+=7
my_bar.progress(i)
pl_std=read_fbref(url_std,std_cl)
i+=7
my_bar.progress(i)
pl_shot=read_fbref(url_shot,shot_cl)
i+=7
my_bar.progress(i)
pl_pos=read_fbref(url_pos,pos_cl)
i+=7
my_bar.progress(i)
pl_time=read_fbref(url_time,time_cl)
i+=7
my_bar.progress(i)
pl_pass=read_fbref(url_pass,pass_cl)
i+=7
my_bar.progress(i)
pl_pass_type=read_fbref(url_pass_tp,pass_type_cl)
i+=7
my_bar.progress(i)
pl_msc=read_fbref(url_msc,msc_cl)
i+=7
my_bar.progress(i)
pl_gk=read_fbref(url_gk,gk_cl)
i+=7
my_bar.progress(i)
pl_goal=read_fbref(url_gca,gca_cl)
i+=7
my_bar.progress(i)

df_fbref_list=[pl_adv_gk,pl_std,pl_shot,pl_pos,pl_time,pl_pass,pl_pass_type,pl_msc,pl_gk,pl_goal]

#rename minutes columns for gk dataframe
pl_gk=pl_gk.rename({'minutes_gk':'minutes'},axis=1)
pl_gk['minutes_90s']=pl_gk['minutes']/90 #creating minutes_90s columns for pl_gk and pl_std
pl_std['minutes_90s']=pl_std['minutes']/90



#desired columns from fbref dataframes
std_cl=["games","games_starts","pens_made","pens_att","goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90","xg","npxg","xa","xg_per90","xa_per90","xg_xa_per90","npxg_per90","npxg_xa_per90"]
shot_cl=["minutes_90s","shots_on_target","shots_on_target_pct","shots_on_target_per90","goals_per_shot_on_target"]
pass_cl=["assisted_shots","passes_into_penalty_area","crosses_into_penalty_area"]
pass_type_cl=["passes_free_kicks","through_balls","crosses","corner_kicks"]
pos_cl=["touches_att_3rd","touches_att_pen_area"]
goal_cl=["sca","sca_per90","sca_passes_live","sca_passes_dead","sca_fouled","gca","gca_per90","gca_passes_live","gca_passes_dead","gca_fouled"]
msc_cl=["pens_won","pens_conceded","aerials_won_pct"]
time_cl=["minutes_per_game","minutes_pct","games_starts","games_complete","games_subs","minutes_per_sub","unused_subs","points_per_match","on_goals_for","on_goals_against","on_xg_for","on_xg_against","xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"]
gk_cl=["games_gk","games_starts_gk","goals_against_per90_gk","shots_on_target_against","save_pct","clean_sheets_pct","pens_att_gk","pens_allowed"]
adv_gk_cl=["minutes_90s","psxg_gk","psnpxg_per_shot_on_target_against","psxg_net_gk","psxg_net_per90_gk"]