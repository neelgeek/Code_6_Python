# import json,requests,urllib
# from datetime import datetime,timedelta
# # get_truckids = requests.get('https://code6sihapi.herokuapp.com/truckCompany/getTrucks').json()
# # print(get_truckids)
# previous_date = datetime.now() - timedelta(days=3)
# s= previous_date.isoformat()
#
# dict = {}
# dict["date"] = s
# print(dict)
# response = requests.post(url="https://code6sihapi.herokuapp.com/shareRequest/getRequests", data = dict ).json()
# print(response)
#
# def format_json(response):
#     orders_dict = {"orders":[]}
#     for each in range(len(response)):
#         #print(each)
#         orders_dict["orders"].append({})
#         orders_dict["orders"][each]["order_id"] = response[each]["_id"]
#         orders_dict["orders"][each]["from"] = response[each]["origin"]
#         orders_dict["orders"][each]["to"] = response[each]["destination"]
#         orders_dict["orders"][each]["quantity"] = response[each]["weight"]
#     return orders_dict
#
# a = format_json(response)
# print(a)

from datetime import *

today = datetime.now()
birthdate = input("Birthdate:")
Birthmonth = input ("Birthmonth:")
def calc(birthdate,birthmonth):
    res = timedelta(days=birthdate,)
    print(res)

calc(birthdate,Birthmonth)