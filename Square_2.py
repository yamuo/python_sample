class Square:
    square_list = []
    
    def __init__(self, w):
        self.width = w
        self.square_list.append(self.width)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width,self.width,self.width,self.width)


s1 = Square(2)
s2 = Square(4)
s3 = Square(6)

print(s1)

