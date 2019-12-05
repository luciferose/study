def Output(ListValue, ListRight, head):
    print(ListValue[head])
    next = ListRight[head]
    while next > -1:
        print(ListValue[next])
        next = ListRight[next]

ListValue = [1, 5, 6, 2, 7, 3]
ListRight = [3, 2, 4, 5, -1, 1]
ListLeft = [-1, 5, 1, 0, 2, 3]
headright = ListLeft.index(-1)
headleft= ListRight.index(-1)
perpos = 5
Output(ListValue, ListRight, headright)
print('*'*50)
Output(ListValue, ListLeft, headleft)
print('*'*50)

ListValue.append(4)
ListRight.append(ListRight[perpos])
ListLeft.append(perpos)
ListLeft[ListRight[perpos]] = len(ListValue)-1
ListRight[perpos] = len(ListValue)-1

Output(ListValue, ListRight, headright)
print('*'*50)
Output(ListValue,ListLeft,headleft)

