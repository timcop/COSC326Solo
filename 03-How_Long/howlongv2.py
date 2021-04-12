import sys
import numpy as np
import copy


for line in sys.stdin:

    if not line.isspace():
        problem = []
        line = line.split()
        try:
            prob = [line[0], int(line[1])]
        except:
            prob = [line[0], line[1]]
        problem.append(prob)

    else:
        n = len(problem)
        colours = np.zeros((n, n))

        for row, prob_i in enumerate(problem):
            colour_code = prob_i[1]
            if not isinstance(colour_code, int):
                for col, prob_j in enumerate(problem):
                    for letter in colour_code:
                        if letter == prob_j[0]:
                            colours[row, col] += 1
            else:
                colours[row, :] = 0

        new_prob = copy.deepcopy(problem)
        print(problem)
        for i in range(n):
            new_prob[i][1] = 0
        print(problem)
        while not np.all((colours == 0)):
            next_colour = None
            for i in range(n):
                if np.all((colours[i, :] == 0)):
                    next_colour = None
                    for j in range(n):
                        new_prob[j][1] += colours[j, i] * int(problem[i][1])
                        colours[j, i] = 0
                        if np.all(colours[j, :] == 0):
                            problem[j][1] = new_prob[j][1]
                            next_colour = j
            if next_colour == None:
                for i in range(n):
                    if not np.all((colours[i, :] == 0)):
                        problem[i, 1] = 'Nan'

        print(problem)
