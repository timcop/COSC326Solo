import sys
problems_all = []
problems = []
for line in sys.stdin:
    if line.isspace() and len(problems) > 0:
        problems_all.append(problems)
        problems = []
    else:
        line = line.split()
        colour = line[0]
        try:
            length = int(line[1])
        except:
            length = line[1]
            for letter in length:
                if letter == line[0]:
                    length = 'NaN'
        
        prob = (colour, length)
        problems.append(prob)

print(problems_all)
print()
for i in range(len(problems_all)):
    solved = []
    #len_prob_init = len(prob)
    
    for i, tup in enumerate(prob):
        print(tup)
        if isinstance(tup[1], int):
            solved.append(prob.pop(i))
        if tup[1] == "NaN":
            print("hello")
            solved.append(prob.pop(i))

print(problems_all)
    #if len(prob) == len_prob_init
        # impossible

if(False):
    while len(prob) > 0:
        print(j)
        for i, tup in enumerate(prob):
            s = 0
            instruct = tup[1]
            instruct_len = len(instruct)
            count = 0
            for letter in tup[1]:
                for solv in solved:
                    if letter == solv[0]:
                        if solv[1] == 'NaN':
                            temp = (tup[0], 'NaN')
                            solved.append(temp)
                            prob.pop(prob.index())
                            
                        else:
                            s += solv[1]
                            count+=1
            if count == instruct_len:
                temp = (tup[0], s)
                solved.append(temp)
                prob.pop(i)


