string = "Hello World!"
print(string[1])

#Reverse indexing example
print(string[-1])

print(len(string))

#Substring - the right number (the stop number) is up to but not including
print(string[1:4])

#This grabs all the string
print(string[::])

#The number will be the step size. By default it is 1.
print(string[::2])

#This will start at index 2 then step every 2.
print(string[2::2])

#The will start at index 2 and end at 7. It will step every 2.
print(string[2:7:2])