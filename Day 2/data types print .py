times = int (input ("Tell me the number of times you want to feed the values: ") )     #a user input driven program
all_list = []
for times in range (times):
    int_type = int(input("Enter an integer= "))         
    print ("Your integer number ",int_type) #int type variable
    all_list.append(int_type)
    
    float_type = float(input(" \nEnter a decimal number= "))
    print ("Your decimal number ",float_type)   #float type variable
    all_list.append(float_type)
    
    str_type = str(input("\nEnter any character= "))  #string variable
    all_list.append(str_type)
    
print ("\nLet's make a list of all input data", all_list)   #list variable output    

print ("\nLet's make a new list and convert it into a set and tuple ")
list_type = int (input ("\nEnter length of list: ") )
a = list ()
for j in range (list_type):             #use of for loop
    j = input("Enter list element = ")
    a.append(j)
print ("\nYour list is ",a)         #list type variable
b = set(a)                          #set type variable
c = tuple (a)                       #tuple type variable
print("\nAbove list in the form of set {} \nand in the form of tuple {}" .format(b, c) )  
print ('\nData type check, %s  is  %s  \nand %s is  %s  \nand is %s  %s  ' %(a, type(a), b, type (b),c, type (c)))   # %s formatting and .format formatting 


#Assignment submitted by Krish Sharma
#email: ksysknp@gmail.com
#Day-2 assignment of creating 7 variables with different data types and with %s and {} formatting
