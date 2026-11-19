# Temperature readings in Celsius
readings = [4, 9, 55, 60, 2, 7.5, 1, 50, 6]

# Remove invalid readings
valid = [
    x for x in readings
    if -50 <= x <= 50
]

# Convert Celsius to Fahrenheit
fahrenheit = [
    (x * 9 / 5) + 32
    for x in valid
]

# Find alarm temperatures
alarms = [
    (i + 1, temp)
    for i, temp in enumerate(readings)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
]

# Using map and filter
filtered = list(
    filter(lambda x: -50 <= x <= 50, readings)
)

converted = list(
    map(lambda x: (x * 9 / 5) + 32, filtered)
)

# Dictionary comprehension
temp_dict = {
    i + 1: round((temp * 9 / 5) + 32, 2)
    for i, temp in enumerate(readings)
    if -50 <= temp <= 50
}

# Set comprehension
alarm_minutes = {
    i + 1
    for i, temp in enumerate(readings)
    if -50 <= temp <= 50 and not (2 <= temp <= 8)
}

print("Valid Temperatures:", valid)
print("Fahrenheit:", fahrenheit)
print("Map and Filter:", filtered)
print("Converted Values:", converted)
print("Alarm Minutes:", alarms)
print("Temperature Dictionary:", temp_dict)
print("Alarm Minute Set:", sorted(alarm_minutes))