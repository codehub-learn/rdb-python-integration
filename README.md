# Starter Kit and Resources for RDB and Python Integration

## Recommended Setup
Depending on the database that you will be using some of the below packages may not be needed.

- Python > 3.7
- Python packages: 
  - psycopg2-binary 
  - SQLAlchemy
- Database
  - PostgreSQL
  
## How to set up your PC

### IDE
This course can be done on an IDE of your choice such as VS Code or PyCharm.

### Databases
#### PostgreSQL

You can use PostgreSQL either locally (with standard install process or Docker) eiter in any of the platforms that provide a free tier. Typically those 
free tiers will be limited (size or record wise) but they will suffice for this module. 

*Note:* For any installation process you pick alwyas make sure you note your credentials.

##### Docker installation
- Please follow instructions found in sharepoint under: `Starter Kit and Resources for Tech Lab: PostgreSQL Lab`
##### PaaS

- ElephantSQL
  - Create an account [here](https://www.elephantsql.com/).
  - You will be prompt to create a new team and after this you will be able to create a new instance.
  - Create the instance with the given wizard and when this is done you can find in its details the connection details which you can use to connect with your IDE or applications.
    -  Create new instance
    ![image](https://user-images.githubusercontent.com/25746825/200164845-2e812125-99a4-4e0e-85a0-20e140d02785.png)
    -  Select instance name and plan (keep tiny turtle for free)
    ![image](https://user-images.githubusercontent.com/25746825/200164907-c6e48b87-bbc9-4e5c-ad7d-71aa85acf468.png)
    - Select the closest region (for less network latency)
    ![image](https://user-images.githubusercontent.com/25746825/200164936-7f272a84-b947-4783-8940-6b42b6a1d9e0.png)
    - Review and create your PG instance
    ![image](https://user-images.githubusercontent.com/25746825/200164959-5cbdb4a5-fcfe-4b43-91ef-1c07a58f7c70.png) 
  - Then you will be able to see something like this:
  ![image](https://user-images.githubusercontent.com/25746825/200164985-a659fd25-b6b9-4936-8680-597be04d1447.png)
  - Click on the name so you can see the details and get the DB URL. Look for this:
  
  ![image](https://user-images.githubusercontent.com/25746825/200165029-980dc9ed-a769-422a-8c4c-e18c9bd65988.png)
  
  This includes username, password, host, port and database which you will need in order to connect from either DB IDE or from an application. 



If you are familiar with Heroku, it also provides a free version of PG which you can use (up to 10k records).

- Heroku
  - For provisioning via cli check [this](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) guide.
  - If you prefer to do it via its web interface you can check this [guide](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1).

##### Local - no docker

Download the respective package for your OS from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads) and follow the relevant instrcuttions

## Testing your setup

Please do the following to make sure you can connect to your database from a Python application (applies for both Driver and ORM sessions).

- install the following packages:
```bash
pip install psycopg2-binary # for driver sessions
pip install SQLAlchemy # for ORM sessions
```
- create in your IDE an app.py/main.py file
  - For Driver sessions write the following:
  ```python
  import psycopg2
  
  conn = psycopg2.connect('postgres://username:password@host:port') # if you need to add database then username:password@host:port/db where db is the db name
  crs = conn.cursor()
  crs.execute("SELECT version()")
  print(crs.fetchone())
  ```
  Expected output shoud be somethinh like this: `('PostgreSQL 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.2.0-19ubuntu1) 11.2.0, 64-bit',)`
  - For ORM sessions

  ```python
  from sqlalchemy import create_engine

  engine = create_engine('postgresql+psycopg2://username:password@host:port') # if you need to add database then username:password@host:port/db where db is the db name
  connection = engine.connect()
  my_query = "SELECT version()"
  results = connection.execute(my_query).fetchone()
  print(results)
  ```
  Expected output shoud be somethinh like this: `('PostgreSQL 14.5 (Ubuntu 14.5-0ubuntu0.22.04.1) on x86_64-pc-linux-gnu, compiled by gcc (Ubuntu 11.2.0-19ubuntu1) 11.2.0, 64-bit',)`
  
  Check `sample_conn.py` for relevant sample code.
