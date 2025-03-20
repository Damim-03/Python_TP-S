# Define knowledge base using dictionary representation
rules = [
    {"if": ["fever", "cough"], "then": "flu"},
    {"if": ["flu", "body_pain"], "then": "severe_flu"},
    {"if": ["sore_throat"], "then": "cold"},
    {"if": ["cold", "sneeze"], "then": "allergy"}
]

# Define known facts
facts = ["fever", "cough", "body_pain"]


def forward_chaining(rules, facts):
    new_facts = set(facts)  # Convert facts to a set for easy lookup
    changed = True  # Track if new facts are inferred

    while changed:
        changed = False
        for rule in rules:
            conditions = rule["if"]
            conclusion = rule["then"]

            # Check if all conditions are met
            if all(condition in new_facts for condition in conditions) and conclusion not in new_facts:
                new_facts.add(conclusion)  # Add inferred fact
                changed = True
                print(f"Derived new fact: {conclusion}")

    return new_facts


# Apply forward chaining
derived_facts = forward_chaining(rules, facts)
print("\nFinal inferred facts:", derived_facts)
