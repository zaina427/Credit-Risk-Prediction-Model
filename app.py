from flask import Flask, render_template, request
import joblib
import pandas as pd
import os

app = Flask(__name__)

model = joblib.load("credit_risk_model.pkl")

@app.route('/')
def index():
    print("Looking for templates in:", os.path.abspath(app.template_folder))
    return render_template('index.html')
@app.route('/predict', methods=['POST'])
def predict():
    if request.method =='POST':
        data = {
            'status': [int(request.form['status'])],
            'duration': [int(request.form['duration'])],
            'credit_history': [int(request.form['credit_history'])],
            'purpose': [int(request.form['purpose'])],
            'amount': [int(request.form['amount'])],
            'savings': [int(request.form['savings'])],
            'employment_duration':[int(request.form['employment_duration'])],
            'installment_rate': [int(request.form['installment_rate'])],
            'personal_status_sex': [int(request.form['personal_status_sex'])],
            'other_debtors': [int(request.form['other_debtors'])],
            'present_residence': [int(request.form['present_residence'])],
            'property': [int(request.form['property'])],
            'age': [int(request.form['age'])],
            'other_installment_plans': [int(request.form['other_installment_plans'])],
            'housing': [int(request.form['housing'])],
            'number_credits': [int(request.form['number_credits'])],
            'job': [int(request.form['job'])],
            'people_liable': [int(request.form['people_liable'])],
            'telephone': [int(request.form['telephone'])],
            'foreign_worker': [int(request.form['foreign_worker'])]
        }
        input_df = pd.DataFrame(data)
        prediction = model.predict(input_df)[0]
        result = "Good Customer (loan Approved)" if prediction == 1 else "Bad Customer (loan Rejected)"
        return render_template("index.html", prediction_text=result)
    
if __name__== "__main__":
    app.run(debug=True)
