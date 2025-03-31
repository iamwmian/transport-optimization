# Import Library
import pulp

# Define the sets
manufacturers = ["Ferrari", "Mercedes", "Renault"]
countries = ["USA", "Italy", "Germany", "France", "Japan"]

# Define parameters
# Manufacturing capacities (units)
capacity = {
    "Ferrari": 5000,
    "Mercedes": 8000,
    "Renault": 4500
}

# Demand (and minimum storage requirement) for each country (units)
demand = {
    "USA": 2500,
    "Italy": 4000,
    "Germany": 2500,
    "France": 6500,
    "Japan": 1000
}

# Storage capacities for shipping containers (units)
storage = {
    "USA": 4000,
    "Italy": 4000,
    "Germany": 7500,
    "France": 7500,
    "Japan": 1500
}

# Transportation cost per engine (in dollars)
cost = {
    ("Ferrari", "USA"): 7,
    ("Ferrari", "Italy"): 2,
    ("Ferrari", "Germany"): 4,
    ("Ferrari", "France"): 3,
    ("Ferrari", "Japan"): 1,
    ("Mercedes", "USA"): 3,
    ("Mercedes", "Italy"): 6,
    ("Mercedes", "Germany"): 5,
    ("Mercedes", "France"): 4,
    ("Mercedes", "Japan"): 2,
    ("Renault", "USA"): 2,
    ("Renault", "Italy"): 3,
    ("Renault", "Germany"): 1,
    ("Renault", "France"): 4,
    ("Renault", "Japan"): 5
}

# Create the LP problem: minimize the total transportation cost
prob = pulp.LpProblem("Transport_Optimization", pulp.LpMinimize)

# Decision variables: x[i][j] is the number of engines shipped from manufacturer i to country j
x = pulp.LpVariable.dicts("shipment", (manufacturers, countries), lowBound=0, cat='Integer')

# Objective: minimize total transportation cost
prob += pulp.lpSum(cost[(i, j)] * x[i][j] for i in manufacturers for j in countries), "Total_Transportation_Cost"

# Manufacturing Capacity Constraints for each manufacturer
for i in manufacturers:
    prob += pulp.lpSum(x[i][j] for j in countries) <= capacity[i], f"Capacity_{i}"

# Demand Constraints for each country
for j in countries:
    prob += pulp.lpSum(x[i][j] for i in manufacturers) >= demand[j], f"Demand_{j}"

# Storage Capacity Constraints for each country
for j in countries:
    prob += pulp.lpSum(x[i][j] for i in manufacturers) <= storage[j], f"Storage_{j}"

# Solve the LP
result = prob.solve()

# Output the solution status
print("Status:", pulp.LpStatus[prob.status])

# Output the total transportation cost
print("Total Transportation Cost = $", pulp.value(prob.objective))

# Output the shipment plan
print("\nOptimal Shipment Plan:")
for i in manufacturers:
    for j in countries:
        print(f"  {i} to {j}: {x[i][j].varValue} units")
