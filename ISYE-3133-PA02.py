# Import statements
import pandas as pd
from gurobipy import *

# Open and assign file variable names
demand_data_df = pd.read_csv("demand_data.csv")
cost_data_df = pd.read_csv("cost_data.csv")
product_data_df = pd.read_csv("product_data.csv")
volume_data_df = pd.read_csv("volume_data.csv")


# Retrieve name of the list
months = cost_data_df["Month"].tolist()
products = cost_data_df.columns.values.tolist()
volumes_per_product = product_data_df["Volume"].tolist()
storage_cost_per_product = product_data_df["Storage cost"].tolist()

# deletes the "Month" column name from the products list
del products[0]

# value of total volume to use in constraints
total_volume = volume_data_df.at[0,"Total volume"]

# CURRENT QUESTION:
# how to get each products value of demand and cost per product per month?

# print(months)
# print(products)
# print(total_volume)
# print(volumes_per_product)
# print(storage_cost_per_product)

# for month in range(len(cost_data_df)):
# 	print(month)
