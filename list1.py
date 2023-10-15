# list = [i for i in range(11)]
# print(list)

list1 = []
for i in range(101):
    # print(i)
    if i%2 == 0:
        list1.append(i)    # add elements in last of a list
    # else:
    #     list.append(None)
    print(list1,len(list1))  #len(list) to calculate length of a list
print(list1[2])
print("iteration End")
