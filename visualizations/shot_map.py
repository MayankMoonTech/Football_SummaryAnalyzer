import matplotlib.pyplot as plt

def plot_shots(df):

    shots = df[df["event_type"]=="shot"]

    plt.scatter(shots["x"],shots["y"],c="red")

    plt.title("Shot Map")

    plt.xlim(0,100)
    plt.ylim(0,100)

    plt.show()