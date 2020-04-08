import numpy
import matplotlib.pyplot as plt
import pandas as pd

def Graph(x, y, filepath):
    df=pd.DataFrame({"x": x, "y": y})

    plt.plot('x', 'y', data=df, linestyle='none', marker='o')
    plt.savefig(filepath)
