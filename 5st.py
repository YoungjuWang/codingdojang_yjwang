num = int(input("input number : "))

sum = 0



for i in range(num):

        if i == 0:

                continue

        if i%3==0 or i%5==0:

                sum = sum+i

print(sum)