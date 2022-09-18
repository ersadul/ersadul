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
import sqlalchemy as db
from sqlalchemy import case

engine = db.create_engine('sqlite:///census.sqlite')
conn = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

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
