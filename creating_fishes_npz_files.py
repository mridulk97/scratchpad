import os
import argparse
import numpy as np
from PIL import Image
from tqdm import tqdm

all_images = []
all_labels = []

def get_keys_by_value(search_value):
    label_to_class_mapping = {0: 'Alosa-chrysochloris', 1: 'Carassius-auratus', 2: 'Cyprinus-carpio', 3: 'Esox-americanus', 
    4: 'Gambusia-affinis', 5: 'Lepisosteus-osseus', 6: 'Lepisosteus-platostomus', 7: 'Lepomis-auritus', 8: 'Lepomis-cyanellus', 
    9: 'Lepomis-gibbosus', 10: 'Lepomis-gulosus', 11: 'Lepomis-humilis', 12: 'Lepomis-macrochirus', 13: 'Lepomis-megalotis', 
    14: 'Lepomis-microlophus', 15: 'Morone-chrysops', 16: 'Morone-mississippiensis', 17: 'Notropis-atherinoides', 
    18: 'Notropis-blennius', 19: 'Notropis-boops', 20: 'Notropis-buccatus', 21: 'Notropis-buchanani', 22: 'Notropis-dorsalis', 
    23: 'Notropis-hudsonius', 24: 'Notropis-leuciodus', 25: 'Notropis-nubilus', 26: 'Notropis-percobromus', 
    27: 'Notropis-stramineus', 28: 'Notropis-telescopus', 29: 'Notropis-texanus', 30: 'Notropis-volucellus', 
    31: 'Notropis-wickliffi', 32: 'Noturus-exilis', 33: 'Noturus-flavus', 34: 'Noturus-gyrinus', 35: 'Noturus-miurus', 
    36: 'Noturus-nocturnus', 37: 'Phenacobius-mirabilis'}

    return [key for key, value in label_to_class_mapping.items() if value == search_value]



def process_images_to_npz(root_folder, npz_output_file):
    all_images = []
    all_labels = []

    for class_folder in tqdm(os.listdir(root_folder)):
        class_path = os.path.join(root_folder, class_folder)
        if os.path.isdir(class_path):
            label = class_folder

            for filename in os.listdir(class_path):
                if filename.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
                    image_path = os.path.join(class_path, filename)
                    image = Image.open(image_path)
                    if not image.mode == "RGB":
                        image = image.convert("RGB")
                    image_arr = np.array(image).astype(np.uint8)
                    all_images.append(image_arr)
                    all_labels.append(get_keys_by_value(label)[0])

    all_images = np.array(all_images)
    all_labels = np.array(all_labels)

    np.savez(npz_output_file, all_images, all_labels)


def main():
    parser = argparse.ArgumentParser(description="Process images in a folder and save as NPZ file.")
    parser.add_argument("--input_folder", type=str, required=True, help="Path to the input folder containing class subfolders with images.")
    parser.add_argument("--output_npz", type=str, required=True, help="Path to the output NPZ file.")
    args = parser.parse_args()

    input_folder = args.input_folder
    output_npz = args.output_npz

    process_images_to_npz(input_folder, output_npz)

if __name__ == "__main__":
    """
    Code Usage:
    python creating_npz_files.py --input_folder /path/to/your/images --output_npz output.npz
    """
    main()


