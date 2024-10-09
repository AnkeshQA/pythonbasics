# optimize way to read , write the file
# with open('test.txt', 'r') for reading the file
# with open('test.txt', 'w') for reading the file

# reverse the list
# write the list back to the file

with open('test.txt', 'r') as reader:
    content = reader.readlines() #[cat, dog, apple,car]
    reversed(content) #[cat dog, apple,car]
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)