name = input("What is your name?")
print(f"Hi {name}")
import random
my_list = ['True', 'False', 'You will find what you seek', 'Your life is a lie']

while True:
    n = input("What do you have to ask the Magic 8-Ball?, Say THANKS if you wish to leave.")
    answer = random.choice(my_list)
    print("The Magic 8-Ball says... %s" %answer)
    if n.strip() == "THANKS":
        break

