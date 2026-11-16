
# Rule-Based Loan Eligibility Advisor

# Knowledge Base: Define predefined IF-THEN rules
rules = [

    # Rule 1: Reject applicants with a low credit score
    {
        "name": "R1",
        "condition": lambda f: f["credit_score"] < 500,
        "conclusion": "Loan Rejected: Credit score too low"
    },

    # Rule 2: Reject applicants with insufficient income
    {
        "name": "R2",
        "condition": lambda f: f["income"] < 20000,
        "conclusion": "Loan Rejected: Income below minimum requirement"
    },

    # Rule 3: Reject applicants with too many existing loans
    {
        "name": "R3",
        "condition": lambda f: f["existing_loans"] >= 3,
        "conclusion": "Loan Rejected: Too many existing loans"
    },

    # Rule 4: Approve applicants with excellent credit score and income
    {
        "name": "R4",
        "condition": lambda f: f["credit_score"] >= 750 and f["income"] >= 50000,
        "conclusion": "Loan Approved: Excellent credit and income"
    },

    # Rule 5: Approve applicants meeting standard eligibility requirements
    {
        "name": "R5",
        "condition": lambda f: 500 <= f["credit_score"] < 750
        and f["income"] >= 20000,
        "conclusion": "Loan Approved: Standard eligibility met"
    }
]


# Inference Engine: Check rules one by one
def run_rule_engine(facts):

    # Evaluate each rule in the knowledge base
    for rule in rules:

        # Check whether the rule condition is satisfied
        if rule["condition"](facts):

            # Return the rule name and its conclusion
            return rule["name"], rule["conclusion"]

    # Return default response if no rule matches
    return None, "No matching rule: Manual review required"


# Facts: Store applicant information
applicant = {
    "credit_score": 680,
    "income": 45000,
    "existing_loans": 1
}


# Execute the rule-based system
rule_fired, decision = run_rule_engine(applicant)

# Display the result
print("Rule fired:", rule_fired)
print("Decision:", decision)
