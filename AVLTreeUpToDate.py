#id1:
#name1:
#username1:
#id2:
#name2:
#username2:


"""A class represnting a node in an AVL tree"""

class AVLNode(object):
	"""Constructor, you are allowed to add more fields. 
	
	@type key: int
	@param key: key of your node
	@type value: string
	@param value: data of your node
	"""
	def __init__(self, key, value):
		self.key = key
		self.value = value
		self.left = None
		self.right = None
		self.parent = None
		self.height = -1
		self.size = 0
		

	"""returns whether self is not a virtual node 

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""
	def is_real_node(self):
		return self.key is not None
	
	def get_balance_F(self):
		return self.left.get_height()-self.right.get_height()

	#Getters
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
	
	#Setters
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
	def set_right_with_parents(self,node):
		self.right = node
		node.set_parent(self)
		return None
	
	def set_left(self, node):
		self.right = node
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
	
	def update_size(self):
		if not self.is_real_node():
			self.set_size(0)
			return
		left_size = self.get_left().get_size() if (self.get_left() and self.get_left().is_real_node()) else 0
		right_size = self.get_right().get_size() if (self.get_right() and self.get_right().is_real_node()) else 0

		new_size = 1 + left_size + right_size
		self.set_size(new_size)
	
	def update_height(self):
		if not self.is_real_node():
			self.set_height(-1)
			return
		left_height = self.get_left().get_height() if (self.get_left() and self.get_left().is_real_node()) else -1
		right_height = self.get_right().get_height() if (self.get_right() and self.get_right().is_real_node()) else -1

		new_height = 1 + max(left_height, right_height)
		self.set_height(new_height)
	
"""
A class implementing an AVL tree.
"""

class AVLTree(object):

	"""
	Constructor, you are allowed to add more fields.
	"""
	def __init__(self):
		self.root = None
		self.max_node = None
	"""searches for a node in the dictionary corresponding to the key (starting at the root)
        
	@type key: int
	@param key: a key to be searched
	@rtype: (AVLNode,int)
	@returns: a tuple (x,e) where x is the node corresponding to key (or None if not found),
	and e is the number of edges on the path between the starting node and ending node+1.
	"""

	def search(self, key):
		#We used helper function - Search_helper.
		#We passed 1 as the value of the depth since we have been asked to return the length of the search route + 1.
		#We understand that in AVL trees, the depth of a node is the same as the searching route to the node. 
		return self.search_helper(self.root,key,1)
	
	#The helper function:
	#Here we used the similar method to the well known algorithem "Binary Search".
	def search_helper(self,node,key,depth):
        #Base case1:
		if (node is None) or (not node.is_real_node()):
			return None, depth - 1
		#Base case2:
		if node.get_key() == key:
			return node, depth
		#Since AVL is kind of a binary search tree, we used the fact that the keys of the left side of the tree are smaller than the node's key, also the right side is bigger.
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
	#this function will help us maintain the max node filed
	def find_max_node(self):
		#If the tree is empty or the root isn't real, there's no max node
		if self.get_root() is None or not self.get_root().is_real_node():
			return None
		current = self.get_root()
		#Traverse right as long as there is a real right child
		while current.get_right().is_real_node():
			current = current.get_right()
		return current
    
    


	def finger_search(self, key):
		# If max_node is not set or is a virtual node, the tree is effectively empty
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
		current = self.max_node
		# Climb up while:
        #   1) there's a real parent,
        #   2) the parent's key >= the key we're searching,
        # because we might find a closer ancestor whose subtree could contain key
		while current.get_parent() is not None and current.get_parent().is_real_node() and current.get_parent().get_key() >= key:
			current = current.get_parent()
			up_steps += 1
		# Now perform a standard BST search starting at 'current'
		node_found, depth_down = self.search_helper(current, key, 1)
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
	def insert(self, key, val):
		# 1) If the tree is empty or the root is virtual, create a new root and return.
		if (self.root is None) or (not self.root.is_real_node()):
			new_root = AVLNode(key, val)
			new_root.set_height(0)
			new_root.set_size(1)

			# Create and link virtual children
			left_virtual = AVLNode(None, None)
			right_virtual = AVLNode(None, None)
			left_virtual.set_parent(new_root)
			right_virtual.set_parent(new_root)
			new_root.set_left_with_parents(left_virtual)
			new_root.set_right_with_parents(right_virtual)

			self.root = new_root
			self.max_node = new_root  # if you maintain a pointer to the max node

			# No edges traveled (0), no rotations (0)
			return new_root, 0, 0
		
		# 2) Otherwise, insert like a BST and track the number of edges.
		inserted_node, e = self.normal_insert_with_edges(key, val, self.root, 0)
		# Update max_node if needed
		if (self.max_node is None) or (key > self.max_node.get_key()):
			self.max_node = inserted_node
		# 3) Rebalance on the path up from the inserted node's parent, tracking rotations.
		promote_count = 0
		current = inserted_node.get_parent()

		while current is not None:
			current.update_height()
			current.update_size()

			balance_factor = current.get_balance_F()

			if balance_factor > 1:
				# Left-Heavy
				if current.get_left().get_balance_F() >= 0:
					# Left-Left
					self.rotate_right(current)
				else:
					self.rotate_left(current.get_left())
					self.rotate_right(current)
				promote_count += 1
			elif balance_factor < -1:
				# Right-Heavy
				if current.get_right().get_balance_F() <= 0:
					# Right-Right
					self.rotate_left(current)
				else:
					# Right-Left
					self.rotate_right(current.get_right())
					self.rotate_left(current)
				promote_count += 1
			current = current.get_parent()
		# 4) Return (x, e, h) per your assignment specs.
		return inserted_node, e, promote_count
		 
		





	def normal_insert(self, key, val, node):
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
		
	def normal_insert_with_edges(self, key, val, node, e):
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
	def rotate_left(self,z):
		# y is z's right child
		y = z.get_right()
		# T2 is y's left subtree
		T2 = y.get_left()
		# 1) Rotate
		# Put T2 as z's right subtree
		z.set_right_with_parents(T2)
		# Put z as y's left subtree
		y.set_left_with_parents(z)
		# 2) Update y's parent to z's old parent
		parent_of_z = z.get_parent()
		y.set_parent(parent_of_z)
		if parent_of_z is not None:
			# If z was a left child of its parent, link y as that parent's new left child
			if parent_of_z.get_left() == z:
				parent_of_z.set_left_with_parents(y)
			else:
				parent_of_z.set_right_with_parents(y)
		else:
			# z was the root, so now y becomes the root
			self.root = y
		# 3) Update heights (and sizes if you track those) for z and then y
		z.update_height()
		z.update_size()
		y.update_height()
		y.update_size()

		return y
	
	def rotate_right(self,z):
		y = z.get_left()
		T2 = y.get_right()

		z.set_left_with_parents(T2)
		y.set_right_with_parents(z)

		parent_of_z = z.get_parent()
		y.set_parent(parent_of_z)
		if parent_of_z is not None:
			# If z was the left or right child, re-link
			if parent_of_z.get_left() == z:
				parent_of_z.set_left_with_parents(y)
			else:
				parent_of_z.set_right_with_parents(y)
		else:
			self.root = y
		z.update_height()
		z.update_size()
		y.update_height()
		y.update_size()
		# If you track subtree sizes, update those as well
		return y


	

	def finger_insert(self, key, val):
		return None, -1, -1


	"""deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	"""
	def delete(self, node):
		return	

	
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
		return


	"""splits the dictionary at a given node

	@type node: AVLNode
	@pre: node is in self
	@param node: the node in the dictionary to be used for the split
	@rtype: (AVLTree, AVLTree)
	@returns: a tuple (left, right), where left is an AVLTree representing the keys in the 
	dictionary smaller than node.key, and right is an AVLTree representing the keys in the 
	dictionary larger than node.key.
	"""
	def split(self, node):
		return None, None

	
	"""returns an array representing dictionary 

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""
	def avl_to_array(self):
		tree_lst = []
		if self.root is None:
			return tree_lst
		self.avl_to_array_rec(self.root,tree_lst)
		return tree_lst
	
	def avl_to_array_rec(self,node,lst):
		if node is None:
			return None
		else:
			self.avl_to_array_rec(node.left, lst)
			lst.append((node.key, node.value))
			self.avl_to_array_rec(node.right, lst)


	"""returns the node with the maximal key in the dictionary

	@rtype: AVLNode
	@returns: the maximal node, None if the dictionary is empty
	"""
	def max_node(self):
		return None

	"""returns the number of items in dictionary 

	@rtype: int
	@returns: the number of items in dictionary 
	"""
	def size(self):
		return self.size	


	"""returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""
	def get_root(self):
		return self.root



