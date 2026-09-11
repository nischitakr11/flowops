import csv
from statistics import mean
from collections import Counter

with open("data/traffic_data.csv", newline="") as file:
    data = list(csv.DictReader(file))

print("===== FLOWOPS TRAFFIC ANALYSIS =====")

print("\nTraffic Data:")
for row in data:
    print(row)

speeds = [float(row["speed"]) for row in data]
print("\nAverage Vehicle Speed:", round(mean(speeds), 2), "km/h")

vehicle_counts = Counter(row["vehicle_type"] for row in data)

print("\nVehicles by Type:")
for vehicle, count in vehicle_counts.items():
    print(vehicle, ":", count)

density_counts = Counter(row["traffic_density"] for row in data)

print("\nTraffic Density:")
for density, count in density_counts.items():
    print(density, ":", count)

if density_counts.get("High", 0) > density_counts.get("Low", 0):
    print("\nTraffic Condition: HIGH")
else:
    print("\nTraffic Condition: NORMAL")
