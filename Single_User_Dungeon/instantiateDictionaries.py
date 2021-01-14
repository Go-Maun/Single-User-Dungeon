import random
import doctest


def create_dungeon_dictionary(x_maximum: int, y_maximum: int) -> dict:
    """ creates the dungeons dictionary

    :param x_maximum: the maximum x value
    :param y_maximum: the maximum y value
    :precondition: positive ints above 3
    :postcondition: instantiates the dungeon dictionary
    :return: the dungeons dictionary

    >>> create_dungeon_dictionary(3, 3)
    {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2]}

    >>> create_dungeon_dictionary(1, 5)
    {0: [0], 1: [0], 2: [0], 3: [0], 4: [0]}
    """
    room_dictionary = {y: [x for x in range(0, x_maximum)] for y in range(0, y_maximum)}
    return room_dictionary


def create_player_dictionary(x_maximum: int, y_maximum: int, name: str) -> dict:
    """ creates the players dictionary

    :param x_maximum: the maximum x value
    :param y_maximum: the maximum y value
    :param name: the input name
    :precondition: positive ints above 3, and a string
    :postcondition: instantiates the player dictionary
    :return: the players dictionary
    """
    return {"position": [random.randint(0, x_maximum - 1), random.randint(0, y_maximum - 1)], "Name": name,
            "inventory": ["Sword", "0 keys"], "health": 10}


def create_enemy_dictionary() -> dict:
    """ creates the enemy dictionary

    :return: the enemy dictionary

    >>> create_enemy_dictionary()
    {'Name': 'Goblin', 'health': 5}
    """
    return {"Name": "Goblin", "health": 5}


def create_exit_dictionary(x_maximum: int, y_maximum: int) -> dict:
    """ creates a location for the exit

    :param x_maximum: the maximum x value
    :param y_maximum: the maximum y value
    :precondition: positive ints above 3
    :postcondition: instantiates the exit dictionary
    :return: an exit dictionary
    """
    return {"position": [random.randint(0, x_maximum - 1), random.randint(0, y_maximum - 1)]}


def generate_hidden_keys(room_dictionary: dict, number_of_keys: int, percentage_to_clear: int) -> dict:
    """

    :param room_dictionary: the rooms dictionary
    :param number_of_keys: the number of keys to be created
    :param percentage_to_clear: the chance for a tile to have a key
    :return: the key location dictionary
    """
    key_dictionary = {}
    created = 0
    while created != number_of_keys:
        for y in room_dictionary:
            for x in room_dictionary[y]:
                percent = random.randint(1, 100)
                if created < number_of_keys:
                    if percent <= percentage_to_clear:
                        if y not in key_dictionary:
                            key_dictionary[y] = [x]
                            created += 1
                        else:
                            key_dictionary[y].append(x)
                            created += 1
    return key_dictionary


if __name__ == "__main__":
    doctest.testmod()
