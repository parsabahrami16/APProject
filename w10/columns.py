gk_list=['id','web_name','first_name','second_name','team'
       ,'now_cost','cost_change_start'
       ,'total_points','selected_by_percent','clean_sheets','goals_conceded','saves','minutes'
       ,'chance_of_playing_next_round','event_points'
       ,'value_season','value_form'
       ,'penalties_saved','bonus','bps'
       ,'cost_change_event','transfers_in_event', 'transfers_out_event'
       ,'form','points_per_game'
       ,'strength_defence_home','strength_defence_away'
       ,'dreamteam_count','in_dreamteam'

     ,"games_gk","games_starts_gk","minutes_90s" 

     ,"goals_against_per90_gk","shots_on_target_against","save_pct","clean_sheets_pct"
     ,"psxg_gk","psnpxg_per_shot_on_target_against","psxg_net_gk","psxg_net_per90_gk"
     ,"pens_att_gk","pens_allowed"
         
       
       ,'ict_index','influence'       
       ,'ict_index_rank_type', 'influence_rank_type','ict_index_rank','influence_rank'       
       ,'yellow_cards', 'red_cards'       
       ,'transfers_in','transfers_out'
       , 'ep_next'
       ,'status'            
       ,'own_goals'
       ,'team_code'
       ,'team_name'
       ,'element_type'
       ,'name'                    
       ]
#GK.reset_index(drop=True,inplace=True)
fw_list=['id','web_name','first_name','second_name','team'
       ,'now_cost','cost_change_start'
       ,'total_points','selected_by_percent','minutes','goals_scored','assists'
       ,'penalties_order','penalties_missed',"pens_won","pens_conceded"
       
       ,'chance_of_playing_next_round','event_points'
       ,'value_season','value_form'
       ,'bonus','bps'
       
       ,'yellow_cards', 'red_cards'
       
       ,'corners_and_indirect_freekicks_order'
       , 'direct_freekicks_order'
       
       ,'cost_change_event','transfers_in_event', 'transfers_out_event'
       ,'form','points_per_game'
       ,'strength_attack_home','strength_attack_away'
       ,'dreamteam_count','in_dreamteam'


    ,"goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90"
    ,"pens_made","pens_att"

    ,"xg","npxg","xg_per90","npxg_per90"
    ,"xa","xa_per90"
    ,"xg_xa_per90","npxg_xa_per90"

    ,"shots_on_target","shots_on_target_pct","shots_on_target_per90","goals_per_shot_on_target"

    ,"assisted_shots","passes_into_penalty_area","crosses_into_penalty_area"
    ,"passes_free_kicks","through_balls","crosses","corner_kicks"
    ,"gca","gca_per90","gca_passes_live","gca_passes_dead","gca_fouled"
    ,"sca","sca_per90","sca_passes_live","sca_passes_dead","sca_fouled"

    ,"games","games_starts","minutes_90s","minutes_per_game","minutes_pct"
    ,"games_complete","games_subs","minutes_per_sub","unused_subs"
       
    ,"points_per_match","on_goals_for","on_goals_against","on_xg_for","on_xg_against"
    ,"xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"

    ,"touches_att_3rd","touches_att_pen_area"


       ,'ict_index','influence','creativity','threat'
       ,'ict_index_rank_type', 'ict_index_rank'
       ,'influence_rank','influence_rank_type'
       ,'creativity_rank','creativity_rank_type'
       ,'threat_rank', 'threat_rank_type' 
       
            
       ,'transfers_in','transfers_out'
       ,'ep_next'
       ,'status'            
       ,'own_goals'
       ,'team_code'
       ,'team_name'
       ,'element_type'
       ,'name'           
            
        ]
#FW.reset_index(drop=True,inplace=True)
df_list=['id','web_name','first_name','second_name','team'
       ,'now_cost','cost_change_start'
       ,'total_points','selected_by_percent','minutes','clean_sheets','goals_scored','assists','goals_conceded'
       
       ,'penalties_order','penalties_missed',"pens_won","pens_conceded"
       ,'corners_and_indirect_freekicks_order'
       ,'direct_freekicks_order'
       
       ,'chance_of_playing_next_round','event_points'
       ,'value_season','value_form'
       ,'bonus','bps'       
       
       ,'yellow_cards', 'red_cards'
       
       ,'cost_change_event','transfers_in_event', 'transfers_out_event'
       ,'form','points_per_game'
       ,'dreamteam_count','in_dreamteam'
       ,'strength_attack_home','strength_attack_away'
       ,'strength_defence_home','strength_defence_away'       
       

    ,"goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90"
    ,"pens_made","pens_att"
    
    ,"xg","npxg","xg_per90","npxg_per90"
    ,"xa","xa_per90"
    ,"xg_xa_per90","npxg_xa_per90"

    ,"shots_on_target","shots_on_target_pct","shots_on_target_per90","goals_per_shot_on_target"
    
    ,"assisted_shots","passes_into_penalty_area","crosses_into_penalty_area"
    ,"passes_free_kicks","through_balls","crosses","corner_kicks"
    ,"gca","gca_per90","gca_passes_live","gca_passes_dead","gca_fouled"
    ,"sca","sca_per90","sca_passes_live","sca_passes_dead","sca_fouled"

    ,"games","games_starts","minutes_90s","minutes_per_game","minutes_pct"
    ,"games_complete","games_subs","minutes_per_sub","unused_subs"

    ,"points_per_match","on_goals_for","on_goals_against","on_xg_for","on_xg_against"
    ,"xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"

    ,"touches_att_3rd","touches_att_pen_area"
    ,"aerials_won_pct"
       
       
              
       ,'ict_index','influence','creativity','threat'
       ,'ict_index_rank_type', 'ict_index_rank'
       ,'influence_rank','influence_rank_type'
       ,'creativity_rank','creativity_rank_type'
       ,'threat_rank', 'threat_rank_type' 
       
              
       ,'transfers_in','transfers_out'
       , 'ep_next'
       ,'status'            
       ,'own_goals'
       ,'team_code'
       ,'team_name'
       ,'element_type'
       ,'name'
]
#DF.reset_index(drop=True,inplace=True)
mf_list=['id','web_name','first_name','second_name','team'
       ,'now_cost','cost_change_start'
       ,'total_points','selected_by_percent','minutes','goals_scored','assists','clean_sheets','goals_conceded'
       
       ,'penalties_order','penalties_missed',"pens_won","pens_conceded"
       ,'corners_and_indirect_freekicks_order'
       , 'direct_freekicks_order'
       
       ,'chance_of_playing_next_round','event_points'
       ,'value_season','value_form'
       ,'bonus','bps'       
       
       ,'yellow_cards', 'red_cards'
       
       ,'cost_change_event','transfers_in_event', 'transfers_out_event'
       ,'form','points_per_game'
       ,'dreamteam_count','in_dreamteam'
       ,'strength_attack_home','strength_attack_away'
       ,'strength_defence_home','strength_defence_away'  
        
    ,"goals_per90","assists_per90","goals_assists_per90","goals_pens_per90","goals_assists_pens_per90"
    ,"pens_made","pens_att"

    ,"xg","npxg","xg_per90","npxg_per90"
    ,"xa","xa_per90"
    ,"xg_xa_per90","npxg_xa_per90"
    
    ,"shots_on_target","shots_on_target_pct","shots_on_target_per90","goals_per_shot_on_target"

    ,"assisted_shots","passes_into_penalty_area","crosses_into_penalty_area"
    ,"passes_free_kicks","through_balls","crosses","corner_kicks"
    ,"gca","gca_per90","gca_passes_live","gca_passes_dead","gca_fouled"
    ,"sca","sca_per90","sca_passes_live","sca_passes_dead","sca_fouled"

    ,"games","games_starts","minutes_90s","minutes_per_game","minutes_pct"
    ,"games_complete","games_subs","minutes_per_sub","unused_subs"

        
    ,"points_per_match","on_goals_for","on_goals_against","on_xg_for","on_xg_against"
    ,"xg_plus_minus","xg_plus_minus_per90","xg_plus_minus_wowy"

    ,"touches_att_3rd","touches_att_pen_area"
           
       
       ,'ict_index','influence','creativity','threat'
       ,'ict_index_rank_type', 'ict_index_rank'
       ,'influence_rank','influence_rank_type'
       ,'creativity_rank','creativity_rank_type'
       ,'threat_rank', 'threat_rank_type' 
       
              
       ,'transfers_in','transfers_out'
       , 'ep_next'
       ,'status'            
       ,'own_goals'
       ,'team_code'
       ,'team_name'
       ,'element_type'
       ,'name']
#MF.reset_index(drop=True,inplace=True)