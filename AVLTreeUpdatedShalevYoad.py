import random



"""
A class representing a node in an AVL tree
(with tree-level size, no per-node size).
"""

class AVLNode(object):
    """Constructor, you are allowed to add more fields.
    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """
    def __init__(self, key, value):
        if key is not None:  # creating a real node
            self.key = key
            self.value = value
            self.left = AVLNode(None, None)
            self.right = AVLNode(None, None)
            self.parent = None
            self.height = -1
            self.bfs = 0
        else:  # creating a virtual node
            self.key = None
            self.value = None
            self.left = None
            self.right = None
            self.parent = None
            self.height = -1
            self.bfs = 0

    # --------------- Getters & Setters ---------------
    def get_key(self):
        return self.key

    def set_key(self, new_key):
        self.key = new_key

    def get_value(self):
        return self.value

    def set_value(self, new_value):
        self.value = new_value

    def get_left(self):
        return self.left

    def set_left(self, node):
        self.left = node

    def get_right(self):
        return self.right

    def set_right(self, node):
        self.right = node

    def get_parent(self):
        return self.parent

    def set_parent(self, node):
        self.parent = node

    def get_height(self):
        return self.height

    def set_height(self, h):
        self.height = h

    def get_bfs(self):
        return self.bfs

    def set_bfs(self, b):
        self.bfs = b

    def is_real_node(self):
        return (self.key is not None)

    """fields_update: Recompute (height, bfs) for this node in O(1)."""
    def fields_update(avl_node):
        if avl_node.get_left() is not None and avl_node.get_left().is_real_node():
            left_h = avl_node.get_left().get_height()
        else:
            left_h = -1
        if avl_node.get_right() is not None and avl_node.get_right().is_real_node():
            right_h = avl_node.get_right().get_height()
        else:
            right_h = -1

        avl_node.set_height(1 + max(left_h, right_h))
        avl_node.set_bfs(left_h - right_h)

    """ Right rotation around avl_node. O(1). Updates BFS & height. """
    def right_rotation(avl_node):
        B = avl_node
        A = avl_node.get_left()

        B.set_left(A.get_right())
        if A.get_right().is_real_node():
            A.get_right().set_parent(B)

        A.set_right(B)
        A.set_parent(B.get_parent())
        if A.get_parent() is not None:
            # re-link parent's child
            if A.get_parent().get_left() == B:
                A.get_parent().set_left(A)
            else:
                A.get_parent().set_right(A)
        B.set_parent(A)

        B.fields_update()
        A.fields_update()

    """ Left rotation around avl_node. O(1). Updates BFS & height. """
    def left_rotation(avl_node):
        B = avl_node
        A = avl_node.get_right()

        B.set_right(A.get_left())
        if A.get_left().is_real_node():
            A.get_left().set_parent(B)

        A.set_left(B)
        A.set_parent(B.get_parent())
        if A.get_parent() is not None:
            if A.get_parent().get_left() == B:
                A.get_parent().set_left(A)
            else:
                A.get_parent().set_right(A)
        B.set_parent(A)

        B.fields_update()
        A.fields_update()

    def set_right_with_parents(self,node):
        self.right = node
        if node is not None:
            node.set_parent(self)
        return None

    def set_left_with_parents(self,node):
        self.left = node
        node.set_parent(self)
        return None
    

class AVLTree(object):
    """
    A class implementing an AVL tree, with a single integer 'tree_size'
    tracking how many real nodes are in the entire tree.
    """

    def __init__(self):
        self.root = AVLNode(None, None)  # starts as a virtual root
        self.tree_size = 0

    def get_root(self):
        return self.root

    def set_root(self, r):
        self.root = r

    def size(self):
        return self.tree_size

    # --------------- COPIED search() ---------------

    # def search(self, key):
        x = self.get_root()
        depth = 0
        while x is not None and x.is_real_node():
            depth += 1
            if key == x.get_key():
                return x, depth + 1
            elif key < x.get_key():
                x = x.get_left()
            else:
                x = x.get_right()
        return None, -1

    #The helper function:
	#Here we used the similar method to the well known algorithem "Binary Search".
    def search_helper(self,node,key,depth):
        # Base case1:
        if node is None or not node.is_real_node():
            return None, depth - 1
        # Base case2:
        if node.get_key() == key:
            return node, depth
        # Since AVL is kind of a binary search tree, we used the fact that the keys of the left side of the tree are smaller than the node's key,
        # also the right side is bigger.
        if key < node.get_key():
            return self.search_helper(node.get_left(), key, depth + 1)
        else:
            return self.search_helper(node.get_right(), key, depth + 1)
        
    def search(self, key):
        #We used helper function - Search_helper.
        #We passed 1 as the value of the depth since we have been asked to return the length of the search route + 1.
        #We understand that in AVL trees, the depth of a node is the same as the searching route to the node. 
        print("\nBEFORE SEARCH:")
        print_tree(self.root)
        return self.search_helper(self.root,key,1)
        
    # ---------------  OUR search() ---------------
        
    def insert_as_leaf(self, avl_node_1):
        e = 0
        if self.get_root() is None or not self.get_root().is_real_node():
            self.set_root(avl_node_1)
            avl_node_1.set_height(0)
            avl_node_1.get_left().set_parent(avl_node_1)
            avl_node_1.get_right().set_parent(avl_node_1)
            self.tree_size += 1
            return e

        y = None
        x = self.get_root()
        while x.is_real_node():
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

    def rebalance_from_insert(self, z):
        height_change_counter = 0
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
                        z = self.rotate_right(z)
                    else:
                        z = self.double_rotate_right(z)
                else:
                    if z.get_right().get_bfs() <= 0:
                        z = self.rotate_left(z)
                    else:
                        z = self.double_rotate_left(z)
        return height_change_counter

    def insert(self, key, val):
        new_node = AVLNode(key, val)
        e = self.insert_as_leaf(new_node)

        print(f"\nAFTER INSERT {key}:")
        print_tree(self.root)

        z = new_node.get_parent()
        # Rebalancing the tree:
        height_change_counter =  self.rebalance_from_insert(z)
        print(f"\nAFTER INSERT {key}:")
        print_tree(self.root)
        return (new_node, e, height_change_counter)

    def one_R_rotation(self, z):
        if self.get_root().is_real_node() and self.get_root().get_key() == z.get_key():
            self.set_root(z.get_left())
        z.right_rotation()

    def one_L_rotation(self, z):
        if self.get_root().is_real_node() and self.get_root().get_key() == z.get_key():
            self.set_root(z.get_right())
        z.left_rotation()

    def L_rotation_R_rotation(self, z):
        self.one_L_rotation(z.get_left())
        self.one_R_rotation(z)

    def R_rotation_L_rotation(self, z):
        self.one_R_rotation(z.get_right())
        self.one_L_rotation(z)

    def avl_to_array(self):
        def inorder(n, arr):
            if n is None or not n.is_real_node():
                return
            inorder(n.get_left(), arr)
            arr.append((n.get_key(), n.get_value()))
            inorder(n.get_right(), arr)
        result = []
        inorder(self.get_root(), result)
        return result

    def min_node(self):
        if not self.get_root().is_real_node():
            return None
        cur = self.get_root()
        while cur is not None and cur.get_left().is_real_node():
            cur = cur.get_left()
        return cur

    def max_node(self):
        if not self.get_root().is_real_node():
            return None
        cur = self.get_root()
        while cur is not None and cur.get_right().is_real_node():
            cur = cur.get_right()
        return cur

    def _bring_to_root(self, x):
        while x is not None and x != self.get_root() and x.get_parent() is not None:
            p = x.get_parent()
            if p.get_left() == x:
                if self.get_root() == p:
                    self.set_root(x)
                p.right_rotation()
            else:
                if self.get_root() == p:
                    self.set_root(x)
                p.left_rotation()

    # --------------------- NEW finger_search(k) ---------------------
    def finger_search(self, key):
        """
        Search for a node with 'key' starting from the max node.
        Return (x, e): x is the found node (None if not found),
                       e is the number of edges in the search route.
        """

        # 1) If tree is empty => (None, 0)
        max_n = self.max_node()
        if max_n is None or max_n.is_real_node() is False:
            return (None, 0)

        e = 0  # number of edges traveled so far
        # 2) If key > max_n.key => not in tree => (None, e)
        if key > max_n.get_key():
            return (None, e)

        # 3) If key == max_n.key => found => (max_n, e)
        if key == max_n.get_key():
            return (max_n, e)

        # 4) Otherwise, key < max_n.key
        #    Climb up while parent's key >= key
        current = max_n
        while (current.get_parent() is not None
               and current.get_parent().is_real_node()
               and current.get_parent().get_key() >= key):
            current = current.get_parent()
            e += 1

        # 5) Now do a normal BST-like search downward from 'current'
        node_found, down_edges = self._search_from_node(current, key, 0)
        # total edges is e (climb up) + down_edges (BST descent)
        total_edges = e + down_edges
        return (node_found, total_edges)

    def _search_from_node(self, start_node, key, edges):
        """ 
        Recursive BST-style search from 'start_node', 
        returning (found_node, edges_used).
        'edges' is how many edges we've traveled so far.
        """
        if not start_node.is_real_node():
            return (None, edges)
        if key == start_node.get_key():
            return (start_node, edges)
        elif key < start_node.get_key():
            return self._search_from_node(start_node.get_left(), key, edges+1)
        else:
            return self._search_from_node(start_node.get_right(), key, edges+1)


    def rotate_left(self, x : AVLNode):
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

        # 3) Update heights (and sizes if you track those) for z and then y
        # z.update_height()
        # z.update_size()
        # y.update_height()
        # y.update_size()
        # TODO: organize

        x.fields_update()
        y.fields_update()

        return y

    def rotate_right(self, y : AVLNode):
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

        # z.update_height()
        # z.update_size()
        # y.update_height()
        # y.update_size()
        # TODO: organize
        x.fields_update()
        y.fields_update()
        # If you track subtree sizes, update those as well
        return x

    def double_rotate_left(self, y : AVLNode):
        x = self.rotate_right(y.get_right())
        z = self.rotate_left(y)
        return z


    # TODO: test DRR
    def double_rotate_right(self, y : AVLNode):
        x = self.rotate_left(y.get_left())
        z = self.rotate_right(y)
        return z

    # --------------------- NEW Delete() ---------------------

    def delete(self, node):
        if (node.get_left() is not None and node.get_right() is not None
            and node.get_left().is_real_node() and node.get_right().is_real_node()):
            # node isn't a leaf nor a unary node
            pre = self.predecessor(node)
            suc = self.successor(node)
            # one of them has to be a leaf or a unary node
            if (pre.get_left() is None or pre.get_right() is None
                or pre.get_left().is_real_node() or pre.get_right().is_real_node()):
                self.switch_two_nodes(node, pre) # switches node with predecessor and updates heights/sizes
            elif (suc.get_left() is None or suc.get_right() is None
                  or suc.get_left().is_real_node() or suc.get_right().is_real_node()):
                self.switch_two_nodes(node, suc) # switches node with successor and updates heights/sizes
        
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
            if node.get_key() < parent.get_key():
                # node is a left leaf
                parent.set_left_with_parents(AVLNode(None, None)) # detach
                self.tree_size -= 1
            else:
                # node is a right leaf
                parent.set_right_with_parents(AVLNode(None, None)) # detach
                self.tree_size -= 1
        else:
            # node is unary
            child = node.get_right() if node.get_right() is not None else node.get_left()
            # if parent is None: # the tree is only node and his single child
            if self.get_root() is node: # the tree is only node and his single child
                self.root = child
                self.tree_size -= 1
                self.root.set_parent(None)
                print(f"\nAFTER DELETION of {node.get_key()}:")
                print_tree(self.root)
                return
            if node.get_key() < parent.get_key():
                # node is a left unary
                self.tree_size -= 1
                parent.set_left_with_parents(child)
            else:
                # node is a right unary
                self.tree_size -= 1
                parent.set_right_with_parents(child)

        # parent.update_height()
        # TODO: organize
        parent.fields_update()
        print("\nBEFORE BALANCE:")
        print_tree(self.root)
        self.check_heights(parent)		
        
        print("\nAFTER BALANCE:")
        print_tree(self.root)
        return	
        

    def case22(self, node : AVLNode):
        # Travel up the tree
        parent = node.get_parent()
        if parent is not None and parent.is_real_node():
            self.check_heights(parent)
        return
        

    def case31(self, node : AVLNode):
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

        
    def case13(self, node : AVLNode):
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


    def check_heights(self, node : AVLNode):
        node.fields_update()
        left_height = node.get_left().get_height() if node.get_left() is not None else -1
        right_height = node.get_right().get_height() if node.get_right() is not None else -1
        
        if left_height == right_height and node.get_height == left_height + 2:
            self.case22(node)
        elif left_height == right_height + 2:
            self.case13(node)
        elif left_height + 2 == right_height:
            self.case31(node)
        return

    def successor(self, node : AVLNode):
            # end cases
            if node is None or not node.is_real_node():
                return None
            # if we dont have right child we start going upwards:
            if node.get_right() is None or not node.get_right().is_real_node():
                if node.get_parent is not None:
                    while node.get_parent().get_key() < node.get_key():
                        node = node.get_parent()
                    if node.get_parent() is None or not node.get_parent().is_real_node():
                        return None
                    return node.get_parent()
                else:
                    return None
            # if we have right child:
            node = node.get_right()
            while node is not None and node.get_left() is not None and node.is_real_node() and node.get_left().is_real_node():
                node = node.get_left()
            return node

    def switch_two_nodes(self, node1, node2):
        nodeP = node1.get_parent()
        nodeR = node1.get_right()
        nodeL = node1.get_left()
        
        node1.set_parent(node2.get_parent())
        node1.set_right(node2.get_right())
        node1.set_left(node2.get_left())
        
        node2.set_parent(nodeP)
        node2.set_right(nodeR)
        node2.set_left(nodeL)
        
        # node1.update_height()
        # node1.update_size()
        # node2.update_size()
        # node2.update_height()
        # TODO: organize
        node1.fields_update()
        node2.fields_update()


    # TODO: test predecessor
    """ returns the predecessor of a given node, that's inside the tree """
    def predecessor(self, node : AVLNode):
        # end cases
        if node is None or not node.is_real_node():
            return None
        # return max of left subtree, if exists
        if node.get_left() is not None and node.get_left().is_real_node():
            node = node.get_left()
            while node is not None and node.get_right() is not None and node.is_real_node() and node.get_right().is_real_node():
                node = node.get_right()
            return node
        # left subtree doesnt exist, travel up the tree:
        if node.get_parent() is not None:
            while node.get_parent().get_key() > node.get_key():
                node = node.get_parent()
            if node.get_parent() is None or not node.get_parent().is_real_node():
                return None
            return node.get_parent()
        return None

    # --------------- finger_insert (from max node) ---------------
    def _finger_insert_as_leaf(self, start_node, new_node):
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

    def finger_insert(self, key, val):
        if not self.get_root().is_real_node():
            new_root = AVLNode(key, val)
            new_root.set_height(0)
            new_root.get_left().set_parent(new_root)
            new_root.get_right().set_parent(new_root)
            self.set_root(new_root)
            self.tree_size += 1
            print(f"\nAFTER FINGER INSERT {key}:")
            print_tree(self.root)
            return (new_root, 0, 0)

        maxn = self.max_node()
        e_up = 0
        current = maxn
        if key > maxn.get_key():
            pass  # no climb up
        else:
            while (current.get_parent() is not None 
                   and current.get_parent().is_real_node()
                   and current.get_parent().get_key() >= key):
                current = current.get_parent()
                e_up += 1

        new_node = AVLNode(key, val)
        e_down = self._finger_insert_as_leaf(current, new_node)
        e = e_up + e_down

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
        print(f"\nAFTER FINGER INSERT {key}:")
        print_tree(self.root)
        return (new_node, e, height_change_counter)
    
    # --------------- COPIED split(x) ---------------
    # def split(self, x):
    #     self._bring_to_root(x)
    #     left_sub = x.get_left()
    #     right_sub = x.get_right()
    #     if left_sub.is_real_node():
    #         left_sub.set_parent(None)
    #     if right_sub.is_real_node():
    #         right_sub.set_parent(None)
    #     if x.is_real_node():
    #         self.tree_size -= 1  # removing x from our tree
    #     self.set_root(AVLNode(None, None))
    #     self.tree_size = 0

    #     t1 = AVLTree()
    #     t1.set_root(left_sub)
    #     t1.tree_size = self._count_real_nodes(left_sub)

    #     c = AVLTree()
    #     c.set_root(right_sub)
    #     c.tree_size = self._count_real_nodes(right_sub)

    #     return (t1, c)

    def _count_real_nodes(self, node):
        if not node or not node.is_real_node():
            return 0
        return 1 + self._count_real_nodes(node.get_left()) + self._count_real_nodes(node.get_right())

    # --------------- MY SPLIT() ---------------
    def split(self, node):
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
    # --------------- copied join(t, k, v) ---------------
    # def join(self, t, k, v):
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

# --------------- my join(t, k, v) ---------------
# ------------------ TESTER FOR MAIN FUNCTIONS ------------------
def test_main_functions(AVLTreeClass):
    """
    A test suite covering:
      - standard insert
      - split
      - join
      - finger_search
      - finger_insert
    (delete is not included here, but can be added if you implement it.)

    We'll do multiple scenarios, print the results, 
    and check BFS in [-1,0,1], in-order sorting, and size consistency.
    """

    print("\n========== START MAIN FUNCTIONS TEST SUITE ==========")

    # Helper to validate BFS, in-order, and size.
    def check_tree_validity(tree, label):
        # 1) check sorted in-order
        arr = tree.avl_to_array()
        keys = [item[0] for item in arr]
        if keys != sorted(keys):
            print(f"  [FAIL] {label}: in-order not sorted => {arr}")
        else:
            print(f"  [OK] {label}: in-order sorted => {arr}")

        # 2) BFS check
        bad_nodes = []
        def check_bfs(node):
            if not node.is_real_node():
                return
            bfs = node.get_bfs()
            if abs(bfs) > 1:
                bad_nodes.append((node.get_key(), bfs))
            check_bfs(node.get_left())
            check_bfs(node.get_right())
        check_bfs(tree.get_root())
        if bad_nodes:
            print(f"  [FAIL] {label}: BFS out of [-1,0,1] => {bad_nodes}")
        else:
            print(f"  [OK] {label}: all BFS in [-1,0,1]")

        # 3) size check
        if len(arr) != tree.size():
            print(f"  [FAIL] {label}: tree.size()={tree.size()} but in-order has {len(arr)}.")
        else:
            print(f"  [OK] {label}: size() = {tree.size()}")

    # SCENARIO A: Basic insert, finger_insert, finger_search
    print("\n[SCENARIO A] Insert & Finger Insert & Finger Search")
    treeA = AVLTreeClass()
    normal_keys = [10, 5, 15, 3, 7, 12, 18]
    for k in normal_keys:
        treeA.insert(k, f"val{k}")
    print("  Inserted normal keys =>", normal_keys)
    check_tree_validity(treeA, "A after normal insert")

    finger_keys = [6, 8, 16]
    for k in finger_keys:
        treeA.finger_insert(k, f"val{k}")
    print("  Finger-inserted =>", finger_keys)
    check_tree_validity(treeA, "A after finger insert")

    # finger_search
    print("\n  Checking finger_search on existing & non-existing keys:")
    search_tests = [5, 8, 17, 20]
    for s in search_tests:
        node_found, edges = treeA.finger_search(s)
        if node_found is not None:
            print(f"   finger_search({s}) => found node key={node_found.get_key()}, edges={edges}")
        else:
            print(f"   finger_search({s}) => None, edges={edges}")

    # SCENARIO B: Split
    print("\n[SCENARIO B] Splitting treeA around key=10")
    node_10 = treeA.search(10)[0]
    if node_10 is None:
        print("  [FAIL] key=10 not found, cannot split!")
    else:
        t1, c = treeA.split(node_10)
        print("  => After split at key=10 (discard 10).")
        print("  t1 in-order:", t1.avl_to_array())
        print("  c in-order:", c.avl_to_array())
        check_tree_validity(t1, "B t1")
        check_tree_validity(c, "B c")

        # SCENARIO C: Join them back with new node key=10
        print("\n[SCENARIO C] Join t1 & c with new node key=10")
        mx_t1 = t1.max_node()
        mn_c = c.min_node()
        if mx_t1 and mn_c and mx_t1.get_key() < mn_c.get_key():
            c.join(t1, 10, "val10")
            joined = c
        else:
            t1.join(c, 10, "val10")
            joined = t1
        check_tree_validity(joined, "C joined after re-join")
        print("  => joined in-order:", joined.avl_to_array())

    # SCENARIO D: Another small join scenario
    print("\n[SCENARIO D] Another join scenario with disjoint sets")
    leftT = AVLTreeClass()
    for k in [1,2,3,4]:
        leftT.insert(k, f"val{k}")
    rightT = AVLTreeClass()
    for k in [10,11,12,13]:
        rightT.insert(k, f"val{k}")

    print("  leftT =>", leftT.avl_to_array())
    print("  rightT =>", rightT.avl_to_array())
    print("  We'll join leftT < rightT with a new node key=7")
    if leftT.max_node().get_key() < rightT.min_node().get_key():
        rightT.join(leftT, 7, "val7")
        merged = rightT
    else:
        leftT.join(rightT, 7, "val7")
        merged = leftT
    check_tree_validity(merged, "D merged")
    print("  => merged in-order:", merged.avl_to_array())

    # SCENARIO E: random finger_inserts, then split & join
    print("\n[SCENARIO E] random finger_inserts, then split & join")
    random_tree = AVLTreeClass()
    random_keys = random.sample(range(20, 41), 8)
    for rk in random_keys:
        random_tree.finger_insert(rk, f"val{rk}")
    print("  => finger-inserted random keys:", random_keys)
    check_tree_validity(random_tree, "E random tree")

    # We'll split around the median
    median_key = sorted(random_keys)[len(random_keys)//2]
    node_med = random_tree.search(median_key)[0]
    if node_med:
        leftS, rightS = random_tree.split(node_med)
        print(f"  => after split at median {median_key}, leftS =>", leftS.avl_to_array(), 
              " rightS =>", rightS.avl_to_array())
        check_tree_validity(leftS, "E leftS")
        check_tree_validity(rightS, "E rightS")

        # rejoin with median_key
        if leftS.max_node() and rightS.min_node() and leftS.max_node().get_key() < rightS.min_node().get_key():
            rightS.join(leftS, median_key, f"val{median_key}")
            final_tree = rightS
        else:
            leftS.join(rightS, median_key, f"val{median_key}")
            final_tree = leftS
        check_tree_validity(final_tree, "E final rejoin")
        print("  => final rejoin in-order:", final_tree.avl_to_array())
    else:
        print(f"  [FAIL] median_key={median_key} not found => can't split")
    print_tree(final_tree.get_root())

    print("\n========== END MAIN FUNCTIONS TEST SUITE ==========\n")


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

# ------------------ RUN TESTS IF MAIN ------------------
if __name__ == "__main__":
    test_main_functions(AVLTree)
