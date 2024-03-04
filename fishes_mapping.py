import os

ancestor_level0 = { 0: ['Alosa chrysochloris', 'Carassius auratus', 'Cyprinus carpio',
                        'Notropis atherinoides', 'Notropis blennius', 'Notropis boops',
                        'Notropis buccatus', 'Notropis buchanani', 'Notropis dorsalis', 
                        'Notropis hudsonius', 'Notropis leuciodus', 'Notropis nubilus', 
                        'Notropis percobromus', 'Notropis stramineus','Notropis telescopus', 
                        'Notropis texanus', 'Notropis volucellus', 'Notropis wickliffi', 
                        'Noturus exilis', 'Noturus flavus','Noturus gyrinus', 'Noturus miurus', 
                        'Noturus nocturnus','Phenacobius mirabilis'],
                    1: ['Esox americanus', 'Gambusia affinis', 'Lepomis auritus',
                        'Lepomis cyanellus', 'Lepomis gibbosus', 'Lepomis gulosus',
                        'Lepomis humilis', 'Lepomis macrochirus', 'Lepomis megalotis', 
                        'Lepomis microlophus', 'Morone chrysops', 'Morone mississippiensis'],
                    2: ['Lepisosteus osseus', 'Lepisosteus platostomus']
                }

ancestor_level1 = { 0: ['Alosa chrysochloris'],
                    1: ['Carassius auratus', 'Cyprinus carpio', 'Notropis atherinoides', 
                        'Notropis blennius', 'Notropis boops', 'Notropis buccatus', 
                        'Notropis buchanani', 'Notropis dorsalis', 'Notropis hudsonius', 
                        'Notropis leuciodus', 'Notropis nubilus', 'Notropis percobromus', 
                        'Notropis stramineus','Notropis telescopus', 'Notropis texanus', 
                        'Notropis volucellus', 'Notropis wickliffi', 'Phenacobius mirabilis'],
                    2: ['Esox americanus'],
                    3: ['Gambusia affinis', 'Lepomis auritus',
                        'Lepomis cyanellus', 'Lepomis gibbosus', 'Lepomis gulosus',
                        'Lepomis humilis', 'Lepomis macrochirus', 'Lepomis megalotis', 
                        'Lepomis microlophus', 'Morone chrysops', 'Morone mississippiensis'],
                    4: ['Lepisosteus osseus', 'Lepisosteus platostomus'],
                    5: ['Noturus exilis', 'Noturus flavus','Noturus gyrinus', 'Noturus miurus', 
                        'Noturus nocturnus']
                }

ancestor_level2 = { 0: ['Alosa chrysochloris'],
                    1: ['Carassius auratus', 'Cyprinus carpio'],
                    2: ['Esox americanus'],
                    3: ['Gambusia affinis'], 
                    4: ['Lepisosteus osseus', 'Lepisosteus platostomus'],
                    5: ['Lepomis auritus','Lepomis cyanellus', 'Lepomis gibbosus', 'Lepomis gulosus',
                        'Lepomis humilis', 'Lepomis macrochirus', 'Lepomis megalotis','Lepomis microlophus'],
                    6: ['Morone chrysops', 'Morone mississippiensis'],

                    7: ['Notropis atherinoides', 'Notropis blennius', 'Notropis boops', 'Notropis buccatus', 
                        'Notropis buchanani', 'Notropis dorsalis', 'Notropis hudsonius', 
                        'Notropis leuciodus', 'Notropis nubilus', 'Notropis percobromus', 
                        'Notropis stramineus','Notropis telescopus', 'Notropis texanus', 
                        'Notropis volucellus', 'Notropis wickliffi', 'Phenacobius mirabilis'],
                    
                    8: ['Noturus exilis', 'Noturus flavus','Noturus gyrinus', 'Noturus miurus', 
                        'Noturus nocturnus']
                }

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

def find_key_for_value(dct, search_value):
    for key, value_list in dct.items():
        if search_value in value_list:
            return key
    return None

# flat_list.extend(value)
# list_ancestor = [value for key, value in ancestor_level2.items() if isinstance(value, list)]

import pickle
with open('/fastscratch/mridul/fishes/class_to_node_bfs_weighted.pkl', 'rb') as pickle_file:
    class_to_node_dict = pickle.load(pickle_file)

classes = sorted(list(class_to_node_dict.keys()))


ancestral_level_label = {}
i = 0
for species in classes:
    label_level0 = find_key_for_value(ancestor_level0, species)
    label_level1 = find_key_for_value(ancestor_level1, species)
    label_level2 = find_key_for_value(ancestor_level2, species)
    label_level3 = i
    level_list = [label_level0, label_level1, label_level2, label_level3]
    ancestral_level_label[species] = [', '.join(map(str, level_list))]
    i += 1

with open('/fastscratch/mridul/fishes/class_to_ancestral_label.pkl', 'wb') as pickle_file:
    pickle.dump(ancestral_level_label, pickle_file)

print('done')