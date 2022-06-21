# Write a function `fib(n)` that takes in a number as an argurment 
# the function should return the n-th number of the Fibonacci sequence. 

# non memoized traditional recurrsive fibonacci sequence 
def fib(n: int) -> int: 

  if (n <= 2): 
    return 1
  return fib(n-1) + fib(n-2)


# Memoized fibonacci sequence
# Storage of duplicate sub problems using something like a hashmap 
# python dictionary

def fibMemo(n:int) -> int: 
  return fibMemoHelp(n, {})

def fibMemoHelp(n:int, memo:dict) -> int: 
  # first check for existence inside of the memo
  # if in memo then return what's in the memo 
  if (n in memo): 
    return memo[n]

  # otherwise continue as always
  if (n <= 2): 
    return 1
  
  # Memoize previous entries 
  memo[n] = fibMemoHelp(n-1, memo) + fibMemoHelp(n-2, memo)
  return memo[n]



print(fibMemo(50))