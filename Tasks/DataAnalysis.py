import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# https://www.kaggle.com/hershyandrew/amzn-dpz-btc-ntfx-adjusted-may-2013may2019

# load csv to dataframe
df = pd.read_csv("Data/portfolio_data.csv")

# show index data
# print(df.index)

# show first 25 rows
# print(df.head(25))

# show last 5 rows
# print(df.tail())

# show column names
# print(df.columns)

# dataframe statistics
# https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/
# print(df.describe()) # overall
# print(df.corr()) # corelation
# print(df.cov()) # covariance
# print(df.quantile(0.1)) # quantile

# get column by name as series
# print(df["BTC"])

# get column by name as dataframe
# print(df[["BTC"]])

# clean missing values
# df = df.dropna()

# fill missing values
# df.fillna(0, inplace=True)
# df.fillna((df.mean()), inplace=True)
# df.fillna((df.mean()), inplace=True)
# df["BTC"] = df.apply(lambda row: 6.0 if np.isnan(row["BTC"]) else row["BTC"], axis=1)
df.interpolate(method='linear', inplace=True)
# print(df.head(25))

# convert date to date and set as index
df["Date"] = pd.to_datetime(df["Date"])
df.set_index("Date", inplace=True)

# rename column
# df.rename({"BTC" : "BTCUSD"}, axis=1, inplace=True)

# adjust values in whole data frame
# df -= 10.0

# use lambda functions to filter data
btc_df = df[["BTC"]]
# btc_df = btc_df[lambda x: x["BTC"] > 1000]
btc_df = btc_df[lambda x: x.index > pd.to_datetime("2016-01-01")]
# btc_df = btc_df[lambda x: np.logical_and(x.index > pd.to_datetime("2016-01-01"), x["BTC"] > 0)]

# calculate values with rolling window
btc_df["MA25"] = btc_df.rolling(25).mean()
btc_df["MA100"] = btc_df["BTC"].rolling(100).mean()

# resample dataframe
# df_mon = df.resample('1M').mean()
# plt.plot(df_mon)
# plt.show()

# visualize data using matplotlib
# btc_df.plot()
plt.plot(btc_df)
plt.plot(btc_df[["BTC"]], label="BTC", color="b")
plt.plot(btc_df[["MA25"]], label="MA25", color="r")
plt.plot(btc_df[["MA100"]], label="MA100", color="r")
plt.legend(loc="upper left")
plt.show()

# trendline
# y_values = btc_df["BTC"].values
# x_values = np.linspace(0, 1, len(y_values))
# poly_degree = 3
# coeffs = np.polyfit(x_values, y_values, poly_degree)
# poly_eqn = np.poly1d(coeffs)
# btc_df["Trend"] = poly_eqn(x_values)

# plt.plot(btc_df)
# plt.show()