def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [None] * (i + 1)
        row[0], row[-1] = 1, 1
 
        for j in range(1, len(row) - 1):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        triangle.append(row)
    
    for row in triangle:
        print(" ".join(map(str, row)).center(n * 2))

n = 5
generate_pascals_triangle(n)
