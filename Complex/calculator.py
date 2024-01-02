import re

print("Our Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True

allowed_chars = set('0123456789+-*/().')  # Define allowed characters for arithmetic operations


def cleanEquation(equation): #filters characters that are not in the variable 'allowed_chars'
    return ''.join(filter(lambda x: x in allowed_chars, equation))


def performMath():
    global run
    global previous
    equation =""
    if previous == 0:
        equation = input("Enter equation:")
    else:
        equation = input(str(previous))
    
    try:
        
        if equation == 'quit':
            run = False
            print("good bye human")
        else:
            cleaned_equation = cleanEquation(equation)
            
            # Check if there are valid characters before attempting evaluation
            if cleaned_equation:
               
                    # Evaluate the cleaned equation
                    if previous == 0:
                        previous = eval(cleaned_equation)
                    else:
                        previous = eval(str(previous)+ equation)
                    
            else:
                print("Invalid input for calculation.")
    
    except Exception as e:
        if equation == '':
            print("No input received.")
        else:
            print("Error:", e)
        # Additional error handling or logging can be added based on specific needs
    

while run:
    performMath()


