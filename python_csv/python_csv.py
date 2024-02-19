import pandas as pd
import numpy as np

url = "https://en.wikipedia.org/wiki/Comma-separated_values"

df = pd.read_html(url)
wikitable = df[1]

wikitable.to_csv("python_csv.csv")