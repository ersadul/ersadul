def read_large_file(file_object):
    """A generator function to read a large file"""

    while True:
        # read a line from the file
        data = file_object.readline()

        # break if this the end of the file
        if not data:
            break

        # yield data of the line
        yield data

# initiate an empty dict
counts_dict = {}

# open a connection to the file
with open('D:/learning and code/python/niomic/Python Data Science Toolbox/world_dev_ind.csv') as file:

    for line in read_large_file(file):

        row = line.split(',')
        first_col = row[0]

        if first_col in counts_dict.keys():
            counts_dict[first_col] += 1
        else:
            counts_dict[first_col] = 1

print(counts_dict)


    
