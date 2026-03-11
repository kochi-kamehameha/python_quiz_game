# Quiz Game in Python

def ask_question(question, options, correct_answer):
    """
    Ask a question to the user, show options, and check the answer.
    Returns 1 if correct, 0 if incorrect.
    """
    print("\n" + question)
    for key, value in options.items():
        print(f"  {key}) {value}")
    
    answer = input("Your answer (a/b/c/d): ").lower()
    
    if answer == correct_answer:
        print("✅ Correct!")
        return 1
    else:
        print(f"❌ Wrong! The correct answer was '{correct_answer}'.")
        return 0

def run_quiz():
    """
    Runs the quiz game with multiple questions.
    """
    print("Welcome to the Python Quiz Game!")
    print("Try to answer the following questions:\n")
    
    # List of questions
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {"a": "Paris", "b": "London", "c": "Berlin", "d": "Rome"},
            "answer": "a"
        },
        {
            "question": "Which language is used to create this game?",
            "options": {"a": "Java", "b": "Python", "c": "C++", "d": "Ruby"},
            "answer": "b"
        },
        {
            "question": "What does 'CPU' stand for?",
            "options": {"a": "Central Processing Unit", "b": "Computer Personal Unit",
                        "c": "Central Performance Utility", "d": "Computer Processing Unit"},
            "answer": "a"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "options": {"a": "Earth", "b": "Mars", "c": "Jupiter", "d": "Venus"},
            "answer": "b"
        },
        {
            "question": "Which is a Python data type?",
            "options": {"a": "integer", "b": "string", "c": "list", "d": "All of the above"},
            "answer": "d"
        }
    ]
    
    score = 0
    for q in questions:
        score += ask_question(q["question"], q["options"], q["answer"])
    
    print(f"\n🎉 Quiz Over! Your final score is {score}/{len(questions)}")

# Start the quiz
if __name__ == "__main__":

    run_quiz()
