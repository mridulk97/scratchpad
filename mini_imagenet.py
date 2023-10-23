import os
import glob
import json
from collections import Counter
import argparse
import random
import shutil
from tqdm import tqdm


if __name__ == '__main__':


    # # Replace 'imagenet_dir' with the path to your ImageNet dataset directory
    # imagenet_dir = '/fastscratch/mridul/data/mini_imagenet_split_test/ILSVRC2012_test/data'
    # class_counter = {}
    # # Iterate through the directories representing classes
    # for class_dir in os.listdir(imagenet_dir):
    #     class_path = os.path.join(imagenet_dir, class_dir)
        
    #     if os.path.isdir(class_path):
    #         # Inside each class directory, you may have multiple image files
    #         for image_file in os.listdir(class_path):
    #             image_path = os.path.join(class_path, image_file)
    #             if class_dir in class_counter:
    #                 class_counter[class_dir] += 1
    #             else:
    #                 class_counter[class_dir] = 1
                
    #             # Process the image as needed
    #             # You can use image processing libraries like PIL, OpenCV, or others here
                
    #             # Example: Print the image path
    #             # print("Image Path:", image_path)
    
    # print(class_counter)



    # Path to the ImageNet dataset directory
    imagenet_dir = '/fastscratch/mridul/data/mini-imagenet'

    # Path to the directory where you want to create the train and test splits
    output_dir = '/globalscratch/mridul/data/mini-imagenet_split_test'

    # Percentage of data to use for training (e.g., 80%)
    train_percentage = 0.85

    # Create directories for train and test splits
    train_dir = os.path.join(output_dir, 'ILSVRC2012_train/data/')
    test_dir = os.path.join(output_dir, 'ILSVRC2012_validation/data/')
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # List all class directories in ImageNet
    class_dirs = [d for d in os.listdir(imagenet_dir) if os.path.isdir(os.path.join(imagenet_dir, d))]

    # Iterate through each class and split the samples
    for class_dir in tqdm(class_dirs):
        class_path = os.path.join(imagenet_dir, class_dir)
        all_samples = os.listdir(class_path)
        num_samples = len(all_samples)
        
        # Calculate the number of samples for training
        num_train_samples = int(num_samples * train_percentage)
        
        # Randomly shuffle the samples
        random.shuffle(all_samples)
        
        # Split the samples into train and test
        train_samples = all_samples[:num_train_samples]
        test_samples = all_samples[num_train_samples:]
        
        # Create directories for the current class in train and test
        train_class_dir = os.path.join(train_dir, class_dir)
        test_class_dir = os.path.join(test_dir, class_dir)
        os.makedirs(train_class_dir, exist_ok=True)
        os.makedirs(test_class_dir, exist_ok=True)
        
        # Copy train samples to the train class directory
        for sample in train_samples:
            src_path = os.path.join(class_path, sample)
            dst_path = os.path.join(train_class_dir, sample)
            shutil.copy(src_path, dst_path)
        
        # Copy test samples to the test class directory
        for sample in test_samples:
            src_path = os.path.join(class_path, sample)
            dst_path = os.path.join(test_class_dir, sample)
            shutil.copy(src_path, dst_path)

    print("Train and test split completed.")




    


    breakpoint()
    print('yee')