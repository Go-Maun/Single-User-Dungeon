def dungeon_size_input(prompt: str) -> int:
    """ the players chosen dungeon size

    :param prompt: the direction of the room
    :precondition: prompt is a string
    :postcondition: returns the users choice
    :return: the chosen maximum
    """
    print("How", prompt, "is the dungeon? Minimum size is 3: ", end="")
    maximum = int(input(""))
    while maximum < 3:
        maximum = int(input(f"{maximum} is less than 3, try again: "))
    return maximum


def get_input() -> str:
    """ gets input from the user

    :return: the users input
    """
    print("Actions you can do:\n"
          "\n\'north\'  - moves your character up"
          "\n\'south\'  - moves your character down"
          "\n\'east\'   - moves your character right"
          "\n\'west\'   - moves your character left"
          "\n\'search\' - searches the current room you're in"
          "\n\'help\'   - explain any inputs in more depth"
          "\n\'quit\'   - quits the game")
    user_input = input("what do you want to do: ")
    print("")
    return user_input


def act_on_input(user_input: str, player_dictionary: dict, x_maximum: int, y_maximum: int, key_location_dictionary: dict, exit_dictionary: dict):
    """ calls various functions based on input

    :param user_input: the users chosen input
    :param player_dictionary: the players dictionary
    :param x_maximum: the maximum x value
    :param y_maximum: the maximum y value
    :param key_location_dictionary: the key locations
    :param exit_dictionary: the exit dictionary
    :precondition: all parameters are fufilled
    :postcondition: calls a function depending on input
    :return: calls various functions based on input
    """
    if user_input.lower() in ("north", "south", "east", "west"):
        player_dictionary = move_player(user_input, player_dictionary, x_maximum, y_maximum)
        return player_dictionary
    elif user_input.lower() == "help":
        input_help()
    elif user_input.lower() == "quit":
        return quit_game()
    elif user_input.lower() == "search":
        search(player_dictionary, key_location_dictionary, exit_dictionary)


def cant_move_minimum(position: int, player_dictionary: dict):
    """ determines if the player can move up and left or not

    :param position: the x or y position of the player dictionary
    :param player_dictionary: the player dictionary
    :precondition: all parameters are fulfilled
    :postcondition: modifies the location
    :return: modifies the players location
    """
    if player_dictionary["position"][position] != 0:
        player_dictionary["position"][position] -= 1


def cant_move_maximum(position, player_dictionary, maximum):
    """ determines if the player can move down and right or not

        :param position: the x or y position of the player dictionary
        :param player_dictionary: the player dictionary
        :param maximum: the maximum x or y value
        :precondition: all parameters are fulfilled
    :postcondition: modifies the location
        :return: modifies the players location
        """
    if player_dictionary["position"][position] != maximum - 1:
        player_dictionary["position"][position] += 1


def move_player(user_input: str, player_dictionary: dict, x_maximum: int, y_maximum: int) -> dict:
    """ moves the player based on the input

    :param user_input: the users input choice
    :param player_dictionary: the players dictionary
    :param x_maximum: the maximum x value
    :param y_maximum: the maximum y value
    :precondition: all parameters are fulfilled
    :postcondition: modifies the location
    :return: the modified player dictionary
    """
    if user_input.lower() == "north":
        cant_move_minimum(1, player_dictionary)
    elif user_input.lower() == "south":
        cant_move_maximum(1, player_dictionary, y_maximum)
    elif user_input.lower() == "east":
        cant_move_maximum(0, player_dictionary, x_maximum)
    elif user_input.lower() == "west":
        cant_move_minimum(0, player_dictionary)
    return player_dictionary


def search(player_dictionary: dict, key_location_dictionary: dict, exit_dictionary: dict):
    """ searches the room

    :param player_dictionary: the players dictionary
    :param key_location_dictionary: the key locations
    :param exit_dictionary: the exit location
    :precondition: all parameters are fulfilled
    :postcondition: modifies the inventory
    :return: the outcome of the search
    """
    current_y = player_dictionary["position"][1]
    current_x = player_dictionary["position"][0]
    item_found = False
    if current_y in key_location_dictionary:
        if current_x in key_location_dictionary[current_y]:
            give_key(player_dictionary)
            key_location_dictionary[current_y].remove(current_x)
            item_found = True
    if current_y == exit_dictionary["position"][1]:
        if current_x == exit_dictionary["position"][0]:
            interact_with_exit(player_dictionary)
            item_found = True
    if not item_found:
        print("You search and search, but the room is empty.\n")


def interact_with_exit(player_dictionary: dict) -> print:
    """ interacts with the exit

    :param player_dictionary: the players dictionary
    :precondition: all parameters are fulfilled
    :postcondition: prints story
    :return: prints some story
    """
    if int(player_dictionary["inventory"][1][0]) != 3:
        print("You glance around, and spot a ladder with a locked hatch. The hatch has 3 key holes.\n")
    elif int(player_dictionary["inventory"][1][0]) == 3:
        print("You insert each key into the respective key hole. One by one the locks clang on the ground as the "
              "ladder hatch swings open.\nFreedom is yours, you escaped the goblins den.")
        return 0


def give_key(player_dictionary: dict) -> print:
    """ gives the player a key

    :param player_dictionary: the players dictionary
    :precondition: all parameters are fulfilled
    :postcondition: modifies the players inventory
    :return: adds a key to the players dictionary
    """
    item_slot = int(player_dictionary["inventory"][1][0])
    item_slot += 1
    player_dictionary["inventory"][1] = f"{item_slot} keys"
    print("You search the room, and a glint catches your eye.\nA shiny golden key sits besides a hay bed roll.\n")


def input_help():
    """ asks the user what they need clarification on

    :return: prints a helpful message
    """
    help_required = input("What input do you need explained? ")
    print("")
    if help_required.lower() in ("north", "south", "east", "west"):
        print("This is a movement input. If", help_required.lower(), "is input, the character will move",
              help_required.lower(), "relative to the \'◘\' character. (Moves character)")
    elif help_required.lower() == "search":
        print("This is a search input. It will allows you to find useful items to use on your adventure, and to gain "
              "information on certain tiles. (Searches current floor tile)")
    elif help_required.lower() == "help":
        print("This is a help input. I know your\'e only in here to not think about the horrific monsters out there, "
              "but how else will you escape this decrepit dungeon. (You are in the help already)")
    elif help_required.lower() == "quit":
        print("This is a quit input. This will end the game, and wont save your progress.")
    else:
        print(help_required.title(), "isn\'t an input I can tell you about.")
    print("")


def quit_game():
    """ quits the game if the user wants to

    :return: whether the user wants to quit or not
    """
    answer = input("Are you sure you want to quit? Your progress will be lost. Type \'yes\' or \'no\'. ")
    loop = 1
    while loop:
        if answer.lower() == "yes":
            return 0
        elif answer.lower() == "no":
            print("")
            return 1
        else:
            answer = input("That isn\'t an answer. Try again. ")