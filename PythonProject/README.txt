'''
ATTENTION: 

Please follow the following instructions to test out the prototype!\

1. Download and open /unit_weight folder

2. Install PostGreSQL package from: (13)
    https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    
3. Install pgAdmin webapp at: (4.25)
    https://www.pgadmin.org/

4. During installation of the PostgreSQL package, please make sure that the data structure have the following config 
    >>>Server [localhost]
    >>>Database [Postgres]
    >>>Port [5432]
    >>>Username [Postgres]
    >>>Password [User_Defined]
    
    ***REMEMBER TO COPY DOWN YOUR PASSWORD, YOU CANNOT RETRIEVE IT LATER ***

5. Create a localhost database with the following commands in SQL Shell (included with PostgreSQL):
    ---Launch "PSQL cmd" by searching in the start menu
    >>>Server [localhost]
    >>>Database [Postgres]
    >>>Port [5432]
    >>>Username [Postgres]
    >>>Password [User_Defined]
    
    *** REMEMBER TO CHANGE THE PARAMETERS IN THE <construct_pg_url> function in python accordingly ***
	IF YOU WANT A CUSTOM DB SETUP/ AWS INTEGRATION, ENSURE PGADMIN<->PSQL<->PYTHON INFO ARE COHERENT	
    
6. PLace the python codes, JSON files in a single folder (Try not to throw loose files around for proper referencing)

7. Run the pythin in the following order: (or sequentially in the jupyter notebook files, also provided)
    >>>table_init.py
    >>>PSQL_method.py
    >>>JSON_method.py
    
    *** Jupyter notebook or CMD running is recommended, somehow VS returns an error ***
    
8.Sit back and enjoy! :0)


'''