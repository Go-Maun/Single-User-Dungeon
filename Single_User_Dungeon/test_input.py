from unittest import TestCase
from unittest.mock import patch
import io
from A01172483_1510_assignments.A3.input import dungeon_size_input
from A01172483_1510_assignments.A3.input import get_input
from A01172483_1510_assignments.A3.input import search
from A01172483_1510_assignments.A3.input import interact_with_exit
from A01172483_1510_assignments.A3.input import give_key
from A01172483_1510_assignments.A3.input import input_help


class TestDungeon_size_input(TestCase):
    @patch("builtins.input", side_effect=["4"])
    def test_dungeon_size_input_4(self, mock_input):
        expected_value = 4
        actual_value = dungeon_size_input("wide")
        self.assertEqual(expected_value, actual_value)

    @patch("builtins.input", side_effect=["2", "4"])
    def test_dungeon_size_input_wrong_then_4(self, mock_input):
        expected_value = 4
        actual_value = dungeon_size_input("wide")
        self.assertEqual(expected_value, actual_value)


class TestGet_input(TestCase):
    @patch('builtins.input', side_effect=["north"])
    def test_get_input_north(self, mock_input):
        expected_value = "north"
        actual_value = get_input()
        self.assertEqual(expected_value, actual_value)

    @patch('builtins.input', side_effect=["search"])
    def test_get_input_search(self, mock_input):
        expected_value = "search"
        actual_value = get_input()
        self.assertEqual(expected_value, actual_value)


class TestCant_move_minimum(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_key(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "0 Keys"]}
        key_dict = {2: [2]}
        exit_dict = {"position": [2, 4]}
        expected_value = "You search the room, and a glint catches your eye.\nA shiny golden key sits besides a hay " \
                         "bed roll.\n\n"
        search(player_dict, key_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_nothing(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "0 Keys"]}
        key_dict = {1: [2]}
        exit_dict = {"position": [2, 4]}
        expected_value = "You search and search, but the room is empty.\n\n"
        search(player_dict, key_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_exit(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "0 Keys"]}
        key_dict = {1: [2]}
        exit_dict = {"position": [2, 2]}
        expected_value = "You glance around, and spot a ladder with a locked hatch. The hatch has 3 key holes.\n\n"
        search(player_dict, key_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_search_escape(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "3 Keys"]}
        key_dict = {1: [2]}
        exit_dict = {"position": [2, 2]}
        expected_value = "You insert each key into the respective key hole. One by one the locks clang on the ground " \
                         "as the ladder hatch swings open.\nFreedom is yours, you escaped the goblins den.\n"
        search(player_dict, key_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestInteract_with_exit(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_interact_with_exit_locked(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "0 Keys"]}
        expected_value = "You glance around, and spot a ladder with a locked hatch. The hatch has 3 key holes.\n\n"
        interact_with_exit(player_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_interact_with_exit_escape(self, mock_print):
        player_dict = {"position": [2, 2], "inventory": ["Sword", "3 Keys"]}
        expected_value = "You insert each key into the respective key hole. One by one the locks clang on the ground " \
                         "as the ladder hatch swings open.\nFreedom is yours, you escaped the goblins den.\n"
        interact_with_exit(player_dict)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestGive_key(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_give_key(self, mock_print):
        player_dict = {"inventory": ["Sword", "0 Keys"]}
        expected_value = "You search the room, and a glint catches your eye.\nA shiny golden key sits besides a hay " \
                         "bed roll.\n\n"
        give_key(player_dict)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestInput_help(TestCase):
    @patch('builtins.input', side_effect=["north"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_help_movement(self, mock_print, mock_input):
        expected_value = "\nThis is a movement input. If north is input, the character will move north relative to " \
                         "the '◘' character. (Moves character)\n\n"
        input_help()
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('builtins.input', side_effect=["search"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_help_north(self, mock_print, mock_input):
        expected_value = "\nThis is a search input. It will allows you to find useful items to use on your adventure," \
                         " and to gain information on certain tiles. (Searches current floor tile)\n\n"
        input_help()
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('builtins.input', side_effect=["quit"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_help_quit(self, mock_print, mock_input):
        expected_value = "\nThis is a quit input. This will end the game, and wont save your progress.\n\n"
        input_help()
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('builtins.input', side_effect=["help"])
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_input_help_help(self, mock_print, mock_input):
        expected_value = "\nThis is a help input. I know your'e only in here to not think about the horrific monsters" \
                         " out there, but how else will you escape this decrepit dungeon. (You are in the help " \
                         "already)\n\n"
        input_help()
        self.assertEqual(expected_value, mock_print.getvalue())
