import numpy
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.gridspec import GridSpec
from src.imagelist import IMAGELIST

def Graph(x, y, filepath, ratings, coords, moviename):
    global IMAGELIST
    def getImage(path):
        return OffsetImage(plt.imread(path))

    ax = plt.subplots()[1]
    ax.set_facecolor("tab:gray")

    figure = plt.gcf()

    figure.set_size_inches((len(set(x))) + 3, (sorted(y)[-1] // 2) + 3)

    df = pd.DataFrame({'x': x,'y': y})

    plt.xlabel("Season #")
    plt.ylabel("Episode #")
    plt.title(moviename)

    ax.set_xticks(x)
    ax.set_yticks(y)

    plt.plot('x', 'y', data=df, linestyle='none', marker='s',markersize=10, color="green")

    for place, rating in zip(coords, ratings):
        ab = AnnotationBbox(getImage(IMAGELIST[rating]), place, frameon=False)
        ax.add_artist(ab)

    plt.subplots_adjust(left=0.05, right=0.98, top=0.96, bottom=0.05)
    plt.margins(x=0.05)
    plt.margins(y=0.05)

    plt.show()
    #plt.savefig(filepath)
