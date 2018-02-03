import pandas as pd
import os
import random
from PIL import Image
import matplotlib.pyplot as plt


# df_labels = read_file('/Users/jordancarson/PyCharmProjects/AmazonKaggle-MLCapstone/resources', 'train_v2.csv', 'csv')

def plot_pictures(label, df_train, TRAIN_PATH):

    images = df_train[df_train[label] == 1].image_name.values

    fig , ax = plt.subplots(nrows=3, ncols=3, figsize=(8,8))
    ax = ax.flatten()

    for i in range(0,9):
        f = random.choice(images)
        img = Image.open(os.path.join(TRAIN_PATH, f + '.jpg'))
        ax[i].imshow(img)
        ax[i].set_xticks([])
        ax[i].set_yticks([])
        ax[i].set_title("{}s h:{}s w:{}s".format(f, img.height, img.width))
    plt.tight_layout()
