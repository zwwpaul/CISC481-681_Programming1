import pancake as pk
import networkx as nx

G = nx.Graph()


def create_graph(p, g):
	p.set_next()
	p1 = p.cakelist[0]
	p2 = p.cakelist[1]
	p3 = p.cakelist[2]
	values = [p1.maximum, p2.maximum, p3.maximum]
	if not g.has_node(p.maximum):
		g.add_node(p.maximum)
	if 4321 not in values:
		for i in p.cakelist:
			if not g.has_node(i.maximum):
				g.add_node(i.maximum)
			if not g.has_edge(p.maximum, i.maximum):
				g.add_edge(p.maximum, i.maximum, weight=i.g)
				create_graph(i, g)
	else:
		values.sort(reverse=True)
		if p1.maximum == values[0]:
			temp = p1
		elif p2.maximum == values[0]:
			temp = p2
		elif p3.maximum == values[0]:
			temp = p3
		G.add_node(temp.maximum)
		G.add_edge(p.maximum, values[0], weight=temp.g)


def create_pc(value):
	elements = []
	for c in str(value):
		elements.append(c)
	elements.append("u")
	temp = pk.Pancake(elements)
	temp.update_h()
	temp.g = 0
	temp.total_g = 0
	return temp


def ucs(self):
	create_graph(self, G)
	optimal_path = nx.shortest_path(G, source=self.maximum, target=4321)

	pcake_list = []
	for i in optimal_path:
		pcake_list.append(create_pc(i))
	k = 1
	while (k < len(optimal_path)):
		w = G.get_edge_data(optimal_path[k], optimal_path[k - 1])
		cost = w.get("weight")
		pcake_list[k].g += cost
		k += 1
	c = 0
	for i in pcake_list:
		c += i.g
		print_ucs(i, c)


def print_ucs(self, totalc):
	str_ucs = self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3]
	if str_ucs == "4321":
		print(self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (totalc) + " h=%d" %
		      self.h)
	else:
		if self.g == 4:
			print("|" + self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				totalc) + " h=%d" %
			      self.h)
		elif self.g == 3:
			print(self.elements[0] + "|" + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				totalc) + " h=%d" %
			      self.h)
		else:
			print(self.elements[0] + self.elements[1] + "|" + self.elements[2] + self.elements[3] + " g=%d" % (
				totalc) + " h=%d" %
			      self.h)


def add_path_ucs(self, maximum):
	if maximum not in self.path_dic_ucs:
		self.path_dic_ucs[maximum] = True;


# This function is to set all the attributes
# I'm trying to make all pancakes link together
# Find the shortest path by just calculating the total_g
def update(self):
	if self.maximum not in self.path_dic_ucs:
		temp2 = []
		temp3 = []
		temp4 = []
		temp2.append(self.elements[0])
		temp2.append(self.elements[1])
		temp2.append(self.elements[3])
		temp2.append(self.elements[2])
		num2 = int(temp2[0] + temp2[1] + temp2[2] + temp2[3])
		if num2 not in self.path_dic_ucs:
			p2 = pk.Pancake(temp2[0] + temp2[1] + temp2[2] + temp2[3] + "u")
			p2.maximum = num2
			p2.parent = self
			self.left = p2
			p2.g = 2
			p2.total_g = self.total_g + p2.g
			p2.path_dic_ucs = self.path_dic_ucs
			add_path_ucs(p2, p2.maximum)
			p2.update_h()

		temp3.append(self.elements[0])
		temp3.append(self.elements[3])
		temp3.append(self.elements[2])
		temp3.append(self.elements[1])
		num3 = int(temp3[0] + temp3[1] + temp3[2] + temp3[3])
		if num3 not in self.path_dic_ucs:
			p3 = pk.Pancake(temp3[0] + temp3[1] + temp3[2] + temp3[3] + "u")
			p3.maximum = num3
			p3.parent = self
			self.mid = p3
			p3.g = 3
			p3.total_g = self.total_g + p3.g
			p3.path_dic_ucs = self.path_dic_ucs
			add_path_ucs(p3, p3.maximum)
			p3.update_h()

		temp4.append(self.elements[3])
		temp4.append(self.elements[2])
		temp4.append(self.elements[1])
		temp4.append(self.elements[0])
		num4 = int(temp4[0] + temp4[1] + temp4[2] + temp4[3])
		if num4 not in self.path_dic_ucs:
			p4 = pk.Pancake(temp4[0] + temp4[1] + temp4[2] + temp4[3] + "u")
			p4.maximum = num4
			p4.parent = self
			self.mid = p4
			p4.g = 4
			p4.total_g = self.total_g + p4.g
			p4.path_dic_ucs = self.path_dic_ucs
			add_path_ucs(p4, p4.maximum)
			p4.update_h()
