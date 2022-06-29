# Really the basis of the coin problem 

# Can sum given a target variable and a list return true if the target can be 
# summed using the list of numbers givven 
# ex. canSum(7, [5, 3, 4, 7]) -> true 
# because 3 + 4 = 7 and 7 - 7 = 0 

# Brute force solution with a runtime complexity of O(n^m) and a space complexity 
# of O(m)

def canSum(target:int, nums:list) -> bool: 
  if (target == 0):
    return True 
  if (target < 0): 
    return False 
  for num in nums: 
    remainder = target - num
    if canSum(remainder, nums) == True: 
      return True 
  
  return False


# print(canSum(7, [2,3])) # true 


# Memoized version of canSum

# The new complexity is O(m * n) time 
# with a space complexity of O(m) 

def canSumMemo(target:int, nums:list) -> bool: 
  return canSumHelp(target, nums, {})

def canSumHelp(target:int, nums:list, memo:dict) -> bool: 
  if target in memo: 
    return memo[target]
  if target == 0: 
    return True
  if target < 0: 
    return False 
  for num in nums: 
    remainder = target - num
    if canSumHelp(remainder, nums, memo): 
      memo[target] = True 
      return True

  memo[target] = False
  return False
  

print(canSumMemo(7, [2,3])) # true 
print(canSumMemo(7, [5, 3, 4, 7])) # true 
print(canSumMemo(7, [2, 4])) # false 
print(canSumMemo(8, [2, 3, 5])) # true 
print(canSumMemo(300, [7, 14])) # false