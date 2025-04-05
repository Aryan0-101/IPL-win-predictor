# 🔥 IPL Win Predictor

This is a dynamic and beautifully styled **Streamlit web app** that predicts the win probability of an IPL team during a live match scenario using a trained machine learning model. It uses match-specific inputs such as target, current score, overs, and wickets to calculate the probability of victory.


## 🎯 Features

- Predict win probability using a pre-trained machine learning model
- Dynamic, team-themed gradient backgrounds (e.g., red-black for RCB, yellow-blue for CSK)
- Real-time input controls for score, overs, and match venue
- Custom animations, Orbitron font, and IPL theme styling
- Responsive and visually engaging layout

## 🧠 ML Model

The model was trained on historical IPL match data and uses features such as:

- Runs left
- Balls left
- Wickets in hand
- Target score
- Run rate (RR) and required run rate (RRR)
- Match location


## 🛠️ Installation

1. Clone the repo

```bash
git clone https://github.com/yourusername/ipl-win-predictor.git
cd IPL-win-predictor
```
2. Install dependencies
```bash
pip install -r requirements.txt
```
3. Run the app
```bash
streamlit run app.py
```

## 📂 File Structure 
```bash 
├── app.py                        # Main Streamlit app
├── requirements.txt              # Python dependencies
├── README.md                     # Project documentation

├── Model/
│   ├── pipe2.pkl                       # Trained model
│   └── IPL_prediction_model.ipynb      # Script to train the model

├── Preprocessing/
│   ├── ipl-prediction-preprocessor.ipynb       # Feature engineering, cleaning, encoding
│   └── ipl_data.csv                            # Processed IPL dataset  
```

## 🧪 Preprocessing
Preprocessing includes:
1. Handling missing values
2. Calculating features like RR, RRR, balls_left, runs_left, etc.
3. Engineering some features. 
4. Handling missing values. 
5. Label encoding of categorical variables (e.g., city)

Located in: preprocessing/preprocess_data.py

## 🧠 Model Training
Model is trained using scikit-learn with logistic regression or other classifiers. 
The model could have been trained using better classifiers to attain more accuracy but inorder to get usable probabilities for the teams Logistic Regression was used. 

## Screenshots
### 1. The Input Controls and Interface 
![image](https://github.com/user-attachments/assets/578353c3-2473-459b-b186-5135a3733d3a)


### 2. The Output Stats and Prediction 
![image](https://github.com/user-attachments/assets/fb7c66ab-7b80-40c9-849a-dda5fa33a6cf)


## 3. Comparison 
  ### Google's Prediction 
![image](https://github.com/user-attachments/assets/31219d28-363f-431a-beae-3acf0fe82e1a)


  ### Our Prediction 
![image](https://github.com/user-attachments/assets/123043f2-407f-493b-bf34-099a49c2411c)


