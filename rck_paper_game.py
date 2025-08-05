import random           
item_list = ["Rock", "Paper", "Scissor"]  
user_choice = input("Enter your move = Rock, Paper, Scissor = ")   
comp_choice = random.choice(item_list)         

print(f"User Choice = {user_choice} , Computer Choice = {comp_choice}")

if user_choice==comp_choice:
    print("Both Chooses same: Match ties")

elif user_choice == "Rock":
    if comp_choice == "Paper":
      print("Paper covers Rock = Computer wins")
    else:
       print("Rock smaches Scissors = You win")

elif user_choice == "Paper":
   if comp_choice == "Scissor":
      print("Scissor cuts Paper , Computer wins")
   else:
      print("Paper covers Rock , You win")

elif user_choice == "Scissor":
   if comp_choice == "Paper":
      print("Scissor cuts Paper , You win")
   else:
      print("Rock breaks Scissor, Computer win") 
else:
   print ("The Given Choice is not possible to execute")  
    
    