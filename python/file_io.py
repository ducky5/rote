
# READING FROM FILES

# open file in reading mode
data_file = open('data/file.txt', 'r')
# check if file is readable: true/false
print(data_file.readable(), end="\n\n")
# read file
print(data_file.read(), end="\n\n")
# close file
data_file.close()

# another file
data_file = open('data/file.txt', 'r')
# read first line from file
print(data_file.readline())
# return array of lines
print(data_file.readlines()[0])

# close file
data_file.close()

# WRITING TO FILES
# if file does not exist it will be created

# open file in append mode
data_file = open('data/file.txt', 'a')
# write to file in append mode
data_file.write("\nkangaroo")
# close file
data_file.close()

# open file in write mode
data_file = open('data/file2.txt', 'w')
# overwrite file
data_file.write("Hello there")
# close file
data_file.close()
