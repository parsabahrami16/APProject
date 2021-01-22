import df
import gk
import mf
import fw
import radarchart
import scatterplot
import barchart
import ranking
import streamlit as st


#first page to select
PAGES_piecharts = {
    "GoalKeepers": gk,
    "Defenders": df,
    "Midfielders":mf,
    "Fowards":fw
}
st.sidebar.title("Parameters' Piecharts")
selection = st.sidebar.radio("Choose Post!", list(PAGES_piecharts.keys()))#choose page
page1 = PAGES_piecharts[selection]
page1.app()#call function app in choosen page

#second page to select
#Radar chart and scatterplot
PAGES_radarchart={
 "Radar Chart":radarchart,
 "Scatter Plot":scatterplot,
 "Bar Chart":barchart,
 "Best Players":ranking
}
st.sidebar.title('Compare Players!')
selection = st.sidebar.radio("Choose Option! Scroll down to see charts.", list(PAGES_radarchart.keys()))#choose page
page1 = PAGES_radarchart[selection]
page1.app()#call function app in choosen page