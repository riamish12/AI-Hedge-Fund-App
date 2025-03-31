# 🚀 AI Hedge Fund – Multi-Mode Pro Enhanced

Your personal **AI-powered Hedge Fund Analyst** — now fully enhanced with multi-mode investment personalities, real-time portfolio analysis, signal scoring, backtest visualization & invite-only access.

---

## 🎯 Features
✅ Portfolio Mode – Track multiple stock tickers  
✅ Signal Scoring Engine – Real-time signal strength evaluation  
✅ Backtest Visualization – Chart historical price + signal performance  
✅ Future Price Prediction – AI-generated directional forecast  
✅ Risk Category & Conviction Score Tagging  
✅ Invite-Only Access (with secure invite code)  
✅ Clean & Fast Streamlit UI

---

## 🌐 Live App
👉 [Launch AI Hedge Fund App](https://ai-hedge-fund-app-7vscq2s6oagywb38umaqcf.streamlit.app/)  
*(Invite Code required to access)*

---

## 📂 Project Structure
```
.
├── app.py                     → Main Streamlit App
├── invite_code.txt            → Invite code for private access
├── pro_features.txt           → Feature list
├── README.md                  → This file
├── requirements.txt           → Dependencies
└── .streamlit/
    └── config.toml            → Streamlit server config
```

---

## 🚀 Deployment Guide

### 1. Streamlit Cloud Setup
- Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
- Create a **New App**
- Connect your GitHub repository
- Choose `app.py` as main file
- Click **Deploy**

### 2. Add TogetherAI API Key
In Streamlit Cloud:
- Go to **Manage App → Settings → Secrets**
- Add:
```
[together]
api_key = "YOUR_ACTUAL_TOGETHER_API_KEY"
```
- Save & Reload app

### 3. Invite-Only Access
The app will prompt for an **Invite Code**  
The code is stored in:
```
invite_code.txt
```
**Default Invite Code:**  
`INVITE-CODE-2025`

You can update the invite code anytime by editing this file.

---

## 📊 How to Use
1. Choose your **Investment Mode**  
2. Enter stock tickers (comma-separated)  
3. The app will:
   - Analyze Portfolio
   - Show Signal Scores
   - Tag Risk Category
   - Display Backtest Chart
   - Predict Future Price Trend
4. Displays final AI-based Buy/Hold/Sell recommendation

---

## 📝 License & Disclaimer
This app is for **educational and personal research purposes only.**  
It is **not financial advice.**  
Always do your own research before making investment decisions.
