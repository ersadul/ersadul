# # Importing Text Files ( 1 )
# r = read file
# file = open('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/lorem-ipsum.txt', mode='r')
# teks = file.read()
# file.close()
# print(teks)

# with open('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/lorem-ipsum.txt', mode='r') as file:
#     print(file.read())


# # Importing Flat Files using NumPy ( 3 )
# import numpy as np
# data = np.loadtxt('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/mnist.txt')
# print(data)

# # Importing Flat Files using Pandas ( 4 )
# import pandas as pd
# data = pd.read_csv('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/data-kategori-event-jakarta-perbulan-tahun-2019.csv')
# print(data.head())


# # Introduction to Other File Types ( 5 )
# pickle extension
# import pickle
# with open('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/contoh.pickle', 'rb') as file:
#     data = pickle.load(file)
# print(data)

# xlsx extension
# import pandas as pd
# data = pd.ExcelFile('D:/learning and code/python/niomic/Importing Data In Python (Part 1)/contoh.xlsx')
# print(data.sheet_names)


# # Creating a Database Engine ( 9 )
# from sqlalchemy import create_engine
# from sqlalchemy import inspect
# engine = create_engine('sqlite:///Northwind_small.sqlite')
# insp = inspect(engine)
# print(insp.get_table_names())


# # Querying Relational Database in Python ( 10 )
# optional way 1
# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine('sqlite:///Northwind_small.sqlite')

# conn = engine.connect()
# query = conn.execute('SELECT * FROM Customer')
# df = pd.DataFrame(query.fetchall())
# df.columns = query.keys()
# conn.close()

# print(df)

# optional way 2 using context manager
# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine('sqlite:///Northwind_small.sqlite')
# with engine.connect() as conn:
#     query = conn.execute('SELECT CompanyName, Phone FROM Customer')
#     df = pd.DataFrame(query.fetchmany(size=3))
#     df.columns = query.keys()

# print(df)


# # Querying Relational Database Directly With Pandas ( 11 )
# simpled version
# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine('sqlite:///Northwind_small.sqlite')

# df = pd.read_sql_query('SELECT * FROM Customer', engine)
# print(df)


# # Advanced Querying: Exploiting Table Relationship ( 12 )
from sqlalchemy import create_engine
import pandas as pd

engine = create_engine('sqlite:///Northwind.db')

df = pd.read_sql_query(
    'SELECT OrderID, CompanyName FROM Orders INNER JOIN Customers on Orders.CustomerID = Customers.CustomerID'
    , engine)

print(df.head())