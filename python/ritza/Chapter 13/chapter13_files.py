# # 13.2. Writing our first file
# myfile = open('test.txt', 'w')
# myfile.write("My first file written from Python\n")
# myfile.write("---------------------------------\n")
# myfile.write("Hello, world!\n")
# myfile.close()


# # 13.3. Reading a file line-at-a-time
# new_handle = open('test.txt', 'r')
# while True:
#     theline = new_handle.readline()
#     if len(theline) == 0:
#         break

#     print(theline,end='')
# new_handle.close()


# # 13.4. Turning a file into a list of lines
# f = open("friends.txt", "r")        # open file as read function
# xs = f.readlines()                  # read per lines and store in list var
# f.close()                           # close opened read file function

# xs.sort()                           # sorting list 

# g = open("sortedfriends.txt", "w")  # open file as write function
# for v in xs:
#     g.write(v)                      # write value in sorted list one by one 
# g.close()                           # close opened write file function


# # 13.5. Reading the whole file at once
# f = open('test.txt')
# content = f.read()
# f.close()

# words = content.split()
# print("There are {0} words in the file.".format(len(words)))


# 13.9. What about fetching something from the web?
# export request into file
# import urllib.request

# url = "https://www.ietf.org/rfc/rfc793.txt"
# dest_filename = 'rfc793.txt'
# urllib.request.urlretrieve(url, dest_filename)

# read direcly request into strings and print that
import urllib.request

def retrieve_page(url):
    """Retrieve the contents of a web page and convert into a strings"""
    socket = urllib.request.urlopen(url)
    data = str(socket.read())
    socket.close()

    return data

content = retrieve_page("https://www.ietf.org/rfc/rfc793.txt")
print(content)
