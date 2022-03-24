def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1
    for key in questions:
        print("-----------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter(A,B,C or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1

    display_score(correct_guesses,guesses)

def check_answer(answer, guess):
    if answer == guess:
        print("correct!")
        return 1
    else:
        print("wrong")
        return 0
def display_score(correct_guesses, guesses):
    print("---------------------------")
    print("RESULTS")
    print("---------------------------")
    print("Answers:", end=" ")

    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = ((correct_guesses / len(questions)) * 100)
    print("your score is: " + str(score) + "%")

def play_again():
    response = input("do u want to play again? (yes or no): ")
    response = response.upper()

    if response == "yes":
        return True
    else:
        return False


questions = {
    "who created python? ": "A",
    "what year was pyhon created? ": "B",
    "python is tributed to which comedy? ": "C",
    "Is the earth round? ": "A"
}
options = [["A. Guido Rossum","B. Elon musk","C. Bill Gate","D. Mark zuckerburg"],
            ["A. 1989","B. 1991","C. 2000","D. 2016"],
            ["A. Lonely Island","B. smosh","C. Monty Python","D. SNL"],
            ["A. True","B. False","C. Sometimes","D. What's earth?"]]
new_game()
while play_again():
    new_game()
print("Byeeeeeeee")



