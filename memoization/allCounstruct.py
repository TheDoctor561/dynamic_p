# Given a target and an list of elements 
# return an array of the combinations of elements 
# in the list that make up the target 

def allConstruct(target, wordBank): 
  if target == '': return [[]]

  result = []

  for word in wordBank: 
    suffix = target.removeprefix(word)
    if(suffix != target): 
      suffixWays = allConstruct(suffix, wordBank)
      targetWays = list(map(lambda x: [word]+x, suffixWays))
      result = result + targetWays

  return result


def allConstruct(target, wordBank): 
  return allCHelp(target, wordBank, {})

def allCHelp(target, wordBank, memo): 
  if target == '': return [[]]
  if target in memo: 
    return memo[target]

  result = []
  
  for word in wordBank: 
    suffix = target.removeprefix(word)
    if(suffix != target): 
      suffixWays = allCHelp(suffix, wordBank, memo)
      targetWays = list(map(lambda x: [word]+x, suffixWays))
      result = result + targetWays
  
  memo[target] = result
  return result


print(allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]))
# [
#  ['purp', 'le']
#  ['p', 'ur', 'p', 'le']
# ]

print(allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))

# [
#   ['ab', 'cd', 'ef'], 
#   ['ab', 'c', 'def'], 
#   ['abc', 'def'], 
#   ['abcd', 'ef']
# ]

print(allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]))

# []

print(allConstruct("aaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]))

# []