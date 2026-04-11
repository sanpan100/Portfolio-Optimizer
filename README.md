# Portfolio Optimization & Automated Equity Research (Python)

This project builds a **quantitative portfolio optimization system** using Python and Modern Portfolio Theory (MPT). It analyzes multiple NSE stocks, simulates thousands of portfolios, and identifies the optimal portfolio based on **risk-return trade-offs**.

The system automatically downloads historical market data, calculates financial metrics, and generates visualizations such as the **efficient frontier, correlation heatmaps, and optimal portfolio allocation**.

An **interactive web dashboard built with Streamlit** allows users to dynamically select stocks, analyze portfolios, and visualize risk-return characteristics.

---

## Live Interactive App

You can explore the project using the live Streamlit application:

**Streamlit App:**
https://sanpan100-portfolio-optimizer.streamlit.app/

The dashboard allows users to:

* Select stocks dynamically
* Run portfolio optimization
* Visualize efficient frontier
* View optimal asset allocation
* Analyze portfolio risk and return

---

## Features

* Automatic download of historical stock data from **Yahoo Finance**
* Portfolio optimization using **Modern Portfolio Theory**
* Monte Carlo simulation of **10,000+ portfolios**
* Identification of:
  * Maximum Sharpe Ratio portfolio
  * Minimum Volatility portfolio
* Efficient Frontier visualization
* Correlation heatmap between assets
* Optimal portfolio allocation visualization
* **Interactive Streamlit dashboard**

---

## Methodology

The project applies quantitative finance techniques including:

* Return calculations
* Annualized returns and volatility
* Covariance and correlation matrices
* Monte Carlo portfolio simulation
* Sharpe ratio optimization

These techniques are commonly used in **asset management, portfolio management, and quantitative finance**.

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* yfinance
* Streamlit

---

## Example Outputs

The project produces several visual and analytical outputs:

* Stock price performance comparison
* Correlation heatmap between assets
* Efficient frontier of simulated portfolios
* Optimal portfolio allocation
* Interactive dashboard visualization

---

## Project Structure

```
portfolio-optimizer
│
├── Data
│   └── tickers.csv
├── Jupiter_Notebook
|   └── main.py
│
├── Python
|   └── main.py
├── requirements.txt
└── README.md

```

---

## Objective

The goal of this project is to demonstrate how **data science and financial modeling can be used to build an automated portfolio optimization framework** similar to those used by investment analysts, portfolio managers, and quantitative researchers.

---

## Future Improvements

* Automated **Equity Research Report generation (PDF)**
* Include **fundamental financial ratios**
* Integrate **NSE official data APIs**
* Add **Value at Risk (VaR) and Expected Shortfall**
* Implement **Black-Litterman portfolio optimization**
* Add **risk parity portfolio construction**
