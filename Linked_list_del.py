def Output(Listvalue, ListRight, head):
    print(Listvalue[head])
    next = ListRight[head]
    while next > -1:
        print(Listvalue[next])
        next = ListRight[next]

Listvalue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
head = 0
prepos = 3
Output(Listvalue, ListRight, head)
print('*'*50)
ListRight[prepos] = ListRight[ListRight[prepos]]
Output(Listvalue,ListRight,head)

print('*'*50)

def Output(Listvalue, ListRight, head):
    print(Listvalue[head])
    next = ListRight[head]
    while next > -1:
        print(Listvalue[next])
        next = ListRight[next]

Listvalue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]
head = 0
prepos = 5
Output(Listvalue,ListRight,head)
print('*'*50)
ListRight[prepos] = ListRight[ListRight[prepos]]
ListLeft[ListRight[ListRight[head]]] = prepos
Output(Listvalue,ListRight,head)

