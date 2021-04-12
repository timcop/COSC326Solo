import sys

problem = []
for line in sys.stdin:
    line = line.split()
    try:
        prob = [line[0], int(line[1])]
    except:
        prob = [line[0], line[1]]
    problem.append(prob)
