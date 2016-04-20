#Given a circular linked list, implement an algorithm which 
#returns node at the begin- ning of the loop.

class Node:
	def __init__(self,data):
		self.data=data
		self.next=None


root=Node("a")
root.next=Node("b")
root.next.next=Node("c")
root.next.next.next=Node("d")
root.next.next.next.next=Node("e")
root.next.next.next.next.next=Node("f")
root.next.next.next.next.next.next=root.next.next

node=root
def getLoopNode(root):
	slow=root.next
	fast=root.next.next

	while slow<>fast:
		slow=slow.next
		fast=fast.next.next

	return slow
	
def RemoveLoop(root):
	# find any node inside the loop
	loopNode=getLoopNode(root)
	node=loopNode
	loopNodeCount=1
	# count the number of nodes in the loop by a single pass over the cycle
	while node.next<>loopNode:
		node=node.next
		loopNodeCount=loopNodeCount+1
	print loopNodeCount
	
	# reach the kth node where k= loopNodeCount
	node=root
	for i in range(loopNodeCount):
		node=node.next
	knode=node
	node=root

	#reach the starting by floyds algorithm hare and tortoise
	while knode.next<>node.next:
		node=node.next
		knode=knode.next

	#break loop
	print knode.data
	knode.next=None


RemoveLoop(root)
node=root
while node:
	print node.data
	node=node.next