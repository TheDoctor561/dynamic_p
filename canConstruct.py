# Given a target string and an array of strings
# return true of there exists a combination of 
# substrings that equate to the target string


def canConstruct(target, wordBank): 
  if target == '': 
    return True
  for i in wordBank: 
    newTarget = target.removeprefix(i)
    
    if (target != newTarget):
      #if newTarget == '': 
        # print("Ho")
      if canConstruct(newTarget, wordBank) == True: 
        return True 
  return False 
 

print(canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))