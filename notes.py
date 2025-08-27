def whatType(userInput):
    print(type(userInput))
# def defines a function, what type is the name of the function
#user input s the parameter of the function
#print and type are python built in functions tat finds the datatype 
#call the function with different user inputs 
#the pund sybol is for one line comments, the program ignores comments 
"""
multi line comments 
"""

#call the function with different data types
whatType(3)
whatType(3.0)
whatType(True)
whatType("Allison")
whatType('p')
#this is a test to see if this works, I have already commited this but I am trying to commit this to save it
#create a variable named message
message = """this is a 
multiline message
to my bestie"""
# the equal assigns variables 
print(message)

#test input to print and see how they print 
print(42000)
print(42.000) # this prints 42.0 because it rounds
print (42,000) #this prints 42 0 this is because it views 40 as a different paramater output so, 
print (42, "Allison", 3, 4.0) #prints 42 Allison 3 4.0

#print 42 is a syntax error 



#8/25 class - variables and data




name = "AllisonZ" 
newName = "Allison"
name = newName 
newName = name
#both of these should be allison 
print(name)
print(newName)
#if something says number=30, that dosent mean that number is assigned 30, it means 30 is assigned to number
# you can simmilaraly assign lists to variables  
classOf2026 = ["student 1", "student 2", "student 3", "student 4"]
#for this case, naming this class of 2026 would be better than naming it seniors 

#MLA formating for geeks 
#normally global variables are assigned to things that dont changes
#global variables are uppercase
#in naming variables, day does not equal DAY
#we want to use lowercase as much as possible
#use underscore or capitalizing first letter instead of spaces
JANUARY = "January"


"""illigal variable names 
21yearsold = "party"
dolla$$$ = whatever
class = "anything"""

"""True, False, and None are the only uppercase keywords
there are a couple other keywords that mean things so variables (and im assuming functions) cannot be named them"""
#dont confuse meaningful to the human and computer reader
#just because something is called something, dosent mean that it is actually performing a function


#8/25 continues   -   statements 


"""some examples of statements include
while - looping
for - finite looping
if- conditional statement
import - because everything is open source, you can get code from other codes 
"""

"""
an expression is a combination of values, variables, operators, and functions 
some examples include:
print (2+2)
print(len("hello"))"""

hour = 1
threeHour = hour*60*3
print(hour*60, "60 minutes in one hour")
print(threeHour)


#str is casting the integer data type to a string so you can concatenate (add) two strings together
#they must be the same type of data
#with strings you can only add and multiply 

"""opperations
addition - add numbers or concatinate string
subtraction - to numbers only 
division - to numbers only 
-/-  division  - returns a float
-//- floor division returns an int
-%- modulous operator returns an int. 
multiplication - for numbers and strings 
-*- multiplication
-**- exponential
order of opperations applies
"""
print (10/3) #3.333
print(10//3) #3
print(10%3) #1



"""convertter functions 
(int, float, string)
print(int(3.14)) #3
print(int(pi))  #error
print(int("1778")) #1778
print(int("Allison")) #error
print(int(-13)) #-13
print(int(-4.999999999)) returns -4

print(str(3.0))
print(str(1778))
"""