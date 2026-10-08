# Loan Approval Prediction

## Project Overview

This project uses Machine Learning to predict whether a loan application will be **approved or rejected** based on the applicant's demographic, financial, and loan-related information.

The goal is to build a classification model that can assist financial institutions in making faster and more consistent loan approval decisions.

---

## Objective

Predict the loan approval status:

* **Y** → Loan Approved
* **N** → Loan Rejected

The target variable is:

```text
Loan_Status
```

---

## Dataset

The dataset contains **614 loan applications** with information about applicants and their loan requests.

### Features Used

* ApplicantIncome
* CoapplicantIncome
* LoanAmount
* Loan_Amount_Term
* Credit_History
* Gender
* Married
* Dependents
* Education
* Self_Employed
* Property_Area

The target variable `Loan_Status` was excluded from the input features because it is the variable being predicted.

---

## Data Preparation

The following preprocessing steps were performed:

1. Missing values were handled.
2. Categorical variables were converted into numerical values.
3. One-hot encoding was applied to categorical features.
4. The target variable was converted:

   * `Y` → `1`
   * `N` → `0`
5. The dataset was divided into training and testing sets.
6. Stratified sampling was used to maintain the class distribution.

The final feature matrix contained **14 features**.

---

## Machine Learning Models

Three classification models were tested:

1. Logistic Regression
2. Decision Tree
3. Random Forest

### Initial Model Performance

| Model               | Accuracy |
| ------------------- | -------: |
| Logistic Regression |   85.37% |
| Decision Tree       |   82.93% |
| Random Forest       |   85.37% |

---

## Hyperparameter Tuning

GridSearchCV was used to improve the performance of the Logistic Regression and Random Forest models.

After tuning:

| Model                     |   Accuracy |
| ------------------------- | ---------: |
| Tuned Logistic Regression | **86.18%** |
| Tuned Random Forest       |     85.37% |

The **Tuned Logistic Regression** model was selected as the final model because it achieved the highest test accuracy.

---

## Final Model

The final model is a **Tuned Logistic Regression classifier**.

### Performance

**Accuracy: 86.18%**

The model was evaluated using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

A confusion matrix was also visualized to understand the model's correct and incorrect predictions.

---

## Example Prediction

The model can accept a new applicant's information and predict whether the loan is likely to be approved.

Example applicant:

```text
Applicant Income: 5000
Coapplicant Income: 2000
Loan Amount: 150
Loan Term: 360
Credit History: 1
Gender: Male
Married: Yes
Dependents: 1
Education: Graduate
Self Employed: No
Property Area: Urban
```

Example prediction:

```text
Loan Status: APPROVED
Approval Probability: 72.45%
```

---

## Streamlit Application

A Streamlit web application was created to allow users to interact with the trained model without writing Python code.

The application allows users to enter applicant information and receive:

* Loan approval prediction
* Approval probability
* Rejection probability

### Run the Application

Clone the repository:

```bash
git clone <YOUR-GITHUB-REPOSITORY-URL>
```

Navigate into the project:

```bash
cd loan-approval-prediction
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Run the Streamlit application:

```bash
python -m streamlit run app.py
```

The application will open in your browser.

---

## Project Structure

```text
loan-approval-prediction/
│
├── app.py
│
├── data/
│   └── loan_data.csv
│
├── models/
│   ├── loan_approval_model.pkl
│   └── model_features.pkl
│
├── notebooks/
│   └── loan_approval_prediction.ipynb
│
├── .gitignore
├── README.md
└── requirements.txt
```

---

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Joblib
* Streamlit
* Jupyter Notebook
* Git & GitHub

---

## Machine Learning Workflow

```text
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Data Encoding
      ↓
Train/Test Split
      ↓
Model Training
      ↓
Model Evaluation
      ↓
Hyperparameter Tuning
      ↓
Final Model Selection
      ↓
Streamlit Deployment
```

---

## Future Improvements

Possible improvements to this project include:

* Testing additional machine learning algorithms
* Improving feature engineering
* Addressing class imbalance
* Adding more evaluation metrics
* Deploying the Streamlit application online
* Adding model explainability
* Improving the user interface

---

## Disclaimer

This project is for educational and portfolio purposes. It should not be used as the sole basis for real-world financial or loan approval decisions.
