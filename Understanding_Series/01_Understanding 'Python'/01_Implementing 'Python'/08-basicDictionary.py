# Dictionary
# collectn of data in pairs as key and data
# items in a dictionary are not stored in the same order as the way they're  declared
colours = {'Red':3,'Blue':4,'Green':5} # line 1
print(colours)    
colours = dict(Red=3,Blue=4,Green=5)   # line 2
print(colours) 
# line 1 and 2 have same meaning
print(colours['Blue'])                    # printing value in dictionary using key
(colours['Orange'])=6                    # appending new value in dictionary using new key
print(colours) 
colours.pop("Green")                      # deleting a value in dictionary using key
print(colours)                           
