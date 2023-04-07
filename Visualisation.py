import matplotlib.pyplot as plt

# data
emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
removed = [48, 5, 56, 120, 64, 56, 104]
remaining = [3947, 431, 4041, 7095, 4901, 4774, 3067]

# plot histograms
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

# plot removed images histogram
ax[0].bar(
    emotions,
    removed,
    color=["red", "green", "blue", "orange", "purple", "gray", "pink"],
)
ax[0].set_title("Removed Outliers in Train set")
ax[0].set_xlabel("Emotion")
ax[0].set_ylabel("Number of Images")


emotions = ["angry", "disgust", "fear", "happy", "neutral", "sad", "surprise"]
removed_test = [16, 2, 13, 23, 13, 23, 24]
remaining_test = [942, 109, 1011, 1751, 1220, 1224, 807]


# plot removed images histogram
ax[1].bar(
    emotions,
    removed,
    color=["red", "green", "blue", "orange", "purple", "gray", "pink"],
)
ax[1].set_title("Removed Outliers in Test Set")
ax[1].set_xlabel("Emotion")
ax[1].set_ylabel("Number of Images")

# display plot
plt.show()

# plot histograms
fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
# plot remaining images histogram
ax[0].bar(
    emotions,
    remaining,
    color=["red", "green", "blue", "orange", "purple", "gray", "pink"],
)
ax[0].set_title("Processed Images in Train Set")
ax[0].set_xlabel("Emotion")
ax[0].set_ylabel("Number of Images")


# plot remaining images histogram
ax[1].bar(
    emotions,
    remaining,
    color=["red", "green", "blue", "orange", "purple", "gray", "pink"],
)
ax[1].set_title("Processed Images in Test Set")
ax[1].set_xlabel("Emotion")
ax[1].set_ylabel("Number of Images")

# display plot
plt.show()
