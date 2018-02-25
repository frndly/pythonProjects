import random


# This is the list of variables
loc = random.choice(['Seattle', 'Chicago', 'London', 'San Francisco'])
bus = random.choice(['auto shop', 'bakery', 'clinic', 'clothing shop', 'restaurant', 'book store', 'law office'])
own = random.choice(['Frank N. Furter', 'George Orwell', 'Rhymenocerous', 'Steve', 'Vincent Adultman'])
nam = random.choice(['Genesis', 'Lily', 'Fifth and Pine', "Quetzl's", 'Gekko Rabbitowitz', 'Vim', 'Vigor'])
colList = ['blue', 'green', 'red', 'white', 'black', 'yellow', 'pink', 'purple', 'orange', 'grey', 'tan']
adjList = ['bright', 'muddy', 'dark', 'light', 'dull', 'pastel', 'neon']

iteList = ['cat', 'dog', 'bird', 'boat', 'elephant', 'cloud', 'building', 'fish', 'circle', 'square', 'line']
a = 'a'

# This establishes the colorsnd a corresponding aadjective.

col = random.choice(colList)
adj = random.choice(adjList)+(' ')+random.choice(colList)


# this establishes the number of ite1
numb = random.choice(['a', 'two', 'three'])


# this establishes the rules for ite1 and ite2
ite1 = random.choice(iteList)
ite2 = random.choice(iteList)



# This code is broken, it still prints a building and a building, for example.  Also prints clouds and a cloud.  

if ite2 == ite1:
	random.choice(iteList)
else:
	ite2




if numb == 'two' or numb == 'three': # Adds syntax
   ite1 = ite1+('s')
   
if ite1 == 'elephant' and numb == 'a': # creates 'an' for elephant
  numb = numb+('n') 






# This code eestablishes 'an' and eliminates the extra 's' from fish

if ite2 == 'elephant':
	a = a+('n')
else:
  a = a

if ite1 == 'fishs':
  ite1 = 'fish'
  
  
  # this is the task

task = ('Your customer {} would like you to build a website for his {}, "{}", which is located in {}. \n\n{} also has the following requests for the design of the site:\n\n1. The color palette must be centered on the color {}.\n\n2. The color palette must not include {}.\n\n3. You must design a logo containing {} {} and {} {}.')
print(task.format(own,bus,nam,loc,own,col,adj,numb,ite1,a, ite2))
