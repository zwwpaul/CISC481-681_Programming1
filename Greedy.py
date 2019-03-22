import pancake as pk


def greedy(p, visited, c):
	cost = c
	p_temp = pk.Pancake("1234a")
	while p.h != 0:
		p.set_next()
		p1 = p.cakelist[0]
		p2 = p.cakelist[1]
		p3 = p.cakelist[2]
		p1.update_h()
		p2.update_h()
		p3.update_h()
		visit = visited
		if p.maximum not in visit:
			visit.append(p.maximum)
		# There is no equality
		if p1.h < p2.h:
			if p1.h < p3.h:
				p_temp = p1
			else:
				p_temp = p3
		else:
			if p2.h < p3.h:
				p_temp = p2
			else:
				p_temp = p3

		if p1.h == p2.h & p2.h == p3.h:
			if p1.maximum > p2.maximum:
				if p1.maximum > p3.maximum:
					p_temp = p1
				else:
					p_temp = p3
			else:
				if p2.maximum > p3.maximum:
					p_temp = p2
				else:
					p_temp = p3

		elif p1.h == p2.h & p3.h > p1.h:
			if p1.maximum > p2.maximum:
				p_temp = p1
			else:
				p_temp = p2

		elif p1.h == p2.h & p3.h < p1.h:
			p_temp = p3

		elif p1.h == p3.h & p2.h > p1.h:
			if p1.maximum > p3.maximum:
				p_temp = p1
			else:
				p_temp = p3

		elif p1.h == p3.h & p2.h < p1.h:
			p_temp = p2

		elif p2.h == p3.h & p1.h > p2.h:
			if p2.maximum > p3.maximum:
				p_temp = p2
			else:
				p_temp = p3
		elif p2.h == p3.h & p1.h < p2.h:
			p_temp = p1

		if p_temp.maximum in visit:
			if p_temp == p1:
				if p2.h > p3.h:
					p_temp = p3
				else:
					p_temp=p2
				if p_temp.maximum in visit:
					if p_temp==p3:
						p_temp = p2
					else:
						p_temp = p3

			elif p_temp == p2:
				if p1.h > p3.h:
					p_temp = p3
				else:
					p_temp=p1
				if p_temp.maximum in visit:
					if p_temp==p3:
						p_temp = p1
					else:
						p_temp = p3

			elif p_temp == p3:
				if p1.h > p2.h:
					p_temp = p2
				else:
					p_temp=p1
				if p_temp.maximum in visit:
					if p_temp==p2:
						p_temp = p1
					else:
						p_temp = p2
		print_gd(p, cost)
		cost = cost + p_temp.g
		greedy(p_temp, visit, cost)
	print_gd(p, cost)
	exit(0)


def print_gd(self, c):
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
