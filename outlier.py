"""To remove outliers."""


import os
import numpy as np
from scipy import stats
import cv2
import glob


# Define the directory containing your image dataset
dir_path = "data/train/*"

# Load images and calculate their z-scores
images = []
z_scores = []
for folder_path in glob.glob(dir_path):
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
        images.append(img)
        z_score = np.abs(stats.zscore(img.flatten()))
        z_scores.append(z_score)

# Set a threshold for the maximum allowable z-score
threshold = 5

# Create a directory to store the outlier images
outlier_dir_path = "data/train/outliers"
if not os.path.exists(outlier_dir_path):
    os.makedirs(outlier_dir_path)

# Identify and remove outliers
filtered_images = []
outlier_images = []
for i in range(len(images)):
    if np.max(z_scores[i]) <= threshold:
        filtered_images.append(images[i])
    else:
        outlier_images.append(images[i])
        # cv2.imwrite(os.path.join(filtered_dir_path, filename), images[i]
        # save the image in a separate folder using other code than cv2.imwrite

        # os.remove(os.path.join(dir_path, os.listdir(dir_path)[i]))

# write outlier images to a separate folder
print(len(outlier_images))
for i in range(len(outlier_images)):
    cv2.imwrite(os.path.join(outlier_dir_path, str(i) + ".jpg"), outlier_images[i])


# Display the number of removed images and remaining images
print(f"Removed {len(images)-len(filtered_images)} images.")
print(f"Remaining {len(filtered_images)} images.")
