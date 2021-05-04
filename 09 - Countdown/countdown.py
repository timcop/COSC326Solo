import sys
from tree import Node, Tree

count = 0
problems_all = []
current = []

for line in sys.stdin:
    count+=1
    line = line.split()
    current.append(line)
    if count % 2 == 0:
        problems_all.append(current)
        current = []


for prob in problems_all:
    # print(prob)
    nums = list(map(int, prob[0]))
    target = int(prob[1][0])
    order = prob[1][1]
    tree = Tree(nums, order, target)
    tree.Load_Tree()
    tree.Print_Solution()
