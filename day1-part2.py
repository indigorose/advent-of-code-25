import csv

testTurns = []
with open('aoc25-day1-part1.csv', newline="") as inputfile:
    for row in csv.reader(inputfile):
        testTurns.append(row[0])
# print(testTurns)


def passwordCounter(turns):
    starting_point = 50

    password = 0
    zero_points = 0
    # If the dial is turning left and steps are greater than the starting point

    for i in turns:
        direction = i[0:1]  # direction
        steps = int(i[1:]) % 100  # turns
        if direction == "L":
            # How many steps back to the starting point
            if steps > starting_point:
                if starting_point-steps % 100 < 0:
                    zero_points += 1
                starting_point = 100 - (steps - starting_point)
            else:
                starting_point = starting_point - steps
        elif direction == "R":
            # How many steps to the starting point
            if steps < starting_point:
                if starting_point + steps > 100:
                    zero_points += 1
                starting_point = steps - (100 - starting_point)
            else:
                starting_point = steps + starting_point
        if starting_point == 0 or starting_point == 100:
            password += 1
            zero_points += 1
            starting_point = 0
    return f'{password, zero_points}'


print(passwordCounter(testTurns))  # Answer is 1097
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
