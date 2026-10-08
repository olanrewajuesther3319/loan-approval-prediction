import streamlit as st
import pandas as pd
import joblib


# Load trained model
model = joblib.load("models/loan_approval_model.pkl")
model_features = joblib.load("models/model_features.pkl")


# Page configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💰",
    layout="centered"
)


# Title
st.title("💰 Loan Approval Prediction")
st.write(
    "Enter the applicant's information below to predict "
    "whether the loan is likely to be approved."
)


# Applicant information
st.header("Applicant Information")

ApplicantIncome = st.number_input(
    "Applicant Income",
    min_value=0,
    value=5000
)

CoapplicantIncome = st.number_input(
    "Coapplicant Income",
    min_value=0.0,
    value=2000.0
)

LoanAmount = st.number_input(
    "Loan Amount",
    min_value=0.0,
    value=150.0
)

Loan_Amount_Term = st.number_input(
    "Loan Term (days)",
    min_value=0.0,
    value=360.0
)

Credit_History = st.selectbox(
    "Credit History",
    [1, 0],
    format_func=lambda x: "Good" if x == 1 else "Poor"
)

Gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

Married = st.selectbox(
    "Married",
    ["Yes", "No"]
)

Dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

Education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

Self_Employed = st.selectbox(
    "Self Employed",
    ["Yes", "No"]
)

Property_Area = st.selectbox(
    "Property Area",
    ["Urban", "Semiurban", "Rural"]
)


# Prediction button
if st.button("Predict Loan Status"):

    applicant = pd.DataFrame({
        "ApplicantIncome": [ApplicantIncome],
        "CoapplicantIncome": [CoapplicantIncome],
        "LoanAmount": [LoanAmount],
        "Loan_Amount_Term": [Loan_Amount_Term],
        "Credit_History": [Credit_History],

        "Gender_Male": [Gender == "Male"],
        "Married_Yes": [Married == "Yes"],

        "Dependents_1": [Dependents == "1"],
        "Dependents_2": [Dependents == "2"],
        "Dependents_3+": [Dependents == "3+"],

        "Education_Not Graduate": [
            Education == "Not Graduate"
        ],

        "Self_Employed_Yes": [
            Self_Employed == "Yes"
        ],

        "Property_Area_Semiurban": [
            Property_Area == "Semiurban"
        ],

        "Property_Area_Urban": [
            Property_Area == "Urban"
        ]
    })


    # Ensure same feature order as training
    applicant = applicant[model_features]


    # Prediction
    prediction = model.predict(applicant)[0]
    probabilities = model.predict_proba(applicant)[0]


    approval_probability = probabilities[1] * 100
    rejection_probability = probabilities[0] * 100


    # Display result
    st.header("Prediction Result")


    if prediction == 1:
        st.success("✅ LOAN APPROVED")
    else:
        st.error("❌ LOAN REJECTED")


    st.write(
        f"**Approval Probability:** "
        f"{approval_probability:.2f}%"
    )

    st.write(
        f"**Rejection Probability:** "
        f"{rejection_probability:.2f}%"
    )

