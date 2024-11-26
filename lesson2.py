# Registration and CBT program

# List to store registered users
users = []
results = {}

# Dictionary to store questions, options, and correct answers
questions = {
    1: {"question": "What is the capital of France?",
        "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"],
        "answer": "A"},
    2: {"question": "Which programming language is known as the 'language of the web'?",
        "options": ["A) Python", "B) JavaScript", "C) Java", "D) C++"],
        "answer": "B"},
    3: {"question": "What is 5 * 6?",
        "options": ["A) 25", "B) 30", "C) 35", "D) 40"],
        "answer": "B"},
    4: {"question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"],
        "answer": "B"},
    5: {"question": "Which planet is known as the Red Planet?",
        "options": ["A) Earth", "B) Mars", "C) Venus", "D) Jupiter"],
        "answer": "B"}
}

# Function to register a new user
def add_new_registration(firstname, lastname, email, state):
    new_user = {"firstname": firstname, "lastname": lastname, "email": email, "state": state}
    users.append(new_user)

# Function to take the test
def take_test():
    username = input("\nEnter your name (used to track your results): ").strip()
    if username in results:
        print(f"\nYou have already taken the test, {username}. Your score is {results[username]} out of {len(questions)}.")
        return
    
    score = 0
    print("\nStarting the test. Answer by selecting A, B, C, or D.")
    for q_no, q_data in questions.items():
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
    print(f"\nYou scored {score} out of {len(questions)}.")
    results[username] = score

# Main program loop
while True:
    print("\n--- Main Menu ---")
    print("1: Register")
    print("2: Take Test")
    print("3: View Results")
    print("4: Exit")
    
    permission = int(input("Enter your choice: "))
    
    if permission == 1:
        # Registration process
        firstname = input("Enter firstname: ")
        lastname = input("Enter lastname: ")
        email = input("Enter email: ")
        state = input("Enter state: ")
        add_new_registration(firstname, lastname, email, state)
        print("Registration successful!")
    
    elif permission == 2:
        # Take the test directly
        take_test()
    
    elif permission == 3:
        # View all results
        if results:
            print("\n--- Results ---")
            for user, score in results.items():
                print(f"{user}: {score} out of {len(questions)}")
        else:
            print("No results available. Users need to take the test first.")
    
    elif permission == 4:
        print("Exiting the program. Goodbye!")
        break
    
    else:
        print("Invalid choice. Please select a valid option.")
