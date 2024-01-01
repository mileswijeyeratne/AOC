def draw_line(point1, point2):
    output = []
    if point1[0] == point2[0]:
        for y in range(min(point1[1], point2[1]), max(point1[1], point2[1])+1):
            output.append((point1[0], y))
    elif point1[1] == point2[1]:
        for x in range(min(point1[0], point2[0]), max(point1[0], point2[0])+1):
            output.append((x, point1[1]))
    return output

def find_sand_pos(cur_pos, points):
    x = cur_pos[0]
    y = cur_pos[1]
    if not (x, y+1) in points:
        return False, (x, y+1)
    elif not (x-1, y+1) in points:
        return False, (x-1, y+1)
    elif not (x+1, y+1) in points:
        return False, (x+1, y+1)
    else:
        return True, (x, y)

