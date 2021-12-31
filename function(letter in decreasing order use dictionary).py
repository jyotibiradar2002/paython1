# WAP to create a function called most_frequent that takes a string and print the letter in decreasing order of frequence.use dictionaries.
string = input('Please enter a string ')
def most_frequent(string):
   d = dict()
for key in string:
   if key not in d:
   d[key] = 1
else :
   d[key] += 1
return d

print(most_frequent(string))
