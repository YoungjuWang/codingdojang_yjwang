str1 = raw_input("input file : ")

f = open(str1,'r')

text=f.read()

print(text)

text2=text.replace("\t"," "*4)

f.close()