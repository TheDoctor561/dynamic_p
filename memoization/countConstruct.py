# Give the number of ways we can construct a string 
# given that we have a target and a wordBank

# Original 
def countConstruct(target, wordBank): 
  ret = 0
  if target == '': 
    return 1 

  for i in wordBank: 
    suffix = target.removeprefix(i)
    if(suffix != target): 
      ret += countConstruct(suffix, wordBank)
  
  return ret 

# memoized 
def countConstruct(target, wordBank): 
  return ccHelp(target, wordBank, {})

def ccHelp(target, wordBank, memo): 
  if target == '': 
    return 1 
  if target in memo: 
    return memo[target]

  ret = 0

  for i in wordBank: 
    suffix = target.removeprefix(i)
    if(suffix != target): 
      ret += ccHelp(suffix, wordBank, memo)

  memo[target] = ret 
  return ret  



print(countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])) # 1
print(countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])) # 0
print(countConstruct("enterapotentpot", ["a", "p", "ent","enter", "ot", "o", "t"])) # 4
print(countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee","eeeee","eeeeee"])) #0 