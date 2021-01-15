import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import streamlit as st
from finalapp import all_posts
def app():
    string_list=['web_name','first_name','second_name','team_code','status','name','team_name','element_type']
    menu=[x for x in all_posts.columns if x not in string_list]
    team=st.selectbox('select team!',all_posts['team_name'].unique())
    param=st.selectbox('select parameter!',menu)
    new_df=all_posts[all_posts['team_name']==team]
    new_df[param]=pd.to_numeric(new_df[param])
    new_df.sort_values(param,inplace=True,ascending=False)
    fig=px.bar(new_df,x='web_name',y=param,color='web_name',color_discrete_sequence=px.colors.qualitative.G10)
    fig.add_trace(go.Scatter(x=new_df['web_name'], y=new_df[param],name='',
                            line = dict(color='firebrick', width=4, dash='dot')))
    fig.update_layout(showlegend=False)
    st.write(fig)