import random


def roll_die(number_of_rolls: int, number_of_sides: int) -> int:
    """ rolls a number of die and adds them together

    :param number_of_rolls: the number of dice to roll
    :param number_of_sides: the number of sides the dice have
    :precondition: all parameters are fulfilled
    :postcondition: returns an int
    :return: an int
    """
    total = 0
    for dice in range(0, number_of_rolls):
        total += random.randint(1, number_of_sides)
    return total


def heal_player(player_dictionary: dict, amount_healed: int, max_health: int) -> dict:
    """ heals the player

    :param player_dictionary: the players dictionary
    :param amount_healed: the amount of health to heal
    :param max_health: the maximum amount of health
    :return: modifies the players dictionary
    """
    if player_dictionary["health"] < max_health:
        player_dictionary["health"] += amount_healed
    if player_dictionary["health"] > max_health:
        player_dictionary["health"] = max_health
    return player_dictionary


def initiative() -> int:
    """ determines combat order

    :return: the outcome of the contested roll
    """
    initiative_one = roll_die(1, 20)
    initiative_two = roll_die(1, 20)
    if initiative_one == initiative_two:
        # the roll-off is a tie
        return 0
    elif initiative_one > initiative_two:
        # the player goes first
        return 1
    elif initiative_two > initiative_one:
        # the enemy goes first
        return 2


def attack_and_defend(attacker_dictionary: dict, defender_dictionary: dict) -> str:
    """ determines if the attacker hits

    :param attacker_dictionary: the character attacking dictionary
    :param defender_dictionary: the character defending dictionary
    :return: the state of opponent_two
    """
    hit = roll_die(1, 2)
    if hit == 1:
        print("Rolling a", hit, ",", attacker_dictionary["Name"], "landed a hit.\n")
        damage = roll_die(1, 6)
        print(attacker_dictionary["Name"], "swings toward", defender_dictionary["Name"], "dealing", damage, "damage.\n")
        defender_dictionary["health"] -= damage
        if defender_dictionary["health"] > 0:
            return "alive"
        else:
            return "dead"
    else:
        print("Rolling a", hit, ",", attacker_dictionary["Name"], "misses the attack.\n")
        return "miss"


def combat_process(attacker_status: str, defender_status: str, attacker_dictionary: dict, defender_dictionary: dict) -> int:
    """ one instance of combat

    the turn of each character

    :param attacker_status: the attackers status
    :param defender_status: the defenders status
    :param attacker_dictionary: the attacker dictionary
    :param defender_dictionary: the defender dictionary
    :return: prints out combat and combat messages
    """
    combat_messages(attacker_status, attacker_dictionary, defender_dictionary)
    if attacker_status in ("alive", "miss", "attacking"):
        defender_status = attack_and_defend(attacker_dictionary, defender_dictionary)
        combat_messages(defender_status, attacker_dictionary, defender_dictionary)
    if defender_status in ("alive", "miss"):
        attacker_status = attack_and_defend(defender_dictionary, attacker_dictionary)
        combat_messages(attacker_status, defender_dictionary, attacker_dictionary)
    if attacker_status == "dead":
        return 1
    elif defender_status == "dead":
        return 2
    else:
        return 0


def combat_messages(status: str, attacker_dictionary: dict, defender_dictionary: dict) -> print:
    """ displays whats happening in combat

    :param status: the status of the defender
    :param attacker_dictionary: the attacker dictionary
    :param defender_dictionary: the defender dictionary
    :return: prints various messages in combat
    """
    if status is "alive":
        print(defender_dictionary["Name"], "recoils from", str(attacker_dictionary["Name"]) + "'s attack, but",
              defender_dictionary["Name"], "stands tall with", defender_dictionary["health"], "HP and prepares to "
                                                                                              "counter attack.\n")
    if status is "miss":
        print(attacker_dictionary["Name"], "swings wide, as", defender_dictionary["Name"], "gracefully dodges the "
                                                                                           "attack.\n")
    if status is "dead":
        print(defender_dictionary["Name"], "falls dead on the ground.", attacker_dictionary["Name"],
              "walks away the victor.\n")
    if status is "attacking":
        print("\n" + attacker_dictionary["Name"], "rushes forwards, readying their weapon, as", defender_dictionary["Name"],
              "prepares to go on the defense.\n")


def combat_round(player_dictionary: dict, enemy_dictionary: dict) -> str:
    """ the round of combat

    :param player_dictionary: the first opponent (non initiative order)
    :param enemy_dictionary: the second opponent (non initiative order)
    :return: a round of combat
    """
    order = initiative()
    player_status = "alive"
    enemy_status = "alive"
    dead = 0
    while order == 0:
        order = initiative()
    if order == 1:
        player_status = "attacking"
        dead = combat_process(player_status, enemy_status, player_dictionary, enemy_dictionary)
    if order == 2:
        enemy_status = "attacking"
        dead = combat_process(enemy_status, player_status, enemy_dictionary, player_dictionary)
    whos_dead = who_died(order, dead)
    return whos_dead


def who_died(order: int, dead: int) -> str:
    """ determines whos died

    :param order: who attacks first
    :param dead: whos died
    :return: who died
    """
    whos_dead = ""
    if order == 1 and dead == 1:
        whos_dead = "player"
    elif order == 1 and dead == 2:
        whos_dead = "enemy"
    elif order == 2 and dead == 1:
        whos_dead = "enemy"
    elif order == 2 and dead == 2:
        whos_dead = "player"
    elif dead == 0:
        whos_dead = ""
    return whos_dead


def combat(player_dictionary: dict, enemy_dictionary: dict) -> int:
    """ the combat process

    :param player_dictionary: the players dictionary
    :param enemy_dictionary: the enemy's dictionary
    :return: if the game should end or not
    """
    whos_dead = ""
    while whos_dead == "":
        whos_dead = combat_round(player_dictionary, enemy_dictionary)
        input("Press \'Enter\' to continue.---------------------------------------------------------------------------")
    if whos_dead == "player":
        return 0
    elif whos_dead == "enemy":
        return 1


def combat_or_flee() -> str:
    """ asks if the user wants to flee a fight or not

    :return: the users answer
    """
    answer = input("Do you \'fight\' or do you \'flee\'? ")
    while answer.lower() not in ("fight", "flee"):
        answer = input("\nThat\'s not something you can do. Do you \'fight\' or do you \'flee\'? ")
    return answer.lower()


def flee(player_dictionary: dict) -> int:
    """ flees the battle

    :param player_dictionary: the players dictionary
    :return: whether the game should end or not
    """
    damage = roll_die(1, 4)
    player_dictionary["health"] -= damage
    print(f"\nAs you flee, the goblin swings out at you, dealing {damage} damage.")
    if player_dictionary["health"] > 0:
        print("You escape, hurt but alive.\n")
        return 1
    elif player_dictionary["health"] < 1:
        print("You fall to the floor, as the goblin drags your corpse away.\n")
        return 0


def combat_chance(player_dictionary: dict, enemy_dictionary: dict, encounter_chance: int) -> int:
    """ the chance to get attacked when moving

    :param player_dictionary: the players dictionary
    :param enemy_dictionary: the enemy dictionary
    :param encounter_chance: the percentage to get into a fight
    :return: whether the game should end or not
    """
    chance = roll_die(1, 100)
    end_the_game = 1
    if chance <= encounter_chance:
        print("You Enter the room, and in front of you stands a goblin.\n")
        answer = combat_or_flee()
        if answer == "fight":
            end_the_game = combat(player_dictionary, enemy_dictionary)
        elif answer == "flee":
            end_the_game = flee(player_dictionary)
    else:
        heal_player(player_dictionary, 2, 10)
    return end_the_game
