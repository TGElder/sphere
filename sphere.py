import math
import matplotlib.pyplot as plt

class SCoord:

    def __init__(self, r, inc, azi):
        self.r = r
        self.inc = inc
        self.azi = azi

    def to_cartesian(self):
        z = self.r / (math.tan(self.inc)**2 + math.tan(self.azi)**2 + 1)
        x = math.tan(self.inc) * z
        y = math.tan(self.azi) * z
        return CCoord3(x, y, z)

    def to_2D(self):
        return self.to_cartesian().to_2D()

    def __str__(self):
        return "({}, {}, {})".format(self.r, self.inc, self.azi)

class CCoord2:
    def __init__(self, x, y):
        self.x = x;
        self.y = y;

    def to_3D(self, radius):
        z = math.sqrt(radius**2.0 - self.x**2.0 - self.y**2.0)
        return CCoord3(self.x, self.y, z)

    def to_spherical(self, radius):
        return self.to_3D(radius).to_spherical()

    def __str__(self):
        return "({}, {})".format(self.x, self.y)


class CCoord3:
    def __init__(self, x, y, z):
        self.x = x;
        self.y = y;
        self.z = z;

    def to_2D(self):
        return CCoord2(self.x, self.y)

    def to_spherical(self):
        r = math.sqrt(self.x**2 + self.y**2 + self.z**2)
        inc = math.atan(self.x / self.z)
        azi = math.atan(self.y / self.z)
        return SCoord(r, inc, azi)

    def __str__(self):
        return "({}, {}, {})".format(self.x, self.y, self.z)


#a = CCoord2(2, 2)
#print(a)
#a_s = a.to_spherical(100)
#print(a_s)
#a_3D = a_s.to_cartesian()
#print(a_3D)
#a_2D = a_3D.to_2D()
#print(a_2D)

r = 3000

a = CCoord2(-49, -32)
b = CCoord2(-47, 97)
c = CCoord2(47, 98)

a_s = a.to_spherical(r);
b_s = b.to_spherical(r);
c_s = c.to_spherical(r);

print(a_s)
print(b_s)
print(c_s)

inc_ba = a_s.inc - b_s.inc
azi_ba = a_s.azi - b_s.azi
inc_bc = c_s.inc - b_s.inc
azi_bc = c_s.azi - b_s.azi

x = []
y = []


for a in range(-10, 10):
    for c in range(-10, 10):
        inc = b_s.inc + a * inc_ba + c * inc_bc
        azi = b_s.azi + a * azi_ba + c * azi_bc
        p_s = SCoord(r, inc, azi)
        p_2D = p_s.to_cartesian()
        x.append(p_2D.x)
        y.append(p_2D.y)

plt.scatter(x, y)
plt.show()
