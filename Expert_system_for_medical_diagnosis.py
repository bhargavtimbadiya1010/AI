
# Expert System for Medical Diagnosis

# Knowledge Base: Store diseases and their typical symptoms
# Each disease is associated with a set of symptoms.

knowledge_base = {
    "Flu": {
        "fever", "cough", "body_ache", "fatigue", "chills"
    },

    "Common Cold": {
        "cough", "sneezing", "sore_throat", "runny_nose"
    },

    "COVID-19": {
        "fever", "cough", "fatigue",
        "loss_of_taste", "shortness_of_breath"
    },

    "Malaria": {
        "fever", "chills", "sweating", "headache", "body_ache"
    },

    "Migraine": {
        "headache", "nausea",
        "sensitivity_to_light", "fatigue"
    }
}


# Function to identify possible diseases based on patient symptoms
def diagnose(patient_symptoms):

    # Convert the patient's symptoms into a set
    patient_symptoms = set(patient_symptoms)

    # Dictionary to store disease names, confidence scores and matched symptoms
    scores = {}

    # Check each disease in the knowledge base
    for disease, symptoms in knowledge_base.items():

        # Find common symptoms between patient and disease
        matched = patient_symptoms & symptoms

        # Calculate confidence if at least one symptom matches
        if matched:

            # Calculate the symptom matching percentage
            confidence = len(matched) / len(symptoms)

            # Store confidence score and matched symptoms
            scores[disease] = (confidence, matched)

    # Sort diseases from highest confidence to lowest
    ranked = sorted(
        scores.items(),
        key=lambda x: x[1][0],
        reverse=True
    )

    # Return the ranked list of possible diseases
    return ranked


# Patient's reported symptoms
patient_symptoms = [
    "fever", "cough", "fatigue", "chills"
]

# Call the diagnosis function
results = diagnose(patient_symptoms)

# Display patient symptoms
print("Patient symptoms:", patient_symptoms)
print()

# Display ranked diseases and their matching details
for disease, (confidence, matched) in results:

    print(
        f"{disease}: {confidence * 100:.0f}% match "
        f"(matched symptoms: {matched})"
    )

# Display medical disclaimer
print("\nNote: Educational demonstration only.")
print("Consult a qualified healthcare professional for diagnosis.")
