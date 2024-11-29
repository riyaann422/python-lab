def check_right_triangle(sides):
    sides.sort()
    if sides[2]**2 == sides [0]**2+sides[1]**2:
        return True
    return False

sides=[]
sides.append(int(input("Enter the hypontenuse :")))
sides.append(int(input("Enter base :")))
sides.append(int(input("Enter altitude:5 ")))
if check_right_triangle(sides):
    print("the given sides are part of right triangle")
else:
    print("the given sides are not a part of right triangle ")


