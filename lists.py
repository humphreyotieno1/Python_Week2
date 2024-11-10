my_list = []
my_list.extend([10, 20, 30, 40])
my_list.insert(2, 15)
del my_list[-1]
my_list.sort()
print(my_list.index(30))
print(my_list)