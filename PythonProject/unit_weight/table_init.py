#initialize table in PostgreSQL database
import dataset
import json

def construct_pg_url(postgres_user='postgres', postgres_password='as457d', postgres_host='localhost', postgres_port='5432', postgres_database='speckle_uno'):
    return ("postgresql://" + postgres_user + ":" + postgres_password + '@' + postgres_host + ':' + postgres_port + '/' + postgres_database)

with open ("RHX1FSNpM.json" ) as e:
    sID = "RHX1FSNpM"
    sData = json.load(e)
    
    db = dataset.connect(construct_pg_url())
    table1 = db['table_uno']
    table1.insert(dict(stream_id = sID, stream_data = sData))
    
e.close()