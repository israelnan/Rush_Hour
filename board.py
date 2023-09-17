#################################################################
# FILE : board.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: A class containing board for the game and all of its methods.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
# NOTES:
#################################################################


from typing import Optional
from car import Car


class Board:
    """
    A class for representing  board object in the game rush hour.
    its purpose is to set and manage the game board with its actions.
    """

    def __init__(self):
        self.__board = [['_'] * 7 for _ in range(7)]
        self.__board[3].append('E')
        self.__cars_in_the_board = []

    def __str__(self):
        """
        This function is called when a board object is to be printed.
        :return: A string of the current status of the board
        """
        return str(self.__board)

    def cell_list(self) -> list[tuple[int, int]]:
        """ This function returns the coordinates of cells in this board
        :return: list of coordinates
        """
        coordinates = []
        for i in range(len(self.__board)):
            for j in range(len(self.__board[i])):
                coordinates.append((i, j))
        return coordinates

    def possible_moves(self) -> list[tuple[str, str, str]]:
        """ This function returns the legal moves of all cars in this board
        :return: list of tuples of the form (name,movekey,description) 
                 representing legal moves
        """
        legal_moves_list = []
        for car in self.__cars_in_the_board:
            moves = car.possible_moves()
            for move in moves.keys():
                one_move = car.movement_requirements(move)
                if one_move[0] in self.cell_list() and self.cell_content(one_move[0]) != car.get_name():
                    legal_moves_list.append((car.get_name(), move, moves[move]))
        return legal_moves_list

    def target_location(self) -> tuple[int, int]:
        """
        This function returns the coordinates of the location which is to be filled for victory.
        :return: (row,col) of goal location
        """
        for i, x in enumerate(self.__board):
            if 'E' in x:
                return i, x.index('E')

    def cell_content(self, coordinate: tuple[int, int]) -> Optional[str]:
        """
        Checks if the given coordinates are empty.
        :param coordinate: tuple of (row,col) of the coordinate to check
        :return: The name if the car in coordinate, None if empty
        """
        not_to_check = '_E'
        if self.__board[coordinate[0]][coordinate[1]] not in not_to_check:
            return self.__board[coordinate[0]][coordinate[1]]
        return None

    def cells_helper(self, coordinates_list: list[tuple[int, int]]) -> bool:
        """
        this function checks for list of all car coordinates if it's empty or not.
        :param coordinates_list: a list of tuples with coordinates.
        :return: True if all coordinates available, False otherwise.
        """
        for cell in coordinates_list:
            if self.cell_content(cell) is not None:
                return False
        return True

    def add_car(self, car: Car) -> bool:
        """
        Adds a car to the game.
        :param car: car object of car to add
        :return: True upon success. False if failed
        """
        if car.get_name() not in self.__board:
            car_coordinates = car.car_coordinates()
            for coor in car_coordinates:
                if coor not in self.cell_list():
                    return False
            if self.cells_helper(car_coordinates):
                for i in car_coordinates:
                    self.__board[i[0]][i[1]] = car.get_name()
                self.__cars_in_the_board.append(car)
                self.possible_moves()
                return True
        return False

    def move_car(self, name: str, movekey: str) -> bool:
        """
        moves car one step in given direction.
        :param name: name of the car to move
        :param movekey: Key of move in car to activate
        :return: True upon success, False otherwise
        """
        for car in self.__cars_in_the_board:
            if name == car.get_name():
                cell_to_move = car.movement_requirements(movekey)
                car_current_coordinates = car.car_coordinates()
                if cell_to_move[0] in self.cell_list() and self.cell_content(cell_to_move[0]) is None:
                    self.__board[cell_to_move[0][0]][cell_to_move[0][1]] = name
                    if movekey in 'lu':
                        self.__board[car_current_coordinates[-1][0]][car_current_coordinates[-1][1]] = '_'
                    elif movekey in 'rd':
                        self.__board[car_current_coordinates[0][0]][car_current_coordinates[0][1]] = '_'
                    return car.move(movekey)
        return False


if __name__ == '__main__':
    board = Board()
    print(board.cell_list())
