##################################################
#       Ch9project
#       Jayant Dharwadkar
#       2/11/2021   
#       Description: Write a program in the language of your choice to implement the sequential search algorithm of Chapter 3, Figure 3.1, except that instead of searching a list of telephone numbers for a particular number, have the program search a list of integers for a particular integer. Use the same input mechanism as in the data cleanup programs of Section 9.3.2 to get the list of integers to be searched. Then get the target number to be searched for. 
#       inputs: the values in the list, the values you want to search for in the list.
#       outputs: “Successful search, the value is in the list”, "Unsuccessful search, the value is not in the list."
#       Dependancies: python input, print codes, and user inputs
##################################################

n = int(input("How many numbers are in the list: ")) #Asks the user to determine the length of the list
varlist = []  #creates an empty list for user to fill in

i = 0 #Define a counter and set the initial value to 0
num = int(input("Enter the first number: ")) #asks user for number
varlist.append(num) #appends the value entered by the user to the list

#This block of code builds the list of numbers as determined by the user in n
while i < n - 1:
    n -= 1   #Decrementing n in each pass. Another approach could be to increment the counter. Both approaches result in same output.
    num = int(input("Enter the next number: "))
    varlist.append(num) #If the user says the list is more than 1 integer, the program will ask for numbers until it reaches the initial value 

var_num = int(input("What number do you want to search for? "))         #asks user to specify what integer they want to search for

######################## Start of alternate code block ################
# The following block of code is more efficient in getting the same result. It declares less variables and has less logic to evaluate. Instead it uses built in keywords in Python "in" to check for presence of a number in a list.

#if var_num in varlist:     # implementing the condition to test the membership of a number in a list of numbers.
#    print("Successful search, the value is in the list")
    #print("The list of numbers is:", varlist)
#else:
#    print("Unsuccessful search, the value is not in the list")
    #print("The list of numbers is:", varlist)
######################## End of alternate code block ################


# The following code block follows the algorithm provided in Chapter 3 figure 3.1 and provides the same result with more logic and code. Here we are implementing the functionality of the Python keyword "in" within the while loop.
Found = False
j = 0   # initializing another counter for second while loop

while (Found == False) and (j <= n):        #While Found is still false and the counter is less the length of the list
    if varlist[j] == var_num:
        print("Successful search, the value is in the list")
        Found = True
    else:
        j += 1 #if the entered number matches with something on the list, the program returns this

if Found == False:
    print("Unsuccessful search, the value is not in the list")
    #if the entered number does not match with something on the list, the program returns this
