def getDirections(tuple3):
    x, y, z = tuple3
    return [
        (x,y,z+1),
        (x,y,z-1),
        (x,y+1,z),
        (x,y-1,z),
        (x+1,y,z),
        (x-1,y,z)
    ]