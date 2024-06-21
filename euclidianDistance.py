import math as mt
def get_tuple_from_user():
    first_coordinate = input("İlk koordinatı aralarında ',' olacak şekilde girin: ")
    second_coordinate = input("İkinci koordinatı aralarında ',' olacak şekilde girin: ")

    first_coordinate = tuple(map(int, first_coordinate.split(',')))
    second_coordinate = tuple(map(int, second_coordinate.split(',')))

    return first_coordinate, second_coordinate

def find_euclidianDistance(firstCoordinate, secondCoordinate):
    substract_x = firstCoordinate[0] - secondCoordinate[0]
    substract_y = firstCoordinate[1] - secondCoordinate[1]

    return mt.sqrt(mt.pow(substract_x,2) + mt.pow(substract_y,2))


coordinates = get_tuple_from_user()
print(find_euclidianDistance(coordinates[0],coordinates[1]))
