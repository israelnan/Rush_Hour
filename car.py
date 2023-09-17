#################################################################
# FILE : car.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: A class containing car for the game and all of its methods.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
# NOTES:
#################################################################



class Car:
    """
    Class for representing each car object with its attributes.
    """
    def __init__(self, name: str, length: int, location: tuple[int, int], orientation: int) -> None:
        """
        A constructor for a Car object
        :param name: A string representing the car's name
        :param length: A positive int representing the car's length.
        :param location: A tuple representing the car's head (row, col) location
        :param orientation: One of either 0 (VERTICAL) or 1 (HORIZONTAL)
        """
        self.__name = name
        self.__length = length
        self.__location = location
        self.__orientation = orientation

    def car_coordinates(self) -> list[tuple[int, int]]:
        """
        :return: A list of coordinates the car is in
        """
        coordinates = []
        i = 0
        while i < self.__length:
            if self.__orientation == 1:
                coordinates.append((self.__location[0], self.__location[1] + i))
                i += 1
            elif self.__orientation == 0:
                coordinates.append((self.__location[0] + i, self.__location[1]))
                i += 1
        return coordinates

    def possible_moves(self) -> dict:
        """
        :return: A dictionary of strings describing possible movements permitted by this car.
        """
        if self.__orientation == 0:
            return {'u': 'you can move the car up', 'd': 'you can move the car down'}
        elif self.__orientation == 1:
            return {'r': 'you can move the car to the right', 'l': 'you can move the car to the left'}

    def movement_requirements(self, movekey: str) -> list[tuple[int, int]]:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: A list of cell locations which must be empty in order for this move to be legal.
        """
        if movekey == 'u':
            return [(self.__location[0]-1, self.__location[1])]
        elif movekey == 'd':
            return [(self.__location[0]+self.__length, self.__location[1])]
        elif movekey == 'l':
            return [(self.__location[0], self.__location[1]-1)]
        elif movekey == 'r':
            return [(self.__location[0], self.__location[1]+self.__length)]

    def move(self, movekey: str) -> bool:
        """ 
        :param movekey: A string representing the key of the required move.
        :return: True upon success, False otherwise
        """
        if movekey in self.possible_moves().keys():
            i, j = self.__location
            if movekey == 'u':
                self.__location = (i-1, j)
            elif movekey == 'd':
                self.__location = (i+1, j)
            elif movekey == 'r':
                self.__location = (i, j+1)
            elif movekey == 'l':
                self.__location = (i, j-1)
            return True
        return False

    def get_name(self) -> str:
        """
        :return: The name of this car.
        """
        return self.__name

    def get_location(self) -> tuple[int, int]:
        """
        :return: The current location of this car.
        """
        return self.__location


if __name__ == '__main__':
    red = Car('R', 3, (0, 0), 1)
    print(red.get_location())
