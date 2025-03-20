# Define knowledge base using tuple of lists
rules = (
    (["fever", "cough"], "flu"),
    (["flu", "body_pain"], "severe_flu"),
    (["sore_throat"], "cold"),
    (["cold", "sneeze"], "allergy")
)

# Define known facts
facts = ["fever", "cough", "body_pain"]

def forward_chaining(rules, facts, goal=None):
    new_facts = set(facts)  # Use a set for fast lookup
    changed = True  # Track if new facts are inferred

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in new_facts for condition in conditions) and conclusion not in new_facts:
                new_facts.add(conclusion)  # Infer new fact
                changed = True
                print(f"Derived new fact: {conclusion}")
                if goal and goal == conclusion:
                    return True  # Stop if goal is reached

    if goal:
        return goal in new_facts  # Return if goal was found
    return new_facts

# Example Usage
goal = "severe_flu"
reached_goal = forward_chaining(rules, facts, goal)
print(f"\nGoal '{goal}' reached: {reached_goal}")
