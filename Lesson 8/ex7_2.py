#Write a program that prompts for a file name, then opens that file and reads through the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

# Use the file name mbox-short.txt as the file name
average = 0
amountfordivide = 0
totalvalue = 0
fname = input("Enter file name: ")
fh = open(fname)
for line in fh:
    line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    #print(line)
    value = float(line[20:])  
    totalvalue += (value)
    amountfordivide += 1
    #print(f'The value is {value}')
    #print(f'The amount to divide by is {amountfordivide}')
    #print(value / amountfordivide)
    
average = totalvalue / amountfordivide
print(f'Average spam confidence: {average}')
#print("Done")
