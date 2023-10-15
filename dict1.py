dic = {"Name" : 'Nitish', 'age' : 28, 38 : 'Shayam'}
print(dic[38])

print(dic['Name']) 

b = dic.get('Name')
print(b)
c = dic.get('Name2')   # get method will return none if key is not present but dict['key'] will through an error
print(c)

d = dic.keys()     # return an array of all keys in given dict
print(d)
print(type(d))

e = dic.values()   # return an array of all values
print(e)
print(type(e))

# For loop for dictionary
for key in dic.keys():
    print(f'key is {key} and value corresponding to key is {dic[key]}')


