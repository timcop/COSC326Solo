import sys
from sympy.utilities.iterables import multiset_permutations

count = 0
problems_all = []
current = []

# Nums is a list
def left_equation(nums, ops):
    sum = nums[0]
    for i in range(len(ops)):
        if ops[i] == 0:
            sum += nums[i+1]
        else:
            sum *= nums[i+1]
    return sum

# Turn nums into queue object
def normal_equation(nums, ops):
    master_sum = 0
    j = 0
    curr_sum = 0
    for i in range(len(ops)):
        if ops[i] == 1:
            curr_sum = nums[j] * nums[j+1]
            nums.pop(j)
            nums.pop(j)
            while ops[i+1] == 1:
                curr_sum *= nums[j]
                nums.pop(j)
                i += 1
            master_sum += curr_sum
            curr_sum = 0
            j += -1
        j += 1

        for i in range(len(ops)):
            master_sum += ops[i]

        return master_sum

# Maybe can just use a list and set things to 0, as when we do sum at the end
# doesn't matter if we add stuff that is 0
def normal_equationv2(nums, ops):
    master_sum = 0
    curr_sum = 0
    for i in range(len(ops)):
        if ops[i] == 1:
            curr_sum = nums[i] * nums[i+1]
            nums[i] = 0
            nums[i+1] = 0
            while ops[i+1] == 1:
                i += 1
                curr_sum += nums[i+1]
                nums[i+1] = 0
            master_sum += curr_sum
            curr_sum = 0
    return master_sum + sum(nums)

# Input
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

    operations = [0 for i in range(len(nums) - 1)]

    # perform left/normal function on operations
    solved = False
    for i in range(len(operations)):
        operations[i] = 1

        # unique permutations
        all_perms = list(multiset_permutations(operations))


        print(all_perms)
        for perm in all_perms:
            # perform left/normal function on operations and store in result
            # if result == target
                # print stuff
                #solved = True
            break
        if solved == True:
            break
