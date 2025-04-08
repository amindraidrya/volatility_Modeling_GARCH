# Volatility Modeling with GARCH :
This project analyzes **S&P 500 volatility** using GARCH-family models to forecast financial risk. Implemented in Python with `yfinance` and `arch` libraries.

# Features
- Fetches S&P 500 recent historical data (2000-2025) using Yahoo Finance API .
- Computes daily returns and models volatility using:
  - **GARCH(1,1)**
  - **GJR-GARCH** (accounts for leverage effects)
- Visualizes results with Matplotlib/Seaborn
