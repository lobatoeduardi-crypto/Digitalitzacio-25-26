list_num = [6,9,6,9]
print(list_num)

for i in range(0,len(list_num)):
    duplicat=False
    for j in range(len(i+1,len(list_num))):
        if list_num[i]==list_num[j]:
            duplicat=True
    if duplicat:
        list_num.pop(i)

print(list_num)