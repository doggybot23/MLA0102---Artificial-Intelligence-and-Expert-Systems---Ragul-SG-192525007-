# Facts
facts = {
    "fever",
    "cough",
    "body_pain"
}

# Rules: conditions -> conclusion
rules = [
    (["fever", "cough", "body_pain"], "flu"),
    (["fever", "cough"], "infection"),
    (["cough"], "cold")
]

def backward_chaining(goal):
    # Goal is already a known fact
    if goal in facts:
        return True

    # Find a rule that can prove the goal
    for conditions, conclusion in rules:
        if conclusion == goal:
            # Check all conditions recursively
            if all(backward_chaining(condition) for condition in conditions):
                return True

    return False


# Goal
goal = "flu"

if backward_chaining(goal):
    print("Conclusion:", goal)
else:
    print("Conclusion cannot be proved.")
