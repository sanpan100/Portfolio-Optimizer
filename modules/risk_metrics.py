import pandas as pd
import numpy as np
from modules.simulation import carlo_simulation

# Function Declaration
def risk_metrics(nse_data):
    pf_returns = nse_data.pct_change().dropna()
    annual_returns = pf_returns.mean() * 252
    cov_matrix = pf_returns.cov() * 252
    corr_matrix = pf_returns.corr()

# Returning the value
    return (
        pf_returns,
        annual_returns,
        cov_matrix,
        corr_matrix,
        )
