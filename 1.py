
# dat = {
# 			'hydrogen': None, 'humidity': None, 'temperature': None,
# 			'CO': None, 'CO2': None, 'heat_index': None, 
# 			'acetona': None, 'tolueno': None, 'NH4': None
# 		}

# def is_valid():
# 	""" Return True if all values of sensors readings are valid """
# 	return all(list(dat.values()))

# c= str(dat.items())

# print(is_valid())


# d = set()#set creation

# from random import randint

# while len(d) <=10:
# 	d.add(randint(10,99))

# d = sorted(d)

# print(d)

from time import sleep as delay
from threading import Thread

class Node(object): # the network node class
	def __init__(
			self, 
			isroot=False, 
			node_id=int(),
			node_energy=int(), 
			node_data=str(), 
			node_rank=int(), 
			network_nodes=list(), 
			node_active=False, 
			node_package=dict(), 
			root_node=str(), 
			test_data=str()
		):
		super(Node, self).__init__()
		self.isroot 			=	isroot
		self.node_id	 		=	node_id
		self.node_energy 		=	node_energy
		self.node_data 	 		=	node_data
		self.node_rank 	 		=	node_rank
		self.network_nodes		=	network_nodes
		self.node_active 		=	node_active
		self.node_package 		=	node_package
		self.root_node			=	root_node
		self.test_data 			=	test_data

		# self.test()

	def node_characteristic(self):
		while True:
			delay(2)
			print(self.isroot, "Checking root node")
			print(self.node_id, "Printing node id")
			print(self.node_energy, 'Checking node node_energy')
			print(self.node_data, 'Encrypting node data')
			print(self.node_rank, "Checking the node rank")
			print(self.network_nodes, "Checking the node connection")
			print(self.node_active, "Checking if node is active")
			print(self.node_package, "Checking the node packages")
			print(self.root_node, "Checking which node is the root node")
			print(self.test_data, "test data")
			print('\n')
			if self.node_active == False:
				break


#node creation
class Connection(Node):
	def __init__(self, count, type='random', interconnected_roots=False):
		super(Connection, self).__init__()
		self.nodes = []
		self.count = count
		self.interconnected_roots = interconnected_roots
		self.create_nodes()
		self.activate_node()

	def create_nodes(self):
		for i in range(self.count):
			create_node = Node
			self.nodes.append(create_node)

	def activate_node(self):
		val = 1
		for node in self.nodes:
			activation = Thread(
							target=node.node_characteristic, 
							args = (
								node(
										isroot=False, 
										node_energy=10,
										node_active=True,
										test_data=str(val)
									 ),
								)
							)
			activation.start()
			val +=1














# class Tree(object):
# 	def __init__(self):
# 		self.left = None
# 		self.right = None
# 		self.data = None

# 	def __repr__(self):
# 		return self.data

# root = Tree()
# root.data = 'root'
# root.left = Tree()
# root.left.data = 'left'
# root.right = Tree()
# root.right.data = 'right'

# root.left.left = Tree()
# root.left.left.data = "left 2"
# root.left.right = Tree()
# root.left.right.data = 'left-right'

# print(root)




# from turtle import *
# from types import *
 

# myTree = ['A', ['B', ["C", "K", ["D", "E"], "F"], "G", "H"]]
# s = 50;
# startpos = (0, 120)
# def cntstrs(list):
# 	return len([item for item in list if type(item) is str])

# def drawtree(tree, pos, head=0):
# 	c = cntstrs(tree)
# 	while len(tree):
# 		goto(pos)
# 		item = tree.pop(0)
# 		if head:
# 			write(item, 1)
# 			drawtree(tree.pop(0), pos)
# 		else:
# 			if type(item) is str:
# 				newpos = (pos[0] + s*c/4 - s*cntstrs(tree), pos[1] - s)
# 				down()
# 				goto(newpos[0], newpos[1] + 15)
# 				up()
# 				goto(newpos)
# 				write(item, 1)
# 			elif type(item) is list:
# 				drawtree(item, newpos)

# up()
# while True:
# 	drawtree(myTree, startpos, 1)
# Connection(count=5)