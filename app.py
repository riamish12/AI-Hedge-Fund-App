
import streamlit as st
import yfinance as yf
import requests
import json

# Load Together API Key
TOGETHER_API_KEY = st.secrets["together"]["api_key"]

# Mode personalities
MODES = {
    "Titan Mode": {
        "desc": "Discipline and time build empires.",
        "theme": "#0F52BA",
        "tone": "You are a calm, long-term value investor. Analyze patiently."
    },
    "Nova Mode": {
        "desc": "Innovate. Disrupt. Grow fast or fade away.",
        "theme": "#FF6F61",
        "tone": "You are an aggressive tech-focused investor who loves innovation."
    },
    "Atlas Mode": {
        "desc": "Balance is strength. Diversify wisely.",
        "theme": "#228B22",
        "tone": "You are a global, macroeconomic investor seeking balance."
    },
    "Pulse Mode": {
        "desc": "Ride the wave, catch the pulse of the market.",
        "theme": "#DAA520",
        "tone": "You are a fast, market-timing trader. Quick and risky."
    },
    "Quantum Mode": {
        "desc": "Data never lies. Trust the signals.",
        "theme": "#800080",
        "tone": "You are an emotionless, algorithmic quant investor."
    },
    "Chaos Mode": {
        "desc": "Risk it all or lose it all — welcome to the jungle.",
        "theme": "#FF0000",
        "tone": "You are wild, reckless, and love speculative moves."
    }
}

# Streamlit Layout
st.set_page_config(page_title="AI Hedge Fund - Multi-Mode", page_icon="🚀", layout="centered")
st.title("🚀 AI Hedge Fund - Multi-Mode")

# Mode selection
mode = st.selectbox("Choose your Investment Mode:", list(MODES.keys()))
st.markdown(f"**🧬 Mode Personality:** _{MODES[mode]['desc']}_")
st.markdown(f"<style>body{{background-color:{MODES[mode]['theme']};}}</style>", unsafe_allow_html=True)

tickers_input = st.text_input("Enter Stock Tickers (comma-separated):", value="AAPL, TSLA")

if tickers_input:
    tickers = [t.strip().upper() for t in tickers_input.split(",")]
    portfolio_data = []
    total_value = 0

    for ticker in tickers:
        stock = yf.Ticker(ticker)
        hist = stock.history(period="1y")
        info = stock.info
        price = hist['Close'][-1] if not hist.empty else "N/A"
        pe_ratio = info.get('trailingPE', 'N/A')

        portfolio_data.append({
            "Ticker": ticker,
            "Price": round(price, 2) if price != 'N/A' else "N/A",
            "PE Ratio": pe_ratio,
            "Summary": info.get('longBusinessSummary', 'N/A')
        })

        if price != "N/A":
            total_value += price

    st.write(f"**💰 Total Portfolio Value:** ${round(total_value, 2)}")
    st.table(portfolio_data)

    # AI Prompt
    portfolio_summary = "\n".join([f"{p['Ticker']}: Price={p['Price']}, P/E={p['PE Ratio']}" for p in portfolio_data])
    prompt = f"""
{MODES[mode]['tone']}

Here is the portfolio data:
{portfolio_summary}

Give a buy/hold/sell recommendation for the entire portfolio.
"""

    with st.spinner(f"Consulting {mode}..."):
        try:
            headers = {
                "Authorization": f"Bearer {TOGETHER_API_KEY}",
                "Content-Type": "application/json"
            }
            payload = {
                "model": "mistralai/Mistral-7B-Instruct-v0.1",
                "messages": [{"role": "user", "content": prompt}]
            }
            response = requests.post(
                "https://api.together.xyz/v1/chat/completions",
                headers=headers,
                data=json.dumps(payload)
            )
            result = response.json()

            if "choices" in result:
                ai_opinion = result["choices"][0]["message"]["content"]
                st.success(f"💡 {mode} Opinion:")
                st.write(ai_opinion)
            else:
                st.error(f"❗ API Error: {result}")

        except Exception as e:
            st.error(f"❗ Failed to get a response: {str(e)}")
