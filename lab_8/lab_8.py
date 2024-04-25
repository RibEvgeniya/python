'''import xmltodict
import re
pattern = r'\s\d{2}.\d{2}-'


def check_tags(check, dct_c):
    tag_time = {}
    for ch in dct_c['osm'][check]:
            if 'tag' in ch:
                tags = ch['tag']
                if isinstance(tags, list):
                    for tag in tags:
                        if tag['@k'] == 'opening_hours':
                            matches = re.findall(pattern, tag['@v'])
                            for match in matches:
                                if match != None:
                                    if not tag_time.get(match[1:3]):
                                        tag_time[match[1:3]] = 1
                                    else:
                                        tag_time[match[1:3]] += 1
    return tag_time


file = open('12.osm', 'r', encoding='utf-8')
text = file.read()
file.close()


dct = xmltodict.parse(text)
dct_time1 = check_tags('way', dct)
dct_time2 = check_tags('node', dct)
for k, v in dct_time1.items():
    if k in dct_time2:
        dct_time2[k] += v
    else:
        dct_time2[k] = v

print(dct_time2)'''




import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type,
                                  elem.id,
                                  elem.version,
                                  elem.visible,
                                  pd.Timestamp(elem.timestamp),
                                  elem.uid,
                                  elem.user,
                                  elem.changeset,
                                  len(elem.tags),
                                  tag.k,
                                  tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")


osmhandler = OSMHandler()
osmhandler.apply_file("12.osm")
df_osm = pd.DataFrame(osmhandler.osm_data,columns=['1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','11c'])

restaurant= df_osm[df_osm['11c'] == 'restaurant']

result = df_osm[(df_osm['10c'] == 'opening_hours')  & (df_osm['2c'].isin(restaurant['2c']))]

result1=result.groupby(result['11c'])
print(result)

osmhandler.apply_file("12 -2.osm")
df_osm = pd.DataFrame(osmhandler.osm_data,columns=['1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','11c'])

restaurant= df_osm[df_osm['11c'] == 'restaurant']

result = df_osm[(df_osm['10c'] == 'opening_hours')  & (df_osm['2c'].isin(restaurant['2c']))]

result1=result.groupby(result['11c'])
print(result)