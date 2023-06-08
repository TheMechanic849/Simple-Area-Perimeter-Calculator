def rectarea(sides):
    sides=sides.split('/')
    sides=list(map(float,sides))
    area = sides[0]*sides[1]
    print(f"Rectangle area = {area}")

def rectperimeter(sides):
    sides = sides.split('/')
    sides = list(map(float, sides))
    perimeter = (sides[0]*2)+(sides[1]*2)
    print(f"Rectangle perimeter = {perimeter}")