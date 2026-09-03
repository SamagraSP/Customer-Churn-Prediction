# Customer Churn Prediction — Full-Stack Machine Learning Application

🚀 **Live Demo:** [Try the deployed application](https://customer-churn-prediction-site.onrender.com)


An end-to-end **Customer Churn Prediction web application** that uses an **Artificial Neural Network (ANN)** to predict whether a customer is likely to churn based on their demographic, account, and service-related information.

The project combines a **TensorFlow/Keras machine learning model** with a **Django backend** and a responsive **HTML, CSS, and JavaScript frontend**. Users can enter customer information through a web form and receive an instant churn prediction along with interactive insights comparing the customer with average churner behavior.

---

## 🚀 Project Overview

Customer churn is one of the most important challenges faced by subscription-based and service-oriented businesses.

This application provides a complete workflow:

**Customer Input → Django Backend → Preprocessing → ANN Model → Churn Prediction → Customer Insights & Visualizations**

A user fills out a customer information form, and the application processes the submitted data through the trained ANN model.

The application then displays:

* 🔴 **Churn Prediction**
* 📊 **Customer vs. Average Churner Comparison**
* 📈 **Feature-based Insight Graph**
* 💡 **Interpretable customer insights**

The goal is not only to predict churn but also to make the prediction easier to understand through visual analysis.

---

# ✨ Key Features

### 1. Customer Churn Prediction

Users can enter customer information through an interactive web form.

The application uses the trained ANN model to predict whether the customer is likely to churn.

**Prediction output:**

* `Churn`
* `No Churn`

---

### 2. Interactive Customer Form

The frontend provides a structured form where users can enter customer-related information such as:

* CustomerID
* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Multiple Lines
* Internet Service
* Online Security
* Online Backup
* Device Protection
* Tech Support
* Streaming TV
* Streaming Movies
* Contract
* Paperless Billing
* Payment Method
* Monthly Charges
* Total Charges

The submitted data is sent to the Django backend for processing and prediction.

---

### 3. Customer vs. Average Churner Comparison

After prediction, the application generates a comparison bar chart and insights showing the customer's values against the **average values of customers who churned**.

The comparison currently focuses on:

* **Tenure**
* **Monthly Charges**
* **Total Charges**

This helps users understand how the customer's profile compares with typical churned customers.

For example:

> A customer with low tenure and relatively high monthly charges may exhibit characteristics commonly associated with churn.

---

### 4. Full-Stack ML Architecture

The project integrates machine learning with a complete web application stack:

```text
Frontend
HTML + CSS + JavaScript
        ↓
Django Backend
        ↓
Data Preprocessing
        ↓
ANN Model
        ↓
Churn Prediction
        ↓
Visualization & Insights
```

---

# 🧠 Machine Learning Model

The prediction engine is built using an **Artificial Neural Network (ANN)** implemented with **TensorFlow/Keras**.

The model learns patterns from historical customer data and predicts the probability of customer churn.

### Model Architecture

```text
Input Layer
29 Engineered Features
        ↓
Dense Layer — 128 Neurons
ReLU Activation
        ↓
Batch Normalization
        ↓
Dropout
        ↓
Dense Layer — 64 Neurons
ReLU Activation
        ↓
Batch Normalization
        ↓
Dropout
        ↓
Dense Layer — 32 Neurons
ReLU Activation
        ↓
Batch Normalization
        ↓
Dropout
        ↓
Dense Layer — 16 Neurons
ReLU Activation
        ↓
Output Layer — 1 Neuron
Sigmoid Activation
        ↓
Churn Probability
```

The sigmoid output produces a probability that can be used to determine whether a customer is likely to churn.

---

# ⚙️ Training Configuration

| Parameter         | Value                     |
| ----------------- | ------------------------- |
| Framework         | TensorFlow / Keras        |
| Model             | Artificial Neural Network |
| Optimizer         | Adam                      |
| Loss Function     | Binary Crossentropy       |
| Evaluation Metric | Accuracy                  |
| Epochs            | 70                        |
| Input Features    | 29                        |

---

# 📊 Model Performance

The current model achieved the following results:

| Metric            |     Score |
| ----------------- | --------: |
| Training Accuracy | **80.1%** |
| Training Loss     | **0.434** |
| Test Accuracy     | **76.7%** |
| Test Loss         | **0.463** |

### Performance Summary

* The model achieved approximately **80.1% training accuracy**.
* The model achieved **76.7% accuracy on the test dataset**.
* The relatively small difference between training and test accuracy indicates reasonable generalization.
* Dropout layers were used to help reduce overfitting.
* The model provides a practical baseline for further experimentation and optimization.

---

# 🖥️ Application Interface

The application provides a web-based interface where users can:

1. Enter customer information.
2. Submit the form.
3. Receive a churn prediction.
4. Compare customer metrics with average churner metrics.
5. View feature-based insights.
6. Understand the factors associated with the prediction.

### Application Workflow

```text
             ┌─────────────────────┐
             │   Customer Form     │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │   Django Backend    │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │ Data Preprocessing  │
             └──────────┬──────────┘
                        ↓
             ┌─────────────────────┐
             │   ANN Prediction    │
             └──────────┬──────────┘
                        ↓
              ┌───────────────────┐
              │ Churn / No Churn  │
              └─────────┬─────────┘
                        ↓
       ┌────────────────┴────────────────┐
       ↓                                 ↓
┌─────────────────────┐        ┌─────────────────────┐
│ Customer vs Churner │        │ Feature-Based       │
│ Comparison Graph    │        │ Insight Graph       │
└─────────────────────┘        └─────────────────────┘
```

---

# 🛠️ Technologies Used

## Machine Learning

* **Python**
* **TensorFlow**
* **Keras**
* **Scikit-learn**
* **NumPy**
* **Pandas**

## Data Visualization

* **Matplotlib**
* **Seaborn**
* **JavaScript-based frontend visualizations** *(where applicable)*

## Backend

* **Django**
* **Python**

## Frontend

* **HTML5**
* **CSS3**
* **JavaScript**

---

# 🔄 Prediction Pipeline

The application follows the following pipeline:

### Step 1 — User Input

The user enters customer information through the web interface.

### Step 2 — Request Handling

The form data is submitted to the Django backend.

### Step 3 — Preprocessing

The input is transformed using the same preprocessing approach used during model training.

### Step 4 — ANN Prediction

The processed customer data is passed to the trained TensorFlow/Keras model.

### Step 5 — Prediction

The model generates a churn probability, which is converted into the final churn classification.

### Step 6 — Visualization

The application generates:

* Customer vs. average churner comparison
* Feature-based insight visualization

### Step 7 — Results

The user receives the prediction and supporting insights through the web interface.

---

# 📈 Example Insights

The visualization layer allows the application to provide additional context around a prediction.

For example, the customer can be compared against average churner behavior:

| Feature         |       Customer | Average Churner |
| --------------- | -------------: | --------------: |
| Tenure          | Customer value |   Average value |
| Monthly Charges | Customer value |   Average value |
| Total Charges   | Customer value |   Average value |

This comparison can help identify whether the customer's characteristics are similar to patterns observed among customers who previously churned.

---

# 🚀 Future Improvements

The project can be further enhanced with:

### Machine Learning

* Hyperparameter optimization
* Cross-validation
* ROC-AUC evaluation
* Precision, Recall, and F1-score
* Model explainability using SHAP or LIME

### Application

* Real-time probability score
* More detailed customer risk analysis
* Personalized retention recommendations
* Customer risk categories such as **Low / Medium / High**
* Improved interactive dashboards
* Prediction history
* User authentication
* Database integration
* REST API integration

### Deployment

The application can be deployed using platforms and services such as:

* Render
* Railway
* AWS
* Azure
* Google Cloud

---

# 🎯 Project Goals

This project demonstrates the integration of:

**Machine Learning + Deep Learning + Data Visualization + Backend Development + Frontend Development**

Rather than simply training a machine learning model, the project focuses on converting the model into a usable web application that allows users to interact with the prediction system and understand the results.

---

# 👨‍💻 Skills Demonstrated

This project demonstrates practical experience with:

* Machine Learning
* Deep Learning
* Artificial Neural Networks
* TensorFlow/Keras
* Data Preprocessing
* Feature Engineering
* Model Evaluation
* Data Visualization
* Python
* Django
* Backend Development
* Frontend Development
* HTML
* CSS
* JavaScript
* ML Model Integration
* End-to-End ML Application Development

---

# ⭐ Conclusion

The **Customer Churn Prediction** project combines an Artificial Neural Network with a Django-powered web application to create an end-to-end customer churn prediction system.

Users can submit customer information through a web interface, receive a churn prediction, and explore visual insights that compare their profile with historical churner behavior.

The project serves as a practical demonstration of how a machine learning model can be transformed into an interactive, user-facing application.

---

## 📌 Project Status

**Status: Completed — Full-Stack ML Application**

Further improvements are planned around model explainability, performance optimization, deployment, and advanced customer retention insights.

---

## ⭐ If you found this project useful

Consider giving the repository a **star ⭐** and exploring the project to see how machine learning can be integrated into a complete web application.
