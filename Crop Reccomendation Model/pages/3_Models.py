import streamlit as st
from streamlit_lottie import st_lottie
import plotly.express as px
import pandas as pd

with st.container():
    st.title("Models")
    st.write("## Context")
    st.write(
        "4 models were used to predict the crop. The models used are as follows:"
    )
    st.write(
            """
            - **Decision Tree Classifier**
            
            - **Naive Bayes Classifier**

            - **Logistic Regression**

            - **Random Fores Classifier**
            """
        )
    
acc = [90, 98, 95, 99]
model = ['Decision Tree Classifier', 'Naive Bayes Classifier', 'Logistic Regression', 'Random Forest Classifier']
data = {"Accuracy": acc, "Model": model}
df = pd.DataFrame(data)

with st.container():
    st.write("---")
    st.write("## Model Comparison")
# Create a bar chart with custom styling
    fig = px.bar(
        df,
        x='Model',
        y='Accuracy',
        text='Accuracy',  # Display accuracy values on the bars
        labels={'Accuracy': 'Accuracy (%)', 'Model': 'Machine Learning Model'},
        # title='Model Accuracy Comparison',
        color='Accuracy',  # Color bars based on accuracy values
        color_continuous_scale=px.colors.sequential.Viridis,  # Choose a color scale
    )


    fig.update_layout(
        coloraxis_colorbar=dict(title='Accuracy (%)'),  # Customize color bar title
        font=dict(family='Arial', size=14, color='black'),  # Customize font
    )

# Display the chart using Streamlit
st.plotly_chart(fig, use_container_width=True)

st.write("#### Random Forest Classifier has the highest accuracy of 99%. Hence, it is used to predict the crop. ####")