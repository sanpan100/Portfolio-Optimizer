import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd

# Normaalization chart function
def normalization_chart(nse_data):
    normalized_data = (nse_data/nse_data.iloc[0]) * 100
    normalized_data = normalized_data.reset_index()
    normalized_data = normalized_data.melt(
        id_vars = "Date",
        var_name = "Stocks",
        value_name = "Performance"
    )

    fig = px.line(
        normalized_data,
        x = "Date",
        y = "Performance",
        color= "Stocks",
        title= "Stock Price Performance"
    )

    st.plotly_chart(fig)

# Correlation Heatmap Function
def correlation_heatmap(corr_matrix):
    fig = px.imshow(
        corr_matrix,
        text_auto=True,
        color_continuous_scale="RdBu_r",
        title="Stock Correlation Heatmap"
    )
    st.plotly_chart(fig, use_container_width=True)

# Portfolio Allocation Chart
def portfolio_allocation(allocation):
    fig = px.pie(
        allocation,
        values="Weights",
        names="Stock",
        title="Optimal Portfolio Allocation"
    )
    st.plotly_chart(fig)


# Efficient Frontier Function
def efficient_frontier(portfolio, max_sharpe_portfolio,  min_volatility_portfolio):
    fig = px.scatter(
        portfolio,
        x = "Volatility",
        y = "Returns",
        title="Efficient Frontier"
    )
    fig.add_scatter(
        x = [min_volatility_portfolio["Volatility"]],
        y = [min_volatility_portfolio["Returns"]],
        mode="markers",
        marker = dict(color="blue", size=12),
        name = "Min Volatility"
    )
    fig.add_scatter(
        x = [max_sharpe_portfolio["Volatility"]],
        y = [max_sharpe_portfolio["Returns"]],
        mode="markers",
        marker = dict(color="Red", size=12),
        name = "Max Sharpe"
    )
    fig.update_layout(
        xaxis_title="Expected Volatility",
        yaxis_title="Expected Returns"
    )

    st.plotly_chart(fig)