import df
import gk
import mf
import fw
import radarchart
import scatterplot
import streamlit as st

#Pie charts
PAGES_piecharts = {
    "GoalKeepers": gk,
    "Defenders": df,
    "Midifilers":mf,
    "Fowards":fw
}
st.sidebar.title('Posts Piecharts')
selection = st.sidebar.radio("PieChart", list(PAGES_piecharts.keys()))
page1 = PAGES_piecharts[selection]
page1.app()
#Radar chart and scatterplot
PAGES_radarchart={
 "Radar Chart":radarchart,
 "Scatter Plot":scatterplot
}
st.sidebar.title('Radarchart and scatterplot')
selection = st.sidebar.radio("Radar Scatter", list(PAGES_radarchart.keys()))
page1 = PAGES_radarchart[selection]
page1.app()