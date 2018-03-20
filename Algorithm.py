import json

orders_string='''
{
    "orders":[
        {
            "order_id": "1",
            "crop": "wheat",
            "from": "Uttar Pradesh",
            "to": "Goa",
            "quantity": "250"
        },
        {
            "order_id": "2",
            "crop": "wheat",
            "from": "Punjab",
            "to": "Kerala",
            "quantity": "70"
        },
        {
            "order_id": "3",
            "crop": "wheat",
            "from": "Punjab",
            "to": "Gujarat",
            "quantity": "125"
        },
        {
            "order_id": "4",
            "crop": "wheat",
            "from": "Punjab",
            "to": "Kerala",
            "quantity": "35"
        },
        {
            "order_id": "5",
            "crop": "rice",
            "from": "West Bangal",
            "to": "Goa",
            "quantity": "95"
        },
        {
            "order_id": "6",
            "crop": "rice",
            "from": "Uttar Pradesh",
            "to": "Goa",
            "quantity": "40"
        },
        {
            "order_id": "7",
            "crop": "rice",
            "from": "Punjab",
            "to": "Uttar Pradesh",
            "quantity": "200"
        },
        {
            "order_id": "8",
            "crop": "rice",
            "from": "Andhra Pradesh",
            "to": "Maharashtra",
            "quantity": "310"
        }
    ]
}
'''


#---------------------------------------------------example json--------------------------------------------------------------


#states_from={}
#states_to={}


states_final={}
orders_dict=json.loads(orders_string)


#print(orders_dict['orders'][0]['order_id'])


#print(len(orders_dict['orders']))


'''for i in range(len(orders_dict['orders'])):
    #print(orders_dict['orders'][i]['order_id'])
    if orders_dict['orders'][i]['from'] not in states_from:
        states_from[orders_dict['orders'][i]['from']]=[]
        states_from[orders_dict['orders'][i]['from']].append(i)
    else:
        states_from[orders_dict['orders'][i]['from']].append(i)

    if orders_dict['orders'][i]['to'] not in states_to:
        states_to[orders_dict['orders'][i]['to']]=[]
        states_to[orders_dict['orders'][i]['to']].append(i)
    else:
        states_to[orders_dict['orders'][i]['to']].append(i)
'''

    # creating master dictionary

for i in range(len(orders_dict['orders'])):
    if orders_dict['orders'][i]['from'] not in states_final:
        states_final[orders_dict['orders'][i]['from']] = {}
        if orders_dict['orders'][i]['to'] not in states_final[orders_dict['orders'][i]['from']]:
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']] = []
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']].append(i)
        else:
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']].append(i)
    else:
        if orders_dict['orders'][i]['to'] not in states_final[orders_dict['orders'][i]['from']]:
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']] = []
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']].append(i)
        else:
            states_final[orders_dict['orders'][i]['from']][orders_dict['orders'][i]['to']].append(i)

print(states_final)


# print(states_to)

def returnSum(group_orders):
    total = 0
    for item in group_orders:
        total += int(orders_dict['orders'][item]['quantity'])

    return total


# small=100 ,medium =500 ,large =1000

def createTruckRequest(total, i):
    if total <= 100:
        global sm
        sm += i
    elif total > 100 and total <= 500:
        global me
        me += i
    elif total > 500 and total <= 1000:
        global la
        la += i
    else:
        q = int(total / 1000)
        r = total % 1000
        la += q
        createTruckRequest(r, 1)


# finding order indices
group_orders = []
group_orders_dict = {}  # dictionary which contains lsit of required trucks
total = 0
sm = me = la = 0
for each in states_final:
    for s in (states_final[each]):
        group_orders = (states_final[each][s])
        total = returnSum(group_orders)
        # print(each)
        # print(total)
        if each not in group_orders_dict:
            group_orders_dict[each] = []
            sm = me = la = 0
            createTruckRequest(total, 1)
            group_orders_dict[each] = [sm, me, la]
        else:
            sm = me = la = 0
            createTruckRequest(total, 1)
            group_orders_dict[each] = [sm, me, la]

print(group_orders_dict)
# for each in group_orders_dict:
#     print(group_orders_dict[each])
