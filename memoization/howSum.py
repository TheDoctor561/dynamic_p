# Write a function `howSum(targetSum, numbers)` that takes in a 
# targetSum and an array of numbers as arguments. 

# The function should return an array containing any combination of 
# elements that add up to exactly the targetSum. If there is no 
# combination that adds up to the targetSum, then return null

# Brute Force
# time: O(n^m * m)
# space: O(m)

def howSum(targetSum, numbers): 
  if (targetSum == 0): 
    return []
  if (targetSum < 0): 
    return None 

  for num in numbers: 
    remainder = targetSum - num
    res = howSum(remainder, numbers)
    if (res != None):            
      return [*res, num]
  
  return None 


# How Sum Memoized version 
# Memoized 
# time: O(n*m^2)
# space: O(m^2)
def howSum(targetSum, numbers): 
  return howSumHelp(targetSum, numbers, {})

def howSumHelp(targetSum, numbers, memo): 
  if (targetSum in memo): 
    return memo[targetSum]
  if (targetSum == 0): 
    return []
  if (targetSum < 0): 
    return None 

  for num in numbers: 
    remainder = targetSum - num
    res = howSumHelp(remainder, numbers, memo)
    if (res != None):   
      memo[targetSum] = [*res, num]        
      return memo[targetSum]

  memo[targetSum] = None
  return None

print(howSum(7, [2, 3])) # [3, 2, 2]
print(howSum(7, [5, 3, 4, 7])) # [4, 3]
print(howSum(7, [2, 4])) # None
print(howSum(8, [2, 3, 5])) # [2, 2, 2, 2] 
print(howSum(300, [7, 15])) # None