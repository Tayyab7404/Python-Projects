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
    
    l = l1+l2
    
    n = len(l)
    
    f = ["Friends", "Love", "Affection", "Marriage", "Enemy", "Siblings"]
 
    while len(f) > 1 :
        Index = (n%len(f) - 1) # reference for slicing the list
        
        if Index >= 0 :
            
            f_right = f[Index + 1 : ] # removing  letter by slicing the list to the right side of the letter
            f_left = f[ : Index] # removing  letter by slicing the list to the left side of the letter
            f = f_right + f_left # swapping the right and left of the list to start counting from the letter next to the deleted letter
            
        else :
            f = f[ : len(f) - 1]

    print("Relationship status :", f[0])

n1 = input("Enter your name: ").replace(' ','').upper()
n2 = input("Enter your crush name: ").replace(' ','').upper()

flames(n1,n2)
