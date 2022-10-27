#Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below. 
# Convert the extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence: 0.8475"

beginnum = text.find(" ")
strlength = len(text)

value = text[beginnum:strlength]
value = float(value)
print(value)
