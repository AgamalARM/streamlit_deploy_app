import streamlit as st
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

x = requests.get('http://dexcom.invasso.com/api/dexcom/simulation', headers=headers)
y = x.json()


st.title("Dexcom sensors G6 Machine Learning Classification Algorithm Demo2")

# trend_name = st.sidebar.selectbox("Select trend", (
# "Flat", "Double up", "Double down", "Single up", "Single down", "Forty_five up", "Forty_five down"))
# reading_value = st.sidebar.number_input('The reading from Dexcom sensor')

trend_name = y['trend']
reading_value = y['sensor_treading_value']
student_id = y['student_id']

st.write('#### Student ID : ', student_id)
st.write('#### The reading value from Dexcom sensor is  ', reading_value)
st.write('#### The trend is ', trend_name)

st.header('The Classification :')


def get_result(reading, trend):
    if ((reading >= 80) and (reading <= 140)):
        st.write('### Class 3')
        st.write('### Normal')
        
    elif ((reading < 80) and (trend in ["Flat", "Double up", "Single up", "Forty_five up"])):
        st.write('### Class 2')
        st.write('### Low')
        color = st.color_picker('Alert', '#FFFF00')
        
    elif ((reading < 80) and (trend in ["Double down", "Single down", "Forty_five down"])):
        st.write('### Class 1')
        st.write('### Critical Low')
        color = st.color_picker('Alert', '#FF0000')
        
    elif ((reading > 140) and (trend in ["Double up", "Single up", "Forty_five up"])):
        st.write('### Class 5')
        st.write('### Critical High')
        color = st.color_picker('Alert', '#FF0000')
        
    elif ((reading > 140) and (trend in ["Flat", "Double down", "Single down", "Forty_five down"])):
        st.write('### Class 4')
        st.write('### High')
        color = st.color_picker('Alert', '#FFFF00')
       
        
        
########################################################################


# import requests
# import json

# res = requests.get("http://agamalarm101.pythonanywhere.com/")    ###("https://2c91-156-194-204-201.eu.ngrok.io/")
# st.write(res)
# data = res.json()
# st.write(data)
# st.write(data["Class"])




get_result(reading_value, trend_name)
