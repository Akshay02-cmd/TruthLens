from flask import Flask, render_template, request
import pickle
import os

# Initialize Flask app
app = Flask(__name__)

# Load ML model and vectorizer
model_path = os.path.join("model", "fake_news_model.pkl")
vectorizer_path = os.path.join("model", "vectorizer.pkl")

with open(model_path, 'rb') as model_file:
    model = pickle.load(model_file)

with open(vectorizer_path, 'rb') as vec_file:
    vectorizer = pickle.load(vec_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    news_text = request.form['news']
    
    if not news_text.strip():
        return render_template('index.html', prediction="Please enter valid news text.")

    # Transform and predict
    input_data = vectorizer.transform([news_text])
    prediction = model.predict(input_data)[0]

    # Convert prediction to label
    result = "✅ Likely Real News" if prediction == "REAL" else "⚠️ Warning: Likely Fake News"

    return render_template('index.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
