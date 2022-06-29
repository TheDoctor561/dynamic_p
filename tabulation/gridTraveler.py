# Say that you are a traveler on a 2D grid. You begin in the 
# top-left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right. 

# In how many ways can you travel to the goal on a gird with 
# dimensions m*n? 

# Write a function `gridTraveler(m,n)` that calculates this. 
# O(mn) Time and Space 

def gridTraveler(n, m): 
  table = [[0 for i in range(m + 1)] for j in range(n + 1)]

  table[1][1] = 1

  for i in range(n + 1): 
    for j in range(m + 1): 
      curr = table[i][j]
      if i + 1 <= n: table[i+1][j] += curr
      if j + 1 <= m: table[i][j+1] += curr 
  return table[n][m]



print(gridTraveler(1,1)) # 1 
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220