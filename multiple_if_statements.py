
a = int(input("Enter your age :"))

# if statement no.1
if(a%2==0):
    print("Even number")
    
# if statenment no.2    
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