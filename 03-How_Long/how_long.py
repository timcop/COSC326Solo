import sys

previous_space = True
first_line = sys.stdin.readline()
if first_line.isspace():
    previous_space = True
else:
    previous_space = False

problems_all = []
current_prob = []
for line in sys.stdin:
    if not line.isspace():
        line = line.split()
        try:
            prob = [line[0], int(line[1])]
        except:
            prob = [line[0], line[1]]
        current_prob.append(prob)

    elif line.isspace() and not previous_space:
        problems_all.append(current_prob)
        previous_space = True

for i in range(len(problems_all)):
    print(problems_all[i], "\n")
