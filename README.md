**Credit Risk Prediction System**
This project is an End-to-End Machine Learning Application that predicts whether a loan applicant is a "Good Customer" (Loan Approved) or a "Bad Customer" (Loan Rejected) based on their financial and personal profile.

**Dataset Overview**
The model is trained on the UCI German Credit Risk Dataset.

**Source:** UCI Machine Learning Repository

**Size:** 1000 records with 21 features.

**Key Features:** Status of checking account, Credit duration, Credit history, Savings, Employment status, Installment rate, Personal status, and more.

**Technical Pipeline**
**1. Data Preprocessing (Pandas)**
**Cleaning:** Removed duplicates and reset indices to ensure data integrity.

**Imputation:** Handled missing values (NaN) to prevent model errors.

**Label Encoding:** Converted categorical text data into numerical values so the machine learning algorithm could process them.

**2. Model Training (Scikit-Learn)**
**Data Split:** 80% Training, 20% Testing.

**Algorithm:** Random Forest Classifier. This ensemble method was chosen for its high accuracy and ability to handle complex relationships between features.

**Evaluation:** Performance was measured using an Accuracy Score, Confusion Matrix, and a detailed Classification Report (Precision, Recall, F1-Score).

**3. Web Deployment (Flask & Frontend)**
**Backend:** Used Flask to create a web server that loads the serialized model.pkl file and handles incoming prediction requests.

**Frontend:** Built a clean, responsive UI using HTML5 and CSS3 to allow users to input customer data easily.

**Integration:** Flask takes form data, converts it into a Pandas DataFrame, passes it to the model, and displays the result back on the webpage dynamically.

**Installation & Setup**
**Clone the repository:**

Bash
git clone https://github.com/your-username/Credit_Risk_Prediction.git
cd Credit_Risk_Prediction
Install dependencies:

Bash
pip install flask pandas joblib scikit-learn
Run the application:

Bash
python app.py
Access the app: Open http://127.0.0.1:5000 in your browser.

**Input Features**
To get a prediction, the model analyzes:

**Financials:** Credit amount, checking account status, savings account, and installment rate.

**History:** Credit history and existing credits at the bank.

**Personal:** Age, employment duration, housing, and job category.
