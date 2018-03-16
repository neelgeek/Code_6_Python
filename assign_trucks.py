import json
import sys
from Algorithm import group_orders_dict

trucks_string='''
{
    "trucks":
        {
            "Andhra Pradesh":{
                "Small":['1','2','3'],
                "Medium":['11','12','13'],
                "Large":['21','22','23']
            },
        
        
            "Punjab":{
                "Small":['31','32','33'],
                "Medium":['41','42','43'],
                "Large":['51','52','53']
            },
        
            "Uttar Pradesh":{
                "Small":['311','321','331'],
                "Medium":['411','421','431'],
                "Large":['511','521','531']
            },
             
            "West Bangal":{
                "Small":['321','322','323'],
                "Medium":['421','422','423'],
                "Large":['521','522','523']
            }
            
        }
    
}
'''
trucks_dict=json.loads(trucks_string)

trucks_assigned = {} #key = truckid , value = group

#Assigns trucks based on grouped truck request.
def assign_truck(group_orders_dict):
    for each in group_orders_dict:
        small,medium,large = group_orders_dict[each][0],group_orders_dict[each][1],group_orders_dict[each][2]
        try:
            for _ in range(small):
                trucks_assigned[trucks_dict['trucks'][each]['Small'][0]] = group_orders_dict[each]
                trucks_dict['trucks'][each]['Small'].pop(0)
            for _ in range(medium):
                trucks_assigned[trucks_dict['trucks'][each]['Medium'][0]] = group_orders_dict[each]
                trucks_dict['trucks'][each]['Medium'].pop(0)
            for _ in range(large):
                trucks_assigned[trucks_dict['trucks'][each]['Large'][0]] = group_orders_dict[each]
                trucks_dict['trucks'][each]['Large'].pop(0)
        except:
            print("Oops!",sys.exc_info()[0],"occured.")
            print("No trucks available in this district.")
assign_truck(group_orders_dict)
print(trucks_assigned)