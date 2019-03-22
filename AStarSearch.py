import pancake as pk


def astar(p, visited, c):
	cost = c
	temp = pk.Pancake("1234a")
	while p.maximum != 4321:
		val = 0
		visit = visited
		if p.maximum not in visit:
			visit.append(p.maximum)
		p.set_next()
		values = []
		p1 = p.cakelist[0]
		p2 = p.cakelist[1]
		p3 = p.cakelist[2]
		p1.update_h()
		p2.update_h()
		p3.update_h()
		p1.astar = p1.g + p1.h
		p2.astar = p2.g + p2.h
		p3.astar = p3.g + p3.h
		dict_star = {p1.maximum: p1.astar, p2.maximum: p2.astar, p3.maximum: p3.astar}
		sort_star = sorted(dict_star.items())
		if sort_star[0][1] == sort_star[1][1] and sort_star[0][1] == sort_star[2][1]:
			for i in sort_star:
				if i[0] not in visit:
					values.append(i[0])
					val = max(values)

		elif sort_star[0][0] == sort_star[1][0]:
			if sort_star[0][0] not in visit and sort_star[1][0] not in visit:
				val = max(sort_star[0][0], sort_star[1][0])
			elif sort_star[0][0] in visit and sort_star[1][0] not in visit:
				val = sort_star[1][0]
			elif sort_star[0][0] not in visit and sort_star[1][0] in visit:
				val = sort_star[0][0]
			else:
				if sort_star[3][0] not in visit:
					val = sort_star[3][0]

		else:
			if sort_star[0][0] not in visit:
				val = sort_star[0][0]
			else:
				if sort_star[1][1] == sort_star[2][1]:
					if sort_star[1][0] not in visit and sort_star[2][0] not in visit:
						val = max(sort_star[1][0], sort_star[2][0])
					elif sort_star[1][0] in visit and sort_star[2][0] not in visit:
						val = sort_star[2][0]
					elif sort_star[1][0] not in visit and sort_star[2][0] in visit:
						val = sort_star[1][0]
				else:
					val = sort_star[1][0]
		if val == p1.maximum:
			temp = p1
		elif val == p2.maximum:
			temp = p2
		elif val == p3.maximum:
			temp = p3

		if val in visit:
			if temp == p1:
				if p2.astar > p3.astar:
					temp = p3
				if temp.maximum in visit:
					temp = p2
				else:
					temp = p3

			elif temp == p2:
				if p1.astar > p3.astar:
					temp = p3
				if temp.maximum in visit:
					temp = p1
				else:
					temp = p3

			elif temp == p3:
				if p1.astar > p2.astar:
					temp = p2
				else:
					temp = p1
				if temp.maximum in visit:
					temp = p1
				else:
					temp = p2

		cost = cost + temp.g
		print_astar(p, cost)
		astar(temp, visit, cost)
	print_astar(p, cost)
	exit(0)


def print_astar(self, c):
	str_ucs = self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3]
	if str_ucs == "4321":
		print(self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
			c) + " h=%d" %
		      self.h)
	else:
		if self.g == 4:
			print("|" + self.elements[0] + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				c) + " h=%d" %
			      self.h)
		elif self.g == 3:
			print(self.elements[0] + "|" + self.elements[1] + self.elements[2] + self.elements[3] + " g=%d" % (
				c) + " h=%d" %
			      self.h)
		else:
			print(self.elements[0] + self.elements[1] + "|" + self.elements[2] + self.elements[3] + " g=%d" % (
				c) + " h=%d" %
			      self.h)
