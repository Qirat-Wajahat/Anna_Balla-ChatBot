import webbrowser as wb
import datetime as dt

# Define chatbot responses
def get_time():
    current_time = dt.datetime.now().strftime("%I:%M:%S %p")
    return f"The current time is {current_time}."

def open_website(query):
    websites = {
        "youtube": "https://www.youtube.com",
        "google": "https://www.google.com",
        "facebook": "https://www.facebook.com",
        "twitter": "https://www.twitter.com",
        "instagram": "https://www.instagram.com",
        "github": "https://www.github.com",
        "stackoverflow": "https://stackoverflow.com",
        "gmail": "https://mail.google.com",
    }

    for site in websites:
        if site in query:
            return {"message": f"{site.capitalize()} is opened...", "open_url": websites[site]}
    
    return {"message": "Sorry, I don't recognize that website. Try asking to open YouTube, Google, etc."}


    
def do_math(query):
    try:
        # Remove unnecessary text
        query = query.lower().replace("calculate", "").replace("what is", "").replace("?", "").strip()
        result = eval(query, {"__builtins__": None}, {})
        return f"The answer is {result}"
    except Exception:
        return "Sorry, I couldn't calculate that. Please try a simpler expression (e.g., 5 + 3)."

# Response map
response_map = {
    "hello": "Hello! How can I assist you today?",
    "hi": "Hello! How can I assist you today?",
    "hey": "Hey there! What can I do for you?",
    "your name": "My name is Anna Belle. I'm a simple chatbot created to assist you.",
    "what can you do": "I can greet you, tell you the time, open websites, perform simple math, and answer basic questions.",
    "your purpose": "I'm here to help you with simple tasks and queries.",
    "bye": "Goodbye! Have a great day.",
    "see you": "See you soon!",
    "goodbye": "Take care! Goodbye!",
    "exit": "Conversation ended. Thank you!",
    "quit": "Conversation ended. Thank you!",
    "who made you": "I was created by Qirat Wajahat.",
    
}

# Main chatbot logic
def chatbot(query):
    query = query.lower().strip()

    if "time" in query:
        return {"message": get_time()}
    elif "open" in query:
        return open_website(query)
    
    elif "calculate" in query or any(op in query for op in ["+", "-", "*", "/", "%"]):
        return {"message": do_math(query)}

    for key in response_map:
        if key in query:
            return {"message": response_map[key]}

    return {"message": "I'm not sure how to respond to that yet."}

def main(query):
    print("User:", query)
    response = chatbot(query)
    print("Bot:", response["message"])
    return response
