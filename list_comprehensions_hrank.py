"""
Source: https://www.hackerrank.com/
Problem: Let's learn about list comprehensions! You are given three integers X, Y and Z representing the dimensions of
a cuboid along with an integer N. You have to print a list of all possible coordinates given by (i, j, k) on a 3D grid
where the sum of i + j + k  is not equal to N. Here, 0 <= i <= X ; 0 <= j <= Y;0 <=k <= Z
"""

x, y, z, n = (int(input()) for _ in range(4))
print([[a, b, c] for a in range(0, x + 1) for b in range(0, y + 1) for c in range(0, z + 1) if a + b + c != n])
