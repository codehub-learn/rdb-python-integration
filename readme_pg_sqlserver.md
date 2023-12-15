# Starter Kit and Resources for RDB and Python Integration

## Recommended Setup
Depending on the database that you will be using some of the below packages may not be needed.

- Python > 3.7
- Python packages: 
  - psycopg2 
  - psycopg2-binary 
  - pyodbc
  - SQLAlchemy
- Database
  - PostgreSQL
  - SQL-Server
  
## How to set up your PC

### IDE
This course can be done on an IDE of your choice such as VS Code or PyCharm.

### Databases
#### PostgreSQL

You can use PostgreSQL either locally eiter in any of the platforms that provide a free tier. Typically those free tiers will be limited (size or record wise)
but they will suffice for this module. 

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
  This includes username, password, host and port which you will need in order to connect from either DB IDE or from an application. 



If you are familiar with Heroku, it also provides a free version of PG which you can use (up to 10k records).

- Heroku
  - For provisioning via cli check [this](https://devcenter.heroku.com/articles/heroku-postgresql#provisioning-heroku-postgres) guide.
  - If you prefer to do it via its web interface you can check this [guide](https://dev.to/prisma/how-to-setup-a-free-postgresql-database-on-heroku-1dc1).

##### Local

Download the respective package for your OS from [here](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)


#### SQL Server

##### Windows

Please check [here](https://github.com/codehub-learn/MS-SQL-Server-) for detailed instructions.

##### Linux

Follow the guidelines in the official [site](https://www.microsoft.com/en-us/sql-server/sql-server-downloads) according to your distibution.
For example [here](https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu?view=sql-server-ver15) you can find details for installation in Ubuntu in the case you do not want to use containers.

##### SQL Server IDE

For SQL IDE you can you [SSMS](https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15) or if it is not available for your OS you can go with [DBeaver](https://dbeaver.io/)

### Notes:

- Please make sure that your database is working properly and you can connect with it. You can try via your SQL IDE or via console.
