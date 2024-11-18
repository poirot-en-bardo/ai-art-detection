import os
import shutil

def ImageGather(source_dir, destination_dir, image_extensions=('jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff')):
    # Ensure destination directory exists
    os.makedirs(destination_dir, exist_ok=True)
    file_count = 0
    # Walk through all subdirectories and files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            # Check if the file has an image extension
            if file.lower().endswith(image_extensions):
                # Get the relative path from the source directory
                relative_path = os.path.relpath(root, source_dir)
                
                # Convert subdirectory path to a prefix for the filename
                folder_prefix = relative_path.replace(os.sep, '-')  # Replace path separator with a hyphen
                
                # Create the new filename with prefix
                new_filename = f"{folder_prefix}-{file}" if folder_prefix else file
                source_path = os.path.join(root, file)
                dest_path = os.path.join(destination_dir, new_filename)
                
                # Handle duplicate file names with suffix if needed
                counter = 1
                while os.path.exists(dest_path):
                    filename, ext = os.path.splitext(new_filename)
                    dest_path = os.path.join(destination_dir, f"{filename}_{counter}{ext}")
                    counter += 1
                
                # Copy the file to the destination folder with the new name
                shutil.copy2(source_path, dest_path)
                file_count += 1

    print(f"Total number of files copied: {counter}")

# Set your source and destination directories
source_directory = '/home/oem/eliza/DL/project/data/deepfakeart'
destination_directory = '/home/oem/eliza/DL/project/data/gathered_art'

# Run the function
ImageGather(source_directory, destination_directory)
