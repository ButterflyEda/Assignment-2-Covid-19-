age = input("Are you cigarette addict older than 75 years old? y/n ") == "Yes"  

chronic = input("Do you have a server chronic disease? y/n ") == "Yes" 

immune = input("Is your immune system too weak? y/n ") == "Yes"          

if age:
    print("You are in risky group")

elif chronic:
    print("You are in risky group")
    
elif immune:
    print("You are in risky group")
    
else:
    print("You are not in riskygroup")
    
