from random import randint


# x = randint(1, 6)
# print(x)

class Die():
    def __init__(self, sides):
        self.sides = sides

    def roll_die(self):

        x = randint(1, self.sides)
        print(x)



rrr = Die(20).roll_die()
rrr2 = Die(20).roll_die()
rrr3 = Die(20).roll_die()
rrr4 = Die(20).roll_die()
rrr5 = Die(20).roll_die()
rrr6 = Die(20).roll_die()
rrr7 = Die(20).roll_die()
rrr8 = Die(20).roll_die()
rrr9 = Die(20).roll_die()
rrr0 = Die(20).roll_die()
