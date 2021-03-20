import dataset
import json
import math

def construct_pg_url(postgres_user='postgres', postgres_password='as457d', postgres_host='localhost', postgres_port='5432', postgres_database='speckle_uno'):
    return ("postgresql://" + postgres_user + ":" + postgres_password + '@' + postgres_host + ':' + postgres_port + '/' + postgres_database)

db = dataset.connect(construct_pg_url())
    
#filters
def filter_element(datab):
    element_list = []
    statement = 'SELECT * FROM (SELECT jsonb_array_elements(stream_data->\'resources\')AS resources FROM table_uno) AS main_table WHERE resources->>\'type\' = \'Polyline/Structural1DElementPolyline\';'
    for row in datab.query(statement):
        element_list.append(row)
    return element_list

def filter_property(datab):
    property_list = []
    statement = 'SELECT * FROM (SELECT jsonb_array_elements(stream_data->\'resources\')AS resources FROM table_uno) AS main_table WHERE resources->>\'materialRef\' IS NOT NULL;'
    for row in datab.query(statement):
        property_list.append(row)
    return property_list

#component functions for weight and length modules
def find_propertyRef(lista):
    return lista['resources']['properties']['structural']['propertyRef']

def find_topology_list(lista):
    return lista['resources']['value']

def find_element_elevation(lista):
    topology_array = lista['resources']['value']
    if (topology_array[2]>topology_array[5]): return topology_array[2]
    else: return topology_array[5]

def gen_property_dict(data):
    property_dict = {}
    for entry in data:
        property_dict[entry['resources']['applicationId']]=entry['resources']['materialRef']
    return property_dict

def gen_weight_by_elev(input_dict, weight, elev):
    if input_dict.get(elev): input_dict[elev] = input_dict[elev] + weight
    else: input_dict[elev] = weight
    return input_dict

#Modules
def length(topo):
    return math.sqrt((abs(topo[0] - topo[3])**2) + (abs(topo[1] - topo[4])**2) + (abs(topo[2] - topo[5])**2))

def unit_weight(lista, entry, data):
    index =  lista[entry]
    return float(data[index])

def element_weight(length, unit_weight):
    gross_weight = length * unit_weight
    return (gross_weight)

#main stuff
with open( "property.json" ) as g:
    property_objects = json.load(g)
    property_dict = gen_property_dict(filter_property(db)) #reference
    filter1D = filter_element(db)

    number_of_elements = len(filter1D)
    total_weight = 0
    print("Total number of 1D Elements: ", number_of_elements)
    
    weight_by_elev_dict = {}
    for d in filter1D:
        element_w = element_weight(length(find_topology_list(d)), unit_weight(property_dict, find_propertyRef(d), property_objects))
        total_weight += element_w
        weight_by_elev_dict = gen_weight_by_elev(weight_by_elev_dict, element_w, find_element_elevation(d))
    
    print("total weight of structural 1D members: " + str(total_weight))
    print(weight_by_elev_dict)
    
g.close()
