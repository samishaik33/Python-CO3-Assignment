readings = [
    0, 2, 5, 0, 8, 12, 3,
    4, 0, 6, 9, 1, 0, 7,
    10, 2, 0, 5, 3, 8, 0
]

# Calculate weekly totals
weekly_totals = []
for i in range(0, len(readings), 7):
    week = readings[i:i+7]
    weekly_totals.append(sum(week))

print("Weekly Totals:", weekly_totals)

# Find maximum and minimum
maximum = max(readings)
minimum = min(readings)

print("Maximum Rainfall:", maximum)
print("Maximum Day:", readings.index(maximum) + 1)
print("Minimum Rainfall:", minimum)
print("Minimum Day:", readings.index(minimum) + 1)

# Find wettest and driest weeks
wettest = max(weekly_totals)
driest = min(weekly_totals)

print("Wettest Week:", weekly_totals.index(wettest) + 1)
print("Driest Week:", weekly_totals.index(driest) + 1)

# Calculate 7-day moving average
averages = []
for i in range(len(readings) - 6):
    avg = sum(readings[i:i+7]) / 7
    averages.append(round(avg, 2))

print("Moving Averages:", averages)

# Find dry days
dry_days = []
for i in range(len(readings)):
    if readings[i] == 0:
        dry_days.append(i + 1)

print("Dry Days:", dry_days)