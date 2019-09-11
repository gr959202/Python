class Node:
	def __init__ (self,val):
		self.value = val
		self.left = None
		self.right = None
	def insert(self,data):
		if self.value == data:
			return False
		elif self.value > data:
			if self.left:
				return self.left.insert(data)
			else:
				self.left = Node(data)
				return True
		else:
			if self.right:
				return self.right.insert(data)
			else:
				self.right = Node(data)
	def find(self,data):
		if self.value == data:
			return True
		elif self.value > data:
			if self.left:
				return self.left.find(data)
			else:
				return False
		else:
			if self.right:
				return self.right.find(data)
			else:
				return False			
	def preorder(self):
		if self:
			print(str(self.value))
			if self.left:
				self.left.preorder()
			if self.right:
				self.right.preorder()
	def postorder(self):
		if self:
			if self.left:
				self.left.postorder()
			if self.right:
				self.right.postorder()
			print(str(self.value))
	def inorder(self):
		if self:
			if self.left:
				self.left.postorder()
			print(str(self.value))
			if self.right:
				self.right.postorder()



###Inside Class Tree, we are going to call the methods associated with Class Node. We can do this with the help of Dot(.) operator. In the following code, we have called insert,find,preorder,postorder methods from Node class inside Tree class.  
##pre-order traversal is Root, Left, Right
##post-order traversal is Left,Right,Root
##In-order traversal is Left, Root, Right

class tree:
	def __init__ (self):
		self.root = None
	def insert(self,data):
		if self.root:
			return self.root.insert(data)
		else:
			self.root = Node(data)
			return True
	def find(self,data):
		if self.root:
			return self.root.find(data)
		else:
			return False
	def preorder(self):
		print("Preorder")
		self.root.preorder()
	def postorder(self):
		print("Postorder")
		self.root.postorder()
	def inorder(self):
		print("Inorder")
		self.root.inorder()

bst = tree()
bst.insert(14)
bst.insert(11)
bst.insert(17)
bst.insert(8)
bst.insert(12)
bst.preorder()
bst.postorder()
bst.inorder()
