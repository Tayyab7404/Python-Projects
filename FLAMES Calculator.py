def flames(n1,n2):
    l1 = []
    l2 = []
    
    for i in n1:
        l1.append(i)
        
    for i in n2:
        l2.append(i)
        
    for i in l1:
        for j in l2:
            if i == j:
                l1.remove(i)
                l2.remove(j)
                break
    
    n = len(l1+l2)
    
    F = ["Friends", "Lovers", "Affection", "Marriage", "Enemies", "Siblings"]
 
    while len(F) > 1 :
        Index = (n%len(F) - 1) # reference for slicing the list
        
        if Index >= 0 :
            
            F_right = F[Index + 1 : ] # removing  letter by slicing the list to the right side of the letter
            F_left = F[ : Index] # removing  letter by slicing the list to the left side of the letter
            F = F_right + F_left # swapping the right and left of the list to start counting from the letter next to the deleted letter
            
        else :
            F = F[ : len(F) - 1]

    print("Relationship status :", F[0])

    if F[0] == "Marriage":
        print("Eyy mama.. party!")

    if F[0] == "Enemies":
        print("Daniki konchem dooram ga undu mawa")

n1 = input("Enter your name: ").replace(' ','').upper()
n2 = input("Enter your crush name: ").replace(' ','').upper()

if n1 == n2:
    print("Self love aa?\nInka nuvvu life-long single ra")
    exit(0)

flames(n1,n2)
