import sys
import numpy as np
import copy

## Handles input
problems_all = []
current = []
for line in sys.stdin:
    if not line.isspace():
        line = line.split()
        try:
            prob = [line[0], int(line[1])]
        except:
            prob = [line[0], line[1]]
        current.append(prob)
    else:
        if len(current) > 0:
            problems_all.append(current)
            current = []
if len(current) > 0:
    problems_all.append(current)

## Loop through each problem
for problem in problems_all:
    finished_rows = set()
    n = len(problem)


    scalar_array = [0 for i in range(n)]
    for i, prob in enumerate(problem):
        if isinstance(prob[1], int):
            scalar_array[i] = prob[1]
        else:
            scalar_array[i] = 0

    colours = np.zeros((n, n), dtype=int)
    for row, prob_i in enumerate(problem):
        colour_code = prob_i[1]
        if not isinstance(colour_code, int):
            for col, prob_j in enumerate(problem):
                for letter in colour_code:
                    if letter == prob_j[0]:
                        colours[row, col] += 1
            if np.sum(colours[row, :]) != len(colour_code):
                scalar_array[row] = 'NaN'
                colours[row, :] = 0
        else:
            colours[row, :] = 0

    # for i in range(n):
    #     if isinstance(scalar_array[i], int) and scalar_array[i] < 0:
    #         scalar_array[i] = 'NaN'

    found_new_row = True
    while found_new_row:
        found_new_row = False
        for i in range(n):
            if np.all((colours[i, :] == 0)) and i not in finished_rows:
                found_new_row = True
                for j in range(n):
                    if colours[j, i] != 0:
                        if scalar_array[i] == 'NaN':
                             scalar_array[j] = 'NaN'
                        elif scalar_array[j] != 'NaN':
                             scalar_array[j] += colours[j, i] * scalar_array[i]
                        colours[j, i] = 0
                finished_rows.add(i)

    for i in range(n):
        if not np.all(colours[i, :] == 0):
            scalar_array[i] = 'NaN'

    for i in range(n):
        print(problem[i][0] + " " + str(scalar_array[i]))
    print("")
