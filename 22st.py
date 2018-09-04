li = [1,3,4,8,13,17,20]

l2 = [(li[x+1]-li[x],[li[x],li[x+1]]) for x in range(len(li)-1)]

mina = [l2[x][1] for x in range(len(l2)) if l2[x] == min(l2)]

print(mina)