import math
def Areaoftriangle(a, b, c):
    Perimeter = a + b + c
    s = (a + b + c) / 2
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print("The perimeter of traiangle = %.2f" %Perimeter);
   # print("The Semi Perimeter of traiangle = %.2f" %s);
    print("The Area of a triangle is %0.2f" %Area)
Areaoftriangle(8, 9, 10)
