import numpy
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.gridspec import GridSpec
from src.imagelist import IMAGELIST

def Graph(x, y, filepath, ratings):
    global IMAGELIST
    def getImage(path):
        return OffsetImage(plt.imread(path))

    fig, ax = plt.subplots()
    fig.set_size_inches((len(set(x))) + 3, (sorted(y)[-1] // 2) + 3)
    ax.set_facecolor("tab:gray")

    ax.scatter(x, y)

    plt.xlabel("Season #")
    plt.ylabel("Episode #")

    for x0, y0 in zip(x, y):
        ab = AnnotationBbox(getImage(IMAGELIST[ratings[y0]]), (x0, y0), frameon=False)
        ax.add_artist(ab)

    plt.savefig(filepath)
