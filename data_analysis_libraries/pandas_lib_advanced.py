import pandas as pd
from pandas.api.types import CategoricalDtype
import numpy as np


def df_categorical():
    # https://pandas.pydata.org/docs/user_guide/categorical.html
    # useful in the following cases:
    # - few different values -> saves some memory
    # - lexical ≠ logical order (one, two, three)
    # - hint for other libraries (matplotlib, scikit)
    print("Categorical:")
    df = pd.DataFrame({"A": ["aaa", "bbb", "ccc", "aaa"]})
    df["B"] = df["A"].astype("category")
    print(df)

    print()
    print(df.dtypes)
    print()

    df = pd.DataFrame({"numbers": ["two", "one", "three", "one"]}).astype(
        CategoricalDtype(categories=["one", "two", "three"], ordered=True)
    )
    print(df.sort_values("numbers"))
    print()


def df_pivot():
    # https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.pivot.html
    print("Pivot:")
    df = pd.DataFrame({"spam": ["a", "a", "a", "b", "b", "b"],
                       "ham": ["A", "B", "C", "A", "B", "C"],
                       "egg": [1, 2, 3, 4, 5, 6],
                       "foo": ["xx", "yy", "zz", "uu", "vv", "ww"]})
    print(df)
    print()
    print(df.pivot(index=["spam", "ham"], columns=["egg"]))
    print()
    print(df.pivot(index=["spam"], columns=["ham"], values=["egg"]))
    print()


def _calculate_ewm_manually(arr, alpha):
    beta = 1 - alpha
    v = arr[0]
    ewm = [v]
    for i in range(1, len(arr)):
        v = beta * v + (1 - beta) * arr[i]
        ewm.append(v)
    return ewm


def df_window():
    # https://pandas.pydata.org/docs/user_guide/window.html
    print("Window:")
    df = pd.DataFrame([[1, 1, 0.6], [1, 2, 0.4], [1, 3, 0.2], [2, 4, 0.7]])
    print("original dataframe")
    print(df)
    print("rolling mean")
    print(df.rolling(window=2).mean())

    print()
    print("Exponentially weighted average")
    alpha = 2/3
    print(f"Approximately averaged over the past {1 / (1 - alpha):.3f} values")
    print(df.ewm(alpha=alpha, adjust=False).mean())
    print(_calculate_ewm_manually(df[1], alpha))
    print()


def df_style():
    # https://pandas.pydata.org/docs/user_guide/style.html
    print("Style:")
    df = pd.DataFrame(np.random.randn(6, 3), columns=["A", "B", "C"])
    df["B"][2] = np.nan
    print(df)

    style = df.style.highlight_null(null_color="grey")
    style = df.style.format("{:.1%}")

    def style_values(value):
        return "color:red;" if value < 0 else "color:blue;"

    style = df.style.applymap(style_values)
    style = df.style.applymap(lambda v: f"opacity: {int(abs(v * 100))}%;" if not np.isnan(v) else "background-color:red;")
    print(style.render())   # can be rendered only in Jupyter, here show html only


df_categorical()
df_pivot()
df_window()
df_style()
