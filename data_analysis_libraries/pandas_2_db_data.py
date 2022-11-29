import pandas as pd
# pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 320)


# Pandas database operations
# comparison to SQL queries: https://pandas.pydata.org/docs/getting_started/comparison/comparison_with_sql.html
# https://learnsql.com/blog/sql-basics-cheat-sheet/sql-basics-cheat-sheet-a4.pdf
df_o = pd.read_csv("../data/okresy.csv")
df_k = pd.read_csv("../data/kraje.csv")
# print(df_o)
# print(df_k)


# 1) Basic selection
# SELECT * FROM okresy;
# print(df_o)

# SELECT okres, zkratka FROM okresy;
# print(df_o[["Okres", "Zkratka"]])

# SELECT COUNT(*) FROM okresy;
print(f"Celkem okresů: {len(df_o)}")


# 2) Filtering
# SELECT * FROM okresy WHERE pocet_obyvatel > 200000;
# print(df_o[df_o["Pocet obyvatel"] > 200_000])

# SELECT * FROM okresy WHERE pocet_obyvatel BETWEEN 200000 AND 300000;
# print(df_o[(df_o["Pocet obyvatel"] > 200_000) & (df_o["Pocet obyvatel"] < 300_000)])

# SELECT * FROM okresy WHERE okres IN ('Jesenik', 'Sumperk', 'Vsetin', 'Kromeriz');
# print(df_o[df_o["Okres"].isin(["Jesenik", "Sumperk", "Vsetin", "Kromeriz"])])

# SELECT * FROM okresy WHERE okres LIKE 'Brno';
# print(df_o[df_o["Okres"].str.contains("Brno")])


# 3) Grouping: for df with multiple groups/categories (labels, names, ...)
# SELECT Kraj, SUM(rozloha), SUM(pocet_obyvatel), SUM(pocet_obci) FROM okresy GROUP BY kraj;
print(df_o.groupby("Kraj").agg({"Rozloha": "sum", "Pocet obyvatel": "sum", "Pocet obci": "sum"}))

# SELECT Kraj, SUM(rozloha), SUM(pocet_obyvatel), SUM(pocet_obci) FROM okresy GROUP BY kraj HAVING SUM(rozloha) > 7000;
# print(df_o.groupby("Kraj").filter(lambda g: g["Rozloha"].sum() > 7000).groupby("Kraj").agg({"Rozloha": "sum", "Pocet obyvatel": "sum", "Pocet obci": "sum"}))


# 4) Sorting
# SELECT * FROM okresy ORDER BY pocet_obyvatel DESC;
# print(df_o.sort_values("Pocet obyvatel", ascending=False))
# print(df_o.sort_values("Pocet obyvatel", ascending=False).reset_index(drop=True))


# 5) Combining data: https://pandas.pydata.org/docs/user_guide/merging.html
# merge: combine dataframes on values of common columns
# join: combine dataframes on index
# concatenate: append dataframes vertically or horizontally (based on the axis)

# types of join:
# inner (default) = matching rows from both tables
# left = all rows from left and corresponding from right
# right = all rows from right and corresponding from left
# outer (full) = all rows from both tables

# SELECT okresy.*, kraje.kraj, kraje.krajske_mesto FROM okresy LEFT JOIN kraje ON okresy.kraj = kraje.kraj;
# print(df_o.merge(df_k[["Kraj", "Krajske mesto"]], on="Kraj", how="left"))
# print(pd.merge(left=df_o, right=df_k[["Kraj", "Krajske mesto"]], on="Kraj", how="left"))

# inner merge - only Olomoucky kraj
# print(pd.merge(left=df_o, right=df_k[df_k["Kraj"] == "Olomoucky"][["Kraj", "Krajske mesto"]], on="Kraj", how="inner"))

# concatenation: append rows
# print(pd.concat([df_o.loc[:5], df_o.loc[70:]], axis=0))  # axis: 0 = rows, 1 = columns


# 6) Multiindex
# https://pandas.pydata.org/docs/user_guide/advanced.html
# print(df_o.set_index(["Kraj", "Okres"]))
# print(df_o.set_index(["Kraj", "Okres"]).loc["Olomoucky"])
# print(df_o.set_index(["Kraj", "Okres"]).loc["Olomoucky", "Jesenik"])
# print(df_o.set_index(["Kraj", "Okres"]).xs("Jesenik", level=1))
