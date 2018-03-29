import json, requests
from Algorithm import group_orders_dict, group_ids

trucks_string = '''
{
    "trucks":{
        "Andhra Pradesh":{
                "Small":["1","2","3"],
                "Medium":["11"],
                "Large":["21","22","23"]
            },
            
        "Punjab":{
                "Small":["31","32","33"],
                "Medium":["41","42"],
                "Large":["51","52","53"]
            },

        "Uttar Pradesh":{
                "Small":["311","311","313"],
                "Medium":["411","412","413"],
                "Large":["511","512","513"]
        
            },
             "West Bangal":{
                "Small":["321","322","323"],
                "Medium":["421","422","423"],
                "Large":["521","522","523"]
            }
        
     }
    
}
'''
#trucks_dict=json.loads(trucks_string)
trucks_dict = {'trucks':{}}
get_json=requests.get('https://code6sihapi.herokuapp.com/truckCompany/getTrucks').json()

trucks_assigned = {} #key = truckid , value = group
unassigned_groups = []
#Formats incoming json into my desired dictionary format.

def reformat_json(get_json):
    for each in get_json:
        trucks_dict['trucks'][each['_id']]= {}
        for bitch in each['trucksid']:
            #print(bitch['type'])
            if bitch['type'] not in trucks_dict['trucks'][each['_id']]:
                trucks_dict['trucks'][each['_id']][bitch['type']] = []
                trucks_dict['trucks'][each['_id']][bitch['type']].append(bitch['id'])
            else:
                trucks_dict['trucks'][each['_id']][bitch['type']].append(bitch['id'])
reformat_json(get_json)
print("Trucks_dict:",trucks_dict)
#Assigns trucks based on grouped truck request.
def assign_truck(group_orders_dict):
    index = 0
    for each in group_orders_dict:
        for bitch in group_orders_dict[each]:
            small, medium, large = bitch[0],bitch[1],bitch[2]

            #small, medium, large = group_orders_dict[each][bitch][0], group_orders_dict[each][bitch][1], group_orders_dict[each][bitch][2]
            try:
                for _ in range(small):
                    trucks_assigned[trucks_dict['trucks'][each]['Small'][0]] = group_ids[index]
                    trucks_dict['trucks'][each]['Small'].pop(0)
                    index+=1
                for _ in range(medium):
                    trucks_assigned[trucks_dict['trucks'][each]['Medium'][0]] = group_ids[index]
                    trucks_dict['trucks'][each]['Medium'].pop(0)
                    index += 1
                for _ in range(large):
                    trucks_assigned[trucks_dict['trucks'][each]['Large'][0]] = group_ids[index]
                    trucks_dict['trucks'][each]['Large'].pop(0)
                    index += 1
            except:
                #print("Oops!", sys.exc_info()[0], "occured.")
                unassigned_groups.append(group_ids[index])
                index += 1

assign_truck(group_orders_dict)

final_dict = {"Assigned":trucks_assigned,"Unassigned":unassigned_groups}

# print('Assigned :')
# print(json.dumps(trucks_assigned))
print('Final:')
final = json. dumps(final_dict)
print(final)
headers = {'content-type': 'application/json'}
resp = requests.post(url = "https://code6sihapi.herokuapp.com/shareRequest/postGroups", data =json. dumps(final_dict) , headers = headers).json()
print ("Response: ", resp)
