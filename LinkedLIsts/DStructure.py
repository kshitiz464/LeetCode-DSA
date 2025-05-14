import dstructure
# from dstructure.SLL import SLL

obj=dstructure.SLL()
obj.insert(10) # insert 10 in linked list
obj.insert(20) # insert 20 in linked list
obj.insert(30) # insert 30 in linked list
obj.insert(40) # insert 40 in linked list
obj.delete_f() # delete first node in linked list
obj.delete_l() # delete last node in linked list
obj.delete(20) # delete the node which we pass and return True otherwise False
obj.getnodes() # return all the node in linked list in list.
obj.print()