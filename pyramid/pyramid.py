#!/usr/bin/python

# open data file
with open('pyramid.txt', 'r') as f:
    data = f.readlines()

# initalize matrix
matrix = []

# add rows to matrix
for i in range(12):
    row = []
    for j in range(60):
        row.append(' ')
    matrix.append(row)


# function for printing the final matrix
def print_matrix(full_matrix):
    for col in full_matrix:
        row_string = ''
        for cell in col:
            # the matrix does not display 0, as it is the filler of the
            # pyramids
            if cell != '0':
                row_string += cell
            else:
                row_string += ' '
        print row_string


# function gets all points for a specific value pair
def get_points(center, height):
    x_int = []
    # each point is a dictionary with three attributes: x, y, and display
    #
    # x and y are simply coordinates sent to matrix. They should have values
    # that are positive integers.
    #
    # display is the character that shows up on the matrix. Forward slashes
    # and backslashes are used for the edges of the pyramid, while an underscore
    # is used for the top of a pyramid and a zero is used for the inside of a
    # pyramid. Zeros are not printed. Points with a display of 0 are called
    # filler points
    points = [
        {
            'x': center,
            'y': height,
            'display': '_'
        }
    ]
    # this loop puts filler points in the middle column of the pyramid
    for y in range(height):
        points.append({
            'x': center,
            'y': y,
            'display': '0'
        })
    # the next two lines put the two x-intercepts of a pyramid into a list
    x_int.append(center - height)
    x_int.append(center + height)
    # this loop runs one time for each x-intercept.
    for i in range(2):
        x = x_int[i]
        if i == 0:
            # if i == 0, the first x-intercept is being used, which means
            # the value of b in y=mx+b is negative and that the slope of the
            # line will be positive
            b = -1 * x
        else:
            # i == 1, so the second x-intercept is being used, which means that
            # the value of b in y=mx+b is positive and that the slope of the
            # line is negative
            b = 1 * x
        # this loop adds the edge points to the array of points
        for y in range(height):
            # this system solves for x in terms of y, so the new_x variable is
            # from the equation x=(y-b)/m. y is the iteration in the loop, m is
            # +/-1, and b is -1(x-int)
            if i == 1:
                new_x = -1 * (y - b)
                # because the slope is -1 and the pyramid is going down, use \
                display_for_use = '\\'
            else:
                new_x = y - b
                # use / because the slope is +1 and the pyramid is going up
                display_for_use = '/'
            points.append({
                'x': new_x,
                'y': y,
                'display': display_for_use
            })
            # add filler characters
            for alt_y in range(y):
                points.append({
                    'x': new_x,
                    'y': alt_y,
                    'display': '0'
                })
    return points

# go through each data pair and set all of their points on the matrix
for line in data:
    values = line.split()
    center = int(values[0])
    height = int(values[1])
    current_points = get_points(center, height)
    if height != 0:
        for coordinate in current_points:
            if matrix[11 - coordinate['y']][coordinate['x']] == ' ':
                matrix[11 - coordinate['y']][coordinate['x']] = coordinate['display']

# print matrix
print_matrix(matrix)
# print ruler
print('0123456789' * 6)
