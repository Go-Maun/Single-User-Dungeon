from unittest import TestCase
from unittest.mock import patch
from A01172483_1510_assignments.A3.combat import roll_die
from A01172483_1510_assignments.A3.combat import heal_player


class TestRoll_die(TestCase):
    @patch("random.randint", return_value=1)
    def test_roll_die_three(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 3
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=2)
    def test_roll_die_six(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 6
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=3)
    def test_roll_die_nine(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 9
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=4)
    def test_roll_die_twelve(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 12
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=5)
    def test_roll_die_fifteen(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 15
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=6)
    def test_roll_die_eighteen(self, mock_roll):
        actual_value = roll_die(3, 6)
        expected_value = 18
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=10)
    def test_roll_die_fifty(self, mock_roll):
        actual_value = roll_die(5, 20)
        expected_value = 50
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=20)
    def test_roll_die_natural_twenty(self, mock_roll):
        actual_value = roll_die(1, 20)
        expected_value = 20
        self.assertEqual(expected_value, actual_value)

    @patch("random.randint", return_value=1)
    def test_roll_die_two_natural_ones(self, mock_roll):
        actual_value = roll_die(2, 20)
        expected_value = 2
        self.assertEqual(expected_value, actual_value)


class TestHeal_player(TestCase):
    def test_heal_player_7_health(self):
        expected_value = {"health": 9}
        actual_value = heal_player({"health": 7}, 2, 10)
        self.assertEqual(expected_value, actual_value)

    def test_heal_player_5_health(self):
        expected_value = {"health": 7}
        actual_value = heal_player({"health": 5}, 2, 10)
        self.assertEqual(expected_value, actual_value)

    def test_heal_player_full_health(self):
        expected_value = {"health": 10}
        actual_value = heal_player({"health": 10}, 2, 10)
        self.assertEqual(expected_value, actual_value)

    def test_heal_player_1_health(self):
        expected_value = {"health": 3}
        actual_value = heal_player({"health": 1}, 2, 10)
        self.assertEqual(expected_value, actual_value)

    def test_heal_player_2_health(self):
        expected_value = {"health": 4}
        actual_value = heal_player({"health": 2}, 2, 10)
        self.assertEqual(expected_value, actual_value)

    def test_heal_player_3_health(self):
        expected_value = {"health": 5}
        actual_value = heal_player({"health": 3}, 2, 10)
        self.assertEqual(expected_value, actual_value)
