print ("A small survey project!\n \
Approx. time 2 minutes to fill survey. ")       #A short survey program
                                                # I used if elif else , def and f string for program
name = str (input ("Name: "))
ph_nbr = int (input("Enter mobile number (without country code): "))
ct = str (input("City/Town name: "))
cnt = str (input ("Country: "))
ag = int (input ("Enter your age: "))

def prt():
   p_nm = str (input ("Your father's name: "))
   m_nm = str (input ("Your mother's name: "))
   fam = str (input ("Total  family members: "))
   adr = str (input ("Share your full address: "))
   sibl = str (input ("Do you have any sibilings? "))
   return (p_nm, m_nm, fam, sibl, adr)

if (12 < ag <= 18) :
    print ("You are a minor.")
    ans = str (input("You take full concern for survey? Type ' Y ' for yes and ' N ' for No... ") )
    
    if (ans == "Y" or 'y') :
        print ("You're eligible.\n")
        std = str (input("Are you a student? "))
        prt() 
        qlf = str (input ("Enter your qualification:  "))
        sprt = str (input ("Which sports do you love most? "))     
    else: 
        print ("See you another time!")

elif (18< ag <= 50) : 
    print ("You're eligible!")
    prt()
    mst = str (input ("Marital status: "))
    qlf = str (input ("Enter your qualification:  "))
    jbst = str (input ("Are you employed? Say yes or no. "))
    jbex = str (input ("Your job experience in years: "))
    pcd = int (input ("Enter your area pincode: "))
    
else :
    print ("You're not eligible for the survey. \n \
     Thank you for your time! Have a nice day. ")

print (f"\nThanks for sharing your information with us {name}. \n\
       You'll further recieve updated on {ph_nbr} \
       We'll be opening new branch in {ct} soon. \n Till then have a great day ahead!")     #f string

#Day-3 Assignment by Krish Sharma
# email - ksysknp@gmail.com
#To take user values and use data to print some output using f string 