import requests
import streamlit as st
from streamlit_lottie import st_lottie


st.set_page_config(page_title="Crop Recommender", page_icon=":tada:", layout="wide")


def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_FYx0Ph.json")

with st.container():
    st.subheader("Hello, welcome to our website :wave:")
    st.title("Crop Recommender")
    st.write("## About us :point_down:")
    st.write(
        "Our app is designed to assist you in making informed decisions about the crops you should grow based on various environmental parameters. Whether you are a seasoned farmer or new to agriculture, our tool can help you maximize your yields and make your farming practices more sustainable."
    )

with st.container():
    st.write("---")
    st.write("## How It Works")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("")
        #st.write("##")
        st.write(
            """
            - **Input Parameters**: Enter essential environmental parameters in the sidebar. These include Nitrogen (N), Phosphorus (P), Potassium (K), temperature, humidity, pH level, and rainfall.
            
            - **Get Crop Recommendation**: Click the "Get Crop Recommendation" button, and our app will analyze your input parameters to suggest the most suitable crop for your conditions.

            - **Expert Guidance**: While our tool can provide valuable recommendations, always remember to consult with agricultural experts for precise guidance and make the best decisions for your farm.
            """
        )

    # with right_column:
    #     st_lottie(lottie_coding, height=300, key="coding")

with st.container():
    st.write("---")
    st.write("## Why Use Our App")
    st.write(
        """
            - **Optimize Crop Selection**: Make data-driven decisions on crop selection to improve your agricultural practices and profitability.

            - **Environmental Sustainability**: Tailor your crop choices to your local climate and soil conditions, promoting sustainable farming.

            - **Easy to Use**: Our user-friendly interface makes it accessible for all farmers, from beginners to experts.

            - **Free and Accessible**: The Crop Recommendation App is free to use, available online, and ready to assist you anytime.

            Start using our app now and make more informed decisions about your crop selection for a successful harvest!
            """
    )