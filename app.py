import streamlit as st
import pandas as pd

st.set_page_config(page_title="Options Dashboard", layout="wide")

st.title("Options Trading Dashboard (Sample)")

summary = {
    "Net Liq": "$150,000",
    "YTD P&L": "+$30,000",
    "Win Rate": "72.4%",
    "Max Drawdown": "-8.6%",
    "Sharpe": "1.78"
}
cols = st.columns(len(summary))
for i, (k, v) in enumerate(summary.items()):
    cols[i].metric(k, v)

st.subheader("Equity Curve (Sample)")
equity = pd.DataFrame({
    "date": ["2025-01-02","2025-01-15","2025-02-01","2025-02-15","2025-03-01","2025-03-15","2025-04-01"],
    "equity": [120000,123400,127800,130200,136900,141300,150000]
})
st.line_chart(equity.set_index("date"))

st.subheader("Recent Trades (Sample)")
trades = pd.DataFrame([
    {"date":"2025-04-08","underlying":"AAPL","type":"Put","dte":21,"iv_rank":64,"premium":420,"pnl":310,"return_pct":1.8,"hold_days":4},
    {"date":"2025-04-09","underlying":"NVDA","type":"Call Credit Spread","dte":14,"iv_rank":58,"premium":510,"pnl":-180,"return_pct":-0.9,"hold_days":2},
])
st.dataframe(trades, use_container_width=True)
