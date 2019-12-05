ListValue = [1,5,6,2,7,3]
ListRight = [3,2,4,5,-1,1]
ListLeft = [-1,5,1,0,2,3]
head = ListLeft.index(-1)
print(ListValue[head])
Next = ListRight[head]
while Next > -1:
    print(ListValue[Next])
    Next = ListRight[Next]
print('*'*50)
head = ListRight.index(-1)
print(ListValue[head])
Next = ListLeft[head]
while Next > -1:
    print(ListValue[Next])
    Next = ListLeft[Next]
print('*'*50)

value = 0
left = 2
right = 1
LinkedList = [ [1, 3, -1], [5, 2, 5], [6, 4, 1], [2, 5, 0], [7, -1, 2], [3, 1, 3]]
head=0
print(LinkedList[head][value])
Next = LinkedList[head][right]
while Next > -1:
    print(LinkedList[Next][value])
    Next = LinkedList[Next][right]
print('*'*50)
head=-2
print(LinkedList[head][value])
Next = LinkedList[head][left]
while Next > -1:
    print(LinkedList[Next][value])
    Next = LinkedList[Next][left]