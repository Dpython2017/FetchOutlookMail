import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
import unittest
from scripts.main import main
from scripts.utils import validate


class SearchMail(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def test_result(self):
        result = main()
        expected = {'ClientAchievements@cerner.com': True, 'Dimple.Mathew@cerner.com': False}
        self.assertEqual(expected, result)

    @unittest.skip('WIP')
    def test_data_not_found(self):
        result = main()
        expected = {}
        self.assertEqual(expected, result)

    def test_valid_user_name(self):
        username = 'DM050767'
        email = 'dimple.mathew@cerner.com'
        result = validate(username,email)
        self.assertEqual(True, result)

    def invalid_user_details(self):
        with self.assertRaises(ValueError):
            validate('', '')

