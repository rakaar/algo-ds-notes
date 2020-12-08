# recursion to calculate fib
def rec_fib(n):
    if n is 1 or n is 0:
        return n
    else:
        return rec_fib(n-1) + rec_fib(n-2)
    
print(rec_fib(10))

# the above func rec_fib is slow and takes exponential time
# two ways to see it exponential
# 1. fibonacci approximation used golden number power n
# 2. T(n) = T(n-1) + T(n-2) + O(1)
#         >= 2 T(n-2)
#         >= 2^(n/2), because u can expand the above as 4*T(n-4) and 8*T(n-6), and so on u can do that n/2 times
# also by drawing the recursion tree, you can see that some values are calculated repeatdly
# fib(4) -> fib(3) + fib(2) -> then for calculate fib(3) -> fib(2) + fib(1), and fib(2) -> fib(1) + fib(0), 
# and but u calculate fib2 again for the second term in  fib(3) + fib(2)
# so to avoid to re calculation, we store the calculated values, and store them, this idea is called memoization

memo = {}
def memo_fib(n):
    if n in memo:
        return memo[n]
    elif n is 1 or n is 0:
        return n
    else:
        f = memo_fib(n-1) + memo_fib(n-2) 
        memo[n] = f # storing it
        return f

print(memo_fib(10))

# the above func is linear time
# reason if we want to calculate fib of n, we make atmost n calls -> fib 1, fib 2, fib 3 ... fib n
# and each call is constant time, as all we do is extraction from dictionary and addition
# so in a generalized way it can be written as time_for_each_sub_problem * number_of_subproblems
# time_taken = O(1)*n = O(n)

# using the same memoization technique, we can write a slightly better code, by reducing the function calls, that iss instead of recurising we wil loop
def loop_fib(n):
    fib = {}
    for i in range(n+1):
        if i is 1 or i is 0:
            fib[i] = i
        else:
            fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

print(loop_fib(10))

# the above 2 functions, reduce time complexity but consume space
# but the above can be still optimized space wise, by saving only the last two, instead of saving all of them
def fib_space_save(n):
    fib = [0,1]
    if n is 0 or n is 1:
        return n
    else:
        for i in range(2,n+1):
            # the pattern can be observed by writing down things [fib0 fib1] for fib2, [fib2 fib1] for fib 3, [fib2 fib3] for fib 4, 
            if i % 2 is 0:
                f = fib[0] + fib[1]
                fib[0] = f
            else:
                f = fib[0] + fib[1]
                fib[1] = f
    return f

print(fib_space_save(10))