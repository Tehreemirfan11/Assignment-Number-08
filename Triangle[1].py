side1 = float(input("length of the first side: "))
side2 = float(input("length of the second side: "))
side3 = float(input("length of the third side: "))
if side1 == side2 == side3:
    print("Equilateral triangle.")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("Isosceles triangle.")
else:
    print("Scalene triangle.")