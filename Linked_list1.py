ListValue = [1,5,6,2,4,3]
ListPointer = [3,2,-1,5,1,4]
head = 0
print(ListValue[head])
next = ListPointer[head]
while next != -1:
    print(ListValue[next])
    next= ListPointer[next]

print('*'*50)

value = 0
pointer = 1
LinkedList=[ [1,3], [5,2], [6,-1], [2,5], [4,1], [3,4]]
head = 0
print(LinkedList[head][value])
next = LinkedList[head][pointer]
while next != -1:
    print(LinkedList[next][value])
    next = LinkedList[next][pointer]