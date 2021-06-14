import streamlit as st
import altair as alt
import pandas as pd
from sklearn import datasets
from PIL import Image
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt


image = Image.open('Cybersecurity.png')
st.image(image, use_column_width=True)

st.title('Cyber Security Price Prediction for Businesses.')
st.write("""
Use the choices below to predict how much it would cost for
a Cyber Security Specialist Team to provide their services for your organisation.

""")
data = pd.read_csv ('CyberPrices.csv')

X = data.drop(columns=['Price'])
y = data['Price']

#Sidebar with currency converter


#st.write("""
# Displaying X & y DataSets from imported CSV file.
#""")
#y
#X

#st.sidebar.header('Specify Input Parameters')

display = ("No", "Yes")
options = list(range(len(display)))

def user_input_features():
    Users = st.slider('Number of Users in Network',0,1000,100)
    Devices = st.slider('Number of End Devices in Network',0,1000,100)
    Sites = st.selectbox("How many sites require solutions?",('1','2','3'))
    Email = st.selectbox("Is Email Protection required?", options, format_func=lambda x: display[x])
    Firewall = st.selectbox("Virtual Firewall installation & Setup",options, format_func=lambda x: display[x])
    Antivirus = st.selectbox("Is Anti-Virus Software required?",options, format_func=lambda x: display[x])
    Cloud = st.selectbox("Is Cloud Protection required?",options, format_func=lambda x: display[x])
    MSSP = st.selectbox("Is a MSSP (Managed Security Service Provider required?",options, format_func=lambda x: display[x])
    Sec = st.selectbox(
        'What security of level is required?   1 = Low 2 = Medium 3 = High',
        ('1', '2', '3'))
    data = {'Users': Users, 
            'Devices': Devices, 
            'Sites': Sites, 
            'Email': Email,
            'Firewall': Firewall,
            'Antivirus': Antivirus,
            'Cloud': Cloud,
            'MSSP': MSSP,
            'Sec': Sec}
    features = pd.DataFrame(data, index=[0])
    return features
df = user_input_features()

model = LinearRegression()
model.fit(X, y)

prediction = model.predict(df)

st.header('Rough Cost Estimation.')
st.write(prediction)
st.write('---')


st.header('Specified Input Parameters (Raw Data)')
st.write(df)
st.write('---')

expander_bar = st.beta_expander("About this project")
expander_bar.markdown("""
* ** Libraries:** Streamlit, Pandas, Requests, Json, Matplotlib, Sklearn.
* ** Education:** Cyber Security & Networks | Teesside University, Uk.
* ** Credit:** Web app & Machine Learning model Built by [Connor Owens]. 

""")

chart = alt.Chart(data).mark_circle().encode(
    x = 'Devices', y='Price',tooltip =['Devices', 'Price']
)
st.write("How the Price is affected by the number of Devices.")
st.altair_chart(chart, use_container_width=True)
