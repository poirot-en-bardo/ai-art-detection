import os
import numpy as np
import cv2
from pathlib import Path
import matplotlib.pyplot as plt

def create_fourier_spectrum(input_folder, output_folder):
    """
    Process images in the input folder (including subfolders) to compute their Fourier spectra
    and save the results in a mirrored folder structure under the output folder.
    """
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    for root, _, files in os.walk(input_folder):
        # Get the relative path for preserving the folder structure
        relative_path = os.path.relpath(root, input_folder)
        output_subfolder = os.path.join(output_folder, relative_path)

        # Create the corresponding subfolder in the output
        os.makedirs(output_subfolder, exist_ok=True)

        for file in files:
            # Process only image files (you can adjust the file types as needed)
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):
                input_image_path = os.path.join(root, file)
                output_image_path = os.path.join(output_subfolder, file)

                # Read the image in grayscale
                image = cv2.imread(input_image_path, cv2.IMREAD_GRAYSCALE)
                if image is None:
                    print(f"Warning: Could not read {input_image_path}. Skipping.")
                    continue

                # Compute the Fourier Transform
                f_transform = np.fft.fft2(image)
                f_shift = np.fft.fftshift(f_transform)
                magnitude_spectrum = np.log1p(np.abs(f_shift))

                # Normalize for better visualization
                magnitude_spectrum_normalized = cv2.normalize(
                    magnitude_spectrum, None, 0, 255, cv2.NORM_MINMAX
                ).astype(np.uint8)

                # Save the spectrum as an image
                cv2.imwrite(output_image_path, magnitude_spectrum_normalized)

                print(f"Processed {input_image_path} -> {output_image_path}")

# Input and output directories
input_folder = "/home/oem/eliza/DL/project/data/artifact"
output_folder = "/home/oem/eliza/DL/project/data/artifact_fourier"


create_fourier_spectrum(input_folder, output_folder)
