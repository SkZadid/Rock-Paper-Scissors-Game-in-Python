import random
item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Inter you move = Rock, Paper, Scissor= ")
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

if user_choice == comp_choice:
    print("Both chooses same: = match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper cover Rock = Compuer Win")
    else:
        print("Rock smashes scissor = You win")

elif user_choice == "Paper":
    if comp_choice == "Rock":
        print("Paper cover rock = You win")
    else:
        print("Scissor cut paper = Compuer win")
elif user_choice == "Scissor":
    if comp_choice == "Rock":
        print("Rock smashes scissor = Computer win")
    else:
        print("Scissor cuts paper = You win")
        
