# Chapter 3: Stacks and Queues

# Build linked list class
class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

def print_list(node):
	while node:
		print node.val
		node = node.next


