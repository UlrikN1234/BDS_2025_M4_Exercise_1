# 🐧 Penguin Prediction Project  

This project predicts the species of a penguin based on its physical characteristics. The model is trained on penguin data and generates daily predictions that are stored in a JSON file. The github page is available at https://ulrikn1234.github.io/BDS_2025_M4_Exercise_1/

## 🚀 Project Overview  

- The project fetches and predicts penguin species daily using a trained Random Forest machine learning model.   
- A **GitHub Actions workflow** automates the process of fetching data, making predictions, and updating the JSON file every day at 7:30 AM.
- The frontend (`index.html`) displays the latest penguin prediction using JavaScript.  

---

## 📂 Project Structure  

```sh
BDS_2025_M4_Exercise_1/
│── .github/workflows/ # GitHub Actions workflows
│ ├── fetch_and_predict.yml # Automates fetching data and making predictions
│
│── data/ # Data storage
│ ├── penguin.db # SQLite database containing penguin data
│ ├── penguin_prediction.json # Daily updated JSON with the latest prediction
│
│── models/ # Saved machine learning models
│ ├── model.pkl # Trained ML model
│ ├── le.pkl # Label encoder
│ ├── scaler.pkl # Scaler for feature normalization
│
│── src/ # Python scripts for data processing and modeling
│ ├── data_to_db.py # Converts raw data into SQLite database
│ ├── train_model.py # Trains the ML model
│ ├── predict_penguin.py # Generates daily predictions
│
│── index.html # Frontend webpage for displaying predictions
│── README.md # Project documentation
│── requirements.txt # Dependencies
```

---

## ⚙️ How It Works  

### 1️⃣ **Data Processing**  
- `data_to_db.py` processes the raw penguin dataset and stores it in `penguin.db`.  

### 2️⃣ **Model Training**  
- `train_model.py` trains a machine learning model to predict penguin species.  
- The trained model is saved in `models/model.pkl`.  

### 3️⃣ **Daily Prediction (Automated via GitHub Actions)**  
- `fetch_and_predict.yml` runs daily to:  
  - Fetch new penguin data.  
  - Use `predict_penguin.py` to predict the species.  
  - Save the prediction to `data/penguin_prediction.json`.  

### 4️⃣ **Frontend Display**  
- The `index.html` file fetches `penguin_prediction.json` and displays the latest prediction on a webpage.  

---

## 📦 Installation & Setup  

1. **Clone the repository**  
   ```sh
   git clone https://github.com/your-username/BDS_2025_M4_Exercise_1.git
   cd BDS_2025_M4_Exercise_1

2. **Install dependencies**  
   ```sh
   pip install -r requirements.txt

3. **Prepare the database**  
   ```sh
   python src/data_to_db.py

4. **Train the model (Optional, only needed if retraining)**  
   ```sh
   python src/train_model.py

4. **Generate a prediction**  
   ```sh
   python src/predict_penguin.py

---

## 📌 Notes 

- The 'penguin_prediction.json' file is updated daily via GitHub Actions and should not be manually modified.
- The frontend fetches the JSON file from '/data/penguin_prediction.json', so it must be correctly updated.

---

## 🛠 Future Improvements
- Improve model accuracy with additional data.
- Add a backend API to dynamically serve predictions.
- Enhance the UI for a better user experience.
