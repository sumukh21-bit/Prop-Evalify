import pandas as pd
import numpy as np


data = pd.read_csv("Housing.csv")
data.dropna()

df = pd.DataFrame(data)

df["mainroad"]= df["mainroad"].map({
    "yes":1,
    "no":0
})

df["guestroom"]= df["guestroom"].map({
    "yes":1,
    "no":0
})

df["basement"]= df["basement"].map({
    "yes":1,
    "no":0
})

