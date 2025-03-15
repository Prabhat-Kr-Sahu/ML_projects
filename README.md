# SCORE PREDICTION

**Prediction of Math Score** - This project predicts students' math scores based on various features such as gender, race/ethnicity, parental level of education, lunch type, test preparation course, and reading & writing scores.

## 📌 Repository Overview
This repository includes:
- **Data Processing Pipelines**: Scripts for cleaning and preprocessing datasets.
- **Model Training**: Implementation of various machine learning models.
- **Deployment**: Flask/Django-based web applications for model inference.
- **Evaluation Metrics**: Performance analysis and comparison of models.
- **Dockerization**: Prebuilt Docker image for easy deployment.

## 📚 Project Structure
```
score_prediction/
│── data/               # Raw and processed datasets
│── notebooks/          # Jupyter Notebooks for experiments and analysis
│── src/
│   ├── pipeline/       # Data processing and model prediction pipeline
│   ├── models/         # Trained models and model training scripts
│   ├── app.py         # Flask-based web application
│── docker/            # Docker-related files
│   ├── Dockerfile      # Docker image configuration
│── README.md           # Project documentation
│── requirements.txt    # Dependencies
│── .dockerignore       # Files to ignore in Docker builds
│── .gitignore          # Files to ignore in Git
```

## 🚀 Getting Started
### **1. Clone the Repository**
```bash
git clone git@github.com:Prabhat-Kr-Sahu/score_prediction.git
cd score_prediction
```

### **2. Set Up a Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **4. Run the Application**
If this project includes a Flask app, run:
```bash
python app.py
```
Then, visit `http://127.0.0.1:5000` in your browser.

### **5. Run Using Docker**
To pull and run the prebuilt Docker image, use:
```bash
docker pull raegar069/score-app
docker run -p 5000:5000 raegar069/score-app
```
Then, access the application at `http://127.0.0.1:5000`.

## 🤝 Contribution Guidelines
Feel free to contribute to this repository!
1. Fork the repository.
2. Create a new branch.
3. Commit your changes.
4. Push and create a pull request.

## 📝 License
This repository is open-source and available under the **MIT License**.

## 🔗 Connect with Me
- **GitHub**: [Prabhat-Kr-Sahu](https://github.com/Prabhat-Kr-Sahu)
- **LinkedIn**: [Your LinkedIn Profile](#)

---
_⭐ If you find this repository useful, don't forget to star it!_

