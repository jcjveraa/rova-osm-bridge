import json
import xml.etree.ElementTree as ET

with open('manual_data_file.json') as f:
    data = json.load(f)

top_level = ET.Element('osmChange',{'version': '0.6', 'generator': 'rova-to-osm'})
create_level = ET.SubElement(top_level, 'create')

idcounter = 0

for item in data:
    idcounter = idcounter -1
    # skip items that do not have a FacilityType to avoid errors below
    if not item.get('FacilityType'):
        continue
    if item['FacilityType']['Id'] == 14:
        # print(item['Address'])
        lat = item['MapLocation']['latitude']
        lon = item['MapLocation']['longitude']
        title = item['Title']
        guid = item['Guid']
        attrib_dict = {'user': 'Pozoman', 'lat': str(lat), 'lon': str(lon), 'visible': 'true', 'version':'1', 'id': str(idcounter)}
        new_node = ET.SubElement(create_level, 'node',attrib_dict)
        ET.SubElement(new_node, 'tag', {'k': 'access', 'v': 'private'})
        ET.SubElement(new_node, 'tag', {'k': 'operator', 'v': 'ROVA'})
        ET.SubElement(new_node, 'tag', {'k': 'amenity', 'v': 'waste_disposal'})
        ET.SubElement(new_node, 'tag', {'k': 'waste', 'v': 'trash'})

tree = ET.ElementTree(top_level)
tree.write('trash.osc')
