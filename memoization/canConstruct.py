# Given a target string and an array of strings
# return true of there exists a combination of 
# substrings that equate to the target string

# Original 
def canConstruct(target, wordBank): 
  if target == '': 
    return True
  for i in wordBank: 
    newTarget = target.removeprefix(i)
    
    if (target != newTarget):
      if canConstruct(newTarget, wordBank) == True: 
        return True 
  return False 


# Memoized 
def canConstruct(target, wordBank): 
  return ccHelp(target, wordBank, {})

def ccHelp(target, wordBank, memo): 
  if target == '': 
    return True
  if target in memo: 
    return memo[target]

  for i in wordBank: 
    newTarget = target.removeprefix(i)
    
    if (target != newTarget):
      if ccHelp(newTarget, wordBank, memo) == True: 
        memo[target] = True
        return True 
  memo[target] = False
  return False 

 

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # True 
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # False
print(canConstruct("enterapotentpot", ["a", "p", "ent","enter", "ot", "o", "t"])) # True 
print(canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee","eeeee","eeeeee"])) # False 