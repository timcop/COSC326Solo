from collections import deque
class Node:

    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        self.parent = None
        self.curr_sum = None
        self.curr_times = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.data)
        if self.right:
            self.right.PrintTree()

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

    def Insert_Right(self, num, prev_num, target, num_set):
        # TODO:
        # num_set
        left_num = self.data + num
        if left_num <= target and not (left_num in num_set):
            self.left = Node(left_num)
            self.left.curr_sum = left_num
            self.left.curr_times = 0
            self.left.parent = self
            num_set.add(left_num)

        if self.curr_times == 0:
            curr_times = num * prev_num
            curr_sum = self.curr_sum - prev_num
            right_num = curr_times + curr_sum
            if right_num <= target and not (right_num in num_set):
                self.right = Node(right_num)
                self.right.curr_times = curr_times
                self.right.curr_sum = curr_sum
                self.right.parent = self
                num_set.add(right_num)

        else:
            curr_times = self.curr_times * num
            curr_sum = self.curr_sum
            right_num = curr_times + curr_sum
            if right_num <= target and not (right_num in num_set):
                self.right = Node(right_num)
                self.right.curr_times = curr_times
                self.right.curr_sum = curr_sum
                self.right.parent = self
                num_set.add(right_num)

class Tree:
    def __init__(self, numbers, order, target):
        self.numbers = numbers
        self.order = order
        self.target = target
        self.root = Node(numbers[0])
        self.bottom_level = None

    def Load_Tree(self):
        queue = deque([self.root])
        temp_queue = deque([])
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
        else:
            self.root.curr_sum = self.root.data
            self.root.curr_times = 0
            for i, num in enumerate(self.numbers):
                num_set = set()
                if i != 0:
                    while queue:
                        prev_num = self.numbers[i-1]
                        node = queue.popleft()
                        node.Insert_Right(num, prev_num, self.target, num_set)
                        if node.left != None:
                            temp_queue.append(node.left)
                        if node.right!= None:
                            temp_queue.append(node.right)
                    queue = temp_queue.copy()
                    temp_queue = deque([])
                self.bottom_level = queue

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
