
from app.orchestrator.intent_classifier import classify_intent
from app.rag.rag_chain import generate_rag_response


def route_query(message: str):

    intent = classify_intent(message)

    print("DETECTED INTENT:", intent)

    if intent == "greeting":
        return {
            "intent": intent,
            "answer": (
                "Hello! Welcome to Automobile Customer Support. "
                "How can I help you with your vehicle today?"
            ),
            "sources": []
        }

    if intent == "out_of_scope":
        return {
            "intent": intent,
            "answer": (
                "I can help with automobile-related questions, "
                "including vehicle information, maintenance, "
                "troubleshooting and warranty."
            ),
            "sources": []
        }

    result = generate_rag_response(message)

    return {
        "intent": intent,
        "answer": result["answer"],
        "sources": result["sources"]
    }
