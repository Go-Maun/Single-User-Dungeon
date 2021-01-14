from input import dungeon_size_input
from input import act_on_input
from input import get_input
from combat import combat_chance
from printDungeon import print_scenario
from instantiateDictionaries import create_dungeon_dictionary
from instantiateDictionaries import create_player_dictionary
from instantiateDictionaries import generate_hidden_keys
from instantiateDictionaries import create_exit_dictionary
from instantiateDictionaries import create_enemy_dictionary


def game():
    print("Welcome to a world of monsters! You have been captured by a hoard of goblins and are trying to escape.\n"
          "Search the dungeons for a means of escape.\n"
          "The larger the game board the harder the game gets, with that in mind,\n")
    x_max = dungeon_size_input("wide")
    y_max = dungeon_size_input("long")
    player_name = input("What is your name? ")
    room_dict = create_dungeon_dictionary(x_max, y_max)
    player_dict = create_player_dictionary(x_max, y_max, player_name.title())
    key_location_dict = generate_hidden_keys(room_dict, 3, 5)
    exit_dict = create_exit_dictionary(x_max, y_max)
    end_game = 1
    while end_game == 1:
        enemy_dict = create_enemy_dictionary()
        print_scenario(x_max, room_dict, player_dict, exit_dict)
        requested_input = get_input()
        if requested_input.lower() in ("north", "south", "east", "west"):
            act_on_input(requested_input, player_dict, x_max, y_max, key_location_dict, exit_dict)
            end_game = combat_chance(player_dict, enemy_dict, 25)
        elif requested_input.lower() == "quit":
            end_game = act_on_input(requested_input, player_dict, x_max, y_max, key_location_dict, exit_dict)
        elif requested_input.lower() == "help":
            act_on_input(requested_input, player_dict, x_max, y_max, key_location_dict, exit_dict)
        elif requested_input.lower() == "search":
            if int(player_dict["inventory"][1][0]) == 3 and player_dict["position"] == exit_dict["position"]:
                end_game = act_on_input(requested_input, player_dict, x_max, y_max, key_location_dict, exit_dict)
            else:
                act_on_input(requested_input, player_dict, x_max, y_max, key_location_dict, exit_dict)


def main():
    game()


if __name__ == "__main__":
    main()
