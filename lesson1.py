# Computer-based test program

# Dictionary to store questions, options, and correct answers
CBTquestions = {
    1: {"question": "What is the capital of nigeria?", 
        "options": ["A) Paris", "B) London", "C) Rome", "D) Abuja"], 
        "answer": "D"},
    2: {"question": "Which programming language are you learning?", 
        "options": ["A) Python", "B) JavaScript", "C) Java", "D) C++"], 
        "answer": "A"},
    3: {"question": "What is 5 * 60?", 
        "options": ["A) 253", "B) 300", "C) 356", "D) 409"], 
        "answer": "B"},
    4: {"question": "Who wrote the play 'Romeo and Juliet'?", 
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"], 
        "answer": "B"},
    5: {"question": "Which of these is a python data type?", 
        "options": ["A) list", "B) flex", "C) controllers", "D) Arrays "], 
        "answer": "A"}
}

# Function to administer the test
def take_test():
    score = 0
    print("\nStarting the test. Answer by selecting A, B, C, or D.")
    for q_no, q_data in CBTquestions.items():
        print(f"\nQuestion {q_no}: {q_data['question']}")
        for option in q_data['options']:
            print(option)
        while True:
            answer = input("Your answer: ").strip().upper()
            if answer in ['A', 'B', 'C', 'D']:
                break
            print("Invalid input. Please select A, B, C, or D.")
        if answer == q_data['answer']:
            score += 1
    print(f"\nYou scored {score} out of {len(CBTquestions)}.")
    return score

# Dictionary to store user results
results = {}

# Main program loop
while True:
    print("\n--- Computer-Based Test ---")
    print("1. Take the test")
    print("2. View results")
    print("3. Exit")
    
    action = input("Enter your choice (1/2/3): ").strip()
    
    if action == "1":
        name = input("\nEnter your name: ").strip()
        if name in results:
            print(f"{name}, you have already taken the test. Your previous score is {results[name]}.")
            retry = input("Do you want to retake the test? (yes/no): ").strip().lower()
            if retry != "yes":
                continue
        results[name] = take_test()
    elif action == "2":
        if results:
            print("\n--- Results ---")
            for user, score in results.items():
                print(f"{user}: {score} out of {len(CBTquestions)}")
        else:
            print("\nNo results available. Take the test first!")
    elif action == "3":
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
