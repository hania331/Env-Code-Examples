## average calculator
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

data = [72, 55, 101, 90]
average = calculate_average(data)
print("Average:", average)

##2D list
stations = [
    ["A1", 62],
    ["B2", 75],
    ["C3", 95],
    ["D4", 110]
]
for station in stations:
    print(f"{station[0]} → {station[1]}")

## report status
def report_status(stations, threshold):
    for station in stations:
        id, pm25 = station
        if pm25 < threshold:
            print(f"{id} {pm25} µg/m³ (safe)")
        else:
            print(f"{id} {pm25} µg/m³ (danger!)")

report_status(stations, 100)
