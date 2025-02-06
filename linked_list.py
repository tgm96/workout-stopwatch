class Node:
	data = None
	next_node = None 

	def __init__(self, data):
		self.data = data

	def __repr__(self):
		return "<Node data: %s>" % self.data

	def store_data(self):
		return self.data

class LinkedList:

	def __init__(self):
		self.head = None 

	def is_empty(self):
		return self.head == None 

	def size(self):
		current = self.head
		count = 0

		while current:
			count += 1
			current = current.next_node

		return count


	def add(self, data):
		new_node = Node(data)
		new_node.next_node = self.head
		self.head = new_node


	def add_last(self, data):
		"""adds a node as the tail of the linked list"""

		new_node = Node(data)
		current = self.head

		if not current:
			self.add(data)
		else:
			while current.next_node:
				current = current.next_node

			current.next_node = new_node


	def search(self, key):
		"""returns the first node containing the data. Returns None if no match"""

		current = self.head

		while current:
			if current.data == key:
				return current
			else:
				current = current.next_node
		return None


	def insert(self, data, index):
		if index == 0:
			self.add(data)

		if index > 0:
			new = Node(data)
			
			position = index
			current = self.head

			while position > 1:
				current = current.next_node
				position -= 1

			prev_node = current
			next_node = current.next_node

			prev_node.next_node = new 
			new.next_node = next_node


	def remove(self, key):
		current = self.head
		previous = None 
		found = False

		while current and not found:
			if current.data == key and current == self.head:
				found = True
				self.head = current.next_node
			elif current.data == key:
				found = True
				previous.next_node = current.next_node
			else:
				previous = current
				current = current.next_node

		return current


	def remove_index(self, index):
		"""removes element at given index"""

		current = self.head
		previous = None
		position = index

		if index == 0:
			self.head = current.next_node
		
		if index > 0:
			while position > 1:
				current = current.next_node
				position -= 1

			previous = current

			if current.next_node == None:
				previous.next_node == None
			else:
				current = current.next_node
				previous.next_node = current.next_node


	def display_index(self, index):
		
		current = self.head
		position = index

		if index == 0:
			return current

		if index > 0:
			while position > 0:
				current = current.next_node
				position -= 1

			return current

	def store_index(self, index):
		
		current = self.head
		position = index

		if index == 0:
			return current.store_data()

		if index > 0:
			while position > 0:
				current = current.next_node
				position -= 1

			return current.store_data()

	def wipe_list(self):

		if self.is_empty() == None:
			return None

		self.head = None 
		

	def __repr__(self):

		nodes = []
		current = self.head

		while current:
			if current is self.head:
				nodes.append("[Head: %s]" % current.data)
			elif current.next_node is None:
				nodes.append("[Tail: %s]" % current.data)
			else:
				nodes.append("[%s]" % current.data)

			current = current.next_node
		return '-> '.join(nodes)


