import random

def game(comp, you):
   if comp == you:
       return None
   elif comp == "s":
       if you == "w":
           return False
       elif you == "g":
           return True
   elif comp == "w":
       if you == "g":
           return False
       elif you == "s":
           return True
   elif comp == "g":
       if you == "s":
           return False
       elif you == "w":
           return True              
   
print("Comp turn: snake(s), water(w), gun(g)")  
randno = random.randint(1, 3)
print(randno)
if randno == 1:
    comp = "s"
elif randno == 2:
    comp = "w"
elif randno == 3:
    comp = "g"    
you = input("Your turn: snake(s), water(w), gun(g) ")
a = game(comp, you)

if a is None:
    print("The round is Tie")
elif a:
    print("You won the round")
else:
    print("Computer won the round")

