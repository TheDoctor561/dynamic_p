# Write a function `bestSum(targetSum, numbers)` that takes in a 
# targetSum and an array of numbers as arguments. 

# The function should return an array containing the shortest 
# combination of numbers that add up to exactly the targetSum. 

# If there is a tie for the shortest combination, you man return any 
# one of the shortest. 

# Pretty much the same complexity of howSum, however since we need to go through all branches it takes longer
#
#
# Brute Force
# time: O(n^m * m)
# space: O(m^2)
# stack depth of m multiplied by the array length 

def bestSum(target, nums):
  if (target == 0): 
    return []
  if (target < 0): 
    return None 
  
  best = None
  for num in nums: 
    remainder = target - num
    res = bestSum(remainder, nums)
    if (res != None):
      curr = [*res, num]
      if (best == None or len(curr) < len(best)): 
        best = curr

  return best 

# Memoized 
# time: O(m^2 * n)
# space: O(m^2)
# Remember the extra m time comes in the worst case of the array being added 
# The actually algorithm takes only O(m*n) time
def bestSum(targetSum, numbers): 
  return bestSumHelp(targetSum, numbers, {})

def bestSumHelp(targetSum, numbers, memo):
  if targetSum in memo: return memo[targetSum]
  if targetSum == 0: return []
  if targetSum < 0: return None
  
  shortestCombination = None
  for num in numbers:
      remainder = targetSum - num
      remainderCombination = bestSumHelp(remainder, numbers, memo)
      
      if remainderCombination is not None:
          combo = [*remainderCombination, num]
          if shortestCombination is None or len(combo) < len(shortestCombination):                
              shortestCombination = combo

  memo[targetSum] = shortestCombination
  return shortestCombination

print(bestSum(7, [5, 3, 4, 7])) # [7] 

print(bestSum(8, [2, 3, 5])) # [3, 5]

print(bestSum(8, [1, 4, 5])) # [4, 4]

print(bestSum(100, [1, 2, 5, 25])) # [25, 25, 25, 25]

[1, 2, 5, 25]
100