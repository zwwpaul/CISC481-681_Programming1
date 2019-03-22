import pancake as pk
import DFS as dfs
import UCS as ucs
import Greedy as gdy
import AStarSearch as astar

# Get user input
user_in = raw_input("\nPlease enter four digits and one letter(d/u/g/a)\n")
length = len(user_in)
# Create a pancake list
# Each pancake cannot have the same value
pancake = []
if length != 5:
	exit(0)
else:
	for x in range(0, length):
		if x != length:
			pancake.append(user_in[x])

# Test Cases
# print(pancake[x], type(pancake[x]))
p1 = pk.Pancake(pancake)

# d is for DFS
if p1.choice == "d":
	dfs.add_path(p1)
	p1.update_h()
	dfs.print_dfs(p1)
	while p1.h != 0:
		dfs.compare_update(p1)
		p1.update_h()
		dfs.print_dfs(p1)
# This part is for UCS
elif p1.choice == "u":
	ucs.ucs(p1)
# This part is for Greedy
elif p1.choice == "g":
	p1.update_h()
	gdy.greedy(p1, p1.visited, 0)
# This part is for A-Star
elif p1.choice == "a":
	p1.update_h()
	astar.astar(p1, p1.visited, 0)
