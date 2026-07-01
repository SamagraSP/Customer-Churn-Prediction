## Customer Churn Prediction using Artificial Neural Networks (ANN)

# Overview
Customer churn is one of the most critical challenges for subscription-based and service-oriented businesses. This project develops an **Artificial Neural Network (ANN)** 
using **TensorFlow/Keras** to predict whether a customer is likely to leave a company based on customer demographics, account information, and service usage patterns.
The model helps businesses identify customers at risk of churning, enabling proactive retention strategies and improving customer lifetime value.

# Objectives
1. Predict customer churn using historical customer data.
2. Build a deep learning model capable of learning complex relationships between customer features.
3. Evaluate model performance on unseen data.
4. Provide a baseline model that can be further optimized for production use.

# Target Variable
 
 Value -> Meaning  
 -------------------------
| 0    -> Customer Stays  |
| 1    -> Customer Churn  |
 -------------------------

# Model Architecture

The ANN consists of multiple fully connected layers with dropout regularization:-
1. Input Layer: 29 engineered features
2. Hidden Layer 1: 128 neurons (ReLU)
3. Dropout
4. Hidden Layer 2: 64 neurons (ReLU)
5. Dropout
6. Hidden Layer 3: 32 neurons (ReLU)
7. Output Layer: 1 neuron (Sigmoid)

# Training Configuration

| Parameter     -> Value               |
| -------------- --------------------- |
| Framework     -> TensorFlow / Keras  |
| Optimizer     -> Adam                |
| Loss Function -> Binary Crossentropy |
| Metric        -> Accuracy            |
| Epochs        -> 30                  |


# Model Performance

| Metric            ->  Score |
| -----------------  ---------|
| Training Accuracy ->  79.4% |
| Training Loss     ->  0.558 |
| Test Accuracy     ->  77.6% |
| Test Loss         ->  0.471 |

# Performance Summary
1. The model demonstrated stable convergence throughout training.
2. Training accuracy improved from approximately 74.7% to 79.4% over 30 epochs.
3. The model achieved 77.6% accuracy on the test dataset, indicating good generalization to unseen customer records.
4.  Dropout regularization helped reduce overfitting by maintaining a small gap between training and testing performance.

# Technologies Used
1. Python
2. TensorFlow
3. Keras
4. NumPy
5. Pandas
6. Matplotlib
7. Seaborn
8. Scikit-learn

# Future Improvements
1. Hyperparameter optimization
2. Batch Normalization
3. Early Stopping
4. Class imbalance handling (SMOTE or class weights)
5. Deployment using Flask, FastAPI, or Streamlit
