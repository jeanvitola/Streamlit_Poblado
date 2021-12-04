#---------------------->Librerias y módulos<--------------------------------
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static
import folium
from streamlit_player import st_player


st.set_page_config(
page_title="Ex-stream-ly Cool App",
page_icon="🧊",
layout="wide",
initial_sidebar_state="expanded",
menu_items={
       'Get Help': 'https://www.extremelycoolapp.com/help',
       'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
     }
 )



primaryColor="#F63366"
backgroundColor="#FFFFFF"
secondaryBackgroundColor="#F0F2F6"
textColor="#262730"
font="sans serif"


a = st.sidebar.radio('Select one:', [1, 2])












#---------------------->Titulo de la página-----------------------------------
st.title("""
🏠¿Cuánto cuesta un PH en el Poblado?
**_by JeanVitola_** 

        
   Summary:
Hace algunos meses, las búsquedas de penthouses en El Poblado 🎵 aumentaron escandalosamente en nuestro portal. 
¿Coincidencia? Tal vez. Aquí te contamos.



""")

 

st.header('This is a header')



# First create a Github instance:



#---------------------->Mapa del Poblado----------------------------------


page=st.radio("Seleciona el tipo de mapa",["single Map", "Dual map"], index=0)

# center El Poblado
if page == "single Map":
    m = folium.Map(location=[6.227259, -75.5719699], zoom_start=13)
    
elif page=="Dual map":
    m = folium.plugins.DualMap(location=[6.227259, -75.5719699], zoom_start=13)
    
# add marker for El Poblado
tooltip = "El Poblado"
folium.Marker([6.227259, -75.5719699], popup="El Poblado", tooltip=tooltip).add_to(m)
# call to render Folium map in Streamlit
folium_static(m)

b= st.sidebar.radio('Select one:', [page,page])




#--------------------------------> Video <----------------------------------------------------------------
# Embed a youtube video
st_player("https://youtu.be/CmSKVW1v0xM")


#---------------------->Open Data-----------------------------------
df2 = pd.read_excel('datapobladoventa_clean.xlsx')
st.write(df2.head(20))

#Expandir los datos
with st.expander("See explanation"):
    
    st.write("""
    The chart above shows some numbers I picked for you.
    I rolled actual dice for these, so they're *guaranteed* to
        be random.
    """)
    st.image("https://static.streamlit.io/examples/dice.jpg")





st.subheader("Tamaño de la viviendas")
poblado_data=pd.DataFrame( df2["Size"].value_counts().head(200))
st.bar_chart(poblado_data)
st.caption('Datos tomados de mediante Web scraping.')
 #------------------------>Categorias<------------------------------------------------
 

#------------------------------------>## Demo
mean_price=df2["price"].mean()
mean_rooms=df2["rooms"].mean()
mean_bathrooms=df2["bathrooms"].mean()
mean_size=df2["Size"].mean()

st.header(mean_price)  #st. cambia el tamaña del texto

st.dataframe(df2)
#----widge temperature
col1, col2, col3 = st.columns(3)
col1.metric("Temperature", "70 °F", "1.2 °F")
col2.metric("Wind", "9 mph", "-8%")
col3.metric("Humidity", "86%", "4%")

import numpy as np
#---Chart_data
col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")
    
jean="https://static.streamlit.io/examples/owl.jpg "
c= st.sidebar.radio('Select one:', [jean])

# Info
