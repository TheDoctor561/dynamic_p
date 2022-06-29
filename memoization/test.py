result = []

a = [["purp"], ["p", "ur", "le"], ["purpl"]]
word = "polp"

targetWays = list(map(lambda x: [word]+x, a))


result = result + targetWays
print(result)