#python program to print out a pyramid pattern   based on a given height...

Height = int(input("Please enter the Height of ŧhe pyramid: "))

for i in range(1, Height+1):
    print(" "* ((Height+1)-i), end="")
    
    for j in range(1,i+1):
        print("*",end=" ")
        
    print('\r')
    
for k in range(Height,1,-1):
    print(" "*((Height+2)-k),end="")
    
    for m in range(k,1,-1):
        print('*',end=" ")
        
    print("\r")