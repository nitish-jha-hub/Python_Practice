num = [2,7,11,15]
sum = 9
# we have to find the index of those two no whose addition is 9. Q1 leetcode
for i in range(len(num)):
    for j in range(i+1, len(num)):
        if num[i] == sum-num[j] :
            print([i,j],type([i,j]))
        
        