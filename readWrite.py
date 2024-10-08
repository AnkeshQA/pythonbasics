file = open('test.txt')
# read all the content of file using file.read
# for printing all the content of file which they have read use print statement
# read n number of character by passing parameter eg :- file.read(2)
#print(file.read())

# get content line by line at a time readline()
# make note that print(file.read())
print(file.readline())
print(file.readline())


file.close()