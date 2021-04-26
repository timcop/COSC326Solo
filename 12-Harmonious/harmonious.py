
import math as m
import time as time

# Returns sum of all factors of n.
def sumofFactors(n):
    temp = n
    # Traversing through all
    # prime factors
    res = 1
    for i in range(2, int(m.sqrt(n) + 1)):

        curr_sum = 1
        curr_term = 1

        while n % i == 0:

            n = n / i;

            curr_term = curr_term * i;
            curr_sum += curr_term;

        res = res * curr_sum

    # This condition is to handle the
    # case when n is a prime number
    # greater than 2
    if n > 2:
        res = res * (1 + n)

    return int(res - temp -1);

# driver code
# done = set()
# for i in range(3, 2000000):
#     if i not in done:
#         i_dsum = sumofFactors(i)
#         if i_dsum >= i and i == sumofFactors(i_dsum):
#             print(str(i) + " " + str(i_dsum))
#             done.add(i)
#             done.add(i_dsum)

start = time.time()
for i in range(3, 2000000):
    sum = sumofFactors(i)
finish = time.time()
print(finish-start)
