import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

def main(labels, x, _iter_labels, _diff_time):
    width = 0.12
    j = 0
    rect = [0, 0, 0, 0, 0, 0, 0]
    plt.rcdefaults()
    fig, ax = plt.subplots()

    for i in _diff_time:
        rect[j] = ax.barh(x - width*j, i, width, label= _iter_labels[j], align='center')
        ax.bar_label(rect[j], padding = 3, fontsize=5)
        #ax.text(rect[j])
        j += 1
    ax.set_xlim(right=15)
    ax.set_yticks(x)
    ax.set_yticklabels(labels)
    ax.invert_yaxis()
    ax.set_ylabel('Algorithms')
    ax.set_xlabel('Time (s)')
    ax.set_title("Perfomance Comparision")

    ax.legend()

    fig.tight_layout()
    plt.savefig("output-16.jpg")


if __name__ == "__main__":

    _file_path = "/mnt/c/Users/khush/Documents/Quansight-Intern/pierre/pierre-2/data16.csv"
    
    df = pd.read_csv(_file_path)

    labels = []
    for i in range(1, len(df.columns)):
        labels.append(df.columns[i])

    df.drop('Unnamed: 0', axis='columns', inplace=True)
    _diff_time = df.to_numpy().tolist()
    _diff_time

    x = np.arange(len(labels))
    _iter_labels = [1, 2, 3, 5, 10, 20, 50]
    
    main(labels, x, _iter_labels, _diff_time)

