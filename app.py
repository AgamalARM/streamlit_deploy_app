import streamlit as st

st.title("Dexcom sensors G6 Machine Learning Classification Algorithm Demo2")

trend_name = st.sidebar.selectbox("Select trend", (
"Flat", "Double up", "Double down", "Single up", "Single down", "Forty_five up", "Forty_five down"))
reading_value = st.sidebar.number_input('The reading from Dexcom sensor')

st.write('#### The reading value from Dexcom sensor is ', reading_value)
st.write('#### The trend is ', trend_name)

st.header('The Classification :')


def get_result(reading, trend):
    if ((reading >= 80) and (reading <= 140)):
        st.write('### Normal')
        st.write('### The system will not send any alerts')
    elif ((reading < 80) and (trend in ["Flat", "Double up", "Single up", "Forty_five up"])):
        st.write('### Low')
        color = st.color_picker('Alert', '#FFFF00')
        st.write('### the system will send yellow alerts')
    elif ((reading < 80) and (trend in ["Double down", "Single down", "Forty_five down"])):
        st.write('### Critical Low')
        color = st.color_picker('Alert', '#FF0000')
        st.write('### the system will send red alerts')
    elif ((reading > 140) and (trend in ["Double up", "Single up", "Forty_five up"])):
        st.write('### Critical High')
        color = st.color_picker('Alert', '#FF0000')
        st.write('### the system will send red alerts')
    elif ((reading > 140) and (trend in ["Flat", "Double down", "Single down", "Forty_five down"])):
        st.write('### High')
        color = st.color_picker('Alert', '#FFFF00')
        st.write('### the system will send yellow alerts')
        
        
########################################################################


import requests
import json

res = requests.get("http://agamalarm101.pythonanywhere.com/")    ###("https://2c91-156-194-204-201.eu.ngrok.io/")
st.write(res)
data = res.json()
st.write(data)
st.write(data["Class"])




get_result(reading_value, trend_name)
