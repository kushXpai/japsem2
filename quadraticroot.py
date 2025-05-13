import math

class QuadraticEquationSolver:
    def findRoots(self, a, b, c):
        if a == 0:
            return "Not a quadratic equation (a cannot be 0)."

        discriminant = b**2 - 4*a*c

        if discriminant > 0:
            root1 = (-b + math.sqrt(discriminant)) / (2 * a)
            root2 = (-b - math.sqrt(discriminant)) / (2 * a)
            return f"Real and distinct roots: {root1}, {root2}"
        elif discriminant == 0:
            root = -b / (2 * a)
            return f"Real and equal roots: {root}, {root}"
        else:
            real_part = -b / (2 * a)
            imag_part = math.sqrt(-discriminant) / (2 * a)
            return f"Complex roots: {real_part}+{imag_part}i, {real_part}-{imag_part}i"

solver = QuadraticEquationSolver()
print(solver.findRoots(2, -5, -3))