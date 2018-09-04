l2 = sum(set(range(1,5000))-{sum([int(a) for a in str(x)])+x for x in range(1,5000)})
print(l2)