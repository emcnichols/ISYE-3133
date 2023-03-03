# Import statements
import pandas as pd
from gurobipy import *

# Open and assign file variable names
demand_data_df = pd.read_csv("demand_data.csv", index_col = 'Month')
cost_data_df = pd.read_csv("cost_data.csv", index_col = 'Month')
product_data_df = pd.read_csv("product_data.csv")
volume_data_df = pd.read_csv("volume_data.csv")


# Retrieve name of the list
months = cost_data_df.index.tolist()
products = cost_data_df.columns.values.tolist()
volumes_per_product = product_data_df["Volume"].tolist()
storage_cost_per_product = product_data_df["Storage cost"].tolist()

# deletes the "Month" column name from the products list
del products[0]

# value of total volume to use in constraints
total_volume = volume_data_df.at[0,"Total volume"]

# Build Model
m = Model()

# Create variables
m.update()

num_months = len(months)
num_products = len(products)

x = m.addVars(num_products, num_months, name="x")
inv = m.addVars(num_products, num_months, name="I")

m.setObjective(quicksum(cost_data_df.iloc[t][i] * x[i, t] for i in range(num_products) for t in range(num_months))
	+ quicksum(storage_cost_per_product[i] * inv[i, t] for i in range(num_products) for t in range(num_months - 1)), GRB.MINIMIZE)

m.addConstrs(inv[i, 0] - x[i, 0] + demand_data_df.iloc[0][i] == 0 for i in range(num_products))

for t in range(1, num_months):
    
    m.addConstrs(((inv[i, t] - inv[i, t - 1] - x[i, t] + demand_data_df.iloc[t][i] == 0) for i in range(num_products)))
    m.update()
    
