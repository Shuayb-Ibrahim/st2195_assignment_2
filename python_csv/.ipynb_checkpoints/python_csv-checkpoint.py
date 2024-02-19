{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "caabc634",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "8d933df3",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = \"https://en.wikipedia.org/wiki/Comma-separated_values\""
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "091b5679",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html(url)\n",
    "wikitable = df[1] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "53e32344",
   "metadata": {},
   "outputs": [],
   "source": [
    "wikitable.to_csv(\"python_csv.csv\")"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
