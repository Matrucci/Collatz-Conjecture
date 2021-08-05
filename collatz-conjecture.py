import networkx as nx
from matplotlib import pyplot as plt

def main():
    G = nx.Graph()

    x = input("Enter a number\n")
    i = int(x)
    j = 0
    temp = i
    while (i != 1):
        i = int(i)
        G.add_node(i, pos=(j, i))
        if temp != i:
            G.add_edge(temp, i)
        temp = i
        if (i % 2 == 0):
            i = i / 2
        else:
            i = 3*i + 1
        j = j + 1

    G.add_node(1, pos=(j, 1))
    G.add_edge(temp, 1)

    pos=nx.get_node_attributes(G,'pos')
    nx.draw(G, pos, with_labels=True)

    plt.show()


if __name__ == "__main__":
    main()