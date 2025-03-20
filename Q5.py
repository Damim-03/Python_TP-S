# Define knowledge base using tuple of lists
rules = (
    (["fever", "cough"], "flu"),
    (["flu", "body_pain"], "severe_flu"),
    (["sore_throat"], "cold"),
    (["cold", "sneeze"], "allergy")
)

# Define known facts
facts = ["fever", "cough", "body_pain"]


def backward_chaining(goal, rules, facts, visited=None):
    if visited is None:
        visited = set()

    if goal in facts:  # If goal is a known fact, return True
        return True

    if goal in visited:  # Prevent infinite loops
        return False

    visited.add(goal)

    for conditions, conclusion in rules:
        if conclusion == goal:  # If the goal is inferred by a rule
            if all(backward_chaining(cond, rules, facts, visited) for cond in conditions):
                return True

    return False


# Example Usage
goal = "severe_flu"
goal_reached = backward_chaining(goal, rules, facts)
print(f"\nGoal '{goal}' can be inferred: {goal_reached}")
