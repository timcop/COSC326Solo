def normal_equation(nums, ops):
    master_sum = 0
    j = 0
    curr_sum = 0
    for i in range(len(ops)):
        if ops[i] == 1:
            curr_sum = nums[j] * nums[j+1]
            nums.pop(j)
            nums.pop(j)
            if i < (len(ops) -2):
                print(i)
                print(len(ops))
                while ops[i+1] == 1:
                    curr_sum *= nums[j]
                    nums.pop(j)
                    i += 1
                    if i == (len(ops)-2):
                        break
            master_sum += curr_sum
            curr_sum = 0
            j += -1
        j += 1

        for i in range(len(ops)):
            master_sum += ops[i]

        return master_sum
