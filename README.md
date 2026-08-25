# 🌱 Krishikalp - AI-Based Crop Recommendation System

Krishikalp is a **Machine Learning-powered agricultural recommendation system** designed to help farmers make data-driven decisions by suggesting suitable crops based on soil and environmental conditions. The system analyzes agricultural parameters and provides crop recommendations to support precision farming and improve productivity.

The application is built with **Flask** and **Dockerized for portable and reproducible deployment**. The Docker image is available on Docker Hub and can be pulled and run without manually configuring the Python environment.

---

## 🚀 Features

* 🌾 **Crop Recommendation**

  * Predicts suitable crops based on agricultural parameters.

* 🧠 **Machine Learning Model**

  * Uses a trained machine learning model to analyze soil and environmental conditions.

* 📊 **Data-Driven Agriculture**

  * Supports informed crop selection using agricultural data.

* 🖥️ **Interactive Web Interface**

  * Provides a simple and user-friendly interface for entering parameters and viewing recommendations.

* 📚 **Crop Information System**

  * Displays additional information about recommended crops, including soil suitability, season, water requirements, and harvesting information.

* 🐳 **Dockerized Deployment**

  * Packaged as a Docker image for consistent and portable deployment across environments.

---

## 🛠️ Tech Stack

### Programming Language

* Python

### Machine Learning

* Scikit-learn
* Pandas
* NumPy
* SciPy
* Joblib

### Backend

* Flask

### Frontend

* HTML
* CSS
* JavaScript

### Deployment

* Docker
* Docker Hub

### Development Tools

* Jupyter Notebook
* VS Code
* Git & GitHub

---

## 📂 Project Structure

```text
Krishikalp/
│
├── app.py
│
├── data/
│   ├── crops.json
│   ├── crop_requirements.json
│   └── processed/
│
├── models/
│   └── trained_model.pkl
│
├── utils/
│   ├── predict.py
│   └── crop_info.py
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── templates/
│   ├── index.html
│   ├── home.html
│   └── result.html
│
├── notebooks/
│   └── Final_Pipeline/
│
├── Dockerfile
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ How It Works

1. The user enters agricultural parameters such as soil and environmental conditions.
2. The input data is processed and passed to the trained machine learning model.
3. The model analyzes the learned patterns from agricultural data.
4. Suitable crops are predicted based on the provided conditions.
5. The application displays the recommended crops along with relevant crop information.

---

## 🧠 Machine Learning Workflow

```text
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

* Data Cleaning
* Data Preprocessing
* Feature Engineering
* Feature Selection
* Model Training
* Model Evaluation
* Model Serialization
* Prediction Pipeline Integration
* Flask Deployment

---

# 🐳 Docker Deployment

Krishikalp has been **containerized using Docker** and the production-ready image has been published to **Docker Hub**.

### Docker Image

```text
sammy2244/krishikalp
```

### Pull the Docker Image

```bash
docker pull sammy2244/krishikalp
```

### Run the Container

```bash
docker run -p 8888:5000 sammy2244/krishikalp
```

The application will be available at:

```text
http://localhost:8888
```

### Docker Architecture

```text
Krishikalp Flask Application
            ↓
       Dockerfile
            ↓
     Docker Image
            ↓
   Docker Hub Repository
            ↓
      Docker Container
            ↓
     Flask Web Application
```

Docker ensures that the application, Python environment, dependencies, and machine learning model can be packaged and executed consistently without requiring users to manually configure the complete development environment.

---

## 💻 Local Installation

### Clone the Repository

```bash
git clone https://github.com/Souravs-Codes/KrishiKalp-Smart-Crop-Recommendation-website-.git
```

### Navigate to the Project

```bash
cd KrishiKalp-Smart-Crop-Recommendation-website-
```

### Create a Virtual Environment

```bash
python -m venv venv
```

### Activate the Environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser:

```text
http://127.0.0.1:5000/
```

---

## 🐳 Why Docker?

Docker was integrated into Krishikalp to:

* Ensure consistent application environments
* Package dependencies with the application
* Simplify deployment
* Avoid environment-specific dependency issues
* Make the application portable across systems
* Provide an easy way to run the application using a single Docker command

---

## 🔮 Future Improvements

* 🌦️ Integrate real-time weather APIs
* 🗺️ Add location-based crop recommendations
* 💧 Include irrigation and fertilizer recommendations
* 🦠 Add plant disease detection using Deep Learning
* 🤖 Develop an AI farming assistant using LLM/RAG technology
* 📱 Create a mobile application
* ☁️ Deploy the Docker container to a cloud platform

---

## 📌 Applications

* Precision farming support
* Smart agriculture systems
* Crop planning assistance
* Agricultural decision support systems

---

## 👨‍💻 Author

**Sourav Mukherjee**

B.Tech Computer Science Engineering (AI & ML)

---

## ⭐ Acknowledgement

Krishikalp demonstrates the practical application of **Machine Learning, Flask, and Docker** to address real-world agricultural challenges and provide data-driven support for smarter crop selection.
