import pandas as pd

url = "https://en.wikipedia.org/wiki/Comma-separated_values"

df = pd.read_html(url)
wikitable = df[1]

wikitable.to_csv("python_csv.csv")