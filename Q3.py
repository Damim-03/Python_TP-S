# Define knowledge base using tuple of lists
rules = (
    (["fever", "cough"], "flu"),
    (["flu", "body_pain"], "severe_flu"),
    (["sore_throat"], "cold"),
    (["cold", "sneeze"], "allergy")
)

# Define known facts
facts = ["fever", "cough", "body_pain"]

def forward_chaining(rules, facts):
    new_facts = set(facts)  # Use a set for fast lookups
    changed = True  # Track if new facts are inferred

    while changed:
        changed = False
        for conditions, conclusion in rules:
            if all(condition in new_facts for condition in conditions) and conclusion not in new_facts:
                new_facts.add(conclusion)  # Infer new fact
                changed = True
                print(f"Derived new fact: {conclusion}")

    return new_facts

# Apply forward chaining
derived_facts = forward_chaining(rules, facts)
print("\nFinal inferred facts:", derived_facts)
