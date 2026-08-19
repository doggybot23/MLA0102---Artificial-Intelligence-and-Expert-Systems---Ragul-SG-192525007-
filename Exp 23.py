# Initial facts
facts = {"computer_on", "power_light_off"}

# Production rules
rules = [
    ({"computer_on", "power_light_off"}, "power_supply_fault"),
    ({"power_supply_fault"}, "check_power_cable"),
    ({"check_power_cable"}, "cable_may_be_loose")
]

# Forward Chaining
changed = True

while changed:
    changed = False

    for conditions, conclusion in rules:
        if conditions.issubset(facts) and conclusion not in facts:
            facts.add(conclusion)
            print("Derived:", conclusion)
            changed = True

print("\nFinal Facts:")
for fact in facts:
    print(fact)
