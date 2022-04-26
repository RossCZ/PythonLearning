import pandas as pd
from sqlalchemy import create_engine

e = create_engine("sqlite:///cv10/databaze.sqlite")
conn = e.connect()

# save data to db only once
# df = pd.read_csv("cv9/portfolio_data.csv")
# df.to_sql(name="portfolio", con=conn)

df = pd.read_sql_table(table_name="portfolio", con=e)
print(df)
