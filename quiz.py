print("Hi there, do u want to play the quiz? ")
player = input().lower()
if player != "yes":
    quit()
print("alright letz! go! ")
score = 0
print("\n")
print("Who's there? : ")
ans = input().lower()
if ans != "knock knock":
    print("Incorrect!")
else:
    print("correct!***")
    score += 10
print("Who's there? : ")
ans = input().lower()
if ans != "knock knock":
    print("Incorrect!")
else:
    print("correct!***")
    score += 10
print("Theif? : ")
ans = input().lower()
if ans != "yes":
    print("Incorrect!")
else:
    print("correct!***")
    score += 10
print("Wat u want? : ")
ans = input().lower()
if ans != "jwells":
    print("Incorrect!")
else:
    print("correct!***")
    score += 10
print("i don't have it!!? : ")
ans = input().lower()
if ans != "ok bye!":
    print("Incorrect!")
else:
    print("correct!***")
    score += 10
print("you have successfully finished you're quiz , type yes to see youre score!")
ans = input().lower()
if ans != "yes":
    quit()
else:
    print("You're score is "+ str(score)+" !! congrats")
