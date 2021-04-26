import sys
from sympy.utilities.iterables import multiset_permutations
import time as time

# solve_equation function that uses the numbers and operations
# passed and computes the result given the order
def solve_equation(nums, ops, order, target):
    nums = list(nums) # make a copy as 'N' order changes the elements

    # Our operations should be 1 less in length than the numbers
    if len(ops) != (len(nums) - 1):
        return None

    # For left order, we work our way through the array either adding or multiplying
    # the current number to our sum that we have computed along the way
    elif order == 'L':
        master_sum = nums[0]
        for i in range(len(ops)):
            if ops[i] == 0:
                master_sum += nums[i+1]
            else:
                master_sum *= nums[i+1]
                if master_sum > target:
                    return None

        return master_sum

    # Normal order is a bit more complicated, we work our way through the array
    # looking for multiplication operations. The current_sum variable multiplies the
    # two numbers adds them to master_sum, then sets those numbers
    # to 0 in the array. If there are consequtive multiplication operations, we
    # want to multiply current_sum by the next number before adding to master_sum.
    # Once the multiplication operations have been handeled, we can just sum
    # the remaining numbers and add the master_sum.

    elif order == 'N':
        master_sum = 0
        curr_sum = 0
        for i in range(len(ops)):
            if ops[i] == 1:
                curr_sum = nums[i] * nums[i+1]
                nums[i] = 0
                nums[i+1] = 0
                while (i < len(ops) - 1) and ops[i+1] == 1: # Checks for consequtive '*'
                    i += 1
                    curr_sum *= nums[i+1]
                    nums[i+1] = 0
                master_sum += curr_sum
                if master_sum > target:
                    return None
                curr_sum = 0
        return master_sum + sum(nums)
    # If neither L or N is the order
    else:
        return None

# Prints the desired output for a solved problem
def print_solution(nums, ops, order, target):
    print(order + " " + str(target), end=" ")
    print(str(nums[0]), end="")
    for i in range(1, len(nums)):
        if ops[i-1] == 0:
            print(" " + '+' + " " + str(nums[i]), end="")
        else:
            print(" " + '*' + " " + str(nums[i]), end="")
    print("")

# For each problem read in by the standard input,
# we make use of the fact that our only allowed operations are
# '+' and '*', so we treat these as 0 = '+', 1 = '*' in our operations array.
# We start the operations array as all 0, then each time add a 1 and then
# find all the unique permutations for that number of 0's and 1's.
# Using these permutations, we are able to compute all possible equations.
def compute_problems(problems_all):
    for problem in problems_all:

        nums = list(map(int, problem[0]))
        target = int(problem[1][0])
        order = problem[1][1]
        operations = [0 for i in range(len(nums) - 1)]
        solved = False

        # First try with all 0's
        result = solve_equation(nums, operations, order, target)

        if result == target:
            print_solution(nums, operations, order, target)
            solved = True

        i = 0
        while solved == False and i < len(operations):

            operations[i] = 1

            # unique permutations
            all_perms = list(multiset_permutations(operations))

            for perm in all_perms:
                result = solve_equation(nums, perm, order, target)

                if result == target:

                    print_solution(nums, perm, order, target)

                    solved = True
                    break
            i += 1
        if not solved:
            print(order + " " + str(target) + " impossible")

# Input
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
start = time.time()
compute_problems(problems_all)
finish = time.time()
print(finish-start)
