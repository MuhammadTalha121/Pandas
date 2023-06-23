import pandas as pd
def kil():
    x = pd.DataFrame({
        "tile": [67, 77, 92, 122, 131, 122, 343, None, 132, 432],
        "hike": [121, 144, 153, 131, 534, 533, 124, None, 188, 264]
    })
    b = x["hike"].median()
    x["hike"].fillna(b, inplace=True)
    c = x["tile"].mode()[0]
    x["tile"].fillna(c, inplace=True)
    return x

print(kil())

