import numpy as np
import pandas as pd

data = pd.read_csv("sample1.csv")

std = data.std(axis = 1)
print(std)
