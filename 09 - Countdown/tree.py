from collections import deque

class Node:
    # Node has left and right children (binary tree). Left corresponds to
    # addition and right is multiplication. Curr_sum and curr_times
    # are variables used the order is "Normal"

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None
        self.curr_sum = None
        self.curr_times = None

    # Prints tree Inorder
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

    # Insert_Left is used to create the two children nodes
    # in a Tree with Left order specificied. We prune the Tree
    # by only creating nodes that are less than the target, we
    # also keep track of the current nodes at this level
    # as we can avoid creating exact same sub trees.
    # If two nodes have the same data at the same level, their
    # trees will be the exact same.
    
    def Insert_Left(self, num, target, num_set):
        left_num = self.data + num
        right_num = self.data * num

        if left_num <= target and not (left_num in num_set):
            self.left = Node(self.data + num)
            self.left.parent = self
            num_set.add(left_num)

        if right_num <= target and not (right_num in num_set):
            self.right = Node(self.data * num)
            num_set.add(right_num)
            self.right.parent = self

    # Insert_Normal is the same idea as Insert_left, however this is for
    # a Tree with Normal order.
        pass
    def Insert_Normal(self, num, prev_num, target, num_set):

        left_num = self.data + num
        if left_num <= target and not (left_num in num_set):
            self.left = Node(left_num)
            self.left.curr_sum = left_num
            self.left.curr_times = 0 # No current multiplication
            self.left.parent = self
            num_set.add(left_num)

        # We handle the right child in this if/else
        if self.curr_times == 0:
            curr_times = num * prev_num
            curr_sum = self.curr_sum - prev_num # Need to take away previously added number
            right_num = curr_times + curr_sum
            if right_num <= target and not (right_num in num_set):
                self.right = Node(right_num)
                self.right.curr_times = curr_times
                self.right.curr_sum = curr_sum
                self.right.parent = self
                num_set.add(right_num)

        else:
            curr_times = self.curr_times * num # Continue multiplying curr_times
            curr_sum = self.curr_sum # Remains unchanged from parent node
            right_num = curr_times + curr_sum
            if right_num <= target and not (right_num in num_set):
                self.right = Node(right_num)
                self.right.curr_times = curr_times
                self.right.curr_sum = curr_sum
                self.right.parent = self
                num_set.add(right_num)

class Tree:
    # Numbers are the numbers to use in the equation, order is either 'L' or 'N'
    # and the target number is what we want from the equation. Variable bottom_level
    # are the numbers at the final tree depth which are the results of all possible equations.
    # We need only to search this depth to see if a solution has been found.
    def __init__(self, numbers, order, target):
        self.numbers = numbers
        self.order = order
        self.target = target
        self.root = Node(numbers[0])
        self.bottom_level = None

    # We add the root to the queue, then loop through the numbers and perform Insert on each one.
    # We then add the children to the queue and perform the insert operations on them.
    # Finally we're left with the maximum depth nodes with are our solutions.
    def Load_Tree(self):
        queue = deque([self.root])
        temp_queue = deque([])

        # Left order
        if self.order == 'L':
            for num in self.numbers[1:]:
                num_set = set()
                while queue:
                    node = queue.popleft()
                    node.Insert_Left(num, self.target, num_set)
                    if node.left != None:
                        temp_queue.append(node.left)
                    if node.right!= None:
                        temp_queue.append(node.right)
                queue = temp_queue.copy()
                temp_queue = deque([])
            self.bottom_level = queue
        # Normal order
        else:
            self.root.curr_sum = self.root.data
            self.root.curr_times = 0
            for i, num in enumerate(self.numbers):
                num_set = set()
                if i != 0:
                    while queue:
                        prev_num = self.numbers[i-1]
                        node = queue.popleft()
                        node.Insert_Normal(num, prev_num, self.target, num_set)
                        if node.left != None:
                            temp_queue.append(node.left)
                        if node.right!= None:
                            temp_queue.append(node.right)
                    queue = temp_queue.copy()
                    temp_queue = deque([])
                self.bottom_level = queue

    # Prints the solution if found, otherwise prints impossible. If the solution
    # is found we work our way back up the tree tracking the path.
    def Print_Solution(self):
        path = []
        found_solution = False
        if self.order == 'L':
            for node in self.bottom_level:
                if node.data == self.target:
                    found_solution = True
                    print(self.order + ' ' + str(self.target), end = ' ')
                    print(self.root.data, end = ' ')
                    for num in reversed(self.numbers):
                        if node.parent != None:
                            if node.parent.data + num == node.data:
                                path.append(('+', num))
                            else:
                                path.append(('*', num))
                            node = node.parent
                    break
            for i in reversed(path):
                print(i[0] + ' ' + str(i[1]), end = ' ')
        else:
            for node in self.bottom_level:

                if node.data == self.target:
                    found_solution = True
                    print(self.order + ' ' + str(self.target), end = ' ')
                    print(self.root.data, end = ' ')
                    for num in reversed(self.numbers):
                        if node.parent != None:
                            if node.parent.left == node:
                                path.append(('+', num))
                            elif node.parent.right == node:
                                path.append(('*', num))
                            node = node.parent
                    break
            for i in reversed(path):
                print(i[0] + ' ' + str(i[1]), end = ' ')
        if not found_solution:
            print(self.order + ' ' + str(self.target) + ' ' + "impossible", end = '')
        print()
