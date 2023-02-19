import math


class Triangle:
    def __init__(self):
        self.points = []

    def add_point(self, x, y):
        self.points.append((x, y))

    def perimeter(self):
        ab = math.sqrt(math.pow(self.points[0][0] - self.points[1][0], 2) + math.pow(
            self.points[0][1] - self.points[1][1], 2))
        bc = math.sqrt(math.pow(self.points[1][0] - self.points[1][0], 2) + math.pow(
            self.points[1][1] - self.points[2][1], 2))
        ca = math.sqrt(math.pow(self.points[0][0] - self.points[2][0], 2) + math.pow(
            self.points[0][1] - self.points[2][1], 2))
        return ab + bc + ca

    def is_equal(self, other):
        if self.points[0][0] != other.points[0][0] or self.points[0][1] != other.points[0][1] or self.points[1][0] != other.points[1][0] or self.points[1][1] != other.points[1][1] or self.points[2][0] != other.points[2][0] or self.points[2][1] != other.points[2][1]:
            return False
        else:
            return True

    # to use this function for checking t2 == t3, comment out the is_equal() and uncomment this function (Obivisiouly).
    # def __eq__(self, other):
    #     if self.points[0][0] != other.points[0][0] or self.points[0][1] != other.points[0][1] or self.points[1][0] != other.points[1][0] or self.points[1][1] != other.points[1][1] or self.points[2][0] != other.points[2][0] or self.points[2][1] != other.points[2][1]:
    #         return False
    #     else:
    #         return True


def main():
    t1 = Triangle()
    t1.add_point(0, 0)
    t1.add_point(0, 3)
    t1.add_point(4, 0)
    print("Perimeter of t1 object triangle is: ", t1.perimeter())

    t2 = Triangle()
    t2.add_point(1, 2)
    t2.add_point(2, 1)
    t2.add_point(1, 5)
    print("Perimeter of t2 object triangle is: ", t2.perimeter())

    if t1.is_equal(t2):
        print("Both objects have SAME points in the list.")
    else:
        print("Both objects have DIFFERENT points in the list.")

    t3 = Triangle()
    t3.add_point(1, 2)
    t3.add_point(2, 1)
    t3.add_point(1, 5)

    # here t2 and t3 objects have same value but t2 == t3 prints false
    # because t2 == t3 checks thier addresses not there value
    print("Are t1 and t3 have same addres: ", t2 == t3)

    print("are t1 and t3 have same values: ", t1.is_equal(t3))
    print("are t3 and t1 have same values: ", t3.is_equal(t1))

    # When we change the function is_equal() to __eq__(), then t2 == t3 prints true
    # because now t2 == t3 cheks their values not their address.
    #print("Is t2 and t3 are equal: ", t2 == t3)


if __name__ == "__main__":
    main()
