class goat:
    def __init__(self , x , y):
        self.x = x
        self.y = y
    def __add__(self , other):
        return goat(self.x - other.y , self.y- self.y)

first = goat(34, 100)
second = goat(24 , 10)


result = first + second

print(result.x)
