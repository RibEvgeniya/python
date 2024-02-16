# №1
#вариант 12
# Pentagon Triangle
# compare, is_intersect
#- compare(T1 t1, T2 t2) сравнение объектов по площади.
#- is_intersect(T1 t1, T2 t2) определяет факт пересечения объектов.
import itertools
from math import sqrt


class Shape:
    def __init__(self, identifier):
        self.identifier = identifier
class Point():
    def __init__(self, x,y):
        self.x=x
        self.y=y
        if type(self.x) in (int, float) and type(self.y) in (int, float):
            pass
        else:
            raise ValueError(f"Wrong data type for {self.__class__.__name__}!")
    def dist(self, p2):
        return sqrt(pow(p2.x-self.x,2)+pow(p2.y-self.y,2))
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y

class Triangle(Shape):
    def __init__(self,identifier, p):
        super().__init__(identifier)
        self.p=p
        if (len(self.p)>3):
            raise ValueError(f"Wrong number of points for {self.__class__.__name__}!")

    def square(self):
        sides=[]
        for i in range (2):
            sides.append(self.p[i].dist(self.p[i+1]))
            if(i==1):
                sides.append(self.p[i+1].dist(self.p[0]))
        perimeter=sum(sides)
        half_per=perimeter/2
        return sqrt(half_per*(half_per-sides[0])*(half_per-sides[1])*(half_per-sides[2]))

class Pentagon(Shape):
    def __init__(self, identifier, p):
        super().__init__(identifier)
        self.p = p
        if (len(self.p) > 5):
            raise ValueError(f"Wrong number of points for {self.__class__.__name__}!")
    def square(self):
        sides = []
        for i in range(4):
            sides.append(self.p[i].dist(self.p[i + 1]))
            if (i == 3):
                sides.append(self.p[i + 1].dist(self.p[0]))
        perimeter = sum(sides)
        triangles=[]
        for i in range(1,4):
            triangles.append(Triangle(self.p[0],self.p[i],self.p[i+1]))

        return triangles[0].square()+triangles[1].square()+triangles[2].square()


def compare(T1, T2):
    if T1.square()>T2.square():
        print("The square of the ", T1.__class__.__name__," with id  ", T1.identifier, " is larger")
    elif T1.square()<T2.square():
        print("The square of the ", T2.__class__.__name__, " with id  ", T2.identifier, " is larger")
    else:
        print("The squares are equal")



def det (a, b, c, d) :
    return a * d - b * c

def between (a, b,c):
    EPS = 1E-9
    return min(a,b) <= c + EPS and c <= max(a,b) + EPS

def intersect_1 (a, b, c, d):
    if (a > b):
        a,b=b,a
    if (c > d):
        c, d = d, c
    return max(a,c) <= min(b,d)
def doIntersect(a,b,c,d):
    A1 = a.get_y() - b.get_y()
    B1 = b.get_x() - a.get_x()
    C1 = -A1 * a.get_x() - B1 * a.get_y()
    A2 = c.get_y() - d.get_y()
    B2 = d.get_x() - c.get_x()
    C2 = -A2 * c.get_x() - B2 * c.get_y()
    zn = det(A1, B1, A2, B2)
    if (zn != 0):
        x = - det (C1, B1, C2, B2) * 1. /zn
        y = - det (A1, C1, A2, C2) * 1. /zn
        return between(a.get_x(), b.get_x(), x) and between(a.get_y(), b.get_y(), y) and between(c.get_x(), d.get_x(), x) and between(c.get_y(), d.get_y(), y)
    else:
        return det(A1, C1, A2, C2) == 0 and det(B1, C1, B2, C2) == 0 and intersect_1(a.get_x(), b.get_x(), c.get_x(), d.get_x()) and intersect_1(a.get_y(), b.get_y(), c.get_y(), d.get_y());

def is_intersect(T1, T2):
    if isinstance(T1, Triangle) and isinstance(T2, Triangle):
        comb_1 = list(itertools.combinations(T1.p, 2))
        comb_2 = list(itertools.combinations(T2.p, 2))
        Flag = False
        for a in comb_1:
            for b in comb_2:
                p11,p12=a
                p21,p22=b
                Flag = Flag or doIntersect(p11,p12,p21,p22)
        return Flag

    elif isinstance(T1, Triangle) and isinstance(T2, Pentagon):
        comb_1 = list(itertools.combinations(T1.p, 2))
        comb_2 = list(itertools.combinations(T2.p, 2))
        Flag = False
        for a in comb_1:
            for b in comb_2:
                Flag = Flag or doIntersect(a, b)
        return Flag

    elif isinstance(T1, Pentagon) and isinstance(T2, Pentagon):
        comb_1 = list(itertools.combinations(T1.p, 2))
        comb_2 = list(itertools.combinations(T2.p, 2))
        Flag = False
        for a in comb_1:
            for b in comb_2:
                Flag = Flag or doIntersect(a,b)
        return Flag
    return False

p=[]
p.append(Point(0,5))
p.append(Point(5,0))
p.append(Point(0,0))
tr1=Triangle(1,p)

p=[]
p.append(Point(0,7))
p.append(Point(7,0))
p.append(Point(1,1))
tr2=Triangle(2,p)

compare(tr1,tr2)
print(is_intersect(tr1,tr2))

