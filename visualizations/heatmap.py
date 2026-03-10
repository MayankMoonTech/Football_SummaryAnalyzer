import seaborn as sns
import matplotlib.pyplot as plt

def player_heatmap(df):

    sns.kdeplot(x=df["x"],y=df["y"],shade=True)

    plt.title("Player Heatmap")

    plt.xlim(0,100)
    plt.ylim(0,100)

    plt.show()