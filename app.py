import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from models.train_model import train_model
from dataset.load_data import load_dataset
from utils.predictor import predict_flower

# Page settings
st.set_page_config(
    page_title="Iris ML Dashboard",
    page_icon="🌸",
    layout="wide"
)

# Load data and model
df, iris = load_dataset()
model, accuracy, iris = train_model()

# Sidebar
st.sidebar.title("🌸 Iris ML Dashboard")

page = st.sidebar.radio(
    "Navigation",
    ["Prediction", "Dataset Visualization", "Model Performance"]
)

st.sidebar.write("Model: Logistic Regression")
st.sidebar.write(f"Accuracy: {accuracy*100:.2f}%")

# ------------------- Prediction Page -------------------

if page == "Prediction":

    st.title("🌸 Iris Flower Prediction")

    st.write("Enter flower measurements to predict species.")

    col1, col2 = st.columns(2)

    with col1:
        sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.4)
        sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.4)

    with col2:
        petal_length = st.slider("Petal Length", 1.0, 7.0, 1.3)
        petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

    features = [
        sepal_length,
        sepal_width,
        petal_length,
        petal_width
    ]

    if st.button("Predict Species"):

        prediction = predict_flower(
            model,
            iris,
            features
        )

        st.success(f"Predicted Species: **{prediction}**")


# ------------------- Dataset Page -------------------

elif page == "Dataset Visualization":

    st.title("📊 Dataset Visualization")

    st.subheader("Dataset Preview")

    st.dataframe(df)

    st.subheader("Feature Distribution")

    fig, ax = plt.subplots()

    sns.histplot(df["sepal length (cm)"], kde=True)

    st.pyplot(fig)

    st.subheader("Pairplot")

    pairplot = sns.pairplot(df, hue="species")

    st.pyplot(pairplot)


# ------------------- Model Performance -------------------

elif page == "Model Performance":

    st.title("📈 Model Performance")

    st.metric(
        label="Model Accuracy",
        value=f"{accuracy*100:.2f}%"
    )

    st.write(
        "This model uses Logistic Regression to classify iris species."
    )

    st.write("Features used:")
    st.write(
        """
        - Sepal Length
        - Sepal Width
        - Petal Length
        - Petal Width
        """
    )