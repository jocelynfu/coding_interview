# Chapter 2: Linked lists

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

def print_list(node):
	while node:
		print node.val
		node = node.next

#2.1
def remove_dup(node):
	seenlist = set()
	seenlist.add(node.val)
	while(node != None):
		if node.next.val in seenlist:
			print node.val
			node.next = node.next.next
		else:
			seenlist.add(node.next.val)
		node = node.next

node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(3)

node1.next=node2
node2.next=node3
node3.next=node4

print_list(node1)
remove_dup(node1)
print_list(node1)