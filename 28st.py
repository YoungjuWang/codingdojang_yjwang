l1= input("input list : ")

l1 = list(l1)



l2 = [i for i in l1 if i < 0] + [i for i in l1 if i > 0]

print(l2)