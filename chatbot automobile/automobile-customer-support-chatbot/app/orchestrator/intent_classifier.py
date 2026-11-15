
from app.llm.model import get_llm


VALID_INTENTS = [
    "greeting",
    "vehicle_information",
    "maintenance",
    "troubleshooting",
    "booking",
    "warranty",
    "pricing",
    "general_enquiry",
    "out_of_scope"
]


def classify_intent(message: str):

    prompt = f"""
You are an intent classification system for an
Automobile Customer Support Chatbot.

Classify the user's message into exactly one category:

greeting
vehicle_information
maintenance
troubleshooting
booking
warranty
pricing
general_enquiry
out_of_scope

Rules:
- Greetings such as Hi and Hello: greeting
- Questions about car parts and features: vehicle_information
- Servicing and maintenance: maintenance
- Vehicle faults and problems: troubleshooting
- Service appointment requests: booking
- Warranty questions: warranty
- Vehicle or service costs: pricing
- Other automobile-related queries: general_enquiry
- Unrelated questions: out_of_scope

Return ONLY the category name.

User message: {message}
"""

    response = get_llm().invoke(prompt)

    intent = response.content.strip().lower()

    # Extract a valid intent if the model adds extra text
    for valid_intent in VALID_INTENTS:
        if valid_intent in intent:
            return valid_intent

    return "general_enquiry"
