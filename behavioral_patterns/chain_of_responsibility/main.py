from chain_of_responsibility import Tier1Support, Tier2Support, Tier3Support

# Set up the chain: Tier 1 → Tier 2 → Tier 3
tier1 = Tier1Support()
tier2 = Tier2Support()
tier3 = Tier3Support()

tier1.set_next(tier2)
tier2.set_next(tier3)

# Create a few tickets with different severities
tickets = [
    (2, "User cannot find the login button"),
    (4, "User facing occasional timeouts"),
    (7, "Database performance issues"),
    (11, "Security breach - data center meltdown"),
]

# Process each ticket starting with Tier 1
for severity, message in tickets:
    print(f"\nIncoming Ticket: Severity {severity} - {message}")
    tier1.handle_ticket(severity, message)
