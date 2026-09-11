import pandas as pd

# Load traffic data
data = pd.read_csv("data/traffic_data.csv")

print("===== FLOWOPS TRAFFIC ANALYSIS =====")

print("\nTraffic Data:")
print(data)

# Calculate average speed
average_speed = data["speed"].mean()

print("\nAverage Vehicle Speed:", round(average_speed, 2), "km/h")

# Count vehicles by type
vehicle_counts = data["vehicle_type"].value_counts()

print("\nVehicles by Type:")
print(vehicle_counts)

# Count traffic density
density_counts = data["traffic_density"].value_counts()

print("\nTraffic Density:")
print(density_counts)

# Determine basic traffic condition
if density_counts.get("High", 0) > density_counts.get("Low", 0):
    print("\nTraffic Condition: HIGH")
else:
    print("\nTraffic Condition: NORMAL")
