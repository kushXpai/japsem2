import math
import cmath

class CubicEquationSolver:
    def findRoots(self, a, b, c, d):
        if a == 0:
            return "Not a cubic equation (a cannot be 0)."

        f = ((3 * c / a) - ((b ** 2) / (a ** 2))) / 3
        g = ((2 * b ** 3) / (a ** 3) - (9 * b * c) / (a ** 2) + (27 * d / a)) / 27
        h = (g ** 2) / 4 + (f ** 3) / 27

        if h > 0:
            R = -g / 2 + math.sqrt(h)
            S = R ** (1/3) if R >= 0 else -(-R) ** (1/3)
            T = -g / 2 - math.sqrt(h)
            U = T ** (1/3) if T >= 0 else -(-T) ** (1/3)

            x1 = (S + U) - (b / (3 * a))
            return f"One real root: {x1:.4f}"

        elif h == 0 and f == 0 and g == 0:
            x = - (d / a) ** (1 / 3)
            return f"Triple real root: {x:.4f}"

        else:
            i = math.sqrt((g ** 2) / 4 - h)
            j = i ** (1 / 3)
            k = math.acos(-g / (2 * i))
            m = math.cos(k / 3)
            n = math.sqrt(3) * math.sin(k / 3)
            p = -b / (3 * a)

            x1 = 2 * j * m + p
            x2 = -j * (m + n) + p
            x3 = -j * (m - n) + p

            return f"Three real roots: {x1:.4f}, {x2:.4f}, {x3:.4f}"

solver = CubicEquationSolver()
print(solver.findRoots(1, -6, 11, -6))