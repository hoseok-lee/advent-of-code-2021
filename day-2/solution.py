import numpy as np



'''
    PROCESS INPUTS
'''

# Open and parse input text
with open("instructions.txt", "r") as f:
    raw_lines = f.read()

# Split by new line and direction and step
instructions = [
    [line.split()[0], int(line.split()[1])]

    for line in raw_lines.split('\n')
]



'''
    PART ONE: TRAVEL WITH DIRECTIONS

    Complexity: O(n)
    
    Iterate through the instructions and keep track of current coordinates.
'''
'''
positions = np.array([
    [
        step * int(direction == "forward"), 
        step * {
            "up": -1, 
            "down": 1,
            "forward": 0
        }[direction]
    ]

    for direction, step in instructions
])

print(np.prod(np.sum(positions, axis=0)))
'''


'''
    PART TWO: TRAVEL WITH AIM

    Complexity: O(n)
    
    Keep track of aim while doing the same process. The solution above does not
    work, since it assumes that there are only cardinal directions to work with.
    There is now a cumulative variable to be kept.
'''

aim = 0
x, y = 0, 0

for direction, step in instructions:
    aim += step * (1 if (direction == "down") else -1 if (direction == "up") else 0)
    
    if direction == "forward":
        x += step
        y += step * aim

print(x * y)