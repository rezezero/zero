import re

responses = {
    r"\b(hi|hello|hey)\b": "Hello! Welcome to RedBus. How can I help you today?",
    r"\bhow are you\b": "I'm good! Ready to assist you with bus bookings ",
    r"\b(book ticket|book bus|bus booking)\b": "Sure! Please provide source, destination, and date.",
    r"\b(cancel ticket|cancellation)\b": "You can cancel your ticket from 'My Bookings' section.",
    r"\b(refund|refund status)\b": "Refunds are processed within 5-7 working days.",
    r"\b(search buses|available buses)\b": "Please provide your travel route and date.",
    r"\b(fare|ticket price)\b": "Fares depend on route and bus type.",
    r"\b(discount|offers)\b": "Use code BUS10 to get discount on booking!",
    r"\b(payment|payment options)\b": "We accept UPI, cards, net banking, wallets.",
    r"\b(track bus|live tracking)\b": "Live tracking is available before departure.",
    r"\bluggage\b": "Up to 15kg luggage is allowed per passenger.",
    r"\b(sleeper|ac bus|non ac)\b": "We offer AC, Non-AC, Sleeper buses.",
    r"\b(customer care|support)\b": "Call 1800-123-1234 for support.",
    r"\b(bye|exit)\b": "Goodbye! Safe travels "
}

def chatbot_response(u):
    u = u.lower().strip()
    return next((r for p, r in responses.items() if re.search(p, u)),
                "Sorry, I didn't understand. Please ask about booking, cancellation, or bus services.")

print("=== RedBus Chatbot ===\nType 'exit' to stop chat.\n")

while True:
    u = input("You: ")
    if u.lower() == "exit":
        print("Chatbot: Goodbye! Safe travels ")
        break
    print("Chatbot:", chatbot_response(u))