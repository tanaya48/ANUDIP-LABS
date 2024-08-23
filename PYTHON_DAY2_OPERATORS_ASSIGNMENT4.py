# Python program to find the area of a triangle whose sides are given

def triangle_area(a, b, c):
    s = (a + b + c) / 2
    area = (s * (s - a) * (s - b) * (s - c)) ** 0.5
    return area


a = float(input("Enter the length of the first side: "))
b = float(input("Enter the length of the second side: "))
c = float(input("Enter the length of the third side: "))

area = triangle_area(a, b, c)

print(area)

# a = 15 b = 13 c = 12 and Ans area = 74.83314