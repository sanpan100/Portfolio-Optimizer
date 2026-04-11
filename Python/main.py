import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import yfinance as yf
import seaborn as sns
import streamlit as st

# Functions
# Historical data Function
def historical_data(tickers,start,end):
    nse_data = pd.DataFrame()
    for ticker in tickers:
        nse_data[ticker] = yf.download(ticker, start=start, end=end, auto_adjust=False)['Adj Close']
    return nse_data

# Risk Metrics Function
def risk_mertrics():
    pf_returns = nse_data.pct_change().dropna()
    annual_returns = pf_returns.mean() * 252
    cov_matrix = pf_returns.cov() *252
    corr_matrix = pf_returns.corr()
    portfolio, portfolio_weights = carlo_simulation(annual_returns,cov_matrix)
    portfolio['Sharpe_Ratio'] = (portfolio['Returns'] - (risk_free_rate/100))/portfolio['Volatility']
    return (pf_returns, annual_returns, cov_matrix, corr_matrix, portfolio, portfolio_weights)

# Normalization Chart Function
def Normalization_chart(nse_data):
    normalized_data = nse_data/nse_data.iloc[0] * 100
    normalized_data = normalized_data.reset_index()
    normalized_data = normalized_data.melt(
        id_vars="Date",
        var_name="Stock",
        value_name="Performance"
    )
    fig = px.line(
        normalized_data,
        x="Date",
        y="Performance",
        color="Stock",
        title="Stock Price Performance"
    )
    st.plotly_chart(fig)

def correlation_heatmap(corr_matrix):
    fig, ax = plt.subplots(figsize=(12,8))
    sns.heatmap(
        corr_matrix,
        annot=False,
        cmap="coolwarm",
        ax=ax
    )
    plt.title("Stock Correlation Heatmap")
    st.pyplot(fig)


# Monte Carlo Simulation
def carlo_simulation(annual_returns, cov_matrix):
    portfolio_returns = []
    portfolio_volatility = []
    portfolio_weights = []

    for i in range(10000):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        portfolio_weights.append(weights)

        returns = np.dot(weights,annual_returns)
        portfolio_returns.append(returns)

        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        portfolio_volatility.append(volatility)

    portfolio_returns = np.array(portfolio_returns)
    portfolio_volatility = np.array(portfolio_volatility)
    portfolio_weights = np.array(portfolio_weights)

    portfolio = pd.DataFrame({
        "Returns" : portfolio_returns,
        "Volatility" : portfolio_volatility
    })
    return (portfolio,portfolio_weights)


# Portfolio Allocation Chart
def portfolio_allocation(allocation):

    fig = px.pie(
        allocation,
        values="Weights",
        names="Stock",
        title="Optimal Portfolio Allocation"
    )

    fig.update_traces(textposition="inside", textinfo="percent+label")
    return fig


# Efficient Frontier Function
def efficient_frontier(portfolio, max_sharpe_portfolio, min_volatility_portfolio):
    fig = px.scatter(
        portfolio,
        x = "Volatility",
        y = "Returns"
    )
    fig.add_scatter(
        x = [max_sharpe_portfolio["Volatility"]],
        y = [max_sharpe_portfolio["Returns"]],
        mode="markers",
        marker=dict(color="red", size=12),
        name="Max Sharpe"
    )
     # Add minimum volatility point
    fig.add_scatter(
        x=[min_volatility_portfolio["Volatility"]],
        y=[min_volatility_portfolio["Returns"]],
        mode="markers",
        marker=dict(color="blue", size=12),
        name="Min Volatility"
    )

    fig.update_layout(
        xaxis_title="Expected Volatility",
        yaxis_title="Expected Returns"
    )
    return fig



# User Input
available_tickers = pd.read_csv("../Data/tickers.csv")["Tickers"]
selected = st.multiselect("select", available_tickers, default=["RELIANCE.NS", "TCS.NS", "INFY.NS"])
custom_input = st.text_input("Or type custom tickers (comma separated)")
custom = []
for t in custom_input.split(','):
    t = t.strip()
    if t:
        custom.append(t)

tickers = list(set(selected + custom))

risk_free_rate = st.number_input("Risk free rate (%)", value=6.5)
start = st.date_input("Start Date")
end = st.date_input("End Date")


# Download historical adjusted close prices for each ticker from Yahoo Finance
if st.button('Run Analyse'):
    nse_data = historical_data(tickers, start, end)
    pf_returns, annual_returns, cov_matrix, corr_matrix, portfolio, portfolio_weights = risk_mertrics()
    
    max_sharpe_portfolio = portfolio.iloc[portfolio['Sharpe_Ratio'].idxmax()] 
    min_volatility_portfolio = portfolio.iloc[portfolio['Volatility'].idxmin()] 
    best_weight = portfolio_weights[portfolio["Sharpe_Ratio"].idxmax()] 

    allocation = pd.DataFrame({
        "Stock" : tickers,
        "Weights" : best_weight
    })

    

    st.write("Mean Returns")
    st.write(annual_returns)

    st.subheader("Growth Chart")
    Normalization_chart(nse_data)

    st.subheader("Correlation Heatmap")
    correlation_heatmap(corr_matrix)

    st.write('Max Sharpe')
    st.write(max_sharpe_portfolio)

    st.write('Min Volatility')
    st.write(min_volatility_portfolio)

    st.subheader("Efficient Frontier")
    fig = efficient_frontier(
        portfolio,
        max_sharpe_portfolio,
        min_volatility_portfolio
    )
    st.plotly_chart(fig)

    st.write("Best Portfolio")
    st.write(allocation)

    st.subheader("Portfolio Allocation")
    fig = portfolio_allocation(allocation)
    st.plotly_chart(fig)