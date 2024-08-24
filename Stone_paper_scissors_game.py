import random

options = ["stone","paper","scissors"]
user_wins = 0
AI_wins = 0
both_won = 0
times = 0
while True:
    answer = input("stone,paper,scissors or quit q:").lower()
    if answer == "q":
        break
    if answer not in options:
        print("unvalued option")
        continue
    
    random_number = random.randint(0,2)
    
    bot = options[random_number]
    print(f"choice of computer: {bot}")
    times += 1
    if answer == "stone" and bot == "scissors":
        print("you won")
        user_wins += 1
    elif answer == bot:
        print("both won")
        both_won += 1
        continue

    elif answer == "scissors" and bot == "paper":
        print("you won")
        user_wins += 1
    
    elif answer == "paper" and bot == "stone":
        print("you won")
        user_wins += 1

    else:
        print("you lost")
        AI_wins += 1 
    

print(f"total {times} times were played")
print("you won ", user_wins," times")
print("computer won ", AI_wins," times")
print("both won ", both_won," times")                


        
        