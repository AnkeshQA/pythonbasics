values = [1, 2, "list", 4.5]
# list is a data type that allow multiple value and can be different data types

print(values[0]) # 1

#print last value

print(values[-1])

#print sub values
#here it works like range fucntion where starting is included and end is not included

print(values[1:3])

#insert value in list in between
values.insert(3,"demo") #[1, 2, 'List', 'demo', 4.5, 'End']
print(values)

#adding new variable in the end
values.append("End")  #[1, 2, 'list', 'demo', 4.5, 'End']
print(values)

#updating value at any index
values[2] = "LIST"
print(values) #[1, 2, 'LIST', 'demo', 4.5, 'End']

#deleting the values
del values[0]
print(values) #[2, 'LIST', 'demo', 4.5, 'End']