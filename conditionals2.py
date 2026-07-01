# If elif else ladder

a = int(input("Enter your age :"))

if(a>18):
    print("You are eligible to vote")
    print("Good for you!")
    
elif(a<0):
    print("Invalid age")
    
elif(a==0):
    print("You are not born yet")
   
else:
    print("You are not eligible to vote") 

print("End of Program")