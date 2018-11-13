#!/user/bin/python

# open data file
with open('skyline.txt', 'r') as f:
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
            if cell != '0':
                row_string += cell
            else:
                row_string += ' '
        print row_string

# function gets all points for a specific value pair
def get_points(center, height):
    m = 1
    x_int = []
    points = [
        {
            'x': center,
            'y': height,
            'display': '_'
        }
    ]
    for y in range(height):
        points.append({
            'x': center,
            'y': y,
            'display': '0'
        })
    x_int.append(center - height)
    x_int.append(center + height)

    for i in range(2):
        x = x_int[i]
        if i == 0:
            b = -1 * x
        else:
            b = 1 * x
        for y in range(height):
            if i == 1:
                new_x = -1 * (y - b)
                display_for_use = '\\'
            else:
                new_x = y - b
                display_for_use = '/'
            points.append({
                'x': new_x,
                'y': y,
                'display': display_for_use
            })
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
            #print str(coordinate['x']) + ' // ' + str(coordinate['y']) + ' Display: ' + coordinate['display']
            if matrix[11 - coordinate['y']][coordinate['x']] == ' ':
                matrix[11 - coordinate['y']][coordinate['x']] = coordinate['display']

# print matrix
print_matrix(matrix)
# print ruler
print('0123456789' * 6)
