# Sentiment Analysis Web Application

## 📌 Introduction

### 🎯 Purpose
This web application enables users to input text-based feedback and receive **real-time sentiment predictions** (Positive, Negative, or Neutral). It is built using a **Neural Network (NN)** model and powered by **Streamlit**, a lightweight Python framework for creating interactive web apps.

### 📦 Scope
The project delivers an end-to-end sentiment analysis solution, including:
- Training and fine-tuning a neural network model
- Integrating it with a Streamlit frontend
- Deploying the application on **AWS** or open-source cloud platforms

**Use Cases:** Customer service, e-commerce reviews, social media monitoring, etc.

### 🧠 Definitions & Abbreviations
- **NN**: Neural Network
- **NLTK**: Natural Language Toolkit, used for text preprocessing
- **VADER**: Lexicon-based sentiment analysis tool optimized for social media
- **Roberta**: Robustly optimized BERT model
- **BERT**: Bidirectional Encoder Representations from Transformers
- **Streamlit**: Python framework for web apps

### 📚 References
- **Amazon Reviews Dataset**

---

## 🌐 System Overview

### 💡 Product Perspective
A standalone web application with a real-time interactive interface to analyze textual data using a pre-trained AI model.

### ⚙️ Product Features
- Accepts and processes text input
- Performs sentiment classification (Positive/Negative/Neutral)
- Displays sentiment predictions in real-time
- Shows model evaluation metrics like accuracy

### 🔗 Assumptions & Dependencies
- Users input meaningful text for analysis
- Model is pre-trained and fine-tuned before deployment
- Streamlit is used as the frontend framework
- Application will be deployed on AWS or an alternative platform

---

## ✅ Functional Requirements

### 1. Neural Network Model Development
- Train on datasets like **IMDb Movie Reviews** or **Sentiment140**
- Use **Roberta** or **BERT** for embeddings
- Fine-tune pre-trained models for sentiment classification
- Evaluate using accuracy, precision, recall, and F1-score

### 2. Streamlit Web Application
- Develop the UI using Streamlit
- Include text input field and "Predict" button
- Display real-time sentiment results

---

## 🚀 System Features

### 🧾 User Input Processing
- Accepts raw text input
- Preprocesses text before model inference

### 🔍 Sentiment Prediction
- Classifies input into Positive, Negative, or Neutral
- Displays output immediately to the user

### 📊 Model Evaluation
- Shows performance metrics (accuracy, precision, recall, F1)
- Supports model retraining

### ☁️ Deployment & Maintenance
- Deploy on **AWS** or alternative cloud services
- Provide updates and improvements regularly
- Implement **logging** and **monitoring** for system health

---

## 🔧 Technologies Used
- Python
- Streamlit
- Transformers (BERT, Roberta)
- NLTK / VADER
- AWS (EC2/S3 or Streamlit Cloud)

---

## 👨‍💻 Author
**Manav Patel**

---

> 💬 *Feel free to clone, contribute, or open issues to improve this project!*
