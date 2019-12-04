numbers=list(range(10000))
head,tail = 0,len(numbers)
search=9999
while tail-head>1:
    mid = (head+tail)//2
    if search<numbers[mid]:
        tail=mid
    if search>numbers[mid]:
        head=mid+1
    if search==numbers[mid]:
        ans=mid
else:
    if search==numbers[head]:
        ans=head
    else:
        ans=-1
print(ans)