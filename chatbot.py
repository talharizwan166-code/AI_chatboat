"""
Rule-Based AI Chatbot
DecodeLabs Industrial Training Kit - AI Project 1
A beginner-friendly chatbot using if-elif-else statements and rule-based logic.

Author: Talha Rizwan
"""

import datetime
import random
from time import sleep


# ============================================================================
# CONSTANTS AND DATA STRUCTURES
# ============================================================================

GREETINGS = ['hi', 'hello', 'hey', 'good morning', 'good evening', 'greetings', 'sup', 'hola']
EXIT_COMMANDS = ['bye', 'exit', 'quit', 'goodbye', 'see you', 'bye bye', 'take care']

# Dictionary for greeting responses
GREETING_RESPONSES = [
    "Hello! Welcome to the AI Chatbot. How can I help you?",
    "Hi there! Nice to meet you. What can I do for you?",
    "Hey! Good to see you. How are you doing today?",
    "Greetings! I'm here to help. What's on your mind?"
]

# Jokes database
JOKES = [
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "Why did the developer go broke? Because he used up all his cache!",
    "How many programmers does it take to change a light bulb? None, that's a hardware problem!",
    "Why do Java developers wear glasses? Because they can't C#!",
    "How many programmers does it take to change a light bulb? Zero, that's what dark mode is for!",
    "Why was the Python programmer sad? Because they didn't have any class!"
]

# Fun facts database
FUN_FACTS = [
    "Did you know? Python was named after the comedy series 'Monty Python', not the snake!",
    "Did you know? The first computer bug was an actual moth found in a computer in 1945!",
    "Did you know? AI was first coined as a term by John McCarthy in 1956!",
    "Did you know? The @ symbol is called 'at sign' but in programming, it's often called 'at monkey'!",
    "Did you know? The first chatbot was called ELIZA, created in 1966!",
    "Did you know? Machine learning was a concept that emerged in the 1950s!",
]

# Motivation quotes
QUOTES = [
    "The only way to do great work is to love what you do. - Steve Jobs",
    "Code is poetry written for computers. - Unknown",
    "Every expert was once a beginner. - Unknown",
    "Stay hungry, stay foolish. - Steve Jobs",
    "Innovation distinguishes between a leader and a follower. - Steve Jobs",
    "The future belongs to those who believe in the beauty of their dreams. - Eleanor Roosevelt"
]


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def show_welcome():
    """Display a welcome banner at the start of the program."""
    print("\n" + "="*70)
    print(" "*15 + "🤖 RULE-BASED AI CHATBOT 🤖")
    print(" "*10 + "DecodeLabs Industrial Training Kit - AI Project 1")
    print("="*70)
    print("\n✨ Welcome to the Interactive AI Chatbot!")
    print("📝 Type 'help' to see what I can do.")
    print("🚪 Type 'bye' or 'exit' to quit.\n")
    sleep(0.5)


def show_help():
    """Display help information about available commands."""
    print("\n" + "="*70)
    print("📚 HELP MENU - Available Commands")
    print("="*70)
    print("\n👋 GREETINGS:")
    print("   • hi, hello, hey, good morning, good evening")

    print("\n❓ QUESTIONS I CAN ANSWER:")
    print("   • 'What is your name?' / 'Who are you?'")
    print("   • 'Who created you?'")
    print("   • 'How are you?'")
    print("   • 'What can you do?'")
    print("   • 'What is your favorite programming language?'")
    print("   • 'Tell me about AI'")

    print("\n⏰ INFORMATION:")
    print("   • 'What is the time?' / 'Tell me the time'")
    print("   • 'What is the date?' / 'Tell me the date'")
    print("   • 'What day is it today?' / 'What is today?'")

    print("\n😂 ENTERTAINMENT:")
    print("   • 'Tell me a joke' / 'Make me laugh'")
    print("   • 'Tell me a fact' / 'Fun fact'")
    print("   • 'Motivate me' / 'Tell me a quote'")

    print("\n🔢 CALCULATOR:")
    print("   • 'Calculator' / 'Open calculator'")
    print("   • Format: number1 operator number2 (e.g., '5 + 3')")

    print("\n🚪 EXIT:")
    print("   • bye, exit, quit, goodbye")

    print("\n💡 OTHER:")
    print("   • 'Thank you' / 'Thanks'")
    print("   • Type 'help' anytime to see this menu")
    print("="*70 + "\n")


def show_goodbye(total_messages, recognized_commands):
    """Display a goodbye message with session statistics."""
    print("\n" + "="*70)
    print("👋 Thank you for chatting with me!")
    print("="*70)
    print(f"\n📊 SESSION STATISTICS:")
    print(f"   • Total messages received: {total_messages}")
    print(f"   • Recognized commands: {recognized_commands}")
    print(f"   • Unrecognized inputs: {total_messages - recognized_commands}")
    if total_messages > 0:
        recognition_rate = (recognized_commands / total_messages) * 100
        print(f"   • Recognition rate: {recognition_rate:.1f}%")
    print(f"\n🎉 Session ended at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    print("\n👨‍💻 Created by: DecodeLabs AI Intern")
    print("📅 Date: 2026-07-14")
    print("🐍 Language: Python 3.x\n")


# ============================================================================
# FEATURE FUNCTIONS
# ============================================================================

def get_current_time():
    """Get and return the current time in a formatted string."""
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    return f"The current time is: {current_time}"


def get_current_date():
    """Get and return the current date in a formatted string."""
    current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
    return f"Today is: {current_date}"


def get_current_day():
    """Get and return the current day of the week."""
    current_day = datetime.datetime.now().strftime("%A")
    return f"Today is: {current_day}"


def get_weather_response():
    """Return a static weather response."""
    weather_responses = [
        "I don't have real-time weather data, but I hope it's sunny where you are! ☀️",
        "Weather updates require internet access, but I'm sure it's beautiful outside! 🌤️",
        "For accurate weather information, check a weather service. Stay safe! 🌈",
    ]
    return random.choice(weather_responses)


def tell_joke():
    """Tell a random programming joke."""
    joke = random.choice(JOKES)
    return f"😂 Here's a joke for you:\n   {joke}"


def tell_fact():
    """Tell a random fun fact."""
    fact = random.choice(FUN_FACTS)
    return f"🧠 Fun Fact:\n   {fact}"


def get_motivation():
    """Get a random motivation quote."""
    quote = random.choice(QUOTES)
    return f"💪 Motivation Quote:\n   \"{quote}\""


def calculator():
    """Simple calculator for basic arithmetic operations."""
    print("\n" + "-"*50)
    print("🔢 SIMPLE CALCULATOR")
    print("-"*50)
    print("Supported operations: +, -, *, /")
    print("Example: '5 + 3' or '10 * 2'\n")

    try:
        calculation = input("Enter your calculation (or 'back' to exit): ").strip()

        if calculation.lower() == 'back':
            return "Calculator closed. Back to chatting!"

        # Parse the calculation
        parts = calculation.split()

        if len(parts) != 3:
            return "❌ Invalid format. Please use: number operator number (e.g., '5 + 3')"

        try:
            num1 = float(parts[0])
            operator = parts[1]
            num2 = float(parts[2])
        except ValueError:
            return "❌ Invalid numbers. Please enter valid numbers."

        # Perform calculation based on operator
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                return "❌ Cannot divide by zero!"
            result = num1 / num2
        else:
            return f"❌ Unknown operator '{operator}'. Supported: +, -, *, /"

        # Format result to remove unnecessary decimals
        if isinstance(result, float) and result.is_integer():
            result = int(result)

        return f"✅ Result: {num1} {operator} {num2} = {result}"

    except Exception as e:
        return f"❌ Error in calculation: {str(e)}"


def get_ai_info():
    """Provide information about AI."""
    ai_info = """
    🤖 ARTIFICIAL INTELLIGENCE - Quick Overview:

    • Definition: AI refers to computer systems designed to perform tasks
      that typically require human intelligence.

    • Types:
      - Narrow AI: Designed for specific tasks (like chatbots, recommendation systems)
      - General AI: Theoretical AI that can perform any intellectual task

    • Key Areas:
      - Machine Learning: Systems that learn from data
      - Natural Language Processing: Understanding human language
      - Computer Vision: Understanding images
      - Robotics: Autonomous machines

    • This Chatbot: Uses rule-based AI (if-elif-else logic) without machine learning!

    • Future: AI will revolutionize healthcare, education, transportation, and more!
    """
    return ai_info


# ============================================================================
# MAIN CHATBOT LOGIC
# ============================================================================

def get_response(user_input):
    """
    Process user input and return appropriate response.

    Parameters:
        user_input (str): The user's input message

    Returns:
        tuple: (response_message, is_recognized)
    """
    # Normalize input: convert to lowercase and strip extra spaces
    user_input_clean = user_input.lower().strip()

    # Remove extra spaces between words
    user_input_clean = ' '.join(user_input_clean.split())

    # Check if input is empty
    if not user_input_clean:
        return "I didn't catch that. Could you say something?", False

    # Check for greetings
    if any(greeting in user_input_clean for greeting in GREETINGS):
        response = random.choice(GREETING_RESPONSES)
        return response, True

    # Check for name questions
    if any(phrase in user_input_clean for phrase in ['what is your name', 'who are you', 'your name']):
        return "My name is RulesBot! I'm a rule-based AI chatbot created to demonstrate fundamental AI concepts.", True

    # Check for creator questions
    if any(phrase in user_input_clean for phrase in ['who created', 'who made', 'your creator', 'your developer']):
        return "I was created by DecodeLabs as an AI training project to teach rule-based chatbot development.", True

    # Check for 'how are you' questions
    if any(phrase in user_input_clean for phrase in ['how are you', 'how are you doing', 'how do you feel']):
        responses = [
            "I'm doing great! Thanks for asking! 😊",
            "I'm functioning perfectly! Ready to help you. ⚙️",
            "Excellent! I'm here and ready to assist. 🚀"
        ]
        return random.choice(responses), True

    # Check for 'what can you do' questions
    if any(phrase in user_input_clean for phrase in ['what can you do', 'your capabilities', 'what can you help', 'what do you do']):
        capabilities = """
I'm a rule-based AI chatbot and I can:
• Answer greetings and questions
• Tell you the current time and date
• Tell jokes to make you laugh 😂
• Share fun facts about tech and AI 🧠
• Motivate you with inspiring quotes 💪
• Perform simple calculations (+ - * /)
• Provide information about AI
• Remember our conversation statistics
• And much more! Type 'help' to learn more!
        """
        return capabilities, True

    # Check for time questions
    if any(phrase in user_input_clean for phrase in ['what is the time', 'tell me the time', 'current time', 'what time']):
        return get_current_time(), True

    # Check for date questions
    if any(phrase in user_input_clean for phrase in ['what is the date', 'tell me the date', 'current date', 'what date']):
        return get_current_date(), True

    # Check for day questions
    if any(phrase in user_input_clean for phrase in ['what day', 'what is today', 'today', 'current day']):
        return get_current_day(), True

    # Check for thank you
    if any(phrase in user_input_clean for phrase in ['thank you', 'thanks', 'thank you so much', 'appreciate']):
        responses = [
            "You're welcome! Happy to help! 😊",
            "No problem! Feel free to ask anytime!",
            "Always happy to assist! Anything else?"
        ]
        return random.choice(responses), True

    # Check for jokes
    if any(phrase in user_input_clean for phrase in ['tell me a joke', 'make me laugh', 'joke', 'funny']):
        return tell_joke(), True

    # Check for facts
    if any(phrase in user_input_clean for phrase in ['tell me a fact', 'fun fact', 'fact', 'facts']):
        return tell_fact(), True

    # Check for motivation/quotes
    if any(phrase in user_input_clean for phrase in ['motivate me', 'quote', 'motivate', 'inspire']):
        return get_motivation(), True

    # Check for favorite programming language
    if any(phrase in user_input_clean for phrase in ['favorite programming language', 'best programming language', 'which language']):
        return "My favorite is Python! 🐍 It's beginner-friendly, versatile, and perfect for AI projects!", True

    # Check for AI questions
    if any(phrase in user_input_clean for phrase in ['tell me about ai', 'what is ai', 'artificial intelligence', 'ai information']):
        return get_ai_info(), True

    # Check for weather
    if any(phrase in user_input_clean for phrase in ['what is the weather', 'weather', 'how is the weather']):
        return get_weather_response(), True

    # Check for calculator request
    if any(phrase in user_input_clean for phrase in ['calculator', 'calculate', 'open calculator', 'start calculator']):
        return calculator(), True

    # Check for help
    if user_input_clean == 'help' or 'help' in user_input_clean:
        show_help()
        return "Help menu displayed above! 👆", True

    # Default response for unrecognized input
    default_responses = [
        "I'm not sure I understand. Could you rephrase that? Try 'help' for available commands.",
        "Hmm, that's not something I can help with. Type 'help' to see what I can do!",
        "I didn't quite get that. Ask me about the time, tell you a joke, or type 'help'!",
        "I'm still learning! That's beyond my knowledge. Try 'help' for more options."
    ]
    return random.choice(default_responses), False


# ============================================================================
# MAIN PROGRAM
# ============================================================================

def main():
    """
    Main function to run the chatbot.
    This is the entry point of the program.
    """
    show_welcome()

    total_messages = 0
    recognized_commands = 0

    while True:
        try:
            # Get user input
            user_input = input("📢 You: ").strip()

            # Check if user wants to exit
            if user_input.lower() in EXIT_COMMANDS:
                show_goodbye(total_messages, recognized_commands)
                break

            # Skip empty input
            if not user_input:
                continue

            # Increment message counter
            total_messages += 1

            # Get response from chatbot
            response, is_recognized = get_response(user_input)

            # Track recognized commands
            if is_recognized:
                recognized_commands += 1

            # Display response
            print(f"\n🤖 Chatbot: {response}\n")

        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n\n⚠️  Program interrupted by user.")
            show_goodbye(total_messages, recognized_commands)
            break

        except Exception as e:
            # Handle any unexpected errors
            print(f"\n❌ An error occurred: {str(e)}")
            print("Please try again.\n")


# ============================================================================
# PROGRAM ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()
