print('Welcome to Geography quiz!')

playing = input("Do you want to play? ")
if playing.lower() == "yes":
    print("Okay! Let`s play!)")
else:
    quit()

score = 0

answer = input("What is the capital of France? ")
if answer.lower() == "paris":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the longest river in the world? ")
if answer.lower() == "nile":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the highest mountain in the world? ")
if answer.lower() == "everest":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the smallest country in the world? ")
if answer.lower() == "vatican":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What is the capital of Australia? ")
if answer.lower() == "canberra":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("Congatulations! You got", score, "questions correct!")
print("You got", ((score / 5) * 100), "%")

