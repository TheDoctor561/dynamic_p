# Tabulized/bottom up version of fibonacci

def fib(n): 
  if n == 0: 
    return 0
  if n == 1: 
    return 1

  tab = [0] * (n + 1)
  tab[1] = 1

  for i in range(2, n + 1): 
    tab[i] = tab[i-1] +  tab[i-2] 

  return tab[n]

print(fib(6)) # 8 
print(fib(7)) # 13
print(fib(8)) # 21
print(fib(50)) # 12586269025