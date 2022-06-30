# Write a function `canSum(targetSum, numbers)` that takes in a 
# targetSum and an array of numbers as arguments. 
# 
# The function should return a boolean indicating whether or not i 
# is possible to generate the targetSum usign numbers from the array. 
#
# You may use an element of the array as many times as needed. 
#
# You may assume that all input numbers are nonnegative. 



def canSum(target, numbers): 
  tab = [False for _ in range(target + 1)]
  tab[0] = True

  for i in range(target + 1): 
    if tab[i] == True: 
      for num in numbers: 
        # check to see that you're not going out of bounds 
        if i + num < target + 1: 
          tab[i + num] = True

  return tab[target]




print(canSum(7, [2,3])) # true 
print(canSum(7, [5, 3, 4, 7])) # true 
print(canSum(7, [2, 4])) # false 
print(canSum(8, [2, 3, 5])) # true  
print(canSum(300, [7, 14])) # false