import math

def quadratic_roots(a,b,c):
    discriminant = b**2 - 4 * a * c
    if discriminant >= 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        return None
    

a = 1
b = 7
c = 12
roots = quadratic_roots (a,b,c)
if roots:
        print(f"the roots are: {roots[0] and {roots[1]}}")
else: 
        print("the equation has complex roots.")
    