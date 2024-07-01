from PIL import Image
import imagehash
import os
import shutil

def find_and_move_duplicates(directory, duplicates_folder):
    # Create a folder for duplicates if it doesn't exist
    if not os.path.exists(duplicates_folder):
        os.makedirs(duplicates_folder)

    image_hashes = {}  # Dictionary to store image hashes and their paths
    duplicates = []  # List to store detected duplicate image paths

    # Iterate through all files in the specified directory
    for filename in os.listdir(directory):
        # Check if the file is an image
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            image_path = os.path.join(directory, filename)  # Get the full image path
            image = Image.open(image_path)  # Open the image
            image_hash = imagehash.phash(image)  # Compute the perceptual hash of the image
            
            # Check if the image hash already exists
            if image_hash in image_hashes:
                duplicates.append((image_path, image_hashes[image_hash]))  # Add to duplicates list
                # Move the duplicate file to the duplicates folder
                shutil.move(image_path, os.path.join(duplicates_folder, filename))
            else:
                image_hashes[image_hash] = image_path  # Store the unique image hash
    
    return duplicates  # Return the list of duplicates

directory_path = 'path/to/directory'  # Define the main directory path
duplicates_folder_path = 'path/to/directory'  # Define the duplicates folder path
duplicates = find_and_move_duplicates(directory_path, duplicates_folder_path)  # Find and move duplicates
for dup in duplicates:
    print(f"Duplicate images found and moved: {dup[0]} and {dup[1]}")  # Print the moved duplicates
