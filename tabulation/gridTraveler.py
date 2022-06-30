# Say that you are a traveler on a 2D grid. You begin in the 
# top-left corner and your goal is to travel to the bottom-right
# corner. You may only move down or right. 

# In how many ways can you travel to the goal on a gird with 
# dimensions m*n? 

# Write a function `gridTraveler(m,n)` that calculates this. 
# O(mn) Time and Space 

def gridTraveler(n, m):   
  tab = [[1 for i in range(m)] for j in range(n)]
  

  for i in range(1, n): 
    for j in range(1, m): 
      
      tab[i][j] = tab[i- 1][j] + tab[i][j - 1]

  return(tab[n-1][m-1])


print(gridTraveler(1,1)) # 1 
print(gridTraveler(2,3)) # 3
print(gridTraveler(3,2)) # 3
print(gridTraveler(3,3)) # 6
print(gridTraveler(18,18)) # 2333606220