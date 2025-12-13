#  Sentiment Analysis on Handwritten and E‑Text Documents

An **AI-powered NLP system** that converts handwritten text into digital text and performs **sentiment and emotion analysis** using **Machine Learning and Deep Learning techniques**.

---

##  Project Overview

This project is designed to analyze **human emotions and sentiment** from both **handwritten documents and electronic text**. The system first extracts text from handwritten images using a **CNN–BiLSTM based OCR pipeline**, then applies NLP models to classify the text into **sentiment** and **emotion categories**.

It is particularly useful for applications such as:

* Feedback analysis
* Opinion mining
* Academic and research document analysis
* Human–computer interaction systems

---

##  Key Features

### ✍️ Handwritten Text Processing

* Image upload support for handwritten documents
* Text extraction using **CNN–BiLSTM OCR + Tesseract**
* Noise removal and preprocessing for improved accuracy

### 🧠 Sentiment & Emotion Analysis

* Sentiment classification: **Positive | Negative | Neutral**
* Emotion detection: **Happiness, Sadness, Anger, Fear, Surprise**, etc.
* Supports both handwritten and plain text input

### 🖥️ User Interface

* Interactive UI for uploading images or entering text
* Real-time prediction results
* Clear visualization of sentiment and emotion outputs

---

## 🛠️ Tech Stack

### 🔹 Backend & AI

* Python
* Flask
* TensorFlow / Keras
* Transformers
* Scikit-learn

### 🔹 OCR & NLP

* CNN–BiLSTM OCR Model
* Tesseract OCR
* Natural Language Processing (NLP)

### 🔹 Datasets

* IAM Handwriting Dataset
* Twitter Sentiment Dataset
* Kaggle Emotion Datasets

---

## 🏗️ System Architecture

```
Input (Image / Text)
        ↓
Image Preprocessing (Noise Removal, Resizing)
        ↓
OCR (CNN–BiLSTM + Tesseract)
        ↓
Text Cleaning & Tokenization
        ↓
Sentiment Classification
        ↓
Emotion Detection
        ↓
Results Display (Web UI)
```



## 📊 Model Performance

* OCR Accuracy: **High accuracy on IAM dataset**
* Sentiment Classification Accuracy: **90%+**
* Emotion Classification Accuracy: **90%+**
