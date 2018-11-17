import math

class Test:
    def move(self, x, y):
        self.x = x
        self.y = y
    def reset(self):
        self.move(0,0)
    def calc_distance(self, other_point):
        return math.sqrt(
            (self.x - other_point.x)**2 + 
            (self.y - other_point.y)**2 )

t1 = Test()
t2 = Test()
t1.move(0,0)
t2.move(5,0)
print(t1.calc_distance(t2))
t1.move(3,4)
print(t1.calc_distance(t2))
print(t1.calc_distance(t1))