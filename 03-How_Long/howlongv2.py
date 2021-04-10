import sys
import numpy as np
import copy

problem = []
for line in sys.stdin:

    if not line.isspace():
        line = line.split()
        try:
            prob = [line[0], int(line[1])]
        except:
            prob = [line[0], line[1]]
        problem.append(prob)

    else:
        n = len(problem)
        colours = np.zeros((n, n))

        for i, prob_i in enumerate(problem):
            colour = prob_i[0]
            for j, prob_j in enumerate(problem):
                colour_code = prob_j[1]
                if not isinstance(colour_code, int):
                    for letter in colour_code:
                        if letter == colour:
                            colours[j, i] += 1

        new_prob = copy.deepcopy(problem)
        print(problem)
        for i in range(n):
            new_prob[i][1] = 0
        print(problem)
        while not np.all((colours == 0)):
            for i in range(n):
                if np.all((colours[i, :] == 0)):
                    for j in range(n):
                        new_prob[j][1] += colours[i, j] * problem[i][1]
                        colours[i, j] = 0
                        #print(problem)
                        problem[j][1] = new_prob[j][1]


        print(problem)
        problem = []
