import sys 

def coinChange(coins, amount: int) -> int:
  tab = [0] + [sys.maxsize for _ in range(amount)]
  for i in range(amount + 1): 
    for coin in coins: 
      if i-coin >= 0: 
        tab[i] = min(tab[i], tab[i-coin] + 1)
  
  if tab[amount] == sys.maxsize: 
    return -1
  return tab[amount]

print(coinChange([1,2], 3))
