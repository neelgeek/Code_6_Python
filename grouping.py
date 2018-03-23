import requests, json

with open("orders_string.json","r") as f:
  data = f.read()
orders_dict = json.loads(data)
# orders_dict = json.load('orders_string.json')

class GroupOrders:
    global states_final, ungroupable
    ungroupable = []#List of order_id's that are single and cant be grouped. They are removed from states_final.
    states_final = {}
    def __init__(self,orders):
        self.orders_dict = orders

    def create_states_final(self,orders):
        self.orders_dict = orders
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
    def print_states_final(self):
        print("States_Final: ", states_final)

    def remove_lone_orders(self):
        #ungroupable = [] #List of order_id's that are single and cant be grouped. They are removed from states_final.
        delete = [] #indices to be deleted from temp
        temp = states_final
        for each in states_final:
            for bitch in states_final[each]:
                if len(states_final[each][bitch]) == 1:
                    index = states_final[each][bitch][0]
                    ungroupable.append(orders_dict['orders'][index]['order_id'])
                    #del temp[each][bitch]
                    delete.append(temp[each][bitch])
        for each in states_final:
            for bitch in states_final[each]:
                del temp[each][bitch]
        print("Temp_states_final:",temp)


    def print_ungroupable(self):
        print("Ungroupable: ", ungroupable)



s = GroupOrders(orders_dict)
s.create_states_final(orders_dict)
s.remove_lone_orders()
s.print_states_final()
s.print_ungroupable()

