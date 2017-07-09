import math
from decimal import Decimal, getcontext

getcontext().prec = 30

class Vector(object):

    CANNOT_NORMALIZE_ZERO_VECTOR_MSG = 'Cannot normalize the zero vector'

    ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG = 'Only defined in two or three dimension'


    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')


    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)


    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(v1,v2):
        new_coordinates = [x+y for x, y in zip(v1.coordinates, v2.coordinates)]
        return Vector(new_coordinates)

    def minus(v1, v2):
        new_coordinates = [x-y for x, y in zip(v1.coordinates, v2.coordinates)]
        return Vector(new_coordinates)

    def times_scalar(v1, c):
        new_coordinates = [Decimal(c)*x for x in v1.coordinates]
        return Vector(new_coordinates)

    def magnitude(self):
        coordinates_squared = [x**2 for x in self.coordinates]
        return Decimal(math.sqrt(sum(coordinates_squared)))

    def normalized(self):
        try:
            magnitude = self.magnitude()
            return self.times_scalar(Decimal(1.0)/magnitude)
        except ZeroDivisionError:
            raise Exception(self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG)

    def dot_product(self, w):
        coordinates_times = [x*y for x, y in zip(self.coordinates, w.coordinates)]
        return sum(coordinates_times)

    def angle(self, w, in_degrees=False):
        try:
            u1 = self.normalized()
            u2 = w.normalized()
            angle_in_radians = math.acos(u1.dot_product(u2))

            if in_degrees:
                degrees_per_radian = 180./math.pi
                return angle_in_radians * degrees_per_radian
            else:
                return angle_in_radians

        except Exception as e:
            if str(e) == self.CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
                raise Exception('cannot calcurate the angle of one vector between a zero vector')
            else:
                raise e

    def is_zero(self, tolerance = 1):
        return self.magnitude() < tolerance

    def is_orthogonal_to(self, w, tolerance = 1):
        return abs(self.dot_product(w)) < tolerance

    def is_parallel_to(self, w):
        return (self.is_zero() or w.is_zero() or self.angle(w) == 0 or self.angle(w) == math.pi)

    def cross_product(self, w):
        try:
            x1, y1, z1 = self.coordinates
            x2, y2, z2 = w. coordinates
            new_coordinates = [y1*z2 - y2*z1,
                                -(x1*z2 - x2*z1),
                                x1*y2 - x2*y1]
            return Vector(new_coordinates)

        except ValueError as e:
            mag = str(e)
            if mag == 'need more than 2 values to unpack':
                self_embedded_in_R3 = Vector(self.coordinates + ('0',))
                w_embedded_in_R3 = Vector(w.coordinates + ('0',))
                return self_embedded_in_R3.cross(w_embedded_in_R3)
            elif (mag == 'too many values to unpack' or mag == 'need more than 1 value to unpack'):
                raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
            else:
                raise e

    def area_of_parallelogram_with(self, w):
        cross_product = self.cross_product(w)
        return cross_product.magnitude()

    def area_of_triangle_with(self, w):
        return self.area_of_parallelogram_with(w)/Decimal(2.0)