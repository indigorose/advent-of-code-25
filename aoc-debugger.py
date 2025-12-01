def passwordCounter(turns):
    startingPoint = 50

    password = 0

    for i in turns:
        direction = i[0:1]  # direction
        steps = int(i[1:])   # turns
        if direction == 'L':
            if steps > startingPoint:
                difference = startingPoint-(steps % 100)
                startingPoint = 100+difference
                if startingPoint == 0 or startingPoint == 100:
                    password += 1
            else:
                startingPoint = startingPoint - (steps % 100)
                if startingPoint == 0 or startingPoint == 100:
                    password += 1
        elif direction == "R":
            if steps < startingPoint:
                difference = steps + startingPoint
                startingPoint = 100 - (difference-100)
                if startingPoint == 0 or startingPoint == 100:
                    password += 1
            else:
                startingPoint = startingPoint + (steps % 100)
                if startingPoint == 0 or startingPoint == 100:
                    password += 1

    return password


print(passwordCounter(turns=['L68', 'L30', 'R48',
                             'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']))