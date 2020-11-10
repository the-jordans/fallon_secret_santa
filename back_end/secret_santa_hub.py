import random
from family_constants import family_dict


def return_possible_matches_indv(find_matches_for_name):
    possible_matches = [possible_match for possible_match in family_dict.keys()
                        if possible_match != find_matches_for_name
                        and possible_match != family_dict[find_matches_for_name]['SO']
                        and possible_match != family_dict[find_matches_for_name][2018]
                        and possible_match != family_dict[find_matches_for_name][2019]
                       ]
    return possible_matches


def return_matches_for_everyone():
    current_available_names = list(family_dict.keys())
    family_pairs = []
    try:
        for giver_name in family_dict.keys():
            optional_names = set(return_possible_matches_indv(giver_name))
            final_options = list(optional_names.intersection(set(current_available_names)))
            reciever_name = random.choice(final_options)
            current_available_names.remove(reciever_name)
            family_pairs.append({'giver': giver_name,
                                 'receiver': reciever_name})
    except:
        return return_matches_for_everyone()
    return family_pairs
