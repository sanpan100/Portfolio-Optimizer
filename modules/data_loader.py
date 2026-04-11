import pandas as pd
import numpy as np
import yfinance as yf

# Function Declaration
def historical_data(tickers,start,end):
    nse_data = pd.DataFrame()
    for ticker in tickers:
        nse_data[ticker] = yf.download(
            ticker,
            start=start,
            end=end,
            auto_adjust=False
        )['Adj Close']

# Returning the value
    return nse_data