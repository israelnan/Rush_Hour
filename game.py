#################################################################
# FILE : game.py
# WRITER : israel_nankencki , israelnan , 305702334
# EXERCISE : intro2cs2 ex9 2021
# DESCRIPTION: A class containing main game activations and all of its methods.
# STUDENTS I DISCUSSED THE EXERCISE WITH: none.
# WEB PAGES I USED: none
# NOTES:
#################################################################


from car import Car
from board import Board

MESSAGE = {'request_move': 'please enter your move', 'invalid': "your input isn't valid",
           'start_game': 'the game is ready, good luck', 'win': 'congratulations, you won!'}
VALID_CAR_NAMES = 'YBOGWR'
VALID_MOVES = 'udrl'
VALID_ORIENTATION = [0, 1]
VALID_LENGTH = [2, 3, 4]
END_KEY = '!'


class Game:
    """
    A class for managing the game itself, with all of its action.
    """

    def __init__(self, board: Board):
        """
        Initialize a new Game object.
        :param board: An object of type board
        """
        self.__board = board

    def validity_check(self, user_input: str) -> bool:
        """
        this function checks whether the users' input is valid and fit for the game.
        :param user_input: a string of 3 characters - the name, a coma, and direction to move to.
        :return: True if its valid, otherwise False.
        """
        if len(user_input) == 3 and user_input[1] == ',':
            if user_input[0] in VALID_CAR_NAMES and user_input[2] in VALID_MOVES:
                if self.__board.move_car(user_input[0], user_input[2]):
                    return True
        print(MESSAGE['invalid'])
        return False

    def __single_turn(self) -> str:
        """
        this function asks repetitively input from the user, and moves the accordingly.
        :return: the user input when the game break.
        """
        user_input = input(MESSAGE['request_move'])
        while user_input != END_KEY and not self.validity_check(user_input):
            Board.move_car(self.__board, user_input[0], user_input[2])
            user_input = input(MESSAGE['request_move'])
        return user_input

    def play(self) -> None:
        """
        The main driver of the Game. Manages the game until completion.
        :return: None
        """
        print(MESSAGE['start_game'])
        print(str(self.__board))
        while self.__single_turn() != END_KEY:
            print(str(self.__board))
            if self.__board.cell_content((3, 7)) == 'R':
                print(MESSAGE['win'])
                break


def cars_key_validation(car_dict: dict[str: list]) -> None:
    """
    this function helps to check the cars specifications validation while loading it to the games' board.
    :param car_dict: A dict with the cars' requested name as key, with a list of its specifications as value.
    :return: None
    """
    if key not in VALID_CAR_NAMES:
        print(key + "isn't a valid name for a car, please fix your car configuration file and activate the game"
                    " again")
        sys.exit()
    if car_dict[key][2] not in VALID_ORIENTATION:
        print(str(car_dict[key][2]) + "isn't a valid orientation for a car, please fix your car configuration "
                                      "file and activate the game again")
        sys.exit()
    if car_dict[key][0] not in VALID_LENGTH:
        print(str(car_dict[key][0]) + "isn't a valid length for a car, please fix your car configuration "
                                      "file and activate the game again")
        sys.exit()
    if not 0 <= car_dict[key][1][0] < 7 or not 0 <= car_dict[key][1][1] < 7:
        print(str(car_dict[key][1]) + "isn't within the game board length and height, please fix your car "
                                      "configuration file and activate the game again")
        sys.exit()


if __name__ == "__main__":
    import helper
    import sys
    boar = Board()
    cars_dict = helper.load_json(sys.argv[1][1:len(sys.argv[1]) - 1])
    for key in cars_dict:
        cars_key_validation({key: cars_dict[key]})
        car = Car(key, cars_dict[key][0], (cars_dict[key][1][0], cars_dict[key][1][1]), cars_dict[key][2])
        boar.add_car(car)
    game = Game(boar)
    game.play()
