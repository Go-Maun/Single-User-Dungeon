from unittest import TestCase
from unittest.mock import patch
import io
from A01172483_1510_assignments.A3.printDungeon import print_scenario
from A01172483_1510_assignments.A3.printDungeon import print_room
from A01172483_1510_assignments.A3.printDungeon import print_hud
from A01172483_1510_assignments.A3.printDungeon import print_player_items
from A01172483_1510_assignments.A3.printDungeon import print_player_health
from A01172483_1510_assignments.A3.printDungeon import print_tile
from A01172483_1510_assignments.A3.printDungeon import print_player
from A01172483_1510_assignments.A3.printDungeon import print_exit


class TestPrint_scenario(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_square(self, mock_print):
        expected_value = "◙ X X X X\nX X X X X\nX X X X X\nX X X ◘ X\nX X X X X\n\nHealth: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥\n" \
                         "Inventory: Sword,  Apple\n\n"
        room_dict = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}
        player_dict = {"position": [3, 3], "health": 10, "inventory": ["Sword", "Apple"]}
        exit_dict = {"position": [0, 0]}
        print_scenario(5, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_longer_than_wide(self, mock_print):
        expected_value = "◙ X X\nX X X\nX X X\nX X ◘\nX X X\n\nHealth: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥\n" \
                         "Inventory: Sword,  Apple\n\n"
        room_dict = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]}
        player_dict = {"position": [2, 3], "health": 10, "inventory": ["Sword", "Apple"]}
        exit_dict = {"position": [0, 0]}
        print_scenario(3, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_wider_than_long(self, mock_print):
        expected_value = "◙ X X X X\nX X X X X\nX X X ◘ X\n\nHealth: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥\n" \
                         "Inventory: Sword,  Apple\n\n"
        room_dict = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4]}
        player_dict = {"position": [3, 2], "health": 10, "inventory": ["Sword", "Apple"]}
        exit_dict = {"position": [0, 0]}
        print_scenario(5, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_room(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_square(self, mock_print):
        expected_value = "◙ X X X X\nX X X X X\nX X X X X\nX X X ◘ X\nX X X X X\n"
        room_dict = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}
        player_dict = {"position": [3, 3]}
        exit_dict = {"position": [0, 0]}
        print_room(5, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_longer_than_wide(self, mock_print):
        expected_value = "◙ X X\nX X X\nX X X\nX X ◘\nX X X\n"
        room_dict = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]}
        player_dict = {"position": [2, 3]}
        exit_dict = {"position": [0, 0]}
        print_room(3, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_scenario_wider_than_long(self, mock_print):
        expected_value = "◙ X X X X\nX X X X X\nX X X ◘ X\n"
        room_dict = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4]}
        player_dict = {"position": [3, 2]}
        exit_dict = {"position": [0, 0]}
        print_room(5, room_dict, player_dict, exit_dict)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_hud(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hud_low_health(self, mock_print):
        expected_value = "\nHealth: ♥ ○ ○ ○ ○ ○ ○ ○ ○ ○\nInventory: sword,  Apple\n\n"
        print_hud({"health": 1, "inventory": ["sword", "Apple"]})
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hud_med_health(self, mock_print):
        expected_value = "\nHealth: ♥ ♥ ♥ ♥ ♥ ○ ○ ○ ○ ○\nInventory: sword,  Apple\n\n"
        print_hud({"health": 5, "inventory": ["sword", "Apple"]})
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_hud_full_health(self, mock_print):
        expected_value = "\nHealth: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥\nInventory: sword,  Apple\n\n"
        print_hud({"health": 10, "inventory": ["sword", "Apple"]})
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_player_items(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_items_one(self, mock_print):
        expected_value = "Inventory: Sword\n"
        print_player_items({"inventory":["Sword"]})
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_items_three(self, mock_print):
        expected_value = "Inventory: Sword,  Apple,  Bag\n"
        print_player_items({"inventory": ["Sword", "Apple", "Bag"]})
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_player_health(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_health_low(self, mock_print):
        expected_value = "Health: ♥ ○ ○ ○ ○ ○ ○ ○ ○ ○\n"
        print_player_health({"health": 1}, 10)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_health_full(self, mock_print):
        expected_value = "Health: ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥ ♥\n"
        print_player_health({"health": 10}, 10)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_tile(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_tile_middle(self, mock_print):
        expected_value = "X "
        print_tile(4, 2)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_tile_end(self, mock_print):
        expected_value = "X\n"
        print_tile(4, 3)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_player(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_middle(self, mock_print):
        expected_value = "◘ "
        print_player(4, 2)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_end(self, mock_print):
        expected_value = "◘\n"
        print_player(4, 3)
        self.assertEqual(expected_value, mock_print.getvalue())


class TestPrint_exit(TestCase):
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_middle(self, mock_print):
        expected_value = "◙ "
        print_exit(4, 2)
        self.assertEqual(expected_value, mock_print.getvalue())

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_player_end(self, mock_print):
        expected_value = "◙\n"
        print_exit(4, 3)
        self.assertEqual(expected_value, mock_print.getvalue())
