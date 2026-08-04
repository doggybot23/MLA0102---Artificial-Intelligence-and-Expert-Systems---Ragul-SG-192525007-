def monkey_banana():
    monkey = "Door"
    box = "Window"
    banana = "Center"

    print("Initial State:")
    print("Monkey:", monkey)
    print("Box:", box)
    print("Banana:", banana)

    if monkey != box:
        print("\nMonkey moves from", monkey, "to", box)
        monkey = box

    print("Monkey pushes the box to", banana)
    box = banana
    monkey = banana

    print("Monkey climbs onto the box")
    print("Monkey picks the banana")

    print("\nGoal Achieved: Monkey has the banana.")

monkey_banana()
