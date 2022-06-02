import random

while True:
    choices = ["R", "P", "S"]
    comp_choice = random.choice(choices)
    user_input = None
    while user_input not in choices :
        user_input = input("\nplease input your choice\n R for rock\n P for paper\n S for scissors\n : ").upper()
        #for good user input
    if user_input in choices :
        if user_input == comp_choice:
            print("It is a tie")
        elif user_input == "R" and comp_choice == "P":
            print("Player (Rock) : Coputer (Paper)")
            print("computer won")
            break
        elif user_input == "R" and comp_choice == "S":
            print("Player (Rock) : Computer (Scissors)")
            print("Player won")
            break
        elif user_input == "P" and comp_choice == "S":
            print("Player (Paper) : Computer (Scissors)")
            print("computer won")
            break
        elif user_input == "P" and comp_choice == "R":
            print("Player (Paper) : Computer (Rock)")
            print("Player won")
            break
        elif user_input == "S" and comp_choice == "R":
            print("Player (Scissors) : Computer (Rock)")
            print("computer won")
            break
        elif user_input == "S" and comp_choice == "P":
            print("Player (Scissors) : Computer (Paper)")
            print("Player won")
            break
#for bad user input
    else :
        print("Error : wrong input,try Again")