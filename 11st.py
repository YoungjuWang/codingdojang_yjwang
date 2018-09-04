l1,l2,l3,result = [],[],[],[]

while True:

        count = 0



        numbers = raw_input()

        if numbers == "0 0": break

        else:

                numbers = numbers.split(" ")

                l1 = [int(x) for x in numbers[0]]

                l2 = [int(x) for x in numbers[1]]

                l3 = [int(x) for x in str(int(numbers[0]) + int(numbers[1]))]



                count = [i for i in range(len(l1)) if l3.pop() < l1.pop()] if int(numbers[0]) > int (numbers[1]) else [i for i in range(len(l1)) if l3.pop() < l2.pop()]

                result.append(count.pop()+1) if count else result.append(0)



for i in range(len(result)):

        print("%s carry operation."% result[i])