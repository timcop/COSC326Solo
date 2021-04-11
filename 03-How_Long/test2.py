import sys
import numpy as np
import copy

problems_all = []
something = []
for line in sys.stdin:
    if not line.isspace():
        line = line.split()
        try:
            prob = [line[0], int(line[1])]
        except:
            prob = [line[0], line[1]]
        something.append(prob)
    else:
        problems_all.append(something)
        something = []
problems_all.append(something)

for problem in problems_all:
    n = len(problem)
    colours = np.zeros((n, n), dtype=int)

    for row, prob_i in enumerate(problem):
        colour_code = prob_i[1]
        if not isinstance(colour_code, int):
            for col, prob_j in enumerate(problem):
                for letter in colour_code:
                    if letter == prob_j[0]:
                        colours[row, col] += 1
            if np.sum(colours[row, :]) != len(colour_code):
                problem[row][1] = 'NaN'
        else:
            colours[row, :] = 0

    new_prob = copy.deepcopy(problem)
    for i in range(n):
        if not isinstance(new_prob[i][1], int) and new_prob[i][1]!='NaN':
            new_prob[i][1] = 0


    next_colour = False
    for i in range(n):
        if np.all((colours[i, :] == 0)):
            for j in range(n):
                if new_prob[j][1]!='NaN' and problem[i][1] != 'NaN':

                    new_prob[j][1] += int(colours[j, i]) * int(problem[i][1])

                    colours[j, i] = 0
                    if np.all(colours[j, :] == 0):
                        problem[j][1] = new_prob[j][1]
                        next_colour = True

    while not np.all((colours == 0)) and next_colour:
        next_colour = False
        for i in range(n):
            if np.all((colours[i, :] == 0)):
                next_colour = False
                for j in range(n):
                    if new_prob[j][1]!='Nan' and problem[i][1] != 'NaN':
                        new_prob[j][1] += int(colours[j, i]) * int(problem[i][1])
                        colours[j, i] = 0
                        if np.all(colours[j, :] == 0):
                            if not (isinstance(problem[j][1], int) or isinstance(problem[j][1], float)):

                                problem[j][1] = new_prob[j][1]
                                next_colour = True
    for i in range(n):
        if np.all((colours[i, :] == 0)):
            for j in range(n):
                if new_prob[j][1]!='Nan' and problem[i][1] != 'NaN':
                    new_prob[j][1] += int(colours[j, i]) * int(problem[i][1])
                    colours[j, i] = 0
                    if np.all(colours[j, :] == 0):
                        problem[j][1] = new_prob[j][1]
                        next_colour = True
    for i in range(n):
        if not np.all((colours[i, :] == 0)):
            problem[i][1] = 'NaN'

    print(problem)
