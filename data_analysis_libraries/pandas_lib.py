import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Python Data Analysis Library
# https://pandas.pydata.org/
# https://www.kaggle.com/hershyandrew/amzn-dpz-btc-ntfx-adjusted-may-2013may2019

# load csv to dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/
df = pd.read_csv("Data/portfolio_data.csv")
# df = pd.read_csv("Data/portfolio_data.csv", index_col="AMZN", delimiter=",", skiprows=range(1, 1000))
print(len(df))
print(df.head())

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

# split
# print(df)
# df1 = df[df["BTC"] < 1000]
# df2 = df[df["BTC"] >= 1000]
# df1 = df[:200]
# df2 = df[300:]
# df3 = df[:400]
# print(df1)
# print(df2)

# use lambda functions to filter data
btc_df = df[["BTC"]]
# btc_df = btc_df[lambda x: x["BTC"] > 1000] # df[df["BTC"] > 1000]
btc_df = btc_df[lambda x: x.index > pd.to_datetime("2016-01-01")]
# btc_df = btc_df[lambda x: np.logical_and(x.index > pd.to_datetime("2016-01-01"), x["BTC"] > 0)]

# calculate values with rolling window
btc_df["MA25"] = btc_df.rolling(25).mean()
btc_df["MA100"] = btc_df["BTC"].rolling(100).mean()
# btc_df["MA150"] = btc_df["BTC"].rolling(150).apply(np.mean())

# resample dataframe
# df_mon = df.resample('1M').mean()
# plt.plot(df_mon)
# plt.show()

# visualize data using matplotlib
btc_df.plot()
plt.plot(btc_df)
plt.plot(btc_df[["BTC"]], label="BTC", color="b")
plt.plot(btc_df[["MA25"]], label="MA25", color="r")
plt.plot(btc_df[["MA100"]], label="MA100", color="r")
plt.legend(loc="upper left")
plt.show()

# trendline
y_values = btc_df["BTC"].values
x_values = np.linspace(0, 1, len(y_values))
poly_degree = 3
coeffs = np.polyfit(x_values, y_values, poly_degree)
poly_eqn = np.poly1d(coeffs)
btc_df["Trend"] = poly_eqn(x_values)

plt.plot(btc_df)
plt.show()

# http://queirozf.com/entries/pandas-dataframe-union-and-concat-examples
# concatenate (all/union)
# df4 = pd.concat([df2, df3], ignore_index=False).drop_duplicates()

# # sort
# df4 = df4.sort_index()

# # sort + other manipulations
# df4 = df4.reset_index()
# df4 = df4.drop(['Date', 'AMZN'], axis=1) # deletes
# df4 = df4.sort_values(by="BTC", ascending=False).reset_index()
# print(df4)
# plt.plot(df4["BTC"])
# plt.show()

# save to csv
btc_df.to_csv("BTC_data.csv", sep=";")

# groupby (for df with multiple groups (labels, names, ...))