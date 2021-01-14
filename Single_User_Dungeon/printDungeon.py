import doctest


def print_scenario(x_maximum: int, room_dictionary: dict, player_dictionary: dict, exit_dictionary: dict) -> print:
    """ prints the scenario

    :param x_maximum: the max x int
    :param room_dictionary: the rooms x/y dictionary
    :param player_dictionary: the players dictionary
    :param exit_dictionary: the exit location
    :precondition: all parameters are met
    :postcondition: prints the scenario
    :return: prints the room
    """
    print_room(x_maximum, room_dictionary, player_dictionary, exit_dictionary)
    print_hud(player_dictionary)


def print_room(x_maximum: int, room_dictionary: dict, player_dictionary: dict, exit_dictionary: dict) -> print:
    """ prints the game board

    :param x_maximum: the max x int
    :param room_dictionary: the rooms x/y dictionary
    :param player_dictionary: the players dictionary
    :param exit_dictionary: the exit location
    :precondition: all parameters are met
    :postcondition: prints the room
    :return: prints the board

    >>> print_room(5, {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}, {"position":[0,0]}, {"position": [4,4]})
    ◘ X X X X
    X X X X X
    X X X X X
    X X X X X
    X X X X ◙
    """
    for y in room_dictionary:
        for x in room_dictionary[y]:
            x_y_current_print_position = [x, y]
            if x_y_current_print_position == player_dictionary["position"]:
                print_player(x_maximum, x)
            elif x_y_current_print_position == exit_dictionary["position"]:
                print_exit(x_maximum, x)
            else:
                print_tile(x_maximum, x)


def print_hud(player_dictionary: dict) -> print:
    """ prints the players information

    :param player_dictionary: the players dictionary
    :precondition: a dictionary is provided
    :postcondition: prints the player information
    :return: the player information

    >>> print_hud({"health": 7, "inventory": ["sword", "Apple"]})
    <BLANKLINE>
    Health: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ○ ○ ○
    Inventory: sword,  Apple
    <BLANKLINE>
    """
    print('')
    print_player_health(player_dictionary, 10)
    print_player_items(player_dictionary)
    print('')


def print_player_items(player_dictionary: dict) -> print:
    """ prints the players items

    :param player_dictionary: the players dictionary
    :precondition: dictionary parameter provided
    :postcondition: prints the players items
    :return: the players inventory

    >>> print_player_items({"inventory":["Sword", "Apple"]})
    Inventory: Sword,  Apple
    """
    print("Inventory:", end=" ")
    item_number = 0
    for items in player_dictionary["inventory"]:
        if item_number == len(player_dictionary["inventory"]) - 1:
            print(items)
        else:
            print(str(items) + ", ", end=" ")
            item_number += 1


def print_player_health(player_dictionary: dict, max_health: int) -> print:
    """ prints the players health

    :param player_dictionary: the players dictionary
    :param max_health: the maximum health
    :precondition: all parameters are met
    :postcondition: prints the players health
    :return: the players health

    >>> print_player_health({"health": 7}, 10)
    Health: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ○ ○ ○
    """
    health = player_dictionary["health"]
    hearts_printed = 0
    print("Health: ", end="")
    while hearts_printed < max_health:
        if hearts_printed < health:
            if hearts_printed < max_health - 1:
                print("♥", end=" ")
                hearts_printed += 1
            else:
                print("♥")
                hearts_printed += 1
        else:
            if hearts_printed < max_health - 1:
                print("○", end=" ")
                hearts_printed += 1
            else:
                print("○")
                hearts_printed += 1


def print_tile(x_maximum: int, x: int) -> print:
    """ prints the floor tile

    :param x_maximum: the maximum x value
    :param x: the current x value
    :precondition: all parameters are met
    :postcondition: prints the floor tile
    :return: prints a tile

    >>> print_tile(4, 3)
    X\n
    """
    if x == x_maximum - 1:
        print("X")
    else:
        print("X", end=" ")


def print_player(x_maximum: int, x: int):
    """ prints the player

    :param x_maximum: the maximum x value
    :param x: the current x value
    :precondition: all parameters are met
    :postcondition: prints the player
    :return: prints the player

    >>> print_player(4, 3)
    ◘\n
    """
    if x == x_maximum - 1:
        print("◘")
    else:
        print("◘", end=" ")


def print_exit(x_maximum: int, x: int) -> print:
    """ prints the exit

    :param x_maximum: the maximum x value
    :param x: the current x value
    :precondition: all parameters are met
    :postcondition: prints the exit
    :return: prints the exit

    >>> print_exit(4, 3)
    ◙\n
    """
    if x == x_maximum - 1:
        print("◙")
    else:
        print("◙", end=" ")


if __name__ == "__main__":
    doctest.testmod()
