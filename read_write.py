# Open the file and store the file object in a variable
file = open('test.txt')

# Read the content of the file

# Print the content of the file
#print(file.read(2))

# read & print one single line
#print(file.readline())
#print(file.readline())
# Close the file after reading


# print line by line using read line method
#line = file.readline()
#while line!= "":
 #   print(line)
  #  line = file.readline()
for line in file.readlines():
    print(line)

file.close()