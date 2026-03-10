import networkx as nx
import matplotlib.pyplot as plt

def plot_pass_network(df):

    passes = df[df["event_type"]=="pass"]

    G = nx.Graph()

    players = passes["player"].unique()

    for p in players:
        G.add_node(p)

    for i in range(len(players)-1):
        G.add_edge(players[i], players[i+1])

    nx.draw(G, with_labels=True)

    plt.title("Pass Network")
    plt.show()