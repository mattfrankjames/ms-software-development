class State():
	def __init__(self, cannibal_left, missionary_left, boat, cannibal_right, missionary_right):
		self.cannibal_left = cannibal_left
		self.missionary_left = missionary_left
		self.boat = boat
		self.cannibal_right = cannibal_right
		self.missionary_right = missionary_right
		self.parent = None

  # check if all cannibals and missionaries have moved from the left side
	def goal_met(self):
		if self.cannibal_left == 0 and self.missionary_left == 0:
			return True
		else:
			return False

	def is_valid_state(self):
    # make sure that there are never more cannibals than missionaries on a side
		if self.missionary_left >= 0 and self.missionary_right >= 0 \
                   and self.cannibal_left >= 0 and self.cannibal_right >= 0 \
                   and (self.missionary_left == 0 or self.missionary_left >= self.cannibal_left) \
                   and (self.missionary_right == 0 or self.missionary_right >= self.cannibal_right):
			return True
		else:
			return False

def move(current_state):
	children = []
	if current_state.boat == 'left':
		updated_state = State(current_state.cannibal_left, current_state.missionary_left - 2, 'right',
                                  current_state.cannibal_right, current_state.missionary_right + 2)
		## Two missionaries to right.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left - 2, current_state.missionary_left, 'right',
                                  current_state.cannibal_right + 2, current_state.missionary_right)
		## Two cannibals to right.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left - 1, current_state.missionary_left - 1, 'right',
                                  current_state.cannibal_right + 1, current_state.missionary_right + 1)
		## One missionary and one cannibal to right.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left, current_state.missionary_left - 1, 'right',
                                  current_state.cannibal_right, current_state.missionary_right + 1)
		## One missionary to right.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left - 1, current_state.missionary_left, 'right',
                                  current_state.cannibal_right + 1, current_state.missionary_right)
		## One cannibal to right.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
	else:
		updated_state = State(current_state.cannibal_left, current_state.missionary_left + 2, 'left',
                                  current_state.cannibal_right, current_state.missionary_right - 2)
		## Two missionaries to left.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left + 2, current_state.missionary_left, 'left',
                                  current_state.cannibal_right - 2, current_state.missionary_right)
		## Two cannibals to left.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left + 1, current_state.missionary_left + 1, 'left',
                                  current_state.cannibal_right - 1, current_state.missionary_right - 1)
		## One missionary and one cannibal to left.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left, current_state.missionary_left + 1, 'left',
                                  current_state.cannibal_right, current_state.missionary_right - 1)
		## One missionary to left.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
		updated_state = State(current_state.cannibal_left + 1, current_state.missionary_left, 'left',
                                  current_state.cannibal_right - 1, current_state.missionary_right)
		## One cannibal to left.
		if updated_state.is_valid_state():
			updated_state.parent = current_state
			children.append(updated_state)
	return children

def breadth_first_search():
	initial_state = State(3,3,'left',0,0)
	if initial_state.goal_met():
		return initial_state
	not_visited = list()
	explored = set()
	not_visited.append(initial_state)
	while not_visited:
		state = not_visited.pop(0)
		if state.goal_met():
			return state
		explored.add(state)
		children = move(state)
		for child in children:
			if (child not in explored) or (child not in not_visited):
				not_visited.append(child)
	return None

def print_solution(solution):
		path = []
		path.append(solution)
		parent = solution.parent
		while parent:
			path.append(parent)
			parent = parent.parent

		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print ("|           {0}            |              {1}             |     {2}     |            {3}             |              {4}             |".format(str(state.cannibal_left), str(state.missionary_left), state.boat.ljust(5), str(state.cannibal_right), str(state.missionary_right)))

def main():
	solution = breadth_first_search()
	print ("Missionaries and Cannibals solution:")
	print ("|no. cannibals left bank | no. missionaries left bank | boat postion  | no. cannibals right bank | no. missionaries right bank|")
	print_solution(solution)

main()