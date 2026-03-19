print("Yo! Welcome to my quiz game!")

play_game = input("Are you interested in playing? (Yes/No) ")
print(play_game)

if play_game.lower() != "yes":
    quit()

print("awesome! Let's get this quiz started :) ")
score = 0

answer = input("What is the capital of VA? ")
if answer == "Richmond":
    print("That's right!")
    score += 1
else:
    print("Sorry, that's not it.")

answer = input("What state the Mall of America Located? ")
if answer == "Minnesota":
    print("That's right!")
    score += 1
else:
    print("Nope. Not that state!")


answer = input("Is Washington D.C. a state? ")
if answer == "No":
    print("You got it!")
    score += 1
else:
    print("Nope. It's the capital of the U.S.")

print(f"You got {score} questions right!")
print(f"You got {score/3*100:.2f} % of the questions right!")