# Rule-Based AI Chatbot

## 📋 Project Overview

A complete **beginner-friendly Rule-Based AI Chatbot** built with Python, designed for the DecodeLabs Industrial Training Kit - AI Project 1. This chatbot demonstrates fundamental AI concepts using **if-elif-else statements** and rule-based logic without any machine learning.

**Key Highlight:** Built by an AI intern - interactive, readable, and creative while remaining purely rule-based.

---

## ✨ Features

### Core Functionality
- ✅ **Continuous Operation** - Runs in a while loop accepting user input until exit
- ✅ **Case-Insensitive Input** - Handles all input variations seamlessly
- ✅ **Greeting Recognition** - Responds to hi, hello, hey, good morning, good evening, etc.
- ✅ **Exit Commands** - bye, exit, quit, goodbye, see you
- ✅ **Multi-way Question Handling** - Same question asked multiple ways gets answers

### Interactive Commands
| Category | Commands |
|----------|----------|
| **Greetings** | hi, hello, hey, good morning, good evening |
| **Information** | What's your name? Who created you? How are you? |
| **Time & Date** | What time is it? What's the date? What day today? |
| **Entertainment** | Tell me a joke, Fun fact, Motivate me |
| **Calculator** | calculator (supports +, -, *, /) |
| **Learning** | What can you do? Tell me about AI, Favorite language? |
| **Help** | help (displays full command menu) |

### Extra Features
- 🎯 **Welcome Banner** - Professional startup greeting
- 📊 **Session Statistics** - Tracks total messages, recognized commands, and recognition rate
- 🎨 **Colored Output** - Emoji-enhanced responses for better UX
- 💾 **Function-Based Architecture** - Organized, maintainable code structure
- 📝 **Full Documentation** - Docstrings and comments throughout
- ⚠️ **Error Handling** - Graceful handling of unexpected inputs and interrupts (Ctrl+C)

---

## 🛠️ Installation

### Prerequisites
- Python 3.x (3.8 or higher recommended)
- No external dependencies required (uses only built-in libraries)

### Setup Steps

1. **Download/Clone the project:**
   ```bash
   cd your_project_directory
   ```

2. **Verify Python installation:**
   ```bash
   python --version
   # or
   python3 --version
   ```

3. **File Structure:**
   ```
   chatbot_project/
   ├── chatbot.py              # Main chatbot application
   ├── README.md               # This file
   ├── PROJECT_REPORT.md       # Detailed project report
   ├── CODE_EXPLANATION.md     # In-depth code walkthrough
   ├── VIVA_QUESTIONS.md       # 20 viva questions with answers
   └── SAMPLE_OUTPUT.txt       # Complete sample conversation
   ```

---

## 🚀 How to Run

### Method 1: Direct Execution
```bash
python chatbot.py
```

### Method 2: Using Python3
```bash
python3 chatbot.py
```

### Method 3: From any directory (if added to PATH)
```bash
python path/to/chatbot.py
```

### Sample Interaction
```
================================================================================
             🤖 RULE-BASED AI CHATBOT 🤖
         DecodeLabs Industrial Training Kit - AI Project 1
================================================================================

✨ Welcome to the Interactive AI Chatbot!
📝 Type 'help' to see what I can do.
🚪 Type 'bye' or 'exit' to quit.

📢 You: hello
🤖 Chatbot: Hi there! Nice to meet you. What can I do for you?

📢 You: what is the time
🤖 Chatbot: The current time is: 14:35:22

📢 You: bye
```

---

## 📋 Sample Commands

### Greetings
```
> hello
> hi there
> good morning
```

### Asking Questions
```
> What is your name?
> Who created you?
> How are you doing?
> What can you do?
```

### Getting Information
```
> What's the time?
> Tell me the date
> What day is today?
```

### Entertainment
```
> Tell me a joke
> Fun fact
> Motivate me
```

### Using Calculator
```
> calculator
> 15 + 25
> 100 * 2
> 50 / 5
```

### Getting Help
```
> help
```

### Exiting
```
> bye
> exit
> quit
> goodbye
```

---

## 📁 Folder Structure

```
E:\Decodes lab\week 1\
│
├── chatbot.py                    # Main application file (700+ lines)
│   ├── Constants & Data          # Greetings, jokes, facts, quotes
│   ├── Display Functions         # Welcome, help, goodbye messages
│   ├── Feature Functions         # Time, date, calculator, jokes
│   ├── Main Logic                # Response generation (get_response)
│   └── Entry Point               # main() and __main__
│
├── README.md                     # Project overview & setup guide
├── PROJECT_REPORT.md             # Professional project report
├── CODE_EXPLANATION.md           # Detailed concept explanations
├── VIVA_QUESTIONS.md            # 20 interview questions
└── SAMPLE_OUTPUT.txt            # Complete sample conversation
```

---

## 🧠 Python Concepts Used

1. **if-elif-else Statements** - Decision making
2. **while Loops** - Continuous program execution
3. **Functions** - Code organization and reusability
4. **String Methods** - lower(), strip(), split(), join()
5. **Lists & Dictionaries** - Data storage
6. **String Formatting** - f-strings
7. **datetime Module** - Time and date handling
8. **random Module** - Random selection from lists
9. **Exception Handling** - try-except blocks
10. **Comments & Docstrings** - Code documentation

---

## 🎓 Learning Outcomes

After completing this project, you will understand:
- How rule-based systems work
- Control flow in Python (if-elif-else, while loops)
- Function definition and calling
- String manipulation and normalization
- Module usage (datetime, random)
- Code organization and best practices
- Error handling and user input validation
- PEP 8 coding standards

---

## 🔄 How It Works

```
START
  ↓
Show Welcome Banner
  ↓
Display Instructions
  ↓
Enter Main Loop
  │
  ├─ Get User Input
  │  ├─ Normalize (lowercase, strip spaces)
  │  └─ Check if exit command
  │
  ├─ Process Input
  │  ├─ Check greetings
  │  ├─ Check questions (if-elif chain)
  │  ├─ Check commands
  │  └─ Return default response if no match
  │
  ├─ Display Response
  │  └─ Update statistics
  │
  └─ Repeat until EXIT
     ↓
   Show Statistics
     ↓
   EXIT
```

---

## 🚀 Future Enhancements

1. **User Profile Management** - Remember user name and preferences
2. **Conversation History** - Save and replay conversations
3. **File-Based Knowledge Base** - Load responses from external files
4. **Advanced Calculator** - Support for math functions (sin, cos, sqrt)
5. **Sentiment Analysis** - Basic emotion detection
6. **Multi-Language Support** - Handle multiple languages
7. **GUI Interface** - Tkinter-based graphical interface
8. **Database Integration** - Store user data and chat history
9. **Web API** - Flask/Django backend with REST API
10. **Machine Learning Integration** - Natural Language Processing with ML models

---

## 📊 Code Statistics

- **Total Lines:** 700+
- **Functions:** 15+
- **Documented:** 100% (All functions have docstrings)
- **Comments:** Extensive inline documentation
- **Modules Used:** datetime, random, time
- **External Dependencies:** None (only Python standard library)

---

## ✅ Testing Checklist

- [x] Greetings recognized
- [x] Questions answered
- [x] Time/Date functionality works
- [x] Calculator functional
- [x] Jokes/Facts display correctly
- [x] Statistics tracked accurately
- [x] Exit commands work
- [x] Error handling active
- [x] Case-insensitive input
- [x] Extra spaces ignored

---

## 🎯 Completion Requirements

✅ Complete Python Code - chatbot.py
✅ Code Explanation - CODE_EXPLANATION.md
✅ Sample Output - SAMPLE_OUTPUT.txt
✅ Project Report - PROJECT_REPORT.md
✅ Viva Questions - VIVA_QUESTIONS.md
✅ README - This file

---

## 👨‍💻 Project Details

- **Created by:** DecodeLabs AI Intern
- **Date:** 2026-07-14
- **Training Kit:** DecodeLabs Industrial Training Kit - AI Project 1
- **Language:** Python 3.x
- **Status:** Complete & Tested ✅

---

## 📞 Support

For questions or improvements:
1. Review the CODE_EXPLANATION.md for detailed concept explanations
2. Check VIVA_QUESTIONS.md for common issues
3. Run with the provided SAMPLE_OUTPUT.txt as reference
4. Consult the PROJECT_REPORT.md for architecture details

---

## 📜 License

This project is created for educational purposes as part of the DecodeLabs Industrial Training Kit.

**Happy Coding! 🚀**
