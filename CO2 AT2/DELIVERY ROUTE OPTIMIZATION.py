routes = {
    "S1": 26,
    "S2": 30,
    "S3": 24,
    "S4": 27,
    "S5": 23,
    "S6": 29
}

current = "S1"

print("Initial Route:", current, routes[current], "km")

while True:

    best = current

    for route in routes:
        if routes[route] < routes[best]:
            best = route

    if best == current:
        break

    current = best
    print("Move to:", current, routes[current], "km")

print("\nOptimal Route:", current)
print("Minimum Distance:", routes[current], "km")
