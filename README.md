# Heart_Disease_Prediction
# Heart Disease Prediction Using Machine Learning

This project is a full-stack machine learning application that predicts the likelihood of heart disease based on patient clinical data. The system compares multiple classification models and deploys the selected model using FastAPI (backend) and Streamlit (frontend) for real-time prediction.

---

## Project Overview

Heart disease remains one of the leading causes of death worldwide. Early detection through predictive models can assist healthcare professionals in identifying high-risk patients and taking preventive measures.

This project builds and evaluates several supervised learning models and deploys the most suitable model as a web-based application.

---

## Machine Learning Process

1. Exploratory Data Analysis (EDA)
2. Model training and comparison:
   - Logistic Regression
   - Decision Tree
   - Random Forest
   - Support Vector Machine (SVM)
3. Model evaluation using:
   - Recall
   - Precision
   - F1-score
   - ROC-AUC
4. Final model selection based on performance
5. Deployment using FastAPI and Streamlit

---

## Dataset Information

- Number of records: 400  
- Number of features: 13  
- Target variable: `heart_disease`  
  - 0: No heart disease  
  - 1: Heart disease  

All features are numerical and required no encoding.

---

## Model Selection

Since this is a healthcare-related application, recall was treated as the primary evaluation metric to reduce false negatives. The Random Forest model achieved the highest recall among the evaluated models and was selected for deployment.

---

## How to Run the Application Locally

### Start Backend

```bash
cd backend
python main.py
```

The backend runs at:
```
http://127.0.0.1:8000
```

API documentation is available at:
```
http://127.0.0.1:8000/docs
```

---

### Start Frontend

Open a new terminal and run:

```bash
cd frontend
python -m streamlit run app.py
```

The web application will open automatically in your browser.

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Streamlit
- Joblib

---

## Evaluation Metrics

Primary Metrics:
- Recall
- Precision
- F1-score
- ROC-AUC

Secondary Metric:
- Accuracy

---
## Author
OM MUJUMDAR

Developed as a capstone machine learning project demonstrating the complete workflow from data analysis to deployment.

