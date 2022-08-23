import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("portfolio_data.csv")
plt.plot(data["AMZN"])
plt.show()
