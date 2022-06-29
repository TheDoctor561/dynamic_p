def gridTraveler(m,n): 
  return gtHelp(m, n, {})

def gtHelp(m, n, memo) -> int: 
  key = str(m) + "," + str(n)
  if (m == 1 or n == 1): 
    return 1 
  if (m == 0 or n == 0): 
    return 0
  if key in memo: 
    return memo[key]
  memo[key] = gtHelp(m-1, n, memo) + gtHelp(m, n-1, memo)
  return memo[key]
  
print(gridTraveler(1,1)) # 1 
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220