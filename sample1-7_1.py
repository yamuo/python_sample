"""
name = "Ted"
for character in name:
    print(character)
"""
"""
people = {
    "bluth":"development",
    "barney":"himym",
    "dennis":"chainbers"
    }

"""
"""
for character in people:
    print(character)
"""
"""
tv = ["GOT","Narcos","Vice"]
i = 0
for show in tv:
    new = tv[i]
    new = new.upper()
    tv[i] = new
    i += 1

print(tv)
"""
"""
tv = ["GOT","Narcos","Vice"]
for i, new in enumerate(tv):
    new = tv[i]
    new = new.upper()
    tv[i] = new

print(tv)
"""
"""
tv = ["GOT","Narcos","Vice"]
coms = ["develop","friends","sunny"]
all_shows = []

for show in tv:
    show = show.upper()
    all_shows.append(show)

for show in coms:
    show = show.upper()
    all_shows.append(show)

print(all_shows)
"""
"""
for i in range(1,11):
    print(i)
"""
"""
x = 10
while x > 0:
    print('{}'.format(x))
    x -= 1
print("happy birth day!!!!")
"""
"""
qs = [
    "What is your name?",
    "What is your fav. color?",
    "What is your quest?"
    ]
n=0
while True:
    print("Type q to quit")
    a = input(qs[n])
    if a == "q":
        break
    n = (n+1) % 3
"""
"""
for i in range(1,6):
    if i == 3:
        continue
    print(i)
"""
"""
for i in range(1,3):
    print(i)
    for letter in["a","b","c"]:
        print(letter)
"""
"""
list1 = [1,2,3,4]
list2 = [5,6,7,8]
added = []
for i in list1:
    for j in list2:
        added.append(i + j)
print(added)
"""
"""
while input('y of n?') != 'n':
    for i in range(1,6):
        print(i)
"""
"""
list1 = ["walking dead","antrajyu","sopranos","vampire"]
for i , new in enumerate(list1):
    print("{}:{}".format(i,new))
"""
"""
for i in range(25,51):
    print(i)
"""
"""
import random

n = random.randrange(10)
while True:
    a = int(input("try your luck:"))
    if a == n:
        break
"""

list1 = [8,19,148,4]
list2 = [9,1,33,83]

for i in list1:
    for j in list2:
        print(i * j)


















