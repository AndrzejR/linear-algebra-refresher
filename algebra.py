from math import sqrt

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def add(self, v):
        self.coordinates = tuple((x+y for x, y in
                                  zip(self.coordinates, v.coordinates)))
    def subtract(self, v):
        self.coordinates = tuple((x-y for x, y in
                                  zip(self.coordinates, v.coordinates)))
    def scalar_multiply(self, s):
        self.coordinates = tuple((x*s for x in self.coordinates))

    def magnitude(self):
        return sqrt(sum((x**2 for x in self.coordinates)))

    def normalization(self):
        mag = self.magnitude()
        return tuple((1/mag*x for x in self.coordinates))


if __name__ == '__main__':
    vector_1 = Vector((8.218,-9.341))
    print(vector_1)
    vector_2 = Vector((-1.129,2.111))
    print(vector_2)
    print("Vector 1 + vector 2:")
    vector_1.add(vector_2)
    print(vector_1)

    vector_3 = Vector((7.119,8.215))
    vector_4 = Vector((-8.223,0.878))
    print("Vector 3 minus vector 4:")
    vector_3.subtract(vector_4)
    print(vector_3)

    vector_5 = Vector((1.671,-1.012,-0.318))
    scalar_1 = 7.41
    print("Vector 5 times scalar 1:")
    vector_5.scalar_multiply(scalar_1)
    print(vector_5)

    vector_6_1 = Vector((-0.221, 7.437))
    print("vector_6_1.magnitude: " + str(round(vector_6_1.magnitude(),3)))
    vector_6_2 = Vector((8.813, -1.331, -6.247))
    print("vector_6_2.magnitude: " + str(round(vector_6_2.magnitude(),3)))

    vector_6_3 = Vector((5.581, -2.136))
    print("vector_6_3.normalization(): " + str(vector_6_3.normalization()))
    vector_6_4 = Vector((1.996, 3.108, -4.554))
    print("vector_6_4.normalization(): " + str(vector_6_4.normalization()))
