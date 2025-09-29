# Welcome the user to the quiz program
# Explain that they will answer multiple-choice questions

# Initialize a score counter to keep track of correct answers

# Present the first question
# Display the question text and the multiple-choice answers
# you can think of questions yourself, or find them online

# Get the user's input for their answer to the first question

# Check if the answer is correct
# If the answer is correct, print a success message and increase the score
# If the answer is incorrect, print the correct answer

# Repeat the above steps for additional questions (Question 2, Question 3, etc.)

# After all questions are answered, display the final score to the user
# Thank them for participating in the quiz

###### Extensions ######

# Use a loop to let people re-try the quiz
# create a leaderboard which stores users with the highest score
# Create a menu to let people access the leaderboard or the quiz
# Modularise the code to make it shorter and more maintainable
print("\n===== Quiz Game Menu =====")
print("1. Take the Quiz")
print("2. View Leaderboard")
print("3. Exit")
choice = input("Please select an option (1-3): ").strip()
match choice:
    case "1":
     print("Welcome to the quiz program!")
     print("You will answer multiple-choice questions.")
     score = 0
     # Question 1
     print("\nQuestion 1: What is the capital of China?")
     print("a) Beijing")
     print("b) Sichuan")
     print("c) Shanghai")
     print("d) Guangzhou")
     answer1 = input("Your answer (a/b/c/d): ").strip().lower()
     if answer1 == 'a':
         print("Correct!")
         score += 1
     else:
         print("Incorrect. The correct answer is a) Beijing.")
     # Question 2
     print("\nQuestion 2: In which year the first computer was invented?")
     print("a) 1935")
     print("b) 1946")
     print("c) 1945")
     print("d) 1950")
     answer2 = input("Your answer (a/b/c/d): ").strip().lower()
     if answer2 == 'b':
         print("Correct!")
         score += 1
     else:
         print("Incorrect. The correct answer is b) 1946.")
     # Question 3
     print("\nQuestion 3: Who is the founder of NVIDIA?")
     print("a) Steve Jobs")
     print("b Bill Gates")
     print("c) Jensen Huang")   
     print("d) Elon Musk")
     answer3 = input("Your answer (a/b/c/d): ").strip().lower()
     if answer3 == 'c':
         print("Correct!")
         score += 1
     else:
         print("Incorrect. The correct answer is c) Jensen Huang.")
     # Final Score
     print(f"\nYour final score is: {score}/3")
     print("Thank you for participating in the quiz!")
    case "2":
     print("Leaderboard feature is under development. Please check back later.")
    case "3":
     print("Exiting the program. Goodbye!")
    case _:
     print("Invalid choice. Please select a valid option (1-3).")