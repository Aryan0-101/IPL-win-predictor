import streamlit as st
import pickle
import pandas as pd

# IPL TEAM COLORS FOR GRADIENT
team_colors = {
    "Chennai Super Kings": ("#fcd116", "#0000ff"),
    "Mumbai Indians": ("#3377ff", "#ffbf00"),
    "Royal Challengers Bengaluru": ("#da1818", "#000000"),
    "Kolkata Knight Riders": ("#3b215d", "#ffc40c"),
    "Punjab Kings": ("#ff471a", "#000000"),
    "Sunrisers Hyderabad": ("#f26522", "#000000"),
    "Rajasthan Royals": ("#ea1a85", "#002c5f"),
    "Delhi Capitals": ("#6666ff", "#ff1a1a"),
    "Gujarat Titans": ("#003366", "#ffd633"),
    "Lucknow Super Giants": ("#191966", "#ff0000")
}

# IPL THEME & BACKGROUND
st.markdown(
    """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500&display=swap');

        .stApp {
            background: linear-gradient(135deg, #000000, #330033, #003d4d, #800000);
            color: white;
            font-family: 'Orbitron', sans-serif;
        }
        .main-title {
            text-align: center;
            font-size: 80px;
            font-weight: bold;
            margin-bottom: 20px;
            margin-top: 15px;
            color: #fddb3a;
            text-shadow: 2px 2px 10px #000000;
            animation: fadeIn 2s ease-in-out;
        }
        .sub-header {
            text-align: center;
            font-size: 36px !important;
            font-weight: bold;
            color: #ffffff;
        }
        .prediction {
            text-align: center;
            font-size: 26px;
            font-weight: bold;
            color: white;
            padding: 20px;
            border-radius: 15px;
            margin: 30px auto;
            width: 60%;
            box-shadow: 0 8px 20px rgba(0,0,0,0.6);
            animation: popUp 1s ease-out;
        }
        .stat-box {
            background-color: rgba(255, 255, 255, 0.05);
            border: 1px solid #ffffff10;
            border-radius: 12px;
            padding: 15px;
            margin: 20px 0;
            font-size: 18px;
        }
        .stButton button {
            background-color: #e71d36;
            color: white;
            font-weight: bold;
            border-radius: 10px;
            border: none;
            padding: 12px 24px;
            transition: all 0.3s ease;
        }
        .stButton button:hover {
            background-color: #fddb3a;
            color: black;
            transform: scale(1.08);
        }
        .css-1d391kg, .css-1kyxreq, .css-ffhzg2, label {
            color: white !important;
        }
        @keyframes popUp {
            0% { transform: scale(0.8); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        @keyframes fadeIn {
            0% { opacity: 0; }
            100% { opacity: 1; }
        }
        .ipl-logo {
            display: block;
            margin-left: auto;
            margin-right: auto;
            origin: center;
            width: 30%;
            height: auto;
            margin-top: -15px;

            animation: fadeIn 2.5s ease;
        }
        .css-1p05t8e, .css-1d391kg, .stSelectbox label, .stSelectbox div {
            font-size: 17px !important;
        }
        .main-title {
            font-size: 40px !important;
        }
        .stNumberInput label, .stNumberInput div, .stNumberInput input {
            font-size: 17px !important;
        }

    </style>
    """,
    unsafe_allow_html=True,
)

# IPL LOGO
st.markdown('<img class="ipl-logo" src="https://1000logos.net/wp-content/uploads/2022/08/Indian-Premier-League-Logo-500x281.png" alt="IPL Logo">', unsafe_allow_html=True)

# Load the model
pipe = pickle.load(open("E:\\Codes\\Projects\\IPl predictor\\pipe2.pkl", "rb"))

st.markdown('<p class="main-title">🏏🎉 IPL Win Predictor🎉🏏</p>', unsafe_allow_html=True)

# Teams and Cities
teams = list(team_colors.keys())
cities = ['Chennai', 'Chandigarh', 'Kolkata', 'Mumbai', 'Indore',
       'Delhi', 'Hyderabad', 'Pune', 'Ranchi',
       'Ahmedabad', 'Jaipur', 'Bengaluru', 'Visakhapatnam', 
       'Rajkot', 'Dharamsala', 'Mohali', 'Lucknow', 'Cuttack',
       'Guwahati', 'Raipur','Nagpur', 'Kanpur'] 

# Layout for team selection
col1, col2 = st.columns(2)

with col1:
    batting_team = st.selectbox("🏏 Select the Batting Team", sorted(teams))

with col2:
    bowling_team = st.selectbox("🏏 Select the Bowling Team", sorted(teams))

# Match Details
selected_city = st.selectbox("📍 Select Host City", sorted(cities))
target = st.number_input("🎯 Target Score", min_value=1, step=1)

col3, col4, col5 = st.columns(3)

with col3:
    score = st.number_input("🏏 Current Score", min_value=0, step=1)

with col4:
    overs = st.number_input("⏳ Overs Completed", min_value=0.0, step=0.1, max_value=20.0)

with col5:
    wickets = st.number_input("❌ Wickets Lost", min_value=0, step=1, max_value=10)

# Prediction Button
if st.button("🔮 Predict Probability"):
    runs_left = target - score
    balls_left = 120 - (overs * 6)
    wickets_left = 10 - wickets
    crr = round(score / overs, 2) if overs > 0 else 0
    rrr = round((runs_left * 6) / balls_left, 2) if balls_left > 0 else 0

    # Input Summary
    st.markdown("""
        <div class="stat-box">
        <b>Match Situation:</b><br>
        Runs Left: <b>{}</b><br>
        Balls Left: <b>{}</b><br>
        Wickets Left: <b>{}</b><br>
        Current Run Rate: <b>{}</b><br>
        Required Run Rate: <b style="color:{}">{}</b>
        </div>
    """.format(runs_left, balls_left, wickets_left, crr, "#ff4b5c" if (rrr - crr)>= 3 else "#00ffb3", rrr), unsafe_allow_html=True)

    input_df = pd.DataFrame({
        "city": [selected_city],
        "runs_left": [runs_left], "balls_left": [balls_left], "wickets_left": [wickets_left],
        "target_runs": [target], "RR": [crr], "RRR": [rrr]
    })

    result = pipe.predict_proba(input_df)
    win_prob = round(result[0][1] * 100, 2)
    loss_prob = round(result[0][0] * 100, 2)

    grad1, grad2 = team_colors[batting_team]

    st.markdown(f'<p class="sub-header">{batting_team} vs {bowling_team}</p>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="prediction" style="background: linear-gradient(to right, {grad1}, {grad2});">{batting_team} Win Probability: {win_prob}%</div>',
        unsafe_allow_html=True
    )
    st.markdown(
        f'<div class="prediction" style="background: linear-gradient(to right, {team_colors[bowling_team][0]}, {team_colors[bowling_team][1]});">{bowling_team} Win Probability: {loss_prob}%</div>',
        unsafe_allow_html=True
    )
