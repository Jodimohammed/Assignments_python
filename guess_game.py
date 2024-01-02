#Python guess game 

secret_num = 4

for i in range(4):
    guess = int(input("guess a number :"))

    if guess == secret_num :
        print("Hooray you won!")
        break
    
    else:
        print("sorry you failed! try again ")
