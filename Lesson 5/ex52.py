#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. 
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
#  Enter 7, 2, bob, 10, and 4 and match the output below. 


done = True
first_loop = True
largest_number = False
smallest_number = False

while(done) :
    answer = input("Input Number: ")
    try:
        answer = int(answer)
        if answer > largest_number :
            largest_number = answer
        elif answer < smallest_number :
            smallest_number = answer
        else :
            continue 
    except TypeError :
        print("Not a valid Answer")  
        continue  
    except answer == type(str) and answer == str("done") :
        print(f'The largest number is {largest_number}')
        print(f'The smallest number is {smallest_number}')
        break
                



