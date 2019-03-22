class Pancake:
	def __init__(self, o):
		self.g = 0
		self.h = 0
		self.choice = o[4]
		self.elements = o
		self.maximum = int(self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3])
		self.length = len(o)
		self.path_dic_dfs =[]
		self.total_g = 0

		self.path_dic_ucs = {}
		self.root=None
		self.parent=None
		self.left=None
		self.mid=None
		self.right=None
		self.visited = []
		self.cakelist = []
		self.astar = 0

	# To eliminate all the element from the element list
	def clean_pancake(self):
		self.elements[:] = []

	# To check whether pancake has the same value
	def check_same(self):
		flag = False
		for i in range(0, len(self.elements) - 1):
			for j in range(i + 1, len(self.elements)):
				if self.elements[i] == self.elements[j]:
					return True
				else:
					flag = False
		return flag

	# To update the value of h
	def update_h(self):
		self.h = 4
		if self.elements[0] == "4":
			self.h = self.h - 1;
		if self.elements[1] == "3":
			self.h = self.h - 1;
		if self.elements[2] == "2":
			self.h = self.h - 1;
		if self.elements[3] == "1":
			self.h = self.h - 1;

	# To determine whether the process is end
	def is_end(self):
		if self.h == 0:
			return True
		else:
			return False

	def set_next(self):
		temp2 = []
		temp3 = []
		temp4 = []
		temp2.append(self.elements[0])
		temp2.append(self.elements[1])
		temp2.append(self.elements[3])
		temp2.append(self.elements[2])
		temp2.append(self.choice)
		p2=Pancake(temp2)
		p2.g=2
		self.cakelist.append(p2)
		temp3.append(self.elements[0])
		temp3.append(self.elements[3])
		temp3.append(self.elements[2])
		temp3.append(self.elements[1])
		temp3.append(self.choice)
		p3=Pancake(temp3)
		p3.g=3
		self.cakelist.append(p3)
		temp4.append(self.elements[3])
		temp4.append(self.elements[2])
		temp4.append(self.elements[1])
		temp4.append(self.elements[0])
		temp4.append(self.choice)
		p4=Pancake(temp4)
		p4.g=4
		self.cakelist.append(p4)