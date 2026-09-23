import requests
import random
import html


while True:
    try:
        questions_num = int(input("How many questions do you want: "))
        break
    except ValueError:
        print("You have to enter a num. Try again.")


call = requests.get(f"https://opentdb.com/api.php?amount={questions_num}").json()

points = 0
question_num = 1 

for question in call["results"]:
    possible_answers = question["incorrect_answers"]
    possible_answers.append(question["correct_answer"])
    random.shuffle(possible_answers)

    print(f"Question number {question_num}.")
    print("Category:",question["category"])
    print("Question:",question["question"])
    possible_answers_num = 1
    for answer in possible_answers:
        print(f"{possible_answers_num}. answer: {answer}")
        possible_answers_num += 1
    
    user_result = int(input("Enter the number of correct result: "))
    if possible_answers[user_result-1] == question["correct_answer"]:
        print("You are right.")
        points += 1
    else:
        print("You are wrong.")

    question_num += 1

print(40*"-")
print(f"You got {points} right.")