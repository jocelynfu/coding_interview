# Chapter 2: Linked lists

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

def print_list(node):
	while node:
		print node.val
		node = node.next

#2.1 Time: O(n)
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

		
#2.2
def find_k_to_last(node, k):
	node1 = node
	node2 = node
	# set node 2 to be k apart from node 1
	for i in range(0,k):
		if node2.next == None:
			return "linked list shorter than k elements"
		node2 = node2.next
	# move two nodes together until node 2 reaches end, then node 1 is the node to return
	while (node2 != None):
		node1 = node1.next
		node2 = node2.next
	return node1


#2.3 Time: O(n)
def remove_mid(node):
	while(True):
		# set node value to next node's value
		node.val = node.next.val
		# if the next node is the last node, then set current node to last node and end
		if (node.next.next == None):
			node.next = None
			return
		# otherwise, move to next node
		node = node.next

#correct solution; Time: O(1)
def remove_mid_sol(node):
	node.val = node.next.val
	node.next = node.next.next


#2.4
# brute force: go through and write down each number and then build new linked list
# Move to front: go through linked list, if a value is smaller than pivot, move it to the first node
# Move to back: go through list, if a value is larger than pivot, move to the end




# Tests
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
node6 = Node(6)
node7 = Node(7)

node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
node5.next=node6
node6.next=node7

#print_list(node1)
print find_k_to_last(node1, 3).val
