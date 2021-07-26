import matplotlib.pyplot as plt
import pandas as pd


def main(labels, x, _color, _diff_time):

    fig, ax = plt.subplots()

    for i in range(len(_diff_time)):
        plt.plot(x, _diff_time[i],
            linewidth=0.5,
            linestyle='--',
            color=_color[i],
            marker='o',
            markersize=10,
            markerfacecolor=(1, 0, 0, 0.1),
            label = labels[i])
        
        for j, txt in enumerate(_diff_time[i]):
            ax.annotate(txt, (x[j], _diff_time[i][j]))

    plt.title('Performance Comparision')
    plt.xlabel('Algorithms')
    plt.ylabel('Time (s)')

    plt.grid(True)
    plt.legend()

    fig.tight_layout()
    plt.savefig("output___16.jpg")


if __name__ == "__main__":

    _file_path = "data-16.csv"
    df = pd.read_csv(_file_path)

    x = []
    for i in range(1, len(df.columns)):
        x.append(df.columns[i])

    _labels = ["Iter 1", "Iter 5", "Iter 10", "Iter 20", "Iter 50", "Iter 100", "Iter 200"]
    _color = ['b', 'g', 'c', 'm', 'r', 'k', 'y']
    df.drop('Unnamed: 0', axis='columns', inplace=True)

    _diff_time = df.to_numpy().tolist()

    main(_labels, x, _color, _diff_time)

