print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play!")

Score = 0

answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
    print("Correct!")
    Score = Score + 1
else:
    print("Incorrect!")
    
answer = input("What does 10/2 equal? ")
if answer.lower() == "5":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("What is the color of the sky? ")
if answer.lower() == "blue":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Who is our current President? ")
if answer.lower() == "joe biden":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

answer = input("Where is the Eiffel Tower? ")
if answer.lower() == "paris":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

print(f"You've reached the end of this game, you got {Score} questions correct")
print(f"Your score is {(Score/5)*100} %")


if Score >= 4:
    print("Congratulations, you passed!")
else:
    print("Sorry, you didn't pass this quiz.")








    
