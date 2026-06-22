helpimport random

computer = random.choice([-1, 0, 1])
youstr = input("Enter your choices: " )
youDict = {"S": 1, "W": -1, "G" : 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\n Computer chose: {reverseDict[computer]}")

# By now we have 2 numbers,you and computer 

if (computer == you):
    print("IT'S A TIE!")
else:
 if(computer ==-1 and you ==1):
    print("YOU WIN!")
 elif(computer ==-1 and you ==0):
    print("YOU LOSE!")    
 elif(computer ==1 and you ==-1):
    print("YOU LOSE!")
 elif(computer ==1 and you ==0):
    print("YOU WIN!")
 elif(computer ==1 and you ==-1):
    print("YOU WIN!")
 elif(computer ==0 and you ==-1):
    print("YOU LOSE!")  

 else:
    print("SOMETHING WENT WRONG!")
