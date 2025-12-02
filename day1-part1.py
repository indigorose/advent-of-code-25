import csv

testTurns = []
with open('aoc25-day1-part1.csv', newline="") as inputfile:
    for row in csv.reader(inputfile):
        testTurns.append(row[0])
print(testTurns)


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
                difference = (steps % 100) + startingPoint
                startingPoint = 100 + (100-difference)
                if startingPoint == 0 or startingPoint == 100:
                    password += 1
            else:
                startingPoint = startingPoint + (steps % 100)
                if startingPoint == 0 or startingPoint == 100:
                    password += 1

    return password


print(passwordCounter(turns=['L68', 'L30', 'R48',
                             'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82']))
'''
If the dial is going left and the turn is greater than the starting point
the difference between them needs to be taken 100 to get the new starting point.
If the dial is going right and the turn is less than the starting point. 
Calculate the difference between the starting point and either 0 or 100 and
take it away from the turn to create the new starting point. 

Test splitting the turn to determine the direction and then apply the test.

'''
