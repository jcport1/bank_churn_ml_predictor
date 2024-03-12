from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():
    # extract features for random forest model
    print("predicting...")

    gender_code = int(request.form['gender'])
    credit_score = int(request.form['credit-score'])
    age = int(request.form['age'])
    tenure = int(request.form['tenure'])
    balance = int(request.form['balance'])
    estimated_salary = int(request.form['salary'])
    credit_card = int(request.form['credit-card'])
    products_number = int(request.form['num-acct'])

    user_input = np.array([[gender_code, credit_score, age, tenure, balance, estimated_salary, credit_card, products_number]])

    print(user_input)

    prediction = model.predict(user_input)
    print(prediction)
    prediction_text = "Customer likely to churn" if prediction[0] == 1 else "Customer not likely to churn"
    return render_template('index.html', prediction_text=prediction_text)

if __name__ == "__main__":
    app.run()