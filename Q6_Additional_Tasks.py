trains = {
    "T101": {
        "name": "City Express",
        "days": {"Mon", "Tue", "Wed"},
        "stops": [
            ("Central", "08:00"),
            ("T Nagar", "08:25"),
            ("Airport", "09:00"),
        ],
    },
    "T102": {
        "name": "Coastal Express",
        "days": {"Mon", "Fri"},
        "stops": [
            ("Central", "07:30"),
            ("Airport", "08:40"),
        ],
    },
    "T103": {
        "name": "Hill Passenger",
        "days": {"Tue", "Thu"},
        "stops": [
            ("Market", "06:45"),
            ("Central", "07:20"),
        ],
    },
    "T104": {
        "name": "Night Mail",
        "days": {"Mon", "Tue"},
        "stops": [
            ("Airport", "21:00"),
            ("Central", "22:10"),
        ],
    },
    "T105": {
        "name": "Morning Local",
        "days": {"Mon", "Wed", "Fri"},
        "stops": [
            ("Central", "06:15"),
            ("Market", "06:50"),
        ],
    },
}

station = "Central"
day = "Mon"

# Create station index
station_index = {}
for train_id, info in trains.items():
    for stop, time in info["stops"]:
        station_index.setdefault(stop, []).append(
            (train_id, time, info["name"])
        )

# Find matching trains
matches = []
for train_id, info in trains.items():
    if day in info["days"]:
        for stop, time in info["stops"]:
            if stop == station:
                matches.append(
                    (train_id, time, info["name"])
                )

# Sort by departure time
matches.sort(key=lambda x: x[1])

print("Trains at", station, "on", day)

for train in matches:
    print(train)

print("Station Index:", station_index)

# Access third stop departure time
print("Third Stop Time:", trains["T101"]["stops"][2][1])