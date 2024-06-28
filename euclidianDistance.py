import math as mt

def find_euclidianDistance(firstCoordinate, secondCoordinate):
    return mt.sqrt((firstCoordinate[0]-secondCoordinate[0])**2 + (firstCoordinate[1]-secondCoordinate[1])**2)

points = [(1, 2), (4, 6), (5, 1), (3, 3)]

distances = []

for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = find_euclidianDistance(points[i], points[j])
        distances.append(distance)

min_distance = min(distances)

print(min_distance)
