from flask import Flask, render_template, request
import os
import cv2
import pytesseract
from transformers import pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the uploads directory exists
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Load pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")
emotion_analyzer = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text_input = request.form.get('text_input')
    image_file = request.files.get('image_input')

    if image_file:
        # Save the uploaded image
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image_file.filename)
        image_file.save(image_path)

        # Perform OCR on the image
        try:
            text_input = pytesseract.image_to_string(cv2.imread(image_path))
        except Exception as e:
            text_input = "Error during OCR processing. Please check the image file."

    # Analyze sentiment and emotion
    if text_input and text_input.strip():  # Ensure text_input is not empty
        try:
            sentiment_result = sentiment_analyzer(text_input)[0]
            emotion_result = emotion_analyzer(text_input)[0]
        except Exception as e:
            sentiment_result = {"label": "Error", "score": 0}
            emotion_result = {"label": "Error", "score": 0}
    else:
        sentiment_result = {"label": "No text provided", "score": 0}
        emotion_result = {"label": "No text provided", "score": 0}

    # Render the results page with the analysis results
    return render_template('results.html', 
                           text_input=text_input, 
                           sentiment=sentiment_result['label'], 
                           emotion=emotion_result['label'])

if __name__ == '__main__':
    app.run(debug=True)