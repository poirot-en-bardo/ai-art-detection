import os
import shutil

def move_images_to_root(folder, extensions=(".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff", ".webp")):
    """
    Moves all image files from subfolders and sub-subfolders to the root of the given folder.
    
    Args:
        folder (str): Path to the root folder.
        extensions (tuple): Tuple of allowed image file extensions.
    """
    if not os.path.isdir(folder):
        print(f"The specified path '{folder}' is not a valid directory.")
        return
    
    # Walk through all subdirectories
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(extensions):  # Check for image file extensions
                src_path = os.path.join(root, file)
                dst_path = os.path.join(folder, file)
                
                # If there's a name conflict, add a suffix to the file
                if os.path.exists(dst_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(dst_path):
                        dst_path = os.path.join(folder, f"{base}_{counter}{ext}")
                        counter += 1
                
                # Move the file
                shutil.move(src_path, dst_path)
                print(f"Moved: {src_path} -> {dst_path}")
    
    print("All images have been moved to the root folder.")

# Example Usage:
# Specify the folder containing subfolders with images
source_folder = "/home/oem/eliza/DL/project/data/processed/resize_generated"
move_images_to_root(source_folder)
