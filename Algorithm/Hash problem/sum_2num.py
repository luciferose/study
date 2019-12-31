import time
num = [4,5,3,7,10]

#遍历
start = time.time()
for x in num:
    for y in num:
        if x+y == 11:
            print(num.index(x)+1,num.index(y)+1)
stop=time.time()
print(stop-start)

print('*'*50)

#双指针
start1=time.time()
def twoSum(numbers, target):
    res = []
    newnumbers=numbers[:]
    newnumbers.sort()
    left=0
    right=len(numbers)-1
    while right > left:
        if newnumbers[left] + newnumbers[right] == target:
            for i in range(0,len(numbers)):
                if numbers[i] == newnumbers[left]:
                    res.append(i)
                    break
            for i in range(len(numbers)-1,-1,-1):
                if numbers[i] == newnumbers[right]:
                    res.append(i)
                    break
            res.sort()
            break
        elif newnumbers[left] + newnumbers[right] < target:
            left = left + 1
        elif newnumbers[left] + newnumbers[right] > target:
            right = right - 1
    return (res[0]+1,res[1]+1)
print(twoSum(numbers=num, target=11))
stop1=time.time()
print(stop1-start1)

print('*'*50)

#hash
start2=time.time()
def twoSum2(numbers, target):
    dict = {}
    for i in range(len(numbers)):
        m = numbers[i]
        if target - m in dict:
            return (dict[target-m]+1,i+1)
        dict[m] = i
print(twoSum2(num,11))
stop2=time.time()
print(stop2-stop1)