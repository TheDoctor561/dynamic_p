# Tabulized/bottom up version of fibonacci

def fib(n): 

  # create an empty python list and fill with zeros
  table = [0]*(n + 1)
  table[1] = 1 

  for i in range(n):
    print(i) 
    table[i+1] += table[i]
    if (i + 2) <= n: 
      table[i+2] += table[i]
    print(table)

  return table[n]
print(fib(6))