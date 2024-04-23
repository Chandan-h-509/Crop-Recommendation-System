import requests
import json
import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

lottie_coding = load_lottiefile("animation.json")
# lottie_coding = load_lottieurl("https://assets3.lottiefiles.com/packages/lf20_ftjfyyep.json")

with st.container():
    st.title("About Dataset")
    st.write("## Context")
    st.write(
        "Precision agriculture is in trend nowadays. It helps the farmers to get informed decision about the farming strategy. Here, I present you a dataset which would allow the users to build a predictive model to recommend the most suitable crops to grow in a particular farm based on various parameters."
    )

with st.container():
    st.write("---")
    df = pd.read_csv("E:\Crop Reccomendation Model\Crop_recommendation.csv")
    st.write("## Dataset")
    st.write(df)


with st.container():
    st.write("---")
    st.write("## Data Fields")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
        #st.write("##")
        st.write(
            """
            - **N**: Ratio of Nitrogen content in soil
            
            - **P**: Ratio of Phosphorous content in soil

            - **K**: ratio of Potassium content in soil

            - **Temperature**: Temperature in degree Celsius

            - **Humidity**: Relative humidity in %

            - **PH**: PH value of the soil

            - **Rainfall**: Rainfall in mm
            """
        )

    with right_column:
        st_lottie(lottie_coding, key="data",height=400)

with st.container():
    st.write("---")
    st.write("## Labels")
    st.write("There are a total of 22 labels. They are:")
    left_column, right_column = st.columns(2)
    with left_column:
        st.write(
            """
                - **rice**
                
                - **maize**

                - **chickpea**

                - **kidneybeans**

                - **pigeonpeas**

                - **mothbeans**

                - **mungbean**

                - **blackgram**

                - **lentil**

                - **pomegranate**

                - **banana**
                """
    )
        
    with right_column:
        st.write(
            """
                - **mango**
                
                - **grapes**

                - **watermelon**

                - **muskmelon**

                - **apple**

                - **orange**

                - **papaya**

                - **coconut**

                - **cotton**

                - **jute**

                - **coffee**
                """
    )