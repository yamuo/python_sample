class Orange:
    def __init__(self,w,c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Created!")

    def rot(self, days, temp):
        self.mold = days * temp

or1 = Orange(200,"orange")

print(or1.mold)
or1.rot(10,37)
print(or1.mold)
