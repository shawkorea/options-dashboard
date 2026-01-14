import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Options Dashboard", layout="wide")

st.title("Options Trading Dashboard (Sample)")

# --- Top Metrics (one set only) ---
col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Net Liq", "$150,000")
col2.metric("YTD P&L", "$30,000", delta="+25.0%")          # green delta
col3.metric("Win Rate", "72.4%")
col4.metric("Max Drawdown", "-8.6%", delta="-8.6%")        # red delta
col5.metric("Sharpe", "1.78")

# --- Data ---
equity = pd.DataFrame({
    "date": ["2025-01-02","2025-01-15","2025-02-01","2025-02-15","2025-03-01","2025-03-15","2025-04-01"],
    "equity": [120000,123400,127800,130200,136900,141300,150000]
})

trades = pd.DataFrame([
    {"date":"2025-04-08","underlying":"AAPL","type":"Put","dte":21,"iv_rank":64,"premium":420,"pnl":310,"return_pct":1.8,"hold_days":4},
    {"date":"2025-04-09","underlying":"NVDA","type":"Call Credit Spread","dte":14,"iv_rank":58,"premium":510,"pnl":-180,"return_pct":-0.9,"hold_days":2},
])

# --- Equity Curve (Plotly for color control) ---
st.subheader("Equity Curve (Sample)")

fig = px.line(equity, x="date", y="equity", title=None)
fig.update_traces(line=dict(color="#2ECC71", width=3))
fig.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    paper_bgcolor="rgba(0,0,0,0)",
    yaxis_title="Equity ($)",
    xaxis_title=""
)
st.plotly_chart(fig, use_container_width=True)

# --- Recent Trades (styled table) ---
st.subheader("Recent Trades (Sample)")

def color_pnl(val):
    if val > 0:
        return "color: #2ECC71; font-weight: 700"
    elif val < 0:
        return "color: #FF4B4B; font-weight: 700"
    return ""

styled_trades = trades.style.applymap(color_pnl, subset=["pnl"])
st.dataframe(styled_trades, use_container_width=True)
