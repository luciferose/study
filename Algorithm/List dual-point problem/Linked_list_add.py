def Output(ListValue,ListRight,head):
    print(ListValue[head])
    next = ListRight[head]
    while next != -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 5

Output(Listvalue,ListRight,head)

print('*'*50)

Listvalue.append(4)
ListRight.append(ListRight[prepos])
ListRight[prepos] = len(Listvalue)-1

Output(ListValue,ListRight,head)
