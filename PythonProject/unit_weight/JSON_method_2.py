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
    
    
#component functions for volume and length modules
def find_propertyRef(lista):
    return lista['properties']['structural']['propertyRef']

def find_topology_list(lista):
    return lista['value']

def find_element_elevation(lista):
    topology_array = lista['value']
    if (topology_array[2]>topology_array[5]): return topology_array[2]
    else: return topology_array[5]

def area_2_list(a_list):
    """Returns the area when given a list of x,y,z,x,y,z... coordinates"""
    if len(a_list) % 3 != 0:
        raise ValueError('List does not contain multiples of three values')
    if a_list[:3] != a_list[-3:]:
        a_list += a_list[:3] # add first to end to close the perimeter
    
    x1, y1, _, *a_list = a_list
    area = 0.0
    while a_list:
        x2, y2, _, *a_list = a_list
        area += (x1 * y2 - x2 * y1) / 2.0
        x1, y1 = x2, y2
    return area

def gen_property_dict(data):
    property_dict = {}
    for entry in data:
        property_dict[entry['applicationId']]=area_2_list(entry['profile']['value'])
    return property_dict

def gen_volume_by_elev(input_dict, volume, elev):
    if input_dict.get(elev): input_dict[elev] = input_dict[elev] + volume
    else: input_dict[elev] = volume
    return input_dict

#Modules
def length(topo):
    return math.sqrt((abs(topo[0] - topo[3])**2) + (abs(topo[1] - topo[4])**2) + (abs(topo[2] - topo[5])**2))
    
def unit_volumn(lista, entry):
    index =  lista[entry]
    return float(index)

def element_volume(length, unit_volume):
     return (length * unit_volume)
    
    
#main stuff
with open( "RHX1FSNpM.json" ) as f:
    speckle_objects = json.load(f)

    property_dict = gen_property_dict(filter_properties(speckle_objects)) 
    filter1D = filter_element(speckle_objects, ['Polyline/Structural1DElementPolyline'])

    number_of_elements = len(filter1D)
    total_volume = 0
    print("Number of Records: " + str(number_of_elements))

    volume_elev_dict = {}
    
    for d in filter1D:
        element_v = element_volume(length(find_topology_list(d)), unit_volumn(property_dict, find_propertyRef(d)))
        total_volume += element_v
        volume_elev_dict = gen_volume_by_elev(volume_elev_dict, element_v, find_element_elevation(d))
    
    print("total volume of structural 1D members: ",total_volume)
    print(volume_elev_dict)
f.close
