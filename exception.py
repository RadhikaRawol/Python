try:
     a = int(input("hii, enter a number:"))     
     print(a)

except ValueError as v: 
    print("hii") 
    print(v)
    
       
except Exception as e:
    print(e) 
    
    print("Thank You")    