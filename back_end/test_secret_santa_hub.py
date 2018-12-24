import unittest
import secret_santa_hub
from collections import Counter
from family_constants import family_dict


class MyTest(unittest.TestCase):
    def test_base_cases(self):
        self.assertTrue("Gabe Fallon" not in secret_santa_hub.return_possible_matches_indv("Gabe Fallon"))
        self.assertTrue("Jen Fallon" not in secret_santa_hub.return_possible_matches_indv("Gabe Fallon"))

    def test_random_matches(self):
        self.assertEqual(len(secret_santa_hub.return_matches_for_everyone()), 8)
        self.assertFalse(None in [list(dic.values())[0] for dic in secret_santa_hub.return_matches_for_everyone()])
        self.assertEqual([list(dic.values())[1] for dic in secret_santa_hub.return_matches_for_everyone()].sort(), list(family_dict.keys()).sort())

    def test_same_name_matches(self):
        for i in range(30):
            self.assertEqual(len([pair for pair
                                  in secret_santa_hub.return_matches_for_everyone()
                                  if pair['giver'] == pair['receiver']]), 0)

    def test_so_matches(self):
        for i in range(30):
            self.assertEqual(len([key_name for pair
                                 in secret_santa_hub.return_matches_for_everyone()
                                 if family_dict[pair['giver']]['SO'] == pair['receiver']]), 0)

    def test_name_repeated_matches(self):
        for i in range(30):
            gift_recipients_list = [pair['receiver'] for pair in secret_santa_hub.return_matches_for_everyone()]
            occurrence_counts_list =  Counter(gift_recipients_list).values()
            self.assertFalse(any(i > 1 for i in occurrence_counts_list))

    def test_2018_matches(self):
        for i in range(30):
            self.assertEqual(len([print(pair) for pair
                                  in secret_santa_hub.return_matches_for_everyone()
                                  if family_dict[pair['giver']][2018] == pair['receiver']]), 0)


if __name__ == '__main__':
    unittest.main()
