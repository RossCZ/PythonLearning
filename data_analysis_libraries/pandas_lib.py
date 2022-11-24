import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Python Data Analysis Library
# 0) links
# https://pandas.pydata.org/
# https://www.kaggle.com/hershyandrew/amzn-dpz-btc-ntfx-adjusted-may-2013may2019

# 1) load csv to dataframe
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# https://www.geeksforgeeks.org/python-read-csv-using-pandas-read_csv/
df = pd.read_csv("../data/portfolio_data.csv")  # default
# df = pd.read_csv("../data/portfolio_data.csv", index_col="AMZN", delimiter=",", decimal=".", skiprows=range(1, 1000))  # advanced settings

# 2) DataFrame basics
# visualize
# df.plot()
# plt.show()

# print(df)  # show df
# print(len(df))  # length of df
# print(df.head(10))  # show first 10 rows
# print(df.tail())  # show last 5 rows
# print(df.columns)  # show column names
# print(df.index)  # show index data

# 3) DataFrame statistics
# https://chrisalbon.com/python/data_wrangling/pandas_dataframe_descriptive_stats/
# print(df.describe())  # overall
# print(df.corr())  # correlation
# print(df.cov())  # covariance
# print(df.quantile(0.1))  # quantile

# 4) access column
# print(df["BTC"])  # get column by name as series
# print(df[["BTC"]])  # get column by name as dataframe

# 5) missing values
# df = df.dropna()  # clean missing values

# fill missing values (nan)
# df.fillna(0, inplace=True)  # fill constant value
# df.fillna((df.mean()), inplace=True)  # fill column mean (or min, max, ...)
df.interpolate(method="linear", inplace=True)  # interpolate
# df["BTC"] = df.apply(lambda row: 6.0 if np.isnan(row["BTC"]) else row["BTC"], axis=1)  # apply lambda function

# 6) data modification
# convert date to datetime object and set as index for further use
df["Date"] = pd.to_datetime(df["Date"])  # format="%m/%d/%Y"  # https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
df.set_index("Date", inplace=True)

# df.rename({"BTC" : "BTCUSD"}, axis=1, inplace=True)  # rename column
# df -= 10.0  # adjust values in whole data frame
# df = df.reset_index()  # moves index to data column and sets index to integers
# print(df.drop([1, 2, 3], axis=0))  # drop rows by index
# print(df.drop(["Date", "AMZN"], axis=1))  # drop columns by name

# 7) slicing
# https://www.statology.org/pandas-loc-vs-iloc/
# print(df.loc[100:400])  # select rows by position
# print(df.iloc[100:400])  # select rows by indices (with integer index)

# 8) data filtering
# df = df[df["BTC"] < 1000]
# df = df[df["BTC"] >= 1000]  # filter values
# df = df[(df.index > pd.to_datetime("2016-01-01")) & (df.index < pd.to_datetime("2017-12-31"))]  # logical and
# df = df.loc["2016-01-01":"2017-12-31"]  # dates in index

# 9) rolling (moving) window - window overlaps
btc_df = df[["BTC"]].copy()  # copy to prevent warning
btc_df["MA25"] = btc_df.rolling(25).mean()
btc_df["MA100"] = btc_df["BTC"].rolling(100).mean()
# btc_df["MA150"] = btc_df["BTC"].rolling(150).apply(np.mean())  # using apply

# 10) resample - window does not overlap
# df_mon = pd.DataFrame()
# df_mon["mean"] = df.resample("1M").mean()  # requires datetime index, (mean, min, max, ...)

# 11) visualize data using matplotlib
# btc_df.plot()  # directly plot df
# plt.plot(btc_df)  # plot all
plt.plot(btc_df[["BTC"]], label="BTC", color="blue")  # plot single column
plt.plot(btc_df[["MA25"]], label="MA25", color="red")
plt.plot(btc_df[["MA100"]], label="MA100", color="orange")
plt.legend(loc="upper left")
plt.show()

# 12) save to csv
btc_df.to_csv("../data/BTC_data.csv", sep=";", header=True, index=True, decimal=",")

# *** OTHER ***
# 13) trendline
# y_values = btc_df["BTC"].values
# x_values = np.linspace(0, 1, len(y_values))
# poly_degree = 3
# coeffs = np.polyfit(x_values, y_values, poly_degree)
# poly_eqn = np.poly1d(coeffs)
# btc_df["Trend"] = poly_eqn(x_values)

# plt.plot(btc_df)
# plt.show()

# 14) concatenate (all/union)
# http://queirozf.com/entries/pandas-dataframe-union-and-concat-examples
# df4 = pd.concat([df2, df3], ignore_index=False).drop_duplicates()

# 15) sort
# df = df.sort_index()
# dff = df.sort_values(by="BTC", ascending=False).reset_index()

# 17) other topics
# groupby (for df with multiple groups (labels, names, ...))
# multiindex

# note: lambda functions to filter data
# btc_df = btc_df[lambda x: x["BTC"] > 1000]
# btc_df = btc_df[lambda x: x.index > pd.to_datetime("2016-01-01")]
# btc_df = btc_df[lambda x: np.logical_and(x.index > pd.to_datetime("2016-01-01"), x["BTC"] > 0)]
