import pandas as pd

asking_prices=pd.Series([15000,18000,15900,18799,16000])
fair_prices=pd.Series([16000,17500,16890,16789,18950])

good_deals=asking_prices[asking_prices<fair_prices].index.tolist()
print(good_deals)
