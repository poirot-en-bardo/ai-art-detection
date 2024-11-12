import os

def delete_duplicate_images(directory):
    """
    Deletes files ending in '-1' before the file extension if a corresponding file without '-1' exists.
    
    Parameters:
    - directory: The directory containing images to check for duplicates.
    """
    # Counter for deleted files
    deleted_count = 0

    # Walk through all files in the directory
    for file in os.listdir(directory):
        # Check if the filename ends with '-1' before the extension
        if '_1' in file:
            # Split the filename to find the corresponding original file name
            base_name, ext = os.path.splitext(file)
            if base_name.endswith('_1'):
                original_name = base_name[:-2] + ext  # Remove the '-1' suffix

                # Check if the original file exists
                original_path = os.path.join(directory, original_name)
                duplicate_path = os.path.join(directory, file)
                
                if os.path.exists(original_path):
                    # Delete the duplicate file
                    os.remove(duplicate_path)
                    deleted_count += 1
                    print(f"Deleted duplicate: {duplicate_path}")

    # Print total deleted files
    print(f"Total duplicates deleted: {deleted_count}")

# Usage
directory_path = '/home/oem/eliza/DL/project/data/deepfakeart/original_all/original'
delete_duplicate_images(directory_path)
