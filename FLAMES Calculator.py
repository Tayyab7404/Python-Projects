def flames(n1,n2):
    for i in n1:
        if i in n2:
                n1.replace(i,"",1)
                n2.replace(i,"",1)
                
    n = len(n1+n2)
    
    F = ["Friends", "Lovers", "Attraction", "Marriage", "Enemies", "Siblings"]
 
    while len(F) > 1 :
        Index = (n%len(F) - 1) # reference for slicing the list
        
        if Index >= 0 :
            F = F[Index + 1 : ] + F[ : Index]
        else :
            F = F[ : -1]

    print(f"Relationship status : '{F[0]}'")

n1 = input("Enter your name: ").replace(' ','').upper()
n2 = input("Enter your crush name: ").replace(' ','').upper()

if n1 == n2:
    print("Flames on same names is not applicable")
    exit(0)

flames(n1,n2)
