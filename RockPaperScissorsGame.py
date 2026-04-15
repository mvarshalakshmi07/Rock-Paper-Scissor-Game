import random
choices = ["rock", "paper", "scissors"]
user_score = 0
computer_score = 0
while True:
    print("--- Rock Paper Scissors Game ---")
    print("1. Play")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        user = input("Enter rock, paper or scissors: ").lower()
        if user not in choices:
            print("Invalid input! Try again.")
            continue
        computer = random.choice(choices)
        print("User choice:", user)
        print("Computer choice:", computer)
        if user == computer:
            print("Result: It's a Draw!")
        elif (user == "rock" and computer == "scissors") or \
             (user == "paper" and computer == "rock") or \
             (user == "scissors" and computer == "paper"):
            print("Result: You Win!")
            user_score += 1
        else:
            print("Result: Computer Wins!")
            computer_score += 1
        print("\nScore -> You:", user_score, "| Computer:", computer_score)
    elif choice == "2":
        print("Final Score -> You:", user_score, "| Computer:", computer_score)
        print("Thanks for playing!")
        break
    else:
        print("Invalid menu choice!")