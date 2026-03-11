# 🧠 Python Quiz Game

A simple **command-line quiz game** built with Python.  
The program asks multiple-choice questions, checks your answers, and displays your final score at the end.

This project is great for beginners learning:
- Python functions
- Lists and dictionaries
- User input handling
- Basic program structure

---

# ✨ Features

## ❓ Multiple Choice Questions
Each question includes four options (a–d).

Example:

What is the capital of France?

a) Paris  
b) London  
c) Berlin  
d) Rome

---

## ✅ Instant Feedback
After answering a question, the program immediately tells you whether your answer is correct or incorrect.

Example:

```
✅ Correct!
```

or

```
❌ Wrong! The correct answer was 'a'.
```

---

## 📊 Score Tracking
Your score increases for every correct answer.

At the end of the quiz you will see:

```
🎉 Quiz Over! Your final score is 4/5
```

---

# 📦 Requirements

Python **3.6 or higher**

No external libraries are required.  
The program uses only built-in Python functionality.

---

# ▶️ How to Run

1. Save the script as:

```
quiz_game.py
```

2. Run it using:

```bash
python quiz_game.py
```

---

# 🎮 Example Gameplay

```
Welcome to the Python Quiz Game!

What is the capital of France?
a) Paris
b) London
c) Berlin
d) Rome

Your answer (a/b/c/d): a
✅ Correct!
```

---

# ⚙️ How It Works

### Question Function
Each question is handled by the function:

```
ask_question(question, options, correct_answer)
```

This function:
1. Displays the question
2. Shows all options
3. Takes user input
4. Checks the answer
5. Returns a score value

---

### Questions Storage

All quiz questions are stored inside a list of dictionaries.

Example structure:

```
{
  "question": "What is the capital of France?",
  "options": {"a": "Paris", "b": "London", "c": "Berlin", "d": "Rome"},
  "answer": "a"
}
```
