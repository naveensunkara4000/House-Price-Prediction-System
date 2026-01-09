### 🏠 House Price Prediction System

**Month 4 – Machine Learning Fundamentals**  
**The Developers Arena | Data Science Internship**

---

## 📘 Project Overview
The **House Price Prediction System** is an end-to-end **machine learning project** developed as part of **Month 4 of The Developers Arena (TDA) Data Science Internship**.

The goal of this project is to build a **complete ML solution** for a real-world business problem, covering the full lifecycle:
- Data preprocessing & feature engineering
- Training and comparing multiple ML models
- Model evaluation and interpretation
- Model persistence and versioning
- Deployment using a simple web interface

This project demonstrates how machine learning can be applied to **predict property prices** and provide actionable business insights.

---

## 🎯 Business Problem
Accurately predicting house prices is crucial for:
- Real estate companies
- Buyers and sellers
- Investors and financial planners

Manual price estimation is error-prone and subjective.  
This system uses **machine learning models** trained on historical data to provide **data-driven price predictions**.

---

## 🛠️ Technologies Used
- **Python 3.8+**
- **Pandas & NumPy** – Data processing
- **Scikit-learn** – Machine learning algorithms
- **Flask** – Web application
- **Pickle** – Model persistence
- **Git & GitHub** – Version control

---

## 🗂️ Project Structure
```bash
House-Price-Prediction-System/
│
├── data/
│ └── house_prices.csv 
│
├── notebooks/
│ └── eda.ipynb 
│
├── src/
│ ├── data_preprocessing.py 
│ ├── model_training.py 
│ ├── model_evaluation.py 
│ ├── model_inference.py 
│
├── app/
│ ├── web_app.py 
│ └── templates/
│ └── index.html 
│
├── models/
│ └── model_v1.pkl 
│
├── tests/
│ └── test_model.py 
│
├── scripts/
│ └── run_training.py 
│
├── config/
│ └── config.py 
│
├── requirements.txt 
└── .gitignore
```

---

## 📊 Dataset Description
**File:** `data/house_prices.csv`

### Features
``` 
| Column | Description |
|------|------------|
| area | Area of the house (sqft) |
| bedrooms | Number of bedrooms |
| bathrooms | Number of bathrooms |
| age | Age of the property (years) |
| location | Location category |
| property_type | Type of property |
| price | Target variable (house price) |
```
---

## ⚙️ Setup Instructions

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/naveensunkara4000/House-Price-Prediction-System.git
cd House-Price-Prediction-System
```
2️⃣ Install Dependencies
      pip install -r requirements.txt

▶️ How to Run the Project
      🔹 Train the Model
           python scripts/run_training.py


Output:

  - Trains multiple ML models
  - Compares performance
  - Saves the best model to models/model_v1.pkl

🔹 Run the Web Application
    python app/web_app.py


**Open in browser:** ` http://127.0.0.1:5000 `


Enter house details to get a price prediction.

### 🤖 Machine Learning Models Used

  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - The best-performing model is automatically selected based on R² score.

### 📈 Model Evaluation Metrics

  - Mean Absolute Error (MAE)
  - R² Score

**Sample Output**
  Linear Regression -> MAE: ₹620,000 | R²: 0.71
  Decision Tree -> MAE: ₹510,000 | R²: 0.78
  Random Forest -> MAE: ₹425,000 | R²: 0.85

### 🔍 Feature Importance & Insights

  - Area (sqft) is the strongest predictor
  - Location significantly impacts price
  - Property age negatively affects value
  - More bedrooms increase property value

### 🌐 Web Application Features

  - User-friendly input form
  - Real-time price prediction
  - Input validation and error handling
  - Lightweight Flask-based deployment

### 🧪 Testing

  Basic unit tests are included to validate model predictions:

  python tests/test_model.py

### 📦 Deliverables

  - Complete ML pipeline
  - Trained model with evaluation
  - Feature engineering workflow
  - Web-based prediction interface
  - Professional project structure
  - GitHub-hosted repository

### 🚀 Internship Outcome

This project demonstrates:

  - End-to-end machine learning workflow
  - Practical feature engineering
  - Model comparison and evaluation
  - Deployment of ML models
  - Production-ready project structure

### 🧑‍💻 Author

- Name: Sunkara Naveen
- Internship: The Developers Arena – Data Science
- Month: Month 4 – Machine Learning Fundamentals
