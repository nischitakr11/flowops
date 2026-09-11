import csv
from statistics import mean
from collections import Counter

# Load traffic data
with open("data/traffic_data.csv", newline="") as file:
    data = list(csv.DictReader(file))

print("===== FLOWOPS TRAFFIC ANALYSIS =====")

print("\nTraffic Data:")
for row in data:
    print(row)

# Calculate average speed
speeds = [float(row["speed"]) for row in data]
average_speed = mean(speeds)

print("\nAverage Vehicle Speed:", round(average_speed, 2), "km/h")

# Count vehicles by type
vehicle_counts = Counter(row["vehicle_type"] for row in data)

print("\nVehicles by Type:")
for vehicle, count in vehicle_counts.items():
    print(vehicle, ":", count)

# Count traffic density
density_counts = Counter(row["traffic_density"] for row in data)

print("\nTraffic Density:")
for density, count in density_counts.items():
    print(density, ":", count)

# Determine basic traffic condition
if density_counts.get("High", 0) > density_counts.get("Low", 0):
    print("\nTraffic Condition: HIGH")
else:
    print("\nTraffic Condition: NORMAL")
