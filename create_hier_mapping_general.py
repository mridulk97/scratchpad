import json
import pickle
import argparse

def list_ancestor_levels(ancestor_dict):
    list_ancestor=[]
    for value in ancestor_dict.values():
        list_ancestor.extend(value)
    return sorted(list_ancestor)


def find_key_for_value(dct, search_value):
    for key, value_list in dct.items():
        if search_value in value_list:
            return key
    return None


def creating_hier_mapping(input_file, output_file):
    with open(input_file, 'r') as file:
        read_dict = json.load(file)
    
    n_levels = len(read_dict) + 1


    all_species = list_ancestor_levels(read_dict['level_0'])
    for _, value in read_dict.items():
        level_species = list_ancestor_levels(value)
        assert all_species==level_species

    # breakpoint()
    ancestral_level_list = {}
    for i, species in enumerate(all_species):
        level_list = []
        for j in range(n_levels-1):
            ancestor_level = f'level_{j}'
            label = find_key_for_value(read_dict[ancestor_level], species)
            level_list.append(label)
        level_list.append(i)
    
        ancestral_level_list[species] = [', '.join(map(str, level_list))]

    with open(output_file, 'wb') as pickle_file:
        pickle.dump(ancestral_level_list, pickle_file)




if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_json",
        type=str,
        default="",
    )

    parser.add_argument(
        "--output_pkl",
        type=str,
        default="mapping.pkl",
    )
    
    opt = parser.parse_args()
    creating_hier_mapping(opt.input_json, opt.output_pkl)
    print('done')