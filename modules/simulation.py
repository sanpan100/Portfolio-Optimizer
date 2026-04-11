import numpy as np
import pandas as pd

# Function Declaration
def carlo_simulation(annual_returns, cov_matrix, risk_free_rate, tickers):
    portfolio_returns = []
    portfolio_volatility = []
    portfolio_weights = []

# Running Simulation
    for i in range(10000):
        weights = np.random.random(len(tickers))
        weights /= np.sum(weights)
        portfolio_weights.append(weights)

        returns = np.dot(weights, annual_returns)
        portfolio_returns.append(returns)

        volatility = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        portfolio_volatility.append(volatility)

# list to array
    portfolio_returns = np.array(portfolio_returns)
    portfolio_volatility = np.array(portfolio_volatility)
    portfolio_weights = np.array(portfolio_weights)

# Compiling the returns and volitilty into DataFrame
    portfolio = pd.DataFrame({
        'Returns' : portfolio_returns,
        'Volatility' : portfolio_volatility
    })

# Calculation of Sharpe Ratio
    portfolio['Sharpe_Ratio'] = (
        portfolio['Returns'] - (risk_free_rate/100)
        )/portfolio['Volatility']
    
    max_sharpe_portfolio = portfolio.iloc[portfolio['Sharpe_Ratio'].idxmax()] 
    min_volatility_portfolio = portfolio.iloc[portfolio['Volatility'].idxmin()] 
    best_weight = portfolio_weights[portfolio["Sharpe_Ratio"].idxmax()] 

    allocation = pd.DataFrame({
        "Stock" : tickers,
        "Weights" : best_weight
    })

# Returning the value
    return (portfolio, max_sharpe_portfolio, min_volatility_portfolio, allocation)