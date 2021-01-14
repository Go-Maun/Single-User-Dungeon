from unittest import TestCase
from unittest.mock import patch
from A01172483_1510_assignments.A3.instantiateDictionaries import create_dungeon_dictionary
from A01172483_1510_assignments.A3.instantiateDictionaries import create_player_dictionary
from A01172483_1510_assignments.A3.instantiateDictionaries import create_enemy_dictionary
from A01172483_1510_assignments.A3.instantiateDictionaries import create_exit_dictionary
from A01172483_1510_assignments.A3.instantiateDictionaries import generate_hidden_keys


class TestCreate_dungeon_dictionary(TestCase):
    def test_create_dungeon_dictionary_square(self):
        expected_value = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4],
                          4: [0, 1, 2, 3, 4]}
        actual_value = create_dungeon_dictionary(5, 5)
        self.assertEqual(expected_value, actual_value)

    def test_create_dungeon_dictionary_longer_than_wide(self):
        expected_value = {0: [0, 1, 2], 1: [0, 1, 2], 2: [0, 1, 2], 3: [0, 1, 2], 4: [0, 1, 2]}
        actual_value = create_dungeon_dictionary(3, 5)
        self.assertEqual(expected_value, actual_value)

    def test_create_dungeon_dictionary_wider_than_long(self):
        expected_value = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4]}
        actual_value = create_dungeon_dictionary(5, 3)
        self.assertEqual(expected_value, actual_value)


class TestCreate_player_dictionary(TestCase):
    @patch("random.randint", return_value=3)
    def test_create_player_dictionary_3(self, mock_random):
        expected_value = {"position": [3, 3], "Name": "Steve", "inventory": ["Sword", "0 keys"], "health": 10}
        actual_value = create_player_dictionary(5, 5, "Steve")
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=0)
    def test_create_player_dictionary_0(self, mock_random):
        expected_value = {"position": [0, 0], "Name": "Steve", "inventory": ["Sword", "0 keys"], "health": 10}
        actual_value = create_player_dictionary(5, 5, "Steve")
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=4)
    def test_create_player_dictionary_4(self, mock_random):
        expected_value = {"position": [4, 4], "Name": "Steve", "inventory": ["Sword", "0 keys"], "health": 10}
        actual_value = create_player_dictionary(5, 5, "Steve")
        self.assertEqual(expected_value, actual_value)


class TestCreate_enemy_dictionary(TestCase):
    def test_create_enemy_dictionary(self):
        expected_value = {'Name': 'Goblin', 'health': 5}
        actual_value = create_enemy_dictionary()
        self.assertEqual(expected_value, actual_value)


class TestCreate_exit_dictionary(TestCase):
    @patch("random.randint", return_value=0)
    def test_create_exit_dictionary_0(self, mock_random):
        expected_value = {"position": [0, 0]}
        actual_value = create_exit_dictionary(5, 5)
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=3)
    def test_create_exit_dictionary_3(self, mock_random):
        expected_value = {"position": [3, 3]}
        actual_value = create_exit_dictionary(5, 5)
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=4)
    def test_create_exit_dictionary_4(self, mock_random):
        expected_value = {"position": [4, 4]}
        actual_value = create_exit_dictionary(5, 5)
        self.assertEqual(expected_value, actual_value)


class TestGenerate_hidden_keys(TestCase):
    @patch("random.randint", return_value=0)
    @patch("random.randint", return_value=3)
    @patch("random.randint", return_value=4)
    def test_generate_hidden_keys(self, mock, mock1, mock2):
        room_dict = {0: [0, 1, 2, 3, 4], 1: [0, 1, 2, 3, 4], 2: [0, 1, 2, 3, 4], 3: [0, 1, 2, 3, 4], 4: [0, 1, 2, 3, 4]}
        expected_value = {0: [0, 1, 2]}
        actual_value = generate_hidden_keys(room_dict, 3, 25)
        self.assertEqual(expected_value, actual_value)
