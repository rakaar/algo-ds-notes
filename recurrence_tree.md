# analysis of any recurrence tree in general

Know how many level are u breaking at each level of problem
for example
  in merge sort- it breaks into 2 sub problems
  in standard multiplication - it breaks into 4 problems
  for karatsuba its 3

and at each level calculate the amount of work done

for example,
merge sort 
T(n) = 2T(n/2) + O(n)
Calculating the second part is important. To do that properly one needs to have proper
understanding of what needs to be done at each stage
For example in Merge sort, if 2 arrays of length n needs to be merged it takes order n time
and in standard multiplication, the final stage is adding up, it takes properly 2 additions
(How 2?- {10*n/2ac + bd} + (ad+bc), the part inside flower braces seems like addition but is simply a concatenation of 2 numbers bcoz most of them are zeros
ad+bc is one addition which takes (Cost_for_unit_addition) times n, bcoz ad is of size n and so is bc
how did ad and bc bcome of size n --> a is of n/2 and c is of n/2, when u multiply both of them u get a number of size n as maximum 98*93
the other addition is adding the result of ad+bc to the the result of the flower braced number
hence cost_for_unit_addition * 2 * n
)

And in some problems like multiplication complexity analysis, it is important to consider the bottom most level too
it happens in these cases the order of bottom most level cost exceeds that of the sum of all above
for example in analyzing standard multiplications
the bottom most level will have COST_FOR_UNIT_MULTIPLCATTION*4^(logn base2)
how did logn base 2 come?
  at level 1 - 4^(1-1) problems
  at level 2 - 4^(2-1) problems
  at bottom most level(1+logn) - 4^(logn) problems, east of cost- `COST_FOR_UNIT_MULTIPLCATTION`
so if u see the cost of bottom most level is order n^2
while the sum of the remaining is of order(n)
hence it is important to consider last level too!

similarly in karatsuba, last level is order(n^log3 base2)

Merge sort tree
              cn                          = cn       
          cn/2   cn/2                     = cn
    cn/4   cn/4  cn/4   cn/4     -> 4*c/4 = cn
c   c  c .....  c ... c .. c  c  -> c * n = cn

cost cn(1 + logn) = O(nlogn)

## standard Multiplication
              tn                  = 1* (2 Cost_for_unit_addition n)
      tn/2    tn/2  tn/2   tn/2   = 4 * (2 Cost_for_unit_addition n/2)
  tn/4 tn/4 tn/4 tn/4 .....       = 16 * (2 Cost_for_unit_addition n/4)
1 1 1 1 1 11 1 1 1 1 .             = 4^(logn)*(COST_FOR_UNIT_MULTIPLCATTION)
sum of all level except last = order(n) = sigma((4/2)^r) r: 1->logn => 2^logn => n
last term dominates the sum = n^2

## karatsuba Multiplication
              tn                  = 1* (4 Cost_for_unit_addition n)
      tn/2  tn/2   tn/2           = 3 * ( Cost_for_unit_addition n/2)
  tn/4 tn/4 tn/4  .....           = 9 * ( Cost_for_unit_addition n/2)
1 1 1 1 1 11 1 1 1 1 .             = 3^(logn base2)*(COST_FOR_UNIT_MULTIPLCATTION)
sum of all level except last = order(n) = sigma((3/2)^r) r: 1->logn => 2^logn => n^(log1.5 base2)
last term dominates the sum = n^(log3 base2)

Mistakes in analysis by own
- Not considering the cost at each level properly, it needs to be calculated properly by considering the number of additions
- The last level was ignored, In merge sort at each level its same, hence even though u didnt go to last level it worked
but here at each level it differs, hence it is better to write down the last level and include it in the addtion rather than simply
assuming i: 1 -> logn.