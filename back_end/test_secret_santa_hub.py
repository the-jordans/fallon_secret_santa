import unittest
import secret_santa_hub
from family_constants import family_dict

class MyTest(unittest.TestCase):
    def test_base_cases(self):
        self.assertTrue("Gabe Fallon" not in secret_santa_hub.return_possible_matches_indv("Gabe Fallon"))
        self.assertTrue("Jen Fallon" not in secret_santa_hub.return_possible_matches_indv("Gabe Fallon"))

    def test_random_matches(self):
        self.assertEqual(len(secret_santa_hub.return_matches_for_everyone()), 8)
        self.assertFalse(None in secret_santa_hub.return_matches_for_everyone().values())
        self.assertEqual(secret_santa_hub.return_matches_for_everyone().keys(), family_dict.keys())

    def test_same_name_matches(self):
        self.assertEqual(len([key_name for key_name, value_name
                                 in secret_santa_hub.return_matches_for_everyone().items()
                                 if key_name == value_name]), 0)


if __name__ == '__main__':
    unittest.main()
