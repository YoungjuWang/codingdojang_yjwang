# 3n+1 Problem

str1 = input()
str1 = str1.split(" ")

nums = [int(x) for x in str1]
count_list = []

for i in range(nums[0],(nums[1]+1)):
    count = 1
    while i != 1:
        i=i/2 if i%2==0 else i*3+1
        count += 1
    count_list.append(count)

maxNum = max(count_list)

print("%s %s %s"% (nums[0],nums[1],maxNum))
