# -*- coding: utf-8 -*-
"""
Created on Friday January 13th 2023

@author: joshiggins
"""
# Importing full packages
import openpyxl
import streamlit as st
import time
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Importing data
df_tools = pd.read_excel('resume-dashboard-data.xlsx', sheet_name='Tools')
df_organizations = pd.read_excel('resume-dashboard-data.xlsx', sheet_name='Organizations')

# Configuring page details
st.set_page_config(page_title='JH Background',  layout='wide', page_icon=':circle:')

# This is the header
t1, t2 = st.columns((0.07,1)) 
t1.image('index.png', width=120)
t2.title("Joseph Higgins' Background")
# t2.markdown("TIPAC")

tab1 = st.tabs(["Background"])

# Creating Header Boxes
m1, m2, m3, m4, m5 = st.columns((1,1,1,1,1))

# Filling Header Boxes In
m1.write('')
m2.metric(label ='Furthest Education', value = 'Masters')
m3.metric(label ='Years of Experience', value = '5+')
m4.metric(label ='Passion', value = 'Data')
m5.write('')

fig = px.line(df_tools, 
            x="Year", 
            y="Tool", 
            color='Tool')

fig.update_layout(xaxis=dict(showgrid=False),
                yaxis=dict(showgrid=False),
                plot_bgcolor = "white",
                font=dict(
                                family="Helvetica",
                                size=14,
                                color="Black"
                            ))

fig.update_traces(line=dict(width=12))
fig.update_yaxes(title='')
fig.update_xaxes(title='')

st.plotly_chart(fig, use_container_width=True)

# # Organizations Worked
# fig = px.line(df_organizations, 
#             x="Year", 
#             y="Organization", 
#             color='Organization')

# fig.update_layout(xaxis=dict(showgrid=False),
#                 yaxis=dict(showgrid=False),
#                 plot_bgcolor = "white",
#                 font=dict(
#                                 family="Helvetica",
#                                 size=14,
#                                 color="Black"
#                             ))

# fig.update_traces(line=dict(width=12))
# fig.update_yaxes(title='')
# fig.update_xaxes(title='')

# g2.plotly_chart(fig, use_container_width=True)