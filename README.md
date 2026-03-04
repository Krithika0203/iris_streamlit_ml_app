# 🌸 Iris Flower Classification – Streamlit ML Dashboard

A Machine Learning Web Application built using Streamlit that predicts the species of an Iris flower based on its physical measurements.

This project demonstrates an end-to-end ML workflow including data loading, model training, prediction, visualization, and a user-friendly dashboard interface.

---

## 🚀 Project Overview

The application uses the Iris Dataset to train a Logistic Regression classification model that predicts the flower species based on:

- Sepal Length
- Sepal Width
- Petal Length
- Petal Width

Users can interact with the dashboard to enter measurements and instantly receive predictions.

---

## 🧠 Machine Learning Model

Algorithm Used:
- Logistic Regression

Evaluation:
- Train-Test Split
- Cross Validation
- Model Accuracy displayed in dashboard

---

## 📊 Features of the Application

✔ Interactive Streamlit dashboard  
✔ Real-time prediction of iris species  
✔ Dataset visualization with charts  
✔ Model accuracy display  
✔ Clean modular Python architecture  
✔ Easy deployment using Streamlit Cloud  

---

## 🖥️ Dashboard Pages

### 🔮 Prediction
- Input flower measurements
- Predict iris species instantly

### 📊 Dataset Visualization
- Dataset preview
- Feature distributions
- Pairplot relationships

### 📈 Model Performance
- Model accuracy metrics
- Model description

---

## 📂 Project Structure

iris_streamlit_ml_app
│
├── app.py  
├── requirements.txt  
├── README.md  
│
├── dataset  
│   └── load_data.py  
│
├── models  
│   └── train_model.py  
│
├── utils  
│   ├── predictor.py  
│   └── visualizer.py  

---

## 📦 Technologies Used

- Python  
- Streamlit  
- Scikit-learn  
- Pandas  
- Matplotlib  
- Seaborn  

---

## 📊 Dataset

The project uses the Iris dataset, one of the most widely used datasets for classification problems in machine learning.

Dataset features:

- 150 flower samples
- 4 numerical features
- 3 flower species

---

## 🌐 Deployment

This project can be deployed using Streamlit Community Cloud.

Steps:

1. Push the project to GitHub
2. Connect repository in Streamlit Cloud
3. Select app.py as the entry file
4. Deploy

---

⭐ If you found this project helpful, consider giving it a star on GitHub.
