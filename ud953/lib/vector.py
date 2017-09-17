import math

class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            if isinstance(coordinates, tuple):
                self.coordinates = coordinates
            else:
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

    def __add__(self, other):
        return Vector(tuple(map(lambda x, y: x + y, self.coordinates,other.coordinates)))

    def __sub__(self, other):
        return Vector(tuple(map(lambda x, y: x - y, self.coordinates,other.coordinates)))
    
    def __mul__(self, value):
        return Vector(tuple(map(lambda x: x*value, self.coordinates)))

    def plus(self, other):
        new_coord = [x+y for x, y in zip(self.coordinates, other.coordinates)]
        return Vector(new_coord)
    
    def dot(self, other):
        d = lambda X, Y: sum(map(lambda x, y: x * y, X, Y))
        return d(self.coordinates, other.coordinates)

    def angle(self, other):
        m1 = self.mag()
        m2 = other.mag()
        if (m1 == 0 or m2 == 0):
            return math.pi
        d = self.dot(other)/(m1*m2)
        return math.acos(d)
        
    def mag(self):
        return math.sqrt(sum(i**2 for i in self.coordinates))

    def norm(self):
        m = self.mag()
        try:
            return Vector(tuple(map(lambda x: x/m, self.coordinates)))
        except ZeroDivisionError:
            raise Exception('cannot normalize zero vector')

    def component_parallel_to(self, basis):
        u = basis.norm()
        weight = self.dot(u)
        return u*weight

    def component_orthogonal_to(self, basis):
        p = self.component_parallel_to(basis)
        return self - p

    def cross_product(self, other):
        x = self.coordinates[1]*other.coordinates[2]-other.coordinates[1]*self.coordinates[2]
        y = -(self.coordinates[0]*other.coordinates[2]-other.coordinates[0]*self.coordinates[2])
        z = self.coordinates[0]*other.coordinates[1]-other.coordinates[0]*self.coordinates[1]
        return Vector([x,y,z])
    
    def cross_parallelogram_area(self, other):    
        c = self.cross_product(other)
        return c.mag()
    
    def cross_triangle_area(self, other):    
        return self.cross_parallelogram_area(other)/2
