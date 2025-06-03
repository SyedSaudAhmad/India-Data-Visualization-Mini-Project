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



temp = df.groupby('State').sum()
temp['Literacy rate'] = df.groupby(df['State'])['Literacy rate'].mean()
temp['Sex ratio'] = df.groupby(df['State'])['Sex ratio'].mean()

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
        st.text("")


        
        

        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.subheader(f"Top 10 States by {primary}")
                st.dataframe(temp[primary].sort_values(ascending=False)[:10], use_container_width=True)
        with col2 :
            with st.container(border=True):    
                st.subheader(f"Top 10 States by {Secondary}")
                st.dataframe(temp[Secondary].sort_values(ascending=False)[:10], use_container_width=True)

        st.text("")

        col1, col2, col3 = st.columns(3)
        with col1:
            with st.container(border=True):
                st.metric("Total Population:",temp['Population'].sum())
        with col2:
            with st.container(border=True):
                st.metric("Total States:", len(temp))    
        with col3:
            with st.container(border=True):
                st.metric("Total Districts:", df['District'].nunique())

        a,b,c,d,e,f, g = st.columns(7)
        with a:
            with st.container(border=True):
                st.metric("Total Hindus:", temp['Hindus'].sum())
        with b:
            with st.container(border=True):
                st.metric("Total Muslims:", temp['Muslims'].sum())
        with c:
            with st.container(border=True):
                st.metric("Total Christians:", temp['Christians'].sum())
        with d:
            with st.container(border=True):
                st.metric("Total Buddhists:", temp['Buddhists'].sum())
        with e:
            with st.container(border=True):
                st.metric("Total Jains:", temp['Jains'].sum())
        with f:
            with st.container(border=True):
                st.metric("Total Sikhs:", temp['Sikhs'].sum())
        with g:
            with st.container(border=True):
                st.metric("Other religions:", temp['Others Religions'].sum())

        st.text("")
        st.title("Map Analysis")
        st.text("")
        st.subheader(f"Primary Parameter - :blue[{primary}] is represented by :red[size]", divider=True)
        st.subheader(f"Secondary Parameter - :blue[{Secondary}] is represented by :red[colour]", divider=True)

        fig = px.scatter_mapbox(df, lat="Latitude", lon="Longitude", size=primary, color=Secondary,
                                color_continuous_scale=px.colors.cyclical.IceFire,
                                hover_name="District", hover_data=[ primary, Secondary],
                                zoom=4,size_max=12,mapbox_style="carto-positron",width=1600,height=900)
        
        
        st.plotly_chart(fig,use_container_width=True,autosize=False)

        




    else:
        # plot for state
        state_df = df[df['State'] == selected_state].set_index('District')
        st.title(f"{selected_state} Analysis")
        st.text("")
        col1, col2 = st.columns(2)
        with col1:
            with st.container(border=True):
                st.subheader(f"Top 10 Districts by {primary}")
                st.dataframe(state_df[primary].sort_values(ascending=False)[:10], use_container_width=True)
        with col2 :
            with st.container(border=True):    
                st.subheader(f"Top 10 Districts by {Secondary}")
                st.dataframe(state_df[Secondary].sort_values(ascending=False)[:10], use_container_width=True)
        st.text("")


        col1, col2, col3, col4 = st.columns(4)
        with col1:
            with st.container(border=True):
                st.metric("Overall Population:",state_df['Population'].sum())
        with col2:
            with st.container(border=True):
                st.metric("Total no. of Districts:", state_df.index.nunique())    
        with col3:
            with st.container(border=True):
                st.metric("Sex ratio:", round(state_df['Sex ratio'].mean()))
        with col4:
            with st.container(border=True):
                st.metric("Net Literacy rate:", round(state_df['Literacy rate'].mean()))
            
        a,b,c,d,e,f, g = st.columns(7)
        with a:
            with st.container(border=True):
                st.metric("Total Hindus:", state_df['Hindus'].sum())
        with b:
            with st.container(border=True):
                st.metric("Total Muslims:", state_df['Muslims'].sum())
        with c:
            with st.container(border=True):
                st.metric("Total Christians:", state_df['Christians'].sum())
        with d:
            with st.container(border=True):
                st.metric("Total Buddhists:", state_df['Buddhists'].sum())
        with e:
            with st.container(border=True):
                st.metric("Total Jains:", state_df['Jains'].sum())
        with f:
            with st.container(border=True):
                st.metric("Total Sikhs:", state_df['Sikhs'].sum())
        with g:
            with st.container(border=True):
                st.metric("Other religions:", state_df['Others Religions'].sum())        
        st.text("")


        st.title("Map Analysis")
        st.text("")

        st.subheader(f"Primary Parameter - :blue[{primary}] is represented by :red[size]", divider=True)
        st.subheader(f"Secondary Parameter - :blue[{Secondary}] is represented by :red[colour]", divider=True)

        fig = px.scatter_mapbox(state_df, lat="Latitude", lon="Longitude", size=primary, color=Secondary,
        hover_name=state_df.index, hover_data=[primary, Secondary],color_continuous_scale=px.colors.cyclical.IceFire,
                    zoom=7,size_max=35,mapbox_style="carto-positron",width=1600,height=900)
        
        st.plotly_chart(fig,use_container_width=True,autosize=False)


