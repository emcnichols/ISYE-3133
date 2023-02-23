# Import statements
import pandas as pd
from gurobipy import *

# Open and assign file variable names
demand_data_df = pd.read_csv("demand_data.csv")
cost_data_df = pd.read_csv("cost_data.csv")
product_data_df = pd.read_csv("product_data.csv")
volume_data_df = pd.read_csv("volume_data.csv")

# Getting the months
for month in range(len(cost_data_df)):
	print(month)
