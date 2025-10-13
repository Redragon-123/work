# Step 1: Create an empty list to hold quiz questions.

# Step 2: Define a function to add a new quiz question.
# This function should prompt the user for the question, options, and the correct answer.
# Store each question as a dictionary in the list.
# hint: dictionary could have keys like 'question', 'options', 'correct_answer'
# hint: options could be stored as a list of strings

# Step 3: Define a function to write the quiz questions to a file called 'quiz_questions.txt'.
# Format the questions nicely for readability, including the question text and possible answers.
# hint: loop through your list of dictionaries
# hint: use \n for formatting and spacing between questions

# Step 4: Define a function to display all current quiz questions in the console.
# hint: similar to step 3, but use print() instead of file writing

# Step 5: In the main part of the program:
# - Call the function to add questions in a loop until the user decides to stop.
# - After finishing, call the function to write all questions to 'quiz_questions.txt' in a nice, human-readable format
# - Optionally, display the questions on the console before writing them to the file.
# hint: use a while loop and you could ask user if they want to continue after each question
list_questions = []
def add_question():
    question=input("Please enter a question:")
    options=[]
    for i in range(4):
        option=input(f"Enter option {i+1}:")
        options.append(option)
    while True:
        correct_answer = input("Enter the correct answer (1-4):")
        if correct_answer in ['1', '2', '3', '4']:
            break
        print("Invalid input! Please enter a number between 1 and 4.")
    question_dict={'question': question, 'options': options, 'correct_answer': correct_answer}
    list_questions.append(question_dict)
def write_questions_to_file():
    with open('quiz_questions.txt','w') as outfile:
        for item in list_questions:
            outfile.write(item["question"] + "\n")
            outfile.write(f"1. {item['options'][0]}\n")
            outfile.write(f"2. {item['options'][1]}\n")
            outfile.write(f"3. {item['options'][2]}\n")
            outfile.write(f"4. {item['options'][3]}\n")
            outfile.write(f"Correct Answer: Option {item['correct_answer']}\n\n")
def display_questions():
    with open('quiz_questions.txt','r') as infile:
        for line in infile:
            print(line.strip())
while True:
    add_question()
    cont=input("Do you want to add another question? (y/n):")
    if cont.lower() != 'y':
        break
write_questions_to_file()
display_questions()