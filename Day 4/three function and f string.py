# write 3 functionS ..1 fun should take all variable set, list, tuple, diction
# make dic age name bla bla use for loop to print key and value
# take 2 no. as argument a and b and take them as a list


def transform (a):              #a function to transform variable list set tuple
    print ("Let's make a list")
    ele = int (input("Tell no. of elements you'll put: "))
    for i in range (ele):
        i = str(input("Input data: "))
        a.append(i)
    print (f"\nGiven data in the form list: \n{a} \nClass type = {type(a)} \
        \n\nYour data as set: \n{set(a)} \nClass type = {type(set(a))} \
        \n\nAnd as tuple: \n{tuple(a)} \nClass type = {type(tuple(a))} ")
    return a


def dict1 ():                   #a function to create dictionary and print  its keys and values
    print ("\nCreating a dictionary!")
    eled  = int (input("Number of key to be defined: "))
    for p in range (eled):
        q = input("Enter key name: ")
        r = input ("Enter it's value: ")
        d.update({q:r})
    print (f"\nThe dictionary is: {d} \n \
    Which has following \n Index       Key            Value ")
    for index, (key, value) in enumerate(d.items()):    #use of enumerate taughtin Day4lecture
        print(index, key, value, sep = '            ')
    print("\n")
    return d



def list_operations(full):              #2 no. as argument a and b and take them as a list
    newList = full
    print (f"\nGiven numbers in a list: {newList} \n\
        Some actions on the list.... \n\
        Sum of list= {sum(newList)} \n\
        Minimum value in list = {min(newList)}" )
    return full

a =[]
d = {}
transform(a)
dict1()

print  ("\nCreating a list and applying some operations in  \n\ two variable integer arguments.")
num1 = int (input("Enter a number: "))
num2 = int (input("Enter a number: "))
full = [num1, num2]

list_operations(full)
print ("\nThank You Sir! \nDay-2 Assignment from Krish Sharma, email: ksysknp@gmail.com")