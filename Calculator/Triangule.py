def triangarea(base,height):
    area=(base*height)/2
    print(f"Triangle area = {area}")

def triangperimeter(base,sides):
    sides=sides.split("/")
    sides=list(map(float,sides))
    perimeter=base+sides[0]+sides[1]
    print(f"Triangle perimeter = {perimeter}")