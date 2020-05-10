class Queue:
	def __init__(self,inputlist=[]):
		self.items = inputlist.copy()

	def queueup(self, item):
		self.items.append(item)

	def queuedown(self):
		return self.items.pop(0)

	def length(self):
		return len(self.items)

	def isEmpty(self):
		if len(self.items) == 0:
			return True
		else:
			return False