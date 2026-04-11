import streamlit as st
import pandas as pd

from modules.data_loader import historical_data
from modules.risk_metrics import risk_metrics
from modules.simulation import carlo_simulation
from modules.visualization import *

# Select the available Stocks
available_tickers = pd.read_csv("Data/tickers.csv")["Tickers"]
selected = st.multiselect(
    "Select Stocks",
    available_tickers,
    default=["RELIANCE.NS", "TCS.NS", "INFY.NS"])

# User Input Tickers
custom_input = st.text_input("Or type custom tickers (comma separated)")
custom = []
for t in custom_input.split(','):
    t = t.strip()
    if t:
        custom.append(t)

# Tickers
tickers = list(set(selected + custom))

# User Input others
risk_free_rate = st.number_input("Risk free rate (%)", value=6.5)
start = st.date_input("Start Date")
end = st.date_input("End Date")

if st.button("Run Analyse"):
    nse_data = historical_data(tickers, start, end)
    pf_returns, annual_returns, cov_matrix, corr_matrix = risk_metrics(nse_data)
    portfolio, max_sharpe_portfolio, min_volatility_portfolio, allocation = carlo_simulation(annual_returns, cov_matrix, risk_free_rate, tickers)


    st.subheader("Mean Returns")
    st.write(annual_returns)

    st.subheader("Growth Chart")
    normalization_chart(nse_data)

    st.subheader("Correlation Heatmap")
    correlation_heatmap(corr_matrix)

    st.subheader('Max Sharpe')
    st.write(max_sharpe_portfolio)

    st.subheader('Min Volatility')
    st.write(min_volatility_portfolio)

    st.subheader("Efficient Frontier")
    efficient_frontier(portfolio,max_sharpe_portfolio,min_volatility_portfolio)

    st.subheader("Best Portfolio")
    st.write(allocation)

    st.subheader("Prtfolio Allocation")
    portfolio_allocation(allocation)