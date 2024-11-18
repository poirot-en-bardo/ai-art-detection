import os
import shutil



def move_images_with_keywords(source_dir, destination_dir, keywords, image_extensions=('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')):
    """
    Searches for images with specific keywords in their filenames and copies them to the destination directory.
    
    Parameters:
    - source_dir: The root directory to search within.
    - destination_dir: The directory to copy matching images to.
    - keywords: A list of keywords to search for in filenames (all keywords must be present in the filename).
    - image_extensions: Tuple of valid image extensions.
    """
    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    
    # Counter for the total number of files copied
    file_count = 0

    # Walk through all subdirectories and files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file has an image extension and contains all keywords
            if file.lower().endswith(image_extensions) and all(keyword in file for keyword in keywords):
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination_dir, file)
                
                # Handle duplicate file names by appending a counter if necessary
                counter = 1
                while os.path.exists(dest_path):
                    filename, ext = os.path.splitext(file)
                    dest_path = os.path.join(destination_dir, f"{filename}_{counter}{ext}")
                    counter += 1
                
                # Copy the file to the destination folder
                shutil.move(source_path, dest_path)
                file_count += 1

    # Print the total number of files copied
    print(f"Total number of files copied: {file_count}")


# Usage
source_directory = '/home/oem/eliza/DL/project/data/gathered_art'
destination_directory = '/home/oem/eliza/DL/project/data/Style_Transfer_Generated_DeepFakeArt'
search_keywords = ['style_transfer','generated']

# Run the function
move_images_with_keywords(source_directory, destination_directory, search_keywords)
