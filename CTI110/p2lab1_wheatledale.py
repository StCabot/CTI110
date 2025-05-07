#Dale Wheatle
#Feb 12,2025
#p2lab1
#variables and exspressions

#user inputs radius
radius=float(input("input radius here: "))

#getting the diameter,circumfrence,and area
import math
diameter=2*radius
circumfrence=2*math.pi*radius
area=math.pi*(radius**2)

#displaying results
print(f"the diameter of the circle is {diameter:.1f}")
print(f"the circumfrence of the circle is {circumfrence:.2f}")
print(f"the area of the circle is {area:.3f}")
