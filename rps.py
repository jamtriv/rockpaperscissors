import random  #imports random for rps

def playrps ():
    number = random.randint (0,2) #chooses random number between 0 and 2
    list = ["rock", "paper", "scissors"] #shows a list of variables to the computer
    computer = list [number] #computer chooses a varible
    player = input("Rock, Paper or Scissors?").lower() #player chooses variable
    if player == computer: #if the player and computer
        print("Draw! This is what the computer played!", computer) #print custom code
        exit()
    if player == "rock" and computer == "paper": #if the player chooses rock and the computer paper
        print("You lose! This is what the computer played!", computer) #prints custom text
        exit()
    if player == "rock" and computer == "scissors": #if the player chooses rock and the computer scissors
        print("You Win! This is what the computer played!", computer) # prints custom text
        exit()
    if player == "scissors" and computer == "paper": #if they player chooses Scissors and the computer Paper
        print("You Win! This is what the computer played!", computer) #prints custom code
        exit()
    if player == "scissors" and computer == "rock": #if player chooses Scissors and computer Rock
        print("You lose! This is what the computer played!", computer) #prints custom text
        exit()
    if player == "paper" and computer == "scissors": #If player chooses paper and the computer Scissors
        print("You lose! This is what the computer played!", computer) #print custom text
        exit()
    if player == "paper" and computer == "rock": #if player chooses Paper and computer rock
        print("You Win! This is what the computer played!", computer) #prints custom code
        exit()
    else:
        print("Please enter a valid move!") #prints custom code
        playrps()


hi = input ("Hello, what is your name?") #asks for name
print("Hi", hi) #prints name
playrps()

print ("Test")
#print yeet