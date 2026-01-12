import re

text = "The rain in Spain"

a = re.search("ai",text)

print(a.span())

b = re.match("The",text)

print(b)

print(re.findall("ai",text))
