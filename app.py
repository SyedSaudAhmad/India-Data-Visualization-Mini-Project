import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

st.set_page_config(layout='wide')
################################################################################################

df = pd.read_csv("india.csv")
for i in range(len(df.columns[:])):
    df.rename(columns={df.columns[i]: df.columns[i].replace("_", " ")}, inplace=True)

State_List = list(df['State'].unique())
State_List.insert(0, "Overall India")


################################################################################################

# Streamlit

st.sidebar.title("India Analysis Dashboard")

selected_state = st.sidebar.selectbox("Select State", State_List)

primary = st.sidebar.selectbox("Select Primary Parameter", sorted(df.columns[:]))
Secondary = st.sidebar.selectbox("Select Secondary Parameter", sorted(df.columns[:]))

plot = st.sidebar.button('Plot Graph')

#################################################################################################

if plot:
    

    if selected_state == "Overall India":
        # plot for india
        st.title("Overall India Analysis")

        st.subheader(f"Primary Parameter: {primary} represented by size")

        st.subheader(f"Secondary Parameter: {Secondary} represented by colour")

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=Secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
        hover_name="District", hover_data=[ primary, Secondary],
                    zoom=4,mapbox_style="carto-positron",width=1600,height=900)
        
        
        st.plotly_chart(fig,use_container_width=True,autosize=False)
    else:
        # plot for state
        st.title(f"{selected_state} Analysis")

        st.subheader(f"Primary Parameter: '{primary}' represented by 'size'")

        st.subheader(f"Secondary Parameter: '{Secondary}' represented by 'colour'")

        state_df = df[df['State'] == selected_state]

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=Secondary,
        hover_name="District", hover_data=[primary, Secondary],color_continuous_scale=px.colors.cyclical.IceFire,
                    zoom=6,mapbox_style="carto-positron",width=1600,height=900)
        
        st.plotly_chart(fig,use_container_width=True,autosize=False)