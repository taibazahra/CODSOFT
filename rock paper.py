import random
word = "ROCK", "PAPER", "SCISSOR"
words = random.choice(word)

choice = input("Enter ROCK, PAPER OR SCISSOR\n")
print(choice)
print(words)
if words=="ROCK" and choice=="PAPER":
    print("Computer wins: ")

elif words=="SCISSOR" and choice=="PAPER":
    print("Computer wins: ")

elif words=="ROCK" and choice=="SCISSOR":
    print("Computer wins: ")     

elif words=="PAPER" and choice=="SCISSOR":
    print("User wins: ")

elif words=="SCISSOR" and choice=="ROCK":
    print("Uer wins: ")

elif words=="PAPER" and choice=="ROCK":
    print("USer wins: ")    

else:
    print("TIE")