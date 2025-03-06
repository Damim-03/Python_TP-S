# Define rules: If all conditions are met, then we infer a conclusion
rules = [
    (["fever", "cough"], "flu"),
    (["flu", "body_pain"], "severe_flu"),
    (["sore_throat"], "cold"),
    (["cold", "sneeze"], "allergy")
]

# Define known facts
facts = ["fever", "cough", "body_pain"]

def forward_chaining(rules, facts):
    new_facts = set(facts)  # Start with the given facts
    changed = True  # Flag to track if new facts are inferred

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in new_facts for condition in conditions) and conclusion not in new_facts:
                new_facts.add(conclusion)  # Add inferred fact
                changed = True
                print(f"Derived new fact: {conclusion}")

    return new_facts

# Apply forward chaining
derived_facts = forward_chaining(rules, facts)
print("\nFinal inferred facts:", derived_facts)
