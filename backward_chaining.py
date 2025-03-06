from forward_chaining import rules, facts


def backward_chaining(goal, rules, facts):
    if goal in facts:
        return True  # Goal is already known as a fact

    for conditions, conclusion in rules:
        if conclusion == goal:
            if all(backward_chaining(condition, rules, facts) for condition in conditions):
                return True

    return False

# Define a goal
goal = "severe_flu"

# Apply backward chaining
if backward_chaining(goal, rules, facts):
    print(f"The goal '{goal}' can be inferred from the facts.")
else:
    print(f"The goal '{goal}' cannot be inferred from the facts.")
