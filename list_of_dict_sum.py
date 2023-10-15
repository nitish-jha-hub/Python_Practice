list1 = []
a = [{'INFY': 7382.25}, {'HDFCBANK': 4895.4}]
# sum_of_values = sum(d.values() for d in a)
for summ in a:
    x = summ.values()
    y = list(x)
    z = y[0]
    list1.append(z)
print(z, type(y), y, type(z), list1)
xx = sum(list1)
print(xx)


# Get this code by ChatGPT but it is throgh an error dict obj cant use sum function
# a = [{'INFY': 7382.25}, {'HDFCBANK': 4895.4}]
# sum_of_values = sum(d.values() for d in a)
