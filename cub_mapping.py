import os
import json
import pickle

with open('/projects/ml4science/mridul/ldm/data/cub/cub_ancestral_mapping.json', 'r') as file:
    read_dict = json.load(file)

# breakpoint()
ancestor_level0 = read_dict['level_0']
ancestor_level1 = read_dict['level_1']
ancestor_level2 = read_dict['level_2']

list_ancestor_level2 = []
for value in ancestor_level2.values():
    list_ancestor_level2.extend(value)
list_ancestor_level2 = sorted(list_ancestor_level2)

list_ancestor_level1 = []
for value in ancestor_level1.values():
    list_ancestor_level1.extend(value)
list_ancestor_level1 = sorted(list_ancestor_level1)

list_ancestor_level0 = []
for value in ancestor_level0.values():
    list_ancestor_level0.extend(value)
list_ancestor_level0 = sorted(list_ancestor_level0)

assert list_ancestor_level0 == list_ancestor_level1 == list_ancestor_level2

def find_key_for_value(dct, search_value):
    for key, value_list in dct.items():
        if search_value in value_list:
            return key
    return None


ancestral_level_label = {}
i = 0
for species in sorted(list_ancestor_level0):
    label_level0 = find_key_for_value(ancestor_level0, species)
    label_level1 = find_key_for_value(ancestor_level1, species)
    label_level2 = find_key_for_value(ancestor_level2, species)
    label_level3 = i
    level_list = [label_level0, label_level1, label_level2, label_level3]
    ancestral_level_label[species] = [', '.join(map(str, level_list))]
    i += 1

# breakpoint()

with open('/projects/ml4science/mridul/ldm/data/cub/cub_class_to_ancestral_label.pkl', 'wb') as pickle_file:
    pickle.dump(ancestral_level_label, pickle_file)

print('done')