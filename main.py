import datetime as dt
import pandas as pd
import yfinance as yf
from arch import arch_model
import matplotlib.pyplot as plt
import seaborn as sns

start = dt.datetime(2000, 1, 2)
end = dt.datetime(2025, 4, 6)

sp500 = yf.download('^GSPC', start=start, end=end, progress=True)

print("Available columns:", sp500.columns)

returns = 100 * sp500['Close'].pct_change().dropna()

plt.figure(figsize=(14, 8))
plt.plot(returns, color='gold')
plt.title('S&P 500 Daily Returns (%)')
plt.grid(True)
plt.show()

models = {
    "GARCH(1,1)": {'vol': 'Garch', 'p': 1, 'o': 0, 'q': 1, 'dist': 'Normal'},
    "GJR-GARCH": {'vol': 'Garch', 'p': 1, 'o': 1, 'q': 1, 'dist': 'Normal'},
}

for name, params in models.items():
    print(f"\n{name} Model")
    res = arch_model(returns, **params).fit(disp='off')
    print(res.summary())