fruit = ["apple","orange","peer"]
fruit.append("banana")
fruit.append("peach")
fruit[1] = "mikan"
fruit.pop()
print(fruit)

guess = input("input your fruit:")

if guess in fruit:
    print("nice")
else:
    print("poor")
