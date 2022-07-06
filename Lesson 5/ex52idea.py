#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below. 


done = True

def numbercheck() :
    answer = input("Enter Number: ")
    try:
        while(done) :
            answer = input("Enter Number: ")        
            if answer == type(int):
                if answer > largest_number :
                    largest_number = answer
                elif answer < smallest_number :
                    smallest_number = answer
                numbercheck()
            elif answer == str("done"):
                print(largest_number)
                print(smallest_number)
                break
    except TypeError :
         print("Not a valid answer")
numbercheck()          


"""
if answer == type(int) :
    largest_number = answer
    smallest_number = answer
else:
    print("Not a valid Answer")
    ###
"""