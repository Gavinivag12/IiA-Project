import json
import math

#filters
def filter_element(data, element_type):
    resources = data['resources']
    filter = [d for d in resources if any([(d['type'] == e) for e in element_type])]
    return filter
def filter_properties(data):
    resources = data['resources']
    filter = [d for d in resources if 'materialRef' in d]
    return filter
    
    
#component functions for weight and length modules
def find_propertyRef(lista):
    return lista['properties']['structural']['propertyRef']

def find_topology_list(lista):
    return lista['value']

def find_element_elevation(lista):
    topology_array = lista['value']
    if (topology_array[2]>topology_array[5]): return topology_array[2]
    else: return topology_array[5]

def gen_property_dict(data):
    property_dict = {}
    for entry in data:
        property_dict[entry['applicationId']]=entry['materialRef']
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
with open( "RHX1FSNpM.json" ) as f:
    with open( "property.json" ) as g:
        speckle_objects = json.load(f)
        property_objects = json.load(g)
        
        property_dict = gen_property_dict(filter_properties(speckle_objects)) 
        filter1D = filter_element(speckle_objects, ['Polyline/Structural1DElementPolyline'])

        number_of_elements = len(filter1D)
        total_weight = 0
        print("Number of Records: " + str(number_of_elements))
        print()

        weight_by_elev_dict = {}
        for d in filter1D:
            element_w = element_weight(length(find_topology_list(d)), unit_weight(property_dict, find_propertyRef(d), property_objects))
            total_weight += element_w
            weight_by_elev_dict = gen_weight_by_elev(weight_by_elev_dict, element_w, find_element_elevation(d))
        
    
        print("total weight of structural 1D members: " + str(total_weight))
        print(weight_by_elev_dict)
    g.close()
f.close()
