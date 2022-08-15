def flames(n1,n2):
    n1 = n1.replace(' ','').upper()
    n2 = n2.replace(' ','').upper()

    if n1 == n2:
        print("Flames for same names is not valid!")
        exit(0)
    s = ""
    
    for i in n1:
        if i in n2:
                s += i*2
                
    n = len(n1+n2) - len(s)
    
    F = ["Friends", "Lovers", "Attraction", "Marriage", "Enemies", "Siblings"]
 
    while len(F) > 1 :
        Index = n%len(F) - 1 # reference for slicing the list
        
        if Index >= 0 :
            F = F[Index + 1 : ] + F[ : Index]
        else :
            F = F[ : -1]

    print(f"Relationship status : '{F[0]}'")

if __name__ == "__main__":
    n1 = input("Enter your full name: ")
    n2 = input("Enter your crush full name: ")

    flames(n1, n2)
