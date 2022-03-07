class tri:
    def areaOfTriangle(self, x, y):
        area = 0.5*x*y
        return area
    def perOfTriangle(self, x, y, z):
        return x+y+z
print("Enter Length of Base and Height: ", end="")
b = float(input())
h = float(input())

print("Enter Length all Three Sides: ", end="")
a = float(input())
b = float(input())
c = float(input())

obj = tri()
a = obj.areaOfTriangle(b, h)

ob = tri()
p = ob.perOfTriangle(a, b, c)
print("\nArea = {:.2f}".format(a))
print("\nPerimeter = {:.2f}".format(p))
 
 
