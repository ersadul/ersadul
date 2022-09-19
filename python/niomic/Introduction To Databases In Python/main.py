# # Connecting to Database ( 2 )
# from sqlalchemy import create_engine
# from sqlalchemy import inspect
# from sqlalchemy import MetaData, Table

# engine = create_engine('sqlite:///census.sqlite') # make connection to db
# conn = engine.connect() # store obj connection
# insp = inspect(engine) # create obj inspect from engine

# print(insp.get_table_names()) # show existed tabels

# metadata = MetaData()
# census = Table('census', metadata, autoload=True, autoload_with=engine) # make an object tabel
# print(repr(metadata.tables['census'])) # show info detail table


# # Introduction to SQL ( 3 )
# from sqlalchemy import create_engine
# import pandas as pd

# engine = create_engine('sqlite:///census.sqlite')
# conn = engine.connect()

# query = 'SELECT * FROM census' # create a query

# # result proxy: we can use the object that method execute return with many variety of ways
# # , like fetchall(), first(), fetchone(), or you want to iterate the data by your own(using loops)
# result_proxy = conn.execute(query)
# # result set
# result_set = result_proxy.fetchall()
# # simple way to fetch all the data
# # result = conn.execute(query).fetchall() # execute and fetch data

# df = pd.DataFrame(result_set) # convert fetched data into dataframe 
# print(df.head()) # print head


# SQLAlchemy Querying
# import sqlalchemy as db

# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect(engine)
# metadata = db.MetaData()

# census = db.Table('census', metadata
#                  , autoload=True, autoload_with=engine)

# query = db.select([census])
# # # query = db.select([census]).where(census.columns.sex == 'F')
# # # query = db.select([census.columns.state, census.columns.sex]).where(census.columns.sex == 'F')

# result = conn.execute(query).fetchall()
# print(result)


# # Filtering and Targeting Data ( 4 )
# import sqlalchemy as db

# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect(engine)
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Where Clause
# query = db.select([census]).where(
#     census.columns.state == 'California'
# )

# results = conn.execute(query).fetchall()
# for col in results:
#     print(col.state, col.age)

# Expressions
# query = db.select([census]).where(
#     census.columns.state.startswith('New')
# )

# for result in conn.execute(query):
#     print(result.state, result.pop2008)

# Conjunctions
# query = db.select([census]).where(
#     db.or_(census.columns.state == 'California',
#            census.columns.state == 'New York'
#            )
# )
# for result in conn.execute(query):
#     print(result.state, result.sex)


# # Ordering ( 5 )
# import sqlalchemy as db

# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Ordering
# query = db.select([census.columns.state])
# print(conn.execute(query).fetchall()[:10])

# Order by Ascending
# query = db.select([census.columns.state]).order_by(
#     census.columns.state
# )
# print(conn.execute(query).fetchall()[:10])

# Order by Descending
# query = db.select([census.columns.state]).order_by(
#     db.desc(census.columns.state)
# )
# print(conn.execute(query).fetchall()[:10])

# Order by Multiple
# query = db.select([census.columns.state
#                   , census.columns.sex]).order_by(
#                     census.columns.state
#                     , census.columns.sex
#                   )
# print(conn.execute(query).first())


# # Counting, Summing and Grouping Data ( 6 )
# import sqlalchemy as db
# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Sum Example
# query = db.select([db.func.sum(census.columns.pop2008)])
# print(conn.execute(query).scalar())

# SUM - Group by
# query = db.select([census.columns.sex
#                   , db.func.sum(census.columns.pop2008)]
#                   ).group_by(
#                     census.columns.sex
#                   )
# print(conn.execute(query).fetchall())

# SUM - Multiple Group by
# query = db.select([census.columns.sex, census.columns.age
#                   , db.func.sum(census.columns.pop2008)]).group_by(
#                     census.columns.sex, census.columns.age
#                   )
# print(conn.execute(query).fetchall())

# # Use Pandas and Matplotlib to Visualize Data ( 7 )
# # #%% # uncomment this when you wanna show the plot 
# import sqlalchemy as db
# import pandas as pd
# import matplotlib.pyplot as plt

# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# # DataFrame Example

# query = db.select([census.columns.sex, (census.columns.pop2008).label('sum_pop2008')]) \
#     .order_by(census.columns.sex)
# result = conn.execute(query).fetchall()
# # print(result)
# df = pd.DataFrame(result)
# df.columns = result[0].keys()
# # print(df)

# # Graphing
# df[10:20].plot.barh()
# plt.show()

# # Calculating Values in a Query ( 8 )
# import sqlalchemy as db
# from sqlalchemy import case

# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect()
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# # Calculating Difference
# query = db.select([census.columns.age, (census.columns.pop2008 
#     - census.columns.pop2000).label('pop_change')]
#     ).order_by(db.desc('pop_change')).limit(5)

# print(conn.execute(query).fetchall())

# Case Statement
# query = db.select([
#     db.func.sum(
#         case([
#             (census.columns.state == 'New York'
#             , census.columns.pop2008)
#         ], else_=0)
#     )
# ])

# print(conn.execute(query).fetchall())

# Percentage Example
# query = db.select([
#     (
#         db.func.sum(
#             case([
#                 (census.columns.state == 'New York'
#                  , census.columns.pop2008)
#             ], else_=0) 
#         ) / db.cast(db.func.sum(census.columns.pop2008)
#                  , db.Float) * 100
#     ).label('ny_percent')
# ])

# print(conn.execute(query).fetchall())

# # SQL Relationships ( 9 )
# import sqlalchemy as db
# engine = db.create_engine('sqlite:///census.sqlite')
# conn = engine.connect(engine)
# metadata = db.MetaData()
# census = db.Table('census', metadata, autoload=True, autoload_with=engine)
# state_fact = db.Table('state_fact', metadata, autoload=True, autoload_with=engine)

# Automatic Joins - show abbreviation col
# query = db.select([
#     census.columns.pop2008, state_fact.columns.abbreviation
# ])
# print(conn.execute(query).fetchall()[:10])

# Join table
# query = db.select([db.func.sum(census.columns.pop2008)])
# query = query.select_from(census.join(state_fact
#         , state_fact.columns.name == census.columns.state))
# query = query.where(state_fact.columns.circuit_court == '10')
# print(conn.execute(query).scalar())


# # Creating Databases and Tables ( 10 )
# from sqlalchemy import Column, String, Integer, Float, Boolean, Table, insert
# import sqlalchemy as db
# engine = db.create_engine('sqlite:///employees.sqlite')
# metadata = db.MetaData()
# insp = db.inspect(engine)
# conn = engine.connect(engine)

# employees = db.Table('employees', metadata,
#     Column('id', Integer()),
#     Column('name', String(255), unique=True, nullable=False),
#     Column('salary', Float(), default=100),
#     Column('active', Boolean(), default=True),
# )
# metadata.create_all(engine)
# print(insp.get_table_names())
# print(metadata.tables.values())


# # Inserting Data into Table ( 11 )
# from sqlalchemy import Table, insert
# import sqlalchemy as db
# engine = db.create_engine('sqlite:///employees.sqlite')
# metadata = db.MetaData()
# conn = engine.connect(engine)
# employees = db.Table('employees', metadata, autoload=True, autoload_with=engine)

# Inserting One Row
# query = employees.insert().values(id=1, name='Jason', salary=1.00, active=True)
# print(conn.execute(query).rowcount)

# Inserting Multiple Rows
# query = employees.insert()
# val_list = [
#     {'id':2, 'name':'Rebecca', 'salary':2.0, 'active':True},
#     {'id':3, 'name':'Bob', 'salary':0.0, 'active':False}
# ]
# result = conn.execute(query, val_list)
# print(result.rowcount)

# fetch data and show
# query = db.select([employees])
# result = conn.execute(query).fetchall()
# print(*result, sep='\n')

# # Updating Data in Database ( 12 )
# from sqlalchemy import Table, update, desc
# import sqlalchemy as db
# engine = db.create_engine('sqlite:///employees.sqlite')
# metadata = db.MetaData()
# conn = engine.connect(engine)
# employees = db.Table('employees', metadata, autoload=True, autoload_with=engine)

# query = employees.update().where(employees.columns.id == 3) \
#     .values(active=True)
# result = conn.execute(query)
# print(result.rowcount)

# Inserting Multiple Rows
# query = employees.update().where(employees.columns.active == True) \
#     .values(active=False, salary=0.00)
# result = conn.execute(query)
# print(result.rowcount)

# Correlated Updates
# new_salary = db.select([employees.columns.salary]).order_by(
#     desc(employees.columns.salary)).limit(1)
# query = employees.update().values(salary=new_salary)
# result = conn.execute(query)
# print(result.rowcount)


# # Removing Data From Database ( 13 )
# import sqlalchemy as db
# from sqlalchemy import delete
# engine = db.create_engine('sqlite:///employees.sqlite')
# metadata = db.MetaData()
# conn = engine.connect(engine)
# employees = db.Table('employees', metadata, autoload=True, autoload_with=engine)

# delete selected data
# query = employees.delete().where(employees.columns.id == 3)
# result = conn.execute(query)
# print(result.rowcount)

# delete all data from a table
# delete_query = employees.delete()
# result = conn.execute(delete_query)
# print(result.rowcount)

# drop a table
# employees.drop(engine)
# print(employees.exists(engine))

# drop all the tables
# metadata.drop_all(engine)


# # Populating the Database ( 14 )
# Study Case: Populating Database

# Create Database and Table

from sqlalchemy import create_engine, MetaData, Table \
    , Column, Integer, String, insert, select, func

# create engine var
engine = create_engine('sqlite:///demography.sqlite')

conn = engine.connect() # create connection var
metadata = MetaData() # create metadata var

# create schema database
# demography = Table('demography', metadata,
#     Column('kode_bps', String(255), primary_key=True),
#     Column('nama', String(255), nullable=False),
#     Column('ibukota', String(255), nullable=False),
#     Column('populasi', String(255)),
#     Column('luas', String(255)),
#     Column('pulau', String(255), nullable=False)
# )

metadata.create_all(engine) # create database

demography = Table('demography', metadata, autoload=True, autoload_with=engine)
# print(engine.table_names())

# Import demography.csv into List
# import csv
# values_list = []
# with open('demography.csv') as data:
#     next(data)
#     reader = csv.reader(data)
#     for row in reader:
#         data = {'kode_bps':row[0], 'nama':row[1], 'ibukota':row[2]
#         , 'populasi':row[3], 'luas':row[4], 'pulau':row[5]}
#         values_list.append(data)

# print(values_list)

# Import List to Table demography
# query = demography.insert()
# result = conn.execute(query, values_list)
# print(result.rowcount)

# Select Data From Table
# query = demography.select()
# result = conn.execute(query).fetchall()
# print(*result, sep='\n')

# Group by Pulau
query = select([demography.columns.pulau
, func.sum(func.replace(demography.columns.populasi, '.', '')).label('populasi')])
query = query.group_by(demography.columns.pulau).order_by(
    demography.columns.pulau)
result = conn.execute(query).fetchall()
# print(*result, sep='\n')

# Change Results Into DataFrame
import matplotlib.pyplot as plt
import pandas as pd

df = pd.DataFrame(result)
df.columns = result[0].keys()
# print(df)

# Graphing
df.plot(kind='bar', x='pulau', y='populasi')
plt.xlabel('Pulau')
plt.ylabel('Populasi')
plt.title('Total Populasi di Indonesia')
plt.show()