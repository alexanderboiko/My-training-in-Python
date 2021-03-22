# магические методы
# метод __bool__

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print('call len')
        return abs(self.x - self.y)

    def __bool__(self):
        print('call bool')
        return self.x != 0 or self.y != 0