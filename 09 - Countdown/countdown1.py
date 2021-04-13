import sys

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

for problem in problems_all:
    nums = problem[0]
    target = problem[1][0]
    order = problem[1][1]

    if order == 'N':
        
    else:
