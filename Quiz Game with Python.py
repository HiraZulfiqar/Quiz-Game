score = 0
def check_guess (question, answer):
    global score
    for attempt in range(3):
        guess = input(question + " ")
        if guess.lower() == answer.lower():
            print("correct answer")
            score +=1
            return
        else:
            print("sorry, wrong answer. try again!")
            print("the correct answer is: ", answer)

print("guess the animal")
check_guess("which bear lives at the north pole?", "polar bear")
check_guess("which is the fastest land animal?", "cheetah")
check_guess("which isthe largest animal?", "blue whale")
print("your score is", score)
            
