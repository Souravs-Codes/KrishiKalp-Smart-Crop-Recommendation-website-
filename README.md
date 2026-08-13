# 🌱 Krishikalp - AI-Based Crop Recommendation System

Krishikalp is a Machine Learning-powered agricultural recommendation system designed to help farmers make data-driven decisions by suggesting suitable crops based on soil and environmental conditions. The system analyzes agricultural parameters and provides crop recommendations to support precision farming and improve productivity.

---

## 🚀 Features

- 🌾 **Crop Recommendation**
  - Predicts suitable crops based on input agricultural parameters.

- 🧠 **Machine Learning Model**
  - Uses trained ML algorithms to analyze patterns between soil conditions, environmental factors, and crop suitability.

- 📊 **Data-Driven Agriculture**
  - Helps in making informed crop selection decisions.

- 🖥️ **User-Friendly Interface**
  - Simple web interface for entering parameters and viewing recommendations.

- 📚 **Crop Information System**
  - Provides additional information about recommended crops.

---

## 🛠️ Tech Stack

### Programming Language
- Python

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### Backend
- Flask

### Frontend
- HTML
- CSS

### Development Tools
- Jupyter Notebook
- VS Code

---

## 📂 Project Structure

```
Krishikalp/
│
├── app.py                  # Flask application
│
├── data/
│   └── processed/
│       └── master_dataset.csv
│
├── models/
│   └── trained_model.pkl   # Trained ML model
│
├── utils/
│   ├── predict.py          # Prediction pipeline
│   └── crop_info.py        # Crop details module
│
├── templates/
│   ├── index.html
│   └── home.html
│
├── requirements.txt
│
└── README.md
```

---

## ⚙️ How It Works

1. User provides agricultural parameters such as soil and environmental conditions.
2. Input data is preprocessed and passed to the trained machine learning model.
3. The model analyzes learned patterns from historical agricultural data.
4. The system predicts the most suitable crop.
5. Additional crop details are displayed to the user.

---

## 🧠 Machine Learning Workflow

```
Data Collection
       ↓
Data Preprocessing
       ↓
Feature Engineering
       ↓
Model Training
       ↓
Model Evaluation
       ↓
Model Deployment
       ↓
Crop Recommendation
```

---

## 📊 Model Pipeline

- Data Cleaning
- Feature Encoding
- Feature Scaling
- Model Training
- Performance Evaluation
- Prediction Pipeline Integration

---

## 🔮 Future Improvements

- 🌦️ Integrate real-time weather APIs
- 🗺️ Add location-based crop recommendations
- 💧 Include irrigation and fertilizer recommendations
- 🦠 Add plant disease detection using Deep Learning
- 🤖 Develop an AI farming assistant using LLM/RAG technology
- 📱 Create a mobile application

---

## 💻 Installation & Setup

### Clone the repository

```bash
git clone https://github.com/yourusername/Krishikalp.git
```

### Navigate to project directory

```bash
cd Krishikalp
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000/
```

---

## 📌 Applications

- Precision farming support
- Smart agriculture systems
- Crop planning assistance
- Agricultural decision support systems

---

## 👨‍💻 Author

**Sourav Mukherjee**

B.Tech Computer Science Engineering (AI & ML)

---

## ⭐ Acknowledgement

This project demonstrates the application of Machine Learning in agriculture by combining data science techniques with real-world farming challenges.
