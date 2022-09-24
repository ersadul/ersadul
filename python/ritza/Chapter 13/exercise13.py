# # 1. Write a program that reads a file and writes out a new file with the lines in reversed order (i.e. the
# first line in the old file becomes the last one in the new file.)

# with open('exercise1.txt', 'w') as file:
#     text = 'this is line number'
#     for i in range(1, 11):
#         file.write(text +" "+ str(i)+'\n')

# words = []
# with open('exercise1.txt', 'r') as file:
#     for word in file:
#         words.append(word)
#     words.reverse()

# with open('exercise1_reversed.txt', 'w') as file:
#     for word in words:
#         file.write(word)


# # 2. Write a program that reads a file and prints only those lines that contain the substring snake
# with open('snakes.txt', 'r') as file:
#     for line in file:
#         if 'snake' in line:
#             print(line)


# 3. Write a program that reads a text file and produces an output file which is a copy of the file, except
# the first five columns of each line contain a four digit line number, followed by a space. Start
# numbering the first line in the output file at 1. Ensure that every line number is formatted to the
# same width in the output file. Use one of your Python programs as test data for this exercise: your
# output should be a printed and numbered listing of the Python program.

# 0001 

with open('snakes.txt', 'r') as file:
    with open('snakes_edited.txt', 'w') as output_file:
        tmplt = '000'
        for i, line in enumerate(file):
            if i < 5:
                output_file.writelines(tmplt + str(i+1)+' '+line)
            else:
                output_file.writelines(line)



# 4. Write a program that undoes the numbering of the previous exercise: it should read a file with
# numbered lines and produce another file without line numbers.

with open('snakes_edited.txt', 'r') as file:
    with open('snakes_edited_without_numbering.txt', 'w') as output_file:
        tmplt = '000'
        for i, line in enumerate(file):
            if tmplt+str(i+1) in line:
                output_file.writelines(line[5:])
            else:
                output_file.writelines(line)
