import numpy
import matplotlib.pyplot as plt
import pandas as pd

def Graph(x, y):
    df=pd.DataFrame({"x": x, "y": y})

    plt.plot('x', 'y', data=df, linestyle='none', marker='o')
    plt.show()
