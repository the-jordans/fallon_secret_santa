import random
import pandas as pd
from family_constants import family_dict

def return_possible_matches_indv(find_matches_for_name):
    possible_matches = [possible_match for possible_match in family_dict.keys()
                        if possible_match != find_matches_for_name
                        and possible_match != family_dict[find_matches_for_name]['SO']]
    return possible_matches


def return_matches_for_everyone():
    return dict((name,random.choice(list(family_dict.keys()))) for name in family_dict.keys())
