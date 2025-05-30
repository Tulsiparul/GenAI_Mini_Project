import random

INTENTS = [
    "earthquake_safety", "flood_guidance", "relief_camps", "general_emergency"
]

def classify_intent(text):
    # Placeholder classifier – replace with real Vertex AI prediction if needed
    return random.choice(INTENTS)
