# Write a function `howSum(target, numbers)` that takes in a 
# targetSum and an array of numbers as arguments. 
#
# The function should return an array containing any combination of 
# elements that add up to exactly the targetSum. 
#
# If there is no combination that adds up to the targetSum, then 
# return -1 
# 
# If there are multiple combinations possibl, you may return any 
# single one. 

from pyparsing import nums


def howSum(target, numbers): 
  tab = [-1 for _ in range(target + 1)]

  tab[0] = []
  for i in range(target + 1): 
    if tab[i] != -1: 
      for num in numbers: 
        if num + i <= target: 
          tab[i + num] = tab[i] + [num] 

  return tab[target]

def test_sum():
    assert howSum(7, [2,3]) == [3, 2, 2], "Should be [3, 2, 2]"
    assert howSum(7, [5, 3, 4, 7]) == [4, 3], "Should be [4, 3]"
    assert howSum(7, [2, 4]) == -1, "Should be -1"
    assert howSum(8, [2, 3, 5]) == [2, 2, 2, 2], "Should be [2, 2, 2, 2]"
    assert howSum(300, [7, 14]) == -1, "Should be -1"

if __name__ == "__main__":
    test_sum()
    print("Everything passed")