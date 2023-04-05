"""To remove outliers."""


import matplotlib.pyplot as plt
import os
import numpy as np
from scipy import stats
import cv2
import glob


dir_path = "data_processed/test/"

# Define the list of emotions to loop over
emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
z_scores = []
for emotion in emotions:
    # Load images for the current emotion and calculate their z-scores

    folder_path = os.path.join(dir_path, emotion)
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
        z_score = stats.zscore(img.flatten())
        z_scores.extend(z_score)

# Plot histogram of z-scores
plt.hist(z_scores, bins=50)
plt.xlabel("Z-score")
plt.ylabel("Frequency")
plt.show()

# Define the directory containing your image dataset
dir_path = "data_processed/test/"

# Define the list of emotions to loop over
emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]

for emotion in emotions:
    # Load images for the current emotion and calculate their z-scores
    images = []
    z_scores = []
    folder_path = os.path.join(dir_path, emotion)
    for filename in os.listdir(folder_path):
        img = cv2.imread(os.path.join(folder_path, filename), cv2.IMREAD_GRAYSCALE)
        images.append(img)
        z_score = np.abs(stats.zscore(img.flatten()))
        z_scores.append(z_score)

    # Set a threshold for the maximum allowable z-score
    threshold = 5

    # Create a directory to store the outlier images
    outlier_dir_path = os.path.join(folder_path, "outliers")
    if not os.path.exists(outlier_dir_path):
        os.makedirs(outlier_dir_path)

    # Create a directory to store the filtered images
    filter_dir_path = os.path.join(folder_path, "filtered")
    if not os.path.exists(filter_dir_path):
        os.makedirs(filter_dir_path)

    # Identify and remove outliers
    filtered_images = []
    outlier_images = []
    for i in range(len(images)):
        if np.max(z_scores[i]) <= threshold:
            filtered_images.append(images[i])
            # Save the image in the filtered folder
            cv2.imwrite(
                os.path.join(filter_dir_path, str(i) + ".jpg"), filtered_images[-1]
            )
        else:
            outlier_images.append(images[i])
            # Save the image in the outlier folder
            cv2.imwrite(
                os.path.join(outlier_dir_path, str(i) + ".jpg"), outlier_images[-1]
            )
            # Delete the image from the original subfolder
            # os.remove(os.path.join(folder_path, os.listdir(folder_path)[i]))

    # Display the number of removed images and remaining images
    print(f"Emotion: {emotion}, removed {len(outlier_images)} outlier images.")
    print(f"Emotion: {emotion}, remaining {len(filtered_images)} images.")
