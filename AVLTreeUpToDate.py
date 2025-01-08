#id1:
#name1:
#username1:
#id2:
#name2:
#username2:

# TODO: Delete prints and copied from entire file

"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		if key is not None:  # Node is real
			self.left = AVLNode(None, None)
			self.right = AVLNode(None, None)
		else:  # Node is virtual
			self.left = None
			self.right = None
		self.key = key
		self.value = value
		self.parent = None
		self.height = -1
		self.size = 0
		self.bfs = 0


	# ************* ↓ COPIED PROCS ↓ *****************
	
	def get_bfs(self):
		return self.bfs

	def set_bfs(self, b):
		self.bfs = b
			
	"""fields_update: Recompute (height, bfs) for this node in O(1)."""
	def fields_update(avl_node):
		left_h = -1
		right_h = -1
		if avl_node.get_left() is not None and avl_node.get_left().is_real_node():
			left_h = avl_node.get_left().get_height()
		if avl_node.get_right() is not None and avl_node.get_right().is_real_node():
			right_h = avl_node.get_right().get_height()

		avl_node.set_height(1 + max(left_h, right_h))
		avl_node.set_bfs(left_h - right_h)

	# ************* ↑ COPIED PROCS ↑ *****************
			

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key is not None
	
	def get_balance_F(self):
		return self.left.get_height()-self.right.get_height()

	# ************* GETTERS *************
	
	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self): # FINAL
		return self.root
	
	def get_key(self):
		return self.key
	
	def get_value(self):
		return self.value
	
	def get_left(self):
		return self.left
	
	def get_right(self):
		return self.right
	
	def get_parent(self):
		return self.parent
	
	def get_height(self):
		return self.height
	
	def get_size(self):
		return self.size
	
	def get_brother(self):
		if self.get_parent() is None:
			return None
		if self.key < self.parent.key:
			return self.get_parent().get_right()
		else:
			return self.get_parent().get_left()

	
	# ************* SETTERS *************
	def set_key(self,key):
		self.key = key
		return None
	
	def set_value(self, value):
		self.value = value
		return None
	
	def set_parent(self, node):
		self.parent = node
		return None
	
	def set_right(self, node):
		self.right = node
		return None
	
	def set_left(self, node):
		self.left = node
		return None
	
	def set_right_with_parents(self,node):
		self.right = node
		if node is not None:
			node.set_parent(self)
		return None
	
	def set_left_with_parents(self,node):
		self.left = node
		node.set_parent(self)
		return None
	
	def set_height(self,h):
		self.height = h
		return None
	
	def set_size(self,s):
		self.size = s
		return None
	
	def update_size(self): # TODO: check if being called
		if not self.is_real_node():
			self.set_size(0)
			return
		left_size = self.get_left().get_size() if (self.get_left() is not None and self.get_left().is_real_node()) else 0
		right_size = self.get_right().get_size() if (self.get_right() is not None and self.get_right().is_real_node()) else 0

		new_size = 1 + left_size + right_size
		self.set_size(new_size)
	
	def update_height(self): # TODO: check if being called
		if not self.is_real_node():
			self.set_height(-1)
			return
		left_height = self.get_left().get_height() if (self.get_left() is not None and self.get_left().is_real_node()) else -1
		right_height = self.get_right().get_height() if (self.get_right() is not None and self.get_right().is_real_node()) else -1

		new_height = 1 + max(left_height, right_height)
		self.set_height(new_height)
	
"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self, root = None):
		self.root = root
		self.tree_size = 0

		# TODO: bring back if necessary:
		# self.max_node = None


	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def search(self, key):	# FINAL
		#We used helper function - Search_helper.
		#We passed 1 as the value of the depth since we have been asked to return the length of the search route + 1.
		#We understand that in AVL trees, the depth of a node is the same as the searching route to the node. 
		print("\nBEFORE SEARCH:")
		print_tree(self.root)
		return self.search_helper(self.root,key,1)
	
	# ************* ↓ COPIED PROCS ↓ *****************
	def size(self):
		return self.tree_size

	# ************* ↑ COPIED PROCS ↑ *****************


	#The helper function:
	#Here we used the similar method to the well known algorithem "Binary Search".
	def search_helper(self,node,key,depth):	# FINAL
        #Base case1:
		if (node is None) or (not node.is_real_node()):
			return None, depth - 1
		#Base case2:
		if node.get_key() == key:
			return node, depth
		#Since AVL is kind of a binary search tree, we used the fact that the keys of the left side of the tree are smaller than the node's key,
		#also the right side is bigger.
		if key < node.get_key():
			return self.search_helper(node.get_left(), key, depth + 1)
		else:
			return self.search_helper(node.get_right(), key, depth + 1)

	"""searches for a node in the dictionary corresponding to the key, starting at the max
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""
	def finger_search(self, key): # FINAL
		# If max_node is not set or is a virtual node, the tree is effectively empty
		self.max_node = self.max_node()
		if (self.max_node is None) or (not self.max_node.is_real_node()):
			return None, 0
		# If the search key is greater than the max key, it can't be in the tree
		if key > self.max_node.get_key():
			return None, 1
		# If it's exactly the max key, we've found it immediately
		if key == self.max_node.get_key():
			return self.max_node, 1
		# Otherwise, the key is less than max_node's key -> we may climb up
		up_steps = 0
		curr = self.max_node
		# Climb up while:
        #   1) there's a real parent,
        #   2) the parent's key >= the key we're searching,
        # because we might find a closer ancestor whose subtree could contain key
		while curr.get_parent() is not None and curr.get_parent().is_real_node() and curr.get_parent().get_key() >= key:
			curr = curr.get_parent()
			up_steps += 1
		# Now perform a standard BST search starting at 'curr'
		node_found, depth_down = self.search_helper(curr, key, 1)
		# Combine 'up_steps' (climbing up) with 'depth_down - 1' (BST descent)
		if node_found is None:
			return None, up_steps + (depth_down - 1)
		else:
			return node_found, up_steps + (depth_down - 1)


	"""inserts a new node into the dictionary with corresponding key and value (starting at the root)

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""

	# ***************** COPIED INSERT: ************************

	def insert_as_leaf(self, avl_node_1 : AVLNode): # FINAL
		e = 0
		if self.get_root() is None or not self.get_root().is_real_node():
			self.root = (avl_node_1)
			avl_node_1.set_height(0)
			# avl_node_1.get_left().set_parent(avl_node_1)
			# avl_node_1.get_right().set_parent(avl_node_1)
			self.tree_size += 1
			return e

		y = None
		x = self.get_root()
		while x is not None and x.is_real_node():
			y = x
			e += 1
			if avl_node_1.get_key() < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()

		avl_node_1.set_parent(y)
		avl_node_1.set_height(0)
		if avl_node_1.get_key() < y.get_key():
			y.set_left(avl_node_1)
		else:
			y.set_right(avl_node_1)
		avl_node_1.get_left().set_parent(avl_node_1)
		avl_node_1.get_right().set_parent(avl_node_1)
		self.tree_size += 1
		return e

	def insert(self, key, val): # FINAL
		new_node = AVLNode(key, val)
		e = self.insert_as_leaf(new_node)

		height_change_counter = 0
		z = new_node.get_parent()
		while z is not None:
			old_h = z.get_height()
			z.fields_update()
			if abs(z.get_bfs()) < 2:
				if z.get_height() != old_h:
					height_change_counter += 1
				z = z.get_parent()
			else:
				if z.get_bfs() == 2:
					if z.get_left().get_bfs() >= 0:
						self.rotate_right(z)
					else:
						self.double_rotate_right(z)
				else:
					if z.get_right().get_bfs() <= 0:
						self.rotate_left(z)
					else:
						self.double_rotate_left(z)
				z = z.get_parent()

		print("\nAFTER INSERT:")
		print_tree(self.root)
		return (new_node, e, height_change_counter)

	def normal_insert(self, key, val, node): # FINAL
		if (node is None) or (not node.is_real_node()):
			new_node = AVLNode(key, val)
			new_node.set_height(0)
			new_node.set_size(1)

			left_virtual = AVLNode(None, None)
			right_virtual = AVLNode(None, None)

			left_virtual.set_parent(new_node)
			right_virtual.set_parent(new_node)

			new_node.set_left_with_parents(left_virtual)
			new_node.set_right_with_parents(right_virtual)

			return new_node
		if key < node.get_key():
			inserted_node = self.normal_insert(key, val, node.get_left())
			node.set_left_with_parents(inserted_node)
			return inserted_node
		else:
			inserted_node = self.normal_insert(key, val, node.get_right())
			node.set_right_with_parents(inserted_node)
			return inserted_node
		
	def normal_insert_with_edges(self, key, val, node, e): # FINAL
		# Base case: if node is None or a virtual node, create and return a new real node
		if (node is None) or (not node.is_real_node()):
			new_node = AVLNode(key, val)
			new_node.set_height(0)
			new_node.set_size(1)

			left_virtual = AVLNode(None, None)
			right_virtual = AVLNode(None, None)
			left_virtual.set_parent(new_node)
			right_virtual.set_parent(new_node)

			new_node.set_left_with_parents(left_virtual)
			new_node.set_right_with_parents(right_virtual)

			return new_node, e  # e does not increase at the moment of creation
		# Recursive BST logic, incrementing edge count
		if key < node.get_key():
			inserted_node, e2 = self.normal_insert_with_edges(key, val, node.get_left(), e + 1)
			node.set_left_with_parents(inserted_node)
			return inserted_node, e2
		else:
			inserted_node, e2 = self.normal_insert_with_edges(key, val, node.get_right(), e + 1)
			node.set_right_with_parents(inserted_node)
			return inserted_node, e2
	
	# ***************** ROTATIONS ************************
	def rotate_left(self, x : AVLNode): # FINAL
		parent = x.get_parent()
		y = x.get_right()

		x.set_right(y.get_left())
		if y.get_left() is not None and y.get_left().is_real_node():
			y.get_left().set_parent(x)

		x.set_parent(y)
		y.set_left(x)

		y.set_parent(parent)
		if parent is not None: # Doesn't have to be a real node!
			if parent.get_left() == x:
				parent.set_left(y)
			else:
				parent.set_right(y)
		else:
			self.set_root(y)

		# Update fields
		x.fields_update()
		y.fields_update()

		return y
	
	def rotate_right(self, y : AVLNode): # FINAL
		parent = y.get_parent()
		x = y.get_left()

		y.set_left(x.get_right())
		if x.get_right() is not None: # Doesn't have to be a real node!
			x.get_right().set_parent(y)

		y.set_parent(x)
		x.set_right(y)
		x.set_parent(parent)
		
		if parent is not None and parent.is_real_node():
			if parent.get_left() == y:
				parent.set_left(x)
			else:
				parent.set_right(x)
		else:
			self.set_root(x)

		
		# update fields
		y.fields_update()
		x.fields_update()

		return x

	def double_rotate_left(self, y : AVLNode): # FINAL
		self.rotate_right(y.get_right()) # this is x from the lecture
		z = self.rotate_left(y)
		return z

	def double_rotate_right(self, y : AVLNode): # FINAL
		self.rotate_left(y.get_left()) # this is x from the lecture
		z = self.rotate_right(y)
		return z


	# ************************* COPIED FINGER_INSERT ↓ *************************
	# TODO: test finger insert
	"""inserts a new node into the dictionary with corresponding key and value, starting at the max

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
	@rtype: (AVLNode,int,int)
	@returns: a 3-tuple (x,e,h) where x is the new node,
	e is the number of edges on the path between the starting node and new node before rebalancing,
	and h is the number of PROMOTE cases during the AVL rebalancing
	"""
	
	def _finger_insert_as_leaf(self, start_node, new_node): # FINAL
		edges_down = 0
		x = start_node
		y = None
		while x.is_real_node():
			y = x
			edges_down += 1
			if new_node.get_key() < x.get_key():
				x = x.get_left()
			else:
				x = x.get_right()

		new_node.set_parent(y)
		new_node.set_height(0)
		if new_node.get_key() < y.get_key():
			y.set_left(new_node)
		else:
			y.set_right(new_node)
		new_node.get_left().set_parent(new_node)
		new_node.get_right().set_parent(new_node)
		self.tree_size += 1
		return edges_down

	def finger_insert(self, key, val): # FINAL
		if not self.get_root().is_real_node():
			new_root = AVLNode(key, val)
			new_root.set_height(0)
			new_root.get_left().set_parent(new_root)
			new_root.get_right().set_parent(new_root)
			self.set_root(new_root)
			self.tree_size += 1
			return (new_root, 0, 0)

		maxn = self.max_node()
		e_up = 0
		curr = maxn
		if key > maxn.get_key():
			pass  # no climb up
		else:
			while (curr.get_parent() is not None 
				and curr.get_parent().is_real_node()
				and curr.get_parent().get_key() >= key):
				curr = curr.get_parent()
				e_up += 1

		new_node = AVLNode(key, val)
		e_down = self._finger_insert_as_leaf(curr, new_node)
		e = e_up + e_down

		height_change_counter = 0
		z = new_node.get_parent()
		while z is not None and z.is_real_node():
			old_h = z.get_height()
			z.fields_update()
			if abs(z.get_bfs()) < 2:
				if z.get_height() != old_h:
					height_change_counter += 1
				z = z.get_parent()
			else:
				if z.get_bfs() == 2:
					if z.get_left().get_bfs() >= 0:
						self.rotate_right(z)
					else:
						self.double_rotate_right(z)
				else:
					if z.get_right().get_bfs() <= 0:
						self.rotate_left(z)
					else:
						self.double_rotate_left(z)
				z = z.get_parent()

		# print("\nAFTER FINGER INSERT:")
		# print_tree(self.root)
		return (new_node, e, height_change_counter)

	# ************************* COPIED FINGER_INSERT ↑ *************************

	""" returns the successor of a given node, that's inside the tree """
	def successor(self, node : AVLNode): # FINAL
		# end cases
		if node is None or not node.is_real_node():
			return None
		# if we dont have right child we start going upwards:
		if node.get_right() is None:
			if node.get_parent is not None:
				while node.get_parent().get_key() < node.get_key():
					node = node.get_parent()
				if node.get_parent() is None:
					return None
				return node.get_parent()
			else:
				return None
		# if we have right child:
		node = node.get_right()
		while node is not None and node.get_left() is not None:
			node = node.get_left()
		return node

	""" returns the predecessor of a given node, that's inside the tree """
	def predecessor(self, node : AVLNode): # FINAL
		# end cases
		if node is None or not node.is_real_node():
			return None
		# return max of left subtree, if exists
		if node.get_left() is not None:
			node = node.get_left()
			while node is not None and node.get_right() is not None:
				node = node.get_right()
			return node
		# left subtree doesnt exist, travel up the tree:
		if node.get_parent() is not None:
			while node.get_parent().get_key() > node.get_key():
				node = node.get_parent()
			if node.get_parent() is None:
				return None
			return node.get_parent()
		return None
		
	
	def switch_two_nodes(self, node1, node2): # FINAL
		nodeP = node1.get_parent()
		nodeR = node1.get_right()
		nodeL = node1.get_left()
		
		node1.set_parent(node2.get_parent())
		node1.set_right(node2.get_right())
		node1.set_left(node2.get_left())
		
		node2.set_parent(nodeP)
		node2.set_right(nodeR)
		node2.set_left(nodeL)
		
		node1.fields_update()
		node2.fields_update()

	
	
	# TODO delete() tests: when we delete root, leaf, unary node, middle node, min and max
	# TODO: Update max if we deleted max
	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node): # FIXME
		isSuc = False # flag for successor
		if (node.get_left() is not None and node.get_right() is not None
			and node.get_left().is_real_node() and node.get_right().is_real_node()):
			# node isn't a leaf nor a unary node
			suc = self.successor(node)
			if suc is not self.max_node(): #TODO: RESOLVE SUC IN DELETE
				# self.switch_two_nodes(node, suc) # switches node with successor and updates heights/sizes
				tempKey = node.get_key()
				tempVal = node.get_value()
				node.set_key(suc.get_key())
				node.set_value(suc.get_value())
				suc.set_key(tempKey)
				suc.set_value(tempVal)
				node = suc
				isSuc = True
		# node is a leaf or unary
		parent = node.get_parent()
		if (node.get_left() is None and (node.get_right() is None or not node.get_right().is_real_node())
			or (not node.get_left().is_real_node() and (node.get_right() is None or not node.get_right().is_real_node()))):
			# node is a leaf
			# if parent is None: # single node in a tree
			if self.get_root() is node: # single node in a tree
				self.root = None
				self.tree_size = 0
				print(f"\nAFTER DELETION OF {node.get_key()}:")
				print_tree(self.root)
				return
			if isSuc or node.get_key() < parent.get_key():
				# node is a left leaf
				parent.set_left_with_parents(AVLNode(None, None)) # detach
				self.tree_size -= 1
			else:
				# node is a right leaf
				parent.set_right_with_parents(AVLNode(None, None)) # detach
				self.tree_size -= 1
		else:
			# node is unary
			child = node.get_right() if (node.get_right() is not None and node.get_right().is_real_node()) else node.get_left()
			# if parent is None: # the tree is only node and his single child
			if self.get_root() is node: # the tree is only node and his single child
				self.root = child
				self.tree_size -= 1
				self.root.set_parent(None)
				print(f"\nAFTER DELETION of {node.get_key()}:")
				print_tree(self.root)
				return
			if isSuc or node.get_key() < parent.get_key():
				# node is a left unary
				self.tree_size -= 1
				parent.set_left_with_parents(child)
			else:
				# node is a right unary
				self.tree_size -= 1
				parent.set_right_with_parents(child)

		# parent.update_height()
		# TODO: organize
		# parent.fields_update()
		print("\nBEFORE BALANCE:")
		print_tree(self.root)
		self.check_heights(parent)		
		
		print("\nAFTER BALANCE:")
		print_tree(self.root)
		return	
		
	def case22(self, node : AVLNode): # FIXME
		# Travel up the tree
		parent = node.get_parent()
		if parent is not None and parent.is_real_node():
			self.check_heights(parent)
		return

	def case31(self, node : AVLNode): # FIXME
		# Rotate to fix subtree
		if node.get_right().get_left().get_height() == node.get_right().get_right().get_height(): # CASE 2
			self.rotate_left(node) # heights updated inside rotate
			print_tree(self.root)
			return
		if node.get_right().get_left().get_height() + 1 == node.get_right().get_right().get_height(): # CASE 3
			node = self.rotate_left(node) # heights updated inside rotate
		elif node.get_right().get_left().get_height() == node.get_right().get_right().get_height() + 1: # CASE 4
			node = self.double_rotate_left(node) # heights updated inside rotate
		# Check parent for none and travel up
		parent = node.get_parent() if node is not None else None
		if parent is not None and parent.is_real_node():
			print_tree(self.root)
			self.check_heights(parent)
		return

	def case13(self, node : AVLNode): # FIXME
		# Rotate to fix subtree
		if node.get_left().get_right().get_height() == node.get_left().get_left().get_height(): # CASE 2 - symmetric
			self.rotate_left(node) # heights updated inside rotate
			return
		if node.get_left().get_right().get_height() + 1 == node.get_left().get_left().get_height(): # CASE 3 - symmetric
			node = self.rotate_right(node) # heights updated inside rotate
		elif node.get_left().get_right().get_height() == node.get_left().get_left().get_height() + 1: # CASE 4 - symmetric
			node = self.double_rotate_right(node) # heights updated inside rotate
		# Check parent for none and travel up
		parent = node.get_parent() if node is not None else None
		if parent is not None and parent.is_real_node():
			self.check_heights(parent)
		return

	def check_heights(self, node : AVLNode): # FIXME
		oldHeight = node.get_height()
		node.fields_update()
		left_height = node.get_left().get_height() if node.get_left() is not None else -1
		right_height = node.get_right().get_height() if node.get_right() is not None else -1
		
		if left_height == right_height and node.get_height == left_height + 2:
			self.case22(node)
		elif left_height == right_height + 2:
			self.case13(node)
		elif left_height + 2 == right_height:
			self.case31(node)
		elif oldHeight != node.get_height() and node.get_parent() is not None and node.get_parent().is_real_node():
			parent = node.get_parent()
			if parent is not None and parent.is_real_node():
				self.check_heights(parent)
		return
	
	# ----------------- MY JOIN -----------------
	"""joins self with item and another AVLTree

	@type tree2: AVLTree 
	@param tree2: a dictionary to be joined with self
	@type key: int 
	@param key: the key separting self and tree2
	@type val: string
	@param val: the value corresponding to key
	@pre: all keys in self are smaller than key and all keys in tree2 are larger than key,
	or the opposite way
	"""
	def join(self, tree2, key, val):
		# special cases - no root node
		if self.root is None or not self.root.is_real_node():
			if tree2.get_root() is None or not tree2.get_root().is_real_node():
				self.insert(key,val)
				return
			tree2.insert(key,val)
			self = tree2
			return
		elif tree2.get_root() is None:
			self.insert(key,val)
			return
		print(f"\nAFTER JOIN {key}:")
		print_tree(self.root)
		# both trees have a root node
		if self.root.get_key() < key:
			lower = self
			higher = tree2
		else:
			lower = tree2
			higher = self
		# Checking if they're the same height
		node = AVLNode(key, val)
		if lower.get_root().get_height() == higher.get_root().get_height():
			node.set_left(lower.get_root())
			node.set_right(higher.get_root())
			lower.get_root().set_parent(node)
			higher.get_root().set_parent(node)
			# node.update_height()
			# node.update_size()
			# TODO: organize
			node.fields_update()
			self.root = node
			return
		# Hights are different
		if lower.get_root().get_height() < higher.get_root().get_height():
			k = lower.get_root().get_height()
			b = higher.get_root()
			while b.get_height() > k:
				b = b.get_left()
			# add new node in place and update pointers
			node.set_left(lower.get_root())
			node.set_right(b)
			node.set_parent(b.get_parent())
			node.get_parent().set_left(node)
			b.set_parent(node)
			lower.get_root().set_parent(node)
			# update hights and rebalance using delete() aid functions
			# TODO: organize
			node.fields_update()
			self.set_root(higher.get_root())
			# self.check_heights(node)
		else:
			k = higher.get_root().get_height()
			b = lower.get_root()
			while b.get_height() > k:
				b = b.get_right()
			# add new node in place and update pointers
			node.set_right(higher.get_root())
			node.set_left(b)
			node.set_parent(b.get_parent())
			node.get_parent().set_right(node)
			b.set_parent(node)
			higher.get_root().set_parent(node)
			# update hights and rebalance using delete() aid functions
			# node.update_height()
			# TODO: organize
			node.fields_update()
			self.set_root(lower.get_root())
			# self.check_heights(node)
			# FIXME: balance like in insert() and not delete()
		self.rebalance_from_insert(node)

		print(f"\nAFTER JOIN {key}:")
		print_tree(self.root)

		return
# --------------- copied join(t, k, v) ---------------
	def join(self, t, k, v):
		if not t.get_root().is_real_node():
			self.insert(k, v)
			return

		if not self.get_root().is_real_node():
			self.set_root(t.get_root())
			self.tree_size = t.size()
			t.set_root(AVLNode(None, None))
			t.tree_size = 0
			self.insert(k, v)
			return

		t_max = t.max_node()
		s_min = self.min_node()
		if t_max and s_min and (t_max.get_key() < s_min.get_key()):
			t._bring_to_root(t_max)
			N = AVLNode(k, v)
			t_max.set_right(N)
			N.set_parent(t_max)
			if self.get_root().is_real_node():
				N.set_right(self.get_root())
				self.get_root().set_parent(N)
			t.tree_size += 1
			t.tree_size += self.tree_size

			z = N
			while z is not None:
				z.fields_update()
				if abs(z.get_bfs()) > 1:
					if z.get_bfs() == 2:
						if z.get_left().get_bfs() >= 0:
							t.rotate_right(z)
						else:
							t.double_rotate_right(z)
					else:
						if z.get_right().get_bfs() <= 0:
							t.rotate_left(z)
						else:
							t.double_rotate_left(z)
				z = z.get_parent()

			self.set_root(t.get_root())
			self.tree_size = t.tree_size
			t.set_root(AVLNode(None, None))
			t.tree_size = 0

		else:
			t_min = t.min_node()
			s_max = self.max_node()
			if t_min and s_max and (t_min.get_key() > s_max.get_key()):
				t._bring_to_root(t_min)
				N = AVLNode(k, v)
				t_min.set_left(N)
				N.set_parent(t_min)
				if self.get_root().is_real_node():
					N.set_left(self.get_root())
					self.get_root().set_parent(N)
				t.tree_size += 1
				t.tree_size += self.tree_size

				z = N
				while z is not None:
					z.fields_update()
					if abs(z.get_bfs()) > 1:
						if z.get_bfs() == 2:
							if z.get_left().get_bfs() >= 0:
								t.one_R_rotation(z)
							else:
								t.double_rotate_right(z)
						else:
							if z.get_right().get_bfs() <= 0:
								t.rotate_left(z)
							else:
								t.double_rotate_left(z)
					z = z.get_parent()

				self.set_root(t.get_root())
				self.tree_size = t.tree_size
				t.set_root(AVLNode(None, None))
				t.tree_size = 0
			else:
				raise ValueError("join: 't' not strictly < or > 'self'.")

	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node): # FINAL
		h = self.get_root().get_height()
		if h < 1:
			return AVLTree(), AVLTree()
		print("Height is: ",h)
		smallerTrees = []
		smallerNodes = []
		biggerTrees = []
		biggerNodes = []
		search = self.get_root()
		# Building arrays, of the bigger and smaller trees/nodes in the path from the root to our split node
		while search.get_key() != node.get_key():
			if node.get_key() < search.get_key():
				biggerNodes.append(search)
				biggerTrees.append(search.get_right()) 
				search = search.get_left()
			else:
				smallerNodes.append(search)
				smallerTrees.append(search.get_left()) 
				search = search.get_right()

		# notice the order of the arrays is reversed, so we can build the trees in the correct order
		# plus - the lengths of the arrays are the same, so we can iterate over them together

		if smallerTrees is not [] and node.get_left() is not None and node.get_left().is_real_node():
			smallerTrees.append(node.get_left())
		if biggerTrees is not [] and node.get_right() is not None and node.get_right().is_real_node():
			biggerTrees.append(node.get_right())

		print("smallerTrees IS = ",smallerTrees)
		print("smallerNodes IS = ",smallerNodes)
		print("BiggerTrees IS = ",biggerTrees)
		print("BiggerNodes IS = ",biggerNodes)

		subTree = AVLTree()
		# Now build the two trees from these arrays, in reverse order - to maintain small time complexity
		# Always - either trees amount = nodes amount, or trees amount = nodes amount + 1. Depends on the node's children
		small = AVLTree()

		# if len(smallerNodes) > 0:
		#     i = len(smallerNodes) - 1
		#     smallerNodes[i].set_right(node.get_left())
			

		if len(smallerTrees) > 0:
			i = len(smallerTrees) - 1
			small.set_root(smallerTrees[i]) 
			small.get_root().set_parent(None)
			while i > 0:
				subTree.root = smallerTrees[i-1]
				subTree.get_root().set_parent(None)
				small.join(subTree, smallerTrees[i-1].get_key(), smallerTrees[i-1].get_value())
				i-=1
			if small.get_root() is not None:
				small.get_root().set_parent(None)
			for node in smallerNodes:
				small.insert(node.get_key(), node.get_value())



		big = AVLTree()
		if len(biggerTrees) > 0:
			j = len(biggerTrees) - 1
			big.set_root(biggerTrees[j]) 
			big.get_root().set_parent(None)
			while j > 0:
				subTree.root = biggerTrees[j-1].get_right()
				subTree.get_root().set_parent(None)
				big.join(subTree, biggerTrees[j-1].get_key(), biggerTrees[j-1].get_value())
				j-=1
			if big.get_root() is not None:
				big.get_root().set_parent(None)
			for node in biggerNodes:
				big.insert(node.get_key(), node.get_value())


		return small, big

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self): # FINAL
		def inorder(n, arr):
			if n is None or not n.is_real_node():
				return
			inorder(n.get_left(), arr)
			arr.append((n.get_key(), n.get_value()))
			inorder(n.get_right(), arr)
		result = []
		inorder(self.get_root(), result)
		return result


	# TODO: test max_node()
	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self): # FINAL
		if self.root is None or not self.get_root().is_real_node():
			return None
		cur = self.get_root()
		while cur.get_right() is not None and cur.get_right().is_real_node():
			cur = cur.get_right()
		return cur


	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self): # FINAL
		return self.size	


	

# TODO: DELETE THIS - only for debugging
def print_tree(root, indent="", pointer="Root: "):
    if root is not None:
        print(indent + pointer + str(root.key))

        if root.left or root.right:
            if root.left:
                print_tree(root.left, indent + "    ", "L--- ")
            else:
                print(indent + "    L--- None")

            if root.right:
                print_tree(root.right, indent + "    ", "R--- ")
            else:
                print(indent + "    R--- None")
