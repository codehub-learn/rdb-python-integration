import psycopg2
from sqlalchemy import create_engine

if __name__ == "__main__":
    conn = psycopg2.connect('postgres://username:password@host:port')
    # A sample connection string can be:'postgres://postgres:postgres@localhost:5432'
    # OR a sample connection string including DB can be:'postgres://postgres:postgres@localhost:5432/my_db'

    crs = conn.cursor()

    crs.execute("SELECT version()")

    print(crs.fetchone())
    # ('PostgreSQL 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.2.0-19ubuntu1) 11.2.0, 64-bit',)
    
    engine = create_engine('postgresql+psycopg2://username:password@host:port')
    # A sample connection string can be:'postgresql+psycopg2://postgres:postgres@localhost:5432'
    # OR a sample connection string including DB can be:'postgresql+psycopg2://postgres:postgres@localhost:5432/my_db'


    connection = engine.connect()

    my_query = "SELECT version()"
    results = connection.execute(my_query).fetchone()
    print(results)
    # ('PostgreSQL 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.2.0-19ubuntu1) 11.2.0, 64-bit',)
