from flask import Flask, render_template, request
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
    return render_template('index.html', prediction_text="prediction goes here")

if __name__ == "__main__":
    app.run()