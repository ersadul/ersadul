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
import sqlalchemy as db

engine = db.create_engine('sqlite:///census.sqlite')
conn = engine.connect()
metadata = db.MetaData()
census = db.Table('census', metadata, autoload=True, autoload_with=engine)

# Ordering
# query = db.select([census.columns.state])
# print(conn.execute(query).fetchall()[:10])

# Order by Ascending
# query = db.select([census.columns.state]).order_by(
#     census.columns.state
# )
# print(conn.execute(query).fetchall()[:10])

# Order by Descending
query = db.select([census.columns.state]).order_by(
    db.desc(census.columns.state)
)
print(conn.execute(query).fetchall()[:10])