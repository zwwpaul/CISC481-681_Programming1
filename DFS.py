# Based on the value of g, change the order
def compare_update(self):
	self.h = 4;
	temp = []
	temp2 = []
	temp3 = []
	temp4 = []
	temp2.append(self.elements[0])
	temp2.append(self.elements[1])
	temp2.append(self.elements[3])
	temp2.append(self.elements[2])
	num2 = int(temp2[0] + temp2[1] + temp2[2] + temp2[3])
	temp.append(num2)
	temp3.append(self.elements[0])
	temp3.append(self.elements[3])
	temp3.append(self.elements[2])
	temp3.append(self.elements[1])
	num3 = int(temp3[0] + temp3[1] + temp3[2] + temp3[3])
	temp.append(num3)
	temp4.append(self.elements[3])
	temp4.append(self.elements[2])
	temp4.append(self.elements[1])
	temp4.append(self.elements[0])
	num4 = int(temp4[0] + temp4[1] + temp4[2] + temp4[3])
	temp.append(num4)
	self.maximum = max(temp)
	if self.maximum == num2:
		self.g = 2
		self.elements = temp2
	elif self.maximum == num3:
		self.g = 3
		self.elements = temp3
	elif self.maximum == num4:
		self.g = 4
		self.elements = temp4

	if self.maximum in self.visited:
		if self.maximum == num2:
			if num3 > num4:
				self.maximum = num3
				self.g = 3
				self.elements = temp3
			else:
				self.maximum = num4
				self.g = 4
				self.elements = temp4
			if self.maximum in self.visited:
				if self.maximum == num3:
					self.maximum = num4
					self.g = 4
					self.elements = temp4
				else:
					self.maximum = num3
					self.g = 3
					self.elements = temp3

		elif self.maximum == num3:
			if num2 > num4:
				self.maximum = num2
				self.g = 2
				self.elements = temp2
			if self.maximum in self.visited:
				if self.maximum == num2:
					self.maximum = num4
					self.g = 4
					self.elements = temp4
				else:
					self.maximum = num2
					self.g = 2
					self.elements = temp2

		elif self.maximum == num4:
			if num2 > num3:
				self.maximum = num2
				self.g = 2
				self.elements = temp2
			if self.maximum in self.visited:
				if self.maximum == num2:
					self.maximum = num3
					self.g = 3
					self.elements = temp3
				else:
					self.maximum = num2
					self.g = 2
					self.elements = temp2

	self.total_g = self.total_g + self.g
	add_path(self)


# Add the path to dictionary
def add_path(self):
	if self.maximum not in self.path_dic_dfs:
		self.path_dic_dfs.append(self.maximum)


def print_dfs(self):
	str_dfs = self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3]
	if str_dfs == "4321":
		print(self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
			self.total_g) + " h=%d" %
		      self.h)
	else:
		if self.g == 4:
			print("|" + self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				self.total_g) + " h=%d" %
			      self.h)
		elif self.g == 3:
			print(self.elements[0] + "|" + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				self.total_g) + " h=%d" %
			      self.h)
		else:
			print(self.elements[0] + self.elements[1] + "|" + self.elements[2] + self.elements[3] + " g=%d" % (
				self.total_g) + " h=%d" %
			      self.h)
